#!/usr/bin/env python3
"""Build a category PDF from namespaced temporary TeX, leaving source files alone."""

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from scratch.tex_references import namespace_references


ROOT = Path(__file__).resolve().parent.parent
BUILD_SUFFIXES = {'.aux', '.log', '.fls', '.fdb_latexmk', '.synctex.gz', '.toc', '.out'}


def prepare_book(source, destination, university, category):
    """Mirror source into destination and qualify references by question path."""
    source = Path(source).resolve()
    destination = Path(destination)
    for directory, subdirectories, files in os.walk(source):
        subdirectories[:] = [name for name in subdirectories if name not in {'out', '.latexmk'}]
        relative = Path(directory).relative_to(source)
        output_dir = destination / relative
        output_dir.mkdir(parents=True, exist_ok=True)
        for filename in files:
            if (any(filename.endswith(suffix) for suffix in BUILD_SUFFIXES)
                    or filename in {'main.pdf', 'problem.pdf', 'solution.pdf'}):
                continue
            original = Path(directory) / filename
            output = output_dir / filename
            parts = relative.parts
            if (filename in {'problem.tex', 'solution.tex'} and len(parts) == 2
                    and all(part.isdigit() for part in parts)):
                prefix = ':'.join((university, category, *parts))
                output.write_text(namespace_references(original.read_text(encoding='utf-8'), prefix), encoding='utf-8')
            else:
                output.symlink_to(original)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', help='university/category, e.g. titech/zenki')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    university, category = args.target.split('/')
    source = ROOT / 'src' / university / category
    if not source.is_dir():
        parser.error(f'no such category: {source}')
    subprocess.run(['python3', 'scratch/generate_main_tex.py', args.target], cwd=ROOT, check=True)
    with tempfile.TemporaryDirectory(prefix='math-solutions-pdf-') as temporary:
        staged = Path(temporary) / category
        prepare_book(source, staged, university, category)
        subprocess.run(['latexmk', '-lualatex', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
                       cwd=staged, check=True)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(staged / 'main.pdf', args.output)
    print(f'Built {args.output}')


if __name__ == '__main__':
    main()
