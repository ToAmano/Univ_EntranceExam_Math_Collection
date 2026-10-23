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
