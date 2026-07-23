import subprocess
import json
import time
import re
from pathlib import Path
from filter_real_incomplete_tasks import scan_real_incompletes

def get_existing_issue_titles():
    try:
        res = subprocess.run(
            ['gh', 'issue', 'list', '--limit', '2000', '--json', 'title'],
            capture_output=True, text=True, check=True
        )
        data = json.loads(res.stdout)
        return set(item['title'] for item in data)
    except Exception as e:
        print(f"Error fetching existing issues: {e}")
        return set()

def create_issues():
    tasks = scan_real_incompletes()
    print(f"Total tasks to check: {len(tasks)}")
    
    existing_titles = get_existing_issue_titles()
    print(f"Existing issue count: {len(existing_titles)}")

    created_count = 0
    skipped_count = 0

    for idx, t in enumerate(tasks, 1):
        title = t['title']
        if title in existing_titles:
            skipped_count += 1
            continue

        body = (
            f"## タスク概要\n"
            f"手書き解答 (`handwritten.pdf`) をもとに TeX 解答 (`solution.tex`) を作成・翻刻するタスクです。\n\n"
            f"### 対象問題情報\n"
            f"- **大学**: {t['uni']}\n"
            f"- **区分**: {t['cat']}\n"
            f"- **年度**: {t['year']}年\n"
            f"- **問題番号**: 第{t['q']}問\n"
            f"- **対象ディレクトリ**: `{t['path']}`\n\n"
            f"### 作業手順\n"
            f"1. `{t['path']}/solution.tex` を作成・編集し、手書き原稿の解答を TeX 化する。\n"
            f"2. `python3 scratch/tex_to_md.py` を実行して Web サイト用 Markdown を更新する。\n"
            f"3. `npm run build` でビルドテストを実施し、コミット & Issue をクローズする。"
        )

        try:
            print(f"[{idx}/{len(tasks)}] Creating issue: {title} ...")
            cmd = ['gh', 'issue', 'create', '--title', title, '--body', body]
            subprocess.run(cmd, check=True)
            created_count += 1
            time.sleep(0.5) # API Rate Limit 回避
        except Exception as e:
            print(f"Failed to create issue for {title}: {e}")

    print(f"\nDone! Created: {created_count}, Skipped (already existed): {skipped_count}")

if __name__ == '__main__':
    create_issues()
