#!/usr/bin/env python3
"""
figure（図）関連の変更のみが行われたかを検証するチェッカー。

TeX 原稿において、行われた変更が「figure 環境や旧式の図（emath zahyou, includegraphics,
図のTODOコメントなど）の修正・置き換え・追加のみ」であり、本文・数式・見出し・プリアンブル等に
一切の余計な変更が含まれていないかを機械的に判定する。

CLIおよびPython関数として使用可能:
    from scratch.check_figure_only_diff import check_figure_only_diff, is_figure_only_diff

    result = check_figure_only_diff(text_old, text_new)
    if result.is_figure_only:
        print("OK: 図のみの変更です")
    else:
        print("NG: 図以外の変更が含まれています")
        print(result.non_figure_diff)
"""

import argparse
import difflib
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass
class FigureDiffResult:
    """figure 変更検証結果"""
    is_figure_only: bool
    non_figure_diff: str
    message: str
    old_figures_count: int
    new_figures_count: int

    def __bool__(self) -> bool:
        return self.is_figure_only


# ---------------------------------------------------------------------------
# 図ブロック抽出用パターン
# ---------------------------------------------------------------------------

FIGURE_ENV_RE = re.compile(
    r'\\begin\{(figure\*?)\}(?:\[.*?\])?.*?\\end\{\1\}',
    re.DOTALL
)

TIKZ_ENV_RE = re.compile(
    r'\\begin\{tikzpicture\}(?:\[.*?\])?.*?\\end\{tikzpicture\}',
    re.DOTALL
)

ZAHYOU_ENV_RE = re.compile(
    r'\\begin\{(zahyou\*?|zahyouX\*?|zyahou\*?)\}(?:\[.*?\])?.*?\\end\{\1\}',
    re.DOTALL
)

CENTER_GRAPHIC_RE = re.compile(
    r'\\begin\{center\}\s*(?:\\includegraphics(?:\[.*?\])?\{.*?\}|\\input\{.*?\})\s*\\end\{center\}',
    re.DOTALL
)

STANDALONE_GRAPHIC_RE = re.compile(
    r'\\includegraphics(?:\[.*?\])?\{.*?\}'
)

# 図に関連する TODO コメント行（例: % TODO: 概要図, % TODO: TikZで描画 等）
FIGURE_TODO_RE = re.compile(
    r'^[ \t]*%[ \t]*TODO:[ \t]*.*?(?:図|figure|概形|グラフ|TikZ|作図).*?$',
    re.MULTILINE | re.IGNORECASE
)

# 旧式図の前後によくある垂直スペース・ページレイアウト調整
VSPACE_RE = re.compile(
    r'\\vspace\*?\{[+-]?[\d.]+\\?(?:zh|cm|mm|pt|in|em|ex)\}'
)


def extract_and_mask_figures(text: str, placeholder: str = "<<FIGURE_BLOCK>>") -> Tuple[str, List[str]]:
    """
    テキスト内の図に関連するすべてのブロックをプレースホルダーに置換し、
    置換されたブロックのリストと共に返す。
    """
    extracted_blocks: List[str] = []

    def _repl(match: re.Match) -> str:
        extracted_blocks.append(match.group(0))
        return f"\n{placeholder}\n"

    # 1. まず最も外側の figure 環境を置換
    masked = FIGURE_ENV_RE.sub(_repl, text)

    # 2. figure 外にある center + includegraphics を置換
    masked = CENTER_GRAPHIC_RE.sub(_repl, masked)

    # 3. figure 外にある zahyou 環境（emath）を置換
    masked = ZAHYOU_ENV_RE.sub(_repl, masked)

    # 4. 単独の tikzpicture（figure に入っていないもの）を置換
    masked = TIKZ_ENV_RE.sub(_repl, masked)

    # 5. 単独の includegraphics を置換
    masked = STANDALONE_GRAPHIC_RE.sub(_repl, masked)

    # 6. 図に関する TODO コメントを置換
    masked = FIGURE_TODO_RE.sub(_repl, masked)

    # 7. 図の直前・直後にありがちな vspace を除去
    masked = VSPACE_RE.sub("", masked)

    return masked, extracted_blocks


def normalize_text_for_comparison(text: str, ignore_blank_lines: bool = True) -> List[str]:
    """
    比較用の行リストに正規化する。
    行末空白を除去し、空行の連続を単一空行に正規化する。
    """
    lines = [line.rstrip() for line in text.splitlines()]
    if ignore_blank_lines:
        normalized = []
        prev_blank = True
        for line in lines:
            if not line:
                if not prev_blank:
                    normalized.append("")
                    prev_blank = True
            else:
                normalized.append(line)
                prev_blank = False
        while normalized and not normalized[-1]:
            normalized.pop()
        return normalized
    return lines


