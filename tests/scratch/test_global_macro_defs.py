"""図の外に書いた定義を、図のコンパイル用に集め、本文から取り除く（#1489）。"""
from scratch import tex_to_md as converter

DECLARE = (
    '\\pgfmathdeclarefunction{gfunc}{1}{\n'
    '  \\pgfmathparse{#1/sqrt((#1)^2-1)}\n'
    '}'
)
NEWCOMMAND = (
    '\\newcommand{\\drawTriangle}[3]{\n'
    '  \\draw (#1) -- (#2) -- (#3) -- cycle;\n'
    '}'
)
TIKZSET = '\\tikzset{pt/.style={circle, fill, inner sep=1.2pt}}'
DEF = '\\def\\r{1.5}'
SETMACRO = '\\pgfmathsetmacro\\maxn{10}'

SOURCE = (
    '\\begin{document}\n'
    'はじめに．\n'
    f'{DECLARE}\n'
    f'{NEWCOMMAND}\n'
    f'{TIKZSET}\n'
    f'{DEF}\n'
    f'{SETMACRO}\n'
    '本文の続き．$x^2$ を考える．\n'
    '\\begin{figure}[H]\n'
    '  \\centering\n'
    '  \\begin{tikzpicture}\n'
    '    \\foreach \\i in {1,2}{ \\pgfmathsetmacro{\\a}{\\i*2} }\n'
    '    \\drawTriangle{0,0}{1,0}{0,1}\n'
    '  \\end{tikzpicture}\n'
    '  \\caption{図}\n'
    '\\end{figure}\n'
    '\\end{document}\n'
)


def test_definitions_with_braced_bodies_are_hoisted_whole():
    defs = converter.extract_global_macro_defs(SOURCE)
    for snippet in (DECLARE, NEWCOMMAND, TIKZSET, DEF, SETMACRO):
        assert snippet in defs
    # 本体の外の本文や数式は拾わない
    assert '本文の続き' not in defs


def test_definitions_inside_tikzpicture_are_not_hoisted():
    defs = converter.extract_global_macro_defs(SOURCE)
    assert '\\pgfmathsetmacro{\\a}' not in defs


def test_definitions_are_stripped_from_body_but_figures_are_kept():
    body = converter.strip_global_macro_defs(SOURCE)
    for snippet in (DECLARE, NEWCOMMAND, TIKZSET, DEF, SETMACRO):
        assert snippet not in body
    assert 'はじめに．' in body and '本文の続き．$x^2$ を考える．' in body
    assert '\\pgfmathsetmacro{\\a}{\\i*2}' in body
    assert '\\drawTriangle{0,0}{1,0}{0,1}' in body


def test_figure_local_view_stays_in_figure():
    source = (
        '\\begin{figure}[H]\n'
        '  \\tdplotsetmaincoords{65}{115}\n'
        '  \\begin{tikzpicture}[tdplot_main_coords]\\end{tikzpicture}\n'
        '\\end{figure}\n'
    )
    assert converter.strip_global_macro_defs(source) == source


def test_similar_command_names_are_not_matched():
    source = '\\default と \\tikzsetnextfilename{x} はそのまま．\n'
    assert converter.strip_global_macro_defs(source) == source
    assert converter.extract_global_macro_defs(source) == ''
