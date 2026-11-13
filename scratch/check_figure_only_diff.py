#!/usr/bin/env python3
"""互換用の入口：本体は skills/math-solution-tex/scripts/check_figure_only_diff.py に移した。

`python3 scratch/check_figure_only_diff.py ...` と `from scratch.check_figure_only_diff import ...`
の既存の呼び出し（AGENTS.md の手順、テスト）を壊さないよう、本体をそのまま使えるようにする。
"""
import importlib.util
import sys
from pathlib import Path

_PATH = (Path(__file__).resolve().parent.parent / 'skills' / 'math-solution-tex' / 'scripts'
         / 'check_figure_only_diff.py')
_NAME = '_math_solution_tex_check_figure_only_diff'
if _NAME not in sys.modules:
    _spec = importlib.util.spec_from_file_location(_NAME, _PATH)
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_NAME] = _module
    _spec.loader.exec_module(_module)

if __name__ == '__main__':
    sys.modules[_NAME].main()
else:
    sys.modules[__name__] = sys.modules[_NAME]
