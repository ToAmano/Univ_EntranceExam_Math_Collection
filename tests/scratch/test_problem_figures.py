import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scratch import tex_to_md


class TestProblemFigures(unittest.TestCase):
    def test_problem_and_solution_figures_survive_either_conversion_order(self):
        # Reusing the image path must not overwrite the other document's diagram.
        for fallback in (False, True):
            for order in (('problem', 'solution'), ('solution', 'problem')):
                with self.subTest(fallback=fallback, order=order), tempfile.TemporaryDirectory() as tmp:
                    dest = Path(tmp)
                    def compile_diagram(code, path, macro_defs=''):
                        Path(path).write_text(code)
                        return True
                    def parse(*args, **kwargs):
                        if fallback:
                            raise ValueError('exercise fallback')
                        return original_parser(*args, **kwargs)
                    original_parser = tex_to_md.TexSoup
                    with patch.object(tex_to_md, 'compile_tikz_to_svg', compile_diagram), patch.object(tex_to_md, 'TexSoup', parse):
                        for kind in order:
                            source = dest / f'{kind}.tex'
                            source.write_text(r'\begin{document}\begin{figure}\begin{tikzpicture}\node {' + kind + r'};\end{tikzpicture}\end{figure}\end{document}')
                            tex_to_md.convert_tex_clean(str(source), str(dest / f'{kind}.md'), {'type': kind}, '/images/example', str(dest / 'images'))
                    problem = (dest / 'problem.md').read_text()
                    solution = (dest / 'solution.md').read_text()
                    self.assertIn('/images/example/fig_problem_1.svg', problem)
                    self.assertIn('id="fig_problem_1"', problem)
                    self.assertIn('/images/example/fig_1.svg', solution)
                    self.assertIn('problem', (dest / 'images/fig_problem_1.svg').read_text())
                    self.assertIn('solution', (dest / 'images/fig_1.svg').read_text())

    def test_labeled_problem_figure_links_keep_their_target(self):
        for fallback in (False, True):
            with self.subTest(fallback=fallback), tempfile.TemporaryDirectory() as tmp:
                dest = Path(tmp)
                source = dest / 'problem.tex'
                source.write_text(r'\begin{document}See \cref{fig:diagram}.\begin{figure}\begin{tikzpicture}\node {P};\end{tikzpicture}\label{fig:diagram}\end{figure}\end{document}')
                def compile_diagram(code, path, macro_defs=''):
                    Path(path).write_text(code)
                    return True
                original_parser = tex_to_md.TexSoup
                def parse(*args, **kwargs):
                    if fallback:
                        raise ValueError('exercise fallback')
                    return original_parser(*args, **kwargs)
                with patch.object(tex_to_md, 'compile_tikz_to_svg', compile_diagram), patch.object(tex_to_md, 'TexSoup', parse):
                    tex_to_md.convert_tex_clean(str(source), str(dest / 'problem.md'), {'type': 'problem'}, '/images/example', str(dest / 'images'))
                md = (dest / 'problem.md').read_text()
                self.assertIn('id="problem_fig:diagram"', md)
                self.assertIn('[図1](#problem_fig:diagram)', md)
