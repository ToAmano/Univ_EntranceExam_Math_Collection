# AGENT.md — Math-Solutions 開発・変換引き継ぎガイドライン

## 1. プロジェクト概要

本リポジトリ（GitHub: `ToAmano/Univ_EntranceExam_Math_Collection`）は、東大・京大・東工大の理系数学の過去問・解答を TeX ソースで管理し、
1. **Web ポータル（Astro）** への自動 Markdown 変換
2. **統合マスター PDF**（大学・区分ごとの解答集）の LuaLaTeX ビルド

を行うマルチ大学対応プラットフォーム。手書き解答 PDF の OCR/文字起こしによる TeX 化、および図版の TikZ 化を GitHub Issues 駆動で継続的に進めている。

* Web 公開 URL: `https://toamano.github.io/Univ_EntranceExam_Math_Collection/`（`web/astro.config.mjs` の `site`/`base` を参照）
* ローカルディレクトリ名は `Math-Solutions` だが、GitHub リポジトリ名・公開パスは `Univ_EntranceExam_Math_Collection`。パスや URL を扱うときはこの不一致に注意する。

---

## 2. ディレクトリ構造

```
src/{university}/{category}/
    main.tex          # その大学/区分の統合マスター PDF 用エントリポイント（generate_main_tex.py が生成）
    {year}/{q_num}/
        problem.tex     # 問題文
        solution.tex     # 解答（{q_num}=0 のときは年度サマリ）
web/
  src/content/solutions/   # tex_to_md.py が生成する Markdown（Astro Content Collections）
  src/content/config.ts    # solutions コレクションの zod スキーマ
  src/pages/                # ルーティング（category/[university] 等）
  public/images/tikz/{university}/{category}/{year}/{q_num}/  # TikZ→SVG 生成物
scratch/                   # 変換・移行・データ整備用の使い捨て/半恒久 Python スクリプト群
docs/status/                # 大学・区分ごとの進捗ダッシュボード（自動生成）
docs/superpowers/           # sdd（spec-driven development）の spec / plan 文書
tests/scratch/               # scratch 配下スクリプトの unit test
京大_後期/, 東工大_後期/       # 手書き解答の元 PDF（スキャン、区分ごとに直下配置）
.github/workflows/          # build-pdf.yml（タグ push で PDF リリース）, deploy-pages.yml（main push で Pages デプロイ）
```

* `university`: `titech` / `utokyo` / `ukyoto`
* `category`: `kouki`（後期）/ `zenki`（前期）
* `q_num`: 大問番号。`0` は年度全体サマリ（`type: "summary"` の frontmatter が自動付与される）
* 年度フォルダ直下に `handwritten.pdf`（手書き解答スキャン）や `out/`（ビルド中間生成物）が置かれていることがある。

---

## 3. LaTeX → Markdown 変換エンジン（`scratch/tex_to_md.py`）

### 実行方法
```bash
# 全件変換
python3 scratch/tex_to_md.py

# 単一ファイルのみ変換（ピンポイント）
python3 scratch/tex_to_md.py src/titech/zenki/2000/1/problem.tex
```
`src/{univ}/{cat}/{year}/{q}/{problem|solution}.tex` を再帰的に走査し、frontmatter 付き Markdown を `web/src/content/solutions/{univ}-{cat}-{year}-{q}-{type}.md` に出力する。

