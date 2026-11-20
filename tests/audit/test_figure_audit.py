import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'audit'))


class FigureAuditTests(unittest.TestCase):
    def test_tikz_extraction_tracks_source_line_and_ignores_comments(self):
        from figure_audit import extract_tikz
        source = ('% \\begin{tikzpicture} ignored\n'
                  'text\n\\begin{tikzpicture}\n\\node at (0,0) {$A$};\n'
                  '\\end{tikzpicture}\n')
        figures = extract_tikz(source)
        self.assertEqual(len(figures), 1)
        self.assertEqual(figures[0]['line'], 3)
        self.assertIn('{$A$}', figures[0]['tex'])

    def test_stext_blocks_keep_fraction_together(self):
        from figure_audit import parse_stext
        xml = '''<document><page id="page1" width="100" height="100">
        <block bbox="1 2 20 18"><line text="1+e"/><line text="4"/></block>
        <block bbox="24 2 30 10"><line text="1"/></block>
        </page></document>'''
        labels = parse_stext(xml)
        self.assertEqual(len(labels), 2)
        self.assertEqual(labels[0]['text'], '1+e / 4')
        self.assertEqual(labels[0]['bbox'], [1.0, 2.0, 20.0, 18.0])

    def test_node_log_preserves_separate_overlapping_nodes(self):
        from figure_audit import parse_node_log
        log = ('AUDIT-NODE|tikz@f@1|-7.2pt|-6.9pt|7.2pt|6.9pt\n'
               'AUDIT-NODE|tikz@f@2|-4.7pt|-6.9pt|10.4pt|6.9pt\n'
               'AUDIT-NODE|coordinate|0.0pt|0.0pt|0.0pt|0.0pt\n'
               'AUDIT-NODE|point|0.0pt|0.0pt|3.0pt|3.0pt\n')
        nodes = parse_node_log(log)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0]['bbox'], [-7.2, -6.9, 7.2, 6.9])
        self.assertGreater(find_overlap(nodes), 0)

    def test_nearby_labels_flagged_but_distant_and_different_pages_not(self):
        from figure_audit import find_collisions
        labels = [
            {'page': 1, 'text': 'A', 'bbox': [0, 0, 10, 10]},
            {'page': 1, 'text': 'B', 'bbox': [12, 0, 20, 10]},
            {'page': 1, 'text': 'C', 'bbox': [50, 0, 60, 10]},
            {'page': 2, 'text': 'D', 'bbox': [0, 0, 10, 10]},
        ]
        found = find_collisions(labels, 3)
        self.assertEqual(len(found), 1)
        self.assertEqual((found[0]['a'], found[0]['b']), ('A', 'B'))
        self.assertEqual(found[0]['distance_pt'], 2)

    def test_default_threshold_catches_close_axis_values(self):
        from figure_audit import DEFAULT_PROXIMITY_PT, find_collisions
        labels = [
            {'page': 1, 'text': '1', 'bbox': [-11.8, 63.3, -0.7, 74.9]},
            {'page': 1, 'text': '(1+e)/4', 'bbox': [-22.1, 41.6, -0.7, 57.5]},
        ]
        self.assertEqual(len(find_collisions(labels, DEFAULT_PROXIMITY_PT)), 1)

    def test_candidate_crop_maps_tikz_points_to_pdf_pixels(self):
        from figure_audit import candidate_crop
        pair = {'bbox_a': [0, 0, 10, 10], 'bbox_b': [12, 0, 20, 10]}
        picture = [-10, -10, 30, 20]
        crop = candidate_crop(pair, picture, (44, 34), dpi=72, pad_pt=2)
        self.assertEqual(crop, (10, 10, 24, 14))

    def test_pdf_block_crop_uses_top_left_pdf_coordinates(self):
        from figure_audit import candidate_crop_pdf
        pair = {'bbox_a': [0, 0, 10, 10], 'bbox_b': [12, 0, 20, 10]}
        self.assertEqual(candidate_crop_pdf(pair, (44, 34), dpi=72, pad_pt=2),
                         (0, 0, 22, 12))

    @unittest.skipUnless(shutil.which('lualatex') and shutil.which('mutool') and shutil.which('pdftoppm'),
                         'TeX, MuPDF and Poppler required')
    def test_cli_reports_candidates_and_preserves_tex(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'solution.tex'
            source.write_text('\\begin{tikzpicture}\n'
                              '\\node at (0,0) {$A$};\n'
                              '\\node at (0.1,0) {$B$};\n'
                              '\\end{tikzpicture}\n', encoding='utf-8')
            before = source.read_bytes()
            output = root / 'report'
            proc = subprocess.run([sys.executable, str(ROOT / 'audit' / 'figure_audit.py'),
                                   '--tex', str(source), '--output', str(output),
                                   '--proximity-pt', '5'], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
            self.assertEqual(report['figures'][0]['status'], 'ready')
            self.assertTrue(report['figures'][0]['candidates'])
            self.assertEqual(before, source.read_bytes())
            self.assertTrue((output / 'figure-1.png').is_file())
            self.assertTrue((output / 'candidate-1-1.png').is_file())

    @unittest.skipUnless(shutil.which('lualatex') and shutil.which('mutool') and shutil.which('pdftoppm'),
                         'TeX, MuPDF and Poppler required')
    def test_no_text_nodes_is_unavailable_not_clear(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'solution.tex'
            source.write_text('\\begin{tikzpicture}\\draw (0,0)--(1,1);\\end{tikzpicture}',
                              encoding='utf-8')
            output = root / 'report'
            proc = subprocess.run([sys.executable, str(ROOT / 'audit' / 'figure_audit.py'),
                                   '--tex', str(source), '--output', str(output)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
            self.assertEqual(report['figures'][0]['status'], 'unavailable')
            self.assertNotEqual(report['status'], 'passed')

    @unittest.skipUnless(shutil.which('lualatex') and shutil.which('mutool') and shutil.which('pdftoppm'),
                         'TeX, MuPDF and Poppler required')
    def test_standalone_uses_repository_math_shortcuts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'solution.tex'
            source.write_text('\\begin{tikzpicture}\\node {$\\R$};\\end{tikzpicture}',
                              encoding='utf-8')
            output = root / 'report'
            proc = subprocess.run([sys.executable, str(ROOT / 'audit' / 'figure_audit.py'),
                                   '--tex', str(source), '--output', str(output)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
            self.assertEqual(report['figures'][0]['status'], 'ready')

    @unittest.skipUnless(shutil.which('lualatex') and shutil.which('mutool') and shutil.which('pdftoppm'),
                         'TeX, MuPDF and Poppler required')
    def test_long_node_name_is_not_lost_to_tex_log_wrapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            name = 'auditnode' + 'x' * 75
            source = root / 'solution.tex'
            source.write_text('\\begin{tikzpicture}'
                              f'\\node ({name}) at (0,0) {{$A$}};'
                              '\\node at (0.1,0) {$B$};'
                              '\\end{tikzpicture}', encoding='utf-8')
            output = root / 'report'
            proc = subprocess.run([sys.executable, str(ROOT / 'audit' / 'figure_audit.py'),
                                   '--tex', str(source), '--output', str(output)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
            labels = report['figures'][0]['label_boxes']
            self.assertIn(name, [label['text'] for label in labels])

    @unittest.skipUnless(shutil.which('lualatex') and shutil.which('mutool') and shutil.which('pdftoppm'),
                         'TeX, MuPDF and Poppler required')
    def test_later_every_node_style_marks_capture_partial(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'solution.tex'
            source.write_text('\\begin{tikzpicture}'
                              '\\node at (0,0) {$A$};'
                              '\\tikzset{every node/.style={font=\\small}}'
                              '\\node at (0.1,0) {$B$};'
                              '\\end{tikzpicture}', encoding='utf-8')
            output = root / 'report'
            proc = subprocess.run([sys.executable, str(ROOT / 'audit' / 'figure_audit.py'),
                                   '--tex', str(source), '--output', str(output)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
            self.assertEqual(report['figures'][0]['status'], 'partial')
            self.assertGreater(report['figures'][0]['missing_node_bounds'], 0)
            self.assertIn('ノード領域の記録が不足',
                          (output / 'report.md').read_text(encoding='utf-8'))


def find_overlap(nodes):
    from figure_audit import find_collisions
    return find_collisions(nodes, 0)[0]['overlap_pt2']


if __name__ == '__main__':
    unittest.main()
