#!/usr/bin/env python3
"""
scratch/lint_latex_style.py のチェック関数を使い、リポジトリ全体の
solution.tex（lint-tex.yml の実施対象と同じスコープ。problem.tex は
対象外——AGENT.md 6節参照）を走査して Markdown レポートを標準出力する。

非ブロッキングの定期レポート用（.github/workflows/lint-tex-full.yml
から呼ばれ、GitHub Issue の本文として投稿・更新される）。CI ゲートの
scratch/lint_latex_style.py と異なり、違反があっても exit code は
常に 0（レポート生成自体の失敗以外では失敗しない）。
"""
import sys
import datetime
from pathlib import Path
from collections import Counter, defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_latex_style import lint_file, REPO_ROOT, SRC_DIR  # noqa: E402

RULE_LABELS = [
    ("align* は使わない", "align* 禁止"),
    ("句読点は全角", "句読点"),
    ("の引数は必ず", "\\sqrt/\\frac/\\dfrac 裸引数"),
    ("tikzpicture は figure", "tikzpicture ネスト"),
    ("\\documentclass", "\\documentclass 不正"),
    ("\\begin{proof}", "\\begin{proof} 使用"),
    ("\\int の上下限", "\\frac/\\dfrac 添字位置"),
    ("分数は（添字位置を除き）", "\\frac/\\dfrac 添字位置"),
    ("\\caption{} がない", "\\caption 欠落"),
]


def classify(msg):
    for needle, label in RULE_LABELS:
        if needle in msg:
            return label
    return "その他"


def main():
    targets = sorted(SRC_DIR.rglob('solution.tex'))
    rule_counts = Counter()
    book_counts = defaultdict(lambda: [0, 0])  # {book: [errors, warnings]}
    worst_files = Counter()
    total_errors = 0
    total_warnings = 0

    for path in targets:
        errors, warnings = lint_file(path)
        rel = path.relative_to(REPO_ROOT)
        parts = rel.parts  # src, {univ}, {cat}, {year}, {q}, solution.tex
        book = f"{parts[1]}/{parts[2]}" if len(parts) > 2 else "?"
        book_counts[book][0] += len(errors)
        book_counts[book][1] += len(warnings)
        if errors:
            worst_files[str(rel)] += len(errors)
        for _, msg in errors:
            rule_counts[classify(msg)] += 1
            total_errors += 1
        total_warnings += len(warnings)

    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    lines = []
    lines.append("# LaTeX Lint Backlog Report")
    lines.append("")
    lines.append("_lint-tex-full.yml が自動生成・更新しています。手動編集しないでください。_")
    lines.append("")
    lines.append(f"**対象**: `src/**/solution.tex`（`problem.tex` は対象外。AGENT.md 6節参照）  ")
    lines.append(f"**最終更新**: {now}  ")
    lines.append(f"**ルール定義**: `scratch/lint_latex_style.py`（AGENT.md 8.3.6 節）")
    lines.append("")
    lines.append(f"## サマリ: エラー {total_errors} 件 / 警告 {total_warnings} 件（{len(targets)} ファイル走査）")
    lines.append("")

    lines.append("## ルール別内訳")
    lines.append("")
    lines.append("| ルール | 件数 |")
    lines.append("|---|---:|")
    for label, count in rule_counts.most_common():
        lines.append(f"| {label} | {count} |")
    if not rule_counts:
        lines.append("| (違反なし) | 0 |")
    lines.append("")

    lines.append("## 書籍別内訳")
    lines.append("")
    lines.append("| 大学/区分 | エラー | 警告 |")
    lines.append("|---|---:|---:|")
    for book in sorted(book_counts):
        e, w = book_counts[book]
        lines.append(f"| {book} | {e} | {w} |")
    lines.append("")

    if worst_files:
        lines.append("## エラー件数が多いファイル（上位10件）")
        lines.append("")
        lines.append("| ファイル | エラー件数 |")
        lines.append("|---|---:|")
        for f, c in worst_files.most_common(10):
            lines.append(f"| `{f}` | {c} |")
        lines.append("")

    print('\n'.join(lines))


if __name__ == '__main__':
    main()
