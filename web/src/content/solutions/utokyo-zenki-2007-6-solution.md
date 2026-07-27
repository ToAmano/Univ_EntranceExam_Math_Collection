---
university: "utokyo"
category: "zenki"
year: "2007"
question: "6"
type: "solution"
title: "UTOKYO 2007 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{proof}[解]
(1) $y = \frac{1}{t}$ のグラフは $t > 0$ の時, 下に凸だから, 右図で面積を比較して ($\because a-x > 0$)

\begin{tikzpicture}[scale=2]
  \draw[->] (-0.2,0) -- (3,0) node[right] {$t$};
  \draw[->] (0,-0.2) -- (0,2.5) node[above] {$y$};
  
  \draw[domain=0.5:2.5, smooth, variable=\t, blue, thick] plot ({\t}, {1.8/\t}) node[right] {$y = \frac{1}{t}$};
  
  \coordinate (P) at (0.8, {1.8/0.8});
  \coordinate (A) at (1.4, {1.8/1.4});
  \coordinate (B) at (2.0, {1.8/2.0});
  
  \draw[dashed] (0.8,0) node[below] {$a-x$} -- (P);
  \draw[dashed] (1.4,0) node[below] {$a$} -- (A);
  \draw[dashed] (2.0,0) node[below] {$a+x$} -- (B);
  
  \draw[red, thick] (0.6, {1.8/1.4 - (-0.918)*(0.6-1.4)}) -- (2.2, {1.8/1.4 - (-0.918)*(2.2-1.4)}) node[right] {点Aでの接線};
  
  \draw[green!60!black, thick] (P) -- (B);
  
  \fill (P) circle (1pt) node[above left] {$P$};
  \fill (A) circle (1pt) node[above right] {$A$};
  \fill (B) circle (1pt) node[right] {$B$};
  \node[left] at (0, {1.8/1.4}) {$\frac{1}{a}$};
\end{tikzpicture}

$$
\begin{align*}
\text{台形} ABCD < \int_{a-x}^{a+x} \frac{1}{t} dt < \text{台形} ABEF
\end{align*}
$$

だから

$$
\begin{align*}
\frac{2x}{a} < \int_{a-x}^{a+x} \frac{1}{t} dt < x \left( \frac{1}{a-x} + \frac{1}{a+x} \right) \quad \text{\#}
\end{align*}
$$

(2) (1) と同様の評価を $[a-x, a]$, $[a, a+x]$ で行うことで以下の不等式を得る.

$$
\begin{align*}
\frac{x}{a - \frac{x}{2}} < \int_{a-x}^a \frac{1}{t} dt < \frac{1}{2} x \left( \frac{1}{a} + \frac{1}{a-x} \right)
\end{align*}
$$

$$
\begin{align*}
\frac{x}{a + \frac{x}{2}} < \int_a^{a+x} \frac{1}{t} dt < \frac{1}{2} x \left( \frac{1}{a} + \frac{1}{a+x} \right)
\end{align*}
$$

辺々足して,

$$
\begin{align*}
2x \left( \frac{1}{2a-x} + \frac{1}{2a+x} \right) < \int_{a-x}^{a+x} \frac{1}{t} dt < \frac{1}{2} x \left( \frac{2}{a} + \frac{1}{a-x} + \frac{1}{a+x} \right) \quad \cdots ①
\end{align*}
$$

この中辺は $\log \frac{a+x}{a-x}$ であることに注意し, $a=3x$ ($0 < x < a$) を ① に代入し,

$$
\begin{align*}
\frac{2}{5} + \frac{2}{7} < \log 2 < \frac{1}{2} \left( \frac{2}{3} + \frac{3}{4} \right)
\end{align*}
$$

$$
\begin{align*}
\frac{24}{35} < \log 2 < \frac{17}{24} \quad \cdots ②
\end{align*}
$$

ここで,

$$
\begin{align*}
\frac{24}{35} - \frac{68}{100} = \frac{1}{5} \left( \frac{24}{7} - \frac{17}{5} \right) = \frac{1}{5} \cdot \frac{1}{35} > 0 \quad \therefore 0.68 < \frac{24}{35}
\end{align*}
$$

$$
\begin{align*}
\frac{71}{100} - \frac{17}{24} = \frac{1}{600} (426 - 425) = \frac{1}{600} > 0 \quad \therefore 0.71 > \frac{17}{24}
\end{align*}
$$

だから, ① とあわせて

$$
\begin{align*}
0.68 < \log 2 < 0.71 \quad \text{\#}
\end{align*}
$$

\end{proof}

### [(2) 別解]

（なぜか中点を $\log 2$ にすると解決する）
$x = (3 - 2\sqrt{2})a$ と推測（条件をみたす！）. (1) に代入して

$$
\begin{align*}
6 - 4\sqrt{2} < \frac{1}{2} \log 2 < \frac{15}{64}
\end{align*}
$$

$$
\begin{align*}
4(3 - 2\sqrt{2}) < \log 2 < \frac{1}{2}
\end{align*}
$$

$1.415 < \sqrt{2} < 1.42$ を示して用いることで, 所望の不等式を得る.

\begin{tikzpicture}[scale=1.8]
  \draw[->] (-0.2,0) -- (2.5,0) node[right] {$t$};
  \draw[->] (0,-0.2) -- (0,2) node[above] {$y$};
  \draw[domain=0.5:2.2, smooth, variable=\t, blue, thick] plot ({\t}, {1.5/\t});
  \draw[dashed] (0.8,0) node[below] {$a-x_2$} -- (0.8, {1.5/0.8});
  \draw[dashed] (1.2,0) node[below] {$a-x_1$} -- (1.2, {1.5/1.2});
  \draw[dashed] (1.6,0) node[below] {$a$} -- (1.6, {1.5/1.6});
  \node at (1.0, 1.2) {誤差};
\end{tikzpicture}

$x_1 = (3-2\sqrt{2})a$, $x_2 = \frac{1}{3}a$ において,
$x_1 < x_2$ となっているので, グラフを考えると, 明らかに $x_1$ の方が正確な評価（近似）になっている, という仕掛けかな.