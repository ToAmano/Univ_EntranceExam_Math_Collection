import os
import re
from pathlib import Path

src_root = Path('/Users/amano/works/research/Math-Solutions/src')

univ_names = {
    'utokyo': '東大',
    'titech': '東工大',
    'ukyoto': '京大',
}
cat_names = {
    'zenki': '前期',
    'kouki': '後期',
}

STANDARD_COUNTS = {
    ('utokyo', 'zenki'): 6,
    ('utokyo', 'kouki'): 3,
    ('ukyoto', 'zenki'): 6,
    ('ukyoto', 'kouki'): 6,
    ('titech', 'zenki'): 5,
    ('titech', 'kouki'): 2,
}

def scan_real_incompletes():
    tasks = []

    for uni in ['utokyo', 'titech', 'ukyoto']:
        for cat in ['zenki', 'kouki']:
            cat_dir = src_root / uni / cat
            if not cat_dir.exists():
                continue
            
            for year_dir in sorted(cat_dir.iterdir()):
                if year_dir.is_dir() and year_dir.name.isdigit():
                    year = year_dir.name
                    has_handwritten = (year_dir / 'handwritten.pdf').exists()
                    
                    std_count = STANDARD_COUNTS.get((uni, cat), 6)
                    
                    for q in range(1, std_count + 1):
                        q_str = str(q)
                        q_dir = year_dir / q_str
                        sol_file = q_dir / 'solution.tex'
                        prob_file = q_dir / 'problem.tex'

                        sol_done = False
                        if sol_file.exists():
                            content = sol_file.read_text(encoding='utf-8', errors='ignore').strip()
                            lines = [l.strip() for l in content.splitlines() if l.strip() and not l.strip().startswith('%')]
                            body_lines = [l for l in lines if not l.startswith(('\\documentclass', '\\begin{document}', '\\end{document}', '\\usepackage', '\\subfiles'))]
                            body_text = "\n".join(body_lines)
                            if len(body_text) >= 40 and '解答' in body_text or '証明' in body_text or '解' in body_text:
                                sol_done = True

                        if not sol_done:
                            # handwritten.pdf または problem.tex が存在する場合、あるいは問題フォルダが存在する場合のみ有効なタスクとする
                            if has_handwritten or prob_file.exists() or q_dir.exists():
                                u_name = univ_names.get(uni, uni)
                                c_name = cat_names.get(cat, cat)
                                title = f"[TeX化] {u_name}{c_name}{year}年 第{q_str}問"
                                tasks.append({
                                    'title': title,
                                    'uni': uni,
                                    'cat': cat,
                                    'year': year,
                                    'q': q_str,
                                    'has_pdf': has_handwritten,
                                    'has_prob': prob_file.exists(),
                                    'path': f"src/{uni}/{cat}/{year}/{q_str}"
                                })

    tasks.sort(key=lambda x: (x['uni'], x['cat'], int(x['year']), int(x['q'])))
    return tasks

if __name__ == '__main__':
    t_list = scan_real_incompletes()
    print(f"Total valid incomplete tasks: {len(t_list)}\n")
    for t in t_list[:25]:
        print(f"{t['title']} (PDF: {t['has_pdf']}, Prob: {t['has_prob']})")
    print(f"... and {len(t_list) - 25} more.")
