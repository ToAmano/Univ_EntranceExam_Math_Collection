# 規約と lint の対応表（作業用）

lint の検査と、規約の記載場所（notation・figure・table の各規約と local/notation.md）を突き合わせたもの。
lint の本体は `skills/math-solution-tex/scripts/lint_tex.py`（汎用）と `skills/math-solution-tex/local/lint_local.py`（固有：行き先が structure のもの）。`scratch/lint_latex_style.py` は両者を読み込む入口。
「行き先」は、スキルの規約ファイルに分けるときの移動先の案。

- notation：数式・記法（`notation-rules.md`）
- table：表（`table-rules.md`）
- figure：図（`figure-rules.md`）
- structure：見出し・ファイル構成など、このリポジトリ固有のもの（`local/`）

## A. lint が検査している規則

| # | lint の検査 | 内容 | 規約の記載 | 行き先 |
|---|---|---|---|---|
| A1 | `check_align_star` | `align*` を使わない | notation §N5.1 | notation |
| A2 | `check_equation_env` | `equation`/`equation*` を使わない | notation §N5.1 | notation |
| A3 | `check_display_math_brackets` | `\[ ... \]` を使わない | notation §N5.1 | notation |
| A4 | `check_display_math_dollars` | `$$ ... $$` を使わない | notation §N5.1 | notation |
| A5 | `check_trailing_align_break` | `align` の最後の行に `\\` を付けない（空の式番号が出る） | notation §N5.3 | notation |
| A6 | `check_bare_args` | `\sqrt`・`\frac`・`\dfrac` の引数を `{}` で囲む | notation §N6.2 | notation |
| A7 | `check_frac_subscript_rule` | 分数は `\dfrac`、添字位置と tikzpicture 内は `\frac` | notation §N6.1・figure §4.2 | notation |
| A8 | `check_left_right_balance` | `align` ブロック内の `\left` と `\right` の数を一致させる | notation §N7.2 | notation |
| A9 | `check_vector_notation` | 1文字は `\vec`、2文字以上は `\overrightarrow`、添字は `\vec` の外 | notation §N8.1 | notation |
| A10 | `check_reference_commands` | `\ref`/`\eqref` を使わず `\cref` | notation §N10.1 | notation |
| A11 | `check_equation_references` | 数式ラベルは `eq:1` 形式の連番。未定義のラベルを参照しない | notation §N10.2・§N10.3 | notation |
| A12 | `check_duplicate_labels` | 同じファイル内でラベルを重複させない | notation §N10.4 | notation |
| A13 | `check_problem_label_conflicts`（旧 `check_local_references`） | 同じ問題の problem.tex とラベルを重複させない | local/notation LN3 | structure |
| A14 | `check_figure_caption` | figure に `\caption` 必須 | figure §1.3 | figure |
| A15 | `check_table_caption` | table に `\caption` 必須 | table §TB1.2 | table |
| A16 | `check_tikz_nesting` | tikzpicture は figure の中（数式中のアイコンは例外） | figure §1.1・§5.3 | figure |
| A17 | `check_tabular_nesting` | tabular は table の中 | table §TB1.1 | table |
| A18 | `check_tikz_point_circle` | 点は `\node[circle]` で打つ | figure §4.1 | figure |
| A19 | `check_punctuation` | 句読点は「．」「，」。「。」「、」と、和文に接する半角の「,」「.」を検出し `--fix` で直す（半角は 2026-11-13 追加） | notation §N4.1 | notation |
| A20 | `check_proof_env` | 解答の冒頭に `\begin{proof}[解]` を使わない | local/notation LN1 | structure |
| A21 | `check_solution_headings` | `[解答]`・`[別解]`・`[別解1]`・`[解説]` に統一（solution.tex のみ） | local/notation LN1 | structure |
| A22 | `check_documentclass` | 1行目は `\documentclass[../../main.tex]{subfiles}` | local/notation LN3 | structure |
| A23 | `check_spacing_commands` | 本文で余白・改行のコマンド（`\medskip`・`\bigskip`・`\vspace`・`\hspace`・`\hfill`・`\noindent`・数式の外の `\quad` など）を使わない（2026-11-13 追加） | notation §N11.1 | notation |
| A24 | `check_qed_mark` | 証明・解答の終わりは数式の外の文末に `\qed`（記号はプリアンブルで ■）。`$\blacksquare$`・`$\Box$`・文末の `$\square$`・数式の中の `\qed`・`\end{proof}` 直前の `\qed` を使わない（2026-11-13 追加） | notation §N3.1 | notation |
| W1 | `check_overline_warning`（警告） | 辺の長さは `\overline{AB}` でなく `|AB|` | notation §N9.1 | notation |
| W2 | `check_long_align_lines`（警告） | `align` の1行が長く `=` が複数あるときは改行する | notation §N5.4 | notation |
| A25 | `check_binom` | `\binom` 系を使わず `{}_nC_k`（2026-11-13 追加） | notation §N2.1 | notation |
| A26 | `check_subfigure_env` | `subfigure` を使わず `subcaptionblock`（2026-11-13 追加） | figure §1.4 | figure |
| A27 | `check_multicols_float` | 2段組の中の figure・table は `[H]`（2026-11-13 追加） | figure §1.2 | figure・table |
| A28 | `check_rotated_arrows` | 凹凸の矢印を `\rotatebox`・`\raisebox` で流用しない（2026-11-13 追加） | table §TB2.4 | table |
| A29 | `check_tdplot_placement` | `\tdplotsetmaincoords` は figure の中、tikzpicture の直前（2026-11-13 追加） | figure §7.1 | figure |
| A30 | `check_math_brackets` | 数式内の丸括弧 `()` と角括弧 `[]` の対応を合わせる（半開区間は許容） | notation §N7.3 | notation |
| A31 | `check_math_fullwidth` | 数式内に `\text{...}` 等を介さず全角文字を入れない | notation §N12.1 | notation |
| A32 | `check_prose_brackets` | 本文（`\text` 等・`\caption` を含む）の `()`・`（）`・`「」`・`『』` の対応を合わせる | notation §N7.4 | notation |
| W3 | `check_cases_env`（警告） | 場合分けは `dcases`（2026-11-13 追加。既存1165件のため警告） | notation §N1.1 | notation |
| W4 | `check_figure_todo_placement`（警告） | 作図の TODO は figure の中（2026-11-13 追加） | figure §1.5 | figure |
| W5 | `check_light_gray`（警告） | 線・文字・斜線に `gray!50` 以下を使わない（2026-11-13 追加） | figure §3.2 | figure |
| W6 | `check_small_coordinate_circle`（警告） | 点を座標単位の小さな `circle` で打たない（2026-11-13 追加） | figure §4.1 | figure |

