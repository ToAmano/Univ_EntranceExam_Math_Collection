#!/usr/bin/env python3
"""数学答案の TeX 規約（skills/math-solution-tex/references/）のうち、機械で判定できるものを調べる lint。

使い方:
  python3 scripts/lint_tex.py <file.tex> [...]
  python3 scripts/lint_tex.py --rules local/lint_local.py <file.tex> [...]   # 利用先固有の検査も行う
  python3 scripts/lint_tex.py --diff <file.tex>   # 機械的な修正の差分を表示する
  python3 scripts/lint_tex.py --fix <file.tex>    # 機械的な修正を書き込んでから検査する

違反が1件でもあれば exit code 1 で終了する（\overline{} と align の長い行は警告で、終了コードに影響しない）。
目視の判断が要る規則（大カッコの大きさ、enumerate が小問のラベルか場合分けか など）は対象外。

利用先固有の検査は --rules で渡すモジュールの PROFILE（Profile の派生）に書く。
"""
import argparse
import difflib
import importlib.util
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load_sibling(stem):
    """同じディレクトリのモジュールを、パッケージの有無によらず同じ名前で読み込む。"""
    name = f'_math_solution_tex_{stem}'
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, _HERE / f'{stem}.py')
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


tex_references = _load_sibling('tex_references')


ENV_TOKEN_RE = re.compile(r'\\begin\{([a-zA-Z*]+)\}|\\end\{([a-zA-Z*]+)\}')

# ファイル先頭などに `% lint-skip: 理由` を書いておくと、このファイルの
# lint チェックを丸ごとスキップできる。古い形式のまま未移行で文書の構造が
# 規約と異なるなど、直す予定はあるが今直すのは別作業というファイルを、
# 直るまでの間 ratchet の対象から外すための避難ハッチ。空のまま放置されると気づかれず
# 違反が溜まり続けるため、理由を書くことを必須にしている。
LINT_SKIP_RE = re.compile(r'%\s*lint-skip\s*:\s*(\S.*)')

FRAC_CMD_RE = re.compile(r'\\(d?frac)(?![a-zA-Z])')

# align 内の1行の推定表示幅（文字数換算）の上限。
# 10.5pt / 本文組版幅（約420〜440pt）では約75〜80文字が1行の収容限界に相当する。
# \dfrac や \label などの TeX コマンドは実際の横幅よりコード長が肥大化しやすいため、
# estimate_math_visual_length で推定表示幅に換算した上で判定する。
ALIGN_LINE_LENGTH_LIMIT = 80
ALIGN_LINE_MIN_EQUALS = 2


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


def _extract_bracket(text, start):
    """text[start] == '[' 前提。ネストした [] と {} を考慮して (中身, 終了直後index) を返す。"""
    depth_k = 0
    depth_b = 0
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        if c == '\\' and i + 1 < n:
            i += 2
            continue
        if c == '{':
            depth_b += 1
        elif c == '}':
            depth_b = max(0, depth_b - 1)
        elif depth_b == 0:
            if c == '[':
                depth_k += 1
            elif c == ']':
                depth_k -= 1
                if depth_k == 0:
                    return text[start + 1:i], i + 1
        i += 1
    return text[start + 1:], n


def check_align_star(text):
    errors = []
    for m in re.finditer(r'\\(begin|end)\{align\*\}', text):
        errors.append((line_of(text, m.start()), "align* は使わない（align を使う）"))
    return errors


def check_equation_env(text):
    errors = []
    for m in re.finditer(r'\\(begin|end)\{\s*(equation\*?)\s*\}', text):
        env = m.group(2)
        errors.append((line_of(text, m.start()), f"{env} は使わない（align を使う）"))
    return errors


# \end{align} の直前の改行 \\（\\[2pt] 等を含む）は中身のない行を作り、
# PDF に空の式番号が出る。間に \label/\notag だけがある場合も
# 中身のない行なので検出する。
TRAILING_ALIGN_BREAK_RE = re.compile(
    r'(?<!\\)\\\\(?:\s*\[[^\]]*\])?'
    r'(?P<tail>(?:\s|\\(?:notag|nonumber)(?![a-zA-Z])|\\label\{[^}]*\})*)'
    r'\\end\{align\}')


def check_trailing_align_break(text):
    errors = []
    for m in TRAILING_ALIGN_BREAK_RE.finditer(text):
        errors.append((
            line_of(text, m.start()),
            "\\end{align} の直前に改行 \\\\ がある（空の式番号が出る）",
        ))
    return errors


def _find_trailing_align_break_edits(text, raw):
    """間が空白・コメントだけの場合に限り、末尾の \\\\ を削除する。
    \\label を挟む場合に削除するとラベルが前の行へ移り番号の意味が変わるため、
    手動修正に任せる。"""
    stripped = strip_comments(raw)
    edits = []
    for m in TRAILING_ALIGN_BREAK_RE.finditer(stripped):
        if m.group('tail').strip() or text[m.start()] == ' ':
            continue
        start = m.start()
        while start > 0 and stripped[start - 1] in ' \t':
            start -= 1
        edits.append((start, m.start('tail'), ''))
    return edits


def _find_equation_env_edits(text):
    edits = []
    for m in re.finditer(r'\\begin\{\s*equation\*?\s*\}', text):
        edits.append((m.start(), m.end(), r'\begin{align}'))
    for m in re.finditer(r'\\end\{\s*equation\*?\s*\}', text):
        edits.append((m.start(), m.end(), r'\end{align}'))
    return edits


DISPLAY_BRACKET_TOKEN_RE = re.compile(r'(?<!\\)(?:\\\\)*(\\\[|\\\])')
DISPLAY_BRACKET_BLOCK_RE = re.compile(
    r'(?<!\\)(?P<pre_open>(?:\\\\)*)\\\[(?P<body>.*?)(?<!\\)(?P<pre_close>(?:\\\\)*)\\\]',
    re.DOTALL,
)
ALIGNED_WRAP_RE = re.compile(
    r'^\s*\\begin\{aligned\}[ \t]*\r?\n?(?P<inner>.*?)\r?\n?[ \t]*\\end\{aligned\}\s*$',
    re.DOTALL,
)


def check_display_math_brackets(text):
    """ディスプレイ数式の \\[ ... \\] を検出し、align 環境の使用を促す。
    改行オプション \\\\[2pt] 等（バックスラッシュ2個）は誤検知しない。"""
    errors = []
    for m in DISPLAY_BRACKET_TOKEN_RE.finditer(text):
        tok = m.group(1)
        errors.append((
            line_of(text, m.start(1)),
            f"{tok} は使わない（align 環境を使う）",
        ))
    return errors


def find_display_math_dollars(text):
    """Scan text for display math $$ ... $$ while respecting inline $...$ and escaped \\$.
    Returns:
      blocks: list of (open_start, open_end, close_start, close_end, masked_body)
      tokens: list of token start indices
    """
    i = 0
    n = len(text)
    blocks = []
    tokens = []
    while i < n:
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '$':
            if i + 1 < n and text[i + 1] == '$':
                open_start = i
                open_end = i + 2
                tokens.append(open_start)
                j = open_end
                close_start = -1
                while j < n:
                    if text[j] == '\\':
                        j += 2
                        continue
                    if text[j] == '$':
                        if j + 1 < n and text[j + 1] == '$':
                            close_start = j
                            close_end = j + 2
                            tokens.append(close_start)
                            blocks.append((open_start, open_end, close_start, close_end, text[open_end:close_start]))
                            i = close_end
                            break
                        else:
                            j += 1
                    else:
                        j += 1
                if close_start == -1:
                    break
            else:
                j = i + 1
                while j < n:
                    if text[j] == '\\':
                        j += 2
                        continue
                    if text[j] == '$':
                        i = j + 1
                        break
                    j += 1
                else:
                    break
        else:
            i += 1
    return blocks, tokens


def check_display_math_dollars(text):
    """ディスプレイ数式の $$ ... $$ を検出し、align 環境の使用を促す。"""
    errors = []
    text_no_comments = strip_comments(text)
    _, tokens = find_display_math_dollars(text_no_comments)
    for pos in tokens:
        errors.append((
            line_of(text, pos),
            "$$ は使わない（align 環境を使う）",
        ))
    return errors


def _find_display_math_dollar_edits(text, raw):
    edits = []
    nl = '\r\n' if '\r\n' in raw else '\n'
    blocks, _ = find_display_math_dollars(text)
    for open_start, open_end, close_start, close_end, masked_body in blocks:
        raw_body = raw[open_end:close_start]

        line_start = text.rfind('\n', 0, open_start) + 1
        indent_m = re.match(r'[ \t]*', text[line_start:open_start])
        indent = indent_m.group(0) if indent_m else ''

        pre_text = text[line_start:open_start].strip()
        line_end = text.find('\n', close_end)
        if line_end == -1:
            line_end = len(text)
        post_text = text[close_end:line_end].strip()

        prefix = f"{nl}{indent}" if pre_text else ""
        suffix = f"{nl}{indent}" if post_text else ""

        m_aligned = ALIGNED_WRAP_RE.match(masked_body)
        if m_aligned:
            inner_start, inner_end = m_aligned.span('inner')
            inner_raw = raw_body[inner_start:inner_end]
            replacement = f"{prefix}\\begin{{align}}{nl}{inner_raw}{nl}{indent}\\end{{align}}{suffix}"
            edits.append((open_start, close_end, replacement))
            continue

        if '\n' not in raw_body:
            replacement = f"{prefix}\\begin{{align}}{nl}{indent}  {raw_body.strip()}{nl}{indent}\\end{{align}}{suffix}"
            edits.append((open_start, close_end, replacement))
            continue

        body_out = raw_body
        if not body_out.startswith(('\n', '\r\n')):
            body_out = f"{nl}{indent}  " + body_out.lstrip(' \t')
        if not body_out.rstrip(' \t').endswith(('\n', '\r\n')):
            body_out = body_out.rstrip(' \t') + f"{nl}{indent}"
        replacement = f"{prefix}\\begin{{align}}{body_out}\\end{{align}}{suffix}"
        edits.append((open_start, close_end, replacement))
    return edits


