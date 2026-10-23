"""Generate cached 1200x630 OGP cards from converted problem Markdown."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import html
import json
import os
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'web/src/content/solutions'
OUTPUT = ROOT / 'web/public/ogp/problems'
FIGURES = ROOT / 'web/public/images/tikz'
VERSION = '7'


@dataclass
class Stats:
    generated: int = 0
    skipped: int = 0
    fallback: int = 0
    failed: int = 0


def extract_excerpt(markdown: str, max_chars: int = 210) -> str:
    body = re.sub(r'\A---\s*\n.*?\n---\s*\n', '', markdown, flags=re.S)
    body = re.sub(r'<figure\b.*?</figure>', ' ', body, flags=re.S | re.I)
    body = re.sub(r'</?[A-Za-z][A-Za-z0-9-]*(?:\s[^>]*)?/?>', ' ', body)
    def simplify_display_math(match: re.Match) -> str:
        formula = re.sub(r'\s+', ' ', match.group(1)).strip()
        return f' ${formula}$ ' if len(formula) < 70 and r'\begin' not in formula else '（数式）'
    body = re.sub(r'\$\$(.*?)\$\$', simplify_display_math, body, flags=re.S)
    body = re.sub(r'(?m)^\s*(?:[-*+]\s+|\d+[.)]\s+)', '', body)
    body = html.unescape(re.sub(r'\s+', ' ', body)).strip()
    if len(body) <= max_chars:
        return body
    # Cut only outside inline math and prefer a complete sentence.
    outside_math = True
    boundaries = []
    last_safe = 0
    for i, char in enumerate(body[:max_chars]):
        if char == '$' and (i == 0 or body[i - 1] != '\\'):
            outside_math = not outside_math
        elif outside_math and char in '．。！？':
            boundaries.append(i + 1)
        if outside_math:
            last_safe = i + 1
    end = boundaries[-1] if boundaries else 0
    if end < min(24, max_chars // 3):
        # A very long first sentence: use the last whitespace outside math.
        outside_math = True
        for i, char in enumerate(body[:max_chars]):
            if char == '$' and (i == 0 or body[i - 1] != '\\'):
                outside_math = not outside_math
            elif outside_math and char.isspace():
                end = i
    return (body[:end or last_safe].rstrip() if end or last_safe else '') + '…'


def _label(stem: str) -> str:
    parts = stem.split('-')
    if len(parts) < 4:
        return '大学入試数学'
    university = {'utokyo': '東京大学', 'ukyoto': '京都大学', 'titech': '東京工業大学'}.get(parts[0], parts[0])
    category = {'zenki': '前期', 'kouki': '後期'}.get(parts[1], parts[1])
    return f'{university} / {category} / {parts[2]}年 / 第{parts[3]}問'


TEMPLATE = r"""\documentclass[border=0pt]{standalone}
\usepackage{luatexja}
\usepackage[haranoaji]{luatexja-preset}
\usepackage{amsmath,amssymb,bm,physics,pifont,graphicx,tikz}
\definecolor{navy}{HTML}{0B1326}
\definecolor{panel}{HTML}{14213A}
\definecolor{muted}{HTML}{ADC0DC}
\definecolor{accent}{HTML}{73D9B5}
\newsavebox{\ogptext}
\begin{document}
\sbox{\ogptext}{\begin{minipage}[t]{__WIDTH__pt}\color{white}\raggedright\fontsize{__SIZE__}{__LEADING__}\selectfont __EXCERPT__\end{minipage}}
\typeout{OGP-TEXT-HEIGHT=\the\ht\ogptext}
\begin{tikzpicture}[x=1pt,y=1pt]
  \path[use as bounding box] (0,0) rectangle (1200,630);
  \fill[navy] (0,0) rectangle (1200,630);
  \fill[panel,rounded corners=24pt] (56,56) rectangle (1144,574);
  \fill[accent] (56,56) rectangle (69,574);
  \node[anchor=west,text=accent,font=\sffamily\bfseries\fontsize{21}{25}\selectfont] at (96,530) {MATH SOLUTIONS};
  \node[anchor=west,text=white,font=\sffamily\bfseries\fontsize{31}{38}\selectfont] at (96,475) {__LABEL__};
  \draw[muted,opacity=.55] (96,439) -- (1104,439);
  \node[anchor=north west,text=muted,font=\sffamily\fontsize{17}{24}\selectfont] at (96,420) {問題文より（抜粋）};
  __FIGURE__
  \node[anchor=north west,inner sep=0pt,text=white] at (96,375) {\usebox{\ogptext}};
  \node[anchor=west,text=muted,font=\sffamily\fontsize{17}{22}\selectfont] at (96,89) {大学入試数学 過去問解答アーカイブ};
