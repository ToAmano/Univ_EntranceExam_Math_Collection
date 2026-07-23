import os
import re
import shutil
from pathlib import Path

def copy_ukyoto_kouki_handwritten_pdf():
    src_dir = Path('/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions/京都後期_整理完了')
    dest_base = Path('/Users/amano/works/research/Math-Solutions/src/ukyoto/kouki')

    copied_count = 0
    for pdf_file in sorted(src_dir.glob('*.pdf')):
        m = re.search(r'(19\d{2}|20\d{2})', pdf_file.name)
        if m:
            year = m.group(1)
            target_dir = dest_base / year
            target_dir.mkdir(parents=True, exist_ok=True)
            target_pdf = target_dir / "handwritten.pdf"
            shutil.copy2(pdf_file, target_pdf)
            print(f"Copied: {pdf_file.name} -> {target_pdf}")
            copied_count += 1

    print(f"\nTotal handwritten PDFs copied for ukyoto kouki: {copied_count}")

if __name__ == '__main__':
    copy_ukyoto_kouki_handwritten_pdf()
