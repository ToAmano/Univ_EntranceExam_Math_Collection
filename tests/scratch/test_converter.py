import unittest
from scratch.tex_to_md import preprocess_latex

class TestConverter(unittest.TestCase):
    def test_preprocess_latex(self):
        # 独自マクロの置換を検証
        latex = r"ベクトル $\bm{a}$ と実数集合 $\R$, 複素数 $\C$, 自然数 $\N$, 整数 $\Z$, 有理数 $\Q$"
        processed = preprocess_latex(latex)
        self.assertEqual(
            processed, 
            r"ベクトル $\mathbf{a}$ と実数集合 $\mathbb{R}$, 複素数 $\mathbb{C}$, 自然数 $\mathbb{N}$, 整数 $\mathbb{Z}$, 有理数 $\mathbb{Q}$"
        )

    def test_macro_boundary_check(self):
        # 境界チェックの検証
        latex = r"\Right \Zeta \Quad \R \C \N \Z \Q"
        processed = preprocess_latex(latex)
        self.assertEqual(
            processed,
            r"\Right \Zeta \Quad \mathbb{R} \mathbb{C} \mathbb{N} \mathbb{Z} \mathbb{Q}"
        )

    def test_nested_bm_and_newline_macros(self):
        # \bm の波括弧ネストバグの修正検証
        self.assertEqual(
            preprocess_latex(r"\bm{\bar{x}}"),
            r"\mathbf{\bar{x}}"
        )
        self.assertEqual(
            preprocess_latex(r"\bm{a_{i}}"),
            r"\mathbf{a_{i}}"
        )
        # 改行後のマクロ誤検出対策の検証
        self.assertEqual(
            preprocess_latex(r"\\R"),
            r"\\R"
        )
        self.assertEqual(
            preprocess_latex(r"\\C"),
            r"\\C"
        )
        self.assertEqual(
            preprocess_latex(r"\\N"),
            r"\\N"
        )
        self.assertEqual(
            preprocess_latex(r"\\Z"),
            r"\\Z"
        )
        self.assertEqual(
            preprocess_latex(r"\\Q"),
            r"\\Q"
        )
        # 混在パターンの検証
        latex = r"A \\R B \bm{\bar{y}}"
        processed = preprocess_latex(latex)
        self.assertEqual(
            processed,
            r"A \\R B \mathbf{\bar{y}}"
        )

if __name__ == '__main__':
    unittest.main()
