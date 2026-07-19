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

### Task 1: マイグレーションスクリプトの実装と実行

**Files:**
* Create: `scratch/migrate.py` (マイグレーションPythonスクリプト)
* Test: `tests/scratch/test_migrate.py` (移行ロジックの単体テスト)

**Interfaces:**
* Consumes: `/Users/amano/works/research/titech_kouki`, `/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions`
* Produces: `src/[todai|kyodai|titech]/[zenki|kouki]/[年度]/[大問]/[problem.tex|solution.tex]` の配置構造

- [ ] **Step 1: 移行テスト用のテストコードを書く**

移行のパス変換ロジックが正しいかを検証するテストコードを `tests/scratch/test_migrate.py` に作成する。

```python
# tests/scratch/test_migrate.py
import unittest
from scratch.migrate import parse_homepage_path, parse_titech_path

class TestMigration(unittest.TestCase):
    def test_parse_titech_path(self):
        # titech_koukiのパスから新構造へのパス変換を検証
        src_path = "/Users/amano/works/research/titech_kouki/KyotoUKouki/manuscript/docs/problems/1989/1/problem.tex"
        dest = parse_titech_path(src_path)
        self.assertEqual(dest, "src/kyodai/kouki/1989/1/problem.tex")

    def test_parse_homepage_path(self):
        # homepageのパスから新構造へのパス変換を検証
        src_path = "/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions/todai/todai-zenki/1961/61-1/ut-61-1.tex"
        dest = parse_homepage_path(src_path)
        self.assertEqual(dest, "src/todai/zenki/1961/1/solution.tex")

if __name__ == '__main__':
    unittest.main()
```

- [ ] **Step 2: テストを実行して失敗することを確認する**

Run: `python3 -m unittest tests/scratch/test_migrate.py`
Expected: `ModuleNotFoundError: No module named 'scratch.migrate'` またはテスト失敗。

- [ ] **Step 3: 移行スクリプト `scratch/migrate.py` を実装する**

```python
# scratch/migrate.py
import os
import re
import shutil

def parse_titech_path(path):
    # KyotoUKouki, TitechKouki, UtokyoKouki の変換
    path = os.path.normpath(path)
    parts = path.split(os.sep)
    
    # 大学名マッピング
    uni_map = {"KyotoUKouki": "kyodai", "TitechKouki": "titech", "UtokyoKouki": "todai"}
    uni = None
    for k, v in uni_map.items():
        if k in parts:
            uni = v
            break
    
    # 区分はすべてkouki
    category = "kouki"
    
    # 年度と大問の抽出
    # partsからproblems/solutionsのインデックスを探す
    idx = -1
    for i, part in enumerate(parts):
        if part in ("problems", "solutions"):
            idx = i
            break
            
    if idx == -1:
        return None
        
    year = parts[idx + 1]
    q_num = parts[idx + 2]
    filename = parts[-1]
    
    # ファイル名標準化
    if "problem" in filename or "problems" in filename:
        target_file = "problem.tex"
    else:
        target_file = "solution.tex"
        
    return f"src/{uni}/{category}/{year}/{q_num}/{target_file}"

def parse_homepage_path(path):
    path = os.path.normpath(path)
    parts = path.split(os.sep)
    
    # 大学と区分の特定
    if "todai-zenki" in parts:
        uni, category = "todai", "zenki"
    elif "todai-kouki" in parts:
        uni, category = "todai", "kouki"
    elif "kyodai" in parts and "zenki" in parts:
        uni, category = "kyodai", "zenki"
    elif "toukou" in parts and "toukou-zenki" in parts:
        uni, category = "titech", "zenki"
    elif "toukou-kouki" in parts:
        uni, category = "titech", "kouki"
    else:
        return None
        
    # 年度の特定 (4桁の数字)
    year = None
    for part in parts:
        if part.isdigit() and len(part) == 4:
            year = part
            break
        elif part.startswith("t") and part[1:].isdigit() and len(part) == 5:
            year = part[1:]
            break
            
    if not year:
        return None
        
    # 大問番号の特定
    # 末尾のフォルダが "61-1" や "t79-1" などの形になっている
    last_folder = parts[-2]
    q_match = re.search(r'-(\d+)$', last_folder)
    if not q_match:
        # 大問フォルダがないフラット配置の場合
        filename = parts[-1]
        fn_match = re.search(r'-(\d+)\.tex$', filename)
        q_num = fn_match.group(1) if fn_match else "1"
    else:
        q_num = q_match.group(1)
        
    filename = parts[-1]
    # ファイル名標準化
    if "p.tex" in filename or "prob" in filename:
        target_file = "problem.tex"
    else:
        target_file = "solution.tex"
        
    return f"src/{uni}/{category}/{year}/{q_num}/{target_file}"

def execute_migration(dry_run=True):
    titech_root = "/Users/amano/works/research/titech_kouki"
    homepage_root = "/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions"
    dest_root = "/Users/amano/works/research/Math-Solutions"
    
    # 1. titech_kouki の走査と移行
    for root, _, files in os.walk(titech_root):
        for file in files:
            if file.endswith(".tex") and not file.startswith("."):
                src_path = os.path.join(root, file)
                # manuscript/docs以下のものだけ対象
                if "manuscript" in src_path and "docs" in src_path:
                    dest_rel = parse_titech_path(src_path)
                    if dest_rel:
                        dest_abs = os.path.join(dest_root, dest_rel)
                        if dry_run:
                            print(f"[DRY RUN] Copy: {src_path} -> {dest_abs}")
                        else:
                            os.makedirs(os.path.dirname(dest_abs), exist_ok=True)
                            shutil.copy2(src_path, dest_abs)

    # 2. homepage_solutions の走査と移行
    for root, _, files in os.walk(homepage_root):
        for file in files:
            if file.endswith(".tex") and not file.startswith("."):
                src_path = os.path.join(root, file)
                dest_rel = parse_homepage_path(src_path)
                if dest_rel:
                    dest_abs = os.path.join(dest_root, dest_rel)
                    if dry_run:
                        print(f"[DRY RUN] Copy: {src_path} -> {dest_abs}")
                    else:
                        os.makedirs(os.path.dirname(dest_abs), exist_ok=True)
                        shutil.copy2(src_path, dest_abs)

if __name__ == "__main__":
    import sys
    dry = "--run" not in sys.argv
    if dry:
        print("--- Dry Run Mode ---")
    execute_migration(dry_run=dry)
```

