---
university: "utokyo"
category: "zenki"
year: "1986"
question: "1"
type: "solution"
title: "UTOKYO 1986 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $C\left(c, \frac{1}{c}\right)$ ($c > 0$) での $y = \frac{1}{x}$ の接線は

$$
\begin{align*}
y = -\frac{1}{c^2} x + \frac{2}{c}
\end{align*}
$$

であるから, これと $x, y$ 軸の交点は各々 $P(2c, 0)$, $Q\left(0, \frac{2}{c}\right)$ である。

条件より, $\triangle ABC$ が $D$ の内部にあるので,

$$
\begin{align*}
\begin{cases}
0 \le a \le 2c \\
0 \le b \le \frac{2}{c}
\end{cases} \quad \dots \text{①}
\end{align*}
$$

である。

[★以下, 解1] $\triangle ABC$ の面積を $S$ とすると

$$
\begin{align*}
S = \frac{1}{2} \left| b(c - a) + \frac{a}{c} \right|
\end{align*}
$$

である。今, $a, c$ を固定し, 上式を $f(b)$ とおくと,

$1^\circ$ $c - a = 0$ の時

$$
\begin{align*}
S = \frac{1}{2} \frac{a}{c} \quad (\because a, c > 0)
\end{align*}
$$

$2^\circ$ $c - a \ne 0$ の時
$f(b)$ は $b$ の単調関数なので, $S$ は $b = 0$ または $b = \frac{2}{c}$ の時, 最大となるから,

$$
\begin{align*}
\max S = \max \left\{ \frac{1}{2} \frac{a}{c}, \,\, \frac{1}{2}\left|2 - \frac{a}{c}\right| \right\}
\end{align*}
$$

である ($\because$ ①より $0 \le \frac{a}{c} \le 2$)。

次に $a$ を動かす。($0 \le a \le 2c, a \ne c$) の時, $\frac{1}{2c} a$, $\frac{1}{2}\left|2 - \frac{a}{c}\right|$ のグラフは右図のようになり,

$$
\begin{align*}
\max S = 1 \text{ であり, この時}
\end{align*}
$$

$\triangle ABC$ は下図のようである。

\begin{tikzpicture}[scale=1.2, >=stealth]
  \begin{scope}[shift={(6,2.5)}, scale=0.9]
    \draw[->] (-0.3,0) -- (2.8,0) node[right] {$x$};
    \draw[->] (0,-0.3) -- (0,2.8) node[above] {$y$};
    \node[below left] at (0,0) {$O$};
    \draw[domain=0.4:2.6, smooth, variable=\x, thick, blue] plot ({\x}, {1/\x});
    \draw[thick, red] (-0.2, 2.2) -- (2.2, -0.2);
    \fill (1,1) circle (1.5pt) node[above right] {$C$};
    \fill (2,0) circle (1.5pt) node[below] {$P$};
    \fill (0,2) circle (1.5pt) node[left] {$Q$};
    \fill (0.6,0) circle (1.5pt) node[below] {$A$};
    \fill (0,1.4) circle (1.5pt) node[left] {$B$};
    \draw[dashed] (0.6,0) -- (1,1) -- (0,1.4) -- cycle;
  \end{scope}

  \begin{scope}[shift={(6,-2)}, scale=1.0]
    \draw[->] (-0.3,0) -- (2.6,0) node[right] {$a$};
    \draw[->] (0,-0.3) -- (0,1.5) node[above] {$y$};
    \node[below left] at (0,0) {$O$};
    \draw[thick] (0,0) -- (2,1) node[right] {$\frac{1}{2c}a$};
    \draw[thick] (0,1) -- (2,0) node[right] {$\frac{1}{2}\left(2-\frac{a}{c}\right)$};
    \draw[dashed] (1,0) node[below] {$c$} -- (1,0.5);
    \draw[dashed] (0,0.5) node[left] {$\frac{1}{2}$} -- (1,0.5);
    \fill (1,0.5) circle (1.5pt);
    \draw[dashed] (2,0) node[below] {$2c$} -- (2,1);
    \draw[dashed] (0,1) node[left] {$1$} -- (2,1);
  \end{scope}

  \begin{scope}[shift={(0,0)}, scale=1.1]
    \draw[->] (-0.3,0) -- (2.8,0) node[right] {$x$};
    \draw[->] (0,-0.3) -- (0,2.8) node[above] {$y$};
    \node[below left] at (0,0) {$O$};
    \begin{scope}
      \clip (0,0) -- (2.5,0) -- (2.5,2.5) -- (0,2.5) -- cycle;
      \fill[gray!20] (0,0) -- (0,2.5) -- plot[domain=0.4:2.5, smooth] ({\x},{1/\x}) -- (2.5,0) -- cycle;
    \end{scope}
    \draw[domain=0.4:2.5, smooth, variable=\x, thick] plot ({\x}, {1/\x});
    \fill (1,1) circle (1.5pt) node[above right] {$C$};
    \fill (2,0) circle (1.5pt) node[below] {$A$};
    \fill (0,0) circle (1.5pt) node[below left] {$B$};
    \draw[thick, blue] (2,0) -- (0,0) -- (1,1) -- cycle;
    \node[left] at (0,2) {$B'$};
    \node[below] at (0,0) {$A'$};
  \end{scope}
\end{tikzpicture}

[★以下, 解2]
$a$ を $0 \le a < c$, $a=c$, $c < a \le 2c$ で場合分けし, 各々の $\triangle ABC$ の高さの $\max$ をみる (以下略)。