### 主な変換ルール
1. **`tabular` 表**: `\multirow`/`\multicolumn` を展開後、`pypandoc.convert_text(..., 'gfm', format='latex')` で Pipe Table に変換し、`<figure class="table-wrapper">` でラップする。
2. **`figure`／`tikzpicture`**: `tikzpicture` を抽出し、LuaLaTeX（フォールバック: pdflatex）でスタンドアロン PDF を生成 → `pdftocairo`（最優先）/ `pdf2svg` / `dvisvgm` の順で SVG 化し、`web/public/images/tikz/{univ}/{cat}/{year}/{q}/fig_N.svg` に配置。`<figure><img/><figcaption/></figure>` の HTML ノードに置換する。
3. **相互参照**: `\cref`/`\ref`/`\eqref` はラベル名（`fig:`/`tab:`/`eq:` プレフィックス）に応じて `[図N](#id)` / `[表N](#id)` / `[(式N)](#id)` のアンカーリンクに変換。
4. **数式環境**: `align`/`align*`/`gather*`/`eqnarray*`、`\[...\]`、`numcases`/`subnumcases` はすべて `$$ ... $$` + 標準 LaTeX 環境（`align*`/`cases` 等）に正規化。MathJax（`rehype-mathjax`）でレンダリングするため、`enumerate`/`itemize`/`description` は Markdown の番号付きリストに変換する一方、数式構造は崩さずそのまま残す。
5. **0番サマリ（`0/solution.tex`）**: `type: "summary"`, `title: "{year}年 全体サマリ"` の frontmatter を自動設定。
6. TexSoup でのパースに失敗した場合は正規表現ベースのフォールバック処理（figure/tikz 抽出・align 変換）に切り替わる。

### frontmatter スキーマ（`web/src/content/config.ts` と一致させること）
`university`, `category`, `year`, `question`, `type`（`problem`/`solution`/`summary`）, `title`

---

## 4. 事前検証・目視検品プロトコル（必須手順）

変換処理や変換コードを修正した後は、**必ず以下を順番に実行**すること：

1. **一括変換**:
   ```bash
   python3 scratch/tex_to_md.py
   ```
2. **Astro Web ビルド検証**:
   ```bash
   cd web && npm install && npm run build
   ```
3. **Python 側ユニットテスト**（`scratch/tex_to_md.py` 内のマクロ前処理などを変更した場合）:
   ```bash
   python3 -m unittest discover tests
   ```
4. **目視検品**: 生成された Markdown（特に `*-0-summary.md` と数式・表・TikZ 図を含む `solution.md`）を直接開き、以下を確認する。
   - 表が `| ... |` の Pipe Table または綺麗な `<figure class="table-wrapper">` になっているか
   - `dcases`/`\displaystyle` を含む数式の `$`/`$$` が壊れていないか
   - 生の改行 `\n` でセルや数式が途中切断されていないか
   - TikZ 由来の SVG が `web/public/images/tikz/...` に生成され、`<img>` が正しいパスを指しているか
5. **GitHub Actions デプロイ確認**（push 後）:
   ```bash
   gh run list --limit 1
   gh run watch [RUN_ID]
   ```

---

## 5. 統合マスター PDF ビルド（大学/区分ごとに 1 冊）

大学・区分（`titech/kouki`, `titech/zenki`, `utokyo/kouki`, `utokyo/zenki`, `ukyoto/kouki`, `ukyoto/zenki` の 6 組）ごとに
`src/{univ}/{cat}/main.tex` が 1 つ存在し、`latexmk -lualatex` でその区分の全年度・全問題を 1 冊の PDF にまとめてビルドできる
（例: `utokyo/zenki/main.tex` → 東大前期の全問題・全解答を収録した PDF）。

### `main.tex` の生成（`scratch/generate_main_tex.py`）
```bash
# 6 区分すべてを再生成
python3 scratch/generate_main_tex.py

# 特定の区分だけ再生成
python3 scratch/generate_main_tex.py utokyo/zenki
```
`main.tex` は **手書きで編集せず、常にこのスクリプトで再生成する**。年度・問題番号ディレクトリを走査し、各 `problem.tex`/`solution.tex` の冒頭を見て `\documentclass[...]{subfiles}` を実際に使っているか（= 内容が独立して埋め込み可能な形式になっているか）を自動判定し、以下のルールで `\subfile{}` する対象を選ぶ：