def check_figure_only_diff(
    text_old: str,
    text_new: str,
    ignore_blank_lines: bool = True,
    allow_figure_addition: bool = True,
    placeholder: str = "<<FIGURE_BLOCK>>"
) -> FigureDiffResult:
    """
    2つの TeX テキストを比較し、変更が図（figure環境等）のみかを判定する。

    Parameters:
        text_old: 変更前の TeX ソースコード
        text_new: 変更後の TeX ソースコード
        ignore_blank_lines: 図挿入前後の空行数の差異を無視するか（デフォルト: True）
        allow_figure_addition: 図の新規追加や削除（プレースホルダー自体の増減）を許容するか（デフォルト: True）

    Returns:
        FigureDiffResult: 検証結果オブジェクト
    """
    masked_old, old_figs = extract_and_mask_figures(text_old, placeholder)
    masked_new, new_figs = extract_and_mask_figures(text_new, placeholder)

    norm_old = normalize_text_for_comparison(masked_old, ignore_blank_lines=ignore_blank_lines)
    norm_new = normalize_text_for_comparison(masked_new, ignore_blank_lines=ignore_blank_lines)

    diff_lines = list(difflib.unified_diff(
        norm_old,
        norm_new,
        fromfile="before (without figures)",
        tofile="after (without figures)",
        lineterm=""
    ))

    # 差分が全くない場合
    if not diff_lines:
        return FigureDiffResult(
            is_figure_only=True,
            non_figure_diff="",
            message="OK: figure環境および図関連ブロック以外の変更はありません。",
            old_figures_count=len(old_figs),
            new_figures_count=len(new_figs),
        )

    # 差分行（---, +++, @@ 以外）を抽出
    substantive_diffs = [
        line for line in diff_lines
        if (line.startswith("+") or line.startswith("-"))
        and not line.startswith("+++")
        and not line.startswith("---")
    ]

    # 差分がプレースホルダー行（または空行）の増減のみであるか判定
    only_placeholder_changes = substantive_diffs and all(
        line[1:].strip() == placeholder or line[1:].strip() == ""
        for line in substantive_diffs
    )

    if allow_figure_addition and only_placeholder_changes:
        return FigureDiffResult(
            is_figure_only=True,
            non_figure_diff="",
            message="OK: 図ブロックの追加・削除・置換のみが行われ、本文の変更はありません。",
            old_figures_count=len(old_figs),
            new_figures_count=len(new_figs),
        )

    diff_text = "\n".join(diff_lines)
    return FigureDiffResult(
        is_figure_only=False,
        non_figure_diff=diff_text,
        message="NG: figure環境以外の本文・数式・見出し等に変更が含まれています。",
        old_figures_count=len(old_figs),
        new_figures_count=len(new_figs),
    )


def is_figure_only_diff(text_old: str, text_new: str, **kwargs) -> bool:
    """簡易判定用ブール関数"""
    return check_figure_only_diff(text_old, text_new, **kwargs).is_figure_only


