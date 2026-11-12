"""#1472: solution.tex の先頭で \\subfile{problem} により問題文を読み込む形のテスト。"""
from pathlib import Path
from unittest.mock import patch

from scratch import generate_main_tex as gen
from scratch import lint_latex_style as lint
from scratch import tex_to_md

HEADER = '\\documentclass[../../main.tex]{subfiles}\n\\begin{document}\n'
EMBED = '\\begin{oframed}\n  \\subfile{problem}\n\\end{oframed}\n'


def write_question(root, univ, cat, year, q, problem, solution):
    qdir = root / 'src' / univ / cat / year / q
    qdir.mkdir(parents=True)
    (qdir / 'problem.tex').write_text(problem, encoding='utf-8')
    (qdir / 'solution.tex').write_text(solution, encoding='utf-8')
    return qdir


# ---------------------------------------------------------------- lint

def test_solution_must_embed_problem_before_heading(tmp_path):
    qdir = write_question(tmp_path, 'utokyo', 'zenki', '2000', '1',
                          HEADER + '問題．\n\\end{document}\n',
                          HEADER + '{\\bf [解答]}\n本文．\n\\end{document}\n')
    errors, _, _ = lint.lint_file(qdir / 'solution.tex')
    assert any('subfile{problem}' in message for _, message in errors)

    (qdir / 'solution.tex').write_text(HEADER + EMBED + '{\\bf [解答]}\n本文．\n\\end{document}\n', encoding='utf-8')
    errors, _, _ = lint.lint_file(qdir / 'solution.tex')
    assert not any('subfile{problem}' in message for _, message in errors)


def test_embedding_after_heading_is_an_error():
    text = HEADER + '{\\bf [解答]}\n' + EMBED + '\\end{document}\n'
    assert lint.check_problem_embedded(text)


def test_problem_must_be_a_document_with_h_figures(tmp_path):
    qdir = write_question(tmp_path, 'utokyo', 'kouki', '2000', '1', '問題の断片．\n', HEADER + EMBED + '\\end{document}\n')
    errors, _, _ = lint.lint_file(qdir / 'problem.tex')
    assert any('begin{document}' in message for _, message in errors)

    (qdir / 'problem.tex').write_text(
        HEADER + '\\begin{figure}[htbp]\n\\centering\n\\caption{図}\n\\end{figure}\n\\end{document}\n', encoding='utf-8')
    errors, _, _ = lint.lint_file(qdir / 'problem.tex')
    assert any('[H]' in message for _, message in errors)


# ---------------------------------------------------------------- main.tex

def test_main_tex_includes_only_solution_when_it_embeds_problem(tmp_path, monkeypatch):
    write_question(tmp_path, 'utokyo', 'zenki', '2000', '1',
                   HEADER + '問題．\n\\end{document}\n', HEADER + EMBED + '解答．\n\\end{document}\n')
    write_question(tmp_path, 'utokyo', 'zenki', '2000', '2',
                   HEADER + '問題．\n\\end{document}\n', HEADER + '解答．\n\\end{document}\n')
    monkeypatch.setattr(gen, 'SRC_ROOT', str(tmp_path / 'src'))
    gen.generate_category('utokyo', 'zenki')
    main = (tmp_path / 'src' / 'utokyo' / 'zenki' / 'main.tex').read_text(encoding='utf-8')
    # 第1問は solution.tex が問題文を読み込むので problem.tex は入れない（問題文が2回出ないように）
    assert '\\subfile{2000/1/solution}' in main and '\\subfile{2000/1/problem}' not in main
    # 移行前の形（第2問）は従来どおり problem → solution
    assert '\\subfile{2000/2/problem}' in main and '\\subfile{2000/2/solution}' in main


# ---------------------------------------------------------------- Web

def test_web_solution_page_drops_embedded_problem(tmp_path):
    qdir = write_question(tmp_path, 'utokyo', 'zenki', '2000', '1',
                          HEADER + '問題文の本文．\n\\end{document}\n',
                          HEADER + EMBED + '{\\bf [解答]}\n解答の本文．\n\\end{document}\n')
    out = tmp_path / 'out.md'
    with patch.object(tex_to_md, 'compile_tikz_to_svg', lambda *a, **k: True):
        tex_to_md.convert_tex_clean(str(qdir / 'solution.tex'), str(out), {'type': 'solution'},
                                    '/images', str(tmp_path / 'images'))
    md = out.read_text(encoding='utf-8')
    assert '解答の本文' in md
    assert 'subfile' not in md and 'oframed' not in md and '問題文の本文' not in md
