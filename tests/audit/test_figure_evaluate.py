import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'audit'))


class FigureEvaluateTests(unittest.TestCase):
    def test_matches_pairs_only_with_matching_source_hash(self):
        from figure_evaluate import evaluate
        cases = [{'issue': 1, 'sha256': 'abc', 'expected_pairs': [
            {'figure_index': 1, 'nodes': ['A', 'B']}],
            'reviewed_nonactionable_pairs': [
                {'figure_index': 1, 'nodes': ['C', 'D']}]}]
        reports = [{'source_sha256': 'abc', 'figures': [
            {'figure_index': 1, 'status': 'ready', 'candidates': [
                {'a': 'B', 'b': 'A'}, {'a': 'C', 'b': 'D'}]}]}]
        self.assertEqual(evaluate(cases, reports)['detected_pairs'], 1)
        self.assertEqual(evaluate(cases, reports)['reviewed_nonactionable_pairs'], 1)
        reports[0]['source_sha256'] = 'changed'
        with self.assertRaises(ValueError):
            evaluate(cases, reports)


if __name__ == '__main__':
    unittest.main()