def _find_display_math_bracket_edits(text, raw):
    edits = []
    nl = '\r\n' if '\r\n' in raw else '\n'
    for m in DISPLAY_BRACKET_BLOCK_RE.finditer(text):
        open_start = m.start() + len(m.group('pre_open'))
        open_end = open_start + 2  # len(r'\[')
        close_end = m.end()
        close_start = close_end - 2  # len(r'\]')
        masked_body = text[open_end:close_start]
        raw_body = raw[open_end:close_start]

        line_start = text.rfind('\n', 0, open_start) + 1
        indent_m = re.match(r'[ \t]*', text[line_start:open_start])
        indent = indent_m.group(0) if indent_m else ''

        m_aligned = ALIGNED_WRAP_RE.match(masked_body)
        if m_aligned:
            inner_start, inner_end = m_aligned.span('inner')
            inner_raw = raw_body[inner_start:inner_end]
            replacement = f"\\begin{{align}}{nl}{inner_raw}{nl}{indent}\\end{{align}}"
            edits.append((open_start, close_end, replacement))
            continue

        if '\n' not in raw_body:
            replacement = f"\\begin{{align}}{nl}{indent}  {raw_body.strip()}{nl}{indent}\\end{{align}}"
            edits.append((open_start, close_end, replacement))
            continue

        body_out = raw_body
        if not body_out.startswith(('\n', '\r\n')):
            body_out = f"{nl}{indent}  " + body_out.lstrip(' \t')
        if not body_out.rstrip(' \t').endswith(('\n', '\r\n')):
            body_out = body_out.rstrip(' \t') + f"{nl}{indent}"
        replacement = f"\\begin{{align}}{body_out}\\end{{align}}"
        edits.append((open_start, close_end, replacement))
    return edits


# 和文に接する半角の「,」「.」（「である.」「から,」「以下, 」など）。数式・図・TikZ の中、
# 「...」のような点の連続、「1.2」のような数字の後の「.」は対象外。
_JA_CHAR = r'[\u3040-\u30ff\u3400-\u9fff\uff01-\uff60\u3000-\u303f]'
HALFWIDTH_PUNCT_RE = re.compile(
    rf'(?<![.0-9])(?:(?<={_JA_CHAR})[,.]|[,.](?={_JA_CHAR}))(?!\.)')
HALFWIDTH_PUNCT_PROTECT_RE = re.compile(
    r'\\begin\{(align\*?|equation\*?|gather\*?|multline\*?|figure|tikzpicture)\}.*?\\end\{\1\}'
    r'|\$\$.*?\$\$|(?<!\\)\$(?:\\\$|[^$])+?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)', re.S)


def _find_halfwidth_punct(masked):
    """和文に接する半角の「,」「.」の位置を返す（masked はコメント等を空白にした本文）。"""
    start = masked.find('\\begin{document}')
    start = 0 if start < 0 else start
    protected = [(m.start(), m.end()) for m in HALFWIDTH_PUNCT_PROTECT_RE.finditer(masked, start)]
    return [m for m in HALFWIDTH_PUNCT_RE.finditer(masked, start)
            if not any(a <= m.start() < b for a, b in protected)]


def check_punctuation(text):
    errors = []
    for m in re.finditer(r'[。、]', text):
        errors.append((line_of(text, m.start()),
                        f"句読点は全角「．」「，」を使う（「{m.group()}」が見つかった）"))
    for m in _find_halfwidth_punct(_mask_protected_regions(text)):
        full = {',': '，', '.': '．'}[m.group()]
        errors.append((line_of(text, m.start()),
                       f"和文の句読点は全角「{full}」を使う（半角の「{m.group()}」が見つかった）"))
    return errors


# enumerate/itemize は「小問(1),(2),...を enumerate で囲う」場合のみ禁止で，
# 場合分け（1°, 2°, ... の case analysis）等での使用は許容される。この2つを
# 構文的に判別するのは信頼できないため機械チェックの対象からは外している
# （大カッコのサイズ判断と同様、目視確認が必要なルール）。


def check_duplicate_labels(text):
    """同一ファイル内で \\label{...} が重複していないかチェックする。
    複数の答案を1冊に束ねる場合も、各答案が自分の中の式だけを \\cref で参照する
    書き方なら、ラベル名が他のファイルと衝突していても実害はない。しかし同一ファイル内の重複は \\cref の参照先が最後に定義された
    方に化けて曖昧になる実害のあるバグなので、ここだけを検出する。"""
    errors = []
    seen = {}
    for m in re.finditer(r'\\label\{([^}]*)\}', text):
        name = m.group(1)
        seen.setdefault(name, []).append(m.start())
    for name, positions in seen.items():
        if len(positions) > 1:
            for pos in positions:
                errors.append((line_of(text, pos),
                                f"\\label{{{name}}} が同一ファイル内で重複している（\\cref の参照先が曖昧になる）"))
    return errors


def check_equation_references(text, problem_text=''):
    """Require local numeric equation labels and resolvable references."""
    errors = []
    definitions = {name for command, name, _, _ in tex_references.commands(text + problem_text)
                   if command == 'label'}
    math_positions = tex_references.math_label_positions(text)
    for command, argument, start, _ in tex_references.commands(text):
        line = line_of(text, start)
        if command == 'label':
            if ('eq:' in argument or start in math_positions) and not re.fullmatch(r'eq:[1-9][0-9]*', argument):
                errors.append((line, f"数式ラベル \\label{{{argument}}} は eq:1 形式の連番にする"))
        else:
            for name in tex_references.references(argument):
                if name not in definitions:
                    errors.append((line, f"\\{command}{{{name}}} は未定義のラベルを参照している"))
    return errors


def check_reference_commands(text):
    r"""\eqref や \ref は使用せず \cref に統一する。"""
    errors = []
    for command, argument, start, _ in tex_references.commands(text):
        if command in ('ref', 'eqref'):
            line = line_of(text, start)
            errors.append((line, f"参照には \\{command} ではなく \\cref を使う（\\{command}{{{argument}}}）"))
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


BARE_ARG_CMD_RE = re.compile(r'\\(sqrt|frac|dfrac)(?![a-zA-Z])')
BARE_ARG_CS_BLOCKLIST = {
    'begin', 'end',
    'frac', 'dfrac', 'tfrac', 'cfrac', 'sqrt',
    'text', 'mathrm', 'mathbf', 'bm', 'boldsymbol',
    'mathit', 'mathsf', 'mathtt', 'mathbb', 'mathcal', 'mathfrak',
    'left', 'right', 'bigl', 'bigr', 'Bigl', 'Bigr', 'biggl', 'biggr', 'Biggl', 'Biggr',
    'big', 'Big', 'bigg', 'Bigg',
    'overline', 'underline', 'overbrace', 'underbrace',
    'vec', 'overrightarrow', 'dot', 'ddot', 'hat', 'tilde', 'bar', 'acute', 'grave', 'check', 'breve',
    'not',
    'displaystyle', 'textstyle', 'scriptstyle', 'scriptscriptstyle',
    'quad', 'qquad', 'hspace', 'vspace',
    'label', 'ref', 'cref', 'eqref', 'cite',
}


def _find_bare_argument_edits(text, raw):
    """\\sqrt, \\frac, \\dfrac の引数で {} で囲まれていない裸引数を検出し、
    {} で囲む置換エディット (start, end, replacement) のリストを返す。
    不正な引数形式（() 等）が含まれる場合は巻き込み防止のため置換しない。"""
    edits = []
    n = len(text)
    for m in BARE_ARG_CMD_RE.finditer(text):
        cmd = m.group(1)
        j = m.end()
        if cmd == 'sqrt':
            k = j
            while k < n and text[k] in ' \t':
                k += 1
            if k < n and text[k] == '[':
                _, j = _extract_bracket(text, k)
        nargs = 1 if cmd == 'sqrt' else 2
        pos = j
        cmd_edits = []
        valid = True
        for _ in range(nargs):
            pre_start = pos
            while pos < n and text[pos] in ' \t':
                pos += 1
            if pos >= n:
                valid = False
                break
            if text[pos] == '{':
                _, pos = extract_braced(text, pos)
            elif text[pos] == '\\':
                k = pos + 1
                if k < n and text[k].isalpha():
                    while k < n and text[k].isalpha():
                        k += 1
                    cs = text[pos + 1:k]
                    if cs in BARE_ARG_CS_BLOCKLIST:
                        valid = False
                        break
                    start_idx = pre_start if all(c in ' \t' for c in raw[pre_start:pos]) else pos
                    cmd_edits.append((start_idx, k, f'{{{raw[pos:k]}}}'))
                    pos = k
                else:
                    valid = False
                    break
            elif text[pos].isalnum():
                start_idx = pre_start if all(c in ' \t' for c in raw[pre_start:pos]) else pos
                cmd_edits.append((start_idx, pos + 1, f'{{{raw[pos]}}}'))
                pos += 1
            else:
                valid = False
                break
        if valid and cmd_edits:
            cmd_edits.reverse()
            edits.extend(cmd_edits)
    return edits


