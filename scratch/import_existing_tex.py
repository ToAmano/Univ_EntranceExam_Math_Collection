#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# Base paths
WORKSPACE_ROOT = Path('/Users/amano/works/research/Math-Solutions')
SRC_DIR = WORKSPACE_ROOT / 'src'
TITECH_KOUKI_SRC = Path('/Users/amano/works/research/titech_kouki')

# Source to target mappings
MAPPINGS = [
    {
        'src_path': TITECH_KOUKI_SRC / 'TitechKouki' / 'manuscript' / 'docs',
        'target_uni': 'titech',
        'category': 'kouki',
    },
    {
        'src_path': TITECH_KOUKI_SRC / 'KyotoUKouki' / 'manuscript' / 'docs',
        'target_uni': 'kyodai',
        'category': 'kouki',
    },
    {
        'src_path': TITECH_KOUKI_SRC / 'UtokyoKouki' / 'manuscript' / 'docs',
        'target_uni': 'todai',
        'category': 'kouki',
    },
]

def import_source(mapping):
    docs_dir = mapping['src_path']
    uni = mapping['target_uni']
    cat = mapping['category']

    if not docs_dir.exists():
        print(f"Skipping non-existent path: {docs_dir}")
        return

    print(f"\n--- Importing {uni}/{cat} from {docs_dir} ---")
    problems_dir = docs_dir / 'problems'
    solutions_dir = docs_dir / 'solutions'

    # Process solutions
    if solutions_dir.exists():
        for year_dir in sorted(solutions_dir.iterdir()):
            if not year_dir.is_dir() or year_dir.name.startswith('.'):
                continue
            year = year_dir.name
            for q_dir in sorted(year_dir.iterdir()):
                if not q_dir.is_dir() or q_dir.name.startswith('.'):
                    continue
                q_num = q_dir.name

                target_dir = SRC_DIR / uni / cat / year / q_num
                target_dir.mkdir(parents=True, exist_ok=True)

                # Copy files inside q_dir (solutions.tex -> solution.tex, etc.)
                for file_path in q_dir.iterdir():
                    if file_path.is_file() and not file_path.name.startswith('.'):
                        dest_name = file_path.name
                        if dest_name == 'solutions.tex':
                            dest_name = 'solution.tex'
                        shutil.copy2(file_path, target_dir / dest_name)
                        print(f"Copied solution file: {file_path.relative_to(TITECH_KOUKI_SRC)} -> {target_dir.relative_to(WORKSPACE_ROOT)}/{dest_name}")

    # Process problems
    if problems_dir.exists():
        for year_dir in sorted(problems_dir.iterdir()):
            if not year_dir.is_dir() or year_dir.name.startswith('.'):
                continue
            year = year_dir.name
            for q_dir in sorted(year_dir.iterdir()):
                if not q_dir.is_dir() or q_dir.name.startswith('.'):
                    continue
                q_num = q_dir.name

                target_dir = SRC_DIR / uni / cat / year / q_num
                target_dir.mkdir(parents=True, exist_ok=True)

                # Copy files inside q_dir (problems.tex -> problem.tex, etc.)
                for file_path in q_dir.iterdir():
                    if file_path.is_file() and not file_path.name.startswith('.'):
                        dest_name = file_path.name
                        if dest_name == 'problems.tex':
                            dest_name = 'problem.tex'
                        shutil.copy2(file_path, target_dir / dest_name)
                        print(f"Copied problem file: {file_path.relative_to(TITECH_KOUKI_SRC)} -> {target_dir.relative_to(WORKSPACE_ROOT)}/{dest_name}")

if __name__ == '__main__':
    for mapping in MAPPINGS:
        import_source(mapping)
    print("\n✅ Import finished successfully!")
