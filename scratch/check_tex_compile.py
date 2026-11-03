#!/usr/bin/env python3
"""CI LaTeX compilation checker for modified solution.tex and problem.tex files."""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import List, Optional, Union

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