def check_env_caption(text, env_name, error_msg):
    """figure/table 環境には \\caption{} が必要。ただし subcaptionblock で
    複数図/表を並べる形式では、個々のパネルに \\subcaption{} が付いていれば
    （環境全体としての \\caption が無くても）説明責務は果たされている
    とみなし、\\subcaption{} の存在も許容する。"""
    errors = []
    for m in re.finditer(r'\\begin\{' + env_name + r'\}', text):
        end_m = re.search(r'\\end\{' + env_name + r'\}', text[m.end():])
        body = text[m.end():m.end() + end_m.start()] if end_m else text[m.end():]
        has_caption = '\\caption{' in body or '\\caption ' in body
        has_subcaption = '\\subcaption{' in body or '\\subcaption ' in body
        if not has_caption and not has_subcaption:
            errors.append((line_of(text, m.start()), error_msg))
    return errors


def check_figure_caption(text):
    return check_env_caption(text, 'figure', "figure 環境に \\caption{} がない")


def check_table_caption(text):
    """table 環境にも figure と同じ理由で \\caption{} を必須にする
    （table があると \\caption で「表N: ...」の通し番号が付き、figure と扱いが揃う）。
    \\shadowbox{...} で囲む凡例的な tabular は check_tabular_nesting 側で
    そもそも table 化の対象外なので、ここにも出現しない。"""
    return check_env_caption(text, 'table', "table 環境に \\caption{} がない")


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


#  figure/table と中身の間に挟まっても構造上は無害な「透過的」レイアウト
#  コンテナ。center は centering 目的、subcaptionblock は複数図/表を
#  並べる目的、minipage は図を横に並べる際の列レイアウト目的で使われ、
#  どれだけ重ねて使っても（例: figure > minipage > center > tikzpicture）
#  入れ子としては許容する（例: 左右2枚の図）。
TRANSPARENT_NESTING_ENVS = ('center', 'subcaptionblock', 'minipage')


def check_env_nesting(text, target_env, required_ancestor, error_msg,
                       allow_subcaptionblock=True, allow_math_exempt=False,
                       exempt_spans=(), exempt_ancestors=()):
    """target_env が required_ancestor の直下、または
    TRANSPARENT_NESTING_ENVS（center/subcaptionblock/minipage）を何重に
    挟んだ先の required_ancestor の下にネストされているかを、環境の
    開始・終了トークンをスタックで追跡してチェックする汎用ロジック。
    tikzpicture・tabular 両方のネストチェックがこれを呼ぶ（別々に実装すると
    2箇所が食い違うバグの元）。
    exempt_spans は find_command_arg_spans 等で求めた (start,end) の
    一覧で、その範囲内にある target_env は無条件で許容する。
    exempt_ancestors に指定した環境内の target_env も許容する。"""
    transparent = TRANSPARENT_NESTING_ENVS if allow_subcaptionblock else \
        tuple(e for e in TRANSPARENT_NESTING_ENVS if e != 'subcaptionblock')
    errors = []
    stack = []
    for m in ENV_TOKEN_RE.finditer(text):
        begin_name, end_name = m.group(1), m.group(2)
        if begin_name:
            if begin_name == target_env:
                pos = m.start()
                ok = any(s <= pos < e for s, e in exempt_spans)
                ok = ok or any(env in exempt_ancestors for env in stack)
                if not ok:
                    i = len(stack) - 1
                    while i >= 0 and stack[i] in transparent:
                        i -= 1
                    ok = i >= 0 and stack[i] == required_ancestor
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
    表全体を枠囲みにする用法（年度サマリファイルの凡例など）と、
    tikzpicture 内の図中ノードに置く表は table 化の対象外として除外する。"""
    return check_env_nesting(
        text, 'tabular', 'table',
        "tabular は table（直下、center/subcaptionblockを挟んで）の中にネストする",
        allow_subcaptionblock=True, allow_math_exempt=False,
        exempt_spans=find_command_arg_spans(text, 'shadowbox'),
        exempt_ancestors=('tikzpicture',))


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
    （TRIGGER_RE 参照）、規約自体は「上付き・下付きの位置」を
    一般的に指しており、x^{\\dfrac{1}{m}} のように \\int/評価カッコを伴わない
    単なる変数の指数でも同じ理由（添字位置では文字が縮小されるため \\dfrac だと
    間延びする）で \\frac にすべき（TRIGGER_RE ベースの実装は \\int_0^{...} のような限られた形にしか
    反応せず、x^{...} のような一般の添字を検出できなかった）。
    そのため _/^ の直後が {...} であれば、直前が何であるかによらず
    無条件に添字位置とみなす（答案の TeX で _ と ^ は数式の添字演算子
    以外の用途では使われないため、一般化しても誤検知のリスクは低い）。

    同じ理由で、tikzpicture 内の node ラベルも例外にする。"""
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


MATH_VISUAL_LABEL_RE = re.compile(r'\\label\{[^}]*\}')
MATH_VISUAL_INVIS_RE = re.compile(
    r'\\(?:notag|nonumber|displaystyle|textstyle|scriptstyle|scriptscriptstyle)(?![a-zA-Z])'
)
MATH_VISUAL_DELIM_RE = re.compile(
    r'\\(?:left|right)\.|\\(?:left|right|Biggl|Biggr|biggl|biggr|Bigl|Bigr|bigl|bigr|Bigg|bigg|Big|big)[lrg]?(?![a-zA-Z])'
)
MATH_VISUAL_FRAC_RE = re.compile(r'\\(?:d|c)?frac(?![a-zA-Z])')
MATH_VISUAL_ACCENT_RE = re.compile(r'\\(?:overrightarrow|overline|underline|vec)(?![a-zA-Z])')
MATH_VISUAL_SQRT_RE = re.compile(r'\\sqrt(?:\[[^\]]*\])?\{([^}]*)\}')
MATH_VISUAL_QQUAD_RE = re.compile(r'\\qquad(?![a-zA-Z])')
MATH_VISUAL_QUAD_RE = re.compile(r'\\quad(?![a-zA-Z])')
MATH_VISUAL_THIN_RE = re.compile(r'\\[,;:! ]')
MATH_VISUAL_FN_RE = re.compile(
    r'\\(sin|cos|tan|cot|sec|csc|log|ln|lim|exp|det|min|max|sup|inf|gcd|deg|dim|hom|ker|arg|Pr|arcsin|arccos|arctan)(?![a-zA-Z])'
)
MATH_VISUAL_CMD_RE = re.compile(r'\\[a-zA-Z]+')


def estimate_math_visual_length(line):
    """align 等の数式行について、TeX コマンドの冗長性を除いた
    レンダリング後の推定表示横幅（文字数相当）を概算する。
    - % コメントや改行・配置記号（\\\\, &）を除去
    - \\label や \\notag などの非表示メタデータを除去
    - \\left / \\right / \\Bigl などの括弧サイズ修飾子を除去
    - \\dfrac{A}{B} などの分数は縦積みを考慮し max(幅(A), 幅(B)) + 1 で換算
    - \\overrightarrow{AB} や \\vec{a} は内容の幅で換算
    - \\sqrt{x} は 1 + 幅(x) で換算
    - \\alpha, \\times, \\cdot などの TeX 記号コマンドは 1 文字換算
    - \\sin, \\cos などの標準関数名はアルファベット文字数換算
    """
    s = re.sub(r'(?<!\\)%.*$', '', line).strip()
    if not s:
        return 0

    s = re.sub(r'\\\\$', '', s).strip()
    s = s.replace('&', '')

    s = MATH_VISUAL_LABEL_RE.sub('', s)
    s = MATH_VISUAL_INVIS_RE.sub('', s)
    s = MATH_VISUAL_DELIM_RE.sub('', s)

    # 分数 (\dfrac, \frac, \cfrac) を内側・先頭から順に抽出して推定幅プレースホルダーに置換
    res = []
    i = 0
    n = len(s)
    while i < n:
        m = MATH_VISUAL_FRAC_RE.search(s, i)
        if not m:
            res.append(s[i:])
            break
        res.append(s[i:m.start()])
        p1 = s.find('{', m.end())
        if p1 == -1 or s[m.end():p1].strip():
            res.append(s[m.start():m.end()])
            i = m.end()
            continue
        num, p2 = extract_braced(s, p1)
        p3 = s.find('{', p2)
        if p3 == -1 or s[p2:p3].strip():
            res.append(s[m.start():p2])
            i = p2
            continue
        den, p4 = extract_braced(s, p3)
        w_num = estimate_math_visual_length(num)
        w_den = estimate_math_visual_length(den)
        w_frac = max(w_num, w_den) + 1
        res.append('x' * w_frac)
        i = p4
    s = ''.join(res)

    # ベクトル・上線等の上乗せ記号 (\overrightarrow{AB} -> AB, \vec{a} -> a)
    res = []
    i = 0
    n = len(s)
    while i < n:
        m = MATH_VISUAL_ACCENT_RE.search(s, i)
        if not m:
            res.append(s[i:])
            break
        res.append(s[i:m.start()])
        p1 = s.find('{', m.end())
        if p1 == -1 or s[m.end():p1].strip():
            res.append(s[m.start():m.end()])
            i = m.end()
            continue
        inner, p2 = extract_braced(s, p1)
        res.append(inner)
        i = p2
    s = ''.join(res)

    s = MATH_VISUAL_SQRT_RE.sub(r'x\1', s)
    s = MATH_VISUAL_QQUAD_RE.sub('    ', s)
    s = MATH_VISUAL_QUAD_RE.sub('  ', s)
    s = MATH_VISUAL_THIN_RE.sub(' ', s)
    s = MATH_VISUAL_FN_RE.sub(r'\1', s)
    s = MATH_VISUAL_CMD_RE.sub('x', s)

    s = s.replace('{', '').replace('}', '')
    s = re.sub(r'\s+', ' ', s).strip()
    return len(s)


