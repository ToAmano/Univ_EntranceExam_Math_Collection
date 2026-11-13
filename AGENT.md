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
    {year}/
        handwritten.pdf # 年度別の手書き解答 PDF
        {q_num}/
            problem.tex  # 問題文
            solution.tex # 解答（{q_num}=0 のときは年度サマリ）
web/
  src/content/solutions/   # tex_to_md.py が生成する Markdown（Astro Content Collections）
  src/content/config.ts    # solutions コレクションの zod スキーマ
  src/pages/                # ルーティング（category/[university] 等）
  public/images/tikz/{university}/{category}/{year}/{q_num}/  # TikZ→SVG 生成物
scratch/                   # 変換・移行・データ整備用の使い捨て/半恒久 Python スクリプト群
docs/status/                # 大学・区分ごとの進捗ダッシュボード（自動生成）
docs/superpowers/           # sdd（spec-driven development）の spec / plan 文書
tests/scratch/               # scratch 配下スクリプトの unit test
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

**通常の `solution.tex`/`problem.tex` の内容修正（数式・図・文章の訂正）では、以下の軽量フローで十分であり、全件変換・Astro フルビルドは不要**：
1. `python3 scratch/lint_latex_style.py <対象ファイル>` で対象ファイルのみ lint
2. `cd <対象ディレクトリ> && latexmk -lualatex -interaction=nonstopmode solution.tex` で単体コンパイル確認（図を直した場合は `pdftoppm` で PNG 化して目視確認。テスト成果物は [local/transcription.md の L6](skills/math-solution-tex/local/transcription.md) の通り残さない）
3. 必要なら `python3 scratch/tex_to_md.py <対象ファイルのパス>`（ピンポイントモード）で markdown 側も確認
   * Web 版で TeX がそのまま表示されないかは `python3 scratch/check_web_leaks.py <対象ファイル>` で確かめられる（TikZ はコンパイルしないので数秒。引数なしなら全件で約30秒）。
4. 全件変換・Astro フルビルドは「コミット直前の最終確認」または下記の「変換処理や変換コードを修正した後」にのみ行う

変換処理や変換コードそのもの（`scratch/tex_to_md.py` 等）を修正した後は、**必ず以下を順番に実行**すること：

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
* **`lint-tex.yml`**（`src/**/*.tex` を含む push / PR）: `scratch/lint_latex_style.py` で 8.3.6 節のルール（機械的に判定可能なもののみ）を **差分に入った `solution.tex` のみ** に対してチェックする。`problem.tex`（原題の問題文）はCIの対象外——著者が書く解答文とは性質が違い、`\caption` 必須などの一部ルールがそもそも馴染まないため。TeX Live 不要の軽量ジョブ。既存コーパスには本ルール導入以前からの違反が大量にあるため（2026年時点で約6800件）、リポジトリ全体を対象にはせず、変更・新規追加された `solution.tex` のみを厳格化する「ratchet」方式を採用している。ローカルでの単体実行は `python3 scratch/lint_latex_style.py [対象ファイル...]`（引数なしならリポジトリ全体を `problem.tex` も含めてスキャンし集計のみ表示。`problem.tex` も個別に指定すれば手動でチェック可能）。
  * **`% lint-skip: 理由`** をファイル中のどこか（通常は1行目）に書いておくと、そのファイルの lint チェックを丸ごとスキップできる（`--no-verify` でのコミットを都度要求する代わりの避難ハッチ）。理由コメントは省略不可——空だとマーカーとして認識されない。旧jarticle形式のまま未移行（Issue #593）のように「直す予定はあるが対応は別作業」と分かっているファイルに使う想定で、個別のバグ修正時に無関係な既存違反でブロックされるのを避けられる。乱用すると ratchet の意味が薄れるため、本当に別issueで追跡済みの既知の問題にのみ使うこと。