* **kouki 系**（`problem.tex` が中身のみの断片で、`solution.tex` 側が `\begin{oframed}\input{problem.tex}\end{oframed}` で問題文を埋め込む構成）: `solution.tex` が subfiles 形式なら、それだけを `\subfile` する（問題文は自動的について来る）。
* **zenki 系**（`problem.tex` 自体が独立した subfiles 文書）: `problem.tex` を `\subfile` し、`solution.tex` が subfiles 形式で存在すれば続けて `\subfile` する。
* どちらの条件も満たさない（＝手書き解答からの移行がまだ済んでいない、旧 `jarticle` 形式のまま等）の場合はスキップし、標準出力に一覧を表示する。

これにより、**手書き解答の TeX 化や TikZ 化が進むたびに `generate_main_tex.py` を再実行するだけで、その分だけ自動的に master PDF に反映される**。

### コンパイル方法
```bash
cd src/utokyo/zenki
latexmk -lualatex -interaction=nonstopmode main.tex
# → main.pdf が生成される
```

### プリアンブルの設計上の注意（`scratch/generate_main_tex.py` の `PREAMBLE` 定数）
* `\documentclass{ltjsarticle}` + `luatexja`/`luatexja-preset`（`haranoaji` フォント、Ubuntu CI の `texlive-lang-japanese` にも同梱）を使用。
* `array` パッケージが**必須**: `subfiles` の `\subfile` は `\begingroup...\endgroup` で子ファイルを読み込むため、グルーピングの深さが標準と 1 段ずれる。この状態で `\begin{center}` を 2 回ネストしてから `p{...}` 列を含む `tabular` を使うと `array` 未読み込みでは `|c|\@nil` という謎の `Undefined control sequence` になる（本プロジェクトで実際に踏んだ地雷。多くの `0/solution.tex` サマリファイルがこのパターンを使っている）。
* `fancybox`（`\shadowbox`）を使う。`ascmac` は `fancybox` と併用すると `\shadowbox` 内の `tabular` パースが壊れるため**使わないこと**。
* `tdplotsetmaincoords{70}{110}` をプリアンブルでデフォルト呼び出ししている。一部の `tikzpicture` が `tdplot_main_coords` スタイルを使うのに `\tdplotsetmaincoords` を呼び忘れているため、そのフォールバック。
* `\roundedArrowDR` 等、増減表の矢印記号を指すが定義されていないソースがあるため `\providecommand` でセーフガードしている。
* ソース中の生の `\hspace{1zw}` のような「バックスラッシュなしの `zw`/`zh` 単位」は LuaTeX-ja では無効（pTeX 由来の記法）。`scratch/generate_main_tex.py` 実行前に一度リポジトリ全体で `\1\zw`/`\1\zh` に機械的に修正済み（`(?<!\\)([0-9.]+)(zw|zh)\b` → `\1\\\2`）。今後インポートする TeX にも同じ問題が出うるので注意。
* kouki 系 `solution.tex` 内の `\input{../../../problems/{year}/{q}/problem.tex}` という壊れた相対パス（過去のディレクトリ構成の残骸）は `\input{problem.tex}`（同じディレクトリの兄弟ファイル）に一括修正済み。

### 既知の軽微な警告（無視してよい）
* `Missing character ... in font nullfont!`: `pgfplots`/TikZ が内部の寸法計算パスで発生させる無害な警告。実際のページを目視確認済みで、文字の欠落やレイアウト崩れは発生しない。
* 一部ファイルで `\ref`/`\eqref` が解決できない（ラベル名の typo など、内容側の軽微な既存バグ）。

---

## 6. CI/CD ワークフロー

