---
university: "titech"
category: "zenki"
year: "1966"
question: "1"
type: "solution"
title: "TITECH 1966 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 題意の円を $C$ とおく．

$$
\begin{align*}
C \equiv(x-2)^2+(y+1)^2=4
\end{align*}
$$

から, $O(2, -1), \, r=2$ である．そこで,

$$
\begin{align*}
\vec{OP} = \begin{pmatrix} x-2 \\ y+1 \end{pmatrix}
\end{align*}
$$

だから, $\vec{OQ} = k\vec{OP} \quad (k>0)$ とおけることより,

$$
\begin{align*}
|\vec{OP}| \cdot |\vec{OQ}| = k \{(x-2)^2+(y+1)^2 \} = 4 \quad(\because\text{題意})
\end{align*}
$$

$O \ne P$ から

$$
\begin{align*}
k = \frac{4}{(x-2)^2+(y+1)^2}
\end{align*}
$$

だから,

$$
\begin{align*}
\vec{OQ} = \begin{pmatrix} X-2 \\ Y+1 \end{pmatrix} = \frac{4}{(x-2)^2+(y+1)^2}\begin{pmatrix} x-2 \\ y+1 \end{pmatrix}
\end{align*}
$$

である．成分を比較して

$$
\begin{align*}
\begin{cases}
X = \dfrac{4(x-2)}{(x-2)^2+(y+1)^2} + 2 \\[10pt]
Y = \dfrac{4(y+1)}{(x-2)^2+(y+1)^2} - 1
\end{cases}\quad\text{(1)}
\end{align*}
$$

(2) $x \in \mathbb{R}, \, y=0$ だから, (1) より

$$
\begin{align*}
\begin{cases}
X-2 = \dfrac{4(x-2)}{(x-2)^2+1} \\[10pt]
Y+1 = \dfrac{4}{(x-2)^2+1}
\end{cases}\quad\dots(*)
\end{align*}
$$

$Y \ne -1$ だから (第2式より), 第2式を変形して,

$$
\begin{align*}
(x-2)^2+1 = \frac{4}{Y+1}
\end{align*}
$$

第1式に代入して,

$$
\begin{align*}
X-2 = (Y+1)(x-2)
\end{align*}
$$

$$
\begin{align*}
\therefore x-2 = \frac{X-2}{Y+1}\quad(\because Y \ne -1)
\end{align*}
$$

だから, $(*)$ に代入して

$$
\begin{align*}
Y+1 = \frac{4}{\left( \dfrac{X-2}{Y+1} \right)^2 + 1}
\end{align*}
$$

$$
\begin{align*}
\therefore(X-2)^2 + (Y+1)^2 = 4(Y+1) \quad(\because Y \ne -1)
\end{align*}
$$

$$
\begin{align*}
(X-2)^2 + (Y-1)^2 = 4 \quad\dots\text{①}
\end{align*}
$$

又, $(*)$ 及び $x \in \mathbb{R}$ から,

$$
\begin{align*}
0 < Y+1 \le 4 \quad\therefore -1 < Y \le 3
\end{align*}
$$

に注意して, $(X, Y) \ne (2, -1)$ である．以上から

$$
\begin{align*}
(X-2)^2 + (Y-1)^2 = 4 \quad((X, Y)=(2, -1) \text{を除く})
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1966/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点$(X,Y)$の軌跡（円）の図示</figcaption>
</figure>