- [ ] **Step 4: テストを実行して成功することを確認する**

Run: `python3 -m unittest tests/scratch/test_migrate.py`
Expected: `OK` (テストがすべてパス)

- [ ] **Step 5: マイグレーションを実行する**

Run: `python3 scratch/migrate.py --run`
Expected: データが本リポジトリの `src/` 以下にコピーされる。

- [ ] **Step 6: コミット**

```bash
git add scratch/migrate.py tests/scratch/test_migrate.py
git commit -m "feat: add migration script and run migration"
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

### Task 5: 重複PDFのクリーンアップとREADME.mdのアップデート

**Files:**
* Modify: `README.md`
* Create: `raw_handwriting_archive/`
* Modify: 重複している手書きPDFファイルを削除・退避

- [ ] **Step 1: 手書きPDFの重複ファイルをアーカイブフォルダに退避・整理する**

* `homepage_solutions/京都前期_整理完了/` ➔ `raw_handwriting_archive/kyodai/zenki/` へコピー
* `homepage_solutions/東大前期_整理完了/` ➔ `raw_handwriting_archive/todai/zenki/` へコピー
* 重複している京大・東工大・東大後期の手書きPDFのハッシュ値やファイルサイズを確認し、不要な方を削除・クリーンアップ。

- [ ] **Step 2: リポジトリの `README.md` を最新化する**

```markdown
# 東大・京大・東工大 数学過去問解答ライブラリ

東大、京大、東工大の理系数学の過去問解答（手書きPDFおよびTeXによる高品質解答）を公開・管理するリポジトリです。

## 🌐 公開サイト (GitHub Pages)
最新の解答は以下のサイトでご覧いただけます。数式が高速で表示され、スマートフォンにも最適化されています。
👉 **[過去問解答サイトのURL（予定）](https://amano.github.io/Math-Solutions/)**

## 📂 リポジトリ構成

* `src/`: LaTeXによる解答ソース（マスターデータ）。大問フォルダ一体型で管理。
* `web/`: AstroによるWebサイトプロジェクト。
* `raw_handwriting_archive/`: 高校時代に作成した手書き答案PDFのオリジナルデータ。
  * `todai/`: 東大（前期・後期）
  * `kyodai/`: 京大（前期・後期）
  * `titech/`: 東工大（前期・後期）

## 🛠️ ローカルでのビルド方法

### 1. Webサイトのローカル開発
```bash
cd web
npm install
npm run dev
```

### 2. PDF書籍のビルド (LuaLaTeX)
```bash
cd src/todai/zenki/1990
latexmk -lualatex main.tex
```
```

- [ ] **Step 3: コミット**

```bash
git add README.md
git commit -m "docs: update README to match new repository structure"
```

---
