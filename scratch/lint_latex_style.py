#!/usr/bin/env python3
"""
このリポジトリの TeX 原稿の lint（入口）。
.github/workflows/lint-tex.yml と pre-commit から呼び出される。

検査の本体はスキル skills/math-solution-tex/ にある。
  - 汎用の検査・修正：skills/math-solution-tex/scripts/lint_tex.py
  - このリポジトリ固有の検査（見出し、subfiles、problem.tex との関係、対象ファイル）：
    skills/math-solution-tex/local/lint_local.py
このファイルは両者を読み込み、従来どおりの名前（check_*、fix_text、lint_file、main）で使えるようにする。

対象は src/**/solution.tex と src/**/problem.tex。
目視判断が必要なルール（大カッコを \\Bigl 化すべきか、enumerate/itemize が小問
ラベリング目的か場合分け目的か等）は対象外。
違反が1件でもあれば exit code 1 で終了する（\\overline{} の使用と align 内の長い行のみ警告扱いで非ブロッキング）。
"""
import importlib.util
import sys
from pathlib import Path

_SKILL = Path(__file__).resolve().parent.parent / 'skills' / 'math-solution-tex'


def _load(name, path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


_lint_tex = _load('_math_solution_tex_lint_tex', _SKILL / 'scripts' / 'lint_tex.py')
_lint_local = _load('_math_solution_tex_lint_local', _SKILL / 'local' / 'lint_local.py')

# 従来の名前（check_*、strip_comments、正規表現の定数など）をこのモジュールからも使えるようにする。
for _module in (_lint_tex, _lint_local):
    globals().update({k: v for k, v in vars(_module).items() if not k.startswith('__')})

PROFILE = _lint_local.PROFILE


def fix_text(raw):
    """汎用の機械的な修正に、このリポジトリ固有の修正（解答の見出し）を加えて適用する。"""
    return _lint_tex.fix_text(raw, PROFILE.edit_finders())


def lint_file(path):
    return _lint_tex.lint_file(path, PROFILE)


def main(argv=None):
    _lint_tex.main(argv, profile=PROFILE, description=__doc__)


if __name__ == '__main__':
    main()
