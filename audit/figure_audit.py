#!/usr/bin/env python3
"""Find likely label collisions in rendered TikZ figures; never edit source TeX."""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from xml.etree import ElementTree


TIKZ_START = re.compile(r'\\begin\s*\{tikzpicture\}(?:\[[^\]]*\])?')
TIKZ_END = re.compile(r'\\end\s*\{tikzpicture\}')
DEFAULT_PROXIMITY_PT = 6.0
PREAMBLE = r'''\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{etoolbox}
\usepackage{luatexja}
\usepackage[haranoaji]{luatexja-preset}
\usepackage{tikz,pgfplots,tikz-3dplot}
\usetikzlibrary{arrows.meta,calc,intersections,patterns,patterns.meta,angles,quotes,through,positioning,decorations.pathmorphing,decorations.markings,math,3d,perspective,shapes.geometric,backgrounds}
\usepgfplotslibrary{fillbetween,colormaps,groupplots}
\pgfplotsset{compat=1.18}
\tdplotsetmaincoords{70}{110}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\providecommand{\roundedArrowDR}{\searrow}
\newwrite\auditbounds
\newcount\auditnodecount
\newif\ifauditpatchok
\makeatletter
\patchcmd{\tikz@node@finish}{\tikz@do@after@node}%
  {\global\advance\auditnodecount by1\relax\tikz@do@after@node}%
  {\auditpatchoktrue}{}
\makeatother
\begin{document}
\immediate\openout\auditbounds=figure.bounds
'''
NODE_HOOK = r'''\tikzset{every node/.append style={append after command={\pgfextra{%
\pgfextractx{\dimen0}{\pgfpointanchor{\tikzlastnode}{south west}}%
\pgfextracty{\dimen2}{\pgfpointanchor{\tikzlastnode}{south west}}%
\pgfextractx{\dimen4}{\pgfpointanchor{\tikzlastnode}{north east}}%
\pgfextracty{\dimen6}{\pgfpointanchor{\tikzlastnode}{north east}}%
\immediate\write\auditbounds{AUDIT-NODE|\tikzlastnode|\the\dimen0|\the\dimen2|\the\dimen4|\the\dimen6}%
}}}}'''
NODE_PATTERN = re.compile(r'AUDIT-NODE\|([^|\n]+)\|([-\d.]+)pt\|([-\d.]+)pt\|'
                          r'([-\d.]+)pt\|([-\d.]+)pt')
PICTURE_HOOK = (r'\makeatletter\immediate\write\auditbounds{AUDIT-PICTURE|\the\pgf@picminx|'
                r'\the\pgf@picminy|\the\pgf@picmaxx|\the\pgf@picmaxy}'
                r'\immediate\write\auditbounds{AUDIT-TOTAL|\the\auditnodecount}'
                r'\ifauditpatchok\else\immediate\write\auditbounds{AUDIT-PATCH-FAILED}\fi'
                r'\makeatother')
PICTURE_PATTERN = re.compile(r'AUDIT-PICTURE\|([-\d.]+)pt\|([-\d.]+)pt\|'
                             r'([-\d.]+)pt\|([-\d.]+)pt')
TEX_PT_TO_PDF_PT = 72 / 72.27


def extract_tikz(source):
    """Return non-nested TikZ pictures, with original starting line numbers."""
    visible = re.sub(r'(?m)(?<!\\)((?:\\\\)*)%[^\n]*',
                     lambda m: m[1] + ' ' * (len(m[0]) - len(m[1])), source)
    out = []
    position = 0
    while match := TIKZ_START.search(visible, position):
        end = TIKZ_END.search(visible, match.end())
        if not end:
            break
        out.append({'line': visible.count('\n', 0, match.start()) + 1,
                    'tex': source[match.start():end.end()]})
        position = end.end()
    return out


