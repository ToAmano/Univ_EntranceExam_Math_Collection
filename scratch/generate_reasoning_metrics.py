#!/usr/bin/env python3
"""Build descriptive problem/solution statistics from the TeX archive.

These are properties of the published text, not exam difficulty ratings.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from generate_solution_metrics import extract_solution_lines, is_placeholder, split_solution_variants

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "web/src/data/reasoning-metrics.json"
PROBLEM_TYPES = ROOT / "data/problem_types.yaml"
KINDS = {"proof", "value", "mixed", "other", "dual", "unclassified"}

PROOF = re.compile(r"(?<!図)(?:証明せよ|証明し|示せ|示し|示すこと|しめせ|確かめよ|確めよ|理由を述べよ)")
VALUE = re.compile(
    r"(?:求め(?:よ|，|、|．|。)|もとめよ|計算せよ|決定せよ|定めよ|"
    r"表せ(?!る|ば)|表わせ|あらわせ|解け|因数分解せよ|列挙せよ|"
    r"何(?:組|通り|回|個|本|秒|時間|メートル)|いくつあるか|どんな値|どのような値)"
)
DISPLAY = re.compile(
    r"\\begin\{(align\*?|equation\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}|\\\[(.*?)\\\]",
    re.DOTALL,
)
ROW_BREAK = re.compile(r"(?<!\\)\\\\(?:\[[^\]]*\])?")
EQUALITY = re.compile(r"(?<![<>=!])=(?!=)")
HEADING_COMMAND = re.compile(r"\\(subparagraph|paragraph|underline|textbf)\{|\\(item)\[")
CASE_LABEL = re.compile(r"(?:場合|とき|の時)")


def clean_tex(text: str) -> str:
    """Discard comments and figures before counting visible content."""
    text = re.sub(r"(?<!\\)%[^\n]*", "", text)
    return re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", "", text, flags=re.DOTALL)


def classify_problem(text: str) -> str:
    """Suggest a starting label for a new problem; not used for published counts."""
    body = clean_tex(text).split(r"\begin{document}")[-1].split(r"\end{document}")[0]
    if "【新課程】" in body and "【旧課程】" in body:
        return "dual"
    has_proof = bool(PROOF.search(body))
    has_value = bool(VALUE.search(body))
    if has_proof and has_value:
        return "mixed"
    if has_proof:
        return "proof"
    if has_value:
        return "value"
    if re.search(r"(?:図示せよ|描け|えがけ|かけ|加筆訂正せよ|穴埋め|□に)", body):
        return "other"
    return "unclassified"


def load_problem_types(path: Path = PROBLEM_TYPES) -> dict[str, str]:
    """Read the one-line-per-problem catalog, matching topic_tags.yaml's keys."""
    catalog = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"([a-z]+/(?:zenki|kouki)/\d{4}/\d+): (proof|value|mixed|other|dual|unclassified)(?:\s+#.*)?", line)
        if not match:
            raise ValueError(f"{path}:{number}: invalid problem type entry: {raw}")
        id_, kind = match.groups()
        if id_ in catalog:
            raise ValueError(f"{path}:{number}: duplicate problem ID: {id_}")
        catalog[id_] = kind
    return catalog


def check_problem_types(catalog: dict[str, str], paths: list[Path]) -> None:
    current = {"/".join(path.parts[-5:-1]) for path in paths}
    missing = sorted(current - catalog.keys())
    stale = sorted(catalog.keys() - current)
    invalid = sorted(id_ for id_, kind in catalog.items() if kind not in KINDS)
    if missing or stale or invalid:
        details = []
        if missing:
            details.append("missing IDs: " + ", ".join(missing[:10]) + (" ..." if len(missing) > 10 else ""))
        if stale:
            details.append("stale IDs: " + ", ".join(stale[:10]) + (" ..." if len(stale) > 10 else ""))
        if invalid:
            details.append("invalid labels: " + ", ".join(invalid[:10]))
        raise ValueError("data/problem_types.yaml: " + "; ".join(details))


def primary_solution(text: str) -> str:
    body = clean_tex(text).split(r"\begin{document}")[-1]
    start = re.search(r"(?:\{\\bf(?:series)?\s*\[解答\]\}|\\textbf\{\[解答\]\}|\[解答\])", body)
    if start:
        body = body[start.end():]
    end = re.search(r"(?:\{\\bf(?:series)?\s*\[(?:別解|解説)[^]]*\]\}|\\textbf\{\[(?:別解|解説)[^]]*\]\}|\\end\{document\})", body)
    return body[:end.start()] if end else body


