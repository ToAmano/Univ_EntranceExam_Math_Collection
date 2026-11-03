# CI LaTeX Compilation Check Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Provide an automated CI workflow and Python CLI tool to verify that modified LaTeX files (`problem.tex` and `solution.tex`) compile cleanly without errors in an isolated environment.

**Architecture:** A standalone Python script `scratch/check_tex_compile.py` discovers changed files using `git diff`, isolates builds within temporary directories using `latexmk -lualatex -outdir=...`, and reports concise errors from the LaTeX log. A GitHub Actions workflow `.github/workflows/compile-tex.yml` executes this script on `push` and `pull_request` targeting `src/**/*.tex` using the `paperist/texlive-ja:latest` Docker image.

**Tech Stack:** Python 3 (standard library: `argparse`, `subprocess`, `tempfile`, `pathlib`, `re`, `time`), LaTeX / LuaLaTeX (`latexmk`), GitHub Actions, Docker (`paperist/texlive-ja:latest`).

## Global Constraints

- Scope: Target files are strictly `src/**/solution.tex` and `src/**/problem.tex` (no `main.tex`, no `handwritten_tex.tex`).
- Cleanliness: Zero untracked or auxiliary files left in the git working tree after compilation.
- Isolation: All intermediate compilation artifacts (`.aux`, `.log`, `.pdf`, `.fls`, `.synctex.gz`) must live only in temporary directories.
- Fast Fail & Error Snippets: On compile failure, output concise error lines from the log rather than flooding output with LaTeX font/package loading logs.

---

### Task 1: Changed Files Detection and Target Filtering

**Files:**
- Create: `scratch/check_tex_compile.py`
- Test: `tests/scratch/test_check_tex_compile.py`

**Interfaces:**
- Produces:
  - `is_target_tex_file(path: str | Path) -> bool`: returns True if file path ends with `solution.tex` or `problem.tex` under `src/`.
  - `get_changed_tex_files(base: str | None = None, head: str | None = None, changed_only: bool = False, repo_root: Path | None = None) -> list[Path]`: returns list of existing target `.tex` files modified between `base` and `head`, or in working tree.

- [ ] **Step 1: Write the failing tests for target detection and diff filtering**

Create `tests/scratch/test_check_tex_compile.py`:
```python
from pathlib import Path
import pytest
from scratch import check_tex_compile as checker


def test_is_target_tex_file():
    assert checker.is_target_tex_file("src/ukyoto/zenki/1996/1/solution.tex") is True
    assert checker.is_target_tex_file("src/ukyoto/zenki/1996/1/problem.tex") is True
    assert checker.is_target_tex_file("src/utokyo/kouki/2000/3/solution.tex") is True
    assert checker.is_target_tex_file("src/ukyoto/zenki/main.tex") is False
    assert checker.is_target_tex_file("src/ukyoto/zenki/1996/handwritten_tex.tex") is False
    assert checker.is_target_tex_file("docs/status/transcription_gaps.md") is False
    assert checker.is_target_tex_file("other/dir/solution.tex") is False


def test_filter_existing_target_files(tmp_path):
    src_dir = tmp_path / "src" / "test_univ" / "zenki" / "1990" / "1"
    src_dir.mkdir(parents=True)
    sol = src_dir / "solution.tex"
    prob = src_dir / "problem.tex"
    other = src_dir / "notes.txt"
    sol.write_text("% sol", encoding="utf-8")
    prob.write_text("% prob", encoding="utf-8")
    other.write_text("text", encoding="utf-8")

    raw_paths = [
        str(sol.relative_to(tmp_path)),
        str(prob.relative_to(tmp_path)),
        str(other.relative_to(tmp_path)),
        "src/test_univ/zenki/1990/1/deleted.tex",
    ]
    targets = checker.filter_target_files(raw_paths, repo_root=tmp_path)
    assert targets == [sol, prob]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/scratch/test_check_tex_compile.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'scratch.check_tex_compile'`

