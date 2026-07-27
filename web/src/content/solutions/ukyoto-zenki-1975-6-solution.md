---
university: "ukyoto"
category: "zenki"
year: "1975"
question: "6"
type: "solution"
title: "UKYOTO 1975 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $A$ を原点、$B(2,0), C(0,2)$ とする $xy$ 平面で考える。又、$O(t,t)\ (0 < t)$ とおき題意の円を $T$ とおく。

$$
\begin{align*}
T : (x-t)^2 + (y-t)^2 = 1
\end{align*}
$$

$$
\begin{align*}
BC : x+y = 2
\end{align*}
$$

\begin{tikzpicture}[scale=1.5]
    \draw[thick] (0,2) node[above left]{$C$} -- (0,0) node[below left]{$A$} -- (2,0) node[below right]{$B$} -- cycle;
    \draw (0,0) -- (0,0.15) -- (0.15,0.15) -- (0.15,0);
    \coordinate (O) at (0.6,0.6);
    \draw (O) circle (0.5);
    \fill (O) circle (1.2pt) node[below left]{$O$};
    \draw[dashed] (O) -- (1.0,1.0) node[above right]{$H$};
    \node at (0.3,-0.2) {$t$};
    \node at (1.0,-0.2) {$2$};
    \node at (-0.2,1.0) {$2$};
\end{tikzpicture}

1.  $T$ と $x$ 軸の交点は $x^2 - 2tx + 2t^2 - 1 = 0$ の2実解\\
    $T$ と $y$ 軸の交点は $y^2 - 2ty + 2t^2 - 1 = 0$ の2実解\\
    $T$ と $BC$ の交点は $2x^2 - 4x + 2t^2 - 4t + 3 = 0$ の2実解\\
    だからこれらが $0 \le x \le 2, 0 \le y \le 2$ に2実解を持つ条件を考えて、

    

$$
\begin{align*}
&\begin{cases}
    \text{軸}: 0 < t < 2 \\
    \text{端}: 2t^2 - 1 \ge 0, \ 2t^2 - 4t + 3 \ge 0 \\
    \text{判}: t^2 - (2t^2 - 1) > 0
    \end{cases}\quad\wedge\quad\begin{cases}
    \text{軸}: 0 < 1 < 2 \\
    \text{端}: 2t^2 - 4t + 3 \ge 0, \ 2t^2 - 4t + 3 \ge 0 \\
    \text{判}: 4 - 2(2t^2 - 4t + 3) > 0
    \end{cases}\\&\iff\begin{cases}
    0 < t < 2 \\
    \frac{\sqrt{2}}{2} \le t < 1
    \end{cases}\quad\wedge\quad
    2 - \sqrt{2} < t < 2 + \sqrt{2}\\&\iff\frac{\sqrt{2}}{2}\le t < 1
\end{align*}
$$

    よって、$x = 1/t$ だから、$1 \le x < \sqrt{2}$。

2.  (i)の時、$T$ の中心と $x, y$ 軸、$BC$ との距離は各々
    

$$
\begin{align*}
t, \quad t, \quad |\sqrt{2} - \sqrt{2}t|
\end{align*}
$$

    だから、$F(t)$ が右図斜線部の面積を表すことから、

    
    \begin{tikzpicture}[scale=1.2]
        \draw (0,0) circle (1);
        \draw (-1.3,0) -- (1.3,0);
        \draw (0,-1.3) -- (0,1.3);
        \draw[thick] (0.5,-0.866) -- (0.5,0.866);
        \fill[gray!40] (0.5,-0.866) arc (-60:60:1) -- cycle;
        \draw (0.5,-0.866) -- (0.5,0.866);
        \node[below right] at (0.5,0) {$t\ (= \frac{1}{x})$};
    \end{tikzpicture}
    

    

$$
\begin{align*}
S = \pi - 2F\left(\frac{1}{x}\right) - F(\sqrt{2} - x)
\end{align*}
$$

3.  (ii)から
    

$$
\begin{align*}
\frac{dS}{dx}&= +4 \sqrt{1 - \frac{1}{x^2}}\cdot\frac{1}{x^2} - 2\sqrt{1 - (\sqrt{2}-x)^2}\\&= 2 \left[\sqrt{2 - x^2} - \sqrt{1 - (\sqrt{2}-x)^2}\right]\\&= 2 \frac{-2\sqrt{2}x + 3}{\sqrt{2-x^2} + \sqrt{1 - (\sqrt{2}-x)^2}}
\end{align*}
$$

    から下表を得る。

    
    

| $x$  | $1$ |  $\dots$   | $\frac{3}{4}\sqrt{2}$ |  $\dots$   | $\sqrt{2}$ |
|:------:|:-----:|:------------:|:-----------------------:|:------------:|:------------:|
| $S'$ |       |    $+$     |          $0$          |    $-$     |              |
| $S$  |       | $\nearrow$ |                         | $\searrow$ |              |

    

    よって、$x = \frac{3}{4}\sqrt{2}$ で $S$ は最大。