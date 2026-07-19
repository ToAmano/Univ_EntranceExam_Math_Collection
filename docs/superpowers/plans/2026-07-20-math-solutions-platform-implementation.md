# 数学過去問解答プラットフォーム 実装計画書

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 複数箇所に散らばっている数学過去問解答（TeXと手書きPDF）を「大問フォルダ一体型」に移行・統合し、AstroでのWeb公開（GitHub Pages）とLuaLaTeXでのPDFビルド・CI/CDを構築する。

**Architecture:** LaTeXソース（`src/`）をマスターとし、Astro (web/) へPandocで自動Markdown変換してKaTeXで静的描画。PDFはLuaLaTeX/latexmkでビルド。GitHub Actionsでこれらを自動化。

**Tech Stack:** Python 3, Astro (v4.x), KaTeX (rehype-katex), TailwindCSS, Pandoc, LuaLaTeX / latexmk, GitHub Actions

## Global Constraints
* すべてのLaTeXソースは `src/` 以下に配置し、「大問フォルダ一体型」（例: `src/todai/zenki/1990/1/problem.tex`）とする。
* Webプロジェクトは `web/` ディレクトリ内にAstroで作成する。
* LaTeX ➔ MD への変換は Pandoc をベースにし、マクロ等の前処理・後処理は Python で実施する。
* 全ての成果物のPDFは `raw_handwriting_archive/` に旧手書きデータを退避させ、一元管理する。

---

### Task 1: テスト用ダミーデータの作成

**Files:**
* Create: `src/sample_todai/zenki/1990/1/problem.tex` (検証用のダミー問題TeX)
* Create: `src/sample_todai/zenki/1990/1/solution.tex` (検証用のダミー解答TeX)

**Interfaces:**
* Consumes: なし
* Produces: テスト検証用のLaTeXフォルダ構造 (`src/sample_todai/zenki/1990/1/`)

- [ ] **Step 1: ダミー問題ファイル `src/sample_todai/zenki/1990/1/problem.tex` を作成する**

```latex
\documentclass{article}
\usepackage{amsmath}
\usepackage{bm}

\begin{document}
東大 1990年 前期 理系数学 第1問の問題文です。

ベクトル $\bm{a} = (1, 2)$ と実数の集合 $\R$ について考えます。
\end{document}
```

- [ ] **Step 2: ダミー解答ファイル `src/sample_todai/zenki/1990/1/solution.tex` を作成する**

```latex
\documentclass{article}
\usepackage{amsmath}
\usepackage{bm}

\begin{document}
東大 1990年 前期 理系数学 第1問の解答文です。

求める値は次の通りです：
\[
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\]
\end{document}
```

- [ ] **Step 3: ディレクトリ構造が正しく作成されたか確認する**

Run: `find src/sample_todai`
Expected:
```
src/sample_todai
src/sample_todai/zenki
src/sample_todai/zenki/1990
src/sample_todai/zenki/1990/1
src/sample_todai/zenki/1990/1/problem.tex
src/sample_todai/zenki/1990/1/solution.tex
```

- [ ] **Step 4: コミット**

```bash
git add src/sample_todai/
git commit -m "feat: add dummy TeX files for testing"
```

---

### Task 2: Astroプロジェクトのセットアップと数式表示の導入

**Files:**
* Create: `web/package.json`
* Create: `web/astro.config.mjs`
* Create: `web/src/layouts/Layout.astro`
* Create: `web/src/pages/index.astro`

**Interfaces:**
* Consumes: なし（初期スキャフォールド）
* Produces: ローカルで動作し、数式を表示可能なAstroサイト

- [ ] **Step 1: `web/package.json` を作成する**

```json
{
  "name": "math-solutions-web",
  "type": "module",
  "version": "1.0.0",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "astro": "^4.11.3",
    "rehype-katex": "^7.0.0",
    "remark-math": "^6.0.0"
  }
}
```

- [ ] **Step 2: `web/astro.config.mjs` を作成し、KaTeXプラグインを設定する**

```javascript
import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

export default defineConfig({
  site: 'https://amano.github.io', // ユーザーのIDに合わせて変更
  base: '/Math-Solutions',         // リポジトリ名
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
});
```

- [ ] **Step 3: 共通レイアウト `web/src/layouts/Layout.astro` を作成する（KaTeXのCSSを読み込み、Glassmorphism調にデザインする）**

```html
---
interface Props {
	title: string;
}
const { title } = Astro.props;
---
<!doctype html>
<html lang="ja">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width" />
		<title>{title}</title>
		<!-- KaTeX CSS for equation rendering -->
		<link
			rel="stylesheet"
			href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css"
		/>
		<style is:global>
			body {
				font-family: 'Inter', sans-serif;
				background: radial-gradient(circle at 50% 50%, #121824 0%, #080c14 100%);
				color: #e2e8f0;
				min-height: 100vh;
				margin: 0;
			}
			/* Glassmorphism card utility */
			.glass {
				background: rgba(255, 255, 255, 0.03);
				backdrop-filter: blur(12px);
				border: 1px solid rgba(255, 255, 255, 0.08);
				border-radius: 12px;
			}
		</style>
	</head>
	<body>
		<main style="max-width: 800px; margin: 0 auto; padding: 2rem;">
			<slot />
		</main>
	</body>
</html>
```

