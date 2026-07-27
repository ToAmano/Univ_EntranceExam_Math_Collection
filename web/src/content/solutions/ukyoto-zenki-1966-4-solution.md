---
university: "ukyoto"
category: "zenki"
year: "1966"
question: "4"
type: "solution"
title: "UKYOTO 1966 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] 右図のような座標平面を考える。

\begin{tikzpicture}[scale=1.5]
    \draw[->] (-0.5,0) -- (3,0) node[below]{$x$};
    \draw[->] (0,-1) -- (0,1.5) node[left]{$y$};
    \fill (0,0) circle (1.5pt) node[below left]{$A$};
    \fill (1.5,0) circle (1.5pt) node[below]{$B$};
    \node at (0.75,-0.15) {$a$};
    \draw[domain=0:2.5,smooth,variable=\x,thick] plot ({\x}, {-0.4*sin(\x*180)});
\end{tikzpicture}

すると $0 \le \theta < 2\pi$ として

$$
\begin{align*}
\vec{AP} = \begin{pmatrix} \cos 2\theta \\ \sin 2\theta \end{pmatrix}, \quad
\vec{AQ} = \begin{pmatrix} a \\ 0 \end{pmatrix} + \begin{pmatrix} \cos(-\theta) \\ \sin(-\theta) \end{pmatrix}
\end{align*}
$$

とおけるから

$$
\begin{align*}
\vec{PQ} = \begin{pmatrix} a + \cos\theta - \cos 2\theta \\ -\sin\theta - \sin 2\theta \end{pmatrix}
\end{align*}
$$

$|\vec{PQ}| \ge 0$ から、$|\vec{PQ}|^2$ が最大の時、$|\vec{PQ}|$ も最大。以下 $\cos\theta = c, \sin\theta = s$ と略記して、

$$
\begin{align*}
|\vec{PQ}|^2 &= \{ a + c - (2c^2 - 1) \}^2 + (-s - 2cs)^2 \\&= (-2c^2 + c + a + 1)^2 + s^2(1 + 2c)^2 \\&= 4c^4 - 4c^3 - (4a + 3)c^2 + 2(a + 1)c + (a + 1)^2 + (1 - c^2)(4c^2 + 4c + 1) \\&= -4ac^2 + 2(a - 1)c + (a^2 + 2a + 2) \equiv f(c)
\end{align*}
$$

以下 $f(c)$ の最大値を求める。$a > 0$ に注意して、軸の大きさで場合分けする。

\begin{tikzpicture}[scale=1.5]
    \draw[->] (-1.2,0) -- (1.5,0) node[right]{$c$};
    \draw[->] (0,-0.5) -- (0,1.5);
    \draw (-1, -0.05) -- (-1, 0.05) node[above]{$-1$};
    \draw (1, -0.05) -- (1, 0.05) node[above]{$1$};
    \draw[dashed] (0.3,-0.3) -- (0.3,1.2) node[above]{軸 $c = \frac{a-1}{4a}$};
    \draw[thick, domain=-1:1] plot ({\x}, {-0.8*(\x-0.3)*(\x-0.3) + 1});
\end{tikzpicture}

1.  $0 < a \le \frac{1}{5}$ の時
    

$$
\begin{align*}
\max f(c) = f(-1) = (a - 2)^2
\end{align*}
$$

2.  $\frac{1}{5} \le a$ の時
    

$$
\begin{align*}
\max f(c) = f\left(\frac{a-1}{4a}\right) = a^2 + \frac{9}{4}a + \frac{3}{2} + \frac{1}{4a}
\end{align*}
$$

以上から、

$$
\begin{align*}
\begin{cases}
0 < a \le \frac{1}{5} \text{の時} & 2 - a \\
\frac{1}{5} \le a \text{の時} & \sqrt{a^2 + \frac{9}{4}a + \frac{3}{2} + \frac{1}{4a}}
\end{cases}
\end{align*}
$$