def check_long_align_lines(text):
    """align/align* 環境内で、1行の推定表示幅が長く（ALIGN_LINE_LENGTH_LIMIT 超）かつ
    '=' を複数個（ALIGN_LINE_MIN_EQUALS 個以上）含む行を警告する。
    AI文字起こしの結果、a=b=c=d=... のように = で全部つないだ1行になって
    いることが多く、\\\\ と &= で複数行に分けた方が読みやすい。ただし
    どこで区切るのが数式的に自然かは機械的には判断できない（\\left(...\\right)
    や \\substack{} 内の = まで割ってしまうと壊れる）ため、ここでは検出のみ
    行い、実際の改行挿入はエラーではなく警告として目視判断に委ねる。
    \\dfrac や \\label などの TeX コマンドでコード文字数が多くても紙面上の横幅が
    短い行を誤検知しないよう、estimate_math_visual_length で推定表示幅に換算して判定する。"""
    warnings = []
    for env_m in re.finditer(r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}', text, re.DOTALL):
        body_start = env_m.start(1)
        body = env_m.group(1)
        offset = 0
        for line in body.split('\n'):
            vis_len = estimate_math_visual_length(line)
            if vis_len > ALIGN_LINE_LENGTH_LIMIT and line.count('=') >= ALIGN_LINE_MIN_EQUALS:
                pos = body_start + offset
                warnings.append((line_of(text, pos),
                                  f"align 内の行が長く（推定表示幅{vis_len}文字、元{len(line)}文字）'=' が{line.count('=')}個ある。"
                                  "\\\\ と &= で複数行に分けた方が読みやすい可能性がある"))
            offset += len(line) + 1
    return warnings


LEFT_CMD_RE = re.compile(r'\\left(?![a-zA-Z])')
RIGHT_CMD_RE = re.compile(r'\\right(?![a-zA-Z])')


def check_left_right_balance(text):
    """align/align* 環境1ブロックまるごとの中で \\left と \\right の出現数が
    一致するかをチェックする。\\left[...\\right) のように \\left と \\right を
    書き間違えて片方だけ余分/不足になっていると、MathJax は "Missing \\left or
    extra \\right" エラーで丸ごと未レンダリングになる（2009年前期2番で発見）。
    array/matrix/cases 環境が \\left\\{ ... \\right. でネストされているとその
    内部に独自の \\\\ 行区切りがあり、行単位や \\\\ 区切り単位で数えると
    \\left...\\right のペアがその区切りをまたいでいるだけの正常なケースまで
    誤検知してしまう（実測で多数の誤検知が発生した）。align ブロック全体での
    合計比較であればネスト構造を気にせず安全に検出でき、誤検知を避けられる。
    行単位の粒度は失うが、実際に崩れている場合はブロック全体でも数が
    合わないことがほとんどのため実用上十分。"""
    errors = []
    for env_m in re.finditer(r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}', text, re.DOTALL):
        body = env_m.group(1)
        n_left = len(LEFT_CMD_RE.findall(body))
        n_right = len(RIGHT_CMD_RE.findall(body))
        if n_left != n_right:
            errors.append((line_of(text, env_m.start()),
                            f"align ブロック内で \\left が{n_left}個、\\right が{n_right}個で数が一致しない"))
    return errors


MATH_TEXT_CMD_RE = re.compile(
    r'\\(?:text|mbox|hbox|textbf|textit|textrm|textsf|texttt|textnormal|'
    r'mathrm|operatorname|tag|intertext|shortintertext|label|ref|cref|Cref|'
    r'eqref|hspace|vspace|phantom|hphantom|vphantom)\*?\s*\{'
)
MATH_NON_MATH_REGION_RE = re.compile(
    r'\\begin\{(verbatim\*?|Verbatim|lstlisting|minted|tikzpicture)\}'
    r'|\\verb\*?([^a-zA-Z\s])'
    r'|\\(?:url|path|href)\b'
)
MATH_DISPLAY_ENV_RE = re.compile(
    r'\\begin\{(align\*?|equation\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}',
    re.S,
)
MATH_STAR_CASES_RE = re.compile(
    r'\\begin\{(d?r?cases\*)\}(.*?)\\end\{\1\}',
    re.S,
)


def _blank_keep_newlines(buf, start, end):
    for k in range(start, end):
        if buf[k] != '\n':
            buf[k] = ' '


def _mask_non_math_regions(raw):
    """コメント・verbatim・TikZ・URL 等を改行を保ったまま空白化して返す。"""
    text = strip_comments(raw)
    out = list(text)
    pos = 0
    n = len(text)
    while pos < n:
        m = MATH_NON_MATH_REGION_RE.search(''.join(out), pos)
        if not m:
            break
        end = m.end()
        if m.group(1):
            env = m.group(1)
            closing = text.find('\\end{' + env + '}', end)
            end = n if closing < 0 else closing + len('\\end{' + env + '}')
        elif m.group(2):
            closing = text.find(m.group(2), end)
            end = n if closing < 0 else closing + 1
        else:
            while end < n and text[end].isspace():
                end += 1
            if end < n and text[end] == '{':
                _, end = extract_braced(text, end)
        _blank_keep_newlines(out, m.start(), end)
        pos = end
    return ''.join(out)


def _iter_math_blocks(raw):
    """本文中の数式ブロック (body_start_offset, body) を順に列挙する。
    \\begin{document} より前や TikZ・コメント・verbatim 内の $ は除外し、
    インライン $...$ 内の \\text{...$...$...} にあるネストした $ は波括弧深さでスキップする。"""
    text = _mask_non_math_regions(raw)
    start = text.find('\\begin{document}')
    start = 0 if start < 0 else start
    work = list(text)
    blocks = []

    for m in MATH_DISPLAY_ENV_RE.finditer(text, start):
        blocks.append((m.start(2), m.group(2)))
        _blank_keep_newlines(work, m.start(), m.end())

    cur = ''.join(work)
    for pat in (
        re.compile(r'\$\$(.*?)\$\$', re.S),
        re.compile(r'(?<!\\)\\\[(.*?)(?<!\\)\\\]', re.S),
        re.compile(r'(?<!\\)\\\((.*?)(?<!\\)\\\)', re.S),
    ):
        for m in pat.finditer(cur, start):
            blocks.append((m.start(1), m.group(1)))
            _blank_keep_newlines(work, m.start(), m.end())
        cur = ''.join(work)

    i = start
    n = len(cur)
    while i < n:
        if cur[i] == '\\' and i + 1 < n:
            i += 2
            continue
        if cur[i] == '$':
            j = i + 1
            depth = 0
            closed = False
            while j < n:
                ch = cur[j]
                if ch == '\\' and j + 1 < n:
                    j += 2
                    continue
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth = max(0, depth - 1)
                elif ch == '\n' and j + 1 < n and cur[j + 1] == '\n':
                    break
                elif ch == '$' and depth == 0:
                    blocks.append((i + 1, cur[i + 1:j]))
                    i = j + 1
                    closed = True
                    break
                j += 1
            if not closed:
                i += 1
            continue
        i += 1
    return blocks


def _strip_math_text_commands(body):
    """数式ブロック中の \\text{...}, \\mbox{...}, dcases* の2列目等を改行を保って空白化する。"""
    def blank_star_cases_col2(m):
        inner = m.group(2)
        rows = re.split(r'(\\\\(?:[ \t]*\[[^\]\n]*\])?)', inner)
        rebuilt = []
        for idx, part in enumerate(rows):
            if idx % 2 == 1:
                rebuilt.append(part)
                continue
            amp = part.find('&')
            if amp < 0:
                rebuilt.append(part)
            else:
                rebuilt.append(part[:amp + 1] + ''.join('\n' if c == '\n' else ' ' for c in part[amp + 1:]))
        return f"\\begin{{{m.group(1)}}}{''.join(rebuilt)}\\end{{{m.group(1)}}}"

    s = MATH_STAR_CASES_RE.sub(blank_star_cases_col2, body)
    out = []
    i = 0
    n = len(s)
    while i < n:
        m = MATH_TEXT_CMD_RE.match(s, i)
        if m:
            brace_idx = m.end() - 1
            _, end_idx = extract_braced(s, brace_idx)
            out.append(''.join('\n' if c == '\n' else ' ' for c in s[i:end_idx]))
            i = end_idx
        else:
            out.append(s[i])
            i += 1
    return ''.join(out)


def check_math_brackets(text):
    """数式中の ( ) と [ ] が片側だけ単体で入らないかチェックする（半開区間 (a,b]・[a,b) は許容）。"""
    errors = []
    for pos, body in _iter_math_blocks(text):
        cleaned = _strip_math_text_commands(body)
        c2 = re.sub(r'\\\\\*?[ \t]*\[[^\]\n]*\]', '', cleaned)
        c2 = re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^\]\n]*\])?', '', c2)
        c2 = re.sub(
            r'\\(?!left\b|right\b|big[lmr]?\b|Big[lmr]?\b|bigg[lmr]?\b|Bigg[lmr]?\b)'
            r'[a-zA-Z]+\*?\s*\[[^\]\n]*\]',
            '',
            c2,
        )
        c2 = re.sub(r'\\[()\[\]{}]', '', c2)
        op, cp = c2.count('('), c2.count(')')
        ob, cb = c2.count('['), c2.count(']')
        if (op + ob) != (cp + cb):
            errors.append((
                line_of(text, pos),
                f"数式内のカッコの対応が一致しない（'(' が{op}個, ')' が{cp}個, '[' が{ob}個, ']' が{cb}個）",
            ))
    return errors


