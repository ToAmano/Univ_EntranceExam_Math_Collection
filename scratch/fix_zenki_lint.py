#!/usr/bin/env python3
"""
titech/zenki の solution.tex / problem.tex に対し、scratch/lint_latex_style.py が
検出する違反のうち「機械的に安全な」ものだけを自動修正する:
  - \\frac / \\dfrac の添字位置ルール（\\int の上下限・評価カッコ ]_a^b の添字内は
    \\frac、それ以外は \\dfrac に統一）
  - \\sqrt の裸引数を {} で囲む
  - 句読点「。」「、」を「．」「，」に統一（% コメント内は対象外）

align* の \\begin{align} 化、tikzpicture のネスト修正、\\caption 追加、
enumerate/itemize の扱いは目視判断が必要なため対象外（別途手動対応）。

使い方: python3 scratch/fix_zenki_lint.py <file1.tex> <file2.tex> ...
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_latex_style import FRAC_CMD_RE, find_frac_exempt_spans  # noqa: E402


def fix_frac_subscript(text):
    """\\int / 評価カッコの添字位置なら \\frac、それ以外なら \\dfrac に統一する。"""
    spans = find_frac_exempt_spans(text)

    def in_span(pos):
        return any(s <= pos < e for s, e in spans)

    out = []
    last = 0
    for m in FRAC_CMD_RE.finditer(text):
        cmd = m.group(1)
        pos = m.start()
        inside = in_span(pos)
        target = None
        if inside and cmd == 'dfrac':
            target = 'frac'
        elif not inside and cmd == 'frac':
            target = 'dfrac'
        if target:
            out.append(text[last:m.start()])
            out.append('\\' + target)
            last = m.end()
    out.append(text[last:])
    return ''.join(out)


def fix_punctuation(text):
    """% コメントを除く箇所の「。」「、」を「．」「，」に置換する。"""
    trans = {'。': '．', '、': '，'}
    out = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == '\\' and i + 1 < n:
            out.append(text[i:i + 2])
            i += 2
            continue
        if c == '%':
            j = i
            while j < n and text[j] != '\n':
                j += 1
            out.append(text[i:j])
            i = j
            continue
        out.append(trans.get(c, c))
        i += 1
    return ''.join(out)


# --- \\sqrt の裸引数修正 (scratch/fix_latex_format.py の parse_arg/fix_sqrt を流用) ---
def parse_arg(text, i):
    n = len(text)
    while i < n and text[i] in ' \t':
        i += 1
    if i >= n:
        raise ValueError("unexpected end of input while parsing argument")
    if text[i] == '{':
        depth = 1
        j = i + 1
        while depth > 0:
            if j >= n:
                raise ValueError("unbalanced braces")
            if text[j] == '\\':
                j += 2
                continue
            if text[j] == '{':
                depth += 1
            elif text[j] == '}':
                depth -= 1
            j += 1
        return text[i + 1:j - 1], i, j
    elif text[i] == '\\':
        j = i + 1
        if j < n and text[j].isalpha():
            while j < n and text[j].isalpha():
                j += 1
        else:
            j += 1
        return text[i:j], i, j
    else:
        return text[i], i, i + 1


SQRT_RE = re.compile(r'\\sqrt(?![a-zA-Z])')


def fix_sqrt(text):
    out = []
    i = 0
    while True:
        m = SQRT_RE.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i:m.start()])
        j = m.end()
        n = len(text)
        k = j
        while k < n and text[k] in ' \t':
            k += 1
        optional = ''
        if k < n and text[k] == '[':
            depth = 1
            e = k + 1
            while depth > 0:
                if text[e] == '[':
                    depth += 1
                elif text[e] == ']':
                    depth -= 1
                e += 1
            optional = text[j:e]
            j = e
        arg, _, e = parse_arg(text, j)
        out.append('\\sqrt' + optional + '{' + fix_sqrt(arg) + '}')
        i = e
    return ''.join(out)


def main():
    paths = [Path(p) for p in sys.argv[1:]]
    changed = 0
    for p in paths:
        original = p.read_text(encoding='utf-8')
        text = original
        text = fix_frac_subscript(text)
        text = fix_sqrt(text)
        text = fix_punctuation(text)
        if text != original:
            p.write_text(text, encoding='utf-8')
            changed += 1
            print(f"fixed: {p}")
    print(f"\n{changed}/{len(paths)} files changed")


if __name__ == '__main__':
    main()
