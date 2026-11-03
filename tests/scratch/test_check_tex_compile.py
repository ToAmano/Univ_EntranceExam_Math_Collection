from pathlib import Path
import subprocess
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

    # Absolute paths (string, Path, backslash)
    assert checker.is_target_tex_file("/workspace/repo/src/ukyoto/zenki/1996/1/solution.tex") is True
    assert checker.is_target_tex_file(Path("/workspace/repo/src/ukyoto/zenki/1996/1/problem.tex")) is True
    assert checker.is_target_tex_file(r"C:\workspace\repo\src\ukyoto\zenki\1996\1\solution.tex") is True
    assert checker.is_target_tex_file("/workspace/repo/src/ukyoto/zenki/main.tex") is False
    assert checker.is_target_tex_file("/workspace/repo/other/dir/solution.tex") is False


def test_filter_existing_target_files(tmp_path):
    src_dir = tmp_path / "src" / "test_univ" / "zenki" / "1990" / "1"
    src_dir.mkdir(parents=True)
    sol = src_dir / "solution.tex"
    prob = src_dir / "problem.tex"
    other = src_dir / "notes.txt"
    sol.write_text("% sol", encoding="utf-8")
    prob.write_text("% prob", encoding="utf-8")
    other.write_text("text", encoding="utf-8")

    # Relative paths
    raw_paths = [
        str(sol.relative_to(tmp_path)),
        str(prob.relative_to(tmp_path)),
        str(other.relative_to(tmp_path)),
        "src/test_univ/zenki/1990/1/deleted.tex",
    ]
    targets = checker.filter_target_files(raw_paths, repo_root=tmp_path)
    assert targets == [sol.resolve(), prob.resolve()]

    # Absolute paths (strings and Path objects)
    abs_paths = [
        str(sol.resolve()),
        prob.resolve(),
        str(other.resolve()),
        str((tmp_path / "src/test_univ/zenki/1990/1/deleted.tex").resolve()),
    ]
    abs_targets = checker.filter_target_files(abs_paths, repo_root=tmp_path)
    assert abs_targets == [sol.resolve(), prob.resolve()]


def test_get_git_diff_and_working_tree(tmp_path):
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=tmp_path, check=True)

    src_dir = tmp_path / "src" / "test_univ" / "zenki" / "1990" / "1"
    src_dir.mkdir(parents=True)
    sol = src_dir / "solution.tex"
    sol.write_text("% sol v1", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=tmp_path, check=True)

    # Modify sol, add prob, add untracked other
    sol.write_text("% sol v2", encoding="utf-8")
    prob = src_dir / "problem.tex"
    prob.write_text("% prob", encoding="utf-8")

    changed = checker.get_working_tree_changed_files(repo_root=tmp_path)
    assert any("problem.tex" in f for f in changed)
    assert any("solution.tex" in f for f in changed)

    targets = checker.get_changed_tex_files(changed_only=True, repo_root=tmp_path)
    assert targets == sorted([sol, prob])

    # Now commit the changes
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-m", "add prob and update sol"], cwd=tmp_path, check=True)

    # Check git diff against HEAD~1
    diff_files = checker.get_git_diff_files(base="HEAD~1", head="HEAD", repo_root=tmp_path)
    assert any("problem.tex" in f for f in diff_files)
    assert any("solution.tex" in f for f in diff_files)

    diff_targets = checker.get_changed_tex_files(base="HEAD~1", head="HEAD", repo_root=tmp_path)
    assert diff_targets == sorted([sol, prob])


def test_get_working_tree_handles_quoted_filenames(monkeypatch):
    class DummyResult:
        stdout = '?? "src/foo/problem.tex"\n M "src/foo/solution.tex"\n'

    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: DummyResult())
    files = checker.get_working_tree_changed_files()
    assert files == ["src/foo/problem.tex", "src/foo/solution.tex"]