- [ ] **Step 3: Implement target detection and filtering functions**

Create `scratch/check_tex_compile.py`:
```python
#!/usr/bin/env python3
"""CI LaTeX compilation checker for modified solution.tex and problem.tex files."""

import os
import re
import subprocess
from pathlib import Path
from typing import List, Optional

TARGET_PATTERN = re.compile(r"^src/.+/(solution|problem)\.tex$")


def is_target_tex_file(path: str | Path) -> bool:
    """Return True if path matches src/**/solution.tex or src/**/problem.tex."""
    normalized = str(path).replace("\\", "/").lstrip("./")
    return bool(TARGET_PATTERN.match(normalized))


def filter_target_files(file_paths: List[str], repo_root: Optional[Path] = None) -> List[Path]:
    """Filter list of string paths to existing target TeX files."""
    root = (repo_root or Path.cwd()).resolve()
    valid_targets: List[Path] = []
    for p in file_paths:
        if is_target_tex_file(p):
            full_path = (root / p).resolve()
            if full_path.is_file():
                valid_targets.append(full_path)
    return sorted(list(dict.fromkeys(valid_targets)))


def get_git_diff_files(base: Optional[str] = None, head: Optional[str] = None, repo_root: Optional[Path] = None) -> List[str]:
    """Retrieve list of modified/added files using git diff."""
    root = (repo_root or Path.cwd()).resolve()
    if base and head:
        cmd = ["git", "diff", "--diff-filter=ACMR", "--name-only", base, head]
    elif base:
        cmd = ["git", "diff", "--diff-filter=ACMR", "--name-only", base]
    else:
        cmd = ["git", "diff", "--diff-filter=ACMR", "--name-only", "HEAD"]
    result = subprocess.run(cmd, cwd=root, capture_output=True, text=True, check=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def get_working_tree_changed_files(repo_root: Optional[Path] = None) -> List[str]:
    """Retrieve uncommitted and unstaged changed files in the working tree."""
    root = (repo_root or Path.cwd()).resolve()
    cmd = ["git", "status", "--porcelain", "-uall"]
    result = subprocess.run(cmd, cwd=root, capture_output=True, text=True, check=True)
    files: List[str] = []
    for line in result.stdout.splitlines():
        if len(line) >= 4:
            status = line[:2]
            if "D" not in status:
                filename = line[3:].strip()
                if " -> " in filename:
                    filename = filename.split(" -> ")[1].strip()
                files.append(filename)
    return files
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/scratch/test_check_tex_compile.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add scratch/check_tex_compile.py tests/scratch/test_check_tex_compile.py
git commit -m "feat(ci): implement changed tex file detection and filtering"
```

---

### Task 2: Isolated LaTeX Compilation and Error Extraction

**Files:**
- Modify: `scratch/check_tex_compile.py`
- Modify: `tests/scratch/test_check_tex_compile.py`

**Interfaces:**
- Produces:
  - `extract_latex_errors(log_text: str) -> str`: parses LaTeX log or console output and extracts lines with `! `, error contexts, and line numbers (`l.<num>`).
  - `compile_single_tex(tex_file: Path, repo_root: Path, use_docker: bool = False, engine_cmd: Optional[List[str]] = None) -> tuple[bool, str, float]`: compiles single file into temporary dir, cleans up, and returns `(success, error_snippet, elapsed_seconds)`.

- [ ] **Step 1: Write tests for error extraction and isolated compilation**

