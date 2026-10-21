"""TikZ commands are opaque to the document parser, including loop variables."""
import re
from pathlib import Path
from unittest.mock import patch

import pytest

from scratch import tex_to_md as converter


@pytest.mark.parametrize('fallback', [False, True])
def test_real_1989_6_keeps_three_separate_figures(tmp_path, fallback):
    source = Path(__file__).resolve().parents[2] / 'src/utokyo/zenki/1989/6/solution.tex'
    original = source.read_bytes()
    # Match the converter's comment removal, including the commented-out fourth figure.
    text = '\n'.join(re.sub(r'(?<!\\)%.*', '', line)
                     for line in original.decode().splitlines()
                     if not line.strip().startswith('%'))
    expected = re.findall(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', text, re.S)
    calls = []
    def compile_diagram(code, path, macro_defs='', **options):
        calls.append((code, options))
        Path(path).write_text('<svg/>')
        return True
    parser = converter.TexSoup
    def parse(*args, **kwargs):
        if fallback:
            raise ValueError('exercise fallback')
        return parser(*args, **kwargs)
    output = tmp_path / 'out.md'
    with patch.object(converter, 'compile_tikz_to_svg', compile_diagram), patch.object(converter, 'TexSoup', parse):
        converter.convert_tex_clean(str(source), str(output), {'type': 'solution'}, '/images', str(tmp_path / 'images'))
    assert len(calls) == len(expected) == 3
    for (code, options), raw in zip(calls, expected):
        assert code == raw
        assert not options.get('figure_layout')
    assert output.read_text().count('<img ') == 3
    assert source.read_bytes() == original


def test_composite_caption_extraction_leaves_tikz_commands_untouched():
    tikz = r'\begin{tikzpicture}\def\label{LOCAL}\node {\label{value}};\end{tikzpicture}'
    source = r'\begin{figure}' + tikz + tikz + r'\caption{Outer}\label{fig:outer}\end{figure}'
    body, caption, label, sublabels = converter.figure_layout_parts(source)
    assert body == tikz + tikz
    assert (caption, label, sublabels) == ('Outer', 'fig:outer', [])


def test_lualatex_diagnostic_survives_pdflatex_fallback(tmp_path, capsys):
    import subprocess
    def fail(cmd, **kwargs):
        message = 'ORIGINAL LUA ERROR' if cmd[0] == 'lualatex' else 'SECONDARY PDFLATEX ERROR'
        return subprocess.CompletedProcess(cmd, 1, stdout=message, stderr='')
    with patch.object(converter.subprocess, 'run', fail):
        assert not converter.compile_tikz_to_svg(r'\begin{tikzpicture}\end{tikzpicture}', str(tmp_path / 'out.svg'))
    output = capsys.readouterr().out
    assert 'ORIGINAL LUA ERROR' in output
    assert 'SECONDARY PDFLATEX ERROR' in output
