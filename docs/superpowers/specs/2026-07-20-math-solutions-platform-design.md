# 設計仕様書: 東大・東工大・京大 数学過去問解答プラットフォーム

本ドキュメントは、散在している数学過去問解答（手書きPDFおよびLaTeXソース）を統合・整理し、Web公開（GitHub Pages）および電子書籍化（Kindle/PDF）を自動化するためのプラットフォーム設計仕様書です。

---

## 1. システム概要 & 目標

* **本尊の一元管理**: 原稿データをLaTeXファーストで作成し、大問ごとのクリーンな構造で管理する。
* **マルチアウトプット**: 
  1. **Web公開**: GitHub Pages上にAstroを用いて構築した、爆速で美しいレスポンシブな解答サイト。
  2. **PDF配信**: 印刷・ダウンロード用の高品質な年度別 / 複数年度まとめたPDF。
  3. **Kindle書籍化**: PDF固定レイアウト形式でのKindleダイレクト・パブリッシング（KDP）向けデータ。
* **CI/CDによる自動化**: GitHub Actionsを活用し、原稿のPushをトリガーに「PDFビルド」「Markdown変換」「GitHub Pagesデプロイ」を完全自動化する。

---

## 2. アーキテクチャとディレクトリ構造

### 2.1 データの流れ (Data Flow)

```mermaid
graph TD
    %% LaTeXソース (本尊)
    Subj[src/大学/区分/年度/大問/] -->|problem.tex / solution.tex| TexSrc[LaTeXソース]

    %% 書籍ビルドライン
    TexSrc -->|master main.tex に input| PDFBuild[latexmk / LuaLaTeX]
    PDFBuild -->|CIで自動生成| OutPDF[配布・電子書籍用 PDF]

    %% Webビルドライン
    TexSrc -->|GitHub Actions CI| Pandoc[Pandoc]
    Pandoc -->|自動Markdown変換| AstroMD[web/src/content/ に配置]
    AstroMD -->|Astro ビルド (KaTeX埋め込み)| AstroBuild[Astro SSG]
    AstroBuild -->|デプロイ| GHPages[GitHub Pages (HTML/CSS)]
```

### 2.2 ディレクトリ構造 (Directory Layout)

大問フォルダ一体型をベースとし、WebプロジェクトとLaTeXソースを完全に分離します。

```
Math-Solutions/
├── .github/
│   └── workflows/
│       ├── build-pdf.yml       # PDF書籍のビルド & リリース Actions
│       └── deploy-pages.yml    # Astroサイトのデプロイ Actions
│
├── src/                        # LaTeXソース（執筆用のマスターデータ）
│   ├── shared/                 # 共通で使うマクロやスタイル
│   │   ├── preamble.tex        # 共通プリアンブル（パッケージ読み込み）
│   │   └── macros.tex          # 共通マクロ（ショートカットなど）
│   │
│   ├── [todai | kyodai | titech]/
│   │   └── [zenki | kouki]/
│   │       ├── 1990/
│   │       │   ├── 1/              # 大問1のフォルダ
│   │       │   │   ├── problem.tex  # 問題文
│   │       │   │   └── solution.tex # 解答
│   │       │   ├── 2/
│   │       │   │   ├── problem.tex
│   │       │   │   └── solution.tex
│   │       │   │
│   │       │   └── main.tex        # 1990年度の一括ビルド用ファイル（1〜6の大問を\inputする）
│   │       └── ...
│   │
│   └── book_template.tex       # 全年度をまとめて一冊の本にする場合のテンプレート
│
├── web/                        # AstroによるWebサイトプロジェクト
│   ├── src/
│   │   ├── content/            # CI/CDによって生成されたMarkdownが置かれる場所
│   │   │   └── solutions/      # 例: todai-zenki-1990-1.md のようにフラットに配置
│   │   ├── pages/              # 各ページのレイアウト・UI
│   │   └── layouts/            # 共通ヘッダー・フッターやGlassmorphismスタイルの適用
│   ├── package.json
│   └── astro.config.mjs
│
└── raw_handwriting_archive/    # 現在ある手書きPDF（旧データ）の保管庫
```

---

## 3. 技術スタック (Tech Stack)

### 3.1 原稿 & PDFビルド
* **言語**: LaTeX (LuaLaTeX)
  * 日本語処理が安定しており、モダンなフォント設定が容易な LuaTeX を採用。
