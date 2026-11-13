# 表の規約（下書き）

増減表などの表を TeX で書くときの規約の正本。節番号（§TB）で引けるようにする。
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

## TB2. 増減表

### TB2.1 行と列の構成
- 1列目を見出しの列にし、上から `$x$`（変数）、`$f'(x)$`、（凹凸も調べるなら）`$f''(x)$`、`$f(x)$` の行を並べる。
- 列の指定は `c|ccc…`（見出しの列のあとに縦線1本）を基本にし、行の間は `\hline` で区切る。列の数は、データの列の数とちょうど合わせる（余分な列を作らない）。
- 変数の行には、定義域の端点・導関数が 0 や定義されない点を左から順に置き、その間を `$\cdots$` でつなぐ。
- 分数を含む表は `\renewcommand{\arraystretch}{1.4}` 程度で行の高さを広げる（`table` の中に書き、ほかの表に影響させない）。
- 例：
  ```latex
  \begin{table}[htb]
    \centering
    \caption{$f(x)$ の増減表}
    \label{tab:increase_decrease}
    % 例：f(x)=x^2(1-x)（0 \le x \le 1），f'(x)=x(2-3x)
    \renewcommand{\arraystretch}{1.4}
    \begin{tabular}{c|ccccc}
      \hline
      $x$     & $0$ & $\cdots$   & $\dfrac{2}{3}$          & $\cdots$   & $1$  \\ \hline
      $f'(x)$ & $0$ & $+$        & $0$                     & $-$        & $-1$ \\ \hline
      $f(x)$  & $0$ & $\nearrow$ & 極大 $\dfrac{4}{27}$    & $\searrow$ & $0$  \\ \hline
    \end{tabular}
  \end{table}
  ```

### TB2.2 符号と矢印を対応させる
- 導関数の行の符号（`$+$`・`$-$`・`$0$`）と、関数の行の矢印を必ず対応させる：`$+$` の区間は `$\nearrow$`、`$-$` の区間は `$\searrow$`。
- 導関数が 0 になる点・端点では、関数の値を書く。極値なら「極大」「極小」を添えてよい。
- 符号は、本文で求めた導関数の式（因数分解した形など）から決め、表の前後の本文と食い違わないようにする。

### TB2.3 端点と、定義されない点
- 定義域に含まれる端点は、その点の値をそのまま書く。
- 含まれない端点・無限大では、極限の値を括弧に入れて書く（例：`$(0)$`、`$(\to\infty)$`、`$(-\infty)$`）。括弧が「その点の値ではなく極限」であることを、caption か本文で一言示す。
- 導関数が定義されない点・その点で値を持たない欄は、空欄にする。記号（`/`・`×` など）を入れる場合は、意味を本文で示す。

### TB2.4 凹凸
- 凹凸も表にする場合は `$f''(x)$` の行を足し、関数の行には増減と凹凸を1つで表す矢印を使う。プリアンブルに次の4つを定義して使う（意味：Convex＝下に凸（$f''>0$）、Concave＝上に凸（$f''<0$））。

  | 命令 | 増減 | 凹凸 |
  |---|---|---|
  | `\carrowIncreaseConvex` | 増加 | 下に凸 |
  | `\carrowIncreaseConcave` | 増加 | 上に凸 |
  | `\carrowDecreaseConvex` | 減少 | 下に凸 |
  | `\carrowDecreaseConcave` | 減少 | 上に凸 |

  ```latex
  % 下に凸の増加・上に凸の増加・下に凸の減少・上に凸の減少（向きは TikZ の bend の左右で決まる）
  \providecommand{\carrowIncreaseConvex}{\tikz[scale=0.22,baseline=-0.2ex]{\draw[->,>=stealth,thick] (0,0) to[bend right=40] (1.2,1);}}
  \providecommand{\carrowIncreaseConcave}{\tikz[scale=0.22,baseline=-0.2ex]{\draw[->,>=stealth,thick] (0,0) to[bend left=40] (1.2,1);}}
  \providecommand{\carrowDecreaseConvex}{\tikz[scale=0.22,baseline=-0.2ex]{\draw[->,>=stealth,thick] (0,1) to[bend right=40] (1.2,0);}}
  \providecommand{\carrowDecreaseConcave}{\tikz[scale=0.22,baseline=-0.2ex]{\draw[->,>=stealth,thick] (0,1) to[bend left=40] (1.2,0);}}
  ```
- 既存の矢印（`\curvearrowright` など）を `\rotatebox`・`\raisebox` で回したりずらしたりして流用しない。向きが読み取りにくく、Web（MathJax）では表示できない。
- 矢印の形は、表を画像にして確かめる（定義の左右を取り違えると、凹凸が逆向きに描かれる）。

### TB2.5 照合すること
- 導関数の符号が、本文の式から計算した符号と一致するか（各区間で1点ずつ代入して確かめる）。
- 矢印の向き・凹凸が、符号の行と一致するか。
- 表の値（極値・端点の値・極限）が、本文で求めた値と一致するか。
- 列の数と、`tabular` の列の指定が合っているか。
- lint：なし。`\rotatebox` で回した矢印の検出は今後追加する。

---

## TODO（これから書く節）
- 数表・場合の数の表
