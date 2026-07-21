# 数学過去問解答プラットフォーム 実装計画書 (Webレイアウト刷新 & 0番サマリ統合版)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Webポータルのトップページ (`index.astro`) と全解答ページをモダンなデザインシステム（カードナビゲーション、パンくずリスト、大学・年度フィルター）で刷新する。また、各年度の `0` 番フォルダに入っている「年度サマリ（難易度・テーマ・全解答一覧・試験形態解説）」を自動変換し、Webポータル上およびPDFマスター (`main.tex`) の各年度冒頭に組み込む。

**Architecture:** LaTeXソース（`src/`）をマスターとし、`0` 番サマリ含む全問題を `scratch/tex_to_md.py` でMarkdown変換。Astro (web/) では `index.astro` で大学・区分・年度別の全過去問アーカイブカードを提供し、`solutions/[...slug].astro` でパンくずナビゲーション付きの詳細解答を表示。一括PDFは `src/[大学]/[区分]/main.tex` の各年度冒頭に `0/solution.tex` を挟み `latexmk -lualatex` でビルド。

**Tech Stack:** Astro (v4.x), KaTeX (rehype-katex), Vanilla CSS, Pandoc, LuaLaTeX / latexmk, Python 3, GitHub Actions

## Global Constraints
* すべてのLaTeXソースは `src/` 以下に配置し、「大問フォルダ一体型」（例: `src/sample_titech/kouki/1990/0/solution.tex`）とする。
* 既存のTeXファイル（`titech_kouki` 内のソースなど）を操作する際は、**絶対にコピーのみを行い、元ファイルを書き換え・移動しない**こと。
* WebプロジェクトのUIは `web/` ディレクトリ内で構築し、トップページ `index.astro` から全大学・全年度・全過去問に簡単にアクセスできるようにする。

---

### Task 1: 年度サマリ (0番) サンプルデータの複製と配置

**Files:**
* Create: `src/sample_titech/kouki/1990/0/solution.tex`
* Create: `src/sample_titech/kouki/1995/0/solution.tex`

- [ ] **Step 1: `titech_kouki` から 1990/0, 1995/0 の `solutions.tex` を `src/sample_titech/kouki/[year]/0/solution.tex` にコピーする**
- [ ] **Step 2: コミットする**

---

### Task 2: Astro WebポータルのUIレイアウト刷新と `index.astro` 構築

**Files:**
* Modify: `web/src/pages/index.astro` (大学・区分・年度カードナビゲーションとトップページ刷新)
* Modify: `web/src/pages/solutions/[...slug].astro` (パンくずナビゲーション、サイドバー/戻るリンクの強化)
* Modify: `web/src/layouts/Layout.astro` (ヘッダー・フッター・ナビゲーションレイアウト)

- [ ] **Step 1: `Layout.astro` に統合ヘッダー・フッター・パンくずナビゲーションを追加**
- [ ] **Step 2: `index.astro` に大学・区分・年度別アーカイブカードビューを構築**
- [ ] **Step 3: `solutions/[...slug].astro` にサマリ表示およびパンくずナビゲーションを組み込み**
- [ ] **Step 4: `cd web && npm run build` でビルドを通す**
- [ ] **Step 5: コミットする**

---

### Task 3: LaTeX ➔ Markdown 変換ツールの `0` 番サマリ対応

**Files:**
* Modify: `scratch/tex_to_md.py` (`q_num == "0"` のサマリパースと Frontmatter 生成)

- [ ] **Step 1: `q_num == "0"` の場合に `type: "summary"`, `title: "XXXX年 全体サマリ"` を Frontmatter に付与**
- [ ] **Step 2: 一括変換を実行し、`web/src/content/solutions/` にサマリMarkdownが生成されることを確認**
- [ ] **Step 3: コミットする**

---

### Task 4: GitHub Actionsパイプラインの確認

(実装済み)

---

### Task 5: README.mdの更新

(実装済み)

---

### Task 6: PDF一括マスター `main.tex` での `0` 番サマリ組み込みとPDFビルド検証

**Files:**
* Modify: `src/sample_titech/kouki/main.tex` (`\part*{1990年}` 直後への `0/solution.tex` 挿入)

- [ ] **Step 1: `src/sample_titech/kouki/main.tex` の各年度冒頭に `\input{YEAR/0/solution.tex}` と `\clearpage` を配置**
- [ ] **Step 2: `cd src/sample_titech/kouki && latexmk -lualatex main.tex` でPDFコンパイルし、サマリページが先頭に挿入されていることを確認**
- [ ] **Step 3: コミットする**

---
