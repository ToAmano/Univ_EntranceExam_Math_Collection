---
university: "titech"
category: "zenki"
year: "1967"
question: "2"
type: "solution"
title: "TITECH 1967 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 直線を $l : y = m(x-2) + 1$ とおく. ($m \in \mathbb{R}$, $\because l$ は$y$軸平行でない) この時, $l$と楕円の交点の$x$座標は

$$
\begin{align*}
3x^2 + 2 \{ m(x-2) + 1 \}^2 = 6
\end{align*}
$$

$$
\begin{align*}
\therefore(2m^2+3)x^2 + 4m(1-2m)x + 4(2m^2-2m-1) = 0 \quad\dots\text{①}
\end{align*}
$$

の実解で与えられる. ①の判別式 $D$ として, ①が $x$ について2実解を持つ条件は,

$$
\begin{align*}
D > 0 \iff\{ 2m(1-2m) \}^2 - (2m^2+3) \{ 2(4m^2-4m-2) \} > 0
\end{align*}
$$

$$
\begin{align*}
\iff -m^2+2m+1 > 0 \iff 1-\sqrt{2} < m < 1+\sqrt{2}\quad\dots\text{②}
\end{align*}
$$

このもとで, ①の2異実解 $\alpha, \beta \; (\alpha < \beta)$ とすると, $|\text{PQ}|, |\text{PR}|$ は,

$$
\begin{align*}
\sqrt{1+m^2}|\alpha-2|, \quad\sqrt{1+m^2}|\beta-2|
\end{align*}
$$

で与えられるから, $I = |\text{PQ}| \cdot |\text{PR}|$ として, ①の左辺 $f(x)$ とすると,

$$
\begin{align*}
I &= (1+m^2)|\alpha-2||\beta-2| \\&= (1+m^2)\left|\frac{f(2)}{2m^2+3}\right|\\&= \frac{1+m^2}{2m^2+3}\cdot 8 \\&= 4 \left( 1 - \frac{1}{2m^2+3}\right)\quad\dots\text{③}
\end{align*}
$$

となる. ここで, ②から, $0 \leqq m^2 < 3+2\sqrt{2}$ だから,

$$
\begin{align*}
3 \leqq 2m^2+3 < 9+4\sqrt{2}
\end{align*}
$$

$$
\begin{align*}
\therefore\frac{1}{9+4\sqrt{2}} < \frac{1}{2m^2+3}\leqq\frac{1}{3}
\end{align*}
$$

$$
\begin{align*}
\therefore\frac{9-4\sqrt{2}}{49} < \frac{1}{2m^2+3}\leqq\frac{1}{3}
\end{align*}
$$

③に代入して,

$$
\begin{align*}
\frac{8}{3}\leqq I < \frac{16}{49}(10+\sqrt{2})
\end{align*}
$$