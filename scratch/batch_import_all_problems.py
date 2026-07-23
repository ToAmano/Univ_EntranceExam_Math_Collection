import os
import re
from pathlib import Path

tmp_dir = Path('/Users/amano/works/research/Math-Solutions/scratch/tmp_download')
src_root = Path('/Users/amano/works/research/Math-Solutions/src')

# 大学・アーカイブフォルダー・区分の対応マップ
UNIV_MAP = {
    '01_tokyo': 'utokyo',
    '02_kyoto': 'ukyoto',
    '08_titech': 'titech',
}

def clean_problem_tex(raw_tex):
    # プリアンブルと不要マクロの削除
    tex = re.sub(r'\\documentclass\[.*?\]\{.*?\}', '', raw_tex)
    tex = re.sub(r'\\usepackage\{.*?\}', '', tex)
    tex = re.sub(r'\\pagestyle\{.*?\}', '', tex)
    tex = re.sub(r'\\setlength\{.*?\}\{.*?\}', '', tex)
    tex = re.sub(r'\\begin\{document\}|\\end\{document\}', '', tex)
    tex = re.sub(r'\\begin\{flushleft\}|\\end\{flushleft\}', '', tex)
    tex = re.sub(r'\\huge\s*\d+', '', tex) # {\huge 1} などの問題番号の見出し

    # 行頭・行末のトリム
    lines = [l.rstrip() for l in tex.splitlines()]
    clean_body = "\n".join(lines).strip()

    # 重複する空行を縮小
    clean_body = re.sub(r'\n{3,}', '\n\n', clean_body)

    # 標準フォーマットでラッピング
    formatted = f"\\documentclass[../../../../main.tex]{{subfiles}}\n\\begin{{document}}\n\n{clean_body}\n\n\\end{{document}}\n"
    return formatted

def process_archive():
    imported_count = 0
    skipped_count = 0

    # 1. 東工大 (titech) の処理
    titech_dir = tmp_dir / '08_titech'
    if titech_dir.exists():
        for year_dir in sorted(titech_dir.iterdir()):
            if year_dir.is_dir() and year_dir.name.isdigit():
                year = year_dir.name
                # 前期 1~5問 (1961〜2014年等)
                for q in range(1, 6):
                    tex_file = year_dir / f"{year}_{q}.tex"
                    if tex_file.exists():
                        target_path = src_root / 'titech' / 'zenki' / year / str(q) / 'problem.tex'
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            raw = tex_file.read_text(encoding='shift_jis', errors='ignore')
                            formatted = clean_problem_tex(raw)
                            target_path.write_text(formatted, encoding='utf-8')
                            imported_count += 1
                        except Exception as e:
                            print(f"Error processing {tex_file}: {e}")

    # 2. 東大 (utokyo) の処理
    tokyo_dir = tmp_dir / '01_tokyo'
    if tokyo_dir.exists():
        for year_dir in sorted(tokyo_dir.iterdir()):
            if year_dir.is_dir() and year_dir.name.isdigit():
                year = year_dir.name
                # 前期 1~6問 (1961〜2014年等)
                for q in range(1, 7):
                    tex_file = year_dir / f"{year}_{q}.tex"
                    if tex_file.exists():
                        target_path = src_root / 'utokyo' / 'zenki' / year / str(q) / 'problem.tex'
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            raw = tex_file.read_text(encoding='shift_jis', errors='ignore')
                            formatted = clean_problem_tex(raw)
                            target_path.write_text(formatted, encoding='utf-8')
                            imported_count += 1
                        except Exception as e:
                            print(f"Error processing {tex_file}: {e}")

    # 3. 京大 (ukyoto) の処理
    kyoto_dir = tmp_dir / '02_kyoto'
    if kyoto_dir.exists():
        for year_dir in sorted(kyoto_dir.iterdir()):
            if year_dir.is_dir() and year_dir.name.isdigit():
                year = year_dir.name
                # 前期 1~6問 (1961〜2014年等)
                for q in range(1, 7):
                    tex_file = year_dir / f"{year}_{q}.tex"
                    if tex_file.exists():
                        target_path = src_root / 'ukyoto' / 'zenki' / year / str(q) / 'problem.tex'
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            raw = tex_file.read_text(encoding='shift_jis', errors='ignore')
                            formatted = clean_problem_tex(raw)
                            target_path.write_text(formatted, encoding='utf-8')
                            imported_count += 1
                        except Exception as e:
                            print(f"Error processing {tex_file}: {e}")

    print(f"\nSuccessfully imported and formatted {imported_count} problem.tex files!")

if __name__ == '__main__':
    process_archive()
