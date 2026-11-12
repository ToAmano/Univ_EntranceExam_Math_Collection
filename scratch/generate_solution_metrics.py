#!/usr/bin/env python3
"""generate_solution_metrics.py

Scans all solution.tex files across universities, measures substantive solution line counts,
filters out placeholders/pending stubs, integrates topic tags from data/topic_tags.yaml,
and computes distributions, rankings, field summaries, and era trends.
Outputs web/src/data/solution-metrics.json.
"""

from __future__ import annotations

import glob
import json
import math
import os
import re
from datetime import datetime, timezone
from typing import Any

TOPIC_TAGS_PATH = "data/topic_tags.yaml"
OUTPUT_JSON_PATH = "web/src/data/solution-metrics.json"

HISTOGRAM_BINS = [
    (1, 15, "1–15"),
    (16, 30, "16–30"),
    (31, 45, "31–45"),
    (46, 60, "46–60"),
    (61, 75, "61–75"),
    (76, 90, "76–90"),
    (91, 120, "91–120"),
    (121, 99999, "121+"),
]

PLACEHOLDER_REGEXES = [
    r"原稿は空欄",
    r"白紙",
    r"未対応",
    r"解答なし",
    r"未解答",
    r"^\\null$",
    r"^\(?\s*(?:行列|一次変換)\s*\)?$",
]

STUB_LINE_REGEX = re.compile(
    r"^(?:"
    r"\$\\cdots\$\(答\)|"
    r"\(答\)|"
    r"\(略\)|"
    r"\\null|"
    r"\\noindent"
    r")$"
)

IGNORE_LINE_MACROS = re.compile(
    r"^(?:"
    r"\\newpage|"
    r"\\clearpage|"
    r"\\casesend|"
    r"\\vspace\{.*?\}|"
    r"\\rhead\{.*?\}|"
    r"\\setcounter\{.*?\}\{.*?\}|"
    r"\\begin\{(?:oframed|multicols)\}.*?|"
    r"\\end\{(?:oframed|multicols)\}|"
    r"\\setlength\{.*?\}\{.*?\}|"
    r"\\input\{.*?\}|"
    r"\\footnotesize\\textit\{.*?\}|"
    r"\\begin\{flushright\}|"
    r"\\end\{flushright\}"
    r")$"
)

VARIANT_HEADING = re.compile(r"\\paragraph\{【([^】]+)】\}")


def split_solution_variants(text: str) -> list[tuple[str, str]]:
    """Split a solution at explicit curriculum or Kyoto track headings."""
    matches = []
    for match in VARIANT_HEADING.finditer(text):
        heading = match.group(1)
        if heading == "新課程":
            variant = "new"
        elif heading == "旧課程":
            variant = "old"
        elif "甲" in heading and "乙" in heading and "共通" in heading:
            variant = "common"
        elif heading == "甲":
            variant = "ko"
        elif heading == "乙":
            variant = "otsu"
        else:
            continue
        matches.append((match.start(), variant))
    if not matches:
        return [("common", text)]
    return [
        (variant, text[start : matches[i + 1][0] if i + 1 < len(matches) else len(text)])
        for i, (start, variant) in enumerate(matches)
    ]


def extract_solution_lines(text: str) -> list[str]:
    """Extract substantive lines from the primary solution block."""
    m_heading = re.search(
        r"(?:\{\\bf(?:series)?\s*\[解答\]\}|\\textbf\{\[解答\]\}|\[解答\])", text
    )
    if m_heading:
        sub = text[m_heading.end() :]
    else:
        m_doc = re.search(r"\\begin\{document\}", text)
        sub = text[m_doc.end() :] if m_doc else text

    # Stop at next section heading or \end{document}
    m_end = re.search(
        r"(?:\{\\bf(?:series)?\s*\[(?:別解|解説).*?\]\}|\\textbf\{\[(?:別解|解説).*?\]\}|\\end\{document\})",
        sub,
    )
    sol_body = sub[: m_end.start()] if m_end else sub

    # Remove tikzpicture environments
    sol_no_tikz = re.sub(
        r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
        "",
        sol_body,
        flags=re.DOTALL,
    )

    lines: list[str] = []
    for raw_line in sol_no_tikz.splitlines():
        # Remove unescaped comments (% not preceded by odd number of backslashes)
        code = re.sub(r"(?<!\\)%.*$", "", raw_line).strip()
        if not code:
            continue
        if IGNORE_LINE_MACROS.match(code):
            continue
        lines.append(code)

    return lines


