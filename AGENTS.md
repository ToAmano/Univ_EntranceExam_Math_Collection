# 数学答案の TeX を書く・直す・文字起こしするとき

スキル `math-solution-tex`（[skills/math-solution-tex/SKILL.md](skills/math-solution-tex/SKILL.md)）の工程に従う。規約の正本と節番号は次のとおり。下の必須規則は要約で、細部・理由・例外は各節にある。

- 数式・記法：[references/notation-rules.md](skills/math-solution-tex/references/notation-rules.md)（§N）
- 図（TikZ）：[references/figure-rules.md](skills/math-solution-tex/references/figure-rules.md)（§0〜§12）
- 表・増減表：[references/table-rules.md](skills/math-solution-tex/references/table-rules.md)（§TB）
- 手書き原稿の文字起こし：[references/transcription-rules.md](skills/math-solution-tex/references/transcription-rules.md)（§TR）
- このリポジトリ固有の記法・手順・コマンド・手本の図：[local/](skills/math-solution-tex/local/)（`notation.md`・`transcription.md`・`workflow.md`）

# 必須の規則

- **見出し**：最初の解法は `{\bf [解答]}`、別解が1つなら `{\bf [別解]}`、複数なら `{\bf [別解1]}`・`{\bf [別解2]}`…、解法の後の説明は `{\bf [解説]}`（local/notation LN1）。
- **数式環境**：別行立ての数式は1行でも `align`。`equation`・`equation*`・`align*`・`\[ ... \]`・`$$ ... $$` は使わない。途中の番号は `\notag` か `split` でまとめる（§N5）。
- **分数**：`\dfrac`。添字の位置と TikZ のラベルでは `\frac`。引数は必ず `{}` で囲む（§N6）。
- **ベクトル**：1文字は `\vec`、2文字以上は `\overrightarrow`。添字・プライムは `\vec{a}_1` のように外に出す（§N8）。
- **参照**：`\cref` に統一し、`\eqref`・`\ref` は使わない。数式のラベルは `eq:1` 形式の連番（§N10）。
- **証明・解答の終わり**：数式の外の文末に `\qed`。`$\blacksquare$` などの記号を直接書かない（§N3）。
- **句読点・余白**：和文の句読点は「．」「，」。本文で `\medskip`・`\vspace`・`\noindent`・数式の外の `\quad` などの余白の命令を使わない（§N4・§N11）。
- **紙面**：1ページに収めるための圧縮（式を詰める、図を縮める）をしない。作業報告でも「1ページに収めた」と書かない（figure §0.3）。
- **図**：点は `\node[circle, ...]` で打つ。領域は斜線パターンで塗る。代表点から座標軸へ点線の垂線を下ろす。`gray!30`〜`gray!50` のような薄い灰色を使わない（figure §3〜§6）。
- **文字起こし**：原稿の解法・表現をそのまま起こし、別の解法に差し替えない。原稿の誤りは直さず `% 原稿ママ：` のコメントで示す（§TR1・§TR4）。

# 図だけを直す指示のとき（厳守）

図の追加・修正・差し替え（旧式の図や作図の TODO を TikZ にする作業を含む）を指示された場合は、**図のブロック以外の本文・数式・見出し・プリアンブル・相互参照・空行を一切変えない**（figure §12）。

- 未移行ファイルの `subfiles` 化、数式環境の書き換え、見出しの統一、`\cref` 化などを「ついでに」行わない。
- 作業後は `python3 scratch/check_figure_only_diff.py <編集したTeXファイル>` を実行し、`PASS` になるまで完了にしない。`FAIL` なら図以外の変更を元に戻す（使い方は local/workflow W3）。

# 京大前期の図を起こすとき

東大前期の TikZ 図の情報の整理の仕方を手本にする。原稿にある点・線・領域・前後関係と、問題や解答に必要な数学的条件を先に確定し、色や装飾のために形状・位置関係・開閉端点を変えない（figure §0）。新しい平面図は figure 付録 A の雛形から作る。手本のファイルと、それぞれ規約と食い違う点は local/workflow W6 にある。

仕上げに PDF の**全ページ**と Web 用 SVG を表示して目視する。TeX のコンパイルだけで表示確認を済ませない（figure §11、コマンドは local/workflow W4・W5）。

# 監査のとき

監査で問題を見つけた場合は、既存の原稿を編集せず Issue に記録する。既存原稿の一括変更（見出しの統一など）は別作業とする。

# 検査

- lint：`python3 scratch/lint_latex_style.py <file>`（本体はスキルの `scripts/lint_tex.py` と `local/lint_local.py`）
- 式変形の検算：`python3 skills/math-solution-tex/scripts/check_math_steps.py <file>`

その他の開発・ビルド・Web 変換の手順は [AGENT.md](AGENT.md) を参照する。
