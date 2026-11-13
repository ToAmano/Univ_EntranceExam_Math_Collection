# 表の規約（下書き）

増減表などの表を TeX で書くときの規約の正本（作成中）。節番号（§TB）で引けるようにする。
利用先固有の例外（凡例の枠囲みなど）は `local/notation.md` にある。

---

## TB1. 表の置き方

### TB1.1 `table` の中に置く
- `tabular` は必ず `table` の中に置き、`\centering` で中央に寄せる（`\begin{table}[htb]\centering\begin{tabular}...\end{tabular}\end{table}`）。増減表も `table` を省略しない。`table` があると「表N」の通し番号が付き、図と扱いがそろう。
- 複数の表を並べる場合は、`table` の中で `subcaptionblock` を使う。
- TikZ の図の中のノードに置く小さな表は対象外。
- lint：`check_tabular_nesting`。

### TB1.2 caption を付ける
- `table` には必ず `\caption{...}` を付け、何を表す表かを一言で書く（増減表なら「$f(x)$ の増減表」など）。
- lint：`check_table_caption`。

---

## TODO（これから書く節）
- 増減表：列の構成、符号と矢印の対応、端点の値、定義されない点の書き方、凹凸の記号（`\rotatebox` の矢印を使わない）
- 数表・場合の数の表
