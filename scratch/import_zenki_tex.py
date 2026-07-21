#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

WORKSPACE_ROOT = Path('/Users/amano/works/research/Math-Solutions')
SRC_DIR = WORKSPACE_ROOT / 'src'
HOMEPAGE_SOLUTIONS = Path('/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions')

ZENKI_TARGETS = [
    {
        'university': 'todai',
        'search_dir': HOMEPAGE_SOLUTIONS / 'todai' / 'todai-zenki',
    },
    {
        'university': 'titech',
        'search_dir': HOMEPAGE_SOLUTIONS / 'toukou' / 'toukou-zenki',
    },
    {
        'university': 'kyodai',
        'search_dir': HOMEPAGE_SOLUTIONS / 'kyodai' / 'zenki',
    },
]

def parse_year(year_str):
    clean_year = year_str.lstrip('t')
    if clean_year.isdigit():
        y = int(clean_year)
        if y < 100:
            return str(1900 + y) if y >= 50 else str(2000 + y)
        return str(y)
    return year_str

def parse_qnum(q_dir_name):
    # e.g., '90-1', '88-4', '13-06', 't79-1', '76-3new' -> '1', '4', '6', etc.
    m = re.search(r'-(\d+)', q_dir_name)
    if m:
        return str(int(m.group(1)))
    return None

def is_main_tex_file(filename):
    # Main file: e.g. ut-90-1.tex, t-79-1.tex, ut-88-5.tex
    # Not main: ut-90-1p.tex, ut-90-1p1.tex, ut-90-1q.tex
    if not filename.endswith('.tex'):
        return False
    base = filename[:-4]
    if base.endswith('p') or base.endswith('q') or re.search(r'p\d+$', base):
        return False
    return True

def import_zenki():
    print("=== Importing Zenki TeX Solutions (Fixed) ===")

    for target in ZENKI_TARGETS:
        uni = target['university']
        search_dir = target['search_dir']

        if not search_dir.exists():
            print(f"Directory not found: {search_dir}")
            continue

        print(f"\nProcessing {uni} zenki from {search_dir}...")

        for year_path in sorted(search_dir.iterdir()):
            if not year_path.is_dir() or year_path.name.startswith('.'):
                continue
            
            raw_year = year_path.name
            if raw_year in ('sample', 'todai-blog'):
                continue

            year = parse_year(raw_year)

            for q_path in sorted(year_path.iterdir()):
                if not q_path.is_dir() or q_path.name.startswith('.'):
                    continue

                q_num = parse_qnum(q_path.name)
                if not q_num:
                    continue

                target_dir = SRC_DIR / uni / 'zenki' / year / q_num
                target_dir.mkdir(parents=True, exist_ok=True)

                # Find main tex file and copy files
                for file_path in q_path.iterdir():
                    if file_path.is_file() and not file_path.name.startswith('.'):
                        dest_name = file_path.name

                        if is_main_tex_file(file_path.name):
                            dest_name = 'solution.tex'

                        shutil.copy2(file_path, target_dir / dest_name)
                        print(f"Copied: {file_path.relative_to(HOMEPAGE_SOLUTIONS)} -> {target_dir.relative_to(WORKSPACE_ROOT)}/{dest_name}")

    print("\n✅ Zenki Import Completed!")

if __name__ == '__main__':
    import_zenki()
