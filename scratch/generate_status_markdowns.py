import os
import re
from pathlib import Path

src_root = Path('/Users/amano/works/research/Math-Solutions/src')
docs_status_dir = Path('/Users/amano/works/research/Math-Solutions/docs/status')

CATEGORIES = [
    ('utokyo', 'zenki', '東大 前期', 'utokyo_zenki.md', 6),
    ('utokyo', 'kouki', '東大 後期', 'utokyo_kouki.md', 3),
    ('titech', 'zenki', '東工大 前期', 'titech_zenki.md', 5),
    ('titech', 'kouki', '東工大 後期', 'titech_kouki.md', 2),
    ('ukyoto', 'zenki', '京大 前期', 'ukyoto_zenki.md', 6),
    ('ukyoto', 'kouki', '京大 後期', 'ukyoto_kouki.md', 5),
]

def check_file_status(file_path, is_solution=False):
    if not file_path.exists():
        return False
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore').strip()
        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.strip().startswith('%')]
        body_lines = [l for l in lines if not l.startswith(('\\documentclass', '\\begin{document}', '\\end{document}', '\\usepackage', '\\subfiles'))]
        body_text = "\n".join(body_lines)
        if len(body_text) < 30:
            return False
        if is_solution:
            # 解答ファイルの場合の完成判定
            return any(k in body_text for k in ['解答', '証明', '解', '方針', '求まる', '示された', 'ゆえに', 'したがって'])
        return True
    except Exception:
        return False

def generate_markdowns():
    docs_status_dir.mkdir(parents=True, exist_ok=True)
    summary_stats = []

    for uni, cat, display_name, filename, default_q_count in CATEGORIES:
        cat_dir = src_root / uni / cat
        if not cat_dir.exists():
            continue

        md_lines = []
        md_lines.append(f"# 📊 問題・解答ステータス一覧: {display_name}\n")
        md_lines.append(f"更新日: `2026-07-23`\n")
        md_lines.append("| 年度 | 問題番号 | 問題文 (`problem.tex`) | 解答 (`solution.tex`) | 手書き原稿 (`handwritten.pdf`) | 総合ステータス |")
        md_lines.append("|:---:|:---:|:---:|:---:|:---:|:---:|")

        total_q = 0
        prob_finished = 0
        sol_finished = 0

        # 年度ディレクトリを取得
        years = sorted([d.name for d in cat_dir.iterdir() if d.is_dir() and d.name.isdigit()])

        for year in years:
            if int(year) > 2015:
                continue
            year_dir = cat_dir / year
            has_pdf = (year_dir / 'handwritten.pdf').exists()
            pdf_mark = "✅ あり" if has_pdf else "❌ なし"

            # 実際のサブフォルダ (0, 1, 2, 3...)
            q_dirs = [d.name for d in year_dir.iterdir() if d.is_dir() and d.name.isdigit()]
            max_q = max([int(q) for q in q_dirs] + [default_q_count]) if q_dirs else default_q_count

            # サマリ 0
            s0_prob = year_dir / '0' / 'problem.tex'
            s0_sol = year_dir / '0' / 'solution.tex'
            if s0_prob.exists() or s0_sol.exists() or (year_dir / '0').exists():
                p_st = "finish" if check_file_status(s0_prob) else "unfinish"
                s_st = "finish" if check_file_status(s0_sol, is_solution=True) else "unfinish"
                p_icon = "✅ finish" if p_st == "finish" else "❌ unfinish"
                s_icon = "✅ finish" if s_st == "finish" else "❌ unfinish"
                st_icon = "🟢 完了" if (p_st == "finish" and s_st == "finish") else "🟡 制作中"
                md_lines.append(f"| {year}年 | 0 (全体サマリ) | {p_icon} | {s_icon} | {pdf_mark} | {st_icon} |")

            for q in range(1, max_q + 1):
                q_str = str(q)
                q_dir = year_dir / q_str
                prob_file = q_dir / 'problem.tex'
                sol_file = q_dir / 'solution.tex'

                p_done = check_file_status(prob_file)
                s_done = check_file_status(sol_file, is_solution=True)

                total_q += 1
                if p_done: prob_finished += 1
                if s_done: sol_finished += 1

                p_icon = "✅ finish" if p_done else "❌ unfinish"
                s_icon = "✅ finish" if s_done else "❌ unfinish"
                st_icon = "🟢 完了" if (p_done and s_done) else "🟡 未完成" if (p_done or s_done) else "🔴 未着手"

                md_lines.append(f"| {year}年 | 第{q_str}問 | {p_icon} | {s_icon} | {pdf_mark} | {st_icon} |")

        out_path = docs_status_dir / filename
        out_path.write_text("\n".join(md_lines) + "\n", encoding='utf-8')
        print(f"Generated: {out_path} (Total Questions: {total_q}, Sol Finished: {sol_finished})")
        summary_stats.append((display_name, filename, total_q, prob_finished, sol_finished))

    # 全体ダッシュボード README.md の作成
    index_lines = []
    index_lines.append("# 🎓 入試数学データソース 進捗管理ダッシュボード\n")
    index_lines.append("| 大学・区分 | ステータスファイル | 総問題数 | 問題文完成度 | 解答完成度 | 進捗率 |")
    index_lines.append("|:---|:---|:---:|:---:|:---:|:---:|")

    for d_name, fname, t_q, p_f, s_f in summary_stats:
        rate = (s_f / t_q * 100) if t_q > 0 else 0
        index_lines.append(f"| **{d_name}** | [{fname}](./{fname}) | {t_q}問 | {p_f}/{t_q} | {s_f}/{t_q} | `{rate:.1f}%` |")

    (docs_status_dir / 'README.md').write_text("\n".join(index_lines) + "\n", encoding='utf-8')
    print("Generated dashboard README.md")

if __name__ == '__main__':
    generate_markdowns()
