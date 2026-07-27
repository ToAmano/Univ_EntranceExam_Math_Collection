---
university: "utokyo"
category: "zenki"
year: "1967"
question: "2"
type: "solution"
title: "UTOKYO 1967 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] 題意の“ある時刻”に自動車が原点にいるとし、自動車は $x$ 軸正方向へ動くものとする。また飛行機は平面 $z=k\ \text{[km]}\ (>0)$ 上をとるとする。

$$
\begin{align*}
\begin{cases}
A \cdots \text{“ある時刻”における飛行機の座標。} yz \text{平面上にとる。} \\
B \cdots 36 \text{秒後の} \qquad \qquad \text{〃} \\
C \cdots \qquad \quad \text{〃} \quad \text{自動車の座標}
\end{cases}
\end{align*}
$$

とする。また点 $X$ に対し、$X$ の $xy$ 平面への正射影を $X'$ で表す。

まず $\angle A O A' = 30^\circ$ から、$A(0, \sqrt{3}k, k)$ である。

時速 $100\ \text{[km]} = \frac{10^5}{36}\ \text{[m/s]}$ ； $\sqrt{7} \times 100\ \text{[km/h]} = \frac{\sqrt{7} \cdot 10^5}{36}\ \text{[m/s]}$

だから、$C(1, 0, 0)$ となる。題意から、

$$
\begin{align*}
B\left( 1 + \frac{3}{2}k, \frac{\sqrt{3}}{2}k, k \right)
\end{align*}
$$

である。したがって、

$$
\begin{align*}
\vec{AB} = \begin{pmatrix} 1 + \frac{3}{2}k \\ -\frac{\sqrt{3}}{2}k \\ 0 \end{pmatrix}
\end{align*}
$$

となる。$|\vec{AB}| = \sqrt{7}\ \text{[km]}$ だから、2乗して整理して、

$$
\begin{align*}
7 &= \left(1 + \frac{3}{2}k\right)^2 + \left(\frac{\sqrt{3}}{2}k\right)^2 \\&= 3k^2 + 3k + 1
\end{align*}
$$

$$
\begin{align*}
\therefore k = 1\ (>0)\ \text{[km]}
\end{align*}
$$

したがって、求める高度は $k = 1000\ \text{[m]}$ である。

\begin{tikzpicture}[scale=1.2, >=stealth]
  \draw[->] (0,0,0) -- (2.5,0,0) node[below left] {$x$};
  \draw[->] (0,0,0) -- (0,3.5,0) node[right] {$y$};
  \draw[->] (0,0,0) -- (0,0,3) node[above] {$z$};

  \coordinate (O) at (0,0,0);
  \coordinate (Ap) at (0, 1.732, 0);
  \coordinate (A) at (0, 1.732, 1.5);
  \coordinate (Bp) at (1.2, 0.866, 0);
  \coordinate (B) at (1.2, 0.866, 1.5);
  \coordinate (C) at (1.0, 0, 0);

  \draw[dashed] (O) -- (Ap);
  \draw[dashed] (Ap) -- (A);
  \draw[thick] (O) -- (A);
  \draw[dashed] (Bp) -- (B);
  \draw[thick] (A) -- (B);
  \draw[dashed] (Ap) -- (Bp);
  \draw[fill] (C) circle (1.5pt) node[below] {$C$};

  \node[right] at (A) {$A$};
  \node[right] at (Ap) {$A'$};
  \node[above] at (B) {$B$};
  \node[below] at (Bp) {$B'$};
  \node[left] at (0, 1.732, 0.75) {$k$};
  \node[right] at (0, 2.3, 0) {$\sqrt{3}k$};

  \draw (0,0.4,0) arc (90:60:0.4);
  \node at (0.2,0.5,0) {$30^\circ$};

  \draw (0.3, 0, 0) arc (0:30:0.4);
  \node at (0.5, 0.2, 0) {$30^\circ$};
\end{tikzpicture}