* **`lint-tex-full.yml`**（毎週月曜 00:00 UTC の `schedule` / 手動実行）: `scratch/lint_full_report.py` でリポジトリ全体の `solution.tex`（`lint-tex.yml` と同じスコープ）を走査し、ルール別・書籍別の内訳を Markdown レポートとして生成、`LaTeX Lint Backlog Report` という固定タイトルの Issue を検索して見つかれば本文を更新、無ければ新規作成する（PR ごとに Issue を乱発しない）。違反があってもジョブ自体は失敗しない非ブロッキングの可視化用ワークフローで、`lint-tex.yml`（差分のみを強制）とは役割が異なる。
ローカルの独自 lint は `--fix` で句読点（`。`/`、` と和文に接する半角の `,`/`.` → `．`/`，`）、分数の `\frac` / `\dfrac`（添字・TikZ 内では `\frac`、それ以外では `\dfrac`）、ディスプレイ数式の `\[ ... \]` → `align` 環境、ベクトルの `\vec` / `\overrightarrow` 表記（添字・プライムの外出しを含む）、`tikzpicture` 内の点描画 `circle (...pt)` → `\node[circle, ...]`、`\end{align}` 直前の余分な改行 `\\`（空の式番号の原因。間に `\label` を挟む場合は番号の意味が変わるため手動修正）を機械修正できる。コメント、URL・参照先・ファイルパス、verbatim 系のコード、マクロ定義は自動修正から除外し、`lint-skip` も尊重する。裸引数、図表構造等は修正しない。既存 lint の検査範囲は変わらないため、保護した箇所の指摘が残ることもある。

```bash
# 差分だけ表示（変更候補または lint エラーがあれば終了コード1）
python3 scratch/lint_latex_style.py --diff src/utokyo/zenki/2000/1/solution.tex
# 修正してから通常の lint（残るエラーがあれば終了コード1）
python3 scratch/lint_latex_style.py --fix src/utokyo/zenki/2000/1/solution.tex
```

`--fix` / `--diff` は対象ファイルの明示指定が必須。一括書き換えを既定動作にはしない。pre-commit では対象の `solution.tex` に `--fix` を実行してから `tex-fmt` を実行する。自動修正された場合は差分確認・`git add`・再commit が必要。CI の `lint-tex.yml` は引き続き検査のみで、原稿を書き換えない。

