import os
import re
from pathlib import Path
from datetime import date

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

# 解答列のステータスは3段階:
#   unfinish : solution.tex が空/未着手
#   transcribed (文字起こし済) : 自動判定でそれらしい内容がある（AI文字起こし直後の既定状態）
#   finish : 人間が最終チェック済み。自動生成では絶対に付与せず、
#            既存マークダウンで既に finish になっている行のみ引き継ぐ。
SOL_UNFINISH = "unfinish"
SOL_TRANSCRIBED = "文字起こし済"
SOL_FINISH = "finish"

PROB_FINISH = "finish"
PROB_UNFINISH = "unfinish"

ROW_RE = re.compile(
    r"^\|\s*(?P<year>\S+?)\s*\|\s*(?P<q>\S+(?:\s*\(全体サマリ\))?)\s*\|"
    r"\s*(?P<prob>[^|]+?)\s*\|\s*(?P<sol>[^|]+?)\s*\|"
)

# 旧フォーマット（絵文字プレフィックス付き）の status ファイルからでも
# finish 状態を正しく引き継げるように、先頭の絵文字・記号を取り除く。
_LEADING_SYMBOLS_RE = re.compile(r"^[^\w぀-ヿ一-鿿]+")


def _normalize_status_text(raw):
    return _LEADING_SYMBOLS_RE.sub('', raw).strip()


def load_existing_solution_status(out_path):
    """既存の status md から (year, q) -> 解答列の正規化済みテキスト を読み取る。
    finish を人手チェック済みとして引き継ぐために使う。"""
    prev = {}
    if not out_path.exists():
        return prev
    for line in out_path.read_text(encoding='utf-8', errors='ignore').splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        year = m.group('year').replace('年', '').strip()
        q = m.group('q').replace('第', '').replace('問', '').strip()
        prev[(year, q)] = _normalize_status_text(m.group('sol'))
    return prev


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
            # 解答ファイルの場合の完成判定（あくまで「それらしい内容がある」の判定であり、
            # 人手チェック済みかどうかは判定しない）
            return any(k in body_text for k in ['解答', '証明', '解', '方針', '求まる', '示された', 'ゆえに', 'したがって'])
        return True
    except Exception:
        return False


def solution_status_icon(sol_file, prev_status_for_row):
    """finish は既存 md で既に finish だった行のみ引き継ぐ。
    それ以外は自動判定で unfinish / transcribed のいずれか。"""
    if prev_status_for_row == SOL_FINISH:
        return SOL_FINISH
    if check_file_status(sol_file, is_solution=True):
        return SOL_TRANSCRIBED
    return SOL_UNFINISH


def generate_markdowns():
    docs_status_dir.mkdir(parents=True, exist_ok=True)
    summary_stats = []
    today = date.today().isoformat()

    for uni, cat, display_name, filename, default_q_count in CATEGORIES:
        cat_dir = src_root / uni / cat
        if not cat_dir.exists():
            continue

        out_path = docs_status_dir / filename
        prev_status = load_existing_solution_status(out_path)

        md_lines = []
        md_lines.append(f"# 問題・解答ステータス一覧: {display_name}\n")
        md_lines.append(f"更新日: `{today}`\n")
        md_lines.append(
            "解答列: `unfinish`(未着手) → `文字起こし済`(AI文字起こし・自己検証済/人手未チェック) → `finish`(人手チェック済)。"
            "`finish` は自動生成では付与されず、人間が手動で書き換えた場合のみ維持される。\n"
        )
        md_lines.append("| 年度 | 問題番号 | 問題文 (`problem.tex`) | 解答 (`solution.tex`) | 手書き原稿 (`handwritten.pdf`) | 総合ステータス |")
        md_lines.append("|:---:|:---:|:---:|:---:|:---:|:---:|")

        total_q = 0
        prob_finished = 0
        sol_transcribed = 0
        sol_human_finished = 0

        # 年度ディレクトリを取得
        years = sorted([d.name for d in cat_dir.iterdir() if d.is_dir() and d.name.isdigit()])

        for year in years:
            if int(year) > 2015:
                continue
            year_dir = cat_dir / year
            has_pdf = (year_dir / 'handwritten.pdf').exists()
            pdf_mark = "あり" if has_pdf else "なし"

            # 実際のサブフォルダ (0, 1, 2, 3...)
            # 出題数は年度によって異なる（例: 東工大前期は1995年以降おおむね4問だが
            # 1999,2012-2014年は5問）ため、既存フォルダがあればその実数に従う。
            # default_q_count はフォルダが1つも無い（未着手）年度のみのフォールバック。
            q_dirs = [d.name for d in year_dir.iterdir() if d.is_dir() and d.name.isdigit()]
            max_q = max(int(q) for q in q_dirs) if q_dirs else default_q_count

            for q in range(1, max_q + 1):
                q_str = str(q)
                q_dir = year_dir / q_str
                prob_file = q_dir / 'problem.tex'
                sol_file = q_dir / 'solution.tex'

                p_done = check_file_status(prob_file)
                s_icon = solution_status_icon(sol_file, prev_status.get((year, q_str)))

                total_q += 1
                if p_done: prob_finished += 1
                if s_icon == SOL_TRANSCRIBED: sol_transcribed += 1
                if s_icon == SOL_FINISH: sol_human_finished += 1

                p_icon = PROB_FINISH if p_done else PROB_UNFINISH
                if s_icon == SOL_FINISH and p_done:
                    st_icon = "完了"
                elif s_icon in (SOL_FINISH, SOL_TRANSCRIBED) or p_done:
                    st_icon = "未完成"
                else:
                    st_icon = "未着手"

                md_lines.append(f"| {year}年 | 第{q_str}問 | {p_icon} | {s_icon} | {pdf_mark} | {st_icon} |")

        out_path.write_text("\n".join(md_lines) + "\n", encoding='utf-8')
        sol_progress = sol_transcribed + sol_human_finished
        print(f"Generated: {out_path} (Total Questions: {total_q}, Transcribed: {sol_transcribed}, Human-finished: {sol_human_finished})")
        summary_stats.append((display_name, filename, total_q, prob_finished, sol_transcribed, sol_human_finished))

    # 全体ダッシュボード README.md の作成
    index_lines = []
    index_lines.append("# 入試数学データソース 進捗管理ダッシュボード\n")
    index_lines.append(f"更新日: `{today}`\n")
    index_lines.append("| 大学・区分 | ステータスファイル | 総問題数 | 問題文完成度 | 解答: 文字起こし済 | 解答: 人手finish | 進捗率 |")
    index_lines.append("|:---|:---|:---:|:---:|:---:|:---:|:---:|")

    for d_name, fname, t_q, p_f, s_t, s_h in summary_stats:
        rate = ((s_t + s_h) / t_q * 100) if t_q > 0 else 0
        index_lines.append(f"| **{d_name}** | [{fname}](./{fname}) | {t_q}問 | {p_f}/{t_q} | {s_t}/{t_q} | {s_h}/{t_q} | `{rate:.1f}%` |")

    gaps_path = docs_status_dir / 'transcription_gaps.md'
    if gaps_path.exists():
        index_lines.append("")
        index_lines.append("`unfinish` のまま残る箇所のうち，原稿を確認済みで転記不能と判明しているものの証跡は [transcription_gaps.md](./transcription_gaps.md) を参照。")

    (docs_status_dir / 'README.md').write_text("\n".join(index_lines) + "\n", encoding='utf-8')
    print("Generated dashboard README.md")

if __name__ == '__main__':
    generate_markdowns()
