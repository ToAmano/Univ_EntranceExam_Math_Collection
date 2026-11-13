"""和文に接する半角の「,」「.」を全角の「，」「．」にする lint のテスト。"""
from scratch import lint_latex_style as lint

DOC = '\\documentclass[../../main.tex]{subfiles}\n\\begin{document}\n%s\n\\end{document}\n'


def fixed(body):
    return lint.fix_text(DOC % body).split('\\begin{document}\n', 1)[1].rsplit('\n\\end{document}', 1)[0]


def errors(body):
    return lint.check_punctuation(DOC % body)


def test_halfwidth_punctuation_next_to_japanese_is_fixed():
    assert fixed('題意から,取り出した数はある.') == '題意から，取り出した数はある．'
    assert fixed('$C_1$ とし, $C_1$ 上に') == '$C_1$ とし，$C_1$ 上に'
    assert len(errors('題意から,取り出した数はある.')) == 2


def test_math_numbers_ellipsis_and_comments_are_kept():
    for body in ['$x$, $y$ は $1.5$ と 1.2 のとき... よって',
                 '\\begin{align}\n  a, b.\n\\end{align}',
                 '% コメント, ある.\n本文．',
                 '\\begin{figure}[H]\n\\begin{tikzpicture}\\node {点A, 点B.};\\end{tikzpicture}\n'
                 '\\caption{c}\n\\end{figure}']:
        assert fixed(body) == body, body
        assert errors(body) == [], body
