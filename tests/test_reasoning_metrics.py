import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scratch"))

from generate_reasoning_metrics import (aggregate, check_problem_types, classify_problem,
                                        load_problem_types, measure_solution, primary_solution)


class ReasoningMetricsTests(unittest.TestCase):
    def test_catalog_is_authoritative_and_rejects_missing_or_stale_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalog_path = root / "problem_types.yaml"
            catalog_path.write_text("titech/zenki/2001/1: proof\n", encoding="utf-8")
            catalog = load_problem_types(catalog_path)
            self.assertEqual(catalog["titech/zenki/2001/1"], "proof")
            path = root / "src/titech/zenki/2001/1/problem.tex"
            check_problem_types(catalog, [path])
            with self.assertRaisesRegex(ValueError, "missing IDs"):
                check_problem_types({}, [path])
            with self.assertRaisesRegex(ValueError, "stale IDs"):
                check_problem_types(catalog, [])

    def test_catalog_duplicate_and_invalid_values_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "problem_types.yaml"
            path.write_text("titech/zenki/2001/1: proof\ntitech/zenki/2001/1: value\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate"):
                load_problem_types(path)
            path.write_text("titech/zenki/2001/1: calculation\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "invalid"):
                load_problem_types(path)
            path.write_text("titech/zenki/2001/1: mixed # reviewed\n", encoding="utf-8")
            self.assertEqual(load_problem_types(path)["titech/zenki/2001/1"], "mixed")

    def test_problem_classes_keep_mixed_and_unclassified_separate(self):
        self.assertEqual(classify_problem(r"\begin{document}これを示せ．\end{document}"), "proof")
        self.assertEqual(classify_problem(r"\begin{document}値を求めよ．\end{document}"), "value")
        self.assertEqual(classify_problem(r"\begin{document}\item 示せ．\item 値を求めよ．\end{document}"), "mixed")
        self.assertEqual(classify_problem(r"\begin{document}図示せよ．\end{document}"), "other")
        self.assertEqual(classify_problem("% 示せ．\n\\begin{document}値を求めよ．\\end{document}"), "value")

    def test_suggestions_cover_historical_phrasing_and_dual_curricula(self):
        self.assertEqual(classify_problem("不等式をしめせ．条件を求め，図示せよ．"), "mixed")
        self.assertEqual(classify_problem("値をもとめよ．"), "value")
        self.assertEqual(classify_problem("面積を$a$であらわせ．"), "value")
        self.assertEqual(classify_problem("この理由を述べよ．"), "proof")
        self.assertEqual(classify_problem("範囲を図示せよ．"), "other")
        self.assertEqual(classify_problem("\\paragraph{【新課程】}示せ．\\paragraph{【旧課程】}求めよ．"), "dual")
        self.assertEqual(classify_problem("表せることを示せ．"), "proof")

    def test_other_counts_as_reviewed_but_dual_is_excluded_from_rate(self):
        records = [{"kind": kind, "univ": "ukyoto", "exam": "zenki", "year": 1967}
                   for kind in ("proof", "value", "other", "dual", "unclassified")]
        era = aggregate(records)["overall"]["1960"]
        self.assertEqual(era["total"], 5)
        self.assertEqual(era["classified"], 3)
        self.assertEqual(era["proof_including"], 1)
        self.assertEqual(era["counts"]["dual"], 1)

    def test_curated_catalog_cases_and_dual_markers(self):
        catalog = load_problem_types()
        self.assertEqual(catalog["titech/kouki/2000/1"], "value")
        self.assertEqual(catalog["ukyoto/kouki/1994/1"], "mixed")
        self.assertEqual(catalog["ukyoto/kouki/1990/5"], "proof")
        self.assertEqual(catalog["titech/zenki/2010/4"], "other")
        dual = {id_ for id_, kind in catalog.items() if kind == "dual"}
        self.assertEqual(len(dual), 15)
        for id_ in dual:
            problem = Path(__file__).resolve().parents[1] / "src" / id_ / "problem.tex"
            text = problem.read_text(encoding="utf-8")
            self.assertIn("【新課程】", text)
            self.assertIn("【旧課程】", text)

    def test_only_primary_solution_is_measured(self):
        text = (r"\begin{document}{\bf [解答]}"
                r"\begin{align}a&=b\\&=c\\&=d\end{align}"
                r"\subparagraph{$a>0$の場合}"
                r"{\bf [別解]}\begin{align}x&=y=z\end{align}\end{document}")
        self.assertNotIn("x&=y", primary_solution(text))
        self.assertEqual(measure_solution(text)["equalities"], 3)
        self.assertEqual(measure_solution(text)["longest_chain"], 3)
        self.assertEqual(measure_solution(text)["case_markers"], 1)

    def test_comments_and_figures_do_not_add_counts(self):
        text = ("\\begin{document}{\\bf [解答]}\n"
                "% \\begin{align}x=y=z\\end{align}\n"
                "\\begin{tikzpicture}\\begin{align}a=b\\end{align}\\end{tikzpicture}\n"
                "\\begin{align}p=q\\end{align}\\end{document}")
        self.assertEqual(measure_solution(text)["equalities"], 1)

    def test_case_count_uses_explicit_headings_not_cases_environments(self):
        text = (r"\begin{document}{\bf [解答]}"
                r"\subparagraph{$a>0$の場合}"
                r"\subparagraph{$a=0$の場合}"
                r"\underline{\textbf{$a<0$の時}}"
                r"\begin{align}f(x)=\begin{cases}1&(x>0)\\0&(x\le0)\end{cases}\end{align}"
                r"ここで場合分けをする．\end{document}")
        self.assertEqual(measure_solution(text)["case_markers"], 3)

    def test_underlined_non_case_text_is_ignored(self):
        text = r"\begin{document}{\bf [解答]}\underline{重要な結論}\subparagraph{(1)}\end{document}"
        self.assertEqual(measure_solution(text)["case_markers"], 0)

    def test_paragraph_is_excluded_even_when_it_mentions_a_case(self):
        text = (r"\begin{document}{\bf [解答]}"
                r"\paragraph{$a>0$の場合}"
                r"\paragraph{\textbf{$a=0$の場合}}"
                r"\subparagraph{$a<0$の場合}"
                r"\end{document}")
        self.assertEqual(measure_solution(text)["case_markers"], 1)

    def test_bold_headings_and_conditional_item_labels_are_cases(self):
        text = (r"\begin{document}{\bf [解答]}"
                r"\textbf{$n=1$の時}"
                r"\item[$a>0$の場合] 計算する．"
                r"\underline{\textbf{$a=0$の場合}}"
                r"\end{document}")
        self.assertEqual(measure_solution(text)["case_markers"], 3)


if __name__ == "__main__":
    unittest.main()
