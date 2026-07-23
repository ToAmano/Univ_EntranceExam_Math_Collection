import subprocess
import json

def create_issue(title, body):
    cmd = ["gh", "issue", "create", "--title", title, "--body", body]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Created Issue: {res.stdout.strip()}")
    else:
        print(f"Failed to create Issue: {res.stderr.strip()}")

# Issue 1: enumerate handling
title_1 = "[Web表示] enumerate環境のMarkdownリスト自動変換・MathJax最適化"
body_1 = """## 概要
`problem.tex` 原稿では LaTeX 標準の `\\begin{enumerate} \\item ... \\end{enumerate}` を維持しつつ、Astro Web 用の Markdown (`*-problem.md`) への変換時に HTML/Markdown の番号付きリスト (`1.  ...`) へスマート変換し、リスト内の数式のみを MathJax でレンダリングさせるパイプラインを調整・最適化する。

## 背景・目的
* MathJax は数式モードブロック内を中心に処理するため、文章構造としての生 `\\begin{enumerate}` は HTML 表示時に直接レンダリングされない。
* Web 上でのレスポンシブデザイン・アクセシビリティ・レイアウト崩れ防止のため、リスト構造は HTML/Markdown (`<ol><li>`) に委ね、内部の `$math$` のみを MathJax に委ねるのがベストプラクティス。

## タスク内容
- [ ] `tex_to_md.py` のリスト変換処理の精緻化
- [ ] `\\item` 直後のスペース補正および `\\begin{enumerate}` のスマートパース動作確認
- [ ] Astro Web ページ上での表示確認
"""

# Issue 2: Figures handling
title_2 = "[画像・図表] ダウンロード済み手書き図画像の配備とTikZ/SVGベクター化パイプライン構築"
body_2 = """## 概要
`server-test.net` 等からダウンロード済みの問題用添付画像（`fig_*.jpg`）を問題フォルダへ自動転送・配備し、Web サイトで表示可能にする。また、重要問題については段階的に TikZ / SVG ベクター画像への書き換えを進める。

## 背景・目的
* 一部の問題には手書きの図形・グラフ・イラスト画像（例: `fig_2000_1.jpg`, `fig_2009_6.jpg`）が含まれている。
* まずは元画像を表示可能にしつつ、将来的には解像度に依存しないベクター画像（TikZ/SVG）へアップグレードする。

## タスク内容
- [ ] アーカイブ内の `fig_*.jpg` を対応する `src/[univ]/[cat]/[year]/[q]/` へ自動配置するスクリプトの作成
- [ ] `problem.tex` の `\\includegraphics` パスおよび Markdown コンバータの画像転送処理の動作確認
- [ ] 主要な図形問題についての段階的な TikZ/SVG コード化
"""

if __name__ == '__main__':
    create_issue(title_1, body_1)
    create_issue(title_2, body_2)
