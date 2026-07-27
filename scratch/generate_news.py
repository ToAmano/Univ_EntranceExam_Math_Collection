"""
git履歴（src/**/solution.tex への変更）から、Webサイトの「更新情報」欄用の
自動ニュースJSONを生成する。

各コミットについて、solution.tex への変更をファイルの Git ステータスで
"追加"（A）/"更新"（M 以降）に振り分け、大学・区分・年度・問題番号ごとに
グルーピングして出力する。手動で書くニュース（サイトデザイン変更など）は
別途 web/src/content/news/ の Astro content collection で管理し、
Web側でこのJSONとマージして表示する。

このスクリプトはビルドのたびに再実行する想定（tex_to_md.py と同様、
出力はコミットしない）。
"""
import json
import re
import subprocess
from pathlib import Path
from collections import OrderedDict

OUTPUT_PATH = Path("web/src/data/news-auto.json")

PATH_RE = re.compile(
    r"^src/(?P<university>[a-z_]+)/(?P<category>[a-z]+)/(?P<year>\d{4})/(?P<question>\d+)/solution\.tex$"
)


def run_git_log():
    result = subprocess.run(
        [
            "git", "log", "--diff-filter=AM", "--name-status",
            "--format=COMMIT_SEP|%H|%aI|%s",
            "--", "src/*/*/*/*/solution.tex",
        ],
        capture_output=True, text=True, check=True,
    )
    return result.stdout


def parse_commits(raw):
    commits = []
    current = None
    for line in raw.splitlines():
        if line.startswith("COMMIT_SEP|"):
            if current is not None:
                commits.append(current)
            _, sha, iso_date, subject = line.split("|", 3)
            current = {"commit": sha, "datetime": iso_date, "subject": subject, "changes": []}
        elif line.strip() and current is not None:
            # "A\tsrc/.../solution.tex" 形式
            parts = line.split("\t", 1)
            if len(parts) == 2:
                status, path = parts
                current["changes"].append((status.strip(), path.strip()))
    if current is not None:
        commits.append(current)
    return commits


def build_news_entries(commits):
    entries = []
    for c in commits:
        items = []
        for status, path in c["changes"]:
            m = PATH_RE.match(path)
            if not m:
                continue
            action = "added" if status == "A" else "updated"
            items.append({
                "university": m.group("university"),
                "category": m.group("category"),
                "year": m.group("year"),
                "question": m.group("question"),
                "action": action,
            })
        if not items:
            continue
        actions = set(i["action"] for i in items)
        overall_action = "added" if actions == {"added"} else "updated" if actions == {"updated"} else "mixed"
        entries.append({
            "date": c["datetime"][:10],
            "datetime": c["datetime"],
            "commit": c["commit"],
            "subject": c["subject"],
            "action": overall_action,
            "items": items,
        })
    return entries


def main():
    raw = run_git_log()
    commits = parse_commits(raw)
    entries = build_news_entries(commits)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated {OUTPUT_PATH} ({len(entries)} news entries from {len(commits)} commits)")


if __name__ == "__main__":
    main()
