"""
{univ}/zenki/{year}/handwritten_tex.tex（1年分をまとめて書き起こした手書き解答）を
\\section*{第N問} / \\subsection*{第N問} の見出しで大問ごとに分割し、
{univ}/zenki/{year}/{q}/solution.tex を生成する。

- 既存の {year}/{q}/solution.tex がある場合は絶対に上書きしない（skip）。
- 見出しが「第N問」に一致しない区間（年度表紙・配点表・難易度一覧など）は
  どの大問にも属さないため書き出さない（元の handwritten_tex.tex には残る）。
- 中身が空（原稿で解答欄が空欄だった等）の場合も書き出さない。
"""
import os
import re
import sys
import glob

HEADING_RE = re.compile(r'^\\(?:sub){0,1}section\*\{(.*?)\}[ \t]*$', re.MULTILINE)
QNUM_RE = re.compile(r'^第(\d+)問$')

SOLUTION_TEMPLATE = """\\documentclass[../../../../main.tex]{{subfiles}}
\\begin{{document}}

\\begin{{flushright}}
\\footnotesize\\textit{{【自動文字起こし・要確認】}}
\\end{{flushright}}

{body}

\\end{{document}}
"""


def split_content(content):
    """Returns list of (qnum:str, body:str)."""
    matches = list(HEADING_RE.finditer(content))
    results = []
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        qm = QNUM_RE.match(title)
        if not qm:
            continue
        qnum = qm.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[start:end]
        # 最後のセクションの場合、元ファイル自身の \end{document} を巻き込むので除去する
        doc_end = body.find('\\end{document}')
        if doc_end != -1:
            body = body[:doc_end]

        non_comment_lines = [l for l in body.splitlines() if not l.strip().startswith('%')]
        if not any(l.strip() for l in non_comment_lines):
            continue

        results.append((qnum, body.strip('\n')))
    return results


def process_year(univ, cat, year_dir, year, dry_run, report):
    hw_path = os.path.join(year_dir, "handwritten_tex.tex")
    if not os.path.isfile(hw_path):
        return

    content = open(hw_path, encoding="utf-8").read()
    parts = split_content(content)

    if not parts:
        return

    for qnum, body in parts:
        qdir = os.path.join(year_dir, qnum)
        target = os.path.join(qdir, "solution.tex")
        problem_path = os.path.join(qdir, "problem.tex")

        if os.path.exists(target):
            report["skipped_existing"].append(target)
            continue

        if not os.path.isfile(problem_path):
            report["no_problem_tex"].append(target)

        report["written"].append(target)
        if not dry_run:
            os.makedirs(qdir, exist_ok=True)
            with open(target, "w", encoding="utf-8") as f:
                f.write(SOLUTION_TEMPLATE.format(body=body))


def main():
    dry_run = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if args:
        univ = args[0]
        targets = [(univ, "zenki")]
    else:
        targets = [("titech", "zenki"), ("utokyo", "zenki"), ("ukyoto", "zenki")]

    report = {"written": [], "skipped_existing": [], "no_problem_tex": []}

    for univ, cat in targets:
        base = f"src/{univ}/{cat}"
        if not os.path.isdir(base):
            continue
        years = sorted([d for d in os.listdir(base) if d.isdigit() and os.path.isdir(os.path.join(base, d))], key=int)
        for year in years:
            process_year(univ, cat, os.path.join(base, year), year, dry_run, report)

    print(f"{'[DRY RUN] ' if dry_run else ''}written: {len(report['written'])}, skipped(既存優先): {len(report['skipped_existing'])}, problem.tex無し(警告): {len(report['no_problem_tex'])}")
    if report["no_problem_tex"]:
        print("\n以下は対応する problem.tex が見つからないまま solution.tex を書き出しました（要確認）:")
        for p in report["no_problem_tex"]:
            print(f"  {p}")
    if report["skipped_existing"]:
        print(f"\n既存ファイルがあったためskipしたもの: {len(report['skipped_existing'])}件")
        for p in report["skipped_existing"][:20]:
            print(f"  {p}")
        if len(report["skipped_existing"]) > 20:
            print(f"  ... 他 {len(report['skipped_existing']) - 20} 件")


if __name__ == "__main__":
    main()