Append to `tests/scratch/test_check_tex_compile.py`:
```python
def test_extract_latex_errors():
    sample_log = """
This is LuaHBTeX, Version 1.24.0
(./solution.tex
LaTeX2e <2025-11-01>
! Undefined control sequence.
l.42 \\invalidcommand
                     here
The control sequence at the end of the top line
of your error message was never \\def'ed.
! LaTeX Error: \\begin{align} on input line 50 ended by \\end{document}.
l.60 \\end{document}
)
Output written on solution.pdf (0 pages).
"""
    extracted = checker.extract_latex_errors(sample_log)
    assert "! Undefined control sequence." in extracted
    assert "l.42 \\invalidcommand" in extracted
    assert "! LaTeX Error: \\begin{align}" in extracted


def test_isolated_compilation_cleanness(tmp_path):
    # Verify that compiling a simple valid subfile in an isolated temp directory
    # leaves no auxiliary files in the source directory.
    dummy_file = tmp_path / "test.tex"
    dummy_file.write_text(r"\documentclass{article}\begin{document}Hello\end{document}", encoding="utf-8")
    
    # We test compilation directly using a minimal mock command if latexmk not run in unit test,
    # or verify that temp directory is cleaned up.
    with checker.temporary_outdir() as outdir:
        out_path = Path(outdir)
        (out_path / "test.aux").write_text("aux", encoding="utf-8")
        assert (out_path / "test.aux").exists()
    assert not out_path.exists()
    assert list(tmp_path.iterdir()) == [dummy_file]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/scratch/test_check_tex_compile.py -v`
Expected: FAIL with `AttributeError: module 'scratch.check_tex_compile' has no attribute 'extract_latex_errors'`

- [ ] **Step 3: Implement error extraction and isolated compilation**

Update `scratch/check_tex_compile.py`:
```python
import contextlib
import shutil
import tempfile
import time
from typing import Tuple


@contextlib.contextmanager
def temporary_outdir():
    """Create a temporary directory that is automatically removed on exit."""
    temp_dir = tempfile.mkdtemp(prefix="tex_compile_")
    try:
        yield Path(temp_dir)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def extract_latex_errors(log_text: str, max_lines: int = 25) -> str:
    """Extract relevant error lines from LaTeX log."""
    lines = log_text.splitlines()
    error_blocks = []
    capture = False
    current_block = []

    for line in lines:
        if line.startswith("!"):
            capture = True
            if current_block:
                error_blocks.append("\n".join(current_block))
                current_block = []
            current_block.append(line)
        elif capture:
            if line.strip() == "" and len(current_block) > 4:
                capture = False
                error_blocks.append("\n".join(current_block))
                current_block = []
            else:
                current_block.append(line)

    if current_block:
        error_blocks.append("\n".join(current_block))

    if not error_blocks:
        # Fallback to lines matching Error or fatal
        fallback = [l for l in lines if "Error" in l or "Fatal" in l or "l." in l]
        return "\n".join(fallback[:max_lines]) if fallback else log_text[-1000:]

    joined = "\n---\n".join(error_blocks)
    return "\n".join(joined.splitlines()[:max_lines])


def compile_single_tex(
    tex_file: Path,
    repo_root: Path,
    use_docker: bool = False,
    engine_cmd: Optional[List[str]] = None,
) -> Tuple[bool, str, float]:
    """Compile a single TeX file in an isolated temporary directory.
    
    Returns (success, error_message, elapsed_seconds).
    """
    rel_path = tex_file.resolve().relative_to(repo_root.resolve())
    file_dir = tex_file.parent
    file_name = tex_file.name

    start_time = time.time()

    with temporary_outdir() as outdir:
        if use_docker:
            # Mount repository root as /work
            container_outdir = f"/tmp/{outdir.name}"
            cmd = [
                "docker", "run", "--rm",
                "-v", f"{repo_root.resolve()}:/work",
                "-w", f"/work/{rel_path.parent}",
                "paperist/texlive-ja:latest",
                "latexmk", "-lualatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-outdir={container_outdir}",
                file_name,
            ]
        else:
            base_engine = engine_cmd or [
                "latexmk", "-lualatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
            ]
            cmd = list(base_engine) + [f"-outdir={outdir}", file_name]

        proc = subprocess.run(
            cmd,
            cwd=file_dir,
            capture_output=True,
            text=True,
        )
        elapsed = time.time() - start_time

        if proc.returncode == 0:
            return True, "", elapsed

        # On failure, look for .log file in outdir first
        log_content = ""
        log_file = outdir / f"{tex_file.stem}.log"
        if log_file.is_file():
            try:
                log_content = log_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                pass

        if not log_content:
            log_content = proc.stdout + "\n" + proc.stderr

        error_summary = extract_latex_errors(log_content)
        return False, error_summary, elapsed
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/scratch/test_check_tex_compile.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add scratch/check_tex_compile.py tests/scratch/test_check_tex_compile.py
git commit -m "feat(ci): implement isolated latexmk compilation and error extraction"
```