def is_placeholder(lines: list[str]) -> bool:
    """Determine whether a solution is empty or an unwritten placeholder."""
    if not lines:
        return True

    # Filter out formatting macros and stub lines
    cleaned_lines = [
        l for l in lines
        if not IGNORE_LINE_MACROS.match(l) and not STUB_LINE_REGEX.match(l)
    ]
    if not cleaned_lines:
        return True

    joined = " ".join(cleaned_lines)
    for pat in PLACEHOLDER_REGEXES:
        if re.search(pat, joined):
            return True

    return False


def parse_topic_tags_content(content: str) -> dict[str, list[str]]:
    """Parse topic tags YAML content into a dictionary."""
    tags: dict[str, list[str]] = {}
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^([^:]+):\s*\[(.*)\]", line)
        if m:
            key = m.group(1).strip()
            items = [x.strip() for x in m.group(2).split(",") if x.strip()]
            tags[key] = items
    return tags


def parse_topic_tags(path: str = TOPIC_TAGS_PATH) -> dict[str, list[str]]:
    """Load topic tags from YAML file."""
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return parse_topic_tags_content(f.read())


def _calc_percentile(sorted_vals: list[int], p: float) -> float:
    """Calculate p-th percentile (0.0 <= p <= 1.0) using linear interpolation."""
    if not sorted_vals:
        return 0.0
    if len(sorted_vals) == 1:
        return float(sorted_vals[0])
    idx = p * (len(sorted_vals) - 1)
    lower = math.floor(idx)
    upper = math.ceil(idx)
    if lower == upper:
        return float(sorted_vals[int(idx)])
    weight = idx - lower
    return float(sorted_vals[lower] * (1.0 - weight) + sorted_vals[upper] * weight)


def _calc_stats(vals: list[int]) -> dict[str, Any]:
    """Calculate count, min, max, mean, median, q1, q3, and histogram."""
    if not vals:
        return {
            "count": 0,
            "min": 0,
            "max": 0,
            "mean": 0.0,
            "median": 0.0,
            "q1": 0.0,
            "q3": 0.0,
            "histogram": [{"bin": label, "count": 0, "pct": 0.0} for _, _, label in HISTOGRAM_BINS],
        }

    sorted_vals = sorted(vals)
    n = len(sorted_vals)
    mean_val = round(sum(sorted_vals) / n, 1)
    median_val = round(_calc_percentile(sorted_vals, 0.5), 1)
    q1_val = round(_calc_percentile(sorted_vals, 0.25), 1)
    q3_val = round(_calc_percentile(sorted_vals, 0.75), 1)

    hist = []
    for low, high, label in HISTOGRAM_BINS:
        cnt = sum(1 for v in sorted_vals if low <= v <= high)
        pct = round(cnt / n * 100, 1)
        hist.append({"bin": label, "count": cnt, "pct": pct})

    return {
        "count": n,
        "min": sorted_vals[0],
        "max": sorted_vals[-1],
        "mean": mean_val,
        "median": median_val,
        "q1": q1_val,
        "q3": q3_val,
        "histogram": hist,
    }


