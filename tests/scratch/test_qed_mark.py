"""証明・解答の終わりの記号（\\qed に統一）の lint のテスト。"""
from scratch import lint_latex_style as lint

DOC = '\\documentclass[../../main.tex]{subfiles}\n\\begin{document}\n%s\n\\end{document}\n'


def messages(body):
    return [message for _, message in lint.check_qed_mark(DOC % body)]


def test_qed_at_end_of_sentence_is_allowed():
    for body in ['よって題意は示された．\\qed',
                 '\\begin{align}\n  a = b\n\\end{align}\nである．\\qed',
                 '\\begin{proof}\n  示された．\n\\end{proof}']:
        assert messages(body) == [], body


def test_other_end_marks_are_errors():
    for body in ['示された．$\\blacksquare$', '示された．$\\Box$', '示された．$\\square$',
                 '示された．$\\qed$', '\\begin{align}\n  a = b \\hfill \\qed\n\\end{align}',
                 '\\begin{align}\n  a = b \\quad \\blacksquare\n\\end{align}']:
        assert messages(body), body


def test_qed_before_end_of_proof_is_an_error():
    assert messages('\\begin{proof}\n  示された．\\qed\n\\end{proof}')


def test_square_as_quadrilateral_and_symbols_in_figures_are_allowed():
    for body in ['$\\square ABCD$ は正方形である．',
                 '面積は $\\dfrac{1}{2}\\square ABCD$ である．',
                 '\\begin{figure}[H]\n\\begin{tikzpicture}\\node {$\\square$};\\end{tikzpicture}\n'
                 '\\caption{c}\n\\end{figure}']:
        assert messages(body) == [], body


def test_web_conversion_places_black_square_at_end_of_sentence():
    from scratch import tex_to_md as converter
    out = converter.convert_text_qed('よって示された． \\qed\n\n次に $a \\qed b$ を考える．')
    assert out.startswith('よって示された．<span class="qed-symbol qed-inline">■</span>')
    assert '$a \\qed b$' in out  # 数式の中は変えない
