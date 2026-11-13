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
