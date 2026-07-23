import shutil
from pathlib import Path

src_root = Path('/Users/amano/works/research/Math-Solutions/src')
web_content_root = Path('/Users/amano/works/research/Math-Solutions/web/src/content/solutions')

removed_src_dirs = 0
removed_md_files = 0

# 1. src/ 配下の 2016年以降の年度フォルダを削除
for p in src_root.rglob('*'):
    if p.is_dir() and p.name.isdigit():
        year = int(p.name)
        if year >= 2016:
            shutil.rmtree(p)
            removed_src_dirs += 1

# 2. web/src/content/solutions/ 配下の 2016年以降の Markdown ファイルを削除
if web_content_root.exists():
    for f in web_content_root.glob('*.md'):
        # 例: utokyo-zenki-2016-1-problem.md
        parts = f.name.split('-')
        for part in parts:
            if part.isdigit() and len(part) == 4:
                year = int(part)
                if year >= 2016:
                    f.unlink()
                    removed_md_files += 1
                    break

print(f"Removed {removed_src_dirs} src year directories and {removed_md_files} Markdown files (2016 and later).")
