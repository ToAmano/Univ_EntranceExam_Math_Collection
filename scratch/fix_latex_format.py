"""
既存 solution.tex/problem.tex に対し、AGENT.md 8.3.6 のルールに従って
  - \frac -> \dfrac
  - \dfrac / \sqrt の引数を必ず {} で囲む
を機械的に適用する（トークンレベルでパースするため、\frac12 のような
裸引数も \dfrac{1}{2} に正しく展開される）。\overline の置換はここでは行わない
（辺の長さ用途かどうか文脈確認が必要なため別対応）。
"""
import re
import sys


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


FRAC_RE = re.compile(r'\\(frac|dfrac)(?![a-zA-Z])')


def fix_frac(text):
    out = []
    i = 0
    while True:
        m = FRAC_RE.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i:m.start()])
        j = m.end()
        arg1, _, e1 = parse_arg(text, j)
        arg2, _, e2 = parse_arg(text, e1)
        # 引数中にさらに \frac / \dfrac がネストしている場合に備えて再帰的に処理する
        out.append('\\dfrac{' + fix_frac(arg1) + '}{' + fix_frac(arg2) + '}')
        i = e2
    return ''.join(out)


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


def fix_text(text):
    return fix_sqrt(fix_frac(text))


def main():
    paths = [l.strip() for l in sys.stdin if l.strip()]
    changed = 0
    for p in paths:
        with open(p, encoding='utf-8') as f:
            original = f.read()
        fixed = fix_text(original)
        if fixed != original:
            with open(p, 'w', encoding='utf-8') as f:
                f.write(fixed)
            changed += 1
    print(f"changed {changed}/{len(paths)} files")


if __name__ == '__main__':
    main()
