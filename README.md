# 東大・京大・東工大 数学過去問解答ライブラリ

東大、京大、東工大の理系数学の過去問解答（手書きPDFおよびTeXによる解答）を公開・管理するリポジトリです．高校生時代に作成した手書き解答をベースにTeXに綺麗化しています．

## 公開サイト (GitHub Pages)
最新の解答は以下のサイトでご覧いただけます．
**[過去問解答サイト]([https://amano.github.io/Math-Solutions/](https://toamano.github.io/Univ_EntranceExam_Math_Collection/)**

## リポジトリ構成

* `src/`: LaTeXによる解答ソース（マスターデータ）．
* `web/`: AstroによるWebサイトプロジェクト．

## ローカルでのビルド・開発手順

### 前提条件 (Prerequisites)
* **Node.js**: `v18.14.1` 以上 (Astro v4 の動作環境)
* **Python**: `3.x`
* **LaTeX / CLIツール**: Pandoc, `poppler-utils` (`pdftocairo`), TeX Live (TikZのSVG変換およびPDFビルドに使用)

---

### 1. LaTeX ➔ Markdown / TikZ-SVG の一括変換
`src/` 配下の全TeXファイルからMarkdownおよびTikZのSVG画像を出力します。

```bash
# リポジトリルートにて実行
python3 scratch/tex_to_md.py
```

※生成された Markdown ファイルは `web/src/content/solutions/` に、TikZ SVG 画像は `web/public/images/tikz/` 以下の階層ディレクトリに自動配置されます。

---

### 2. Webサイトのローカル開発サーバー起動 (`npm run dev`)

```bash
cd web
npm install
npm run dev
```

ブラウザで `http://localhost:4321/` を開くと、ポータル画面（`index.astro`）および数式・図形付きの解答ページを確認できます。

---

### 3. Webサイトのプロダクションビルド (`npm run build`)
GitHub Pages デプロイ用の静的 HTML bundle (`dist/`) を生成・動作検証します。

```bash
cd web
npm run build
npm run preview   # ビルド成果物 (dist/) のローカルプレビュー
```

---

### 4. 過去問解答集 PDF マスターの一括ビルド (LuaLaTeX)
大学・区分ごとの統合マスターTeXから、1冊の解答集PDFをコンパイルします。

```bash
# 東工大後期の過去問解答集PDFを一括ビルド
cd src/sample_titech/kouki
latexmk -lualatex main.tex

# 東大前期の過去問解答集PDFを一括ビルド
cd src/sample_todai/zenki
latexmk -lualatex main.tex
```

---

## ライセンス (License)

本リポジトリは、コンテンツとプログラムコードでデュアルライセンスを採用しています。詳細な規定は [LICENSE](LICENSE) をご参照ください。

* **解答解説文章・TeXソース・TikZ画像 (コンテンツ)**: 
  **[CC BY-NC-SA 4.0 (Creative Commons 表示-非営利-継承 4.0 国際)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)**
  * クレジット表示を行い、非営利目的に限って自由にご利用・学習・共有・改変いただけます。
* **プログラムコード (`web/`, `scratch/`, 設定ファイル)**: 
  **[MIT License](LICENSE)**
  * 商用・非営利問わず自由に利用・改変いただけます。