- [ ] **Step 4: トップページ `web/src/pages/index.astro` を作成する**

```html
---
import Layout from '../layouts/Layout.astro';
---
<Layout title="東大・東工大・京大数学過去問解答">
	<div class="glass" style="padding: 2rem; text-align: center; margin-bottom: 2rem;">
		<h1 style="margin: 0; font-size: 2.5rem; background: linear-gradient(to right, #60a5fa, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
			大学入試数学 過去問解答ライブラリ
		</h1>
		<p style="color: #94a3b8; margin-top: 1rem;">
			東大・京大・東工大の理系数学解答を、TeXコンパイル済みの美しいHTMLとPDFで公開しています。
		</p>
	</div>
	
	<div class="glass" style="padding: 2rem;">
		<h2>テスト用数式描画</h2>
		<p>インライン数式: $E = mc^2$</p>
		<p>ブロック数式:</p>
		$$
		\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
		$$
	</div>
</Layout>
```

- [ ] **Step 5: パッケージをインストールして動作確認する**

Run: `cd web && npm install`
Run: `npm run build` (ビルドが正常に終了するか確認)
Expected: エラーなく `dist/` が作成される。

- [ ] **Step 6: コミット**

```bash
git add web/package.json web/astro.config.mjs web/src/
git commit -m "feat: setup astro web project with KaTeX"
```

---

### Task 3: LaTeX ➔ Markdown 変換ツールの実装

**Files:**
* Create: `scratch/tex_to_md.py` (LaTeXからMDへの変換＋置換スクリプト)
* Test: `tests/scratch/test_converter.py` (マクロ置換の単体テスト)

**Interfaces:**
* Consumes: `src/[大学]/[区分]/[年度]/[大問]/[problem.tex|solution.tex]`
* Produces: `web/src/content/solutions/[大学]-[区分]-[年度]-[大問].md`

- [ ] **Step 1: 変換スクリプトのテストコードを書く**

```python
# tests/scratch/test_converter.py
import unittest
from scratch.tex_to_md import preprocess_latex

class TestConverter(unittest.TestCase):
    def test_preprocess_latex(self):
        # 独自マクロの置換を検証
        latex = r"ベクトル $\bm{a}$ と実数集合 $\R$"
        processed = preprocess_latex(latex)
        self.assertEqual(processed, r"ベクトル $\mathbf{a}$ と実数集合 $\mathbb{R}$")

if __name__ == '__main__':
    unittest.main()
```

- [ ] **Step 2: テストを実行して失敗することを確認する**

Run: `python3 -m unittest tests/scratch/test_converter.py`
Expected: `ModuleNotFoundError: No module named 'scratch.tex_to_md'`

- [ ] **Step 3: 変換スクリプト `scratch/tex_to_md.py` を実装する**

```python
# scratch/tex_to_md.py
import os
import re
import subprocess

def preprocess_latex(content):
    # \bm{x} ➔ \mathbf{x}
    content = re.sub(r'\\bm\{([^}]+)\}', r'\\mathbf{\1}', content)
    # \R ➔ \mathbb{R}
    content = content.replace(r'\R', r'\mathbb{R}')
    content = content.replace(r'\C', r'\mathbb{C}')
    content = content.replace(r'\N', r'\mathbb{N}')
    content = content.replace(r'\Z', r'\mathbb{Z}')
    content = content.replace(r'\Q', r'\mathbb{Q}')
    return content

def convert_tex_to_md(tex_path, output_md_path, frontmatter):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    processed_content = preprocess_latex(content)
    
    # テンポラリファイルを作成
    temp_tex = tex_path + ".temp"
    with open(temp_tex, 'w', encoding='utf-8') as f:
        f.write(processed_content)
        
    try:
        # Pandocを走らせてMarkdownへ変換
        cmd = ["pandoc", temp_tex, "-t", "markdown", "--mathjax"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        md_body = result.stdout
    finally:
        if os.path.exists(temp_tex):
            os.remove(temp_tex)

    # Frontmatterを付与して保存
    fm_str = "---\n"
    for k, v in frontmatter.items():
        fm_str += f"{k}: \"{v}\"\n"
    fm_str += "---\n\n"
    
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(fm_str + md_body)

def process_all_src():
    src_root = "src"
    dest_root = "web/src/content/solutions"
    
    for root, _, files in os.walk(src_root):
        for file in files:
            if file in ("problem.tex", "solution.tex"):
                parts = os.path.normpath(root).split(os.sep)
                if len(parts) >= 5: # src/todai/zenki/1990/1
                    uni, category, year, q_num = parts[1], parts[2], parts[3], parts[4]
                    type_str = "problem" if file == "problem.tex" else "solution"
                    
                    output_name = f"{uni}-{category}-{year}-{q_num}-{type_str}.md"
                    output_path = os.path.join(dest_root, output_name)
                    
                    fm = {
                        "university": uni,
                        "category": category,
                        "year": year,
                        "question": q_num,
                        "type": type_str,
                        "title": f"{uni.upper()} {year} {category} Q{q_num} ({type_str})"
                    }
                    
                    convert_tex_to_md(os.path.join(root, file), output_path, fm)

if __name__ == "__main__":
    process_all_src()
```

