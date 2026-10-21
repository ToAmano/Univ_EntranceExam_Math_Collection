import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from scratch import tex_to_md


class TestFigureLayout(unittest.TestCase):
    def test_composite_keeps_all_panels_layout_and_subcaptions(self):
        figure = r'''\begin{figure}[htb]
\centering
\begin{subfigure}[b]{0.48\textwidth}
\begin{tikzpicture}\node {LEFT};\end{tikzpicture}
\caption{Left panel}\label{fig:left}
\end{subfigure}\hfill
\begin{subfigure}[b]{0.48\textwidth}
\begin{tikzpicture}\node {RIGHT};\end{tikzpicture}
\caption{Right panel}\label{fig:right}
\end{subfigure}
\caption{Whole figure}\label{fig:whole}
\end{figure}'''
        for fallback in (False, True):
            with self.subTest(fallback=fallback), tempfile.TemporaryDirectory() as tmp:
                dest = Path(tmp)
                source = dest / 'solution.tex'
                source.write_text(r'\begin{document}See \cref{fig:whole}.' + figure + r'\end{document}')
                calls = []
                def compile_diagram(code, path, macro_defs='', **kwargs):
                    calls.append((code, kwargs));Path(path).write_text(code);return True
                parser = tex_to_md.TexSoup
                def parse(*args, **kwargs):
                    if fallback:raise ValueError('exercise fallback')
                    return parser(*args, **kwargs)
                with patch.object(tex_to_md, 'compile_tikz_to_svg', compile_diagram), patch.object(tex_to_md, 'TexSoup', parse):
                    tex_to_md.convert_tex_clean(str(source), str(dest/'out.md'), {'type':'solution'}, '/images', str(dest/'images'))
                self.assertEqual(len(calls), 1)
                code, options = calls[0]
                self.assertIn('RIGHT', code)
                self.assertIn(r'\hfill', code)
                self.assertIn(r'{0.48\textwidth}', code)
                self.assertIn(r'\caption{Left panel}', code)
                self.assertIn(r'\caption{Right panel}', code)
                self.assertNotIn(r'\caption{Whole figure}', code)
                self.assertTrue(options.get('figure_layout'))
                md = (dest/'out.md').read_text()
                self.assertIn('Whole figure', md)
                self.assertIn('id="fig:whole"', md)
                self.assertIn('[図1](#fig:whole)', md)
                self.assertEqual(md.count('<img '), 1)

    def test_problem_without_outer_label_does_not_use_a_panel_label(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            source = dest/'problem.tex'
            source.write_text(r'\begin{document}\begin{figure}\begin{subfigure}{.5\textwidth}\begin{tikzpicture}\node{A};\end{tikzpicture}\caption{A}\label{fig:panel}\end{subfigure}\begin{tikzpicture}\node{B};\end{tikzpicture}\end{figure}\end{document}')
            def compile_diagram(code, path, macro_defs='', **kwargs):
                Path(path).write_text(code);return True
            with patch.object(tex_to_md, 'compile_tikz_to_svg', compile_diagram):
                tex_to_md.convert_tex_clean(str(source),str(dest/'out.md'),{'type':'problem'},'/images',str(dest/'images'))
            md = (dest/'out.md').read_text()
            self.assertIn('id="fig_problem_1"',md)
            self.assertIn('id="problem_fig:panel"',md)

    def test_composite_compile_failure_does_not_silently_drop_panels(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            source = dest/'solution.tex'
            source.write_text(r'\begin{document}\begin{figure}\begin{tikzpicture}\node{A};\end{tikzpicture}\begin{tikzpicture}\node{B};\end{tikzpicture}\end{figure}\end{document}')
            with patch.object(tex_to_md, 'compile_tikz_to_svg', return_value=False) as compile_diagram:
                with self.assertRaises(RuntimeError):
                    tex_to_md.convert_tex_clean(str(source),str(dest/'out.md'),{'type':'solution'},'/images',str(dest/'images'))
                self.assertEqual(compile_diagram.call_count,1)
            self.assertFalse((dest/'out.md').exists())

    @unittest.skipUnless(__import__('shutil').which('lualatex') and __import__('shutil').which('rsvg-convert'), 'TeX and SVG renderer required')
    def test_visible_ink_outside_the_layout_box_is_not_clipped(self):
        import subprocess
        from PIL import Image
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            svg = dest/'figure.svg'
            code = r'\begin{tikzpicture}\fill[magenta] (20,0) rectangle (21,1);\pgfresetboundingbox\useasboundingbox (0,0) rectangle (1,1);\end{tikzpicture}'
            self.assertTrue(tex_to_md.compile_tikz_to_svg(code,str(svg),figure_layout=True))
            subprocess.run(['rsvg-convert','-b','white','-o',str(dest/'figure.png'),str(svg)],check=True)
            pixels = Image.open(dest/'figure.png').convert('RGB').getdata()
            # CMYK magenta is converted through the renderer's color profile;
            # test that colored ink survived, rather than exact RGB values.
            self.assertGreater(sum(g<80 and r>g+80 and b>g+80 for r,g,b in pixels),10)

    def test_minipage_captions_are_kept_with_their_panels(self):
        code = r'\begin{figure}\begin{minipage}{.45\textwidth}\begin{tikzpicture}\node{L};\end{tikzpicture}\caption{Left case}\label{fig:left}\end{minipage}\hfill\begin{minipage}{.45\textwidth}\begin{tikzpicture}\node{R};\end{tikzpicture}\caption{Right case}\label{fig:right}\end{minipage}\end{figure}'
        body, caption, label, panels = tex_to_md.figure_layout_parts(code)
        self.assertIn(r'\caption{Left case}',body)
        self.assertIn(r'\caption{Right case}',body)
        self.assertEqual(caption,'')
        self.assertEqual(label,'')
        self.assertEqual(panels,['fig:left','fig:right'])
