import os
import shutil

src_solutions_dir = "/Users/amano/works/research/titech_kouki/TitechKouki/manuscript/docs/solutions"
src_problems_dir = "/Users/amano/works/research/titech_kouki/TitechKouki/manuscript/docs/problems"
target_dir = "src/sample_titech/kouki"

# 1990 ~ 2005 年の全大問・サマリをコピー対象とする
years = [str(y) for y in range(1990, 2006)]

copied_count = 0

for year in years:
    sol_year_dir = os.path.join(src_solutions_dir, year)
    if os.path.exists(sol_year_dir):
        for q in os.listdir(sol_year_dir):
            sol_q_dir = os.path.join(sol_year_dir, q)
            if os.path.isdir(sol_q_dir):
                dest_q_dir = os.path.join(target_dir, year, q)
                os.makedirs(dest_q_dir, exist_ok=True)
                
                # solution.tex
                sol_file = os.path.join(sol_q_dir, "solutions.tex")
                if os.path.exists(sol_file):
                    dest_sol_file = os.path.join(dest_q_dir, "solution.tex")
                    shutil.copy2(sol_file, dest_sol_file)
                    
                    # subfiles パス修正
                    with open(dest_sol_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = content.replace(r'\documentclass[../../../../main.tex]{subfiles}', r'\documentclass[../../main.tex]{subfiles}')
                    with open(dest_sol_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    copied_count += 1

                # problem.tex
                prob_file = os.path.join(src_problems_dir, year, q, "problems.tex")
                if os.path.exists(prob_file):
                    dest_prob_file = os.path.join(dest_q_dir, "problem.tex")
                    shutil.copy2(prob_file, dest_prob_file)
                    
                    with open(dest_prob_file, 'r', encoding='utf-8') as f:
                        p_content = f.read()
                    p_content = p_content.replace(r'\documentclass[../../../../main.tex]{subfiles}', r'\documentclass[../../main.tex]{subfiles}')
                    with open(dest_prob_file, 'w', encoding='utf-8') as f:
                        f.write(p_content)
                    copied_count += 1

print(f"Successfully copied {copied_count} TeX files into {target_dir}")
