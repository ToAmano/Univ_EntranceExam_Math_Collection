import os
import re
import json
import subprocess
from pathlib import Path

# Open Issues で [TikZ化] を含むものを取得
res = subprocess.run(["gh", "issue", "list", "--limit", "1000", "--state", "open", "--json", "number,title,body"], capture_output=True, text=True)

if res.returncode != 0:
    print(f"Error fetching issues: {res.stderr}")
    exit(1)

issues = json.loads(res.stdout)
tikz_issues = [i for i in issues if i['title'].startswith('[TikZ化]')]

print(f"Found {len(tikz_issues)} open TikZ issues.")

# 保存用 scratch JSON
tasks_file = Path('scratch/tikz_tasks.json')
tasks = []

for issue in tikz_issues:
    title = issue['title']
    number = issue['number']
    body = issue['body']
    
    # [TikZ化] 東大前期1961年 第1問
    m = re.search(r'\[TikZ化\]\s*(東大|京大|東工大)前期(\d{4})年\s*第(\d+)問', title)
    if m:
        display_univ = m.group(1)
        year = m.group(2)
        q_num = m.group(3)
        
        univ_map = {'東大': 'utokyo', '京大': 'ukyoto', '東工大': 'titech'}
        dir_map = {'東大': '01_tokyo', '京大': '02_kyoto', '東工大': '08_titech'}
        
        univ_id = univ_map[display_univ]
        dir_name = dir_map[display_univ]
        
        tex_path = f"src/{univ_id}/zenki/{year}/{q_num}/problem.tex"
        
        # 原本画像の検索
        orig_dir = Path('scratch/tmp_download') / dir_name / year
        fig_files = list(orig_dir.glob(f"fig_{year}_{q_num}.*")) + list(orig_dir.glob(f"fig_{year}_0_{q_num}.*")) + list(orig_dir.glob(f"fig_*_{q_num}.*"))
        
        fig_path = str(fig_files[0]) if fig_files else ""
        
        tasks.append({
            'issue_number': number,
            'title': title,
            'univ_id': univ_id,
            'display_univ': display_univ,
            'year': year,
            'question': q_num,
            'tex_path': tex_path,
            'fig_path': fig_path,
            'status': 'pending'
        })

tasks_file.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Saved {len(tasks)} tasks to {tasks_file}")
