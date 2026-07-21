# 数学過去問解答プラットフォーム 実装計画書 (階層化TikZ画像管理対応版)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 複数箇所に散らばっている数学過去問解答（TeXと手書きPDF）を「大問フォルダ一体型」に移行・統合し、AstroでのWeb公開（GitHub Pages）とLuaLaTeXでのPDFビルド・CI/CDを構築する。TikZ図形を `src/` の構造と完全に対称な階層ディレクトリ (`web/public/images/tikz/[uni]/[category]/[year]/[q_num]/fig_[N].svg`) に出力・保存する。

**Architecture:** LaTeXソース（`src/`）をマスターとし、Astro (web/) へPandocで自動Markdown変換してKaTeXで静的描画。TikZブロックは `render_tikz_to_svg` で階層化SVG画像に切り出し・コンパイル。一括PDFは `src/[大学]/[区分]/main.tex` をマスターとして `latexmk -lualatex` でビルド。

**Tech Stack:** Python 3, Astro (v4.x), KaTeX (rehype-katex), Pandoc, LuaLaTeX / latexmk, poppler-utils (pdftocairo), GitHub Actions

## Global Constraints
* すべてのLaTeXソースは `src/` 以下に配置し、「大問フォルダ一体型」（例: `src/todai/zenki/1990/1/problem.tex`）とする。
* 既存のTeXファイル（`titech_kouki` 内のソースなど）を操作する際は、**絶対にコピーのみを行い、元ファイルを書き換え・移動しない**こと。
* Webプロジェクトは `web/` ディレクトリ内にAstroで作成する。
* TikZ画像は `web/public/images/tikz/[uni]/[category]/[year]/[q_num]/fig_[N].svg` の階層構造で保存する。

---

### Task 1: 検証用データの拡張 (複数年度のTeXをコピー配置)

(実装済み)

---

### Task 2: Astroプロジェクトのセットアップと数式表示の導入

(実装済み)

---

### Task 3: LaTeX ➔ Markdown 変換ツールの実装 (階層ディレクトリ型TikZ画像化)

**Files:**
* Modify: `scratch/tex_to_md.py` (階層化ディレクトリへのSVG保存とパス置換)
* Modify: `tests/scratch/test_converter.py` (テストの引数およびパス確認)

**Interfaces:**
* Consumes: `src/[大学]/[区分]/[年度]/[大問]/[problem.tex|solution.tex]`
* Produces: `web/public/images/tikz/[大学]/[区分]/[年度]/[大問]/fig_[N].svg` および `web/src/content/solutions/` 内の `\includegraphics{/Math-Solutions/images/tikz/...}` タグ

- [ ] **Step 1: `scratch/tex_to_md.py` の TikZ 画像出力処理を階層フォルダに対応させる**

```python
# scratch/tex_to_md.py の変更点イメージ
def render_tikz_to_svg(content, uni, category, year, q_num):
    # 階層型出力ディレクトリ
    rel_tikz_dir = f"images/tikz/{uni}/{category}/{year}/{q_num}"
    public_tikz_dir = os.path.join("web/public", rel_tikz_dir)
    os.makedirs(public_tikz_dir, exist_ok=True)

    pattern = re.compile(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', re.DOTALL)
    matches = pattern.findall(content)
    
    for i, tikz_code in enumerate(matches):
        full_tikz = f"\\begin{{tikzpicture}}{tikz_code}\\end{{tikzpicture}}"
        fig_name = f"fig_{i+1}.svg"
        svg_dest_path = os.path.join(public_tikz_dir, fig_name)
        rel_svg_path = f"/Math-Solutions/{rel_tikz_dir}/{fig_name}"
        
        # ... standalone LaTeX compile & pdftocairo ...
        
        latex_image_tag = f"\\includegraphics{{{rel_svg_path}}}"
        content = content.replace(full_tikz, latex_image_tag, 1)
        
    return content
```

- [ ] **Step 2: テストコード `tests/scratch/test_converter.py` も階層パラメータに対応させる**

- [ ] **Step 3: テストを実行してパスすることを確認する**

Run: `python3 -m unittest tests/scratch/test_converter.py`
Expected: `OK`

- [ ] **Step 4: 旧フラット画像をクリーンアップし、一括変換を再実行する**

Run:
```bash
rm -rf web/public/images/tikz/*
python3 scratch/tex_to_md.py
```
Expected: `web/public/images/tikz/sample_todai/zenki/1995/2/fig_1.svg` のように階層構造で保存される。

- [ ] **Step 5: Astroビルドを通す**

Run: `cd web && npm run build`
Expected: エラー0で完了。

- [ ] **Step 6: コミット**

```bash
git add scratch/tex_to_md.py tests/scratch/test_converter.py web/public/images/tikz/ web/src/content/solutions/
git commit -m "feat: restructure TikZ SVG storage path into hierarchical directories matching src tree"
```

---

### Task 4: GitHub Actionsパイプラインの確認

(実装済み)

---

### Task 5: README.mdの更新

(実装済み)

---

### Task 6: 統合マスター `main.tex` の構築とPDF一括ビルド・改ページ検証

(実装済み)

---