* **ビルドツール**: `latexmk`
  * 相互参照や図表の自動コンパイル（複数回コンパイル）を処理。

### 3.2 Webフロントエンド (Astro)
* **静的サイトジェネレータ**: **Astro (v4.x+)**
  * HTMLファーストで、パフォーマンスが極めて高い。
* **CSSフレームワーク**: **TailwindCSS** または **Vanilla CSS**
  * ダークモード対応やGlassmorphismなどのプレミアムな質感の実装。
* **数式描画**: **KaTeX** (ビルド時レンダリング)
  * `remark-math` ＋ `rehype-katex` プラグインを使用し、ビルド時に数式をHTML化。数式の瞬時表示を実現。

### 3.3 変換システム (LaTeX ➔ Markdown)
* **コアコンバータ**: **Pandoc**
  * `pandoc [file].tex -t markdown --mathjax -o [file].md` のように変換。
* **前処理・後処理スクリプト (Python)**:
  * LaTeXの独自マクロ（`\bm`, `\R` など）を、MathJax/KaTeXが認識できる標準的な数式表記（`\mathbf`, `\mathbb` など）に事前に置換する。
  * Astro用のフロントマター（タイトル、年度、大学名など）をMarkdownの先頭に自動挿入する。

---

## 4. ビルド & デプロイ パイプライン (CI/CD)

GitHub Actionsを用いて自動ビルドを構成します。

### 4.1 deploy-pages.yml (GitHub Pagesデプロイ)
1. **トリガー**: `src/` 以下の更新が `main` ブランチにプッシュされた時。
2. **ステップ**:
   * Pythonスクリプトによる LaTeX ➔ Markdown (Frontmatter付き) への一括変換。
   * 生成されたMarkdownファイルを `web/src/content/solutions/` に格納。
   * Node.js環境をセットアップし、Astroビルド (`npm run build`) を実行。数式がHTMLにプリコンパイルされる。
   * `github-pages` アクションを使用してビルド結果 (`dist/` フォルダ) をデプロイ。

### 4.2 build-pdf.yml (PDF書籍ビルド & リリース)
1. **トリガー**: リリースタグ（例: `v1.0.0`）がプッシュされた時。
2. **ステップ**:
   * TeX Live環境を立ち上げ、`src/` 以下の各 `main.tex` または `book_template.tex` をLuaLaTeXでコンパイル。
   * 生成されたPDFファイルを GitHub Release に自動アタッチし、ユーザーが直接ダウンロードできるようにする。

---

## 5. 移行計画 (Migration Plan)

既存の散らばったデータを新構造へ移行する手順です。

### 5.1 手書きPDFのクリーンアップ・移行
* `homepage_solutions/京都前期_整理完了/` などのファイルを、本リポジトリの `raw_handwriting_archive/` に集約する。
* ファイルサイズが異なり、重複している可能性のあるもの（東工大・京大後期）は、画質と書き込み内容を検証したうえで、優れたバージョン1ファイルのみを残し、他を削除する。

### 5.2 TeXソースのマイグレーション
現行のバラバラな構造を、Pythonによる自動配置スクリプトを用いて一括整理します。

1. **`titech_kouki` (後期試験) の移行**:
   * `problems/[年度]/[大問]/problem.tex` と `solutions/[年度]/[大問]/solutions.tex` を読み込み、`src/[大学]/[区分]/[年度]/[大問]/` の中にコピーして同居させる。
2. **`homepage_solutions` (前期試験) の移行**:
   * `todai/todai-zenki/1961/61-1/ut-61-1.tex` のようなファイルを解析し、`src/todai/zenki/1961/1/problem.tex`（または `solution.tex`）として整理・リネームして配置。

---

## 6. 将来のKindle（固定レイアウト）販売プロセス

1. **原稿の仕上げ**: `src/book_template.tex` にて、全ての年度と大学の解答を章立てしてインクルード。
2. **PDFビルド**: LuaLaTeXにより、KDP（Kindle Direct Publishing）の推奨サイズ（例: A5判、B5判など）で美しいインデックスと目次付き of 単一PDFを出力。
3. **KDP登録**:
   * KDP管理画面にて「固定レイアウト形式の電子書籍」を選択し、PDFをアップロード。
   * 表紙画像（A5/B5比率）をセットし、プレビューで数式の崩れがないか最終確認。
   * 販売開始。
