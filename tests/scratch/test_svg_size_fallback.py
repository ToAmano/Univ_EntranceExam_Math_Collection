"""Large PDF-to-SVG outputs can be replaced without losing the original."""

from pathlib import Path
from types import SimpleNamespace

from scratch import tex_to_md


def test_oversized_svg_is_replaced_by_smaller_dvisvgm_output(tmp_path, monkeypatch):
    svg = tmp_path / 'figure.svg'
    svg.write_bytes(b'x' * (5_000_001))
    pdf = tmp_path / 'figure.pdf'
    pdf.write_bytes(b'pdf')

    monkeypatch.setattr(tex_to_md.shutil, 'which', lambda name: '/usr/bin/dvisvgm')

    def run(command, **kwargs):
        assert command[:3] == ['/usr/bin/dvisvgm', '--pdf', '--no-fonts']
        assert command[-1] == str(pdf)
        Path(command[command.index('-o') + 1]).write_bytes(b'<svg/>')
        return SimpleNamespace(returncode=0, stderr='')

    monkeypatch.setattr(tex_to_md.subprocess, 'run', run)

    assert tex_to_md._replace_oversized_svg_with_dvisvgm(str(pdf), str(svg))
    assert svg.read_bytes() == b'<svg/>'


def test_svg_at_threshold_is_left_untouched(tmp_path, monkeypatch):
    svg = tmp_path / 'figure.svg'
    svg.write_bytes(b'x' * 5_000_000)
    monkeypatch.setattr(tex_to_md.subprocess, 'run', lambda *a, **k: (_ for _ in ()).throw(AssertionError('conversion ran')))

    assert not tex_to_md._replace_oversized_svg_with_dvisvgm('unused.pdf', str(svg))
    assert svg.stat().st_size == 5_000_000


def test_failed_dvisvgm_keeps_original_svg(tmp_path, monkeypatch):
    svg = tmp_path / 'figure.svg'
    svg.write_bytes(b'x' * (5_000_001))
    monkeypatch.setattr(tex_to_md.shutil, 'which', lambda name: '/usr/bin/dvisvgm')

    def run(command, **kwargs):
        Path(command[command.index('-o') + 1]).write_bytes(b'partial')
        return SimpleNamespace(returncode=1, stderr='conversion error')

    monkeypatch.setattr(tex_to_md.subprocess, 'run', run)

    assert not tex_to_md._replace_oversized_svg_with_dvisvgm('figure.pdf', str(svg))
    assert svg.stat().st_size == 5_000_001
    assert svg.read_bytes()[:1] == b'x'


def test_larger_dvisvgm_output_keeps_original_svg(tmp_path, monkeypatch):
    svg = tmp_path / 'figure.svg'
    svg.write_bytes(b'x' * (5_000_001))
    monkeypatch.setattr(tex_to_md.shutil, 'which', lambda name: '/usr/bin/dvisvgm')

    def run(command, **kwargs):
        Path(command[command.index('-o') + 1]).write_bytes(b'y' * (5_000_002))
        return SimpleNamespace(returncode=0, stderr='')

    monkeypatch.setattr(tex_to_md.subprocess, 'run', run)

    assert not tex_to_md._replace_oversized_svg_with_dvisvgm('figure.pdf', str(svg))
    assert svg.read_bytes()[:1] == b'x'


def test_invalid_dvisvgm_svg_keeps_original(tmp_path, monkeypatch):
    svg = tmp_path / 'figure.svg'
    svg.write_bytes(b'x' * (5_000_001))
    monkeypatch.setattr(tex_to_md.shutil, 'which', lambda name: '/usr/bin/dvisvgm')

    def run(command, **kwargs):
        Path(command[command.index('-o') + 1]).write_bytes(b'partial')
        return SimpleNamespace(returncode=0, stderr='')

    monkeypatch.setattr(tex_to_md.subprocess, 'run', run)

    assert not tex_to_md._replace_oversized_svg_with_dvisvgm('figure.pdf', str(svg))
    assert svg.read_bytes()[:1] == b'x'
