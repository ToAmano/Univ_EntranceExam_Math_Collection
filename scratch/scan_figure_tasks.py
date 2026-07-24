import os
import re
from pathlib import Path

tmp_dir = Path('/Users/amano/works/research/Math-Solutions/scratch/tmp_download')

# (univ_key, display_univ, dir_name)
UNIVS = [
    ('utokyo', '東大', '01_tokyo'),
    ('ukyoto', '京大', '02_kyoto'),
    ('titech', '東工大', '08_titech'),
]

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
            
            # 図画像の探査 (fig_*.jpg / fig_*.png / *.jpg で 2000_1.jpg 以外の fig_)
            fig_files = list(year_dir.glob('fig_*.*'))
            
            # TeX ファイル内で \includegraphics がある問題の探査
            tex_files = list(year_dir.glob('*.tex'))
            q_with_fig = set()
            
            for fig in fig_files:
                # 例: fig_2000_1.jpg -> Q1, fig_1994_8.jpg -> Q8, fig_2001_8_1.jpg -> Q8
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
                figure_tasks.append({
                    'univ_id': univ_id,
                    'display_univ': display_univ,
                    'category': 'zenki', # デフォルト前期
                    'year': year,
                    'question': q,
                    'issue_title': f"[TikZ化] {display_univ}前期{year}年 第{q}問"
                })

print(f"Total figure tasks found (1961-2015): {len(figure_tasks)}")
for t in figure_tasks[:20]:
    print(t['issue_title'])
