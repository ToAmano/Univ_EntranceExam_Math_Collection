from pathlib import Path
import subprocess
import sys
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


def test_extract_latex_errors_fallback():
    # Fallback to lines with Error or Fatal
    log_without_bang = """
This is LuaHBTeX
Some line
Fatal error occurred, no output PDF file produced!
Transcript written on solution.log.
"""
    extracted = checker.extract_latex_errors(log_without_bang)
    assert "Fatal error occurred" in extracted

    # Fallback when no keywords exist
    plain_log = "Just regular log output line 1\nJust regular log output line 2"
    extracted_plain = checker.extract_latex_errors(plain_log)
    assert "Just regular log output line 2" in extracted_plain


def test_isolated_compilation_cleanness(tmp_path):
    # Verify that compiling a simple valid subfile in an isolated temp directory
    # leaves no auxiliary files in the source directory.
    dummy_file = tmp_path / "test.tex"
    dummy_file.write_text(r"\documentclass{article}\begin{document}Hello\end{document}", encoding="utf-8")

    # Verify that temp directory is cleaned up.
    with checker.temporary_outdir() as outdir:
        out_path = Path(outdir)
        (out_path / "test.aux").write_text("aux", encoding="utf-8")
        assert (out_path / "test.aux").exists()
    assert not out_path.exists()
    assert list(tmp_path.iterdir()) == [dummy_file]


def test_compile_single_tex_success(tmp_path):
    repo_root = tmp_path
    tex_dir = repo_root / "src" / "test_univ" / "zenki" / "1990" / "1"
    tex_dir.mkdir(parents=True)
    tex_file = tex_dir / "solution.tex"
    tex_file.write_text("% valid tex", encoding="utf-8")

    # Mock engine that succeeds
    mock_engine = [sys.executable, "-c", "import sys; sys.exit(0)"]
    success, err, elapsed = checker.compile_single_tex(
        tex_file=tex_file,
        repo_root=repo_root,
        engine_cmd=mock_engine,
    )
    assert success is True
    assert err == ""
    assert elapsed >= 0


def test_compile_single_tex_failure_with_log(tmp_path):
    repo_root = tmp_path
    tex_dir = repo_root / "src" / "test_univ" / "zenki" / "1990" / "1"
    tex_dir.mkdir(parents=True)
    tex_file = tex_dir / "solution.tex"
    tex_file.write_text("% broken tex", encoding="utf-8")

    # Mock engine that writes a .log file into the -outdir argument and fails
    mock_script = (
        "import sys, pathlib\n"
        "for arg in sys.argv[1:]:\n"
        "    if arg.startswith('-outdir='):\n"
        "        out = pathlib.Path(arg.split('=', 1)[1])\n"
        "        (out / 'solution.log').write_text('! LaTeX Error: syntax error\\nl.10 \\\\bad\\n')\n"
        "sys.exit(1)\n"
    )
    mock_engine = [sys.executable, "-c", mock_script]
    success, err, elapsed = checker.compile_single_tex(
        tex_file=tex_file,
        repo_root=repo_root,
        engine_cmd=mock_engine,
    )
    assert success is False
    assert "! LaTeX Error: syntax error" in err
    assert "l.10 \\bad" in err
    assert elapsed >= 0


def test_compile_single_tex_failure_stdout_fallback(tmp_path):
    repo_root = tmp_path
    tex_dir = repo_root / "src" / "test_univ" / "zenki" / "1990" / "1"
    tex_dir.mkdir(parents=True)
    tex_file = tex_dir / "solution.tex"
    tex_file.write_text("% broken tex", encoding="utf-8")

    # Mock engine that outputs error to stderr/stdout but no .log file
    mock_script = "import sys; print('! Fatal error from stdout'); sys.exit(1)"
    mock_engine = [sys.executable, "-c", mock_script]
    success, err, elapsed = checker.compile_single_tex(
        tex_file=tex_file,
        repo_root=repo_root,
        engine_cmd=mock_engine,
    )
    assert success is False
    assert "! Fatal error from stdout" in err


def test_compile_single_tex_docker_cmd(tmp_path, monkeypatch):
    repo_root = tmp_path
    tex_dir = repo_root / "src" / "test_univ" / "zenki" / "1990" / "1"
    tex_dir.mkdir(parents=True)
    tex_file = tex_dir / "solution.tex"
    tex_file.write_text("% tex", encoding="utf-8")

    executed_cmd = []

    def mock_run(cmd, *args, **kwargs):
        nonlocal executed_cmd
        executed_cmd = cmd
        class Result:
            returncode = 0
            stdout = ""
            stderr = ""
        return Result()

    monkeypatch.setattr(subprocess, "run", mock_run)

    success, err, elapsed = checker.compile_single_tex(
        tex_file=tex_file,
        repo_root=repo_root,
        use_docker=True,
    )
    assert success is True
    assert executed_cmd[0] == "docker"
    assert executed_cmd[1] == "run"
    assert f"{repo_root.resolve()}:/work" in executed_cmd[ executed_cmd.index("-v") + 1 ]
    assert executed_cmd[ executed_cmd.index("-w") + 1 ] == "/work/src/test_univ/zenki/1990/1"
    assert "paperist/texlive-ja:latest" in executed_cmd