* **`deploy-pages.yml`**（`main` push / 手動実行）: `tex_to_md.py` 実行 → `web` で `npm ci && npm run build` → GitHub Pages にデプロイ。
* **`build-pdf.yml`**（`v*` タグ push / 手動実行）: 大学・区分の 6 通りを matrix ビルドし、各ジョブで `generate_main_tex.py` → `latexmk -lualatex` → `{univ}_{cat}.pdf`（例: `utokyo_zenki.pdf`）にリネームして artifact化。最後に release ジョブが全 artifact を集約して GitHub Release に添付する。

---

## 7. データ整備ワークフロー（`scratch/` の主要スクリプト）

進捗状況は GitHub Issues と `docs/status/*.md`（`generate_status_markdowns.py` で自動生成、`docs/status/README.md` がダッシュボード）で管理している。

* **手書き解答の文字起こし**: `import_handwritten_*.py`（大学・区分ごと）→ `transcribe_handwritten.py`（PDF を PNG 化し `scratch/handwritten_tasks.json` でタスク管理しつつ TeX 化）
* **図版の TikZ 化**: `scan_figure_tasks.py`（要 TikZ 化の図を検出）→ `create_all_tikz_issues.py`（`[TikZ化]` prefix で GitHub Issue を一括作成）→ `collect_tikz_tasks.py`（`gh issue list` から Open な `[TikZ化]` Issue を収集し `scratch/tikz_tasks.json` に保存）。直近のコミット履歴はこの Issue 番号を `(fixes #NNN)` として参照する運用になっている。
* **既存 TeX の取り込み**: `import_existing_tex.py`, `import_zenki_tex.py`, `copy_titech.py`
* **進捗集計**: `analyze_missing_solutions.py`, `check_incomplete_solutions.py`, `filter_real_incomplete_tasks.py`, `generate_status_markdowns.py`

---

## 8. 手書き解答の文字起こしワークフロー（詳細手順）

`{univ}/{cat}/{year}/handwritten.pdf`（手書き解答のスキャン）を年度ごとに TeX 化する作業の実践手順。年度は**古い順に1年ずつ**処理し、各年度で以下のサイクルを回す。

### 8.1 年度ごとの基本サイクル

1. **構成確認**: `pdfinfo {year}/handwritten.pdf` でページ数を確認する。表紙1ページ＋大問ごとに1ページが基本だが、**大問の数は年度によって4〜6問程度で変動する**。`scratch/tmp_download/08_titech/{year}/{year}_{q}.tex` の実在数が、その年度の実際の大問数の手がかりになる（`{year}_6.tex` があれば第6問が存在する、等）。
2. **全体レンダリング**: `pdftoppm -png -r 200 {year}/handwritten.pdf {tmpdir}/hw{year}` 程度の解像度でまず全ページを概観する。
3. **`problem.tex` との突き合わせ**: 各大問の `problem.tex`（既存）を読み、手書き解答がどの設問に対応するか確認してから読み進める。
4. **既存 `handwritten_tex.tex` への書き起こし**: 大問ごとに `\section*{第N問}` 見出しで区切り、`\begin{proof}[解]...\end{proof}` で解答を囲む。ファイル冒頭は `\documentclass[../../../../main.tex]{subfiles}` + `\begin{document}`、末尾は `\end{document}`。図は TikZ で再現する（8.3参照）。
5. **分割**: `python3 scratch/split_handwritten_tex.py {univ}` で `{year}/{q}/solution.tex` に自動分割する。**既存の `solution.tex` は上書きされない**（既存優先でスキップされる。過去に別形式で解答が存在する年度・設問はそのまま残る）。
6. **`problem.tex` の欠落補完**: `scratch/batch_import_all_problems.py` は `range(1,6)` のバグにより第6問を取り込まないため、第6問が存在する年度は `scratch/tmp_download/08_titech/{year}/{year}_6.tex` 等から手動インポートが必要になることがある。
7. **単体コンパイル確認**: プリアンブル一式（`scratch/generate_main_tex.py` の `PREAMBLE` と同一内容）＋対象年度の大問だけを `\subfile` するテスト用 `test{year}.tex` を作り、`latexmk -lualatex -interaction=nonstopmode -halt-on-error test{year}.tex` でエラーが出ないことを確認する。TikZ 図がある場合は `pdftoppm` で PNG 化し、元のスキャンと見比べて図の忠実性も目視確認する。
8. **テスト成果物の削除**: `test{year}.{pdf,aux,log,fls,fdb_latexmk,synctex.gz,toc,out,tex}` を必ず削除してから次の年度に進む。
9. **`main.tex` の再生成**: 複数年度まとめて処理したあとは `python3 scratch/generate_main_tex.py {univ}/{cat}` を実行し、可能なら全体ビルド（第5章参照）でも通しでコンパイル確認する。