---

### Task 3: CLI Interface and End-to-End Execution

**Files:**
- Modify: `scratch/check_tex_compile.py`
- Modify: `tests/scratch/test_check_tex_compile.py`

**Interfaces:**
- Produces:
  - `main(argv: Optional[List[str]] = None) -> int`: Main CLI entry point supporting positional `files`, `--changed`, `--base`, `--head`, and `--docker`.
  - Return code `0` on success or when no files need compilation, `1` on any failure.

- [ ] **Step 1: Write CLI tests for argument parsing and exit codes**

Append to `tests/scratch/test_check_tex_compile.py`:
```python
import sys


def test_cli_empty_args_success(capsys):
    ret = checker.main([])
    captured = capsys.readouterr()
    assert ret == 0
    assert "No target tex files to compile." in captured.out


def test_cli_valid_file_local_compile():
    # Test compiling an existing valid solution from the repository
    valid_file = Path("src/ukyoto/zenki/1996/2/solution.tex")
    if not valid_file.exists():
        pytest.skip("Test file src/ukyoto/zenki/1996/2/solution.tex does not exist")
    ret = checker.main([str(valid_file)])
    assert ret == 0


def test_cli_broken_file_fails(tmp_path):
    broken_file = tmp_path / "src" / "dummy" / "solution.tex"
    broken_file.parent.mkdir(parents=True)
    broken_file.write_text(r"\documentclass{article}\begin{document}\undefinedcommand\end{document}", encoding="utf-8")
    ret = checker.main([str(broken_file)])
    assert ret == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/scratch/test_check_tex_compile.py -k "test_cli" -v`
Expected: FAIL with `AttributeError: module 'scratch.check_tex_compile' has no attribute 'main'`

- [ ] **Step 3: Implement main CLI function and argument handling**