* **`web-leaks.yml`**（`src/**/*.tex`・`scratch/tex_to_md.py`・検査スクリプトを含む push / PR）: `scratch/check_web_leaks.py` で、Web 版の数式の外に TeX のコマンド（`\begin`・`\label` など）がそのまま表示される箇所を探す（#1489）。原稿の変更なら差分に入った `problem.tex`・`solution.tex` だけを、変換・検査スクリプトの変更なら全原稿を調べる。原稿を `tex_to_md.py` で Markdown にし（TikZ はコンパイルせず空の画像で置き換えるので TeX Live 不要）、`web/scripts/find-tex-leaks.mjs` がサイトと同じ Markdown 処理（remark-math・生 HTML）で HTML にしてから判定するので、`\%` などの Markdown のエスケープや数式の中の `>` を漏れと取り違えない。対応する Issue がある既知の漏れ（`check_web_leaks.py` の `KNOWN`）と `lint-skip` の旧形式の原稿は警告にとどめ、新しい漏れだけを失敗にする。既知の漏れを直したら `KNOWN` から外す。
* **`pre-commit.yml`**（`**/*.tex` を含む push / PR）: [pre-commit](https://pre-commit.com/) フレームワーク経由で [tex-fmt](https://github.com/WGUNDERWOOD/tex-fmt)（Rust製 LaTeX フォーマッタ）を実行する。設定は `.pre-commit-config.yaml`（対象は `solution.tex`/`problem.tex`/`handwritten_tex.tex` のみ、`generate_main_tex.py` が再生成する `main.tex` は対象外）と `tex-fmt.toml`（2 スペースインデント、`wrap = false` で自動80桁折返しは無効化——`align` 内の改行位置は `scratch/lint_latex_style.py` の長い行警告に従って人間が選ぶ方針のため）。`lint-tex.yml` と異なりリポジトリ全体を対象にした「ratchet でない」強制チェックだが、導入時（2026年9月）に全 `.tex` へ一括適用済みのため全体適用でも問題ない。ローカルでは初回に `pre-commit install` を実行しておけば、以後 `git commit` のたびに変更した `.tex` ファイルが自動整形される（整形が入るとコミットは一旦中断されるので、`git add` し直して再コミットする）。

---

## 7. データ整備ワークフロー（`scratch/` の主要スクリプト）

進捗状況は GitHub Issues と `docs/status/*.md`（`generate_status_markdowns.py` で自動生成、`docs/status/README.md` がダッシュボード）で管理している。

一問単位のIssue識別・分類ラベルは [docs/issue-labels.md](docs/issue-labels.md) を参照。まとめIssue・サイト全体のIssueは対象外。同期は `scratch/sync_issue_labels.py`（既定はdry-run）を使用し、計画を再検証してラベルの追加だけを行う。Web表示用の対応表は `--export web/src/data/issues-by-problem.json` で生成し、通常ビルド時にOpen Issueを問題文・解答へ埋め込む。Issue更新時の自動再ビルドは未導入。

* **手書き解答の文字起こし**: `import_handwritten_*.py`（大学・区分ごと）→ `transcribe_handwritten.py`（PDF を PNG 化し `scratch/handwritten_tasks.json` でタスク管理しつつ TeX 化）
* **図版の TikZ 化**: `scan_figure_tasks.py`（要 TikZ 化の図を検出）→ `create_all_tikz_issues.py`（`[TikZ化]` prefix で GitHub Issue を一括作成）→ `collect_tikz_tasks.py`（`gh issue list` から Open な `[TikZ化]` Issue を収集し `scratch/tikz_tasks.json` に保存）。直近のコミット履歴はこの Issue 番号を `(fixes #NNN)` として参照する運用になっている。
* **既存 TeX の取り込み**: `import_existing_tex.py`, `import_zenki_tex.py`, `copy_titech.py`
* **進捗集計**: `analyze_missing_solutions.py`, `check_incomplete_solutions.py`, `filter_real_incomplete_tasks.py`, `generate_status_markdowns.py`

---

## 8. 手書き解答の文字起こしワークフロー

`{univ}/{cat}/{year}/handwritten.pdf`（手書き解答のスキャン）を TeX に起こす作業の規約と手順は、スキル `math-solution-tex` に移した。文字起こしをするときは次の2つを読む。

* **規約（汎用）**：[skills/math-solution-tex/references/transcription-rules.md](skills/math-solution-tex/references/transcription-rules.md)
  * §TR1 原稿の解法・表現をそのまま起こす（別の解法に差し替えない，くだけた表現も残す，別解はすべて起こす）
  * §TR2 着手前に全ページを洗い出す（1つの大問が複数ページにまたがることがある），空欄の確認
  * §TR3 判読（高解像度での切り出し，計算による読みの検証，`% 判読：` コメント）
  * §TR4 原稿の誤りは直さず，`% 原稿ママ：` の TeX コメントで示す
  * §TR5 構成と見出し（既存の TeX 解答が原稿由来でない場合は，原稿の解法を別解として後ろに付ける）
  * §TR6 図の再現，§TR7 仕上げの確認
* **このリポジトリ固有の手順**：[skills/math-solution-tex/local/transcription.md](skills/math-solution-tex/local/transcription.md)
  * 原稿のページ構成，年度ごとの基本サイクル，一時ファイルの置き場所，`split_handwritten_tex.py` による分割，空欄の記録，単体コンパイル，ステータス更新

記法（数式環境，分数，見出し，句読点など）は下の 8.3.6 節，図は 8.4 節に従う。

### 8.3.6 LaTeX フォーマットの注意事項

記法の規約は、スキル `math-solution-tex` の次のファイルに移した（節番号 § で引ける）。

* **数式・記法（汎用）**：[skills/math-solution-tex/references/notation-rules.md](skills/math-solution-tex/references/notation-rules.md)
  * §N1 場合分け（`dcases`），§N2 組合せ（`{}_nC_k`），§N3 証明の終わり（`\qed`），§N4 句読点（「．」「，」）
  * §N5 別行立ての数式（`align`，`split`/`\notag`，最後の行の `\\`，長い行），§N6 分数・根号（`\dfrac`，添字位置と TikZ のラベルは `\frac`，引数の `{}`）
  * §N7 括弧（`\Bigl`，`\left`/`\right` の対），§N8 ベクトル（`\vec`/`\overrightarrow`），§N9 辺の長さ（`|AB|`），§N10 相互参照とラベル（`\cref`，`eq:1` 形式の連番，重複・未定義），§N11 余白・改行の命令
* **表**：[skills/math-solution-tex/references/table-rules.md](skills/math-solution-tex/references/table-rules.md)（§TB1 `table` の中に置く，caption）
* **図**：[skills/math-solution-tex/references/figure-rules.md](skills/math-solution-tex/references/figure-rules.md)（`figure` の中に置く，caption，数式中の図形アイコン，点は `\node[circle]`）
* **このリポジトリ固有**：[skills/math-solution-tex/local/notation.md](skills/math-solution-tex/local/notation.md)（解答の見出し，小問の `\paragraph`，`\documentclass[../../main.tex]{subfiles}`，問題文の読み込み，`problem.tex` の形式，年度のまとめ・凡例の例外，`% lint-skip:`）

機械的に判定できる規則は `scratch/lint_latex_style.py`（本体はスキルの `scripts/lint_tex.py` と `local/lint_local.py`）が検査する。各節の「lint」に検査の名前を書いてある。大カッコの大きさや，`enumerate` が小問のラベルか場合分けかなど，目視が必要なものは対象外。

### 8.4 図（TikZ）の再現について

* 元の手書き図は TikZ で簡略化して再現する。厳密な形状の一致より、問題の理解を妨げない程度の忠実さを優先する。
* 曲線や領域は `\draw[domain=...] plot` で近似し、塗りつぶし領域は `\fill[gray!15] plot ... -- cycle;` のようなパスで表現する。
* 近接する2点のラベルは `node[above left]` / `node[below]` 等でアンカー位置を調整し、重ならないようにする（実際に本作業で座標が近い2点のラベルが重なる不具合が発生したため、要注意）。
* **空間図形（立体・切断面など3次元の図）は通常の2次元 `tikzpicture` で無理に描かず，`tikz-3dplot`（3D TikZ）を使う**。`src/titech/zenki/1985/2/solution.tex` の記法に従うこと：`\begin{tikzpicture}` の直前に視点を `\tdplotsetmaincoords{65}{120}`（極角・方位角。手書きのスケッチに近い見え方になる角度を選ぶ）で設定し，`\begin{tikzpicture}[tdplot_main_coords, scale=1.5]` のオプションに `tdplot_main_coords` を指定する。座標は `\coordinate (A) at (x,y,z);` のように3成分で与え，`\draw[dashed, thick] ...` で隠れ線（奥の辺）を，`\draw[thick] ...` で見える辺を描き分ける。断面や領域は `\fill[red!25, opacity=0.6] (P1) -- (P2) -- (P3) -- cycle;` のように半透明で塗ると奥行きが分かりやすい。メインプリアンブル（`scratch/generate_main_tex.py` の `PREAMBLE`）側で `\tdplotsetmaincoords{70}{110}` を既定値として一度呼んでいるが（5節参照），個々の図でそれと異なる視点を使う場合は図の直前で明示的に呼び直すこと。

### 8.4.1. 基本方針・必須パッケージ

* すべての TikZ コードは `\begin{figure}[htb] ... \end{figure}` で囲み、単独でコンパイル可能な最小構成（MWE）または埋め込み用ブロックとして出力する。
* 必須ライブラリ:
* 2D: `\usetikzlibrary{calc, patterns, angles, quotes}`
* 3D: `\usepackage{tikz-3dplot}`
* 共通オプション:
* 基本設定: `\begin{tikzpicture}[scale=2.0, >=stealth, every node/.style={font=\small}]`* 縮尺は描画内容に応じて $1.2 \sim 3.2$ の範囲で視認性よく調整する。

### 8.4.2. デザインシステム（視覚スタイル規約）

#### 8.4.2.1 カラーパレット

* **主曲線・主輪郭**: `blue!85!black`（太さ: `very thick`）
* **副曲線・境界・対比線**: `red!85!black`, `teal!85!black`, `orange!90!black`（太さ: `thick` または `very thick`）
* **座標軸**: `black`（太さ: `thick`, 矢印: `->`）
* **補助線・投影線・切片ガイド**: `gray!70` または `gray!60`（線種: `dashed`）
* **漸近線・参考線**: `gray!50`（線種: `dotted`）
* **領域塗りつぶし（共通・重複領域）**:
* ハッチング: `\fill[pattern=north east lines, pattern color=blue!60, opacity=0.8]`
* 比較用別パターン: `horizontal lines`（`teal!70` や `blue!70`）
* 複数面の重なり: `opacity=0.5 ～ 0.75` の薄いベタ塗り（例: `teal!15`, `blue!15`, `orange!25`）

#### 8.4.2.2 点・ノードの表現

* **一般プロット点 / 座標上の点**（`xscale`/`yscale` で楕円に潰れないよう `circle` パスではなく `\node[circle, ...]` を使う）:
* 黒塗り小丸: `\node[circle, fill, inner sep=1.2pt] at (coord) {};`
* 色付き強調点: `\node[circle, fill=red!85!black, inner sep=1.4pt] at (coord) {};`
* **確率過程・木構造（世代木）のノード**:
* **必ず白抜きの丸**を使用: `\node[circle, draw, thick, fill=white, inner sep=2.0pt] at (coord) {};`
* 省略表現: 実線 $\rightarrow$ 中間白丸 $\rightarrow$ `\node at (...) {$\cdots$};` $\rightarrow$ 破線（`thick, dashed`） $\rightarrow$ 終端白丸
* **白丸（端点・定義域外境界）**:
* `\node[circle, fill=white, draw=blue!85!black, thick, inner sep=1.4pt] at (coord) {};`

#### 8.4.2.3 ラベル・注釈ボックス

* **グラフ上の重要注釈**:
* 白背景＋枠線付き角丸ボックスで背景と被らないように配置する。
```latex
\node[draw=blue!85!black, fill=white, rounded corners=2pt, inner sep=2.5pt, font=\footnotesize, align=center]
  at (x, y) {注釈テキスト};
```
* **引き出し線**:
* `\draw[<-, thin, blue!85!black] (target) to[bend left=15] (label_pos) node[right, font=\footnotesize] {説明};`

### 8.4.3. 分野別実装ルール

#### 8.4.3.1 2D パラメータ平面・不等式領域

* 不等式の境界が切り替わる折れ曲がり点や交点は、必ず交点座標を計算して破線で各軸へ投影する。
* 領域ハッチングの閉路は `plot` と `-- cycle` を組み合わせて確実に閉じる。
```latex
\fill[pattern=north east lines, pattern color=blue!60, opacity=0.8]
  plot[domain=x1:x2, samples=50] (\x, {f(\x)})
  -- plot[domain=x2:x3, samples=50] (\x, {g(\x)})
  -- (x3, y_top) -- (x1, y_top) -- cycle;

```

#### 8.4.3.2 3D 幾何および回転体

* **視線角の設定**:
* `\tdplotsetmaincoords{65}{115}` または `{70}{120}` を標準とし、各頂点や面が重なって潰れない角度を選ぶ。

* **立体の前後関係**:
* 奥に隠れる稜線・投影線は必ず `dashed, gray!60` で描く。
* 手前の面は薄いカラー（`opacity=0.6` 程度）で透過塗りつぶしを行う。

* **直交・等長記号**:
* 中点等長マーク: ベクトル方向を算出し、短い2本線（`||`）を各線分中央に描画。
* 面と直線の直交: 単位方向ベクトルを用いて立体的に整合する直角マークを描く。

* **回転体の切断面**:
* 円環領域は `even odd rule` でくり抜いてハッチングする。

```latex
\fill[pattern=north east lines, pattern color=blue!55, opacity=0.7, even odd rule]
  (O) circle (r_max)
  (O) circle (r_min);

```
* 外径 $r_{\max}$、内径 $r_{\min}$ の動径ベクトル矢印と、元の切断線分を重ねて表示する。

### 8.4.4. 自動検証・ワークフロー（CLI 実行時）

1. **構文の事前チェック**:
* `pgfmath` の trigonometric 関数において、ラジアン指定時は引数に `r` を付ける（例: `sin(\x r)`）。
* `\x` の累乗展開エラーを防ぐため、`\x^2` ではなく `(\x*\x)` を優先する。

2. **コンパイル検証**:
* コード生成後、CLI 側でテンポラリ `.tex` を作成し、`pdflatex -interaction=nonstopmode` または `lualatex` でコンパイルを実行する。
* エラーが出た場合はログの行番号とエラーメッセージを解析し、自動でコードを修正・再実行する。

3. **成果物**:
* 修正済み LaTeX コードブロックと、成功した確認用 PNG 画像を出力する。

---

## 9. 開発環境の前提

* Node.js v18.14.1 以上（Astro v4）
* Python 3.x（`pypandoc`, `TexSoup` が必須）
* Pandoc, poppler-utils（`pdftocairo`）, TeX Live（LuaLaTeX / pdflatex, 日本語対応。統合マスター PDF ビルドには `texlive-lang-japanese texlive-luatex texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-science texlive-fonts-extra` 相当が必要）
* `gh` CLI（Issue 駆動の進捗管理・デプロイ確認に使用、認証済みであること）
* [`pre-commit`](https://pre-commit.com/)（`pip install pre-commit` 等）と Rust ツールチェイン（`tex-fmt` フックが `language: rust` で自身をビルドするため）。クローン後に一度 `pre-commit install` を実行しておくと、以後のコミットで `.tex` ファイルが自動整形される（6節参照）。

---

## 10. ライセンス

デュアルライセンス（詳細は `LICENSE`）。
* コンテンツ（解答解説・TeX ソース・TikZ 画像）: CC BY-NC-SA 4.0
* プログラムコード（`web/`, `scratch/`, 設定ファイル）: MIT License
