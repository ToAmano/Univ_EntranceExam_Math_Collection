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
    source = r'\begin{align*}\sqrt x+\frac12+\left(x\end{align*}\label{a}\label{a}'
    assert lint.fix_text(source) == source.replace(r'\frac12', r'\dfrac12')


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
    source.write_text(r'\sqrt x。', encoding='utf-8')
    assert run('--fix').returncode == 1
    assert source.read_text() == r'\sqrt x．'


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
    assert fixed == r'\label{eq:1} \cref{eq:1} \label{eq:2} \eqref{eq:2}'
    duplicate = r'\label{eq:1} \label{eq:1} \cref{eq:1}'
    assert lint.fix_text(duplicate) == duplicate
    path = tmp_path / 'solution.tex'
    path.write_text(duplicate, encoding='utf-8')
    errors, _, _ = lint.lint_file(path)
    assert any('重複' in message for _, message in errors)


def test_math_environment_rejects_untyped_label(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_text(r'\begin{equation}x=1\label{1}\end{equation} \cref{1}', encoding='utf-8')
    errors, _, _ = lint.lint_file(source)
    assert any('eq:1' in message and '形式' in message for _, message in errors)


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




