import os
import subprocess
import sys
from pathlib import Path

from scratch import lint_latex_style as lint


def test_cli_starts_without_pythonpath(tmp_path):
    environment = os.environ.copy()
    environment.pop('PYTHONPATH', None)
    script = Path(lint.__file__).resolve()
    result = subprocess.run([sys.executable, str(script), '--help'], cwd=tmp_path,
                            env=environment, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_safe_fixes_and_idempotence():
    source = r'本文、です。 $\frac{1}{2}+x^{\dfrac{1}{2}}$' + '\n' + r'\begin{tikzpicture}\node {$\dfrac{a}{b}$};\end{tikzpicture}'
    expected = r'本文，です． $\dfrac{1}{2}+x^{\frac{1}{2}}$' + '\n' + r'\begin{tikzpicture}\node {$\frac{a}{b}$};\end{tikzpicture}'
    assert lint.fix_text(source) == expected
    assert lint.fix_text(expected) == expected


def test_protected_regions_and_skip():
    protected = r'''% コメント、。
\url{https://example.org/、。}
\href{https://example.org/。}{リンク。}
\verb|、。\frac{1}{2}|
\begin{verbatim}、。\frac{1}{2}\end{verbatim}
\newcommand{\foo}{、。\frac{1}{2}}
\label{eq:、。}
\input{dir/、。.tex}
'''
    assert lint.fix_text(protected) == protected.replace('リンク。', 'リンク．').replace(r'\label{eq:、。}', r'\label{eq:1}')
    skipped = '% lint-skip: legacy\n本文。'
    assert lint.fix_text(skipped) == skipped


def test_structural_errors_are_not_fixed():
    source = r'\begin{align*}\left(x\end{align*}\label{a}\label{a}\dfrac(1-a)(1-b)'
    assert lint.fix_text(source) == source


def test_cli_diff_fix_and_remaining_errors(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_text('本文。\n', encoding='utf-8')
    script = str(Path(lint.__file__).resolve())
    def run(*args):
        return subprocess.run([sys.executable, script, *args, str(source)], capture_output=True, text=True)
    preview = run('--diff')
    assert preview.returncode == 1
    assert '-本文。' in preview.stdout and '+本文．' in preview.stdout
    assert source.read_text() == '本文。\n'
    assert run('--fix').returncode == 0
    assert source.read_text() == '本文．\n'
    assert run('--fix').returncode == 0
    source.write_text(r'\dfrac(1-a)(1-b)。', encoding='utf-8')
    assert run('--fix').returncode == 1
    assert source.read_text() == r'\dfrac(1-a)(1-b)．'


def test_fix_requires_explicit_targets():
    result = subprocess.run([sys.executable, lint.__file__, '--fix'], capture_output=True, text=True)
    assert result.returncode == 2


def test_multiline_definitions_and_literal_code_are_preserved():
    source = r'''\newcommand\foo{本文。
\frac{1}{2}} {本文。}
\newcommand{\bar}[1]{本文。
\frac{#1}{2}}
\def\baz#1{本文。\frac{#1}{2}}
\begin{minted}{tex}
本文。\frac{1}{2}
\end{minted}
'''
    assert lint.fix_text(source) == source.replace('{本文。}', '{本文．}')


def test_cli_preserves_crlf(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_bytes('本文。\r\n次。\r\n'.encode())
    result = subprocess.run([sys.executable, lint.__file__, '--fix', str(source)], capture_output=True)
    assert result.returncode == 0
    assert source.read_bytes() == '本文．\r\n次．\r\n'.encode()


def test_equation_labels_must_be_local_numbered_and_references_defined(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_text(r'\label{2004-2:eq:1} \cref{2004-2:eq:1,eq:missing}', encoding='utf-8')
    errors, _, _ = lint.lint_file(source)
    messages = [message for _, message in errors]
    assert any('eq:1' in message and '形式' in message for message in messages)
    assert any('eq:missing' in message and '未定義' in message for message in messages)


def test_equation_fix_updates_refs_but_leaves_ambiguous_duplicates(tmp_path):
    source = r'\label{2004-2:eq:3} \cref{2004-2:eq:3} \label{eq:7} \eqref{eq:7}'
    fixed = lint.fix_text(source)
    assert fixed == r'\label{eq:1} \cref{eq:1} \label{eq:2} \cref{eq:2}'
    duplicate = r'\label{eq:1} \label{eq:1} \cref{eq:1}'
    assert lint.fix_text(duplicate) == duplicate
    path = tmp_path / 'solution.tex'
    path.write_text(duplicate, encoding='utf-8')
    errors, _, _ = lint.lint_file(path)
    assert any('重複' in message for _, message in errors)


def test_reference_commands_rule(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_text(
        r'\documentclass[../../main.tex]{subfiles}' + '\n'
        r'\begin{document}' + '\n'
        r'{\bf [解答]}' + '\n'
        r'\begin{align} x = 1 \label{eq:1} \end{align}' + '\n'
        r'\begin{figure}\begin{tikzpicture}\node {A};\end{tikzpicture}\caption{T}\label{fig:1}\end{figure}' + '\n'
        r'式\eqref{eq:1}と図\ref{fig:1}より，また\cref{eq:1}より．' + '\n'
        r'\end{document}' + '\n',
        encoding='utf-8')
    errors, _, _ = lint.lint_file(source)
    messages = [msg for _, msg in errors]
    assert any(r'\eqref' in msg and r'\cref' in msg for msg in messages)
    assert any(r'\ref' in msg and r'\cref' in msg for msg in messages)
    assert not any(r'未定義' in msg for msg in messages)

    fixed = lint.fix_text(source.read_text(encoding='utf-8'))
    assert r'\eqref' not in fixed
    assert r'\ref{' not in fixed
    assert r'式\cref{eq:1}と図\cref{fig:1}より，また\cref{eq:1}より．' in fixed

    source.write_text(fixed, encoding='utf-8')
    clean_errors, _, _ = lint.lint_file(source)
    assert not any('参照には' in msg for _, msg in clean_errors)



def test_math_environment_rejects_untyped_label(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_text(r'\begin{align}x=1\label{1}\end{align} \cref{1}', encoding='utf-8')
    errors, _, _ = lint.lint_file(source)
    assert any('eq:1' in message and '形式' in message for _, message in errors)


def test_trailing_break_before_end_align_rejected_and_fixed():
    # Issue #1414: \end{align} 直前の \\ は空の式番号を作る
    source = r'''
\begin{align}
  x &= 1 \\
  y &= 2 \\
\end{align}
\begin{align}
  z = 3 \\[2pt] % コメント
\end{align}
\begin{align}
  a = 1 \\
  \label{eq:9}
\end{align}
\begin{align}
  b = 1 \\
  c = 2
\end{align}
'''
    errors = lint.check_trailing_align_break(lint.strip_comments(source))
    assert [line for line, _ in errors] == [4, 7, 10]

    fixed = lint.fix_text(source)
    assert r'y &= 2' + '\n' + r'\end{align}' in fixed
    assert r'z = 3 % コメント' in fixed
    # \label を挟む場合は番号の意味が変わるため自動修正しない
    assert r'a = 1 \\' in fixed
    # 行の途中の \\ は変更しない
    assert r'b = 1 \\' in fixed
    assert [line for line, _ in lint.check_trailing_align_break(lint.strip_comments(fixed))] == [10]
    assert lint.fix_text(fixed) == fixed


def test_equation_environment_rejected_and_fixed(tmp_path):
    source = r'''
\begin{equation}
  x = 1 \label{eq:1}
\end{equation}
\begin{equation*}
  y = 2
\end{equation*}
% コメント内の \begin{equation} は無視
'''
    errors = lint.check_equation_env(lint.strip_comments(source))
    assert len(errors) == 4
    assert any('equation は使わない' in msg for _, msg in errors)
    assert any('equation* は使わない' in msg for _, msg in errors)

    fixed = lint.fix_text(source)
    assert r'\begin{align}' in fixed
    assert r'\end{align}' in fixed
    assert r'\begin{equation}' not in lint.strip_comments(fixed)
    assert r'\begin{equation*}' not in fixed
    assert r'% コメント内の \begin{equation} は無視' in fixed
    assert lint.check_equation_env(lint.strip_comments(fixed)) == []
    assert lint.fix_text(fixed) == fixed

    # CLI --fix でも正しく修正されること
    doc = tmp_path / 'solution.tex'
    doc.write_text('\\documentclass[../../main.tex]{subfiles}\n\\begin{document}\n\\begin{equation}x=1\\label{eq:1}\\end{equation}\n\\end{document}\n', encoding='utf-8')
    errs, _, _ = lint.lint_file(doc)
    assert any('equation は使わない' in msg for _, msg in errs)
    res = subprocess.run([sys.executable, lint.__file__, '--fix', str(doc)], capture_output=True, text=True)
    assert res.returncode == 0
    assert r'\begin{align}' in doc.read_text(encoding='utf-8')
    errs_after, _, _ = lint.lint_file(doc)
    assert not any('equation は使わない' in msg for _, msg in errs_after)


def test_same_label_in_problem_and_solution_is_duplicate(tmp_path):
    (tmp_path / 'problem.tex').write_text(r'\label{fig:a}', encoding='utf-8')
    solution = tmp_path / 'solution.tex'
    solution.write_text(r'\label{fig:a}', encoding='utf-8')
    errors, _, _ = lint.lint_file(solution)
    assert any('fig:a' in message and '重複' in message for _, message in errors)


def test_legacy_style_skip_does_not_hide_broken_references(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_text('% lint-skip: legacy\n' + r'\begin{align*}x=1\label{old}\end{align*} \cref{missing}', encoding='utf-8')
    errors, _, reason = lint.lint_file(source)
    assert reason == 'legacy'
    assert any('old' in message and '形式' in message for _, message in errors)
    assert any('missing' in message and '未定義' in message for _, message in errors)
    assert not any('align* は使わない' in message for _, message in errors)


def test_tabular_inside_tikzpicture_is_not_required_to_have_table():
    source = r'''
\begin{figure}
  \begin{tikzpicture}
    \node {\begin{tabular}{c}A\\B\end{tabular}};
  \end{tikzpicture}
  \caption{State diagram}
\end{figure}
'''
    assert lint.check_tabular_nesting(source) == []


def test_tabular_outside_tikzpicture_still_requires_table():
    source = r'''
\begin{figure}
  \begin{tikzpicture}\node {A};\end{tikzpicture}
  \begin{tabular}{c}B\end{tabular}
\end{figure}
'''
    errors = lint.check_tabular_nesting(source)
    assert len(errors) == 1
    assert errors[0][0] == 4


def test_vector_notation_rule(tmp_path):
    valid = (
        r'\vec{a} + \vec{0} + \vec{A} + \vec{\ell} + \vec{\alpha} + \vec a + \vec\ell '
        r'+ \vec{a}_1 + \vec{e}_k + \vec{b}\x27 + \vec{P}_{n-1} '
        r'+ \overrightarrow{AB} + \overrightarrow{OP_n} + \overrightarrow{P_{n-1}P_n} '
        r'+ \overrightarrow{P_1(t)P_2(t)} + \overrightarrow{\mathrm{OA}}'
    ).replace(r'\x27', "'")
    assert lint.check_vector_notation(valid) == []

    # 2文字以上に \vec を使っている違反
    err_multi_vec = lint.check_vector_notation(r'\vec{AB} + \vec{OP_n} + \vec{\text{PQ}}')
    assert len(err_multi_vec) == 3
    assert all(r'\overrightarrow' in msg for _, msg in err_multi_vec)

    # 1文字に \overrightarrow を使っている違反
    err_single_ora = lint.check_vector_notation(r'\overrightarrow{a} + \overrightarrow{A} + \overrightarrow{0} + \overrightarrow{\ell}')
    assert len(err_single_ora) == 4
    assert all(r'\vec' in msg for _, msg in err_single_ora)

    # 添字・プライム付き1文字ベクトルで添字が中括弧内に入っている違反
    err_sub_vec = lint.check_vector_notation(r"\vec{a_1} + \vec{b'} + \vec{a_{k+1}}")
    assert len(err_sub_vec) == 3
    assert any(r'\vec{a}_1' in msg for _, msg in err_sub_vec)
    assert any(r"\vec{b}'" in msg for _, msg in err_sub_vec)
    assert any(r'\vec{a}_{k+1}' in msg for _, msg in err_sub_vec)

    err_sub_ora = lint.check_vector_notation(r"\overrightarrow{a_1} + \overrightarrow{P_{n-1}} + \overrightarrow{b'}")
    assert len(err_sub_ora) == 3
    assert any(r'\vec{a}_1' in msg for _, msg in err_sub_ora)
    assert any(r'\vec{P}_{n-1}' in msg for _, msg in err_sub_ora)
    assert any(r"\vec{b}'" in msg for _, msg in err_sub_ora)

    # lint_file 経由でもエラーとして検出されること
    doc = tmp_path / 'solution.tex'
    doc.write_text('\\documentclass[../../main.tex]{subfiles}\n\\begin{document}\n$\\vec{AB} + \\overrightarrow{a_1}$\n\\end{document}\n', encoding='utf-8')
    errors, _, _ = lint.lint_file(doc)
    assert len(errors) == 2

    # fix_text（--fix）で自動書き換えされること（コメント・マクロ定義内は保護）
    src_to_fix = (
        r'$\vec{AB} + \vec{OP_n} + \vec{\text{PQ}} + \overrightarrow{a} + \overrightarrow{\ell} '
        r"+ \vec{a_1} + \vec{b'} + \overrightarrow{P_{n-1}}$"
        '\n'
        r'\newcommand{\myvec}{\vec{AB}}'
        '\n'
        r'% \vec{AB} \overrightarrow{a_1}'
    )
    expected_fixed = (
        r'$\overrightarrow{AB} + \overrightarrow{OP_n} + \overrightarrow{\text{PQ}} + \vec{a} + \vec{\ell} '
        r"+ \vec{a}_1 + \vec{b}' + \vec{P}_{n-1}$"
        '\n'
        r'\newcommand{\myvec}{\vec{AB}}'
        '\n'
        r'% \vec{AB} \overrightarrow{a_1}'
    )
    assert lint.fix_text(src_to_fix) == expected_fixed


def test_tikz_point_circle_rule(tmp_path):
    # 図形としての円（座標単位の circle (1), circle (\r), circle[radius=1], 4pt以上の玉など）は許容
    valid_tikz = r'''
\begin{tikzpicture}[xscale=1.4, yscale=0.25]
  \draw (0, 0) circle (1);
  \draw[thick, blue!80!black] (O) circle (\r);
  \fill[gray!20] (0, 0) circle (1.5);
  \draw (0, 0) circle[radius=1];
  \fill[red!80!black] (0.5, 0.45) circle (7pt) node[white] {赤};
  \node[circle, fill, inner sep=1.5pt] at (P) {};
  \node[circle, draw=blue!80!black, thick, fill=white, inner sep=1.8pt] at (A) {};
\end{tikzpicture}
'''
    assert lint.check_tikz_point_circle(valid_tikz) == []
    assert lint.fix_text(valid_tikz) == valid_tikz

    # 点を打つ目的の circle（半径 <= 3.5pt）はエラーとして検出され、fix_text で \node[circle, ...] に変換される
    invalid_tikz = r'''
\begin{tikzpicture}[xscale=1.4, yscale=0.25]
  \draw (0, 0) circle (1);
  \fill (-3, -18) circle (2pt);
  \fill[black] (1, -2) circle (1.5pt);
  \fill[red!85!black] (P) circle (1.4pt) node[above right=2pt] {$P(p,q)$};
  \draw[thick, blue!80!black, fill=white] (A) circle (1.8pt);
  \fill[red!75!black] (P1) circle (1.5pt) (P2) circle (1.5pt);
\end{tikzpicture}
'''
    errors = lint.check_tikz_point_circle(invalid_tikz)
    assert len(errors) == 6

    fixed = lint.fix_text(invalid_tikz)
    assert lint.check_tikz_point_circle(fixed) == []
    assert r'\draw (0, 0) circle (1);' in fixed
    assert r'\node[circle, fill, inner sep=2pt] at (-3, -18) {};' in fixed
    assert r'\node[circle, fill, inner sep=1.5pt] at (1, -2) {};' in fixed
    assert (
        r'\node[circle, fill=red!85!black, inner sep=1.4pt] at (P) {}; '
        r'\node[red!85!black, above right=2pt] at (P) {$P(p,q)$};'
    ) in fixed
    assert r'\node[circle, draw, thick, blue!80!black, fill=white, inner sep=1.8pt] at (A) {};' in fixed
    assert (
        r'\node[circle, fill=red!75!black, inner sep=1.5pt] at (P1) {}; '
        r'\node[circle, fill=red!75!black, inner sep=1.5pt] at (P2) {};'
    ) in fixed


def test_display_math_brackets_rule(tmp_path):
    # 改行幅指定 \\[2pt] は \[ として誤検知しないこと
    valid = (
        '\\begin{align}\n'
        '  a &= b \\\\[2pt]\n'
        '  &= c\n'
        '\\end{align}\n'
    )
    assert lint.check_display_math_brackets(valid) == []
    assert lint.fix_text(valid) == valid

    # 単一行 \[ ... \]、複数行 \[ ... \]、\[ \begin{aligned} ... \end{aligned} \] の検出と自動修正
    src = (
        '  \\[ f(x) = x^2 \\]\n'
        '\\[\n'
        '  g(x) = x + 1\n'
        '\\]\n'
        '\\[\n'
        '  \\begin{aligned}\n'
        '    h(x) &= f(x) + g(x) \\\\\n'
        '    &= x^2 + x + 1\n'
        '  \\end{aligned}\n'
        '\\]\n'
    )
    errors = lint.check_display_math_brackets(src)
    assert len(errors) == 6  # \[ と \] が3組で6件

    fixed = lint.fix_text(src)
    assert lint.check_display_math_brackets(fixed) == []
    expected = (
        '  \\begin{align}\n'
        '    f(x) = x^2\n'
        '  \\end{align}\n'
        '\\begin{align}\n'
        '  g(x) = x + 1\n'
        '\\end{align}\n'
        '\\begin{align}\n'
        '    h(x) &= f(x) + g(x) \\\\\n'
        '    &= x^2 + x + 1\n'
        '\\end{align}\n'
    )
    assert fixed == expected


def test_display_math_dollars_rule(tmp_path):
    # インライン数式 $...$ やエスケープ \$ は誤検知しないこと
    valid = (
        'これは $x = 1$ と $y = 2$ の例であり，\\$100 である．\n'
        '$\\Longleftrightarrow$$y=f(p)$ もインライン数式同士なので誤検知しない．\n'
        '\\begin{align}\n'
        '  a &= b\n'
        '\\end{align}\n'
    )
    assert lint.check_display_math_dollars(valid) == []
    assert lint.fix_text(valid) == valid

    # コメントアウト内の $$ は誤検知しないこと
    comment_src = '% $$ x = 1 $$\n'
    assert lint.check_display_math_dollars(comment_src) == []

    # 単一行 $$ ... $$、連続行 $$ ... $$、複数行 $$ ... $$、$$ \begin{aligned} ... \end{aligned} $$ の検出と自動修正
    src = (
        '  $$ f(x) = x^2 $$\n'
        '$$ a = 1 $$\n'
        '$$ b = 2 $$\n'
        '$$\n'
        '  g(x) = x + 1\n'
        '$$\n'
        '$$\n'
        '  \\begin{aligned}\n'
        '    h(x) &= f(x) + g(x) \\\\\n'
        '    &= x^2 + x + 1\n'
        '  \\end{aligned}\n'
        '$$\n'
    )
    errors = lint.check_display_math_dollars(src)
    assert len(errors) == 10  # 5組の $$ ... $$ で10件

    fixed = lint.fix_text(src)
    assert lint.check_display_math_dollars(fixed) == []
    expected = (
        '  \\begin{align}\n'
        '    f(x) = x^2\n'
        '  \\end{align}\n'
        '\\begin{align}\n'
        '  a = 1\n'
        '\\end{align}\n'
        '\\begin{align}\n'
        '  b = 2\n'
        '\\end{align}\n'
        '\\begin{align}\n'
        '  g(x) = x + 1\n'
        '\\end{align}\n'
        '\\begin{align}\n'
        '    h(x) &= f(x) + g(x) \\\\\n'
        '    &= x^2 + x + 1\n'
        '\\end{align}\n'
    )
    assert fixed == expected

    # 文中埋め込みの $$ ... $$
    inline_display = '前$$ x = 1 $$後\n'
    assert len(lint.check_display_math_dollars(inline_display)) == 2
    fixed_inline = lint.fix_text(inline_display)
    expected_inline = (
        '前\n'
        '\\begin{align}\n'
        '  x = 1\n'
        '\\end{align}\n'
        '後\n'
    )
    assert fixed_inline == expected_inline


def test_solution_headings_rule():
    # 1解法 + 1別解 + 解説（文中参照の [解]では は誤検知しない）
    src_two = (
        '[\\textbf{解}] 最初の解法．\n'
        '\\noindent{\\bf [解2]}\n'
        '[解]では座標を用いたが，ここでは幾何的に示す．\n'
        '\\noindent{\\bf [注]}\n'
        '補足説明．\n'
    )
    errors = lint.check_solution_headings(src_two)
    assert len(errors) == 3
    fixed_two = lint.fix_text(src_two)
    assert lint.check_solution_headings(fixed_two) == []
    assert fixed_two == (
        '{\\bf [解答]} 最初の解法．\n'
        '\\noindent{\\bf [別解]}\n'
        '[解]では座標を用いたが，ここでは幾何的に示す．\n'
        '\\noindent{\\bf [解説]}\n'
        '補足説明．\n'
    )

    # 1解法 + 複数別解（[別解1], [別解2]）および全角括弧［解］直後のスペース挿入
    src_three = (
        '［解1］解法1．\n'
        '[解2] 解法2．\n'
        '[解3] 解法3．\n'
    )
    fixed_three = lint.fix_text(src_three)
    assert lint.check_solution_headings(fixed_three) == []
    assert fixed_three == (
        '{\\bf [解答]} 解法1．\n'
        '{\\bf [別解1]} 解法2．\n'
        '{\\bf [別解2]} 解法3．\n'
    )


def test_bare_arguments_fix_and_lint():
    # \sqrt bare arguments
    assert lint.fix_text(r'$\sqrt2$') == r'$\sqrt{2}$'
    assert lint.fix_text(r'$\sqrt 2$') == r'$\sqrt{2}$'
    assert lint.fix_text(r'$\sqrt2a$') == r'$\sqrt{2}a$'
    assert lint.fix_text(r'$\sqrt[3]2$') == r'$\sqrt[3]{2}$'
    assert lint.fix_text(r'$\sqrt[3]{2}$') == r'$\sqrt[3]{2}$'
    assert lint.fix_text(r'$\sqrt[3] 2$') == r'$\sqrt[3]{2}$'
    assert lint.fix_text(r'$\sqrt\pi$') == r'$\sqrt{\pi}$'
    assert lint.fix_text(r'$\sqrt\beta$') == r'$\sqrt{\beta}$'

    # \frac / \dfrac bare arguments (display math -> \dfrac)
    assert lint.fix_text(r'\begin{align}\frac12\end{align}') == r'\begin{align}\dfrac{1}{2}\end{align}'
    assert lint.fix_text(r'\begin{align}\frac 1 2\end{align}') == r'\begin{align}\dfrac{1}{2}\end{align}'
    assert lint.fix_text(r'\begin{align}\frac 1{2}\end{align}') == r'\begin{align}\dfrac{1}{2}\end{align}'
    assert lint.fix_text(r'\begin{align}\frac{1} 2\end{align}') == r'\begin{align}\dfrac{1}{2}\end{align}'
    assert lint.fix_text(r'\begin{align}\frac\pi2\end{align}') == r'\begin{align}\dfrac{\pi}{2}\end{align}'
    assert lint.fix_text(r'\begin{align}\frac1\pi\end{align}') == r'\begin{align}\dfrac{1}{\pi}\end{align}'
    assert lint.fix_text(r'\begin{align}\frac\alpha\beta\end{align}') == r'\begin{align}\dfrac{\alpha}{\beta}\end{align}'

    # Exempt spans (inline exponent remains \frac)
    assert lint.fix_text(r'$x^{\frac12}$') == r'$x^{\frac{1}{2}}$'
    assert lint.fix_text(r'$x^{\dfrac12}$') == r'$x^{\frac{1}{2}}$'

    # Nested bare arguments
    assert lint.fix_text(r'\begin{align}\frac1{\sqrt2}\end{align}') == r'\begin{align}\dfrac{1}{\sqrt{2}}\end{align}'
    assert lint.fix_text(r'$\sqrt{\frac12}$') == r'$\sqrt{\dfrac{1}{2}}$'

    # Invalid parentheses / syntax are left untouched
    assert lint.fix_text(r'\frac1(x+1)') == r'\dfrac1(x+1)'  # 2nd arg invalid -> not bare-fixed
    assert lint.fix_text(r'\dfrac(1-a)(1-b)') == r'\dfrac(1-a)(1-b)'

    # Protected regions are untouched
    assert lint.fix_text('% \\sqrt2\n') == '% \\sqrt2\n'
    assert lint.fix_text(r'\verb|\sqrt2|') == r'\verb|\sqrt2|'

    # Fixed text has no bare arg errors
    fixed_sample = lint.fix_text(r'$\sqrt2+\sqrt3+\sqrt\pi+\frac12$')
    assert lint.check_bare_args(fixed_sample) == []


def test_estimate_math_visual_length_and_long_align_lines():
    # 1. Basic fractions and vertical stacking
    assert lint.estimate_math_visual_length(r'\dfrac{1}{2}') == 2
    assert lint.estimate_math_visual_length(r'\dfrac{\sqrt{2}}{2}') == 3
    assert lint.estimate_math_visual_length(r'\dfrac{a+b}{c+d}') == 4
    assert lint.estimate_math_visual_length(r'\dfrac{1}{\dfrac{2}{3}}') == 3

    # 2. Invisible metadata commands
    assert lint.estimate_math_visual_length(r'\label{eq:foo}') == 0
    assert lint.estimate_math_visual_length(r'\notag') == 0
    assert lint.estimate_math_visual_length(r'\displaystyle') == 0

    # 3. Accents and vector notation
    assert lint.estimate_math_visual_length(r'\overrightarrow{AB}') == 2
    assert lint.estimate_math_visual_length(r'\vec{a}') == 1

    # 4. Long code with \dfrac that has small visual width should not trigger warning
    # (116 raw characters, but ~48 visual width)
    sample_compact = (
        '\\begin{align}\n'
        r'  g(x) = \dfrac{\sin x}{1+\sin x}, \quad h(x) = \dfrac{2x}{\pi+4x} \text{について} \left(0 < x \le \dfrac{\pi}{2}\right)' + '\n'
        '\\end{align}\n'
    )
    assert lint.check_long_align_lines(sample_compact) == []

    # 5. Genuinely long visual line with >= 2 equals should trigger warning
    sample_long = (
        '\\begin{align}\n'
        r'k^5 = k^2(-ak-b) = -ak^3 - bk^2 = -a(-ak-b) - bk^2 = -bk^2 + a^2 k + ab + cdefg = hijklmn' + '\n'
        '\\end{align}\n'
    )
    warnings = lint.check_long_align_lines(sample_long)
    assert len(warnings) == 1
    line_no, msg = warnings[0]
    assert line_no == 2
    assert '推定表示幅' in msg
    assert '読みやすい可能性がある' in msg

    # 6. Long line with only 1 equal should not trigger warning
    sample_one_eq = (
        '\\begin{align}\n'
        r'A + B + C + D + E + F + G + H + I + J + K + L + M + N + O + P = Q + R + S + T + U + V + W' + '\n'
        '\\end{align}\n'
    )
    assert lint.check_long_align_lines(sample_one_eq) == []






