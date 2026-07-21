# 数学過去問解答プラットフォーム 実装計画書 (マルチ大学対応検証版)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 複数箇所に散らばっている数学過去問解答（TeXと手書きPDF）を「大問フォルダ一体型」に移行・統合し、AstroでのWeb公開（GitHub Pages）とLuaLaTeXでのPDFビルド・CI/CDを構築する。東大 (`sample_todai`) に加え、東工大 (`sample_titech`) のサンプルデータを追加し、複数大学が存在する場合でもWeb変換・画像階層出力・PDFマスター一括ビルドの全パイプラインが正常に動作することを検証する。

**Architecture:** LaTeXソース（`src/`）をマスターとし、Astro (web/) へPandocで自動Markdown変換してKaTeXで静的描画。TikZブロックは `render_tikz_to_svg` で大学別の階層化SVG画像に切り出し・コンパイル。一括PDFは `src/[大学]/[区分]/main.tex` をマスターとして `latexmk -lualatex` でビルド。

**Tech Stack:** Python 3, Astro (v4.x), KaTeX (rehype-katex), Pandoc, LuaLaTeX / latexmk, poppler-utils (pdftocairo), GitHub Actions

## Global Constraints
* すべてのLaTeXソースは `src/` 以下に配置し、「大問フォルダ一体型」（例: `src/sample_titech/kouki/1990/1/problem.tex`）とする。
* 既存のTeXファイル（`titech_kouki` 内のソースなど）を操作する際は、**絶対にコピーのみを行い、元ファイルを書き換え・移動しない**こと。
* Webプロジェクトは `web/` ディレクトリ内にAstroで作成する。
* TikZ画像は `web/public/images/tikz/[uni]/[category]/[year]/[q_num]/fig_[N].svg` の階層構造で保存する。

---

### Task 1: 検証用データのマルチ大学拡張 (東工大サンプルのコピー配置)

**Files:**
* Create: `src/sample_titech/kouki/1990/1/problem.tex`, `solution.tex`
* Create: `src/sample_titech/kouki/1995/1/problem.tex`, `solution.tex`
* Create: `src/sample_titech/kouki/2000/1/problem.tex`, `solution.tex`
* Retain: `src/sample_todai/zenki/` (既存東大サンプル)

**Interfaces:**
* Consumes: `/Users/amano/works/research/titech_kouki/TitechKouki/manuscript/docs/` 内の各該当 TeX ソース
* Produces: 東工大サンプルTeXディレクトリ構造 `src/sample_titech/kouki/`

- [ ] **Step 1: 東工大1990, 1995, 2000年の各問題・解答TeXを `src/sample_titech/kouki/` 以下にコピーする**

(※元ファイルはいじらず、コピーして `solution.tex` という単数形名で配置)

- [ ] **Step 2: コピー結果を確認しコミットする**

Run: `git status`
Expected: `src/sample_titech/` が新規作成され、`titech_kouki` 側には変更がないこと。

```bash
git add src/sample_titech/
git commit -m "feat: add Titech (sample_titech) exam files for multi-university validation"
```

---

### Task 2: Astroプロジェクトのセットアップと数式表示の導入

(実装済み)

---

### Task 3: LaTeX ➔ Markdown 変換ツールの実行 (マルチ大学一括Web変換)

**Files:**
* Executed script: `scratch/tex_to_md.py`

- [ ] **Step 1: マルチ大学サンプルデータを一括変換する**

Run: `python3 scratch/tex_to_md.py`
Expected: `web/src/content/solutions/sample_titech-kouki-...md` が追加生成され、TikZ画像が `web/public/images/tikz/sample_titech/kouki/...` に出力される。

- [ ] **Step 2: Astroビルドを検証する**

Run: `cd web && npm run build`
Expected: エラー0で全大学のページがビルドされる。

- [ ] **Step 3: コミット**

```bash
git add web/src/content/solutions/ web/public/images/tikz/
git commit -m "feat: generate converted markdown and tikz svgs for multi-university dataset"
```

---

### Task 4: GitHub Actionsパイプラインの確認

(実装済み)

---

### Task 5: README.mdの更新

(実装済み)

---

### Task 6: 東工大統合マスター `main.tex` の構築とマルチ大学PDF一括ビルド検証

**Files:**
* Create: `src/sample_titech/kouki/main.tex` (東工大区分の統合マスターTeX)

**Interfaces:**
* Consumes: `src/sample_titech/kouki/` 配下の全年度・全大問
* Produces: 東工大の一括解答集PDF `src/sample_titech/kouki/main.pdf`

- [ ] **Step 1: 東工大統合マスター `src/sample_titech/kouki/main.tex` を作成する**

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

\title{東京工業大学 後期 数学過去問解答集 (サンプル)}
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

% --- 1995年 ---
\part*{1995年}
\section*{第1問}
\input{1995/1/problem.tex}
\subsection*{解答}
\input{1995/1/solution.tex}
\clearpage

% --- 2000年 ---
\part*{2000年}
\section*{第1問}
\input{2000/1/problem.tex}
\subsection*{解答}
\input{2000/1/solution.tex}
\clearpage

\end{document}
```

- [ ] **Step 2: 東工大および東大の両方のマスターPDFをビルド検証する**

Run:
```bash
cd src/sample_titech/kouki && latexmk -lualatex main.tex
cd ../../../sample_todai/zenki && latexmk -lualatex main.tex
```
Expected: 双方ともエラーなく `main.pdf` が生成される。

- [ ] **Step 3: コミット**

```bash
git add src/sample_titech/kouki/main.tex
git commit -m "feat: construct unified master main.tex for Titech (sample_titech)"
```

---