def _calc_by_field(records_with_tags: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Compute per-topic descriptive statistics for the given subset of records."""
    field_data: dict[str, list[int]] = {}
    for r in records_with_tags:
        for tag in r.get("tags", []):
            field_data.setdefault(tag, []).append(r["lines"])

    by_field = []
    for tag, lines_list in field_data.items():
        if not lines_list:
            continue
        sorted_l = sorted(lines_list)
        by_field.append(
            {
                "tag": tag,
                "count": len(lines_list),
                "mean": round(sum(sorted_l) / len(sorted_l), 1),
                "median": round(_calc_percentile(sorted_l, 0.5), 1),
                "min": sorted_l[0],
                "max": sorted_l[-1],
            }
        )
    by_field.sort(key=lambda x: (-x["count"], -x["mean"], x["tag"]))
    return by_field


def compute_metrics(
    records: list[dict[str, Any]], topic_tags: dict[str, list[str]]
) -> dict[str, Any]:
    """Compute complete statistical summary across all dimensions."""
    valid_records = [r for r in records if not r["is_placeholder"]]
    pending_records = [r for r in records if r["is_placeholder"]]

    all_vals = [r["lines"] for r in valid_records]
    overall_stats = _calc_stats(all_vals)
    overall_stats["total_problems"] = len(records)
    overall_stats["valid_solutions"] = len(valid_records)
    overall_stats["pending_solutions"] = len(pending_records)

    # Attach topic tags to valid records
    valid_with_tags = []
    for r in valid_records:
        r_copy = dict(r)
        r_copy["tags"] = topic_tags.get(r["id"], [])
        valid_with_tags.append(r_copy)

    # 6 Categories
    cat_keys = [
        ("utokyo_zenki", "utokyo", "zenki", "東大前期"),
        ("utokyo_kouki", "utokyo", "kouki", "東大後期"),
        ("ukyoto_zenki", "ukyoto", "zenki", "京大前期"),
        ("ukyoto_kouki", "ukyoto", "kouki", "京大後期"),
        ("titech_zenki", "titech", "zenki", "東工大前期"),
        ("titech_kouki", "titech", "kouki", "東工大後期"),
    ]

    categories: dict[str, Any] = {}
    for cat_key, u, e, label in cat_keys:
        cat_all = [r for r in records if r["univ"] == u and r["exam"] == e]
        cat_valid = [r for r in cat_all if not r["is_placeholder"]]
        cat_stats = _calc_stats([r["lines"] for r in cat_valid])
        cat_stats["label"] = label
        cat_stats["univ"] = u
        cat_stats["exam"] = e
        cat_stats["total_problems"] = len(cat_all)
        cat_stats["valid_solutions"] = len(cat_valid)
        cat_stats["pending_solutions"] = len(cat_all) - len(cat_valid)

        # Per-category topic breakdown
        cat_tagged = [r for r in valid_with_tags if r["univ"] == u and r["exam"] == e]
        cat_stats["by_field"] = _calc_by_field(cat_tagged)
        categories[cat_key] = cat_stats

    # TOP 10 Rankings
    sorted_longest = sorted(valid_with_tags, key=lambda x: (-x["lines"], x["year"], x["question"]))
    sorted_shortest = sorted(valid_with_tags, key=lambda x: (x["lines"], x["year"], x["question"]))

    longest_top10 = sorted_longest[:10]
    shortest_top10 = sorted_shortest[:10]

    # By Field (Topic) - Overall and by-category mapping
    overall_by_field = _calc_by_field(valid_with_tags)
    by_field_by_category: dict[str, list[dict[str, Any]]] = {
        "overall": overall_by_field,
    }
    for cat_key in categories:
        by_field_by_category[cat_key] = categories[cat_key]["by_field"]

    # Annual totals keep entrance exam sessions and curriculum/track variants separate.
    year_groups: dict[tuple[str, str, int], list[dict[str, Any]]] = {}
    for record in valid_records:
        year_groups.setdefault((record["univ"], record["exam"], record["year"]), []).append(record)

    by_year = []
    for (univ, exam, year), group in sorted(year_groups.items()):
        variants = {r.get("variant", "common") for r in group}
        if variants & {"new", "old"}:
            tracks = ("new", "old")
        elif variants & {"ko", "otsu"}:
            tracks = ("ko", "otsu")
        else:
            tracks = ("common",)
        for variant in tracks:
            included = [r for r in group if r.get("variant", "common") in ("common", variant)]
            total = sum(r["lines"] for r in included)
            by_year.append({
                "category": f"{univ}_{exam}", "year": year, "variant": variant,
                "count": len(included), "total_lines": total,
                "mean": round(total / len(included), 1) if included else None,
            })

    # Historical Era Trends (by decade: 1960s, 1970s, 1980s, 1990s, 2000s, 2010s)
    decades = [
        (1960, 1969, "1960年代"),
        (1970, 1979, "1970年代"),
        (1980, 1989, "1980年代"),
        (1990, 1999, "1990年代"),
        (2000, 2009, "2000年代"),
        (2010, 2019, "2010年代"),
    ]

    by_era = []
    for start_yr, end_yr, label in decades:
        era_records = [
            r for r in valid_records if start_yr <= r["year"] <= end_yr
        ]
        if not era_records:
            continue

        def avg_for_category(univ_name: str, exam_name: str) -> float | None:
            sub = [r["lines"] for r in era_records if r["univ"] == univ_name and r["exam"] == exam_name]
            return round(sum(sub) / len(sub), 1) if sub else None

        all_era_lines = [r["lines"] for r in era_records]
        by_era.append(
            {
                "era": label,
                "start_year": start_yr,
                "end_year": end_yr,
                "count": len(era_records),
                "mean": round(sum(all_era_lines) / len(all_era_lines), 1),
                "median": round(_calc_percentile(sorted(all_era_lines), 0.5), 1),
                "utokyo_zenki": avg_for_category("utokyo", "zenki"),
                "utokyo_kouki": avg_for_category("utokyo", "kouki"),
                "ukyoto_zenki": avg_for_category("ukyoto", "zenki"),
                "ukyoto_kouki": avg_for_category("ukyoto", "kouki"),
                "titech_zenki": avg_for_category("titech", "zenki"),
                "titech_kouki": avg_for_category("titech", "kouki"),
            }
        )

    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "overall": overall_stats,
        "categories": categories,
        "rankings": {
            "longest": longest_top10,
            "shortest": shortest_top10,
        },
        "by_field": overall_by_field,
        "by_field_by_category": by_field_by_category,
        "by_era": by_era,
        "by_year": by_year,
    }


def main() -> None:
    topic_tags = parse_topic_tags(TOPIC_TAGS_PATH)

    files = sorted(glob.glob("src/**/solution.tex", recursive=True))
    records: list[dict[str, Any]] = []

    for path in files:
        parts = path.split("/")
        if len(parts) != 6:
            continue
        _, univ, exam, year_str, q_str, _ = parts
        if q_str == "0":
            continue  # Summary file

        try:
            year = int(year_str)
        except ValueError:
            continue

        with open(path, encoding="utf-8") as f:
            text = f.read()

        for variant, section in split_solution_variants(text):
            lines = extract_solution_lines(section)
            is_ph = is_placeholder(lines)

            records.append({
                "id": f"{univ}/{exam}/{year}/{q_str}",
                "univ": univ,
                "exam": exam,
                "year": year,
                "question": q_str,
                "lines": len(lines),
                "variant": variant,
                "is_placeholder": is_ph,
            })

    metrics = compute_metrics(records, topic_tags)

    os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)

    print(
        f"[OK] Generated {OUTPUT_JSON_PATH}: "
        f"{metrics['overall']['valid_solutions']} valid solutions, "
        f"{metrics['overall']['pending_solutions']} pending solutions."
    )


if __name__ == "__main__":
    main()
