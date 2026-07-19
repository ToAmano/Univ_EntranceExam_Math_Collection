# 数学過去問解答プラットフォーム 実装計画書 (TikZ・改ページ検証追加版)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 複数箇所に散らばっている数学過去問解答（TeXと手書きPDF）を「大問フォルダ一体型」に移行・統合し、AstroでのWeb公開（GitHub Pages）とLuaLaTeXでのPDFビルド・CI/CDを構築する。特に、TikZ図形をSVGとして自動コンパイル・Web埋め込みする仕組みと、PDF一括ビルド時の大問ごとの改ページを検証する。

**Architecture:** LaTeXソース（`src/`）をマスターとし、Astro (web/) へPandocで自動Markdown変換してKaTeXで静的描画。TikZブロックは一時的にLuaLaTeXでコンパイルし `pdftocairo` でSVG化して埋め込み。PDFはLuaLaTeX/latexmkでビルド。GitHub Actionsでこれらを自動化。

**Tech Stack:** Python 3, Astro (v4.x), KaTeX (rehype-katex), TailwindCSS, Pandoc, LuaLaTeX / latexmk, poppler-utils (pdftocairo), GitHub Actions

## Global Constraints
* すべてのLaTeXソースは `src/` 以下に配置し、「大問フォルダ一体型」（例: `src/todai/zenki/1990/1/problem.tex`）とする。
* 既存 of TeXファイル（`titech_kouki` 内のソースなど）を操作する際は、**絶対にコピーのみを行い、元ファイルを書き換え・移動しない**こと。
* Webプロジェクトは `web/` ディレクトリ内にAstroで作成する。
* LaTeX ➔ MD への変換は Pandoc をベースにし、マクロ等の前処理・後処理は Python で実施する。
* 全ての成果物のPDFは `raw_handwriting_archive/` に旧手書きデータを退避させ、一元管理する。

---

### Task 1: 検証用データの作成 (既存のTikZ入りTeXのコピー)

**Files:**
* Create: `src/sample_todai/zenki/1995/2/problem.tex` (東大1995年後期第2問のコピー)
* Create: `src/sample_todai/zenki/1995/2/solution.tex` (同・解答のコピー。TikZ図が3つ、tabular表が1つ含まれる)
* Modify (from Task 1): `src/sample_todai/zenki/1990/1/problem.tex`, `solution.tex` (以前のダミーデータ)

**Interfaces:**
* Consumes: `/Users/amano/works/research/titech_kouki/UtokyoKouki/manuscript/docs/problems/1995/2/problem.tex`, `/Users/amano/works/research/titech_kouki/UtokyoKouki/manuscript/docs/solutions/1995/2/solutions.tex`
* Produces: 実際のTikZを含むテスト用データフォルダ `src/sample_todai/zenki/1995/2/`

- [ ] **Step 1: 既存の1995年第2問「問題文」を `src/sample_todai/` 以下にコピーする**

* 元ファイル: `/Users/amano/works/research/titech_kouki/UtokyoKouki/manuscript/docs/problems/1995/2/problem.tex`
* コピー先: `src/sample_todai/zenki/1995/2/problem.tex`
(※ディレクトリが無い場合は作成してコピーする。)

- [ ] **Step 2: 既存の1995年第2問「解答文」を `src/sample_todai/` 以下にコピーする**

* 元ファイル: `/Users/amano/works/research/titech_kouki/UtokyoKouki/manuscript/docs/solutions/1995/2/solutions.tex`
* コピー先: `src/sample_todai/zenki/1995/2/solution.tex`

- [ ] **Step 3: コピーされたファイルに問題がないか確認する**

Run: `git status`
Expected: `src/sample_todai/zenki/1995/2/problem.tex` と `solution.tex` が Untracked として検出される。既存の `titech_kouki` 側には変更がないことを確認する。

- [ ] **Step 4: コミット**

```bash
git add src/sample_todai/
git commit -m "feat: copy real 1995 exam TeX files for TikZ and pagination testing"
```

---

### Task 2: Astroプロジェクトのセットアップと数式表示の導入

(すでに実装済み。変更がないか再度ビルドを確認)

- [ ] **Step 1: `web/` 内でAstroビルドが正常に通ることを確認する**

Run: `cd web && npm run build`
Expected: エラーなく `dist/` が作成される。

---

### Task 3: LaTeX ➔ Markdown 変換ツールの実装 (TikZのSVG自動画像化対応)

**Files:**
* Modify: `scratch/tex_to_md.py` (変換スクリプトを拡張してTikZ抽出・SVGコンパイル・MD画像置換を実装)
* Modify: `tests/scratch/test_converter.py` (TikZ処理ロジックのテスト追加)

**Interfaces:**
* Consumes: `src/[大学]/[区分]/[年度]/[大問]/[problem.tex|solution.tex]` (TikZコードを含む)
* Produces: `web/src/content/solutions/[ファイル名].md` 内の `![図](/Math-Solutions/images/tikz/[ファイル名]_[図ID].svg)` タグ、および `web/public/images/tikz/[ファイル名]_[図ID].svg`

