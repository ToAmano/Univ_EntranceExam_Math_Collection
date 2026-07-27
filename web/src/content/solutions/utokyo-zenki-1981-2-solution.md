---
university: "utokyo"
category: "zenki"
year: "1981"
question: "2"
type: "solution"
title: "UTOKYO 1981 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 正六角形の一辺の長さは $1$ であり, 三角形ができる時, その面積は

1.  $A_1 A_2 A_6$ 形 $\dots \frac{\sqrt{3}}{4}$

2.  $A_1 A_2 A_5$ 形 $\dots \frac{\sqrt{3}}{2}$

3.  $A_1 A_3 A_5$ 形 $\dots \frac{3}{4}\sqrt{3}$

のいずれかである。$3$ つの頂点のえらび方 $6^3$ 通りが同様にたしからしい。以下, $1$ つ目に $A_1$ がえらばれたとして

$1^\circ$ の時
\begin{quote}
どの点が頂点になるかで $2 \times 3 = 6$ 通り
\end{quote}

$2^\circ$ の時
\begin{quote}
$1$ つの頂点に対し, のこりの頂点が $2$ 通りあるから

$$
\begin{align*}
4 \times 2 + 2 \times 2 = 12 \text{ 通り}
\end{align*}
$$

\end{quote}

$3^\circ$ の時
\begin{quote}
$2$ 通り
\end{quote}

だから, これらの $6$ 倍ずつえらび方があるので, もとめる期待値として

$$
\begin{align*}
E = \frac{6}{36} \cdot \frac{\sqrt{3}}{4} + \frac{12}{36} \cdot \frac{\sqrt{3}}{2} + \frac{2}{36} \cdot \frac{3}{4}\sqrt{3}
\end{align*}
$$

$$
\begin{align*}
= \frac{\sqrt{3}}{36} \left( \frac{3}{2} + 6 + \frac{3}{2} \right)
\end{align*}
$$

$$
\begin{align*}
= \frac{\sqrt{3}}{4}
\end{align*}
$$

\begin{tikzpicture}[scale=1.5]
  \coordinate (A1) at (90:1.8);
  \coordinate (A2) at (30:1.8);
  \coordinate (A3) at (-30:1.8);
  \coordinate (A4) at (-90:1.8);
  \coordinate (A5) at (-150:1.8);
  \coordinate (A6) at (150:1.8);

  \draw (A1) -- (A2) -- (A3) -- (A4) -- (A5) -- (A6) -- cycle;

  \draw[dashed] (A1) -- (A3);
  \draw[dashed] (A1) -- (A4);
  \draw[dashed] (A1) -- (A5);

  \node[above] at (A1) {$A_1$};
  \node[above right] at (A2) {$A_2$};
  \node[right] at (A3) {$A_3$};
  \node[below] at (A4) {$A_4$};
  \node[left] at (A5) {$A_5$};
\end{tikzpicture}