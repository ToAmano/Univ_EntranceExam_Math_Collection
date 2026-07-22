#!/usr/bin/env python3
import os
import re
from pathlib import Path

SRC_DIR = Path('/Users/amano/works/research/Math-Solutions/src')

def scan_four_spaces():
    results = []

    for tex_file in sorted(SRC_DIR.rglob('*.tex')):
        if tex_file.name.startswith('.'):
            continue

        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()

            matching_lines = []
            for idx, line in enumerate(lines, 1):
                # 行頭または文中にスペース4つ以上が存在するかチェック
                if re.search(r'^\s{4,}\S', line) or '    ' in line:
                    matching_lines.append((idx, line.rstrip('\n')))

            if matching_lines:
                rel_path = tex_file.relative_to(SRC_DIR)
                parts = rel_path.parts
                uni = parts[0] if len(parts) > 0 else ''
                cat = parts[1] if len(parts) > 1 else ''
                year = parts[2] if len(parts) > 2 else ''
                q_num = parts[3] if len(parts) > 3 else ''

                results.append({
                    'rel_path': str(rel_path),
                    'university': uni,
                    'category': cat,
                    'year': year,
                    'question': q_num,
                    'filename': tex_file.name,
                    'count': len(matching_lines),
                    'sample_line': matching_lines[0][1][:60]
                })
        except Exception as e:
            pass

    print(f"Total matching tex files: {len(results)}")
    
    # Sort by university, category, year, question
    results.sort(key=lambda x: (x['university'], x['category'], x['year'], x['question']))

    # Write summary artifact or text
    out_file = Path('/Users/amano/works/research/Math-Solutions/scratch/four_spaces_report.md')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write("# 行頭・文中にスペース4つ(    )を含む TeX ファイル一覧\n\n")
        f.write(f"該当ファイル総数: **{len(results)} 件**\n\n")
        f.write("| 大学 | 区分 | 年度 | 問題 | ファイルパス | 該当行数 | サンプル行 |\n")
        f.write("|:---|:---|:---|:---|:---|:---:|:---|...\n")
        for r in results:
            f.write(f"| {r['university']} | {r['category']} | {r['year']} | 第{r['question']}問 | `{r['rel_path']}` | {r['count']} | `{r['sample_line']}` |\n")

    print(f"Report saved to {out_file}")

if __name__ == '__main__':
    scan_four_spaces()
