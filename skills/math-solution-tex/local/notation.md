# このリポジトリ固有の記法（下書き）

汎用の記法は `references/notation-rules.md`（§N）、表は `references/table-rules.md`（§TB）。
ここには、このリポジトリのファイル構成・見出し・Web への変換に結びついた記法だけを書く。
lint の検査は `local/lint_local.py`。

---

## LN1. 解答の見出し

- 解答関連の見出しは次の表記に統一する。
  - 最初の解法：`{\bf [解答]}`
  - 別解が1つ：`{\bf [別解]}`
  - 別解が複数：`{\bf [別解1]}`、`{\bf [別解2]}`、…（最初の解法は番号に含めない）
  - 解法の後の説明：`{\bf [解説]}`
- 手書き原稿が `[解1]`・`[解2]` など別の見出しでも、本文と順序を保ったまま、TeX の見出しはこの表記にする（文字起こしでの対応は `references/transcription-rules.md` §TR5）。
- 解答の冒頭に `\begin{proof}[解]...\end{proof}` は使わない。補題の証明などの本物の `proof` 環境（`[...]` なし）は使ってよい。
- lint：`check_solution_headings`（`--fix` で直す）、`check_proof_env`。

## LN2. 小問の見出し

- 小問（(1)、(2)、…）は `enumerate` で囲まず、`\paragraph{(1)}` を単独の行に置き、次の行から解答を続ける。`\paragraph` は Web（Markdown）への変換で見出しになる。
- 地の文で既出の小問を参照する場合（「(1)の結果より」など）は見出しにしない。
- 場合分け（1°、2°、…）に `enumerate`・`itemize` を使うのはかまわない。
- lint：なし（小問か場合分けかは目視で判断）。

## LN3. ファイルの構成

- `solution.tex`・`problem.tex` の1行目は `\documentclass[../../main.tex]{subfiles}`（`src/{univ}/{cat}/{year}/{q}/` から `src/{univ}/{cat}/main.tex` へは2階層上がる）。
- `solution.tex` は、`[解答]` の見出しより前で問題文を枠付きで読み込む：`\begin{oframed}\subfile{problem}\end{oframed}`。
- `problem.tex` は `\begin{document}` を持つ独立した subfiles 文書にする。`solution.tex` の枠の中に読み込まれ、枠の中では浮動体を使えないので、`problem.tex` の `figure` は `[H]` にする。
- `solution.tex` のラベルは、同じ問題の `problem.tex` のラベルと重複させない（§N10.4 の補足。`\cref` は `problem.tex` のラベルも参照できる）。
- lint：`check_documentclass`、`check_problem_embedded`、`check_problem_is_document`、`check_problem_figure_float`、`check_problem_label_conflicts`。

## LN4. 年度のまとめ・凡例

- 年度のまとめ（`{year}/0/solution.tex`）は、余白の命令（§N11）と `\qed`（§N3）の検査の対象外。
- `\shadowbox{...}` で表全体を枠で囲む凡例的な `tabular` は、`table` に入れなくてよい（§TB1.1 の例外）。

## LN5. lint の対象外にする印

- 古い形式のまま未移行のファイルは、先頭付近に `% lint-skip: 理由` を書くと、ラベル・参照の検査以外を外せる。理由は必ず書く（空のまま放置されると違反が溜まる）。
