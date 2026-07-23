import os
from pathlib import Path

src_root = Path('/Users/amano/works/research/Math-Solutions/src')

# 大学・区分ごとの標準問題数
STANDARD_QUESTION_COUNTS = {
    ('utokyo', 'zenki'): 6,
    ('utokyo', 'kouki'): 3,
    ('ukyoto', 'zenki'): 6,
    ('ukyoto', 'kouki'): 6,
    ('titech', 'zenki'): 5,
    ('titech', 'kouki'): 2,
}

univ_names = {
    'utokyo': '東大',
    'titech': '東工大',
    'ukyoto': '京大',
}
cat_names = {
    'zenki': '前期',
    'kouki': '後期',
}

def analyze():
    missing_tasks = []

    # 1. 既存のフォルダ構造をスキャン
    for root, dirs, files in os.walk(src_root):
        parts = Path(root).relative_to(src_root).parts
        if len(parts) == 4 and parts[3].isdigit() and parts[3] != '0':
            uni, cat, year, q_num = parts
            sol_file = Path(root) / 'solution.tex'
            prob_file = Path(root) / 'problem.tex'

            sol_exists = sol_file.exists() and len(sol_file.read_text(encoding='utf-8', errors='ignore').strip()) > 50

            if not sol_exists:
                u_name = univ_names.get(uni, uni)
                c_name = cat_names.get(cat, cat)
                title = f"{u_name}{c_name}{year}年第{q_num}問"
                missing_tasks.append({
                    'uni': uni, 'cat': cat, 'year': year, 'q': q_num,
                    'title': title,
                    'has_prob': prob_file.exists(),
                    'path': f"src/{uni}/{cat}/{year}/{q_num}"
                })

    # 2. フォルダ自体が存在しない年度・問題のチェック (handwritten.pdf が存在する年度について)
    for uni in ['utokyo', 'titech', 'ukyoto']:
        for cat in ['zenki', 'kouki']:
            cat_dir = src_root / uni / cat
            if not cat_dir.exists():
                continue
            std_count = STANDARD_QUESTION_COUNTS.get((uni, cat), 6)
            for year_dir in sorted(cat_dir.iterdir()):
                if year_dir.is_dir() and year_dir.name.isdigit():
                    year = year_dir.name
                    for q in range(1, std_count + 1):
                        q_str = str(q)
                        q_dir = year_dir / q_str
                        sol_file = q_dir / 'solution.tex'
                        sol_exists = sol_file.exists() and len(sol_file.read_text(encoding='utf-8', errors='ignore').strip()) > 50
                        
                        if not sol_exists and not any(t['uni'] == uni and t['cat'] == cat and t['year'] == year and t['q'] == q_str for t in missing_tasks):
                            u_name = univ_names.get(uni, uni)
                            c_name = cat_names.get(cat, cat)
                            title = f"{u_name}{c_name}{year}年第{q_str}問"
                            missing_tasks.append({
                                'uni': uni, 'cat': cat, 'year': year, 'q': q_str,
                                'title': title,
                                'has_prob': (q_dir / 'problem.tex').exists(),
                                'path': f"src/{uni}/{cat}/{year}/{q_str}"
                            })

    missing_tasks.sort(key=lambda x: (x['uni'], x['cat'], int(x['year']), int(x['q'])))
    return missing_tasks

if __name__ == '__main__':
    tasks = analyze()
    print(f"Total incomplete/missing solution tasks: {len(tasks)}\n")
    for t in tasks[:40]:
        print(f"[{t['title']}] (has_prob: {t['has_prob']}) -> {t['path']}")
    print(f"\n... total {len(tasks)} tasks.")
