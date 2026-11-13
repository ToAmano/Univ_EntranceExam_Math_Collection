"""本文での余白・改行のコマンドの禁止（lint）のテスト。"""
from scratch import lint_latex_style as lint

DOC = '\\documentclass[../../main.tex]{subfiles}\n\\begin{document}\n%s\n\\end{document}\n'


def messages(body):
    return [message for _, message in lint.check_spacing_commands(DOC % body)]


def test_spacing_commands_in_body_are_errors():
    for command in ['\\medskip', '\\bigskip', '\\smallskip', '\\hfill', '\\noindent{\\bf [別解]}',
                    '\\vspace{10pt}', '\\hspace{1cm}', 'である．\\quad', '\\qquad 本文']:
        assert messages(command), command


def test_spacing_inside_math_figure_table_and_blank_underline_is_allowed():
    allowed = [
        '\\begin{align}\n  a = b \\quad (\\because c)\n\\end{align}',
        '$x \\quad y$',
        '\\begin{figure}[htb]\n\\begin{subcaptionblock}{.4\\linewidth}x\\end{subcaptionblock}\\hfill\n\\caption{c}\n\\end{figure}',
        '\\begin{tabular}{c}\n\\hspace{1em}a\n\\end{tabular}',
        '空欄 \\underline{\\hspace{0.8cm}} を埋めよ．',
    ]
    for body in allowed:
        assert messages(body) == [], body


def test_commented_out_commands_are_ignored(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_text(DOC % '% \\bigskip\n{\\bf [解答]}\n本文．', encoding='utf-8')
    errors, _, _ = lint.lint_file(source)
    assert not any('余白' in message for _, message in errors)