### 8.2 判読困難な箇所への対処（クロップ・拡大）

手書き文字が薄い・小さい・類似記号で紛らわしい場合は、以下の手順で段階的に解像度を上げる。

1. 該当ページだけを高解像度（300dpi、必要なら400〜600dpi）で再レンダリングする: `pdftoppm -png -r 300 -f {page} -l {page} {year}/handwritten.pdf {tmpdir}/hw{year}_hires`
2. Python（PIL）の `Image.crop((left,upper,right,lower))` で該当領域を絞り込み、必要に応じて `resize()` で数倍に拡大してから `Read` ツールで確認する。
3. それでも数字・記号が曖昧な場合（例: 「8/3」か「6/3」か）は、**独立に代数計算をして値を逆算し**、どちらの読み取りが式全体と整合するかで判定する。単なる目視の勘に頼らないこと。
4. 手書きの最終結果（答え）は、可能な限り自力で計算し直して照合する。計算が一致しない場合は該当箇所を再度クロップして読み直し、それでも不明な場合は最も妥当な解釈を採用しつつ、致命的な不整合があれば作業ログで明示する。

### 8.3 空欄解答・問題数の変動について

* **原稿自体が空欄のページ**は、無理に埋めずに `% (原稿において第N問の解答は空欄)` という1行コメントのみを残し、本文なしで `\newpage` を置く。これは文字起こし漏れではなく、**当時から解答が存在しなかったことを示す正当な状態**であり、`solution.tex` は生成されるがコメントのみで内容は空になる。
* 特に**行列（一次変換）の問題は、出題当時の教育課程の都合で解かれていないことがある**。これも同様に空欄が正解であり、無理に解答を創作してはならない。
* **大問の数は年度によって4問・5問・6問などと変動する**。存在しない設問番号のディレクトリを作る必要はない。

### 8.4 図（TikZ）の再現について

* 元の手書き図は TikZ で簡略化して再現する。厳密な形状の一致より、問題の理解を妨げない程度の忠実さを優先する。
* 曲線や領域は `\draw[domain=...] plot` で近似し、塗りつぶし領域は `\fill[gray!15] plot ... -- cycle;` のようなパスで表現する。
* 近接する2点のラベルは `node[above left]` / `node[below]` 等でアンカー位置を調整し、重ならないようにする（実際に本作業で座標が近い2点のラベルが重なる不具合が発生したため、要注意）。

---

## 9. 開発環境の前提

* Node.js v18.14.1 以上（Astro v4）
* Python 3.x（`pypandoc`, `TexSoup` が必須）
* Pandoc, poppler-utils（`pdftocairo`）, TeX Live（LuaLaTeX / pdflatex, 日本語対応。統合マスター PDF ビルドには `texlive-lang-japanese texlive-luatex texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-science texlive-fonts-extra` 相当が必要）
* `gh` CLI（Issue 駆動の進捗管理・デプロイ確認に使用、認証済みであること）

---

## 10. ライセンス

デュアルライセンス（詳細は `LICENSE`）。
* コンテンツ（解答解説・TeX ソース・TikZ 画像）: CC BY-NC-SA 4.0
* プログラムコード（`web/`, `scratch/`, 設定ファイル）: MIT License
