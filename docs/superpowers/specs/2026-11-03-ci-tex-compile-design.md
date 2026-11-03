# CI LaTeX Compilation Check Design Spec

- **Author**: Antigravity
- **Date**: 2026-11-03
- **Status**: Approved by User

## 1. Overview & Objective

To prevent syntax errors, missing package dependencies, or broken macros from being committed, we introduce an independent, automated CI check that verifies whether LaTeX files compile cleanly into PDF without error.

To avoid the performance degradation of local commits (where running `latexmk` during `pre-commit` could add 10-30+ seconds to every commit), this verification runs:
1. In a standalone GitHub Actions workflow on `push` and `pull_request`.
2. On-demand locally via a Python CLI script when desired.
3. Strictly scoped to files modified or added in the commit/push (specifically `src/**/solution.tex` and `src/**/problem.tex`).

---

## 2. GitHub Actions Workflow: `.github/workflows/compile-tex.yml`

### 2.1 Trigger Events
- `push`: On `branches: [main]` when `paths` matches `'src/**/*.tex'`.
- `pull_request`: On any PR when `paths` matches `'src/**/*.tex'`.

### 2.2 Runner & TeX Environment
- **Runner**: `ubuntu-latest`.
- **TeX Engine**: `paperist/texlive-ja:latest` Docker image.
  - Using pre-built Docker avoids apt installation latency (~2-4 minutes every build).
  - GitHub Actions `ubuntu-latest` provides Docker out of the box.

### 2.3 Changed File Detection
- Follows the tested pattern from `.github/workflows/lint-tex.yml`:
  - On PR: compare `${{ github.event.pull_request.base.sha }}` against `${{ github.event.pull_request.head.sha }}`.
  - On Push: compare `${{ github.event.before }}` against `${{ github.sha }}`. If `${{ github.event.before }}` is missing or zero SHA (initial branch push), fallback to `HEAD^`.
- Targets:
  ```bash
  git diff --diff-filter=ACMR --name-only "$BASE" "$HEAD" | grep -E '(^|/)(solution|problem)\.tex$'
  ```
- If 0 matching files are modified, exit with success immediately.

---

## 3. Python Verification Script: `scratch/check_tex_compile.py`

### 3.1 CLI Arguments
- `files` (positional, optional): Explicit list of `.tex` files to compile.
- `--changed`: Check modified/uncommitted `.tex` files in working tree (`git status` / `git diff HEAD`).
- `--base <commit> --head <commit>`: Check `.tex` files modified between two commits (for CI).
- `--docker`: Force compilation using Docker (`paperist/texlive-ja:latest`).
- `--engine`: TeX engine command (default: `latexmk -lualatex -interaction=nonstopmode -halt-on-error`).

### 3.2 Execution Modes & Backend Detection
- **Host Native Mode**: If `latexmk` is present on `PATH` (e.g., local macOS development environment), execute directly via Python `subprocess.run`.
- **Docker Mode**: If `--docker` is specified, or if `latexmk` is missing on host while `docker` is available, wrap the compilation command in:
  ```bash
  docker run --rm -v "<REPO_ROOT>:/work" -w /work paperist/texlive-ja:latest latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir="<TEMP_DIR>" "<REL_TEX_PATH>"
  ```

### 3.3 Isolation & Cleanliness
- Compilation of subfiles requires running from the directory containing the file (or using `-cd`) so that `\documentclass[../../main.tex]{subfiles}` resolves relative paths correctly.
- All output and temporary auxiliary files (`.aux`, `.log`, `.pdf`, `.fls`, `.synctex.gz`) MUST be directed to a temporary directory (`tempfile.TemporaryDirectory()`).
- The repository source tree must remain 100% untouched. No untracked `.aux` or `.pdf` files left behind.

### 3.4 Error Reporting & Logging
- **Success**: Output clean confirmation line:
  `[PASS] src/ukyoto/zenki/1996/2/solution.tex (3.2s)`
- **Failure**:
  1. Output `[FAIL] <path>`.
  2. Parse the generated `.log` file or stdout/stderr to locate the fatal error (lines matching `! LaTeX Error:`, `! Undefined control sequence.`, `l.<line>`, etc.).
  3. Print the error snippet (5-15 lines) with clear highlighting.
  4. Ensure exit code is `1` to fail CI.
- **Summary**:
  Print a final summary line:
  `Checked 4 files: 4 passed, 0 failed.` (or `3 passed, 1 failed.`)

---

## 4. Verification & Testing Strategy

1. **Local Test with Passed File**:
   - Run `python3 scratch/check_tex_compile.py src/ukyoto/zenki/1996/2/solution.tex`.
   - Verify it outputs `[PASS]` and leaves no new files in `git status`.
2. **Local Test with problem.tex**:
   - Run `python3 scratch/check_tex_compile.py src/ukyoto/zenki/1996/1/problem.tex`.
   - Verify it outputs `[PASS]`.
3. **Local Test with Broken File**:
   - Run against a test file with intentional syntax error.
   - Verify it fails with exit code 1 and extracts the error line clearly.
4. **Git Diff Flag Test**:
   - Run `python3 scratch/check_tex_compile.py --changed` or `--base HEAD~1 --head HEAD`.
   - Verify file discovery logic works as expected.
5. **Workflow Syntax & Lint**:
   - Check YAML syntax of `.github/workflows/compile-tex.yml`.
