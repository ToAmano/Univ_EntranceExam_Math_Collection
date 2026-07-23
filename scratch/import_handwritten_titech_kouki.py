import os
import shutil
from pathlib import Path

def copy_titech_kouki_handwritten_pdf():
    src_dir = Path('/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions/TK_kouki')
    dest_base = Path('/Users/amano/works/research/Math-Solutions/src/titech/kouki')

    copied_count = 0
    for pdf_file in sorted(src_dir.glob('*.pdf')):
        year = pdf_file.stem
        if year.isdigit():
            target_dir = dest_base / year
            target_dir.mkdir(parents=True, exist_ok=True)
            target_pdf = target_dir / "handwritten.pdf"
            shutil.copy2(pdf_file, target_pdf)
            print(f"Copied: {pdf_file} -> {target_pdf}")
            copied_count += 1

    print(f"\nTotal handwritten PDFs copied for titech kouki: {copied_count}")

if __name__ == '__main__':
    copy_titech_kouki_handwritten_pdf()
