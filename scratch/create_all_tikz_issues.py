import os
import re
import json
import subprocess
import time
from pathlib import Path

tmp_dir = Path('/Users/amano/works/research/Math-Solutions/scratch/tmp_download')

UNIVS = [
    ('utokyo', '東大', '01_tokyo'),
    ('ukyoto', '京大', '02_kyoto'),
    ('titech', '東工大', '08_titech'),
]

# 既存の全 Issue タイトルを取得
print("Fetching existing GitHub Issues...")
res = subprocess.run(["gh", "issue", "list", "--limit", "2000", "--json", "title"], capture_output=True, text=True)
existing_titles = set()
if res.returncode == 0:
    data = json.loads(res.stdout)
    existing_titles = {item['title'] for item in data}
print(f"Found {len(existing_titles)} existing GitHub Issues.")

figure_tasks = []

for univ_id, display_univ, dir_name in UNIVS:
    univ_dir = tmp_dir / dir_name
    if not univ_dir.exists():
        continue
    for year_dir in sorted(univ_dir.iterdir()):
        if year_dir.is_dir() and year_dir.name.isdigit():
            year_num = int(year_dir.name)
            if year_num > 2015:
                continue
            year = year_dir.name
            
            fig_files = list(year_dir.glob('fig_*.*'))
            tex_files = list(year_dir.glob('*.tex'))
            q_with_fig = set()
            
            for fig in fig_files:
                m = re.search(r'fig_\d+_(?:0_)?(\d+)', fig.name)
                if m:
                    q_num = m.group(1)
                    q_with_fig.add(q_num)
            
            for tex in tex_files:
                if 'fig_' in tex.name or tex.name.startswith('0_'):
                    continue
                try:
                    content = tex.read_text(encoding='shift_jis', errors='ignore')
                    if '\\includegraphics' in content:
                        m = re.search(r'^(\d+)_(\d+)\.tex$', tex.name)
                        if m:
                            q_num = m.group(2)
                            q_with_fig.add(q_num)
                except Exception:
                    pass
            
            for q in sorted(q_with_fig, key=lambda x: int(x) if x.isdigit() else 99):
                title = f"[TikZ化] {display_univ}前期{year}年 第{q}问" if f"[TikZ化] {display_univ}前期{year}年 第{q}问" in existing_titles else f"[TikZ化] {display_univ}前期{year}年 第{q}問"
                figure_tasks.append({
                    'univ_id': univ_id,
                    'display_univ': display_univ,
                    'category': 'zenki',
                    'year': year,
                    'question': q,
                    'issue_title': f"[TikZ化] {display_univ}前期{year}年 第{q}問"
                })

print(f"Total figure tasks to check: {len(figure_tasks)}")

created_count = 0
skipped_count = 0

for i, task in enumerate(figure_tasks, 1):
    title = task['issue_title']
    if title in existing_titles:
        print(f"[{i}/{len(figure_tasks)}] Skipped (already exists): {title}")
        skipped_count += 1
        continue
    
    body = f"""## 概要
{task['display_univ']}前期 {task['year']}年 第{task['question']}問 に含まれる手書き図形・イラスト画像を解像度に依存しない高品質な LaTeX TikZ ベクターコード (`\\begin{{tikzpicture}} ... \\end{{tikzpicture}}`) へ書き直す。

## 対象ファイル
* TeX 原稿: `src/{task['univ_id']}/zenki/{task['year']}/{task['question']}/problem.tex`
* 原本手書き画像: `scratch/tmp_download/{UNIVS[[u[0] for u in UNIVS].index(task['univ_id'])][2]}/{task['year']}/`

## タスク内容
- [ ] 原本手書き図画像を解析・目視確認
- [ ] `problem.tex` 内の画像を TikZ ベクターコードへ修正・記述
- [ ] ピンポイント変換 (`python3 scratch/tex_to_md.py src/{task['univ_id']}/zenki/{task['year']}/{task['question']}/problem.tex`) による SVG 生成および動作検証
"""
    print(f"[{i}/{len(figure_tasks)}] Creating issue: {title} ...")
    cmd = ["gh", "issue", "create", "--title", title, "--body", body]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        created_count += 1
        existing_titles.add(title)
    else:
        print(f"  Failed: {res.stderr.strip()}")
    time.sleep(0.3)

print(f"\nDone! Created: {created_count}, Skipped: {skipped_count}")
