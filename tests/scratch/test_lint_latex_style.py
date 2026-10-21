import subprocess
import sys
from pathlib import Path

from scratch import lint_latex_style as lint


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
    assert lint.fix_text(protected) == protected.replace('リンク。', 'リンク．')
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