def check_math_fullwidth(text):
    """数式中に（\\text 等を除いて）全角・非ASCII文字が混入していないかチェックする。"""
    errors = []
    for pos, body in _iter_math_blocks(text):
        cleaned = _strip_math_text_commands(body)
        m = re.search(r'[^\x00-\x7f]', cleaned)
        if m:
            ch = m.group(0)
            disp = '\\u3000(全角空白)' if ch == '\u3000' else f'「{ch}」'
            errors.append((
                line_of(text, pos + m.start()),
                f"数式内に \\text{{...}} 等を介さず全角文字 {disp} が入っている",
            ))
    return errors


PROSE_IN_MATH_CMD_RE = re.compile(
    r'\\(?:text|mbox|hbox|textbf|textit|textrm|textsf|texttt|textnormal|intertext|shortintertext)\*?\s*\{'
)
PROSE_NON_TEXT_CMD_RE = re.compile(
    r'\\(?:label|cref|Cref|ref|eqref|hspace|vspace|subfile|documentclass|includegraphics)\*?(?:\[[^\]\n]*\])?\s*\{'
)


def _extract_prose_text(raw):
    """数式・TikZ・コメント・verbatim・コマンド引数を除いた本文（\\caption や数式内 \\text 等は残す）を
    元の行番号を保って返す。"""
    text = _mask_non_math_regions(raw)
    prose = list(text)
    doc_start = text.find('\\begin{document}')
    if doc_start > 0:
        _blank_keep_newlines(prose, 0, doc_start)

    for pos, body in _iter_math_blocks(raw):
        end = pos + len(body)
        inner_kept = ['\n' if ch == '\n' else ' ' for ch in body]
        i = 0
        n = len(body)
        while i < n:
            m = PROSE_IN_MATH_CMD_RE.match(body, i)
            if m:
                brace_idx = m.end() - 1
                _, end_idx = extract_braced(body, brace_idx)
                seg = list(body[brace_idx + 1:end_idx - 1])
                seg_str = ''.join(seg)
                for dm in re.finditer(r'(?<!\\)\$(?:\\\$|[^$])+?(?<!\\)\$', seg_str):
                    _blank_keep_newlines(seg, dm.start(), dm.end())
                inner_kept[brace_idx + 1:end_idx - 1] = seg
                i = end_idx
            else:
                i += 1
        prose[pos:end] = inner_kept

    cur = ''.join(prose)
    for m in re.finditer(r'\\(?:begin|end)\{[^}]*\}(?:\[[^\]\n]*\])?', cur):
        _blank_keep_newlines(prose, m.start(), m.end())
    cur = ''.join(prose)
    for m in PROSE_NON_TEXT_CMD_RE.finditer(cur):
        _, end_idx = extract_braced(cur, m.end() - 1)
        _blank_keep_newlines(prose, m.start(), end_idx)
    return ''.join(prose)


def check_prose_brackets(text):
    """数式外の本文（\\caption や \\text 等を含む）で半角 ()・全角（）・「」・『』の対応をチェックする。"""
    prose = _extract_prose_text(text)
    errors = []
    for open_ch, close_ch in (('(', ')'), ('（', '）'), ('「', '」'), ('『', '』')):
        stack = []
        for idx, ch in enumerate(prose):
            if ch == open_ch:
                stack.append(idx)
            elif ch == close_ch:
                if stack:
                    stack.pop()
                else:
                    errors.append((
                        line_of(text, idx),
                        f"対応する「{open_ch}」のない「{close_ch}」がある",
                    ))
        for idx in stack:
            errors.append((
                line_of(text, idx),
                f"対応する「{close_ch}」のない「{open_ch}」がある",
            ))
    return errors


VEC_CMD_RE = re.compile(r'\\(vec|overrightarrow)(?![a-zA-Z])')
VEC_SINGLE_BASE_RE = re.compile(r'^(?:[a-zA-Z0-9]|\\[a-zA-Z]+)$')
VEC_SINGLE_WITH_MOD_RE = re.compile(
    r'^(?P<base>[a-zA-Z0-9]|\\[a-zA-Z]+)'
    r'(?P<mod>(?:\s*(?:\'+|[_^]\s*(?:\{[^{}]*\}|\\[a-zA-Z]+|[a-zA-Z0-9])))+)$'
)
VEC_FONT_WRAP_RE = re.compile(r'^\\(?:text|mathrm|mathbf|mathit|mathsf|mathtt)\s*\{')


def _unwrap_vec_font(arg):
    s = arg.strip()
    while True:
        m = VEC_FONT_WRAP_RE.match(s)
        if not m:
            break
        brace_idx = s.find('{')
        inner, end_idx = extract_braced(s, brace_idx)
        if end_idx == len(s):
            s = inner.strip()
        else:
            break
    return s


def check_vector_notation(text):
    """ベクトルの表記ルールをチェックする。
    - 1文字のベクトルは \\vec{a}（\\overrightarrow{a} は不可）
    - 2文字以上のベクトルは \\overrightarrow{AB}（\\vec{AB} は不可）
    - 1文字ベクトルの添字・プライムは \\vec{a}_1, \\vec{b}' のように外に出す
      （\\vec{a_1}, \\overrightarrow{a_1} 等は不可）
    """
    errors = []
    n = len(text)
    for m in VEC_CMD_RE.finditer(text):
        cmd = m.group(1)
        i = m.end()
        while i < n and text[i].isspace():
            i += 1
        if i >= n or text[i] != '{':
            # 裸の \vec a や \vec\ell は1文字対象なので許容
            continue
        arg, _ = extract_braced(text, i)
        unwrapped = _unwrap_vec_font(arg)
        if not unwrapped:
            continue
        lineno = line_of(text, m.start())
        if VEC_SINGLE_BASE_RE.match(unwrapped):
            if cmd == 'overrightarrow':
                errors.append((
                    lineno,
                    f"1文字のベクトルには \\overrightarrow ではなく \\vec を使う"
                    f"（\\overrightarrow{{{arg}}} → \\vec{{{arg}}}）",
                ))
        else:
            mod_m = VEC_SINGLE_WITH_MOD_RE.match(unwrapped)
            if mod_m:
                base = mod_m.group('base')
                mod = re.sub(r'\s+', '', mod_m.group('mod'))
                if cmd == 'vec':
                    errors.append((
                        lineno,
                        f"1文字ベクトルの添字・プライムは \\vec の外に出す"
                        f"（\\vec{{{arg}}} → \\vec{{{base}}}{mod}）",
                    ))
                else:
                    errors.append((
                        lineno,
                        f"1文字ベクトルの添字・プライムは \\overrightarrow ではなく \\vec を使い外に出す"
                        f"（\\overrightarrow{{{arg}}} → \\vec{{{base}}}{mod}）",
                    ))
            else:
                if cmd == 'vec':
                    errors.append((
                        lineno,
                        f"2文字以上のベクトルには \\vec ではなく \\overrightarrow を使う"
                        f"（\\vec{{{arg}}} → \\overrightarrow{{{arg}}}）",
                    ))
    return errors


def _find_vector_edits(text):
    edits = []
    n = len(text)
    for m in VEC_CMD_RE.finditer(text):
        cmd = m.group(1)
        i = m.end()
        while i < n and text[i].isspace():
            i += 1
        if i >= n or text[i] != '{':
            continue
        arg, end = extract_braced(text, i)
        unwrapped = _unwrap_vec_font(arg)
        if not unwrapped:
            continue
        if VEC_SINGLE_BASE_RE.match(unwrapped):
            if cmd == 'overrightarrow':
                edits.append((m.start(), m.end(), r'\vec'))
        else:
            mod_m = VEC_SINGLE_WITH_MOD_RE.match(unwrapped)
            if mod_m:
                if arg.strip() != unwrapped:
                    continue
                before = text[:m.start()].rstrip()
                if before and before[-1] in ('_', '^'):
                    continue
                after = text[end:].lstrip()
                base = mod_m.group('base')
                mod = re.sub(r'\s+', '', mod_m.group('mod'))
                if after:
                    if after[0] == '_' and '_' in mod:
                        continue
                    if after[0] in ('^', "'") and ('^' in mod or "'" in mod):
                        continue
                edits.append((m.start(), end, f"\\vec{{{base}}}{mod}"))
            else:
                if cmd == 'vec':
                    edits.append((m.start(), m.end(), r'\overrightarrow'))
    return edits


def _mask_protected_regions(raw):
    masked = list(strip_comments(raw))

    def protect(start, end):
        masked[start:end] = ' ' * (end - start)

    # Scan original text in order so commands inside verbatim/comments are ignored.
    token = re.compile(
        r'\\begin\{(verbatim\*?|Verbatim|lstlisting|minted)\}'
        r'|\\verb\*?([^a-zA-Z\s])'
        r'|\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand|def|gdef|edef|xdef)\b'
        r'|\\(?:url|path|href|label|ref|eqref|cref|Cref|input|include|includegraphics|texttt)\b')
    pos = 0
    while True:
        m = token.search(''.join(masked), pos)
        if not m:
            break
        end = m.end()
        if m.group(1):
            closing = raw.find('\\end{' + m.group(1) + '}', end)
            end = len(raw) if closing < 0 else closing + len('\\end{' + m.group(1) + '}')
        elif m.group(2):
            closing = raw.find(m.group(2), end)
            end = len(raw) if closing < 0 else closing + 1
        elif re.match(r'\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand|[egx]?def)\b', m.group()):
            # Conservatively keep whole definition lines, including multiline bodies.
            brace = raw.find('{', end)
            end = extract_braced(raw, brace)[1] if brace >= 0 else end
            # newcommand's first group can be the macro name; preserve its body too.
            if (not re.match(r'\\[egx]?def\b', m.group())
                    and raw[m.end():brace].strip() in ('', '*')):
                while end < len(raw) and raw[end].isspace():
                    end += 1
                while end < len(raw) and raw[end] == '[':
                    closing = raw.find(']', end)
                    if closing < 0:
                        end = len(raw)
                        break
                    end = closing + 1
                    while end < len(raw) and raw[end].isspace():
                        end += 1
                if end < len(raw) and raw[end] == '{':
                    end = extract_braced(raw, end)[1]
        else:
            while end < len(raw) and raw[end].isspace():
                end += 1
            if end < len(raw) and raw[end] == '[':
                closing = raw.find(']', end)
                end = len(raw) if closing < 0 else closing + 1
                while end < len(raw) and raw[end].isspace():
                    end += 1
            if end < len(raw) and raw[end] == '{':
                end = extract_braced(raw, end)[1]
        protect(m.start(), end)
        pos = end

    return ''.join(masked)