def test_cli_empty_args_success(capsys, monkeypatch):
    monkeypatch.setattr(checker, "get_working_tree_changed_files", lambda repo_root=None: [])
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


def test_cli_parse_args():
    args = checker.parse_args(["--changed", "--docker"])
    assert args.changed is True
    assert args.docker is True
    assert args.files == []

    args2 = checker.parse_args(["--base", "main", "--head", "feature", "file1.tex"])
    assert args2.base == "main"
    assert args2.head == "feature"
    assert args2.files == ["file1.tex"]


def test_cli_missing_tools(monkeypatch, tmp_path, capsys):
    target = tmp_path / "src" / "dummy" / "solution.tex"
    target.parent.mkdir(parents=True)
    target.write_text("% valid", encoding="utf-8")

    monkeypatch.setattr(checker.shutil, "which", lambda cmd: None)
    ret = checker.main([str(target)])
    captured = capsys.readouterr()
    assert ret == 1
    assert "Neither 'latexmk' nor 'docker' is available on PATH" in captured.err


def test_cli_changed_flag(monkeypatch, tmp_path, capsys):
    target = tmp_path / "src" / "univ" / "1990" / "1" / "solution.tex"
    target.parent.mkdir(parents=True)
    target.write_text("% valid", encoding="utf-8")

    monkeypatch.setattr(checker, "get_working_tree_changed_files", lambda repo_root=None: [str(target)])
    monkeypatch.setattr(checker, "compile_single_tex", lambda t, repo_root, use_docker=False: (True, "", 0.42))

    ret = checker.main(["--changed"])
    captured = capsys.readouterr()
    assert ret == 0
    assert "[PASS]" in captured.out
    assert "Summary: 1 checked, 1 passed, 0 failed." in captured.out


def test_cli_base_head_flag(monkeypatch, tmp_path, capsys):
    target = tmp_path / "src" / "univ" / "1990" / "1" / "problem.tex"
    target.parent.mkdir(parents=True)
    target.write_text("% valid", encoding="utf-8")

    called_diff = {}
    def mock_get_git_diff_files(base=None, head=None, repo_root=None):
        called_diff["base"] = base
        called_diff["head"] = head
        return [str(target)]

    monkeypatch.setattr(checker, "get_git_diff_files", mock_get_git_diff_files)
    monkeypatch.setattr(checker, "compile_single_tex", lambda t, repo_root, use_docker=False: (True, "", 0.5))

    ret = checker.main(["--base", "origin/main", "--head", "my-branch"])
    captured = capsys.readouterr()
    assert ret == 0
    assert called_diff["base"] == "origin/main"
    assert called_diff["head"] == "my-branch"
    assert "[PASS]" in captured.out


def test_cli_docker_autodetect(monkeypatch, tmp_path, capsys):
    target = tmp_path / "src" / "univ" / "1990" / "1" / "solution.tex"
    target.parent.mkdir(parents=True)
    target.write_text("% valid", encoding="utf-8")

    # latexmk missing, docker present
    def mock_which(cmd):
        if cmd == "docker":
            return "/usr/local/bin/docker"
        return None

    passed_use_docker = {}
    def mock_compile(t, repo_root, use_docker=False):
        passed_use_docker["val"] = use_docker
        return (True, "", 1.0)

    monkeypatch.setattr(checker.shutil, "which", mock_which)
    monkeypatch.setattr(checker, "compile_single_tex", mock_compile)

    ret = checker.main([str(target)])
    captured = capsys.readouterr()
    assert ret == 0
    assert passed_use_docker["val"] is True
    assert "engine=docker" in captured.out


def test_cli_failure_output_and_exit_code(monkeypatch, tmp_path, capsys):
    target = tmp_path / "src" / "univ" / "1990" / "1" / "solution.tex"
    target.parent.mkdir(parents=True)
    target.write_text("% broken", encoding="utf-8")

    def mock_compile(t, repo_root, use_docker=False):
        return (False, "! LaTeX Error: Bad syntax\nl.12 \\foo", 0.8)

    monkeypatch.setattr(checker, "compile_single_tex", mock_compile)

    ret = checker.main([str(target)])
    captured = capsys.readouterr()
    assert ret == 1
    assert "[FAIL]" in captured.err
    assert "--- Error Details ---" in captured.err
    assert "! LaTeX Error: Bad syntax" in captured.err
    assert "Summary: 1 checked, 0 passed, 1 failed." in captured.out



