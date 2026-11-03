#!/usr/bin/env python3
"""CI LaTeX compilation checker for modified solution.tex and problem.tex files."""

from __future__ import annotations

import argparse
import contextlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import List, Optional, Tuple, Union

TARGET_PATTERN = re.compile(r"(?:^|/)src/.+/(solution|problem)\.tex$")


def is_target_tex_file(path: Union[str, Path]) -> bool:
    """Return True if path matches src/**/solution.tex or src/**/problem.tex."""
    normalized = str(path).replace("\\", "/")
    return bool(TARGET_PATTERN.search(normalized))


def filter_target_files(file_paths: List[Union[str, Path]], repo_root: Optional[Path] = None) -> List[Path]:
    """Filter list of paths to existing target TeX files."""
    root = (repo_root or Path.cwd()).resolve()
    valid_targets: List[Path] = []
    for p in file_paths:
        p_obj = Path(p)
        full_path = p_obj.resolve() if p_obj.is_absolute() else (root / p).resolve()
        if is_target_tex_file(full_path):
            if full_path.is_file():
                valid_targets.append(full_path)
    return list(dict.fromkeys(valid_targets))


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
                filename = filename.strip('"')
                files.append(filename)
    return files


def get_changed_tex_files(
    base: Optional[str] = None,
    head: Optional[str] = None,
    changed_only: bool = False,
    repo_root: Optional[Path] = None,
) -> List[Path]:
    """Retrieve existing target TeX files changed in git diff or working tree."""
    if changed_only or (not base and not head):
        raw = get_working_tree_changed_files(repo_root=repo_root)
    else:
        raw = get_git_diff_files(base=base, head=head or "HEAD", repo_root=repo_root)
    return sorted(filter_target_files(raw, repo_root=repo_root))


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
    try:
        rel_path = tex_file.resolve().relative_to(repo_root.resolve())
    except ValueError:
        rel_path = tex_file.resolve()
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
                "-w", f"/work/{rel_path.parent.as_posix()}",
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
        try:
            rel = target.relative_to(repo_root)
        except ValueError:
            rel = target
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


