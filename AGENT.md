# AGENT.md - Math-Solutions 開発・変換引き継ぎガイドライン

## 1. プロジェクト概要

本リポジトリは、複数大学（東大 `sample_todai` / 東工大 `sample_titech` 等）の数学過去問・解答 TeX ソースを管理し、Web ポータル（Astro）への自動 Markdown 変換および LuaLaTeX に統合マスター PDF の生成を行うマルチ大学対応プラットフォームです。

---

## 2. ディレクトリ構造ルール

* **TeX ソース (`src/`)**: 「大問フォルダ一体型」構成を遵守。
  - 例: `src/sample_titech/kouki/1990/0/solution.tex`（※ 0番は年度全体サマリ）
  - 例: `src/sample_titech/kouki/1990/1/solution.tex`
* **Web プロジェクト (`web/`)**:
  - Content Collections: `web/src/content/solutions/`
  - TikZ 生成 SVG: `web/public/images/tikz/[uni]/[cat]/[year]/[q_num]/`

---

## 3. LaTeX ➔ Markdown 変換エンジン (`scratch/tex_to_md.py`) の決定ルール

1. **`tabular` 表の完全自動変換 (`pypandoc` 部分適用)**:
   - 表ブロック抽出時、`tabular` 内にある物理改行コード（`\n`, `\r`）をすべてスペースに全置換。
   - `pypandoc.convert_text(tab_clean, 'markdown_strict+pipe_tables+tex_math_dollars', format='latex')` を適用。
   - これにより、`dcases` や `\displaystyle` を含む数式が `$ \displaystyle ... $` のまま保持され、セル内が生改行で分割されない 100% 正確な 1 行の Markdown Pipe Table（`| ... |`）が生成される。
2. **TikZ 図表 (`figure`)**:
   - `tikzpicture` ノードを抽出し、LuaLaTeX + dvisvgm で独立 SVG を自動生成。
   - `<figure id="..."> <img src="..." alt="図 N" /> <figcaption>図 N: ...</figcaption> </figure>` の HTML ノードへ置換。
3. **相互参照 (`\cref` / `\ref`)**:
   - 図表参照: `[図N](#id)` のアンカーリンク。
   - 数式参照: `$\eqref{id}$`（MathJax 公式対応記法）。
4. **0番サマリ (`0/solution.tex`)**:
   - `type: "summary"`、`title: "{year}年 全体サマリ"` の Frontmatter を自動設定。

---

## 4. 事前検証・目視検品プロトコル（必須手順）

変換処理や変換コードの修正を行った後は、**必ず以下の検証プロトコルを順番に実行**すること：

1. **一括変換の実行**:
   ```bash
   python3 scratch/tex_to_md.py
   ```
2. **Astro Web ビルドの検証**:
   ```bash
   export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build
   ```
3. **`view_file` による全要素の目視検品**:
   生成された Markdown ファイル（特に `...-0-summary.md` および複雑な数式を含む `solution.md`）を `view_file` ツールで直接開き、以下を目視チェックすること：
   - 表が崩れず `| ... |` または綺麗な HTML 表になっているか
   - `dcases` や `\displaystyle` の数式内の `$` が壊れていないか
   - 生の改行コード `\n` でセルが途中切断されていないか
4. **GitHub Actions デプロイ状態の確認**:
   - `gh run list --limit 1` および `gh run watch [RUN_ID]` でリモートデプロイの成功を確認すること。
