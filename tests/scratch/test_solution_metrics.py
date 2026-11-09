import unittest
import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scratch.generate_solution_metrics import (
    extract_solution_lines,
    is_placeholder,
    parse_topic_tags_content,
    compute_metrics,
)


class TestSolutionMetrics(unittest.TestCase):
    def test_extract_solution_lines_basic(self):
        sample = r"""
\documentclass[../../main.tex]{subfiles}
\begin{document}

{\bf [解答]}
First line of solution.
\begin{align}
  x + y = 1 \label{eq:1}
\end{align}
% This is a full-line comment
Second line with inline comment. % comment here

\newpage
{\bf [別解]}
This should not be included.
\end{document}
"""
        lines = extract_solution_lines(sample)
        self.assertEqual(len(lines), 5)
        self.assertEqual(lines[0], "First line of solution.")
        self.assertEqual(lines[1], r"\begin{align}")
        self.assertEqual(lines[2], r"x + y = 1 \label{eq:1}")
        self.assertEqual(lines[3], r"\end{align}")
        self.assertEqual(lines[4], "Second line with inline comment.")

    def test_extract_solution_lines_with_tikz(self):
        sample = r"""
\documentclass[../../main.tex]{subfiles}
\begin{document}

{\bf [解答]}
Before figure.
\begin{figure}[htb]
  \centering
  \begin{tikzpicture}
    \draw (0,0) -- (1,1);
    \node at (0,0) {O};
  \end{tikzpicture}
  \caption{Test diagram}
\end{figure}
After figure.
\end{document}
"""
        lines = extract_solution_lines(sample)
        self.assertIn("Before figure.", lines)
        self.assertIn("After figure.", lines)
        # TikZ drawing code should be stripped
        for line in lines:
            self.assertNotIn(r"\draw", line)
            self.assertNotIn("tikzpicture", line)

    def test_extract_solution_lines_without_heading(self):
        sample = r"""
\documentclass[../../main.tex]{subfiles}
\begin{document}
Direct solution without heading.
$f(x) = x^2$
\end{document}
"""
        lines = extract_solution_lines(sample)
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], "Direct solution without heading.")
        self.assertEqual(lines[1], "$f(x) = x^2$")

    def test_is_placeholder(self):
        self.assertTrue(is_placeholder([]))
        self.assertTrue(is_placeholder(["（原稿は空欄）"]))
        self.assertTrue(is_placeholder(["（白紙）"]))
        self.assertTrue(is_placeholder(["（行列（一次変換）の問題のため，未対応）"]))
        self.assertTrue(is_placeholder(["(未解答)"]))
        self.assertTrue(is_placeholder(["（手書き解答なし）"]))
        self.assertTrue(is_placeholder([r"\null"]))
        self.assertTrue(is_placeholder([r"$\cdots$(答)"]))
        self.assertTrue(is_placeholder([r"$\cdots$(答)", r"\vspace{10pt}"]))

        # Real short solution should not be marked as placeholder
        valid_short = [
            "$a_1$のえらび方が$6$通りである．",
            r"従って,求める場合の数は$6 \cdot 3^6 = 4374$ 通りである．$\cdots$(答)",
        ]
        self.assertFalse(is_placeholder(valid_short))

    def test_parse_topic_tags_content(self):
        content = """
# Comments here
titech/kouki/1990/1: [方程式・不等式]
titech/kouki/1990/2: [三角関数, 数列]
utokyo/zenki/1981/6: [空間図形, 積分]
"""
        tags = parse_topic_tags_content(content)
        self.assertEqual(tags.get("titech/kouki/1990/1"), ["方程式・不等式"])
        self.assertEqual(tags.get("titech/kouki/1990/2"), ["三角関数", "数列"])
        self.assertEqual(tags.get("utokyo/zenki/1981/6"), ["空間図形", "積分"])

    def test_compute_metrics(self):
        records = [
            {"id": "utokyo/zenki/1981/6", "univ": "utokyo", "exam": "zenki", "year": 1981, "question": "6", "lines": 284, "is_placeholder": False},
            {"id": "utokyo/zenki/1981/1", "univ": "utokyo", "exam": "zenki", "year": 1981, "question": "1", "lines": 40, "is_placeholder": False},
            {"id": "ukyoto/kouki/2003/6", "univ": "ukyoto", "exam": "kouki", "year": 2003, "question": "6", "lines": 3, "is_placeholder": False},
            {"id": "titech/zenki/1976/6", "univ": "titech", "exam": "zenki", "year": 1976, "question": "6", "lines": 1, "is_placeholder": True},
        ]
        topic_tags = {
            "utokyo/zenki/1981/6": ["空間図形", "積分"],
            "utokyo/zenki/1981/1": ["整数"],
            "ukyoto/kouki/2003/6": ["場合の数・確率"],
        }
        res = compute_metrics(records, topic_tags)
        self.assertEqual(res["overall"]["total_problems"], 4)
        self.assertEqual(res["overall"]["valid_solutions"], 3)
        self.assertEqual(res["overall"]["pending_solutions"], 1)
        self.assertEqual(res["overall"]["min"], 3)
        self.assertEqual(res["overall"]["max"], 284)
        self.assertEqual(len(res["rankings"]["longest"]), 3)
        self.assertEqual(res["rankings"]["longest"][0]["id"], "utokyo/zenki/1981/6")
        self.assertEqual(res["rankings"]["shortest"][0]["id"], "ukyoto/kouki/2003/6")
        # Check by_field in overall and by_field_by_category
        self.assertTrue(len(res["by_field"]) > 0)
        self.assertIn("overall", res["by_field_by_category"])
        self.assertIn("utokyo_zenki", res["by_field_by_category"])
        self.assertTrue(len(res["categories"]["utokyo_zenki"]["by_field"]) > 0)
        utokyo_tags = [f["tag"] for f in res["categories"]["utokyo_zenki"]["by_field"]]
        self.assertIn("空間図形", utokyo_tags)
        self.assertIn("整数", utokyo_tags)


if __name__ == "__main__":
    unittest.main()
