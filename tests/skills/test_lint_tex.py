"""数学答案の lint（skills/math-solution-tex/scripts/lint_tex.py）をスキル単体で使うときのテスト。

リポジトリ固有の検査（local/lint_local.py）を読み込まない場合に、汎用の検査だけが動くことと、
--rules で固有の検査を足せることを確かめる。従来の入口 scratch/lint_latex_style.py の
テストは tests/scratch/ にある。
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

_SKILL = Path(__file__).resolve().parents[2] / 'skills' / 'math-solution-tex'
_SCRIPT = _SKILL / 'scripts' / 'lint_tex.py'
_RULES = _SKILL / 'local' / 'lint_local.py'


def _load(name, path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


lint = _load('_math_solution_tex_lint_tex', _SCRIPT)


def run(*args, cwd=None):
    return subprocess.run([sys.executable, str(_SCRIPT), *args], capture_output=True, text=True, cwd=cwd)


DOC = '\\documentclass{article}\n\\begin{document}\n{\\bf [解]}本文です。$\\frac12$\n\\[ x \\]\n\\end{document}\n'


def test_generic_lint_reports_generic_rules_only(tmp_path):
    source = tmp_path / 'a.tex'
    source.write_text(DOC, encoding='utf-8')
    errors, warnings, skipped = lint.lint_file(source)
    messages = ' '.join(msg for _, msg in errors)
    assert '\\[ は使わない' in messages
    assert '句読点は全角' in messages
    # 見出し・subfiles の documentclass はリポジトリ固有の検査なので、汎用では出ない
    assert '解答見出し' not in messages
    assert 'subfiles' not in messages
    assert skipped is None


def test_generic_fix_leaves_headings(tmp_path):
    fixed = lint.fix_text(DOC)
    assert '本文です．$\\dfrac{1}{2}$' in fixed
    assert '\\begin{align}' in fixed
    assert '{\\bf [解]}' in fixed  # 見出しの統一は固有の修正


def test_rules_profile_adds_local_checks_and_fixes(tmp_path):
    local = _load('_math_solution_tex_lint_local', _RULES)
    source = tmp_path / 'solution.tex'
    source.write_text(DOC, encoding='utf-8')
    errors, _, _ = lint.lint_file(source, local.PROFILE)
    messages = ' '.join(msg for _, msg in errors)
    assert '解答見出し' in messages
    assert 'subfiles' in messages
    assert '{\\bf [解答]}' in lint.fix_text(DOC, local.PROFILE.edit_finders())


def test_cli_requires_files_without_rules():
    result = run()
    assert result.returncode == 2
    assert '検査するファイルを指定する' in result.stderr


def test_cli_diff_and_fix(tmp_path):
    source = tmp_path / 'a.tex'
    source.write_text(DOC, encoding='utf-8')
    preview = run('--diff', str(source), cwd=tmp_path)
    assert preview.returncode == 1
    assert any(line.startswith('+') and '本文です．' in line for line in preview.stdout.splitlines())
    assert source.read_text(encoding='utf-8') == DOC
    fixed = run('--fix', str(source), cwd=tmp_path)
    assert 'Fixed:' in fixed.stdout
    assert '\\begin{align}' in source.read_text(encoding='utf-8')


def test_cli_rules_option(tmp_path):
    source = tmp_path / 'solution.tex'
    source.write_text(DOC, encoding='utf-8')
    result = run('--rules', str(_RULES), str(source), cwd=tmp_path)
    assert result.returncode == 1
    assert '解答見出し' in result.stdout


def test_lint_skip_marker(tmp_path):
    source = tmp_path / 'a.tex'
    source.write_text('% lint-skip: 旧形式\n' + DOC, encoding='utf-8')
    errors, warnings, skipped = lint.lint_file(source)
    assert skipped == '旧形式'
    assert errors == [] and warnings == []


def _messages(results):
    return ' '.join(msg for _, msg in results)


def test_lint_file_tags_section_numbers(tmp_path):
    source = tmp_path / 'a.tex'
    source.write_text(DOC, encoding='utf-8')
    errors, _, _ = lint.lint_file(source)
    assert all('[§' in msg for _, msg in errors)
    assert '\\[ は使わない（align 環境を使う） [§N5.1]' in _messages(errors)


def test_check_functions_keep_plain_messages():
    # 節番号は lint_file で付ける。個々の検査関数の戻り値は変えない
    assert '[§' not in _messages(lint.check_align_star('\\begin{align*}x\\end{align*}'))


def test_new_error_checks():
    assert lint.check_binom('$\\binom{n}{k}$ と $\\dbinom{6}{2}$') and len(lint.check_binom('$\\dbinom{6}{2}$')) == 1
    assert lint.check_subfigure_env('\\begin{subfigure}{0.4\\textwidth}\\end{subfigure}')
    two_col = '\\begin{multicols}{2}\\begin{figure}[htb]\\end{figure}\\begin{table}[H]\\end{table}\\end{multicols}'
    assert len(lint.check_multicols_float(two_col)) == 1
    assert lint.check_rotated_arrows('$\\rotatebox[origin=c]{-45}{$\\curvearrowright$}$')
    assert not lint.check_rotated_arrows('$\\curvearrowright$')
    good = '\\begin{figure}[htb]\n  \\centering\n  \\tdplotsetmaincoords{65}{115}\n  \\begin{tikzpicture}\\end{tikzpicture}\n\\end{figure}'
    assert not lint.check_tdplot_placement(good)
    assert lint.check_tdplot_placement('\\tdplotsetmaincoords{65}{115}\n' + good.replace('\\tdplotsetmaincoords{65}{115}\n', ''))


def test_new_warning_checks():
    assert lint.check_cases_env('\\begin{cases} a \\end{cases}')
    assert not lint.check_cases_env('\\begin{dcases} a \\end{dcases}')
    raw = '% TODO: 概要図\n\\begin{figure}\n% TODO: 図を描く\n\\end{figure}\n'
    assert [line for line, _ in lint.check_figure_todo_placement(raw)] == [1]
    pic = ('\\begin{tikzpicture}\\draw[dashed, gray!50] (0,0)--(1,1); \\fill[gray!20] (0,0) circle (1);'
           ' \\draw[fill=gray!20] (0,0)--(1,0); \\node[gray!30!black] at (0,0) {a};'
           ' \\fill[pattern=north east lines, pattern color=gray!40] (0,0) rectangle (1,1);'
           ' \\fill (0,0) circle (0.05); \\draw (0,0) circle (1);\\end{tikzpicture}')
    assert len(lint.check_light_gray(pic)) == 2  # gray!50 の線と gray!40 の斜線（塗りと黒との混色は対象外）
    assert len(lint.check_small_coordinate_circle(pic)) == 1  # 図形の円 circle (1) は対象外
