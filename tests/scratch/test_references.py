import re
from pathlib import Path
from unittest.mock import patch

import pytest
from scratch import tex_to_md as converter


@pytest.mark.parametrize('fallback', [False, True])
@pytest.mark.parametrize('kind', ['solution', 'problem'])
def test_multiple_mixed_references_use_actual_numbers_and_anchors(tmp_path, fallback, kind):
    prefix = 'problem_' if kind == 'problem' else ''
    refs = r'\cref{fig:beta, fig:alpha}; \ref{tab:beta, tab:alpha}; \cref{fig:beta,tab:beta,eq:99,plain}.'
    source = r'\begin{document}' + refs + '\n'
    for label in ('fig:alpha', 'fig:beta', 'plain'):
        source += r'\begin{figure}\begin{tikzpicture}\node{A};\end{tikzpicture}\caption{Panel}\label{' + label + r'}\end{figure}'
    for label in ('tab:alpha', 'tab:beta'):
        source += r'\begin{table}\begin{tabular}{c}A\end{tabular}\caption{Data}\label{' + label + r'}\end{table}'
    source += r'\begin{align}x=1\label{eq:99}\end{align}'
    source += r'\begin{align}\text{\cref{fig:beta,tab:beta,eq:99}}\end{align}'
    source += r'Inline $\text{\cref{fig:beta,tab:beta,eq:99}}$.'
    source += r'\end{document}'
    dest = tmp_path / (kind + '.tex')
    dest.write_text(source)
    parser = converter.TexSoup
    def parse(*args, **kwargs):
        if fallback:
            raise ValueError('exercise fallback')
        return parser(*args, **kwargs)
    output = tmp_path / 'out.md'
    with patch.object(converter, 'TexSoup', parse), patch.object(converter, 'compile_tikz_to_svg', return_value=True), patch.object(converter.pypandoc, 'convert_text', return_value='| A |\n|---|'):
        converter.convert_tex_clean(str(dest), str(output), {'type': kind}, '/images', str(tmp_path / 'images'))
    md = output.read_text()
    assert f'[図2](#{prefix}fig:beta),[図1](#{prefix}fig:alpha)' in md
    assert '[表2](#tab:beta),[表1](#tab:alpha)' in md
    assert f'[図2](#{prefix}fig:beta),[表2](#tab:beta),[(式1)](#eq:99),[図3](#{prefix}plain)' in md
    assert r'\text{図2,表2,(式1)}' in md
    assert r'Inline $\text{図2,表2,(式1)}$' in md
    for math in re.findall(r'\$\$.*?\$\$|\$[^$]*\$', md, re.S):
        assert '](' not in math
    for target in re.findall(r'\]\(#([^)]*)\)', md):
        assert ',' not in target
        assert f'id="{target}"' in md
    assert r'\cref{' not in md and r'\ref{' not in md
