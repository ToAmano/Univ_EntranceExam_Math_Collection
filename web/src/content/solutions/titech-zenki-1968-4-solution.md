---
university: "titech"
category: "zenki"
year: "1968"
question: "4"
type: "solution"
title: "TITECH 1968 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

直線 $PQ$ を $l$ とする．$C = \cos\theta$, $S = \sin\theta$ とする．

$$
\begin{align*}
l : (S^2+C^2)(x-C^2) + (S^2-C^2)(y-C^2) &= 0 \\
x-C^2 + (S^2-C^2)y - C^2(S^2-C^2) &= 0
\end{align*}
$$

$t = C^2$ とする．

$$
\begin{align*}
x - t + (1-2t)y - t(1-2t) = 0
\end{align*}
$$

$(X, Y)$ を $l$ が通る時，

$$
\begin{align*}
X - t + Y(1-2t) + t(2t-1) = 0 \quad\cdots\text{①}
\end{align*}
$$

が $0 \le t \le 1$ に解を持つ．①の左辺を $f(t)$ とする．

$$
\begin{align*}
f(t) = 2t^2 + (-2-2Y)t + X+Y
\end{align*}
$$

である．

### $1^\circ \ [0, 1]$ に $1$ つだけ

$$
\begin{align*}
f(0)f(1) \le 0 \iff(X+Y)(X-Y) \le 0
\end{align*}
$$

### $2^\circ \ [0, 1]$ に $2$ つ（重解含む）

$$
\begin{align*}
\begin{cases}
\text{判: } (-1-Y)^2 - 2(X+Y) \ge 0 \\
\text{端: } f(0) \ge 0, f(1) \ge 0 \\
\text{軸: } 0 \le \frac{1+Y}{2} \le 1
\end{cases}\iff\begin{cases}
Y^2+1-2X \ge 0 \\
X+Y \ge 0 \\
X-Y \ge 0 \\
-1 \le Y \le 1
\end{cases}
\end{align*}
$$

したがって，$1^\circ, 2^\circ$ の和集合が求める領域で，図示して下図非斜線部（境界含む）．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1968/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $1^\circ$，$2^\circ$の和集合となる領域（非斜線部）</figcaption>
</figure>