\end{tikzpicture}
\end{document}
"""


def _tex_text(value: str) -> str:
    # Converted Markdown intentionally contains TeX commands such as \quad.
    # Keep them intact while escaping plain-text special characters.
    pieces = re.split(r'(\$[^$]*\$)', value)
    for i in range(0, len(pieces), 2):
        prose = pieces[i]
        prose = re.sub(r'(?<!\\)([&%#_])', lambda match: '\\' + match.group(1), prose)
        pieces[i] = prose
    return ''.join(pieces)


def _figure_path(stem: str) -> Path | None:
    parts = stem.split('-')
    if len(parts) < 4:
        return None
    candidates = sorted((FIGURES / parts[0] / parts[1] / parts[2] / parts[3]).glob('fig_problem_*.svg'))
    return candidates[0] if candidates else None


def render_card(markdown: str, destination: Path, figure: Path | None = None) -> str:
    """Render one card. Returns 'fallback' if the excerpt could not fit/render."""
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    stem = destination.stem
    with tempfile.TemporaryDirectory(prefix='problem-ogp-') as tmp:
        work = Path(tmp)
        figure_code = ''
        if figure and figure.exists():
            figure_png = work / 'figure.png'
            converted = subprocess.run(['rsvg-convert', '-w', '330', '-h', '325', '-o', str(figure_png), str(figure)], capture_output=True)
            if converted.returncode:
                raise RuntimeError(f'Could not rasterize problem figure: {figure}')
            figure_code = (r'\fill[white,rounded corners=14pt] (766,172) rectangle (1110,394);' + '\n'
                           + rf'\node at (938,283) {{\includegraphics[width=320pt,height=207pt,keepaspectratio]{{{figure_png}}}}};')
        for limit, size in [(200, 30), (140, 28), (95, 27), (60, 26), (0, 28)]:
            excerpt = extract_excerpt(markdown, limit) if limit else '問題文と解答はリンク先でご覧ください．'
            if excerpt == '…' or not excerpt.strip():
                excerpt = '問題文と解答はリンク先でご覧ください．'
                limit = 0
            width = 640 if figure_code else 1000
            tex = TEMPLATE
            for key, value in {'__LABEL__': _label(stem), '__WIDTH__': str(width), '__SIZE__': str(size),
                               '__LEADING__': str(round(size * 1.5)), '__EXCERPT__': _tex_text(excerpt),
                               '__FIGURE__': figure_code}.items():
                tex = tex.replace(key, value)
            (work / 'card.tex').write_text(tex, encoding='utf-8')
            result = subprocess.run(['lualatex', '-halt-on-error', '-interaction=nonstopmode',
                                     '-output-directory', str(work), str(work / 'card.tex')],
                                    cwd=work, capture_output=True, text=True)
            if result.returncode:
                continue
            match = re.search(r'OGP-TEXT-HEIGHT=([\d.]+)pt', result.stdout)
            if not match or float(match.group(1)) > 255:
                continue
            if any(float(width) > 20 for width in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\)', result.stdout)):
                continue
            raster = work / 'card.png'
            subprocess.run(['pdftocairo', '-f', '1', '-l', '1', '-singlefile', '-png',
                            '-scale-to-x', '1200', '-scale-to-y', '630', str(work / 'card.pdf'),
                            str(raster.with_suffix(''))], check=True, capture_output=True)
            with Image.open(raster) as image:
                image.resize((1200, 630), Image.Resampling.LANCZOS).save(destination, 'PNG', optimize=True)
            return 'fallback' if limit == 0 else 'excerpt'
    raise RuntimeError(f'Could not render OGP card for {stem}')


def generate_cards(paths: list[Path], output: Path, workers: int = 1, prune: bool = False) -> Stats:
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / 'manifest.json'
    try:
        manifest = json.loads(manifest_path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        manifest = {}
    stats = Stats()
    pending = []
    for md in paths:
        stem = md.stem.removesuffix('-problem')
        card = output / f'{stem}.png'
        figure = _figure_path(stem)
        markdown = md.read_text(encoding='utf-8')
        digest = hashlib.sha256(VERSION.encode() + markdown.encode() + (figure.read_bytes() if figure else b'')).hexdigest()
        if manifest.get(stem) == digest and card.is_file():
            stats.skipped += 1
            continue
        pending.append((stem, card, markdown, figure, digest))

    if prune:
        expected = {md.stem.removesuffix('-problem') for md in paths}
        for stale in output.glob('*.png'):
            if stale.stem not in expected:
                stale.unlink()
        manifest = {stem: digest for stem, digest in manifest.items() if stem in expected}

    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = {pool.submit(render_card, markdown, card, figure): (stem, card, digest)
                   for stem, card, markdown, figure, digest in pending}
        for future in as_completed(futures):
            stem, card, digest = futures[future]
            try:
                mode = future.result()
            except Exception as exc:
                stats.failed += 1
                card.unlink(missing_ok=True)
                manifest.pop(stem, None)
                print(f'OGP failed {stem}: {exc}', flush=True)
                continue
            manifest[stem] = digest
            stats.generated += 1
            stats.fallback += mode == 'fallback'
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=CONTENT)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    parser.add_argument('--limit', type=int)
    parser.add_argument('--workers', type=int, default=min(4, os.cpu_count() or 1))
    args = parser.parse_args()
    paths = sorted(args.source.glob('*-problem.md'))
    if args.limit is not None:
        paths = paths[:args.limit]
    stats = generate_cards(paths, args.output, workers=args.workers, prune=args.limit is None)
    print(f'OGP cards: total={len(paths)} generated={stats.generated} cached={stats.skipped} fallback={stats.fallback} failed={stats.failed}')


if __name__ == '__main__':
    main()