def get_git_file_content(file_path: Path, git_ref: str = "HEAD") -> Optional[str]:
    """Git の指定 ref からファイル内容を取得する"""
    try:
        # 相対パスを取得
        try:
            rel_path = file_path.resolve().relative_to(Path.cwd())
        except ValueError:
            rel_path = file_path
        cmd = ["git", "show", f"{git_ref}:{rel_path}"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return res.stdout
    except subprocess.CalledProcessError:
        return None


def check_git_file(file_path: Path, base_ref: str = "HEAD", target_ref: Optional[str] = None) -> FigureDiffResult:
    """
    Git 上の特定ファイルについて、base_ref と target_ref（未指定ならワーキングツリー）を比較する。
    """
    text_old = get_git_file_content(file_path, base_ref)
    if text_old is None:
        return FigureDiffResult(
            is_figure_only=False,
            non_figure_diff="",
            message=f"Git 上で {base_ref}:{file_path} を取得できませんでした（新規ファイル等）。",
            old_figures_count=0,
            new_figures_count=0,
        )

    if target_ref:
        text_new = get_git_file_content(file_path, target_ref)
        if text_new is None:
            return FigureDiffResult(
                is_figure_only=False,
                non_figure_diff="",
                message=f"Git 上で {target_ref}:{file_path} を取得できませんでした（削除ファイル等）。",
                old_figures_count=0,
                new_figures_count=0,
            )
    else:
        if not file_path.exists():
            return FigureDiffResult(
                is_figure_only=False,
                non_figure_diff="",
                message=f"ローカルファイル {file_path} が存在しません。",
                old_figures_count=0,
                new_figures_count=0,
            )
        text_new = file_path.read_text(encoding="utf-8")

    return check_figure_only_diff(text_old, text_new)


def check_commit(commit_ref: str) -> Dict[Path, FigureDiffResult]:
    """
    指定したコミットとその親コミット（commit_ref~1）を比較し、
    変更された全 .tex ファイルについて figure のみの変更かを検証する。
    """
    cmd = ["git", "diff", "--name-only", f"{commit_ref}~1", commit_ref]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    results = {}
    for line in res.stdout.splitlines():
        line = line.strip()
        if line.endswith(".tex"):
            p = Path(line)
            results[p] = check_git_file(p, base_ref=f"{commit_ref}~1", target_ref=commit_ref)
    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="figure環境以外の変更がないかを機械的に検証するチェッカー"
    )
    parser.add_argument("files", nargs="*", help="検証対象の TeX ファイル（または比較する2ファイル）")
    parser.add_argument("--ref", default="HEAD", help="git 比較基準のリファレンス（デフォルト: HEAD）")
    parser.add_argument("--staged", action="store_true", help="ステージされた変更（git diff --cached）をチェック")
    parser.add_argument("--commit", help="指定したコミットの変更内容をチェック（例: HEAD, a1b2c3d）")
    parser.add_argument("--compare-two", action="store_true", help="渡された2ファイルを old / new として直接比較")

    args = parser.parse_args()

    # 1. 2ファイル直接比較モード
    if args.compare_two:
        if len(args.files) != 2:
            print("エラー: --compare-two には 2 つのファイルパスを指定してください。", file=sys.stderr)
            sys.exit(2)
        p1, p2 = Path(args.files[0]), Path(args.files[1])
        result = check_figure_only_diff(p1.read_text(encoding="utf-8"), p2.read_text(encoding="utf-8"))
        print(f"[{'PASS' if result.is_figure_only else 'FAIL'}] {p1.name} vs {p2.name}")
        print(f"  {result.message}")
        if not result.is_figure_only:
            print("\n--- 図以外の差分 ---")
            print(result.non_figure_diff)
            sys.exit(1)
        sys.exit(0)

    # 2. コミット検証モード
    if args.commit:
        results = check_commit(args.commit)
        if not results:
            print(f"コミット {args.commit} に変更された .tex ファイルはありませんでした。")
            sys.exit(0)
        any_failure = False
        print(f"=== コミット {args.commit} の figure 変更検証 ===")
        for path, res in results.items():
            label = "PASS" if res.is_figure_only else "FAIL"
            print(f"[{label}] {path} (旧図: {res.old_figures_count}個, 新図: {res.new_figures_count}個)")
            if not res.is_figure_only:
                any_failure = True
                print(f"  理由: {res.message}")
                print("  --- 図以外の差分（抜粋） ---")
                for dl in res.non_figure_diff.splitlines()[:20]:
                    print(f"    {dl}")
                print()
        if any_failure:
            sys.exit(1)
        print("\n全ファイル検証成功: すべて figure/図ブロック のみの変更です。")
        sys.exit(0)

    # 3. 通常モード（ワーキングツリー または ステージング）
    target_files: List[Path] = []
    if args.files:
        target_files = [Path(f) for f in args.files]
    else:
        diff_cmd = ["git", "diff", "--name-only"]
        if args.staged:
            diff_cmd.append("--cached")
        else:
            diff_cmd.append(args.ref)
        res = subprocess.run(diff_cmd, stdout=subprocess.PIPE, text=True)
        for line in res.stdout.splitlines():
            line = line.strip()
            if line.endswith(".tex"):
                target_files.append(Path(line))

    if not target_files:
        print("検証対象の TeX ファイルが見つかりませんでした。")
        sys.exit(0)

    any_failure = False
    for f in target_files:
        if not f.exists():
            continue
        base = "HEAD" if not args.staged else "HEAD"
        res = check_git_file(f, base_ref=base)
        status_label = "PASS" if res.is_figure_only else "FAIL"
        print(f"[{status_label}] {f} (旧図: {res.old_figures_count}個, 新図: {res.new_figures_count}個)")
        if not res.is_figure_only:
            any_failure = True
            print(f"  理由: {res.message}")
            print("  --- 図以外の差分（抜粋） ---")
            diff_lines = res.non_figure_diff.splitlines()
            for dl in diff_lines[:25]:
                print(f"    {dl}")
            if len(diff_lines) > 25:
                print(f"    ... 残り {len(diff_lines) - 25} 行省略 ...")
            print()

    if any_failure:
        sys.exit(1)
    else:
        print("\n全ファイル検証成功: すべて figure/図ブロック のみの変更です。")
        sys.exit(0)


if __name__ == "__main__":
    main()
