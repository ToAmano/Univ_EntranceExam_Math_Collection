"""Web 版で TeX のコマンドがそのまま表示される箇所（漏れ）を探す（#1489）。

使い方:
    python3 scratch/check_web_leaks.py [--warn] [FILE.tex ...]

FILE を省くと src/ の全ての problem.tex・solution.tex を調べる。各ファイルを
tex_to_md.py で Web 用 Markdown に変換し、web/scripts/find-tex-leaks.mjs で
サイトと同じ Markdown 処理にかけて、数式の外に表示される TeX のコマンドを探す。
TikZ の図は SVG にコンパイルせず空の画像で置き換えるので、TeX Live は要らない
（pandoc・Node.js と web/ の npm パッケージは要る）。

漏れが見つかると終了コード 1 を返す。KNOWN に挙げたファイル（対応する Issue が
あるもの）と lint-skip の旧形式の原稿は警告にとどめる。--warn を付けると常に 0 を返す。
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from unittest.mock import patch

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

NODE_SCRIPT = REPO / 'web' / 'scripts' / 'find-tex-leaks.mjs'
LINT_SKIP_RE = re.compile(r'%\s*lint-skip\s*:')

# 対応する Issue があり、修正待ちの漏れ。直したらここから外す。
_SUMMARY_TABLES = [f'src/titech/kouki/{y}/0/solution.tex'
                   for y in (1993, 1994, 1998, 1999, 2000, 2001, 2005, 2006, 2010, 2011)]
KNOWN = {
    **{path: '#1496 年度一覧の表の中の数式' for path in _SUMMARY_TABLES},
    'src/utokyo/zenki/1991/3/solution.tex': '#1496 増減表のセル内の複数行の数式',
    'src/utokyo/zenki/1977/6/solution.tex': '#1497 増減表の凹凸の矢印',
    'src/utokyo/zenki/2005/3/solution.tex': '#1497 増減表の凹凸の矢印',
    'src/titech/zenki/1981/2/solution.tex': '#1497 増減表の凹凸の矢印',
    'src/utokyo/zenki/1976/2/solution.tex': '旧形式（zahyou 等）の原稿。#1489 の対象外',
    'src/utokyo/kouki/1994/1/problem.tex': '#1500 \\item の直後の別行立て数式が変換で崩れる',
}


def page_type(path):
    parts = Path(path).parts
    if parts[-1] == 'problem.tex':
        return 'problem'
    return 'summary' if parts[-2] == '0' else 'solution'


def _fake_compile(code, output_svg_path, macro_defs='', **options):
    Path(output_svg_path).write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding='utf-8')
    return True


def convert(args):
    """1ファイルを Markdown に変換して、その出力先を返す（失敗したらエラー文）。"""
    tex_path, out_dir = args
    from scratch import tex_to_md
    md_path = os.path.join(out_dir, tex_path.replace('/', '__') + '.md')
    try:
        with patch.object(tex_to_md, 'compile_tikz_to_svg', _fake_compile), \
                open(os.devnull, 'w') as devnull, patch('sys.stdout', devnull):
            tex_to_md.convert_tex_clean(str(REPO / tex_path), md_path, {'type': page_type(tex_path)},
                                        '/images/check', os.path.join(out_dir, 'img'))
        return md_path, None
    except Exception as exc:  # 変換できないものも報告する
        return None, f'{type(exc).__name__}: {exc}'


def find_leaks(tex_paths, jobs=8):
    """{tex_path: [ {command, context}, ... ]} と、変換に失敗したファイルを返す。"""
    with tempfile.TemporaryDirectory(prefix='web_leaks_') as out_dir:
        tasks = [(p, out_dir) for p in tex_paths]
        if len(tasks) > 1:
            with ProcessPoolExecutor(jobs) as pool:
                results = list(pool.map(convert, tasks, chunksize=8))
        else:
            results = [convert(t) for t in tasks]
        failures = {p: err for p, (_, err) in zip(tex_paths, results) if err}
        md_to_tex = {md: p for p, (md, _) in zip(tex_paths, results) if md}
        leaks = {}
        if md_to_tex:
            proc = subprocess.run(['node', str(NODE_SCRIPT), *md_to_tex], capture_output=True,
                                  text=True, cwd=REPO)
            if proc.returncode != 0:
                raise RuntimeError(f'find-tex-leaks.mjs が失敗した:\n{proc.stderr}')
            for line in proc.stdout.splitlines():
                item = json.loads(line)
                leaks.setdefault(md_to_tex[item['file']], []).append(item)
    return leaks, failures


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('files', nargs='*', help='調べる problem.tex・solution.tex（省くと全て）')
    parser.add_argument('--warn', action='store_true', help='漏れがあっても終了コード 0 を返す')
    args = parser.parse_args(argv)

    os.chdir(REPO)
    files = args.files or sorted(glob.glob('src/*/*/*/*/problem.tex') + glob.glob('src/*/*/*/*/solution.tex'))
    files = [os.path.relpath(os.path.abspath(f), REPO) for f in files
             if f.endswith(('problem.tex', 'solution.tex')) and os.path.exists(f)]
    if not files:
        print('調べる problem.tex・solution.tex がない。')
        return 0

    leaks, failures = find_leaks(files)
    annotate = os.environ.get('GITHUB_ACTIONS') == 'true'
    errors = warnings = 0
    for path in files:
        items = leaks.get(path, [])
        if not items:
            continue
        legacy = LINT_SKIP_RE.search(Path(path).read_text(encoding='utf-8'))
        reason = KNOWN.get(path) or ('lint-skip の旧形式の原稿' if legacy else None)
        commands = ', '.join(sorted({i['command'] for i in items}))
        message = f'Web で TeX のまま表示される（{len(items)} 件: {commands}）。例: …{items[0]["context"]}…'
        if reason:
            warnings += 1
            message += f'［既知: {reason}］'
        else:
            errors += 1
        level = 'warning' if reason else 'error'
        print(f'::{level} file={path}::{message}' if annotate else f'{level.upper()} {path}: {message}')
    for path, err in failures.items():
        errors += 1
        print(f'::error file={path}::Web 用の変換に失敗した: {err}' if annotate
              else f'ERROR {path}: Web 用の変換に失敗した: {err}')

    print(f'{len(files)} 個の .tex を調べた。漏れ {errors} 件、既知の漏れ {warnings} 件。')
    return 0 if args.warn or errors == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
