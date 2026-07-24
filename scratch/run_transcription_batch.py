import os
import sys
import json
import subprocess
from pathlib import Path

TASK_FILE = Path('scratch/handwritten_tasks.json')

def load_tasks():
    return json.loads(TASK_FILE.read_text())

def update_task_status(univ, year):
    tasks = load_tasks()
    for t in tasks:
        if t['univ'] == univ and t['year'] == year:
            t['already_done'] = Path(t['tex_out']).exists()
    TASK_FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False))

def get_next_unprocessed(limit=5):
    tasks = load_tasks()
    unprocessed = []
    for t in tasks:
        tex_out = Path(t['tex_out'])
        if not tex_out.exists():
            unprocessed.append(t)
            if len(unprocessed) >= limit:
                break
    return unprocessed

if __name__ == '__main__':
    unprocessed = get_next_unprocessed(10)
    print(f"Unprocessed count: {len(unprocessed)}")
    for t in unprocessed:
        print(f"  {t['univ']} {t['year']}: PDF={t['pdf_path']} -> OUT={t['tex_out']}")