def parse_stext(xml):
    """Use MuPDF text blocks as initial labels; preserve multi-line math blocks."""
    root = ElementTree.fromstring(xml)
    labels = []
    for page_number, page in enumerate(root.findall('page'), 1):
        for block in page.findall('block'):
            lines = [line.get('text', '').strip() for line in block.findall('line')]
            text = ' / '.join(line for line in lines if line)
            if not text:
                continue
            try:
                bbox = [float(value) for value in block.attrib['bbox'].split()]
            except (KeyError, ValueError):
                continue
            if len(bbox) != 4 or not all(math.isfinite(x) for x in bbox):
                continue
            labels.append({'page': page_number, 'text': text, 'bbox': bbox})
    return labels


def parse_node_log(log):
    """Read TikZ node bounds from an instrumented standalone build."""
    nodes = []
    for match in NODE_PATTERN.finditer(log):
        bbox = [float(match.group(i)) for i in range(2, 6)]
        if bbox[2] - bbox[0] < 4 and bbox[3] - bbox[1] < 4:
            continue  # Point marks and empty coordinates are not text labels.
        if bbox[0] >= bbox[2] or bbox[1] >= bbox[3]:
            continue
        nodes.append({'page': 1, 'text': match.group(1), 'bbox': bbox})
    return nodes


def candidate_crop(pair, picture, page_size, dpi=200, pad_pt=8):
    """Map a TikZ node pair to a Poppler pixel crop (x, y, width, height)."""
    min_x, min_y, max_x, max_y = picture
    page_w, page_h = page_size
    scale = TEX_PT_TO_PDF_PT
    offset_x = (page_w - (max_x - min_x) * scale) / 2
    offset_y = (page_h - (max_y - min_y) * scale) / 2
    boxes = [pair['bbox_a'], pair['bbox_b']]
    left = min(b[0] for b in boxes)
    right = max(b[2] for b in boxes)
    bottom = min(b[1] for b in boxes)
    top = max(b[3] for b in boxes)
    factor = dpi / 72
    x1 = max(0, math.floor(((left - min_x) * scale + offset_x - pad_pt) * factor))
    y1 = max(0, math.floor(((max_y - top) * scale + offset_y - pad_pt) * factor))
    x2 = min(math.ceil(page_w * factor),
             math.ceil(((right - min_x) * scale + offset_x + pad_pt) * factor))
    y2 = min(math.ceil(page_h * factor),
             math.ceil(((max_y - bottom) * scale + offset_y + pad_pt) * factor))
    if x2 <= x1 or y2 <= y1:
        raise ValueError('candidate crop lies outside PDF page')
    return x1, y1, x2 - x1, y2 - y1


def candidate_crop_pdf(pair, page_size, dpi=200, pad_pt=8):
    """Crop MuPDF text boxes, whose coordinates already use a top-left origin."""
    page_w, page_h = page_size
    boxes = [pair['bbox_a'], pair['bbox_b']]
    factor = dpi / 72
    x1 = max(0, math.floor((min(b[0] for b in boxes) - pad_pt) * factor))
    y1 = max(0, math.floor((min(b[1] for b in boxes) - pad_pt) * factor))
    x2 = min(math.ceil(page_w * factor),
             math.ceil((max(b[2] for b in boxes) + pad_pt) * factor))
    y2 = min(math.ceil(page_h * factor),
             math.ceil((max(b[3] for b in boxes) + pad_pt) * factor))
    if x2 <= x1 or y2 <= y1:
        raise ValueError('candidate crop lies outside PDF page')
    return x1, y1, x2 - x1, y2 - y1


def find_collisions(labels, proximity_pt):
    """Return each intersecting or nearby pair on the same page."""
    found = []
    for i, a in enumerate(labels):
        for b in labels[i + 1:]:
            if a['page'] != b['page']:
                continue
            x1, y1, x2, y2 = a['bbox']
            u1, v1, u2, v2 = b['bbox']
            dx = max(0.0, x1 - u2, u1 - x2)
            dy = max(0.0, y1 - v2, v1 - y2)
            distance = math.hypot(dx, dy)
            if distance > proximity_pt:
                continue
            area = max(0.0, min(x2, u2) - max(x1, u1)) * max(0.0, min(y2, v2) - max(y1, v1))
            found.append({'page': a['page'], 'a': a['text'], 'b': b['text'],
                          'bbox_a': a['bbox'], 'bbox_b': b['bbox'],
                          'distance_pt': round(distance, 3), 'overlap_pt2': round(area, 3)})
    return found


