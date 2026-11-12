"""式変形の自動検算（skills/math-solution-tex/scripts/check_math_steps.py）のテスト。

sympy と antlr4-python3-runtime==4.11 が無い環境では飛ばす。
"""
import pytest

pytest.importorskip('sympy')
pytest.importorskip('antlr4')

import importlib.util  # noqa: E402
from pathlib import Path  # noqa: E402

_PATH = Path(__file__).resolve().parents[2] / 'skills' / 'math-solution-tex' / 'scripts' / 'check_math_steps.py'
_spec = importlib.util.spec_from_file_location('check_math_steps', _PATH)
cms = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cms)


def findings(body, prose=''):
    text = prose + '\n\\begin{align}\n' + body + '\n\\end{align}\n'
    return cms.check_text(text, 'x.tex')[0]


def kinds(body, prose=''):
    return [(f['kind'], f['tier']) for f in findings(body, prose)]


def test_wrong_expansion_is_flagged():
    body = r'f &= (1-p)(8p-5)+(4p-3)^2 \\ &= 8p^2+11p+4 \\ &= 8\left(p-\dfrac{11}{16}\right)^2+\dfrac{7}{32}'
    assert ('EQ', 'B') in kinds(body)


def test_correct_chain_is_not_flagged():
    body = r'f &= (1-p)(8p-5)+(4p-3)^2 \\ &= 8p^2-11p+4 \\ &= 8\left(p-\dfrac{11}{16}\right)^2+\dfrac{7}{32}'
    assert kinds(body) == []


def test_numeric_arithmetic_error_is_tier_a():
    body = r'E &= \dfrac{6}{36}\cdot\dfrac{\sqrt{3}}{4} \\ &= \dfrac{\sqrt{3}}{36}\Bigl(\dfrac{3}{2}\Bigr) \\ &= \dfrac{3\sqrt{3}}{4}'
    assert ('EQ', 'A') in kinds(body)


def test_definitions_from_prose_are_substituted():
    prose = r'$c=\cos t,\ s=\sin t$とおく．'
    body = r'L &= (2c+4)^2+4s^2 \\ &= 4+16+16c \\ &= 20+16c'
    assert kinds(body, prose) == []


def test_evaluation_bracket_and_integral():
    body = r'I &= \int_0^{\pi/2}\dfrac{\cos 2\theta+1}{2} d\theta \\ &= \dfrac{1}{2}\left[\dfrac{\sin 2\theta}{2}+\theta\right]_{0}^{\pi/2} \\ &= \dfrac{\pi}{4}'
    assert kinds(body) == []


def test_sum_upper_limit_single_character():
    body = r'S &= \sum_{k=1}^9 99k \\ &= \dfrac{99}{2} \cdot 9 \cdot 10 \\ &= 4455'
    assert kinds(body) == []


def test_function_argument_without_parentheses():
    body = r'f &= \sin(k+1)\theta \\ &= \sin k\theta\cos\theta+\cos k\theta\sin\theta \\ &= \sin(k+1)\theta'
    assert kinds(body) == []


def test_continuation_row_starting_with_operator():
    body = r'I &= \left[-\dfrac{4}{7}c^7 + c \right]_{0}^{1} \\ &= \left[-\dfrac{4}{7} + 1\right] \\ & - \left[0\right] \\ &= \dfrac{3}{7}'
    assert kinds(body) == []


def test_conditions_with_variables_are_not_checked():
    body = r'1 &< 4s^2-1 < 2'
    assert kinds(body) == []


def test_wrong_numeric_inequality_is_flagged():
    body = r'A &= \dfrac{1}{2}\log 2 \\ &< \dfrac{15}{64} \\ &< 1'
    assert ('INEQ', 'A') in kinds(body)


def test_tikz_inside_align_is_ignored():
    body = r'S &= \text{\begin{tikzpicture}\draw (0,0) -- (1,1);\end{tikzpicture}} \\ &= 1 \\ &= 1'
    assert kinds(body) == []