def fix_text(raw, extra_edit_finders=()):
    """Apply punctuation, bare-argument wrapping, fraction-style, vector-notation, reference-command, and equation-label fixes; preserve opaque TeX regions.

    extra_edit_finders: 利用先固有の機械的な修正（関数 (masked, raw) -> [(start, end, replacement)]）。
    汎用の修正のあと、参照・ラベルの正規化の前に順に適用する。"""
    if LINT_SKIP_RE.search(raw):
        return raw

    bare_edits = _find_bare_argument_edits(_mask_protected_regions(raw), raw)
    for start, end, replacement in sorted(bare_edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    text = _mask_protected_regions(raw)
    edits = [(m.start(), m.end(), {'。': '．', '、': '，'}[m.group()])
             for m in re.finditer('[。、]', text)]
    spans = find_frac_exempt_spans(text)
    for m in FRAC_CMD_RE.finditer(text):
        inside = any(a <= m.start() < b for a, b in spans)
        replacement = r'\frac' if inside else r'\dfrac'
        if m.group() != replacement:
            edits.append((m.start(), m.end(), replacement))
    for start, end, replacement in sorted(edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    # 和文に接する半角の「,」「.」を全角にする。直後の空白は全角の句読点に含まれるので詰める。
    masked = _mask_protected_regions(raw)
    punct_edits = []
    for m in _find_halfwidth_punct(masked):
        end = m.end()
        while end < len(raw) and raw[end] in ' \t':
            end += 1
        punct_edits.append((m.start(), end, {',': '，', '.': '．'}[m.group()]))
    for start, end, replacement in sorted(punct_edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    vec_edits = _find_vector_edits(_mask_protected_regions(raw))
    for start, end, replacement in sorted(vec_edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    tikz_circle_edits = _find_tikz_point_circle_edits(_mask_protected_regions(raw))
    for start, end, replacement in sorted(tikz_circle_edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    bracket_edits = _find_display_math_bracket_edits(_mask_protected_regions(raw), raw)
    for start, end, replacement in sorted(bracket_edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    dollar_edits = _find_display_math_dollar_edits(_mask_protected_regions(raw), raw)
    for start, end, replacement in sorted(dollar_edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    eq_edits = _find_equation_env_edits(_mask_protected_regions(raw))
    for start, end, replacement in sorted(eq_edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    break_edits = _find_trailing_align_break_edits(_mask_protected_regions(raw), raw)
    for start, end, replacement in sorted(break_edits, reverse=True):
        raw = raw[:start] + replacement + raw[end:]

    for find_edits in extra_edit_finders:
        edits = find_edits(_mask_protected_regions(raw), raw)
        for start, end, replacement in sorted(edits, reverse=True):
            raw = raw[:start] + replacement + raw[end:]

    raw = tex_references.normalize_reference_commands(raw)
    try:
        raw = tex_references.normalize_equation_labels(raw)
    except tex_references.AmbiguousLabelError:
        pass  # Keep duplicate definitions visible to the linter for manual repair.
    return raw


TIKZ_POINT_CIRCLE_MAX_PT = 3.5
TIKZ_PT_CIRCLE_RE = re.compile(
    r'\bcircle\s*(?:\(\s*([0-9.]+)\s*pt\s*\)|\[\s*radius\s*=\s*([0-9.]+)\s*pt\s*\])'
)
TIKZ_STYLE_KEYWORDS = {
    'thick', 'very thick', 'ultra thick', 'thin', 'very thin', 'ultra thin',
    'semithick', 'solid', 'dashed', 'dotted', 'fill', 'draw', 'tdplot_screen_coords',
}
TIKZ_POS_KEYWORDS = {
    'above', 'below', 'left', 'right',
    'above left', 'above right', 'below left', 'below right', 'center',
}


def _extract_paren(text, start):
    """text[start] == '(' 前提。ネストした () と {} を考慮して (中身, 終了直後index) を返す。"""
    depth_p = 0
    depth_b = 0
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        if c == '\\' and i + 1 < n:
            i += 2
            continue
        if c == '{':
            depth_b += 1
        elif c == '}':
            depth_b = max(0, depth_b - 1)
        elif depth_b == 0:
            if c == '(':
                depth_p += 1
            elif c == ')':
                depth_p -= 1
                if depth_p == 0:
                    return text[start + 1:i], i + 1
        i += 1
    return text[start + 1:], n


def _is_bare_tikz_color(tok):
    return (
        bool(tok)
        and '=' not in tok
        and tok not in TIKZ_STYLE_KEYWORDS
        and tok not in TIKZ_POS_KEYWORDS
    )


def check_tikz_point_circle(text):
    """tikzpicture 内で点を打つ目的の circle（半径が 3.5pt 以下の pt 指定）を検出し、
    \\node[circle, ...] の使用を促す。図形としての円（座標単位の circle (1), circle (\\r) 等）は除外する。"""
    errors = []
    for env_start, env_end in find_tikzpicture_spans(text):
        body = text[env_start:env_end]
        for m in TIKZ_PT_CIRCLE_RE.finditer(body):
            rad_str = m.group(1) or m.group(2)
            rad_val = float(rad_str)
            if 0 < rad_val <= TIKZ_POINT_CIRCLE_MAX_PT:
                pos = env_start + m.start()
                errors.append((
                    line_of(text, pos),
                    f"tikzpicture 内で点を打つときは circle ではなく \\node[circle, ...] を使う（{m.group(0)}）",
                ))
    return errors


def _convert_point_circle_stmt(stmt):
    m_cmd = re.match(r'^\\(fill|draw|filldraw)\b', stmt)
    if not m_cmd:
        return None
    cmd = m_cmd.group(1)
    i = m_cmd.end()
    n = len(stmt) - 1  # Exclude trailing ';'
    while i < n and stmt[i].isspace():
        i += 1
    opts = ''
    if i < n and stmt[i] == '[':
        opts, i = _extract_bracket(stmt, i)
    opts_list = [o.strip() for o in opts.split(',') if o.strip()]
    inherited_colors = [o for o in opts_list if _is_bare_tikz_color(o) and o != 'black']
    inherited_color = inherited_colors[-1] if inherited_colors else None

    items = []
    while i < n:
        while i < n and stmt[i].isspace():
            i += 1
        if i >= n:
            break
        if stmt[i] == '(':
            coord, i = _extract_paren(stmt, i)
            coord_str = f'({coord})'
        elif stmt[i] == '\\':
            m_mac = re.match(r'\\[a-zA-Z]+', stmt[i:])
            if not m_mac:
                return None
            coord_str = m_mac.group(0)
            i += len(coord_str)
        else:
            return None
        while i < n and stmt[i].isspace():
            i += 1
        m_cir = TIKZ_PT_CIRCLE_RE.match(stmt[i:])
        if not m_cir:
            return None
        rad_str = m_cir.group(1) or m_cir.group(2)
        if not (0 < float(rad_str) <= TIKZ_POINT_CIRCLE_MAX_PT):
            return None
        i += m_cir.end()
        nodes = []
        while True:
            while i < n and stmt[i].isspace():
                i += 1
            if stmt[i:i + 4] == 'node' and (i + 4 == n or not stmt[i + 4].isalpha()):
                i += 4
                n_opts = None
                n_name = None
                while i < n and stmt[i].isspace():
                    i += 1
                if i < n and stmt[i] == '[':
                    n_opts, i = _extract_bracket(stmt, i)
                while i < n and stmt[i].isspace():
                    i += 1
                if i < n and stmt[i] == '(':
                    n_name, i = _extract_paren(stmt, i)
                while i < n and stmt[i].isspace():
                    i += 1
                if i < n and stmt[i] == '[':
                    n_opts2, i = _extract_bracket(stmt, i)
                    n_opts = f'{n_opts}, {n_opts2}' if n_opts else n_opts2
                while i < n and stmt[i].isspace():
                    i += 1
                if i < n and stmt[i] == '{':
                    n_text, i = extract_braced(stmt, i)
                    nodes.append((n_opts, n_name, n_text))
                else:
                    return None
            else:
                break
        items.append((coord_str, rad_str, nodes))
    if not items:
        return None

    out_parts = []
    for coord_str, rad_str, nodes in items:
        if cmd in ('fill', 'filldraw'):
            if not opts_list or opts_list == ['black']:
                c_opts = ['circle', 'fill']
            elif len(opts_list) == 1 and _is_bare_tikz_color(opts_list[0]):
                c_opts = ['circle', f'fill={opts_list[0]}']
            else:
                has_fill = any(o == 'fill' or o.startswith('fill=') for o in opts_list)
                has_draw = any(o == 'draw' or o.startswith('draw=') for o in opts_list)
                c_opts = ['circle']
                if not has_fill:
                    c_opts.append('fill')
                if cmd == 'filldraw' and not has_draw:
                    c_opts.append('draw')
                c_opts.extend(opts_list)
        else:  # draw
            has_draw = any(o == 'draw' or o.startswith('draw=') for o in opts_list)
            c_opts = ['circle'] + ([] if has_draw else ['draw']) + opts_list
        c_opts.append(f'inner sep={rad_str}pt')
        c_opts_str = ', '.join(c_opts)
        out_parts.append(f'\\node[{c_opts_str}] at {coord_str} {{}};')
        for n_opts, n_name, n_text in nodes:
            n_opts_list = [o.strip() for o in (n_opts or '').split(',') if o.strip()]
            if inherited_color and not any(_is_bare_tikz_color(o) for o in n_opts_list):
                n_opts_list = [inherited_color] + n_opts_list
            n_opts_str = ', '.join(n_opts_list)
            opt_s = f'[{n_opts_str}]' if n_opts_str else ''
            name_s = f' ({n_name})' if n_name else ''
            out_parts.append(f'\\node{opt_s}{name_s} at {coord_str} {{{n_text}}};')
    return ' '.join(out_parts)


def _find_tikz_point_circle_edits(text):
    edits = []
    for env_start, env_end in find_tikzpicture_spans(text):
        body = text[env_start:env_end]
        for m_stmt in re.finditer(r'\\(fill|draw|filldraw)\b[^;]*;', body):
            stmt = m_stmt.group(0)
            if not TIKZ_PT_CIRCLE_RE.search(stmt):
                continue
            replacement = _convert_point_circle_stmt(stmt)
            if replacement is not None:
                edits.append((env_start + m_stmt.start(), env_start + m_stmt.end(), replacement))
    return edits


SPACING_CMD_RE = re.compile(
    r'\\(?:medskip|bigskip|smallskip|hfill|vfill|noindent|newline)(?![A-Za-z])'
    r'|\\(?:vspace|hspace)\*?\s*\{[^{}]*\}'
    r'|\\q?quad(?![A-Za-z])')
SPACING_PROTECT_RE = re.compile(
    r'\\begin\{(align\*?|equation\*?|gather\*?|multline\*?|cases|dcases|split|array|tabular|'
    r'pmatrix|bmatrix|matrix|numcases|subnumcases|figure|table|tikzpicture|minipage|subcaptionblock)\}'
    r'.*?\\end\{\1\}'
    r'|\$\$.*?\$\$|(?<!\\)\$(?:\\\$|[^$])+?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)'
    r'|\\underline\{(?:[^{}]|\{[^{}]*\})*\}',  # 空欄の下線 \underline{\hspace{..}} は可
    re.S)


def check_spacing_commands(text):
    """本文で余白・改行のためのコマンド（\\medskip・\\bigskip・\\smallskip・\\vspace・\\hspace・
    \\hfill・\\noindent・\\newline、数式の外の \\quad・\\qquad）を使わない。
    見出しの前後などの余白は文書側で一律に付ける。数式・図・表・TikZ の中と、
    空欄の下線（\\underline{\\hspace{..}}）は対象外。"""
    start = text.find('\\begin{document}')
    if start < 0:
        start = 0
    protected = [(m.start(), m.end()) for m in SPACING_PROTECT_RE.finditer(text, start)]
    errors = []
    for m in SPACING_CMD_RE.finditer(text, start):
        if any(a <= m.start() < b for a, b in protected):
            continue
        errors.append((line_of(text, m.start()),
                       f"余白・改行のコマンド {m.group(0)} は本文で使わない（数式・図・表の中は可）"))
    return errors


QED_MATH_RE = re.compile(
    r'\\begin\{(align\*?|equation\*?|gather\*?|multline\*?|split)\}.*?\\end\{\1\}'
    r'|\$\$.*?\$\$|(?<!\\)\$(?:\\\$|[^$])+?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)', re.S)
QED_FIGURE_RE = re.compile(r'\\begin\{(figure|tikzpicture)\}.*?\\end\{\1\}', re.S)
# 証明の終わりの記号として使われる書き方（文末の $\square$ も含む。四角形の \square ABCD は対象外）
QED_SYMBOL_RE = re.compile(r'\\(?:blacksquare|Box)(?![A-Za-z])|\$\s*\\square\s*\$[ \t\u3000]*$', re.M)


def check_qed_mark(text):
    """証明・解答の終わりは、数式の外の文末に \\qed と書く（記号はプリアンブルで ■ に統一）。
    \\qed は行の右端へ自動で寄せるので \\hfill は要らない。$\\blacksquare$・$\\Box$・
    文末の $\\square$ や、数式の中の \\qed（右に寄らない）は使わない。
    proof 環境は末尾に自動で \\qed を付けるので、\\end{proof} の直前にも書かない。
    図・TikZ の中の記号は対象外。"""
    start = text.find('\\begin{document}')
    if start < 0:
        start = 0
    figures = [(m.start(), m.end()) for m in QED_FIGURE_RE.finditer(text, start)]
    maths = [(m.start(), m.end()) for m in QED_MATH_RE.finditer(text, start)]

    def inside(spans, pos):
        return any(a <= pos < b for a, b in spans)

    errors = []
    for m in QED_SYMBOL_RE.finditer(text, start):
        if not inside(figures, m.start()):
            errors.append((line_of(text, m.start()),
                           f"証明の終わりは {m.group(0).strip()} ではなく，数式の外の文末に \\qed と書く"))
    for m in re.finditer(r'\\qed(?![A-Za-z])', text[start:]):
        pos = start + m.start()
        if inside(figures, pos):
            continue
        if inside(maths, pos):
            errors.append((line_of(text, pos), "\\qed は数式の中に書かず，数式の後の文末に書く"))
        elif re.match(r'\s*\\end\{proof\}', text[pos + 4:]):
            errors.append((line_of(text, pos), "proof 環境は末尾に自動で \\qed を付けるので，\\end{proof} の直前には書かない"))
    return errors


# ---------------------------------------------------------------------------
# 規約に合わせて追加した検査（2026-11-13）
# ---------------------------------------------------------------------------

def check_cases_env(text):
    """場合分けは dcases で書く（§N1.1）。既存原稿に多いので警告にする。"""
    return [(line_of(text, m.start()), "場合分けは cases ではなく dcases を使う（残す場合は中に \\displaystyle を補う）")
            for m in re.finditer(r'\\begin\{cases\}', text)]


def check_binom(text):
    """組合せは {}_nC_k で書き、\\binom 系は使わない（§N2.1）。"""
    return [(line_of(text, m.start()), f"{m.group()} は使わず，組合せは {{}}_nC_k の形で書く")
            for m in re.finditer(r'\\[dt]?binom(?![a-zA-Z])', text)]


def check_subfigure_env(text):
    """複数の図・表を並べるときは subfigure ではなく subcaptionblock を使う（figure §1.4）。"""
    return [(line_of(text, m.start()), "subfigure は使わず subcaptionblock を使う")
            for m in re.finditer(r'\\begin\{subfigure\}', text)]


def check_multicols_float(text):
    """2段組（multicols）の中の figure・table は [H] にする（figure §1.2）。段の中の浮動体は消えたりずれたりする。"""
    errors = []
    for block in re.finditer(r'\\begin\{multicols\*?\}.*?\\end\{multicols\*?\}', text, re.DOTALL):
        for m in re.finditer(r'\\begin\{(figure|table)\}(\[[^\]]*\])?', block.group()):
            if m.group(2) != '[H]':
                errors.append((line_of(text, block.start() + m.start()),
                               f"2段組（multicols）の中の {m.group(1)} は [H] にする"))
    return errors


ROTATED_ARROW_RE = re.compile(
    r'\\(?:rotatebox|raisebox)\s*(?:\[[^\]]*\])?\s*\{[^{}]*\}\s*\{\s*\$?\s*\\(?:curvearrow(?:right|left)|hook(?:right|left)arrow)')


def check_rotated_arrows(text):
    """増減表の凹凸を、既存の矢印を回したりずらしたりして書かない（§TB2.4）。"""
    return [(line_of(text, m.start()),
             "凹凸の矢印を \\rotatebox・\\raisebox で流用しない（\\carrowIncreaseConvex などを使う）")
            for m in ROTATED_ARROW_RE.finditer(text)]


def check_tdplot_placement(text):
    """3D の視点（\\tdplotsetmaincoords）は figure の中、\\begin{tikzpicture} の直前に書く（figure §7.1）。"""
    errors = []
    for m in re.finditer(r'\\tdplotsetmaincoords\s*\{[^}]*\}\s*\{[^}]*\}', text):
        before = text[:m.start()]
        inside = before.rfind('\\begin{figure}') > before.rfind('\\end{figure}')
        follows = re.match(r'\s*\\begin\{tikzpicture\}', text[m.end():]) is not None
        if not (inside and follows):
            errors.append((line_of(text, m.start()),
                           "\\tdplotsetmaincoords は figure の中，\\begin{tikzpicture} の直前に書く"))
    return errors


FIGURE_TODO_RE = re.compile(
    r'^[ \t]*%[ \t]*TODO[ \t]*(?::|：)+[ \t]*.*?(?:図|figure|概形|グラフ|TikZ|作図).*?$', re.MULTILINE | re.IGNORECASE)


def check_figure_todo_placement(raw):
    """作図の TODO は figure の中に書く（figure §1.5）。コメントを読むので、コメントを消す前の本文を渡す。"""
    warnings = []
    for m in FIGURE_TODO_RE.finditer(raw):
        before = raw[:m.start()]
        if not before.rfind('\\begin{figure}') > before.rfind('\\end{figure}'):
            warnings.append((line_of(raw, m.start()), "作図の TODO は figure の中に書く（図だけの差分を検証できるように）"))
    return warnings


LIGHT_GRAY_VALUE_RE = re.compile(r'^gray!(\d+)$')
LIGHT_GRAY_LINE_KEYS = ('draw', 'color', 'text', 'pattern color')


def _light_gray_items(opts, command):
    """TikZ のオプションから、線・文字・斜線パターンに使われた gray!N（N<=50。黒などとの混色は除く）を返す。"""
    found = []
    for item in opts.split(','):
        item = item.strip()
        key, _, value = item.partition('=')
        key, value = key.strip(), value.strip()
        if not value:
            if command in ('fill', 'filldraw'):
                continue  # \fill[gray!20] の色は塗りの色
            value, key = key, ''  # 色だけを書いた項目（\draw[gray!40] など）
        elif key not in LIGHT_GRAY_LINE_KEYS:
            continue  # fill などの塗りは対象外
        m = LIGHT_GRAY_VALUE_RE.match(value)
        if m and int(m.group(1)) <= 50:
            found.append(value)
    return found


def check_light_gray(text):
    """線・文字・斜線パターンに薄い灰色（gray!50 以下）を使わない（figure §3.2）。塗りは対象外。"""
    warnings = []
    for span_start, span_end in find_tikzpicture_spans(text):
        body = text[span_start:span_end]
        for m in re.finditer(r'\\(draw|node|path|fill|filldraw)\s*\[([^\]]*)\]', body):
            items = _light_gray_items(m.group(2), m.group(1))
            if items:
                warnings.append((line_of(text, span_start + m.start()),
                                 f"線・文字に薄い灰色 {items[0]} を使わない（gray!60!black 以上の濃さにする）"))
    return warnings


SMALL_COORD_CIRCLE_RE = re.compile(r'\\(?:fill|filldraw|draw)\b[^;]*?\bcircle\s*\(\s*(0?\.\d+|0)\s*\)')


def check_small_coordinate_circle(text):
    """点を座標単位の小さな circle（circle (0.05) など）で打たない（figure §4.1）。図形の円は対象外なので警告にする。"""
    warnings = []
    for span_start, span_end in find_tikzpicture_spans(text):
        body = text[span_start:span_end]
        for m in SMALL_COORD_CIRCLE_RE.finditer(body):
            if float(m.group(1)) < 0.15:
                warnings.append((line_of(text, span_start + m.start()),
                                 "点は circle パスではなく \\node[circle, ...] で打つ（座標単位の小さな円が見つかった）"))
    return warnings


def tag(results, section):
    """検査の結果に規約の節番号を付ける（例：[§N5.1]）。"""
    return [(line, f"{msg} [§{section}]") for line, msg in results]


def _tag_equation_references(results):
    return [(line, f"{msg} [§{'N10.2' if '連番' in msg else 'N10.3'}]") for line, msg in results]


class Profile:
    """利用先ごとの検査の設定。既定は汎用の検査だけを行う。

    利用先は派生クラスを作り、固有の検査・対象ファイル・修正を足す（例：local/lint_local.py）。
    """

    def default_targets(self):
        """引数なしで実行したときに検査するファイル。汎用の既定では、ファイルの指定を必須にする。"""
        return None

    def is_target(self, path):
        return path.suffix == '.tex'

    def label_context(self, path):
        """ラベルの参照先として一緒に読む本文（例：解答から参照する問題文）。コメントは除いて返す。"""
        return ''

    def body_rules_apply(self, path):
        """本文の書き方の検査（余白の命令・\\qed）をこのファイルに適用するか。"""
        return True

    def reference_errors(self, path, text, context):
        """lint-skip のファイルにも適用する、利用先固有のラベル・参照の検査。"""
        return []

    def errors(self, path, text):
        """利用先固有の検査（エラー）。"""
        return []

    def edit_finders(self):
        """利用先固有の機械的な修正。fix_text の extra_edit_finders に渡す。"""
        return ()

    def display_path(self, path):
        return path


def lint_file(path, profile=None):
    """1ファイルを検査し、(エラー, 警告, lint-skip の理由) を返す。
    指摘の末尾には規約の節番号を付ける（N：notation-rules、F：figure-rules、TB：table-rules、LN：local/notation）。"""
    profile = profile or Profile()
    raw = path.read_text(encoding='utf-8')
    skip_m = LINT_SKIP_RE.search(raw)
    text = strip_comments(raw)
    context = profile.label_context(path)
    reference_errors = tag(check_duplicate_labels(text), 'N10.4')
    reference_errors += profile.reference_errors(path, text, context)
    reference_errors += _tag_equation_references(check_equation_references(text, context))
    if skip_m:
        return reference_errors, [], skip_m.group(1).strip()
    errors = []
    errors += tag(check_align_star(text), 'N5.1')
    errors += tag(check_equation_env(text), 'N5.1')
    errors += tag(check_trailing_align_break(text), 'N5.3')
    errors += tag(check_display_math_brackets(text), 'N5.1')
    errors += tag(check_display_math_dollars(text), 'N5.1')
    errors += tag(check_punctuation(text), 'N4.1')
    errors += tag(check_bare_args(text), 'N6.2')
    errors += tag(check_figure_caption(text), 'F1.3')
    errors += tag(check_table_caption(text), 'TB1.2')
    errors += tag(check_tikz_nesting(text), 'F1.1')
    errors += tag(check_tabular_nesting(text), 'TB1.1')
    if profile.body_rules_apply(path):
        errors += tag(check_spacing_commands(text), 'N11.1')
        errors += tag(check_qed_mark(text), 'N3.1')
    errors += profile.errors(path, text)
    errors += reference_errors
    errors += tag(check_frac_subscript_rule(text), 'N6.1')
    errors += tag(check_left_right_balance(text), 'N7.2')
    errors += tag(check_math_brackets(text), 'N7.3')
    errors += tag(check_prose_brackets(text), 'N7.4')
    errors += tag(check_math_fullwidth(text), 'N12.1')
    errors += tag(check_vector_notation(text), 'N8.1')
    errors += tag(check_tikz_point_circle(text), 'F4.1')
    errors += tag(check_reference_commands(text), 'N10.1')
    errors += tag(check_binom(text), 'N2.1')
    errors += tag(check_subfigure_env(text), 'F1.4')
    errors += tag(check_multicols_float(text), 'F1.2')
    errors += tag(check_rotated_arrows(text), 'TB2.4')
    errors += tag(check_tdplot_placement(text), 'F7.1')
    warnings = tag(check_overline_warning(text), 'N9.1')
    warnings += tag(check_long_align_lines(text), 'N5.4')
    warnings += tag(check_cases_env(text), 'N1.1')
    warnings += tag(check_figure_todo_placement(raw), 'F1.5')
    warnings += tag(check_light_gray(text), 'F3.2')
    warnings += tag(check_small_coordinate_circle(text), 'F4.1')
    return errors, warnings, None


def load_profile(path):
    """--rules で渡されたファイルを読み込み、その PROFILE を返す。"""
    spec = importlib.util.spec_from_file_location('_math_solution_tex_rules', Path(path).resolve())
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.PROFILE


def main(argv=None, profile=None, description=__doc__):
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--fix', action='store_true', help='Apply mechanical style fixes, then lint')
    mode.add_argument('--diff', action='store_true', help='Preview mechanical fixes without writing')
    if profile is None:
        parser.add_argument('--rules', help='利用先固有の検査を書いたモジュール（PROFILE を定義する .py）')
    parser.add_argument('files', nargs='*')
    args = parser.parse_args(argv)
    if profile is None:
        profile = load_profile(args.rules) if args.rules else Profile()
    if (args.fix or args.diff) and not args.files:
        parser.error('--fix/--diff requires explicit file paths')
    if args.files:
        targets = sorted(set(Path(p).resolve() for p in args.files))
    else:
        targets = profile.default_targets()
        if targets is None:
            parser.error('検査するファイルを指定する')
    for path in targets:
        if not path.is_file():
            parser.error(f'file not found: {path}')
    differences = False
    total_errors = 0
    total_warnings = 0
    files_checked = 0
    files_skipped = 0
    for path in targets:
        if not profile.is_target(path):
            continue
        if args.fix or args.diff:
            with path.open(encoding='utf-8', newline='') as stream:
                original = stream.read()
            fixed = fix_text(original, profile.edit_finders())
            if original != fixed:
                differences = True
                if args.diff:
                    print(''.join(difflib.unified_diff(
                        original.splitlines(keepends=True), fixed.splitlines(keepends=True),
                        fromfile=str(path), tofile=str(path))), end='')
                else:
                    with path.open('w', encoding='utf-8', newline='') as stream:
                        stream.write(fixed)
                    print(f'Fixed: {path}')
        files_checked += 1
        errors, warnings, skip_reason = lint_file(path, profile)
        rel = profile.display_path(path)
        if skip_reason is not None:
            files_skipped += 1
            print(f"::notice file={rel}::lint-skip: {skip_reason}")
        for lineno, msg in sorted(errors):
            print(f"::error file={rel},line={lineno}::{msg}")
            total_errors += 1
        for lineno, msg in sorted(warnings):
            print(f"::warning file={rel},line={lineno}::{msg}")
            total_warnings += 1

    skipped_note = f"（うち lint-skip {files_skipped} 件）" if files_skipped else ""
    print(f"\n{files_checked} 個の .tex を走査{skipped_note}。エラー {total_errors} 件、警告 {total_warnings} 件。")
    if total_errors > 0 or (args.diff and differences):
        sys.exit(1)


if __name__ == '__main__':
    main()
