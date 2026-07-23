import os
import re
from pathlib import Path

tmp_dir = Path('/Users/amano/works/research/Math-Solutions/scratch/tmp_download')
src_root = Path('/Users/amano/works/research/Math-Solutions/src')

def clean_problem_tex(raw_tex):
    # 1. プリアンブルと不要マクロの削除
    tex = re.sub(r'\\documentclass\[.*?\]\{.*?\}', '', raw_tex)
    tex = re.sub(r'\\usepackage\{.*?\}', '', tex)
    tex = re.sub(r'\\pagestyle\{.*?\}', '', tex)
    tex = re.sub(r'\\setlength\{.*?\}\{.*?\}', '', tex)
    tex = re.sub(r'\\begin\{document\}|\\end\{document\}', '', tex)
    tex = re.sub(r'\\begin\{flushleft\}|\\end\{flushleft\}', '', tex)
    tex = re.sub(r'\\huge\s*\d+|\\Large\s*\d+|\\large\s*\d+', '', tex) # {\huge 1} などの問題番号の見出し
    tex = re.sub(r'\{\s*\}', '', tex) # 空の中括弧 {} の削除

    # 2. description / itemize 環境を標準的な enumerate 環境へ統一・置換
    tex = re.sub(r'\\begin\{description\}', r'\\begin{enumerate}', tex)
    tex = re.sub(r'\\end\{description\}', r'\\end{enumerate}', tex)
    tex = re.sub(r'\\begin\{itemize\}', r'\\begin{enumerate}', tex)
    tex = re.sub(r'\\end\{itemize\}', r'\\end{enumerate}', tex)

    # \item[(1)] や \item[(イ)] などを標準の \item へ統一化
    tex = re.sub(r'\\item\[\s*\(?([0-9a-zA-Z1-9①-⑨一二三四五イロハニホヘトチリヌルヲ]+)\)?\s*\]', r'  \\item', tex)

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

    # 1. 東工大 (titech) の処理
    titech_dir = tmp_dir / '08_titech'
    if titech_dir.exists():
        for year_dir in sorted(titech_dir.iterdir()):
            if year_dir.is_dir() and year_dir.name.isdigit():
                year = year_dir.name
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

    print(f"\nSuccessfully imported and standardized {imported_count} problem.tex files with enumerate environment!")

if __name__ == '__main__':
    process_archive()
