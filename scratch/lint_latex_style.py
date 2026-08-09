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
    """kouki 系の problem.tex は \\begin{document} を持たない中身だけの
    フラグメントで、solution.tex 側から \\input{problem.tex} される設計
    （scratch/generate_main_tex.py 冒頭のコメント参照）。\\begin{document}
    が無いファイルは documentclass も無くて正しいので対象外とする。"""
    errors = []
    if '\\begin{document}' not in text:
        return errors
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
    """figure 環境には \\caption{} が必要。ただし subcaptionblock で複数図を
    並べる形式では、個々のパネルに \\subcaption{} が付いていれば
    （figure 全体としての \\caption が無くても）説明責務は果たされている
    とみなし、\\subcaption{} の存在も許容する。"""
    errors = []
    for m in re.finditer(r'\\begin\{figure\}', text):
        end_m = re.search(r'\\end\{figure\}', text[m.end():])
        body = text[m.end():m.end() + end_m.start()] if end_m else text[m.end():]
        has_caption = '\\caption{' in body or '\\caption ' in body
        has_subcaption = '\\subcaption{' in body or '\\subcaption ' in body
        if not has_caption and not has_subcaption:
            errors.append((line_of(text, m.start()), "figure 環境に \\caption{} がない"))
    return errors


MATH_DISPLAY_ENVS = {'align', 'align*', 'equation', 'equation*', 'gather', 'gather*',
                     'multline', 'multline*', 'split', 'flalign', 'flalign*'}


def find_command_arg_spans(text, command):
    """\\command{...} の引数部分 (中身を含む {} の start,end) の一覧を返す。
    \\shadowbox{\\begin{tabular}...\\end{tabular}} のように、環境ではなく
    ブレース引数を取るコマンドで囲われている場合はスタック追跡に乗らない
    ため、別途この関数で除外対象の範囲を求める。"""
    spans = []
    for m in re.finditer(r'\\' + re.escape(command) + r'\{', text):
        start = m.end() - 1
        _, end = extract_braced(text, start)
        spans.append((start, end))
    return spans


def check_env_nesting(text, target_env, required_ancestor, error_msg,
                       allow_subcaptionblock=True, allow_math_exempt=False,
                       exempt_spans=()):
    """target_env が required_ancestor の直下、required_ancestor > center
    （\\centering 利用時は center 環境自体が無いので直下でもよい）、または
    required_ancestor > subcaptionblock（複数図/表を並べる場合、許可時）の
    いずれかにネストされているかを、環境の開始・終了トークンをスタックで
    追跡してチェックする汎用ロジック。tikzpicture・tabular 両方の
    ネストチェックがこれを呼ぶ（別々に実装すると2箇所が食い違うバグの元）。
    exempt_spans は find_command_arg_spans 等で求めた (start,end) の
    一覧で、その範囲内にある target_env は無条件で許容する。"""
    errors = []
    stack = []
    for m in ENV_TOKEN_RE.finditer(text):
        begin_name, end_name = m.group(1), m.group(2)
        if begin_name:
            if begin_name == target_env:
                pos = m.start()
                ok = any(s <= pos < e for s, e in exempt_spans)
                ok = ok or (len(stack) >= 1 and stack[-1] == required_ancestor) or \
                     (len(stack) >= 2 and stack[-1] == 'center' and stack[-2] == required_ancestor)
                if allow_subcaptionblock:
                    ok = ok or (len(stack) >= 1 and stack[-1] == 'subcaptionblock') or \
                         (len(stack) >= 2 and stack[-1] == 'center' and stack[-2] == 'subcaptionblock')
                if allow_math_exempt:
                    ok = ok or any(s in MATH_DISPLAY_ENVS for s in stack)
                if not ok:
                    errors.append((line_of(text, m.start()), error_msg))
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


