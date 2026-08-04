#!/usr/bin/env python3
"""
AGENT.md 8.3.6「LaTeX フォーマットの注意事項」を機械的にチェックする lint スクリプト。
.github/workflows/lint-tex.yml から呼び出される。

対象は src/**/solution.tex と src/**/problem.tex。
目視判断が必要なルール（大カッコを \\Bigl 化すべきか、enumerate/itemize が小問
ラベリング目的か場合分け目的か等）は対象外。
違反が1件でもあれば exit code 1 で終了する（\\overline{} の使用のみ警告扱いで非ブロッキング）。
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / 'src'

ENV_TOKEN_RE = re.compile(r'\\begin\{([a-zA-Z*]+)\}|\\end\{([a-zA-Z*]+)\}')

# \int の上下限、または評価カッコ ]_a^b の添字位置を示す「起点」トークン
TRIGGER_RE = re.compile(
    r'(\\int|\\bigr\]|\\Bigr\]|\\biggr\]|\\Biggr\]|\\right\]|\])\s*([_^])'
)

FRAC_CMD_RE = re.compile(r'\\(d?frac)(?![a-zA-Z])')


def line_of(text, pos):
    return text.count('\n', 0, pos) + 1


def strip_comments(text):
    """% 以降 行末までをスペースに置き換える（文字位置・行番号は変えない）。
    \\% はエスケープされたパーセント記号なのでコメント開始とはみなさない。
    TikZ 内のコメントは句読点など解答文の規約と別の慣習（「、」等）で
    書かれていることが多く、コメントを対象外にしないと誤検知になる。"""
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
            out.append(' ' * (j - i))
            i = j
            continue
        out.append(c)
        i += 1
    return ''.join(out)


def extract_braced(text, start):
    """text[start] == '{' 前提。対応する '}' までの (中身, 終了直後index) を返す。"""
    depth = 0
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        if c == '\\' and i + 1 < n:
            i += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return text[start + 1:], n


def check_align_star(text):
    errors = []
    for m in re.finditer(r'\\(begin|end)\{align\*\}', text):
        errors.append((line_of(text, m.start()), "align* は使わない（align を使う）"))
    return errors


def check_punctuation(text):
    errors = []
    for m in re.finditer(r'[。、]', text):
        errors.append((line_of(text, m.start()),
                        f"句読点は全角「．」「，」を使う（「{m.group()}」が見つかった）"))
    return errors


# enumerate/itemize は「小問(1),(2),...を enumerate で囲う」場合のみ禁止で，
# 場合分け（1°, 2°, ... の case analysis）等での使用は許容される。この2つを
# 構文的に判別するのは信頼できないため機械チェックの対象からは外している
# （大カッコのサイズ判断と同様、目視確認が必要なルール）。


def check_proof_env(text):
    errors = []
    for m in re.finditer(r'\\begin\{proof\}', text):
        errors.append((line_of(text, m.start()), "\\begin{proof} は使わない（{\\bf [解]} を使う）"))
    return errors


def check_documentclass(text):
    errors = []
    m = re.search(r'\\documentclass\[([./]*)main\.tex\]\{subfiles\}', text)
    if not m:
        errors.append((1, "\\documentclass[../../main.tex]{subfiles} が見つからない"))
        return errors
    up_count = m.group(1).count('../')
    if up_count != 2:
        errors.append((line_of(text, m.start()),
                        f"\\documentclass の相対パスは ../../ であるべき（{up_count} 階層になっている）"))
    return errors


def check_bare_args(text):
    """\\sqrt, \\frac, \\dfrac の引数が {} で囲まれているかチェックする。"""
    errors = []
    n = len(text)
    for cmd in ('sqrt', 'frac', 'dfrac'):
        for m in re.finditer(r'\\' + cmd + r'(?![a-zA-Z])', text):
            j = m.end()
            while j < n and text[j] in ' \t':
                j += 1
            if cmd == 'sqrt' and j < n and text[j] == '[':
                depth = 1
                e = j + 1
                while e < n and depth > 0:
                    if text[e] == '[':
                        depth += 1
                    elif text[e] == ']':
                        depth -= 1
                    e += 1
                j = e
                while j < n and text[j] in ' \t':
                    j += 1
            nargs = 1 if cmd == 'sqrt' else 2
            pos = j
            ok = True
            for _ in range(nargs):
                if pos < n and text[pos] == '{':
                    _, pos = extract_braced(text, pos)
                    while pos < n and text[pos] in ' \t':
                        pos += 1
                else:
                    ok = False
                    break
            if not ok:
                errors.append((line_of(text, m.start()),
                                f"\\{cmd} の引数は必ず {{}} で囲む（裸引数が見つかった）"))
    return errors


def check_figure_caption(text):
    errors = []
    for m in re.finditer(r'\\begin\{figure\}', text):
        end_m = re.search(r'\\end\{figure\}', text[m.end():])
        body = text[m.end():m.end() + end_m.start()] if end_m else text[m.end():]
        if '\\caption{' not in body and '\\caption ' not in body:
            errors.append((line_of(text, m.start()), "figure 環境に \\caption{} がない"))
    return errors


def check_tikz_nesting(text):
    """tikzpicture は figure の直下、または figure > center の下にネストする
    （\\centering コマンド利用時は center 環境自体が無いので figure 直下でよい）。"""
    errors = []
    stack = []
    for m in ENV_TOKEN_RE.finditer(text):
        begin_name, end_name = m.group(1), m.group(2)
        if begin_name:
            if begin_name == 'tikzpicture':
                ok = (len(stack) >= 1 and stack[-1] == 'figure') or \
                     (len(stack) >= 2 and stack[-1] == 'center' and stack[-2] == 'figure')
                if not ok:
                    errors.append((line_of(text, m.start()),
                                    "tikzpicture は figure（直下、または center を挟んで）の中にネストする"))
            stack.append(begin_name)
        elif end_name:
            if stack and stack[-1] == end_name:
                stack.pop()
            elif end_name in stack:
                while stack and stack[-1] != end_name:
                    stack.pop()
                if stack:
                    stack.pop()
    return errors


def find_frac_exempt_spans(text):
    """\\int の上下限・評価カッコ ]_a^b の添字位置の (start, end) 一覧を返す。
    そこに現れる分数は \\dfrac ではなく \\frac を使ってよい（使うべき）。

    添字は _{...} や ^{...} のように {} で囲まれている場合だけでなく、
    _0 や ^n のような裸の1トークンのこともある。裸トークンの場合でも
    "もう一方の添字" を見逃さないよう、必ず1トークン分だけ読み飛ばして
    次を確認する（\\int_0^{\\frac{\\pi}{2}t} で ^{...} 側を見逃すと、
    その中の \\frac を誤って \\dfrac に変換してしまうバグになる）。"""
    n = len(text)
    spans = []
    for m in TRIGGER_RE.finditer(text):
        j = m.end()
        for _ in range(2):  # 添字は _{...}^{...} の順不同で最大2つ
            while j < n and text[j] in ' \t':
                j += 1
            if j >= n:
                break
            if text[j] == '{':
                _, j2 = extract_braced(text, j)
                spans.append((j, j2))
                j = j2
            elif text[j] == '\\':
                k = j + 1
                while k < n and text[k].isalpha():
                    k += 1
                if k == j + 1:
                    k += 1  # \X（英字以外1文字）はそれ自体が1つのコマンド
                j = k
            else:
                j += 1  # 裸の1文字（数字・添え字変数など）
            while j < n and text[j] in ' \t':
                j += 1
            if j < n and text[j] in '_^':
                j += 1
                continue
            break
    return spans


def check_frac_subscript_rule(text):
    """\\int の上下限・評価カッコ ]_a^b の添字位置では \\frac、それ以外では \\dfrac を使う。"""
    errors = []
    spans = find_frac_exempt_spans(text)

    def in_span(pos):
        return any(s <= pos < e for s, e in spans)

    for m in FRAC_CMD_RE.finditer(text):
        cmd = m.group(1)
        pos = m.start()
        inside = in_span(pos)
        if inside and cmd == 'dfrac':
            errors.append((line_of(text, pos),
                            "\\int の上下限・評価カッコ ]_a^b の添字位置では \\dfrac ではなく \\frac を使う"))
        elif not inside and cmd == 'frac':
            errors.append((line_of(text, pos),
                            "分数は（添字位置を除き）\\frac ではなく \\dfrac を使う"))
    return errors


def check_overline_warning(text):
    warnings = []
    for m in re.finditer(r'\\overline\{', text):
        warnings.append((line_of(text, m.start()),
                          "\\overline{...} は辺の長さの表記では使わない（|AB| を使う。循環小数等の用途なら無視してよい）"))
    return warnings


def lint_file(path):
    text = strip_comments(path.read_text(encoding='utf-8'))
    errors = []
    errors += check_align_star(text)
    errors += check_punctuation(text)
    errors += check_bare_args(text)
    errors += check_figure_caption(text)
    errors += check_tikz_nesting(text)
    errors += check_documentclass(text)
    errors += check_proof_env(text)
    errors += check_frac_subscript_rule(text)
    warnings = check_overline_warning(text)
    return errors, warnings


def main():
    only_changed = None
    if len(sys.argv) > 1:
        only_changed = set(Path(p).resolve() for p in sys.argv[1:])

    targets = sorted(SRC_DIR.rglob('*.tex'))
    total_errors = 0
    total_warnings = 0
    files_checked = 0
    for path in targets:
        if path.name not in ('solution.tex', 'problem.tex'):
            continue
        if only_changed is not None and path.resolve() not in only_changed:
            continue
        files_checked += 1
        errors, warnings = lint_file(path)
        rel = path.relative_to(REPO_ROOT)
        for lineno, msg in sorted(errors):
            print(f"::error file={rel},line={lineno}::{msg}")
            total_errors += 1
        for lineno, msg in sorted(warnings):
            print(f"::warning file={rel},line={lineno}::{msg}")
            total_warnings += 1

    print(f"\n{files_checked} 個の .tex を走査。エラー {total_errors} 件、警告 {total_warnings} 件。")
    if total_errors > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