補足
- A18 が検出するのは pt 単位で 3.5pt 以下の `circle` だけ。座標単位の小さな円（`circle (0.07)`）は W6 が警告する。
- 2026-11-13 から、lint の指摘の末尾に規約の節番号（`[§N5.1]`、`[§F1.3]`、`[§TB1.2]`、`[§LN1]`）が付く。
- `% lint-skip:` の印があるファイルは、A13 以外を検査しない（旧 jarticle 形式の未移行ファイル用、#593）。

## B. 規約にあるが lint が検査していない規則

判定：◯ 機械的に検出できる　△ 経験則で候補を出せる（警告向き）　× 機械では判定できない

| # | 規則 | 記載 | 判定 | 行き先 |
|---|---|---|---|---|
| B1 | 途中式に番号が要らない変形は `split` で番号を1つにまとめる | notation §N5.2 | △ | notation |
| B2 | 大きい括弧は `\Bigl`/`\Bigr` などでサイズを明示し、素の `( )` `[ ]` を使わない | notation §N7.1 | △（分数・指数を含む素の括弧を検出） | notation |
| B3 | `cases` の中では `\displaystyle` を使う | notation §N1.1（`dcases` へ移行。残す `cases` には `\displaystyle`） | ◯ | notation |
| B4 | 小問は `\paragraph{(1)}` で見出しにし、`enumerate` で囲まない | local/notation LN2 | △（場合分けの `enumerate` は許容されるため） | structure |
| B5 | 1ページに収めるための圧縮をしない | AGENTS.md・figure §0.3 | × | notation |
| B6 | 手書き原稿の解法に忠実に文字起こしする | transcription §TR1.1（旧 AGENT.md 8.3.7） | × | transcription |
| B7 | 2段組の中の figure・table は `[H]` | figure §1.2 | ◯ → 実装済み（A27） | figure・table |
| B8 | 中央寄せは `center` 環境ではなく `\centering` | figure §1.1 | ◯ | figure・table |
| B9 | `subfigure` を使わず `subcaptionblock` | figure §1.4 | ◯ → 実装済み（A26） | figure |
| B10 | 図の TODO は figure 環境の中に書く | figure §1.5 | ◯ → 実装済み（W4） | figure |
| B11 | 線・パターンの灰色は `gray!60!black` 以上 | figure §3.2 | ◯ → 実装済み（W5） | figure |
| B12 | 座標軸は `gray!80!black` | figure §3.1 | △ | figure |
| B13 | 破線（`dashed`）は隠れ線専用 | figure §3.1 | △（3D でない図の `dashed` を警告） | figure |
| B14 | 平面の領域は斜線パターン（ベタ塗りだけにしない） | AGENTS.md・figure §5.1 | △（3D でない図の `\fill` を警告） | figure |
| B15 | 3D の視点は figure の中、tikzpicture の直前で `\tdplotsetmaincoords` | figure §7.1 | ◯ → 実装済み（A29） | figure |
| B16 | 遷移図で各状態から出る確率の和が1 | figure §8.5 | △（ラベルが数値なら検算できる） | figure |
| B17 | 点が線上にある・接する・直角などの幾何の整合 | figure §10 | △（座標を評価する別ツールが要る） | figure |
| B18 | PDF の全ページと Web 用 SVG を目視する | AGENTS.md・figure §11 | × | figure |
| B19 | 代表点から座標軸へ垂線を下ろす | AGENTS.md・figure §6.1 | × | figure |
| B20 | 増減表の凹凸を `\rotatebox` の矢印で書かない | table §TB2.4 | ◯ → 実装済み（A28） | table |
| B21 | 場合分けは `dcases` を使い、`cases` を使わない（2026-11-12 採用） | notation §N1.1 | ◯ → 実装済み（W3） | notation |
| B22 | `\binom` 系を使わず `{}_nC_k` で書く（2026-11-12 採用） | notation §N2.1 | ◯ → 実装済み（A25） | notation |

## C. 規約に書き足す必要があるもの

A5・A8・A11・A12・A13・W2 は、notation §N5.3・§N7.2・§N10.2〜§N10.4・§N5.4 と local/notation LN3 に理由つきで記載した（2026-11-13）。残りは、lint のメッセージから節番号で引けるようにすること。