- [ ] **Step 1: TikZ抽出・コンパイル用のロジックが正しいかを検証するテストコードを `tests/scratch/test_converter.py` に追加する**

```python
# tests/scratch/test_converter.py の末尾に追加
    def test_tikz_extraction_and_replacement(self):
        latex = r"""
        問題文です。
        \begin{figure}[H]
          \begin{tikzpicture}
            \draw (0,0) -- (1,1);
          \end{tikzpicture}
          \caption{図}
        \end{figure}
        """
        # 置換後のテキストに markdown 画像タグが含まれているか検証
        processed = preprocess_latex(latex) # 実装側でTikZ置換ロジックを呼び出す
        self.assertIn("![TikZ図]", processed)
```

- [ ] **Step 2: 変換スクリプト `scratch/tex_to_md.py` に TikZ画像化・置換の処理を実装する**

```python
# scratch/tex_to_md.py
import os
import re
import sys
import subprocess
import tempfile
import shutil

# 独自マクロ置換
def preprocess_latex_macros(content):
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\R(?![a-zA-Z])', r'\1\\mathbb{R}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\C(?![a-zA-Z])', r'\1\\mathbb{C}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\N(?![a-zA-Z])', r'\1\\mathbb{N}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\Z(?![a-zA-Z])', r'\1\\mathbb{Z}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\Q(?![a-zA-Z])', r'\1\\mathbb{Q}', content)
    content = re.sub(r'\\bm\{((?:[^{}]|\{[^{}]*\})*)\}', r'\\mathbf{\1}', content)
    return content

# TikZを抽出し、SVG画像化してMarkdownの画像タグに置換する
def render_tikz_to_svg(content, base_name):
    # Astro公開ディレクトリ
    public_tikz_dir = "web/public/images/tikz"
    os.makedirs(public_tikz_dir, exist_ok=True)

    # TikZ環境の抽出
    pattern = re.compile(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', re.DOTALL)
    matches = pattern.findall(content)
    
    for i, tikz_code in enumerate(matches):
        full_tikz = f"\\begin{{tikzpicture}}{tikz_code}\\end{{tikzpicture}}"
        fig_id = f"{base_name}_tikz_{i+1}"
        svg_filename = f"{fig_id}.svg"
        svg_dest_path = os.path.join(public_tikz_dir, svg_filename)
        
        # 1. 最小限の standalone LaTeX ドキュメントを作成
        standalone_latex = f"""\\documentclass{{standalone}}
\\usepackage{{tikz}}
\\usepackage{{pgfplots}}
\\pgfplotsset{{compat=1.18}}
\\usetikzlibrary{{angles,quotes}}
\\begin{{document}}
{full_tikz}
\\end{{document}}
"""
        # 一時ディレクトリでビルド
        with tempfile.TemporaryDirectory() as tmpdir:
            tex_file = os.path.join(tmpdir, "tikz.tex")
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.write(standalone_latex)
                
            # Compile to PDF using pdflatex or lualatex
            try:
                subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "tikz.tex"],
                    cwd=tmpdir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
                )
                pdf_file = os.path.join(tmpdir, "tikz.pdf")
                
                # Convert PDF to SVG using pdftocairo
                subprocess.run(
                    ["pdftocairo", "-svg", pdf_file, svg_dest_path],
                    check=True
                )
            except Exception as e:
                sys.stderr.write(f"Warning: Failed to compile TikZ for {fig_id}: {e}\n")
                # 失敗時はプレースホルダー画像を配置するか、元のコードのままとする
                continue

        # Markdown画像タグに置換
        md_image_tag = f"![TikZ図](/Math-Solutions/images/tikz/{svg_filename})"
        content = content.replace(full_tikz, md_image_tag)
        
    return content

def convert_tex_to_md(tex_path, output_md_path, frontmatter, base_name):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # マクロ置換
    processed_content = preprocess_latex_macros(content)
    # TikZ置換
    processed_content = render_tikz_to_svg(processed_content, base_name)
    
    # テンポラリファイルを作成してPandocで変換
    temp_tex = tex_path + ".temp.tex"
    with open(temp_tex, 'w', encoding='utf-8') as f:
        f.write(processed_content)
        
    try:
        cmd = ["pandoc", temp_tex, "-t", "markdown", "--mathjax"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        md_body = result.stdout
    finally:
        if os.path.exists(temp_tex):
            os.remove(temp_tex)

    # Frontmatterを付与して保存
    fm_str = "---\n"
    for k, v in frontmatter.items():
        # クォートのエスケープ
        escaped_v = str(v).replace('"', '\\"')
        fm_str += f"{k}: \"{escaped_v}\"\n"
    fm_str += "---\n\n"
    
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(fm_str + md_body)

def process_all_src():
    src_root = "src"
    dest_root = "web/src/content/solutions"
    has_errors = False
    
    for root, _, files in os.walk(src_root):
        for file in files:
            if file in ("problem.tex", "solution.tex"):
                parts = os.path.normpath(root).split(os.sep)
                # 深さ制限チェック（5番目の要素まで）
                if len(parts) == 5: 
                    uni, category, year, q_num = parts[1], parts[2], parts[3], parts[4]
                    type_str = "problem" if file == "problem.tex" else "solution"
                    
                    base_name = f"{uni}-{category}-{year}-{q_num}"
                    output_name = f"{base_name}-{type_str}.md"
                    output_path = os.path.join(dest_root, output_name)
                    
                    fm = {
                        "university": uni,
                        "category": category,
                        "year": year,
                        "question": q_num,
                        "type": type_str,
                        "title": f"{uni.upper()} {year} {category} Q{q_num} ({type_str})"
                    }
                    
                    try:
                        convert_tex_to_md(os.path.join(root, file), output_path, fm, base_name)
                    except Exception as e:
                        sys.stderr.write(f"Error converting {os.path.join(root, file)}: {e}\n")
                        has_errors = True
                        
    if has_errors:
        sys.exit(1)

if __name__ == "__main__":
    process_all_src()
```

