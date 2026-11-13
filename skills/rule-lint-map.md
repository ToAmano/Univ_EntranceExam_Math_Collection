# 規約と lint の対応表（作業用）

`scratch/lint_latex_style.py` の検査と、規約の記載場所（AGENTS.md・AGENT.md 8.3.6・figure-rules.md）を突き合わせたもの。
「行き先」は、スキルの規約ファイルに分けるときの移動先の案。

- notation：数式・記法（`notation-rules.md`）
- table：表（`table-rules.md`）
- figure：図（`figure-rules.md`）
- structure：見出し・ファイル構成など、このリポジトリ固有のもの（`local/`）

## A. lint が検査している規則

| # | lint の検査 | 内容 | 規約の記載 | 行き先 |
|---|---|---|---|---|
| A1 | `check_align_star` | `align*` を使わない | AGENTS.md・8.3.6 | notation |
| A2 | `check_equation_env` | `equation`/`equation*` を使わない | AGENTS.md・8.3.6 | notation |
| A3 | `check_display_math_brackets` | `\[ ... \]` を使わない | AGENTS.md・8.3.6 | notation |
| A4 | `check_display_math_dollars` | `$$ ... $$` を使わない | AGENTS.md | notation |
| A5 | `check_trailing_align_break` | `align` の最後の行に `\\` を付けない（空の式番号が出る） | **記載なし** | notation |
| A6 | `check_bare_args` | `\sqrt`・`\frac`・`\dfrac` の引数を `{}` で囲む | 8.3.6 | notation |
| A7 | `check_frac_subscript_rule` | 分数は `\dfrac`、添字位置と tikzpicture 内は `\frac` | 8.3.6・figure §4.2 | notation |
| A8 | `check_left_right_balance` | `align` ブロック内の `\left` と `\right` の数を一致させる | **記載なし** | notation |
| A9 | `check_vector_notation` | 1文字は `\vec`、2文字以上は `\overrightarrow`、添字は `\vec` の外 | AGENTS.md・8.3.6 | notation |
| A10 | `check_reference_commands` | `\ref`/`\eqref` を使わず `\cref` | AGENTS.md | notation |
| A11 | `check_equation_references` | 数式ラベルは `eq:1` 形式の連番。未定義のラベルを参照しない | **記載なし**（`\cref` のみ記載） | notation |
| A12 | `check_duplicate_labels` | 同じファイル内でラベルを重複させない | **記載なし** | notation |
| A13 | `check_local_references` | 同じ問題の problem.tex とラベルを重複させない | **記載なし** | structure |
| A14 | `check_figure_caption` | figure に `\caption` 必須 | 8.3.6・figure §1.3 | figure |
| A15 | `check_table_caption` | table に `\caption` 必須 | 8.3.6 | table |
| A16 | `check_tikz_nesting` | tikzpicture は figure の中（数式中のアイコンは例外） | 8.3.6・figure §1.1 | figure |
| A17 | `check_tabular_nesting` | tabular は table の中 | 8.3.6 | table |
| A18 | `check_tikz_point_circle` | 点は `\node[circle]` で打つ | AGENTS.md・figure §4.1 | figure |
| A19 | `check_punctuation` | 句読点は「．」「，」 | 8.3.6 | structure |
| A20 | `check_proof_env` | 解答の冒頭に `\begin{proof}[解]` を使わない | 8.3.6 | structure |
| A21 | `check_solution_headings` | `[解答]`・`[別解]`・`[別解1]`・`[解説]` に統一（solution.tex のみ） | AGENTS.md | structure |
| A22 | `check_documentclass` | 1行目は `\documentclass[../../main.tex]{subfiles}` | 8.3.6 | structure |
| A23 | `check_spacing_commands` | 本文で余白・改行のコマンド（`\medskip`・`\bigskip`・`\vspace`・`\hspace`・`\hfill`・`\noindent`・数式の外の `\quad` など）を使わない（2026-11-13 追加） | AGENTS.md | notation |
| W1 | `check_overline_warning`（警告） | 辺の長さは `\overline{AB}` でなく `|AB|` | 8.3.6 | notation |
| W2 | `check_long_align_lines`（警告） | `align` の1行が長く `=` が複数あるときは改行する | **記載なし** | notation |

