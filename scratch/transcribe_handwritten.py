import os
import sys
import json
import subprocess
from pathlib import Path

TASK_FILE = Path('scratch/handwritten_tasks.json')

def load_tasks():
    if not TASK_FILE.exists():
        print("Task file not found.")
        sys.exit(1)
    return json.loads(TASK_FILE.read_text())

def save_tasks(tasks):
    TASK_FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False))

def render_pdf(pdf_path, tmp_prefix):
    # Renders pdf pages to png files
    cmd = ['pdftoppm', '-png', '-r', '150', str(pdf_path), str(tmp_prefix)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error rendering PDF {pdf_path}: {res.stderr}")
        return []
    parent = Path(tmp_prefix).parent
    prefix_name = Path(tmp_prefix).name
    pages = sorted(list(parent.glob(f"{prefix_name}-*.png")))
    return [str(p) for p in pages]

def main():
    tasks = load_tasks()
    todo = [t for t in tasks if not Path(t['tex_out']).exists()]
    print(f"Total tasks: {len(tasks)}, Remaining: {len(todo)}")

if __name__ == '__main__':
    main()
