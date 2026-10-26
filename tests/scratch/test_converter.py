"""Regression tests for the current TeX-to-Markdown entry point.

Math macros remain in Markdown for MathJax; figures become HTML images.
"""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scratch import tex_to_md


class TestConverter(unittest.TestCase):
    def convert(self, latex):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            source = dest / 'solution.tex'
            output = dest / 'solution.md'
            source.write_text(
                r'\begin{document}' + latex + r'\end{document}',
                encoding='utf-8',
            )
            tex_to_md.convert_tex_clean(
                str(source), str(output), {'type': 'solution'},
                '/images/example', str(dest / 'images'),
            )
            return output.read_text(encoding='utf-8')

    def test_math_macros_are_preserved_for_mathjax(self):
        latex = r'ベクトル $\bm{a}$ と $\R,\C,\N,\Z,\Q$'
        self.assertIn(latex, self.convert(latex))

    def test_macro_boundaries_are_preserved(self):
        latex = r'$\Rightarrow \Zeta \Quad \R \C \N \Z \Q$'
        self.assertIn(latex, self.convert(latex))

    def test_nested_bold_macros_are_preserved(self):
        latex = r'$\bm{\bar{x}} + \bm{a_{i}}$'
        self.assertIn(latex, self.convert(latex))

    def test_backslashes_in_math_are_preserved(self):
        # Line breaks before a macro must survive without consuming a slash.
        for macro in ('R', 'C', 'N', 'Z', 'Q'):
            for count in range(1, 7):
                with self.subTest(macro=macro, count=count):
                    latex = '$a ' + '\\' * count + macro + '$'
                    self.assertIn(latex, self.convert(latex))

    def test_display_math_in_list_keeps_its_boundaries(self):
        latex = r'''
        \begin{align}u&=0\end{align}
        \begin{enumerate}
        \item first
        \begin{align}a&=1\end{align}
        \item second
        \begin{align}b&=2\end{align}
        \end{enumerate}
        after the list
        \begin{align}v&=3\end{align}
        '''
        processed = self.convert(latex)
        self.assertIn('1.  first\n\n    $$\n    \\begin{align}', processed)
        self.assertIn('2.  second\n\n    $$\n    \\begin{align}', processed)
        self.assertIn('    \\end{align}\n    $$\n\n2.', processed)
        self.assertIn('after the list', processed)

    def test_labeled_display_math_keeps_dollar_delimiters_on_own_lines(self):
        latex = r'''
        \begin{align}x&=1\label{eq:1}\end{align}
        following text
        \begin{align}y&=2\end{align}
        '''
        processed = self.convert(latex)
        self.assertIn('<span id="eq:1"></span>\n\n$$\n\\begin{align}', processed)
        self.assertIn('$$\n\n        following text', processed)

    def test_adjacent_enumerate_environments_remain_separate_lists(self):
        latex = r'''
        \begin{enumerate}
        \item definition one
        \item definition two
        \end{enumerate}
        \begin{enumerate}
        \item question one
        \item question two
        \end{enumerate}
        '''
        processed = self.convert(latex)
        self.assertRegex(processed, r'2\.  definition two\s+<!--.*?-->\s+1\.  question one')

    def test_tikz_is_replaced_with_html_image(self):
        latex = r'''
        問題文です。
        \begin{figure}[H]
          \begin{tikzpicture}
            \draw (0,0) -- (1,1);
          \end{tikzpicture}
          \caption{図}
        \end{figure}
        '''

        def compile_diagram(code, path, macro_defs=''):
            self.assertIn(r'\draw (0,0) -- (1,1);', code)
            Path(path).write_text('<svg/>', encoding='utf-8')
            return True

        with patch.object(tex_to_md, 'compile_tikz_to_svg', side_effect=compile_diagram) as compiler:
            processed = self.convert(latex)
        compiler.assert_called_once()
        self.assertIn('<img ', processed)
        self.assertIn('src="/images/example/fig_1.svg"', processed)
        self.assertRegex(processed, r'<figcaption>\s*図 1: 図\s*</figcaption>')
        self.assertNotIn(r'\begin{tikzpicture}', processed)
        self.assertNotIn(r'\includegraphics', processed)


if __name__ == '__main__':
    unittest.main()