def _run(args, cwd, env=None, timeout=90):
    proc = subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True,
                          timeout=timeout)
    if proc.returncode:
        raise RuntimeError(f'{args[0]} failed ({proc.returncode}): {(proc.stderr or proc.stdout)[-500:]}')
    return proc.stdout


def audit_figure(figure, index, output, work, proximity_pt, cache):
    record = {'figure_index': index, 'source_line': figure['line'],
              'status': 'unavailable', 'reason': None, 'candidates': []}
    folder = work / f'figure-{index}'
    folder.mkdir()
    tex_path = folder / 'figure.tex'
    instrumented = re.sub(r'(\\begin\s*\{tikzpicture\}(?:\[[^\]]*\])?)',
                          lambda match: match.group(1) + '\n' + NODE_HOOK + '\n',
                          figure['tex'], count=1)
    instrumented = instrumented.replace(r'\end{tikzpicture}',
                                        PICTURE_HOOK + '\n' + r'\end{tikzpicture}', 1)
    tex_path.write_text(PREAMBLE + instrumented + '\n\\end{document}\n', encoding='utf-8')
    env = dict(os.environ, TEXMFVAR=str(cache), TEXMFCACHE=str(cache))
    try:
        _run(['lualatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
              'figure.tex'], folder, env=env)
        pdf = folder / 'figure.pdf'
        if not pdf.is_file():
            raise RuntimeError('lualatex did not create a PDF')
        bounds_file = folder / 'figure.bounds'
        bounds = bounds_file.read_text(encoding='utf-8') if bounds_file.is_file() else ''
        labels = parse_node_log(bounds)
        record['node_bounds_extracted'] = len(labels)
        total_match = re.search(r'AUDIT-TOTAL\|(\d+)', bounds)
        total_nodes = int(total_match.group(1)) if total_match else None
        raw_bounds_count = bounds.count('AUDIT-NODE|')
        record['nodes_seen'] = total_nodes
        record['missing_node_bounds'] = (max(0, total_nodes - raw_bounds_count)
                                         if total_nodes is not None else None)
        if not labels:
            xml = _run(['mutool', 'draw', '-F', 'stext', str(pdf)], folder)
            labels = parse_stext(xml)
            record['extraction_method'] = 'pdf-text-blocks'
            record['limitation'] = 'PDF text blocks may merge separate TikZ labels'
        else:
            record['extraction_method'] = 'tikz-node-bounds'
        if not labels:
            raise RuntimeError('no extractable node bounds or text in rendered figure')
        record['label_boxes'] = labels
        record['candidates'] = find_collisions(labels, proximity_pt)
        record['labels_extracted'] = len(labels)
        complete_nodes = (record['extraction_method'] == 'tikz-node-bounds'
                          and total_nodes is not None
                          and 'AUDIT-PATCH-FAILED' not in bounds
                          and total_nodes == raw_bounds_count)
        record['status'] = 'ready' if complete_nodes else 'partial'
        if not complete_nodes:
            record['limitation'] = 'Some TikZ nodes may be missing from candidate detection'
        prefix = output / f'figure-{index}'
        _run(['pdftoppm', '-f', '1', '-l', '1', '-singlefile', '-r', '200',
              '-png', str(pdf), str(prefix)], folder)
        record['image'] = prefix.with_suffix('.png').name
        picture_match = PICTURE_PATTERN.search(bounds)
        if record['candidates'] and (picture_match or record['extraction_method'] == 'pdf-text-blocks'):
            picture = ([float(picture_match.group(i)) for i in range(1, 5)]
                       if picture_match else None)
            info = _run(['pdfinfo', str(pdf)], folder)
            size_match = re.search(r'^Page size:\s*([\d.]+) x ([\d.]+) pts', info, re.M)
            if size_match:
                page_size = tuple(float(size_match.group(i)) for i in (1, 2))
                for n, pair in enumerate(record['candidates'], 1):
                    try:
                        if record['extraction_method'] == 'pdf-text-blocks':
                            x, y, width, height = candidate_crop_pdf(pair, page_size)
                        else:
                            x, y, width, height = candidate_crop(pair, picture, page_size)
                        crop = output / f'candidate-{index}-{n}'
                        _run(['pdftoppm', '-f', '1', '-l', '1', '-singlefile', '-r', '200',
                              '-x', str(x), '-y', str(y), '-W', str(width), '-H', str(height),
                              '-png', str(pdf), str(crop)], folder)
                        pair['image'] = crop.with_suffix('.png').name
                    except (OSError, RuntimeError, ValueError) as error:
                        pair['image_error'] = str(error)
            else:
                record['crop_warning'] = 'cannot read PDF page size'
        elif record['candidates']:
            record['crop_warning'] = 'cannot read TikZ picture bounds'
    except (OSError, RuntimeError, subprocess.TimeoutExpired, ElementTree.ParseError) as error:
        record['status'] = 'unavailable'
        record['reason'] = str(error)
        record['candidates'] = []
    return record