補足
- A18 が検出するのは pt 単位で 3.5pt 以下の `circle` だけ。座標単位の小さな円（`circle (0.07)`）や `circle (10pt)` は検出できない。
- `% lint-skip:` の印があるファイルは、A13 以外を検査しない（旧 jarticle 形式の未移行ファイル用、#593）。

## B. 規約にあるが lint が検査していない規則

判定：◯ 機械的に検出できる　△ 経験則で候補を出せる（警告向き）　× 機械では判定できない

| # | 規則 | 記載 | 判定 | 行き先 |
|---|---|---|---|---|
| B1 | 途中式に番号が要らない変形は `split` で番号を1つにまとめる | AGENTS.md・8.3.6 | △ | notation |
| B2 | 大きい括弧は `\Bigl`/`\Bigr` などでサイズを明示し、素の `( )` `[ ]` を使わない | 8.3.6 | △（分数・指数を含む素の括弧を検出） | notation |
| B3 | `cases` の中では `\displaystyle` を使う | 8.3.6 | ◯ | notation |
| B4 | 小問は `\paragraph{(1)}` で見出しにし、`enumerate` で囲まない | 8.3.6 | △（場合分けの `enumerate` は許容されるため） | structure |
| B5 | 1ページに収めるための圧縮をしない | AGENTS.md・figure §0.3 | × | notation |
| B6 | 手書き原稿の解法に忠実に文字起こしする | 8.3.7 | × | structure |
| B7 | 2段組の中の figure・table は `[H]` | figure §1.2 | ◯ | figure・table |
| B8 | 中央寄せは `center` 環境ではなく `\centering` | figure §1.1 | ◯ | figure・table |
| B9 | `subfigure` を使わず `subcaptionblock` | figure §1.4 | ◯ | figure |
| B10 | 図の TODO は figure 環境の中に書く | figure §1.5 | ◯ | figure |
| B11 | 線・パターンの灰色は `gray!60!black` 以上 | figure §3.2 | ◯ | figure |
| B12 | 座標軸は `gray!80!black` | figure §3.1 | △ | figure |
| B13 | 破線（`dashed`）は隠れ線専用 | figure §3.1 | △（3D でない図の `dashed` を警告） | figure |
| B14 | 平面の領域は斜線パターン（ベタ塗りだけにしない） | AGENTS.md・figure §5.1 | △（3D でない図の `\fill` を警告） | figure |
| B15 | 3D の視点は figure の中、tikzpicture の直前で `\tdplotsetmaincoords` | figure §7.1 | ◯ | figure |
| B16 | 遷移図で各状態から出る確率の和が1 | figure §8.5 | △（ラベルが数値なら検算できる） | figure |
| B17 | 点が線上にある・接する・直角などの幾何の整合 | figure §10 | △（座標を評価する別ツールが要る） | figure |
| B18 | PDF の全ページと Web 用 SVG を目視する | AGENTS.md・figure §11 | × | figure |
| B19 | 代表点から座標軸へ垂線を下ろす | AGENTS.md・figure §6.1 | × | figure |
| B20 | 増減表の凹凸を `\rotatebox` の矢印で書かない | 1977-6 の TODO のみ | ◯ | table |
| B21 | 場合分けは `dcases` を使い、`cases` を使わない（2026-11-12 採用） | notation §N1.1 | ◯ | notation |
| B22 | `\binom` 系を使わず `{}_nC_k` で書く（2026-11-12 採用） | notation §N2.1 | ◯ | notation |

## C. 規約に書き足す必要があるもの

lint だけにあって規約に書かれていない規則（A5・A8・A11・A12・A13・W2）。規約側に理由つきで記載し、lint のメッセージから節番号で引けるようにする。
