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
  * LaTeXの独自マクロ（`\bm`, `\R` など）を、MathJax/KaTeXが認識できる標準的な数式表記に事前に置換する。
  * Astro用のフロントマター（タイトル、年度、大学名など）をMarkdownの先頭に自動挿入する。
  * **TikZ環境の自動画像化 (SVG)**:
    1. LaTeXソース内から `\begin{tikzpicture}` 〜 `\end{tikzpicture}` を正規表現で抽出。
    2. 抽出したコードを `standalone` クラスを用いた一時的なTeXファイルにラップしてコンパイル。
    3. `pdftocairo -svg` を用いて、PDFから拡大しても画質が落ちない **SVG形式の画像** に変換。
    4. 生成したSVGを `web/public/images/tikz/[大学]/[区分]/[年度]/[大問]/` 以下の階層ディレクトリに配置。
    5. Markdown内では、元のTikZブロックを `\includegraphics{/Math-Solutions/images/tikz/[大学]/[区分]/[年度]/[大問]/fig_[番号].svg}` に置換してPandocに渡し、HTMLへ自動変換する。

---

## 4. ビルド & デプロイ パイプライン (CI/CD)

GitHub Actionsを用いて自動ビルドを構成します。

### 4.1 deploy-pages.yml (GitHub Pagesデプロイ)
1. **トリガー**: `src/` 以下の更新が `main` ブランチにプッシュされた時。
2. **ステップ**:
   * TeX Liveおよび `poppler-utils` (`pdftocairo`) のセットアップ。
   * Pythonスクリプトによる LaTeX ➔ Markdown (Frontmatter付き & TikZのSVG画像化) への一括変換。
   * 生成されたMarkdownファイルを `web/src/content/solutions/` に格納。
   * Node.js環境をセットアップし、Astroビルド (`npm run build`) を実行。
   * `github-pages` アクションを使用してビルド結果 (`dist/` フォルダ) をデプロイ。

### 4.2 build-pdf.yml (PDF書籍ビルド & リリース)
1. **トリガー**: リリースタグ（例: `v1.0.0`）がプッシュされた時。
2. **ステップ**:
   * TeX Live環境を立ち上げ、区分直下に配置された一括マスターTeX（例: `src/[大学]/[区分]/main.tex`）をLuaLaTeXでコンパイル。
   * **全年度・全大問の順序と改ページの保証**:
     * マスターファイル `main.tex` が、配下の全年度・全大問の `problem.tex` / `solution.tex` を年度順・大問順に `\input` します。
     * 年度の切り替わりには `\part*{XXXX年}` の見出しページを挿入し、各大問の読み込み後には確実に `\clearpage` を実行。これにより、PDF全体で順序の混在がなく、各大問が美しい改ページ付きで一括ビルドされます。
   * 生成されたPDFファイルを GitHub Release に自動アタッチし、ユーザーが直接ダウンロードできるようにする。

---

## 5. テスト・検証用ダミーデータと既存データの保護 (Data Safety & Testing)

本プロジェクトの開発および検証段階では、既存のLaTeX原稿や手書きPDFファイルの破損・誤削除を防ぐため、**実際のデータを直接操作・マイグレーションすることはしません**。

### 5.1 既存データの保護
* 手書き解答PDFファイル群の整理・移動は、システムによる自動操作を行わず、**すべてユーザーが手動で実施**します。
* 既存のTeXファイル（`titech_kouki` 内のソースなど）も、本システムのスクリプトから直接書き換えや移動を行わず、安全に温存します。

### 5.2 検証用ダミー（サンプル）データの作成
本システムの開発、LaTeX ➔ Markdown変換テスト、Astroビルドの検証には、以下のテスト用のダミーフォルダとダミーTeXファイルを新規作成して使用します。

* **ダミー問題ファイル**: `src/sample_todai/zenki/1990/1/problem.tex`
* **ダミー解答ファイル**: `src/sample_todai/zenki/1990/1/solution.tex`

これ以降の変換スクリプト（`scratch/tex_to_md.py`）やAstroプロジェクト、GitHub ActionsによるCI/CDの検証は、この `sample_todai` ディレクトリ以下のデータに対して実行し、本番環境への影響をゼロにします。

---

## 6. 将来のKindle（固定レイアウト）販売プロセス

1. **原稿の仕上げ**: `src/book_template.tex` にて、全ての年度と大学の解答を章立てしてインクルード。
2. **PDFビルド**: LuaLaTeXにより、KDP（Kindle Direct Publishing）の推奨サイズ（例: A5判、B5判など）で美しいインデックスと目次付き of 単一PDFを出力。
3. **KDP登録**:
   * KDP管理画面にて「固定レイアウト形式の電子書籍」を選択し、PDFをアップロード。
   * 表紙画像（A5/B5比率）をセットし、プレビューで数式の崩れがないか最終確認。
   * 販売開始。
