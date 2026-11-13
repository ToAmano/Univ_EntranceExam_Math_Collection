# 手書き答案の文字起こし：このリポジトリ固有の手順（下書き）

汎用の規約は `references/transcription-rules.md`（§TR）。ここには、このリポジトリでの置き場所・スクリプト・ステータス管理だけを書く。
元の手順は AGENT.md 8節。移し終えたら AGENT.md 8節はこのファイルへの案内に縮める。

---

## L1. 原稿の置き場所とページ構成

- 原稿は年度ごとに `src/{univ}/{cat}/{year}/handwritten.pdf`。
- 基本は「表紙1ページ ＋ 大問ごとに1ページ」だが、1つの大問が2ページ以上にわたることがある（例：東大前期1976年第2問は、検討メモの物理3ページと本解の物理4ページ）。§TR2.1 に従い、見出しの「第N問」で全ページを確認する。
- 大問の数は年度によって4〜6問で変わる。
- 各設問ディレクトリの個別 PDF（`ut-{YY}-{Q}.pdf` など）は問題文だけのことがある。空欄かどうかは必ず年度単位の `handwritten.pdf` で確かめる。

## L2. 年度ごとの基本サイクル

年度は**古い順に1年ずつ**処理する。

1. **構成確認**：`pdfinfo {year}/handwritten.pdf` でページ数を確認する。東工大では `scratch/tmp_download/08_titech/{year}/{year}_{q}.tex` の実在数が、その年度の大問数の手がかりになる（`{year}_6.tex` があれば第6問がある）。
2. **全体の描画**：`pdftoppm -png -r 200 {year}/handwritten.pdf <一時ディレクトリ>/hw{year}` 程度で全ページを一覧する（§TR2.1）。
3. **`problem.tex` と照合**してから読み進める（§TR2.2）。
4. **書き起こし・分割**（L4）。
5. **検査とビルド**（L6）。
6. **ステータス更新**（L7）。
7. 複数年度をまとめて処理したら `python3 scratch/generate_main_tex.py {univ}/{cat}` で `main.tex` を作り直し、可能なら全体ビルド（AGENT.md 5節）でも通しで確認する。

## L3. 一時ファイル

- ページの描画（`pdftoppm`）や切り出しの画像は、セッションの scratchpad（なければ `mktemp -d` で作った一時ディレクトリ）に置き、リポジトリに残さない。
- 単体コンパイルも `latexmk -outdir=<一時ディレクトリ>` で行い、`solution.aux` などをリポジトリに作らない。

## L4. 新規の文字起こし（年度単位）

1. `{year}/handwritten_tex.tex` に大問ごとに `\section*{第N問}` で区切って起こす。冒頭は `\documentclass[../../../../main.tex]{subfiles}` と `\begin{document}`、末尾は `\end{document}`。各大問の解答は `{\bf [解答]}` から始める（`\begin{proof}[解]` は使わない）。
2. `python3 scratch/split_handwritten_tex.py {univ}` で `{year}/{q}/solution.tex` に分割する。既存の `solution.tex` は上書きされない。
3. 既存の `solution.tex` に追記する場合は、§TR5.2 に従い、既存の解答の後ろに別解として足す。
4. 第6問がある年度は、`problem.tex` が取り込まれていないことがある（`scratch/batch_import_all_problems.py` の不具合）。必要なら手動で取り込む。

## L5. 空欄の記録

- 原稿が空欄の大問は、`% (原稿において第N問の解答は空欄)` の1行コメントだけを残し、本文なしで `\newpage` を置く。分割後の `solution.tex` はコメントだけになる。これは起こし漏れではなく、当時から解答がなかったことを示す状態である。
- 存在しない設問番号のディレクトリは作らない。
- 行列（一次変換）の問題は、当時の教育課程の都合で解かれていないことがある。これも空欄のままにする。

## L6. 検査とビルド

- `python3 scratch/lint_latex_style.py <ファイル>` を通す。
- 単体コンパイル：`cd src/{univ}/{cat}/{year}/{q} && latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=<一時ディレクトリ> solution.tex`
- 年度の複数の大問をまとめて確認したい場合は、プリアンブル一式（`scratch/generate_main_tex.py` の `PREAMBLE` と同じ内容）と対象年度の大問だけを `\subfile` する `test{year}.tex` を作ってコンパイルしてもよい。この場合は確認後に `test{year}.{pdf,aux,log,fls,fdb_latexmk,synctex.gz,toc,out,tex}` を必ず削除する。
- 図がある場合は `pdftoppm` で PNG にし、原稿のスキャンと見比べる。
- 古い `zahyou` 環境（emath）は今のプリアンブルでは未定義でビルドが止まる。同じファイルに残っている場合は TikZ に書き直す。

## L7. ステータスと誤りの記録

- 大問1つを起こし終えるたびに `python3 scratch/generate_status_markdowns.py` を実行し、`docs/status/{univ}_{cat}.md` を更新する。自動で付くのは「文字起こし済」まで。`finish` は人が最終確認したあとに手で付ける。
- `% 原稿ママ：` を付けた誤りのうち、結論や論証に影響するものは、文字起こしとは別に Issue で扱う（既存の Issue があれば追記する）。
