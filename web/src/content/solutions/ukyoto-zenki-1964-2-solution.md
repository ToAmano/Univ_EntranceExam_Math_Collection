---
university: "ukyoto"
category: "zenki"
year: "1964"
question: "2"
type: "solution"
title: "UKYOTO 1964 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (i), (ii) から、3つの組を $f(x), g(x), h(x)$ として、

$$
\begin{align*}
\begin{cases}
f(x) = (x+3) f'(x) \\
g(x) = (x+3) g'(x) \\
h(x) = (x+3) h'(x)
\end{cases}
\quad (f', g', h' \text{はいずれも最高次係数1の2次式})
\end{align*}
$$

とおける。さて、(iii) の式を $t(x)$ とおくと

$$
\begin{align*}
\begin{aligned}
t(x) &= (x-1)(x^4 + 2x^3 - 39x^2 - 72x + 108) \\
&= (x-1)^2 (x^3 + 3x^2 - 36x - 108) \\
&= (x-1)^2 (x+3)(x^2 - 36) \\
&= (x-1)^2 (x+3)(x+6)(x-6)
\end{aligned}
\end{align*}
$$

だから、これらの項を $f', g', h'$ に、$(x+3)$ 以外全てに共通な項がないようにふりわけれはよい。解答のため

$$
\begin{align*}
\begin{cases}
A = x-1 \\
B = x+6 \\
C = x-6
\end{cases}
\end{align*}
$$

とおく。まず、$A^2$ が $t(x)$ に含まれることと、$f', g', h'$ が2次式であることから、このうちのいずれかが $A^2$ と等しい。対称性から、$f' = A^2$ の1つとする。以下 $g', h'$ を決める。対称性に注意し、他は多くても1つしか $g', h'$ に入らないことと、全てに共通な因数がないこと、この2つも異なることから

$$
\begin{align*}
(g', h') = (BC, AB), \ (BC, AC)
\end{align*}
$$

の2つ。

以上から、求める組は

$$
\begin{align*}
\begin{aligned}
&\left( (x+3)(x-1)^2, \ (x+3)(x-1)(x+6), \ (x+3)(x+6)(x-6) \right), \\
&\left( (x+3)(x-1)^2, \ (x+3)(x-1)(x-6), \ (x+3)(x+6)(x-6) \right)
\end{aligned}
\end{align*}
$$

**[本時のミス]**\\
数えあげの予期病 $\implies$ 必ず条件として照らしあわせて確認