def count_case_headings(body: str) -> int:
    """Count explicitly labelled branches, not mathematical cases environments.

    TeX command arguments may contain nested braces, so a flat regex misses
    headings such as ``\subparagraph{$1^{\circ}$ $a>0$の時}``.
    """
    candidates = []
    paragraphs = []
    for match in HEADING_COMMAND.finditer(body):
        command = match.group(1) or match.group(2)
        opener = "[" if command == "item" else "{"
        closer = "]" if command == "item" else "}"
        depth = 1
        index = match.end()
        while index < len(body) and depth:
            if body[index] == opener and (index == 0 or body[index - 1] != "\\"):
                depth += 1
            elif body[index] == closer and (index == 0 or body[index - 1] != "\\"):
                depth -= 1
            index += 1
        if depth:
            continue
        span = (match.start(), index)
        if command == "paragraph":
            paragraphs.append(span)
        elif CASE_LABEL.search(body[match.end():index - 1]):
            candidates.append(span)
    # A conditional \paragraph is still a subquestion heading in this corpus.
    # Nested styling commands describe one branch, not several branches.
    return sum(
        not any(outer_start <= start and end <= outer_end for outer_start, outer_end in paragraphs)
        and not any(outer_start <= start and end <= outer_end and (outer_start, outer_end) != (start, end)
                    for outer_start, outer_end in candidates)
        for start, end in candidates
    )


def measure_solution(text: str) -> dict[str, int]:
    body = primary_solution(text)
    total_equals = 0
    longest_chain = 0
    display_rows = 0
    for block in DISPLAY.finditer(body):
        math = block.group(2) or block.group(3) or ""
        run = 0
        for row in ROW_BREAK.split(math):
            row = re.sub(r"\\(?:notag|nonumber|label\{[^}]*\})", "", row)
            if not row.strip():
                continue
            display_rows += 1
            count = len(EQUALITY.findall(row))
            total_equals += count
            run = run + count if count else 0
            longest_chain = max(longest_chain, run)
    # Only explicit branch headings are counted; a cases environment can list
    # simultaneous conditions without representing a new reasoning branch.
    case_markers = count_case_headings(body)
    return {
        "equalities": total_equals,
        "longest_chain": longest_chain,
        "display_rows": display_rows,
        "case_markers": case_markers,
    }


def aggregate(records: list[dict]) -> dict:
    groups = defaultdict(list)
    for record in records:
        groups["overall"].append(record)
        groups[f"{record['univ']}_{record['exam']}"].append(record)
    result = {}
    for key, items in groups.items():
        decades = {}
        for decade in sorted({item["year"] // 10 * 10 for item in items}):
            subset = [item for item in items if item["year"] // 10 * 10 == decade]
            counts = {kind: sum(item["kind"] == kind for item in subset)
                      for kind in ("proof", "value", "mixed", "other", "dual", "unclassified")}
            classified = len(subset) - counts["unclassified"] - counts["dual"]
            decades[str(decade)] = {
                "total": len(subset),
                "classified": classified,
                "proof_including": counts["proof"] + counts["mixed"],
                "counts": counts,
            }
        result[key] = decades
    return result


def main() -> None:
    problems = []
    solutions = []
    paths = sorted((ROOT / "src").glob("*/*/*/*/problem.tex"))
    catalog = load_problem_types()
    if "--suggest-missing" in sys.argv:
        for path in paths:
            id_ = "/".join(path.parts[-5:-1])
            if id_ not in catalog:
                print(f"{id_}: {classify_problem(path.read_text(encoding='utf-8'))}")
        return
    check_problem_types(catalog, paths)
    for path in paths:
        univ, exam, year, question = path.parts[-5:-1]
        id_ = f"{univ}/{exam}/{year}/{question}"
        problems.append({"id": id_, "univ": univ, "exam": exam, "year": int(year), "question": question,
                         "kind": catalog[id_]})
        solution_path = path.with_name("solution.tex")
        if not solution_path.exists():
            continue
        for variant, section in split_solution_variants(solution_path.read_text(encoding="utf-8")):
            if is_placeholder(extract_solution_lines(section)):
                continue
            solutions.append({"id": id_, "univ": univ, "exam": exam, "year": int(year),
                              "question": question, "variant": variant, **measure_solution(section)})
    output = {"schema_version": 1, "generated_at": datetime.now(timezone.utc).isoformat(),
              "problem_count": len(problems), "solution_count": len(solutions),
              "problem_eras": aggregate(problems), "solutions": solutions}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] {OUTPUT}: {len(problems)} problems, {len(solutions)} solutions")


if __name__ == "__main__":
    main()
