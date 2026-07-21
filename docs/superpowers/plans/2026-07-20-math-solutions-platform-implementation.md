# 数学過去問解答プラットフォーム 実装計画書 (複数年度拡張・一括マスターPDF対応版)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 複数箇所に散らばっている数学過去問解答（TeXと手書きPDF）を「大問フォルダ一体型」に移行・統合し、AstroでのWeb公開（GitHub Pages）とLuaLaTeXでのPDFビルド・CI/CDを構築する。複数年度のサンプルデータ（1990, 1992, 1993, 1994, 1995）を拡充し、区分直下の一括マスターTeX (`src/sample_todai/zenki/main.tex`) により、全年度・全大問が整然と年度順・大問順に並んだ高品質な一括解答集PDFをビルド・検証する。

**Architecture:** LaTeXソース（`src/`）をマスターとし、Astro (web/) へPandocで自動Markdown変換してKaTeXで静的描画。TikZブロックは一時的にLuaLaTeXでコンパイルし `pdftocairo` でSVG化して埋め込み。一括PDFは `src/[大学]/[区分]/main.tex` をマスターとして `latexmk -lualatex` でビルド。

**Tech Stack:** Python 3, Astro (v4.x), KaTeX (rehype-katex), Pandoc, LuaLaTeX / latexmk, poppler-utils (pdftocairo), GitHub Actions

## Global Constraints
* すべてのLaTeXソースは `src/` 以下に配置し、「大問フォルダ一体型」（例: `src/todai/zenki/1990/1/problem.tex`）とする。
* 既存のTeXファイル（`titech_kouki` 内のソースなど）を操作する際は、**絶対にコピーのみを行い、元ファイルを書き換え・移動しない**こと。
* Webプロジェクトは `web/` ディレクトリ内にAstroで作成する。
* 一括PDF用のマスター `main.tex` は各区分直下（例: `src/sample_todai/zenki/main.tex`）に置き、年度順・大問順にインポートする。

---

### Task 1: 検証用データの拡張 (複数年度のTeXをコピー配置)

**Files:**
* Create: `src/sample_todai/zenki/1992/1/problem.tex`, `solution.tex`
* Create: `src/sample_todai/zenki/1992/2/problem.tex`, `solution.tex`
* Create: `src/sample_todai/zenki/1993/2/problem.tex`, `solution.tex`
* Create: `src/sample_todai/zenki/1993/3/problem.tex`, `solution.tex`
* Create: `src/sample_todai/zenki/1994/2/problem.tex`, `solution.tex`
* Retain: `1990/1/`, `1995/2/` (既存コピー)

**Interfaces:**
* Consumes: `/Users/amano/works/research/titech_kouki/UtokyoKouki/manuscript/docs/` 内の各該当 TeX ソース
* Produces: 複数年度・大問がそろった検証用TeXディレクトリ構造 `src/sample_todai/zenki/`

- [ ] **Step 1: 1992, 1993, 1994年の各問題・解答TeXを `src/sample_todai/zenki/` 以下にコピーする**

(※元ファイルはいじらず、コピーして `solution.tex` という単数形名で配置)

- [ ] **Step 2: コピー結果を確認しコミットする**

Run: `git status`
Expected: コピー先のみが新規作成され、`titech_kouki` 側には変更がないこと。

```bash
git add src/sample_todai/
git commit -m "feat: expand sample dataset with 1992, 1993, 1994 exam TeX files"
```

---

### Task 2: Astroプロジェクトのセットアップと数式表示の導入

(実装済み)

---

### Task 3: LaTeX ➔ Markdown 変換ツールの実行 (全データ一括Web変換)

**Files:**
* Executed script: `scratch/tex_to_md.py`

- [ ] **Step 1: 拡張された全サンプルデータを一括変換する**

Run: `python3 scratch/tex_to_md.py`
Expected: `web/src/content/solutions/` にすべての問題・解答のMarkdownが生成され、TikZ画像が `web/public/images/tikz/` に出力される。

- [ ] **Step 2: Astroビルドを検証する**

Run: `cd web && npm run build`
Expected: エラーなく全ページがビルドされる。

- [ ] **Step 3: コミット**

```bash
git add web/src/content/solutions/ web/public/images/tikz/
git commit -m "feat: generate converted markdown and tikz svgs for expanded dataset"
```

---

### Task 4: GitHub Actionsパイプラインの確認

(実装済み)

---

### Task 5: README.mdの更新

(実装済み)

---

### Task 6: 統合マスター `main.tex` の構築とPDF一括ビルド・改ページ検証

**Files:**
* Delete: `src/sample_todai/zenki/1995/main.tex` (混在していた旧テストファイル)
* Create: `src/sample_todai/zenki/main.tex` (区分の統合マスターTeX)

**Interfaces:**
* Consumes: `src/sample_todai/zenki/` 配下の全年度・全大問
* Produces: 全問題が年度順・大問順に並んだ一括解答集PDF `src/sample_todai/zenki/main.pdf`

- [ ] **Step 1: 旧1995年フォルダ内の不要なテスト用 `main.tex` や `main.pdf` を削除する**

- [ ] **Step 2: 統合マスター `src/sample_todai/zenki/main.tex` を作成する**

```latex
\documentclass[a4paper,11pt]{ltjsarticle}
\usepackage{amsmath,amssymb}
\usepackage{bm}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{angles,quotes,intersections,patterns,fillbetween}
\usepackage{docmute}
\usepackage{hyperref}

\title{東京大学 前期 理系数学 過去問解答集 (サンプル)}
\author{Math-Solutions}
\date{\today}

\begin{document}
\maketitle
\clearpage

% --- 1990年 ---
\part*{1990年}
\section*{第1問}
\input{1990/1/problem.tex}
\subsection*{解答}
\input{1990/1/solution.tex}
\clearpage

% --- 1992年 ---
\part*{1992年}
\section*{第1問}
\input{1992/1/problem.tex}
\subsection*{解答}
\input{1992/1/solution.tex}
\clearpage

\section*{第2問}
\input{1992/2/problem.tex}
\subsection*{解答}
\input{1992/2/solution.tex}
\clearpage

% --- 1993年 ---
\part*{1993年}
\section*{第2問}
\input{1993/2/problem.tex}
\subsection*{解答}
\input{1993/2/solution.tex}
\clearpage

\section*{第3問}
\input{1993/3/problem.tex}
\subsection*{解答}
\input{1993/3/solution.tex}
\clearpage

% --- 1994年 ---
\part*{1994年}
\section*{第2問}
\input{1994/2/problem.tex}
\subsection*{解答}
\input{1994/2/solution.tex}
\clearpage

% --- 1995年 ---
\part*{1995年}
\section*{第2問}
\input{1995/2/problem.tex}
\subsection*{解答}
\input{1995/2/solution.tex}
\clearpage

\end{document}
```

- [ ] **Step 3: LuaLaTeXで一括コンパイルを実行する**

Run: `cd src/sample_todai/zenki && latexmk -lualatex main.tex`
Expected: エラーなく `main.pdf` が生成される。

- [ ] **Step 4: コミット**

```bash
git add src/sample_todai/zenki/main.tex
git commit -m "feat: construct unified category-root master main.tex for multi-year PDF generation"
```

---