Update `scratch/check_tex_compile.py`:
```python
import argparse
import sys


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify LaTeX compilation of modified solution.tex and problem.tex files."
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific .tex files to compile. If omitted, files are determined via --changed or --base/--head.",
    )
    parser.add_argument(
        "--changed",
        action="store_true",
        help="Check modified/uncommitted target .tex files in git working tree.",
    )
    parser.add_argument(
        "--base",
        type=str,
        help="Base git commit SHA for diff check.",
    )
    parser.add_argument(
        "--head",
        type=str,
        help="Head git commit SHA for diff check (default: HEAD).",
    )
    parser.add_argument(
        "--docker",
        action="store_true",
        help="Force using Docker image paperist/texlive-ja:latest for compilation.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    repo_root = Path.cwd().resolve()

    # Determine files to compile
    if args.files:
        targets = filter_target_files(args.files, repo_root=repo_root)
    elif args.changed:
        changed_raw = get_working_tree_changed_files(repo_root=repo_root)
        targets = filter_target_files(changed_raw, repo_root=repo_root)
    elif args.base:
        head = args.head or "HEAD"
        diff_raw = get_git_diff_files(base=args.base, head=head, repo_root=repo_root)
        targets = filter_target_files(diff_raw, repo_root=repo_root)
    else:
        # If no arguments provided, check working tree changes
        changed_raw = get_working_tree_changed_files(repo_root=repo_root)
        targets = filter_target_files(changed_raw, repo_root=repo_root)

    if not targets:
        print("No target tex files to compile. Skipping compilation check.")
        return 0

    # Auto-detect docker if latexmk is missing and docker is available
    use_docker = args.docker
    if not use_docker and shutil.which("latexmk") is None:
        if shutil.which("docker") is not None:
            use_docker = True
        else:
            print("ERROR: Neither 'latexmk' nor 'docker' is available on PATH.", file=sys.stderr)
            return 1

    print(f"Checking LaTeX compilation for {len(targets)} file(s) (engine={'docker' if use_docker else 'host'})...")

    failed_count = 0
    for target in targets:
        rel = target.relative_to(repo_root)
        success, error_snippet, elapsed = compile_single_tex(
            target,
            repo_root=repo_root,
            use_docker=use_docker,
        )
        if success:
            print(f"[PASS] {rel} ({elapsed:.1f}s)")
        else:
            print(f"[FAIL] {rel} ({elapsed:.1f}s)", file=sys.stderr)
            if error_snippet:
                print("--- Error Details ---", file=sys.stderr)
                print(error_snippet, file=sys.stderr)
                print("---------------------", file=sys.stderr)
            failed_count += 1

    print(f"\nSummary: {len(targets)} checked, {len(targets) - failed_count} passed, {failed_count} failed.")
    return 1 if failed_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run all unit tests to verify they pass**

Run: `pytest tests/scratch/test_check_tex_compile.py -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add scratch/check_tex_compile.py tests/scratch/test_check_tex_compile.py
git commit -m "feat(ci): complete check_tex_compile CLI with isolated build and error display"
```

---

### Task 4: Standalone GitHub Actions Workflow (`compile-tex.yml`)

**Files:**
- Create: `.github/workflows/compile-tex.yml`

**Interfaces:**
- Produces: GitHub Actions workflow running on push and PR for changes matching `'src/**/*.tex'`.

- [ ] **Step 1: Write `.github/workflows/compile-tex.yml`**

Create `.github/workflows/compile-tex.yml`:
```yaml
name: Compile LaTeX Check

on:
  pull_request:
    paths:
      - 'src/**/*.tex'
  push:
    branches:
      - main
    paths:
      - 'src/**/*.tex'

permissions:
  contents: read

jobs:
  check-compile:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Pull Docker TeX Image
        run: docker pull paperist/texlive-ja:latest

      - name: Run LaTeX Compilation Check on Changed Files
        run: |
          if [ "${{ github.event_name }}" = "pull_request" ]; then
            BASE="${{ github.event.pull_request.base.sha }}"
            HEAD="${{ github.event.pull_request.head.sha }}"
          else
            BASE="${{ github.event.before }}"
            HEAD="${{ github.sha }}"
          fi

          if ! git cat-file -e "$BASE" 2>/dev/null; then
            echo "Base commit $BASE not available; falling back to HEAD^."
            BASE=$(git rev-parse "$HEAD^" 2>/dev/null || echo "$HEAD")
          fi

          python3 scratch/check_tex_compile.py --base "$BASE" --head "$HEAD" --docker
```

- [ ] **Step 2: Validate YAML syntax of the workflow**

Run: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/compile-tex.yml'))"`
Expected: No syntax errors.

- [ ] **Step 3: End-to-end check of working tree status and git cleanliness**

Run: `python3 scratch/check_tex_compile.py --files src/ukyoto/zenki/1996/1/problem.tex src/ukyoto/zenki/1996/2/solution.tex`
Run: `git status --porcelain` to verify no auxiliary files (`.aux`, `.log`, `.pdf`) were created in `src/`.
Expected: `[PASS]` for both files, `git status` clean of compilation products.

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/compile-tex.yml
git commit -m "ci: add standalone compile-tex workflow using paperist/texlive-ja"
```