def check_tikz_nesting(text):
    """tikzpicture は figure の直下、figure > center の下、figure >
    subcaptionblock の下（複数図を並べる場合）のいずれかにネストする
    （\\centering コマンド利用時は center 環境自体が無いので figure 直下でよい）。
    また、S=[小さな図]-[小さな図] のように align 等の数式環境内で
    \\text{\\begin{tikzpicture}...} を図形記号として使う用法もあるため、
    align 等の数式表示環境の中にある tikzpicture も許容する。"""
    return check_env_nesting(
        text, 'tikzpicture', 'figure',
        "tikzpicture は figure（直下、center/subcaptionblockを挟んで）の中、"
        "または align 等の数式環境内（図形記号として使う場合）にネストする",
        allow_subcaptionblock=True, allow_math_exempt=True)


def check_tabular_nesting(text):
    """tabular は table の直下、table > center の下、table >
    subcaptionblock の下（複数表を並べる場合）のいずれかにネストする
    （\\centering コマンド利用時は center 環境自体が無いので table 直下でよい）。
    tikzpicture と異なり、align 等の数式内にインライン記号として tabular を
    使う慣習は無いため math_exempt は許可しない。ただし \\shadowbox{...} で
    表全体を枠囲みにする用法（年度サマリファイルの凡例など）は table 化の
    対象外として除外する。"""
    return check_env_nesting(
        text, 'tabular', 'table',
        "tabular は table（直下、center/subcaptionblockを挟んで）の中にネストする",
        allow_subcaptionblock=True, allow_math_exempt=False,
        exempt_spans=find_command_arg_spans(text, 'shadowbox'))


def find_tikzpicture_spans(text):
    """\\begin{tikzpicture}...\\end{tikzpicture} の (start, end) 一覧を返す。
    図中の node ラベル（多くは font=\\small 等で縮小表示される）でも、
    添字位置と同じ理由で \\dfrac だと間延びするため \\frac を使ってよい。"""
    return [(m.start(), m.end())
            for m in re.finditer(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', text, re.DOTALL)]


def find_frac_exempt_spans(text):
    """あらゆる上付き・下付き（_{...} / ^{...}）の中身、および tikzpicture
    環境全体の (start, end) 一覧を返す。そこに現れる分数は \\dfrac ではなく
    \\frac を使ってよい（使うべき）。

    当初は \\int の上下限や評価カッコ ]_a^b の直後の添字だけに限定していたが
    （TRIGGER_RE 参照）、AGENT.md のルール文自体は「上付き・下付きの位置」を
    一般的に指しており、x^{\\dfrac{1}{m}} のように \\int/評価カッコを伴わない
    単なる変数の指数でも同じ理由（添字位置では文字が縮小されるため \\dfrac だと
    間延びする）で \\frac にすべき。実際 titech zenki 1986/5 で見逃していた
    （TRIGGER_RE ベースの実装は \\int_0^{...} のような限られた形にしか
    反応せず、x^{...} のような一般の添字を検出できなかった）。
    そのため _/^ の直後が {...} であれば、直前が何であるかによらず
    無条件に添字位置とみなす（このコーパスで _ と ^ は数式の添字演算子
    以外の用途では使われないため、一般化しても誤検知のリスクは低い）。

    同じ理由で、tikzpicture 内の node ラベルも titech zenki 1987/1988 で
    まとめて \\frac が使われていたことから例外に加えた。"""
    n = len(text)
    spans = []
    for m in re.finditer(r'[_^]\s*\{', text):
        brace_start = m.end() - 1
        _, end = extract_braced(text, brace_start)
        spans.append((brace_start, end))
    spans.extend(find_tikzpicture_spans(text))
    return spans


def check_frac_subscript_rule(text):
    """上付き・下付き（_{...} / ^{...}）の添字位置および tikzpicture 内では
    \\frac、それ以外では \\dfrac を使う。"""
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
                            "添字位置・tikzpicture内では \\dfrac ではなく \\frac を使う"))
        elif not inside and cmd == 'frac':
            errors.append((line_of(text, pos),
                            "分数は（添字位置・tikzpicture内を除き）\\frac ではなく \\dfrac を使う"))
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
    errors += check_tabular_nesting(text)
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
