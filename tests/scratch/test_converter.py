import os
import shutil
import unittest
from scratch.tex_to_md import preprocess_latex

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.test_svg_path = "web/public/images/tikz/test_uni/test_uni/test_uni/test_uni/fig_1.svg"
        if os.path.exists(self.test_svg_path):
            os.remove(self.test_svg_path)

    def tearDown(self):
        if os.path.exists(self.test_svg_path):
            os.remove(self.test_svg_path)
        shutil.rmtree("web/public/images/tikz/test_uni", ignore_errors=True)
        shutil.rmtree("web/public/images/tikz/test", ignore_errors=True)

    def test_preprocess_latex(self):
        # 独自マクロの置換を検証
        latex = r"ベクトル $\bm{a}$ と実数集合 $\R$, 複素数 $\C$, 自然数 $\N$, 整数 $\Z$, 有理数 $\Q$"
        processed = preprocess_latex(latex, "test_uni", "test_uni", "test_uni", "test_uni")
        self.assertEqual(
            processed, 
            r"ベクトル $\mathbf{a}$ と実数集合 $\mathbb{R}$, 複素数 $\mathbb{C}$, 自然数 $\mathbb{N}$, 整数 $\mathbb{Z}$, 有理数 $\mathbb{Q}$"
        )

    def test_macro_boundary_check(self):
        # 境界チェックの検証
        latex = r"\Right \Zeta \Quad \R \C \N \Z \Q"
        processed = preprocess_latex(latex, "test_uni", "test_uni", "test_uni", "test_uni")
        self.assertEqual(
            processed,
            r"\Right \Zeta \Quad \mathbb{R} \mathbb{C} \mathbb{N} \mathbb{Z} \mathbb{Q}"
        )

    def test_nested_bm_and_newline_macros(self):
        # \bm の波括弧ネストバグの修正検証
        self.assertEqual(
            preprocess_latex(r"\bm{\bar{x}}", "test_uni", "test_uni", "test_uni", "test_uni"),
            r"\mathbf{\bar{x}}"
        )
        self.assertEqual(
            preprocess_latex(r"\bm{a_{i}}", "test_uni", "test_uni", "test_uni", "test_uni"),
            r"\mathbf{a_{i}}"
        )
        # 改行後のマクロ誤検出対策の検証
        self.assertEqual(
            preprocess_latex(r"\\R", "test_uni", "test_uni", "test_uni", "test_uni"),
            r"\\R"
        )
        self.assertEqual(
            preprocess_latex(r"\\C", "test_uni", "test_uni", "test_uni", "test_uni"),
            r"\\C"
        )
        self.assertEqual(
            preprocess_latex(r"\\N", "test_uni", "test_uni", "test_uni", "test_uni"),
            r"\\N"
        )
        self.assertEqual(
            preprocess_latex(r"\\Z", "test_uni", "test_uni", "test_uni", "test_uni"),
            r"\\Z"
        )
        self.assertEqual(
            preprocess_latex(r"\\Q", "test_uni", "test_uni", "test_uni", "test_uni"),
            r"\\Q"
        )
        # 混在パターンの検証
        latex = r"A \\R B \bm{\bar{y}}"
        processed = preprocess_latex(latex, "test_uni", "test_uni", "test_uni", "test_uni")
        self.assertEqual(
            processed,
            r"A \\R B \mathbf{\bar{y}}"
        )

    def test_backslash_escaping_for_blackboard_macros(self):
        # Odd number of backslashes (1, 3, 5) -> converts
        self.assertEqual(preprocess_latex(r"\R", "test_uni", "test_uni", "test_uni", "test_uni"), r"\mathbb{R}")
        self.assertEqual(preprocess_latex(r"\\\R", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\\mathbb{R}")
        self.assertEqual(preprocess_latex(r"\\\\\R", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\\\\mathbb{R}")
        self.assertEqual(preprocess_latex(r"\\\C", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\\mathbb{C}")
        self.assertEqual(preprocess_latex(r"\\\N", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\\mathbb{N}")
        self.assertEqual(preprocess_latex(r"\\\Z", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\\mathbb{Z}")
        self.assertEqual(preprocess_latex(r"\\\Q", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\\mathbb{Q}")

        # Even number of backslashes (2, 4, 6) -> does not convert
        self.assertEqual(preprocess_latex(r"\\R", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\R")
        self.assertEqual(preprocess_latex(r"\\\\R", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\\\R")
        self.assertEqual(preprocess_latex(r"\\\\\\R", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\\\\\R")
        self.assertEqual(preprocess_latex(r"\\C", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\C")
        self.assertEqual(preprocess_latex(r"\\N", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\N")
        self.assertEqual(preprocess_latex(r"\\Z", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\Z")
        self.assertEqual(preprocess_latex(r"\\Q", "test_uni", "test_uni", "test_uni", "test_uni"), r"\\Q")

    @unittest.skipUnless(shutil.which("pdflatex") and shutil.which("pdftocairo"), "pdflatex or pdftocairo not available")
    def test_tikz_extraction_and_replacement(self):
        latex = r"""
        問題文です。
        \begin{figure}[H]
          \begin{tikzpicture}
            \draw (0,0) -- (1,1);
          \end{tikzpicture}
          \caption{図}
        \end{figure}
        """
        # 置換後のテキストに LaTeX の \includegraphics が含まれているか検証
        processed = preprocess_latex(latex, "test_uni", "test_uni", "test_uni", "test_uni")
        self.assertIn(r"\includegraphics{", processed)
        self.assertIn("/Math-Solutions/images/tikz/test_uni/test_uni/test_uni/test_uni/fig_1.svg", processed)

if __name__ == '__main__':
    unittest.main()