- [ ] **Step 4: テストを実行して成功することを確認する**

Run: `python3 -m unittest tests/scratch/test_converter.py`
Expected: `OK`

- [ ] **Step 5: 変換処理を実行する**

Run: `python3 scratch/tex_to_md.py`
Expected: `web/src/content/solutions/` 以下に `.md` ファイル群が生成される。

- [ ] **Step 6: コミット**

```bash
git add scratch/tex_to_md.py tests/scratch/test_converter.py
git commit -m "feat: add LaTeX to Markdown converter script"
```

---

### Task 4: GitHub Actionsによる自動デプロイとPDFビルドパイプラインの構築

**Files:**
* Create: `.github/workflows/deploy-pages.yml`
* Create: `.github/workflows/build-pdf.yml`

**Interfaces:**
* Consumes: GitHubでのプッシュ・リリースイベント
* Produces: 自動デプロイされたWebサイトと、GitHub Releaseに添付されるPDFファイル

- [ ] **Step 1: GitHub Pagesデプロイ用 Workflow を作成する**

```yaml
# .github/workflows/deploy-pages.yml
name: Deploy GitHub Pages

on:
  push:
    branches:
      - main
    paths:
      - 'src/**'
      - 'web/**'

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: 'pages'
  cancel-in-progress: true

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Pandoc
        run: sudo apt-get update && sudo apt-get install -y pandoc

      - name: Run Tex to MD conversion
        run: python3 scratch/tex_to_md.py

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: 'web/package.json'

      - name: Install dependencies
        run: cd web && npm ci

      - name: Build Astro site
        run: cd web && npm run build

      - name: Upload Pages Artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: web/dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: PDF書籍自動ビルド用 Workflow を作成する**

```yaml
# .github/workflows/build-pdf.yml
name: Build PDF Books

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write

jobs:
  build-pdf:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install TeX Live
        run: |
          sudo apt-get update
          sudo apt-get install -y texlive-lang-japanese texlive-luatex latexmk

      - name: Build PDFs
        run: |
          # 各年度の main.tex をビルドする例
          find src -name "main.tex" | while read main_tex; do
            dir=$(dirname "$main_tex")
            cd "$dir"
            latexmk -lualatex main.tex
            cd -
          done

      - name: Create Release and Upload PDFs
        uses: softprops/action-gh-release@v2
        with:
          files: |
            src/**/*.pdf
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

- [ ] **Step 3: ローカルで GitHub Actions のシンタックスをチェックする**

Run: `actionlint` が使える場合は `actionlint .github/workflows/*.yml` で検証。ない場合は目視でインデント等を再確認する。

- [ ] **Step 4: コミット**

```bash
git add .github/workflows/
git commit -m "feat: add CI/CD workflows for GitHub Pages and PDF builds"
```

---

### Task 5: README.mdのアップデート

**Files:**
* Modify: `README.md`

- [ ] **Step 1: リポジトリの `README.md` を最新化する**

```markdown
# 東大・京大・東工大 数学過去問解答ライブラリ

東大、京大、東工大の理系数学の過去問解答（手書きPDFおよびTeXによる高品質解答）を公開・管理するリポジトリです。

## 🌐 公開サイト (GitHub Pages)
最新の解答は以下のサイトでご覧いただけます。数式が高速で表示され、スマートフォンにも最適化されています。
👉 **[過去問解答サイトのURL（予定）](https://amano.github.io/Math-Solutions/)**

## 📂 リポジトリ構成

* `src/`: LaTeXによる解答ソース（マスターデータ）。大問フォルダ一体型で管理。
* `web/`: AstroによるWebサイトプロジェクト。

## 🛠️ ローカルでのビルド方法

### 1. Webサイトのローカル開発
```bash
cd web
npm install
npm run dev
```

### 2. PDF書籍のビルド (LuaLaTeX)
```bash
cd src/sample_todai/zenki/1990/1
# 個別ビルドは各フォルダにて行えます。
```
```

- [ ] **Step 2: コミット**

```bash
git add README.md
git commit -m "docs: update README to match new repository structure"
```

---
