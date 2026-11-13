"""Web 版の TeX の漏れの検査（scratch/check_web_leaks.py）のテスト。"""
import shutil
from pathlib import Path

import pytest

from scratch import check_web_leaks as checker

REPO = Path(__file__).resolve().parents[2]
DOC = '\\documentclass[../../main.tex]{subfiles}\n\\begin{document}\n%s\n\\end{document}\n'


def test_known_files_exist():
    # 直してファイルが消えたり移ったりしたら KNOWN から外す
    for path in checker.KNOWN:
        assert (REPO / path).exists(), path


def test_page_type():
    assert checker.page_type('src/utokyo/zenki/2000/1/problem.tex') == 'problem'
    assert checker.page_type('src/utokyo/zenki/2000/1/solution.tex') == 'solution'
    assert checker.page_type('src/titech/kouki/2010/0/solution.tex') == 'summary'


@pytest.mark.skipif(shutil.which('node') is None or shutil.which('pandoc') is None,
                    reason='Node.js と pandoc が要る')
def test_leaks_are_found_through_the_site_markdown_pipeline(tmp_path):
    leaky = tmp_path / 'leaky' / 'solution.tex'
    clean = tmp_path / 'clean' / 'solution.tex'
    for path, body in ((leaky, '{\\bf [解答]}\nとかける．\\null\n'),
                       (clean, '{\\bf [解答]}\n割合は69\\%で，$r > \\dfrac{1}{2}$ である．\n')):
        path.parent.mkdir()
        path.write_text(DOC % body, encoding='utf-8')
    leaks, failures = checker.find_leaks([str(leaky), str(clean)])
    assert failures == {}
    assert [item['command'] for item in leaks[str(leaky)]] == ['\\null']
    assert str(clean) not in leaks
