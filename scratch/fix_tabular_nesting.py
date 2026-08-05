#!/usr/bin/env python3
"""
scratch/lint_latex_style.py の check_tabular_nesting が検出する
「tabular が center 直下にあるが table でラップされていない」violation を、
その center 環境全体を \\begin{table}[htb]\\centering ... \\end{table} に
変換することで機械的に修正する。

対象は「tabular の直近の親が center で、その center の親が table でない」
場合のみ（このリポジトリの現状の違反は全てこのパターン。center も無い
"裸の" tabular や、他の未知のパターンは対象外とし手動対応に回す）。

使い方: python3 scratch/fix_tabular_nesting.py <file1.tex> <file2.tex> ...
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_latex_style import ENV_TOKEN_RE  # noqa: E402


def fix_text(text):
    stack = []  # list of dict(name, begin_start, begin_end, needs_table)
    replacements = []  # (start, end, replacement)
    for m in ENV_TOKEN_RE.finditer(text):
        begin_name, end_name = m.group(1), m.group(2)
        if begin_name:
            if begin_name == 'tabular':
                if stack and stack[-1]['name'] == 'center':
                    grand_is_table = len(stack) >= 2 and stack[-2]['name'] == 'table'
                    if not grand_is_table:
                        stack[-1]['needs_table'] = True
            stack.append({'name': begin_name, 'begin_start': m.start(),
                           'begin_end': m.end(), 'needs_table': False})
        elif end_name:
            if stack and stack[-1]['name'] == end_name:
                top = stack.pop()
                if top['name'] == 'center' and top['needs_table']:
                    replacements.append((top['begin_start'], top['begin_end'],
                                          '\\begin{table}[htb]\n  \\centering'))
                    replacements.append((m.start(), m.end(), '\\end{table}'))
            elif end_name in [s['name'] for s in stack]:
                while stack and stack[-1]['name'] != end_name:
                    stack.pop()
                if stack:
                    stack.pop()

    if not replacements:
        return text, 0
    replacements.sort(key=lambda r: r[0], reverse=True)
    new_text = text
    for start, end, repl in replacements:
        new_text = new_text[:start] + repl + new_text[end:]
    return new_text, len(replacements) // 2


def main():
    paths = [Path(p) for p in sys.argv[1:]]
    changed = 0
    total = 0
    for p in paths:
        original = p.read_text(encoding='utf-8')
        new_text, n = fix_text(original)
        if new_text != original:
            p.write_text(new_text, encoding='utf-8')
            changed += 1
            total += n
            print(f"fixed {n} table(s): {p}")
    print(f"\n{changed}/{len(paths)} files changed, {total} table(s) wrapped")


if __name__ == '__main__':
    main()
