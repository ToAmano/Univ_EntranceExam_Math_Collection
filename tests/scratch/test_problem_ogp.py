"""Problem OGP cards are derived from the problem, never the answer."""

import json
import struct
from pathlib import Path

from scratch import generate_problem_ogp as ogp


def test_excerpt_ignores_problem_figure_html_and_keeps_inline_math():
    markdown = '''---
type: "problem"
---

$p$ を $0<p<1$ とする．
<figure><img src="/images/tikz/fig_problem_1.svg" /></figure>
次の確率を求めよ．
'''
    excerpt = ogp.extract_excerpt(markdown)
    assert '$0<p<1$' in excerpt
    assert '次の確率を求めよ' in excerpt
    assert 'fig_problem' not in excerpt


def test_long_problem_excerpt_ends_at_a_sentence_boundary():
    markdown = '最初の条件を考える．' + '長い説明をする．' * 40
    excerpt = ogp.extract_excerpt(markdown, max_chars=45)
    assert excerpt.startswith('最初の条件を考える．')
    assert excerpt.endswith('…')
    assert len(excerpt) < len(markdown)


def test_display_math_is_simplified_without_leaking_tex_markup():
    markdown = r'''\quad $n$ を整数とする．
$$\begin{align}x+y=1\end{align}$$
この条件を用いて示せ．'''
    excerpt = ogp.extract_excerpt(markdown)
    assert '（数式）' in excerpt
    assert r'\begin{align}' not in excerpt
    assert r'\quad' in ogp._tex_text(excerpt)


def test_inequalities_are_not_removed_as_html_tags():
    markdown = '$a_0<b_0$，$a_1<b_1$を満たす．<figure><img src="/fig.svg" /></figure>'
    excerpt = ogp.extract_excerpt(markdown)
    assert '$a_0<b_0$' in excerpt
    assert '$a_1<b_1$' in excerpt
    assert 'fig.svg' not in excerpt


def test_cache_regenerates_only_when_input_changes(tmp_path, monkeypatch):
    md = tmp_path / 'utokyo-zenki-1999-3-problem.md'
    md.write_text('---\ntype: problem\n---\n問題A．')
    output = tmp_path / 'images'
    calls = []

    def fake_render(markdown, destination, figure=None):
        calls.append(markdown)
        destination.write_bytes(b'\x89PNG\r\n\x1a\ncard')
        return 'excerpt'

    monkeypatch.setattr(ogp, 'render_card', fake_render)
    first = ogp.generate_cards([md], output)
    second = ogp.generate_cards([md], output)
    md.write_text('---\ntype: problem\n---\n問題B．')
    third = ogp.generate_cards([md], output)
    assert [first.generated, second.generated, third.generated] == [1, 0, 1]
    assert len(calls) == 2
    assert (output / 'utokyo-zenki-1999-3.png').exists()
    assert json.loads((output / 'manifest.json').read_text())['utokyo-zenki-1999-3']


def test_full_generation_removes_cards_for_deleted_problems(tmp_path, monkeypatch):
    md = tmp_path / 'utokyo-zenki-1999-3-problem.md'
    md.write_text('---\ntype: problem\n---\n問題A．')
    output = tmp_path / 'images'
    output.mkdir()
    (output / 'deleted-problem.png').write_bytes(b'old')

    def fake_render(markdown, destination, figure=None):
        destination.write_bytes(b'new')
        return 'excerpt'

    monkeypatch.setattr(ogp, 'render_card', fake_render)
    ogp.generate_cards([md], output, prune=True)
    assert not (output / 'deleted-problem.png').exists()
    assert (output / 'utokyo-zenki-1999-3.png').exists()


def test_short_card_renders_at_ogp_dimensions(tmp_path):
    md = '''---
type: "problem"
---

$a>0$とし，$x>0$で定義された関数$f(x)=x^a$を考える．
面積を求めよ．
'''
    output = tmp_path / 'card.png'
    ogp.render_card(md, output)
    data = output.read_bytes()
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    assert struct.unpack('>II', data[16:24]) == (1200, 630)


def test_problem_vector_and_numbered_condition_macros_render(tmp_path):
    markdown = r'$\va*{a}$ と $\va*{b}$ は条件\ding{"AC}を満たす．'
    assert ogp.render_card(markdown, tmp_path / 'card.png') == 'excerpt'