- [ ] **Step 3: テストを実行して成功することを確認する**

Run: `python3 -m unittest tests/scratch/test_converter.py`
Expected: `OK`

- [ ] **Step 4: 実際に 1995年後期のTikZ入りTeXの変換を走らせる**

Run: `python3 scratch/tex_to_md.py`
Expected:
* `web/src/content/solutions/sample_todai-zenki-1995-2-solution.md` が生成される。
* `web/public/images/tikz/` 以下に3つのSVGファイル（`sample_todai-zenki-1995-2_tikz_1.svg` 等）が生成され、Markdown内には `![TikZ図](...)` として埋め込まれている。

- [ ] **Step 5: コミット**

```bash
git add scratch/tex_to_md.py tests/scratch/test_converter.py
git commit -m "feat: add TikZ automatic SVG compilation and image replacement support"
```

---

### Task 4: GitHub Actionsによる自動デプロイとPDFビルドパイプラインの構築

(TikZ画像化のために、GitHub Actions側に `poppler-utils` と `pdftocairo`、LaTeXコンパイル環境を追加します)

**Files:**
* Modify: `.github/workflows/deploy-pages.yml`

- [ ] **Step 1: `deploy-pages.yml` の中に、画像変換ユーティリティとTeX Live環境のセットアップを追加する**

```yaml
# .github/workflows/deploy-pages.yml への変更点
# ...
      - name: Install Pandoc and TikZ dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y pandoc poppler-utils texlive-latex-base texlive-latex-extra texlive-pictures texlive-science
# ...
```

- [ ] **Step 2: コミット**

```bash
git add .github/workflows/deploy-pages.yml
git commit -m "ci: add latex and poppler-utils dependencies for TikZ rendering on GitHub Pages deploy"
```

---

### Task 5: README.mdのアップデート

(すでに実装済み。Astroのローカル実行方法などを記述)

---

### Task 6: PDF一括ビルドテストと大問ごとの改ページの検証 (新規)

**Files:**
* Create: `src/sample_todai/zenki/1995/main.tex` (1995年度の一括ビルド用マスターファイル)

**Interfaces:**
* Consumes: `src/sample_todai/zenki/1995/2/problem.tex`, `solution.tex`
* Produces: 大問ごとに正しく改ページ（`\clearpage`）される一括解答PDF

- [ ] **Step 1: 1995年度の一括ビルド用マスターTeX `src/sample_todai/zenki/1995/main.tex` を作成する**

```latex
\documentclass[a4paper,11pt]{article}
\usepackage{amsmath,amssymb}
\usepackage{bm}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{angles,quotes}

\title{東京大学 1995年 前期 理系数学解答集 (ダミー)}
\author{Math-Solutions}
\date{\today}

\begin{document}
\maketitle
\clearpage

% --- 第1問 (1990年の問題などを仮に読み込む) ---
\section*{第1問}
\input{../../1990/1/problem.tex}
\subsection*{解答}
\input{../../1990/1/solution.tex}
\clearpage % 確実に改ページを保証

% --- 第2問 (今回移行したTikZ入りの1995年問題) ---
\section*{第2問}
\input{2/problem.tex}
\subsection*{解答}
\input{2/solution.tex}
\clearpage % 確実に改ページを保証

\end{document}
```

- [ ] **Step 2: 一括ビルドを実行し、PDFをコンパイルする**

Run: `cd src/sample_todai/zenki/1995 && latexmk -lualatex main.tex`
Expected: `main.pdf` が正常に出力され、ビルドエラーが発生しないこと。

- [ ] **Step 3: 生成されたPDFを確認し、大問1と大問2が異なるページに開始（改ページが機能）していることを検証する**

(PDFビューアー等で、第1問の解答の後に `\clearpage` が効いて、第2問が新しいページから開始していることを視覚的に確認する)

- [ ] **Step 4: コミット**

```bash
git add src/sample_todai/zenki/1995/main.tex
git commit -m "feat: add 1995 master main.tex and verify PDF compilation with page breaks"
```

---
