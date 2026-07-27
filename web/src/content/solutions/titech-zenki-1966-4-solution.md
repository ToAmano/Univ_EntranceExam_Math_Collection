---
university: "titech"
category: "zenki"
year: "1966"
question: "4"
type: "solution"
title: "TITECH 1966 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $f(x) = x^2+ax+b, \, g(x) = x^2+cx+d$ とおく．共通接線を $l : y = h(x)$ とすると,

$$
\begin{align*}
\begin{cases}
f(x) - h(x) = (x-p)^2 \\[5pt]
g(x) - h(x) = (x-q)^2
\end{cases}\quad\dots\text{①}
\end{align*}
$$

だから, 辺々引いて,

$$
\begin{align*}
f(x) - g(x) = (x-p)^2 - (x-q)^2 = (2x - p - q)(q - p)
\end{align*}
$$

となり, $y = f(x)$ と $y = g(x)$ の交点の $x$ 座標は $x = \dfrac{p+q}{2}$ である．

したがって, 求める面積 $S$ として ①から, $p < q$ の時

$$
\begin{align*}
\begin{aligned}
S &= \int_p^{\frac{p+q}{2}} (x-p)^2 dx + \int_{\frac{p+q}{2}}^q (x-q)^2 dx \\[10pt]
&= \frac{1}{12}(q-p)^3
\end{aligned}
\end{align*}
$$

$q < p$ の時もかんがえて, $S = \dfrac{1}{12}|q-p|^3$