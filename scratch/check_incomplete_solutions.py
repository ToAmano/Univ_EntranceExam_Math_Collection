import os
from pathlib import Path

def find_incomplete_solutions():
    src_root = Path('/Users/amano/works/research/Math-Solutions/src')
    
    univ_labels = {
        'utokyo': '東大',
        'titech': '東工大',
        'ukyoto': '京大',
    }
    cat_labels = {
        'zenki': '前期',
        'kouki': '後期',
    }

    incomplete_list = []

    for root, dirs, files in os.walk(src_root):
        parts = Path(root).relative_to(src_root).parts
        # parts: (university, category, year, question)
        if len(parts) == 4 and parts[3] != '0':
            uni, cat, year, q_num = parts
            sol_file = Path(root) / 'solution.tex'
            prob_file = Path(root) / 'problem.tex'

            is_incomplete = False
            reason = ""

            if not sol_file.exists():
                is_incomplete = True
                reason = "solution.tex が存在しない"
            else:
                content = sol_file.read_text(encoding='utf-8', errors='ignore').strip()
                # コメント行や documentclass/document 環境を除外して実際の解答本文があるかチェック
                lines = [l.strip() for l in content.splitlines() if l.strip() and not l.strip().startswith('%')]
                body_lines = [l for l in lines if not l.startswith(('\\documentclass', '\\begin{document}', '\\end{document}', '\\usepackage', '\\subfiles'))]
                
                if len(body_lines) == 0:
                    is_incomplete = True
                    reason = "solution.tex が空またはコメントのみ"
                body_text = "\n".join(body_lines)
                if len(body_text) < 30: # 非常に短いダミー
                    is_incomplete = True
                    reason = f"solution.tex の本文が極めて少ない ({len(body_text)}文字)"

            if is_incomplete:
                u_label = univ_labels.get(uni, uni)
                c_label = cat_labels.get(cat, cat)
                title = f"{u_label}{c_label}{year}年第{q_num}問"
                incomplete_list.append({
                    'university': uni,
                    'category': cat,
                    'year': year,
                    'question': q_num,
                    'title': title,
                    'path': str(Path(root).relative_to(src_root)),
                    'reason': reason
                })

    # ソート (大学, 区分, 年度, 問題番号)
    incomplete_list.sort(key=lambda x: (x['university'], x['category'], x['year'], int(x['question']) if x['question'].isdigit() else 99))
    return incomplete_list

if __name__ == '__main__':
    incompletes = find_incomplete_solutions()
    print(f"Total incomplete questions found: {len(incompletes)}\n")
    for item in incompletes[:30]:
        print(f"[{item['title']}] ({item['path']}) -> {item['reason']}")
    if len(incompletes) > 30:
        print(f"... and {len(incompletes) - 30} more.")
