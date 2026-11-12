"""3D 図の視点（\\tdplotsetmaincoords）を図ごとに Web 用 SVG へ反映する。"""
import re
from pathlib import Path
from unittest.mock import patch

import pytest

from scratch import tex_to_md as converter

VIEW_A = r'\tdplotsetmaincoords{60}{120}'
VIEW_B = r'\tdplotsetmaincoords{75}{30}'
VIEW_TOP = r'\tdplotsetmaincoords{80}{200}'
DEFAULT = r'\tdplotsetmaincoords{70}{110}'


def figure(view, label):
    head = f'  {view}\n' if view else ''
    return (
        '\\begin{figure}[htb]\n'
        '  \\centering\n'
        f'{head}'
        '  \\begin{tikzpicture}[tdplot_main_coords]\n'
        '    \\draw (0,0,0) -- (1,1,1);\n'
        '  \\end{tikzpicture}\n'
        f'  \\caption{{{label}}}\n'
        f'  \\label{{fig:{label}}}\n'
        '\\end{figure}\n'
    )


SOURCE = (
    '\\documentclass[../../main.tex]{subfiles}\n'
    '\\begin{document}\n'
    '{\\bf [解答]}\n'
    'はじめの図．\n'
    + figure('', 'nodefault')          # 呼び出しなし → 既定値
    + figure(VIEW_A, 'a')               # 図の中で呼ぶ → その図だけ
    + figure('', 'afterA')             # 前の図の視点は漏れない → 既定値
    + VIEW_TOP + '\n'                   # figure の外で呼ぶ → 以降の図に効く
    + figure('', 'top')
    + figure(VIEW_B, 'b')               # 図の中の呼び出しが優先
    + figure('', 'afterB')             # figure 外の呼び出しが残る
    + '\\end{document}\n'
)
EXPECTED = [DEFAULT, VIEW_A, DEFAULT, VIEW_TOP, VIEW_B, VIEW_TOP]


def test_figure_tdplot_views_follow_tex_grouping():
    assert converter.figure_tdplot_views(SOURCE) == EXPECTED


def test_files_without_tdplot_get_no_views():
    assert converter.figure_tdplot_views(figure('', 'x')) == []


def test_figure_local_views_are_not_hoisted_to_global_defs():
    defs = converter.extract_global_macro_defs(SOURCE)
    assert VIEW_A not in defs and VIEW_B not in defs
    assert VIEW_TOP in defs


@pytest.mark.parametrize('fallback', [False, True])
def test_each_figure_compiles_with_its_own_view(tmp_path, fallback):
    source = tmp_path / 'solution.tex'
    source.write_text(SOURCE, encoding='utf-8')
    calls = []

    def compile_diagram(code, path, macro_defs='', **options):
        calls.append(macro_defs)
        Path(path).write_text('<svg/>')
        return True

    parser = converter.TexSoup

    def parse(*args, **kwargs):
        if fallback:
            raise ValueError('exercise fallback')
        return parser(*args, **kwargs)

    with patch.object(converter, 'compile_tikz_to_svg', compile_diagram), \
            patch.object(converter, 'TexSoup', parse):
        converter.convert_tex_clean(str(source), str(tmp_path / 'out.md'), {'type': 'solution'},
                                    '/images', str(tmp_path / 'images'))

    assert len(calls) == len(EXPECTED)
    for defs, view in zip(calls, EXPECTED):
        # 最後に呼ばれた視点がその図で有効になる
        assert re.findall(r'\\tdplotsetmaincoords\{[^}]*\}\{[^}]*\}', defs)[-1] == view
