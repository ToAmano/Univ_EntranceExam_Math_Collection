import os
import shutil
from pathlib import Path

def copy_titech_handwritten_pdf():
    src_dir = Path('/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions/toukou/toukou-zenki')
    dest_base = Path('/Users/amano/works/research/Math-Solutions/src/titech/zenki')

    copied_count = 0
    for folder in sorted(src_dir.iterdir()):
        if folder.is_dir() and folder.name.startswith('t') and folder.name[1:].isdigit():
            year = folder.name[1:]
            pdf_path = folder / f"t{year}.pdf"
            if pdf_path.exists():
                target_dir = dest_base / year
                target_dir.mkdir(parents=True, exist_ok=True)
                target_pdf = target_dir / "handwritten.pdf"
                shutil.copy2(pdf_path, target_pdf)
                print(f"Copied: {pdf_path} -> {target_pdf}")
                copied_count += 1

    print(f"\nTotal handwritten PDFs copied for titech zenki: {copied_count}")

if __name__ == '__main__':
    copy_titech_handwritten_pdf()
