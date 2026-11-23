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

    def test_bf_group_becomes_bold_but_heading_and_math_are_kept(self):
        md = self.convert(
            '{\\bf [解答]}\n\n\\begin{itemize}\n\\item {\\bf 方べきの定理：} $PA \\cdot PB$ は一定．\n'
            '\\end{itemize}\n\n{\\bfseries 注意} は $\\{\\bf x\\}$ と書かない．')
        self.assertIn('## 【解答】', md)
        self.assertIn('**方べきの定理：**', md)
        self.assertIn('**注意**', md)
        self.assertNotIn('{\\bf 方べき', md)
        self.assertIn('$\\{\\bf x\\}$', md)

    def test_math_macros_are_preserved_for_mathjax(self):
        latex = r'ベクトル $\bm{a}$ と $\R,\C,\N,\Z,\Q$'
        self.assertIn(latex, self.convert(latex))

    def test_multiline_cases_stays_in_one_table_cell(self):
        latex = r'''
        \begin{tabular}{|c|c|p{8cm}|}
        \hline
        問題 & 小問 & 答え \\
        \hline
        第2問 & (2) & $\displaystyle n(\alpha)=\begin{dcases}
          1 & 0<\alpha\le 1 \\
          2 & \alpha>1
        \end{dcases}$ \\
        \hline
        \end{tabular}
        '''
        md = self.convert(latex)
        self.assertIn(r'\begin{dcases}', md)
        self.assertIn(r'2 & \alpha>1', md)
        self.assertIn(r'\end{dcases}', md)
        self.assertEqual(3, len([line for line in md.splitlines() if line.startswith('|')]))

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

    def test_bracket_display_math_keeps_following_text_in_list_item(self):
        latex = ('\\begin{enumerate}\n'
                 '  \\item 条件を示せ．\n'
                 '    \\[ a=b \\]\n'
                 '    および次の条件も示せ．\n'
                 '    \\[ c=d \\]\n'
                 '    が成り立つ．\n'
                 '  \\item 次の問\n'
                 '\\end{enumerate}')
        processed = self.convert(latex)
        self.assertIn('1.  条件を示せ．\n\n    $$', processed)
        self.assertIn('    および次の条件も示せ．\n\n    $$', processed)
        self.assertIn('    が成り立つ．\n\n2.  次の問', processed)

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

    def test_item_immediately_followed_by_japanese_text(self):
        processed = self.convert(
            r'\begin{enumerate}\item点Aを求めよ．\item点Bを求めよ．\end{enumerate}'
        )
        self.assertIn('1.  点Aを求めよ．', processed)
        self.assertIn('2.  点Bを求めよ．', processed)
        self.assertNotIn(r'\item', processed)

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

    def test_pifont_ding_converted_in_prose(self):
        latex = r'下の3条件\ding{"AC}，\ding{"AD}，\ding{"AE}を仮定する．'
        processed = self.convert(latex)
        self.assertIn('下の3条件①，②，③を仮定する．', processed)

    def test_pifont_ding_converted_in_item_label(self):
        latex = r'''
        \begin{enumerate}
          \item [\ding{"AC}] $a<0$
          \item [\ding{"AD}] $b>0$
        \end{enumerate}
        '''
        processed = self.convert(latex)
        self.assertIn('-   **①**　$a<0$', processed)
        self.assertIn('-   **②**　$b>0$', processed)

    def test_pifont_ding_decimal_and_variants(self):
        # 172 -> ①, 182 -> ❶, 51 -> ✓, curly quotes, lowercase hex
        latex = r'\ding{172} \ding{“AC”} \ding{"ac} \ding{182} \ding{51}'
        processed = self.convert(latex)
        self.assertIn('① ① ① ❶ ✓', processed)

    def test_pifont_ding_in_standalone_list_render(self):
        # Direct call to _render_list_items also converts \ding in labels
        body = r'\item[\ding{"AC}] 第一条件' + '\n' + r'\item[\ding{"AD}] 第二条件'
        rendered = tex_to_md._render_list_items(body, 0)
        self.assertIn('<div class="labeled-list">', rendered)
        self.assertIn('-   **①**　第一条件', rendered)
        self.assertIn('-   **②**　第二条件', rendered)

    def test_labeled_items_do_not_get_auto_numbers(self):
        # Issue #1304, #1305: \item[$1^\circ$] 等の独自ラベルと自動番号が二重にならない
        body = r'\item[$1^\circ$] 3辺とも違う' + '\n' + r'\item[$2^\circ$] 2等辺'
        rendered = tex_to_md._render_list_items(body, 0)
        self.assertIn('-   **$1^\\circ$**　3辺とも違う', rendered)
        self.assertNotIn('1.  ', rendered)

    def test_textbf_with_nested_braces_becomes_bold(self):
        # Issue #971: 中身に {} を含む \textbf が生の TeX のまま残っていた
        processed = self.convert(r'\textbf{$1^{\circ}$ 2回} と \textbf{$P=\dfrac{1}{8}\pi$の時}')
        self.assertIn(r'**$1^{\circ}$ 2回**', processed)
        self.assertIn(r'**$P=\dfrac{1}{8}\pi$の時**', processed)
        self.assertNotIn(r'\textbf', processed)

    def test_textbf_inside_math_is_left_for_mathjax(self):
        processed = self.convert(r'$\textbf{v}_{1}$ と本文')
        self.assertIn(r'$\textbf{v}_{1}$', processed)

    def test_underline_outside_math_becomes_html(self):
        processed = self.convert(r'\underline{\textbf{$0 \le t \le \dfrac{1}{3}$ の場合}}')
        self.assertIn(r'<u>**$0 \le t \le \dfrac{1}{3}$ の場合**</u>', processed)
        self.assertNotIn(r'\underline', processed)

    def test_quote_environment_becomes_blockquote(self):
        # Issue #898: \begin{quote} が問題文に生の TeX のまま表示されていた
        processed = self.convert('さらに，\n\\begin{quote}\n  「玉を$1$つ取り出す．」\n\\end{quote}\nという操作')
        self.assertIn('> 「玉を$1$つ取り出す．」', processed)
        self.assertNotIn(r'\begin{quote}', processed)
        self.assertNotIn(r'\end{quote}', processed)

    def test_quote_inside_list_item_keeps_indent(self):
        latex = ('\\begin{enumerate}\n  \\item 条件\n    \\begin{quote}\n      「$a_n$ が等しい」\n'
                 '    \\end{quote}\n    を満たす $a_1$\n  \\item 次の問\n\\end{enumerate}')
        processed = self.convert(latex)
        self.assertIn('    > 「$a_n$ が等しい」', processed)
        self.assertIn('2.  次の問', processed)

    def test_unlabeled_items_keep_auto_numbers(self):
        body = r'\item 第一' + '\n' + r'\item 第二'
        rendered = tex_to_md._render_list_items(body, 0)
        self.assertIn('1.  第一', rendered)
        self.assertIn('2.  第二', rendered)
        self.assertNotIn('labeled-list', rendered)

    def test_theorem_and_proof_converted_to_cards(self):
        latex = r'''
        \begin{theorem}
          任意の $n \ge 2$ に対し $P(n)$ が成り立つ．
        \end{theorem}
        \begin{proof}
          帰納法により示された．
        \end{proof}
        '''
        processed = self.convert(latex)
        self.assertIn('<div class="math-card theorem">', processed)
        self.assertIn('<div class="math-card-header">定理</div>', processed)
        self.assertIn('任意の $n \\ge 2$ に対し $P(n)$ が成り立つ．', processed)
        self.assertIn('<div class="math-card proof">', processed)
        self.assertIn('<div class="math-card-header">証明</div>', processed)
        self.assertIn('<div class="qed-symbol">■</div>', processed)
        self.assertNotIn(r'\begin{theorem}', processed)
        self.assertNotIn(r'\end{theorem}', processed)
        self.assertNotIn(r'\begin{proof}', processed)
        self.assertNotIn(r'\end{proof}', processed)

    def test_lemma_with_optional_title(self):
        latex = r'''
        \begin{lemma}[補題I]
          ベクトル等式が成り立つ．
        \end{lemma}
        '''
        processed = self.convert(latex)
        self.assertIn('<div class="math-card lemma">', processed)
        self.assertIn('<div class="math-card-header">補題I</div>', processed)
        self.assertIn('ベクトル等式が成り立つ．', processed)

    def test_proof_strips_explicit_square_and_adds_qed(self):
        latex = r'''
        \begin{proof}
          計算より示された．$\square$
        \end{proof}
        '''
        processed = self.convert(latex)
        self.assertIn('計算より示された．', processed)
        self.assertNotIn(r'$\square$', processed)
        self.assertIn('<div class="qed-symbol">■</div>', processed)

    def test_carrow_macros_in_table_become_inline_svgs(self):
        latex = r'''
        \begin{table}[htb]
          \centering
          \caption{増減表}
          \begin{tabular}{c|cccc}
            \hline
            $f(x)$ & \carrowIncreaseConvex & \carrowIncreaseConcave & \carrowDecreaseConvex & $\carrowDecreaseConcave$ \\ \hline
          \end{tabular}
        \end{table}
        '''
        md = self.convert(latex)
        for label in ('下に凸で増加', '上に凸で増加', '下に凸で減少', '上に凸で減少'):
            self.assertIn(f'aria-label="{label}"', md)
        self.assertIn('<svg class="carrow"', md)
        self.assertNotIn(r'\carrow', md)
        self.assertNotIn(r'$\searrow$', md)
        self.assertNotIn(r'$\nearrow$', md)
        self.assertNotIn('CARROWCELLPLACEHOLDER', md)

    def test_inline_tikz_in_align_converted_to_mathjax_placeholders(self):
        latex = r'''
        \begin{figure}[htb]
          \centering
          \begin{tikzpicture}
            \draw (0,0) -- (1,1);
          \end{tikzpicture}
          \caption{図}
        \end{figure}
        \begin{align}
          V &= \left(\text{
            \begin{tikzpicture}[scale=0.8]
              \draw (0,0) -- (1,0) -- (1,1) -- cycle;
            \end{tikzpicture}
          }\right) - \mathord{\vcenter{\hbox{
            \begin{tikzpicture}[scale=0.8]
              \draw (0,0) rectangle (1,1);
            \end{tikzpicture}
          }}} + \begin{tikzpicture}[scale=0.5]
            \draw (0,0) circle (0.5);
          \end{tikzpicture}
        \end{align}
        '''
        compiled = []

        def fake_compile(code, out_path, macro_defs='', **opts):
            compiled.append((Path(out_path).name, code))
            Path(out_path).parent.mkdir(parents=True, exist_ok=True)
            Path(out_path).write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="27.5pt" height="28.6pt"/>',
                encoding='utf-8',
            )
            return True

        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            source = dest / 'solution.tex'
            output = dest / 'solution.md'
            source.write_text(r'\begin{document}' + latex + r'\end{document}', encoding='utf-8')
            with patch.object(tex_to_md, 'compile_tikz_to_svg', side_effect=fake_compile):
                tex_to_md.convert_tex_clean(
                    str(source), str(output), {'type': 'solution'},
                    '/images/example', str(dest / 'images'),
                )
            md = output.read_text(encoding='utf-8')

        self.assertNotIn(r'\begin{tikzpicture}', md)
        self.assertIn('/images/example/fig_1.svg', md)
        self.assertIn(r'\class{mjx-inline-tikz}{\style{background-image:url(/images/example/inline_1.svg);}{\vcenter{\hbox{\rule{2.75em}{2.86em}}}}}', md)
        self.assertIn(r'\class{mjx-inline-tikz}{\style{background-image:url(/images/example/inline_2.svg);}{\vcenter{\hbox{\rule{2.75em}{2.86em}}}}}', md)
        self.assertIn(r'\class{mjx-inline-tikz}{\style{background-image:url(/images/example/inline_3.svg);}{\vcenter{\hbox{\rule{2.75em}{2.86em}}}}}', md)
        self.assertEqual([name for name, _ in compiled], ['inline_1.svg', 'inline_2.svg', 'inline_3.svg', 'fig_1.svg'])


if __name__ == '__main__':
    unittest.main()
