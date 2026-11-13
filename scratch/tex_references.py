"""互換用の入口：本体は skills/math-solution-tex/scripts/tex_references.py に移した。

`from scratch import tex_references` / `import tex_references` の既存の呼び出しを壊さないよう、
本体のモジュールをそのままこの名前で使えるようにする。
"""
import importlib.util
import sys
from pathlib import Path

_PATH = Path(__file__).resolve().parent.parent / 'skills' / 'math-solution-tex' / 'scripts' / 'tex_references.py'
_NAME = '_math_solution_tex_tex_references'
if _NAME not in sys.modules:
    _spec = importlib.util.spec_from_file_location(_NAME, _PATH)
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_NAME] = _module
    _spec.loader.exec_module(_module)
sys.modules[__name__] = sys.modules[_NAME]
