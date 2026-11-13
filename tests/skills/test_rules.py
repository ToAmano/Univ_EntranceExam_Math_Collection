"""規約の節を引くスクリプト（skills/math-solution-tex/scripts/rules.py）のテスト。"""
import importlib.util
import sys
from pathlib import Path

_PATH = Path(__file__).resolve().parents[2] / 'skills' / 'math-solution-tex' / 'scripts' / 'rules.py'
_spec = importlib.util.spec_from_file_location('_math_solution_tex_rules_cli', _PATH)
rules = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rules)

SECTIONS = rules.load_sections()


def ids(found):
    return [s.sid for s in found]


def test_every_source_has_sections():
    sources = {s.source for s in SECTIONS}
    assert sources == {name for name, _, _ in rules.SOURCES}


def test_section_ids_are_unique():
    seen = [s.sid for s in SECTIONS]
    assert len(seen) == len(set(seen))


def test_normalize_accepts_lint_and_prose_forms():
    assert rules.normalize('[§N5.1]') == 'N5.1'
    assert rules.normalize('§TB2.4') == 'TB2.4'
    assert rules.normalize('figure §7.1') == 'F7.1'
    assert rules.normalize('f7.1') == 'F7.1'


def test_select_includes_subsections_but_not_similar_numbers():
    assert ids(rules.select(SECTIONS, ['N5'])) == ['N5']
    assert 'N5.3' in rules.select(SECTIONS, ['N5'])[0].text
    assert ids(rules.select(SECTIONS, ['N1'])) == ['N1']  # N10・N11 を含まない
    assert ids(rules.select(SECTIONS, ['F7.1'])) == ['F7.1']
    assert ids(rules.select(SECTIONS, ['FA'])) == ['FA']


def test_prefix_query_selects_whole_file():
    assert ids(rules.select(SECTIONS, ['TR'])) == [f'TR{i}' for i in range(1, 8)]


def test_every_lint_section_tag_exists():
    lint_path = _PATH.parent / 'lint_tex.py'
    local_path = _PATH.parent.parent / 'local' / 'lint_local.py'
    import re
    tags = set()
    for path in (lint_path, local_path):
        tags |= set(re.findall(r"tag\([^)]*\), '([A-Z]+[0-9.]+)'\)", path.read_text(encoding='utf-8')))
    tags |= {'N10.2', 'N10.3'}
    known = {s.sid for s in SECTIONS}
    assert tags and tags <= known, tags - known


def test_phases_resolve():
    for phase, queries in rules.PHASES.items():
        assert rules.select(SECTIONS, queries), phase


def test_cli(capsys):
    assert rules.main(['--sec', '[§N5.3]']) == 0
    assert '### N5.3' in capsys.readouterr().out
    assert rules.main(['--sec', 'X9']) == 1
    assert rules.main(['--grep', 'dcases']) == 0
    assert 'N1.1' in capsys.readouterr().out