def audit(tex_path, output, proximity_pt=DEFAULT_PROXIMITY_PT):
    if not tex_path.is_file():
        raise ValueError(f'TeX file not found: {tex_path}')
    if output.exists() and any(output.iterdir()):
        raise ValueError('output directory must be new or empty')
    if proximity_pt < 0 or not math.isfinite(proximity_pt):
        raise ValueError('--proximity-pt must be a finite nonnegative number')
    for name in ('lualatex', 'mutool', 'pdftoppm', 'pdfinfo'):
        if not shutil.which(name):
            raise ValueError(f'required executable not found: {name}')
    source = tex_path.read_text(encoding='utf-8')
    figures = extract_tikz(source)
    if not figures:
        raise ValueError('no tikzpicture found')
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='tikz-figure-audit-') as tmp:
        work = Path(tmp)
        cache = work / 'cache'
        cache.mkdir()
        records = [audit_figure(fig, i, output, work, proximity_pt, cache)
                   for i, fig in enumerate(figures, 1)]
    report = {'source': str(tex_path.resolve()),
              'source_sha256': hashlib.sha256(tex_path.read_bytes()).hexdigest(),
              'proximity_pt': proximity_pt, 'status': 'candidates-only',
              'figures': records}
    (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                                        encoding='utf-8')
    lines = ['# TikZ label collision candidates', '',
             '候補ゼロは監査合格を意味しない。PDF 全ページと Web 用 SVG を目視する。', '']
    for fig in records:
        lines.append(f"## 図{fig['figure_index']}（TeX L{fig['source_line']}）")
        lines.append('')
        if fig['status'] == 'unavailable':
            lines.append(f"抽出不可: {fig['reason']}")
        else:
            lines.append(f"![図{fig['figure_index']}]({fig['image']})")
            lines.append('')
            lines.append(f"候補 {len(fig['candidates'])} 件。")
            if fig['status'] == 'partial':
                if fig['extraction_method'] == 'pdf-text-blocks':
                    lines.append('PDF文字抽出のみ。別々のラベルが結合されるため見落としの可能性あり。')
                else:
                    lines.append('ノード領域の記録が不足。候補ゼロでも見落としの可能性あり。')
            for item in fig['candidates']:
                lines.append(f"- `{item['a']}` と `{item['b']}`: "
                             f"距離 {item['distance_pt']} pt、交差面積 {item['overlap_pt2']} pt²")
                if item.get('image'):
                    lines.append(f"  ![候補の拡大]({item['image']})")
        lines.append('')
    (output / 'report.md').write_text('\n'.join(lines), encoding='utf-8')
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tex', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--proximity-pt', type=float, default=DEFAULT_PROXIMITY_PT)
    args = parser.parse_args(argv)
    try:
        report = audit(args.tex, args.output, args.proximity_pt)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"{len(report['figures'])} figures; "
          f"{sum(len(fig['candidates']) for fig in report['figures'])} candidates; "
          f"{sum(fig['status'] == 'partial' for fig in report['figures'])} partial; "
          f"{sum(fig['status'] == 'unavailable' for fig in report['figures'])} unavailable")


if __name__ == '__main__':
    main()
