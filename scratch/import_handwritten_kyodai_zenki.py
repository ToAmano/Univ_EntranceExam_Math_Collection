import os
import shutil
from pathlib import Path

def copy_handwritten_pdf():
    src_dir = Path('/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions/kyodai/zenki')
    dest_base = Path('/Users/amano/works/research/Math-Solutions/src/ukyoto/zenki')

    copied_count = 0
    for year_dir in sorted(src_dir.iterdir()):
        if year_dir.is_dir() and year_dir.name.isdigit():
            year = year_dir.name
            pdf_path = year_dir / f"kt{year}.pdf"
            if pdf_path.exists():
                target_dir = dest_base / year
                target_dir.mkdir(parents=True, exist_ok=True)
                target_pdf = target_dir / "handwritten.pdf"
                shutil.copy2(pdf_path, target_pdf)
                print(f"Copied: {pdf_path} -> {target_pdf}")
                copied_count += 1

    print(f"\nTotal handwritten PDFs copied: {copied_count}")

if __name__ == '__main__':
    copy_handwritten_pdf()
