---
university: "titech"
category: "zenki"
year: "1972"
question: "4"
type: "solution"
title: "TITECH 1972 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$f'(x)>0$ から $f(x)$ は単調増加であるから，

$$
\begin{align*}
F(x) = \int_a^x [f(x)-f(t)]dt + \int_x^b[f(t)-f(x)]dt
\end{align*}
$$

$$
\begin{align*}
= f(x)\int_a^x dt - \int_a^x f(t)dt + \int_x^b f(t)dt - f(x)\int_x^b dt
\end{align*}
$$

$$
\begin{align*}
F'(x) = f'(x)(x-a) + f(x) - f(x) - f(x) - f'(x)(b-x) + f(x)
\end{align*}
$$

$$
\begin{align*}
= f'(x)(2x-a-b)
\end{align*}
$$

$f'(x)>0$ から下記のようになる．

| $x$  | $a$ |     $\dfrac{a+b}{2}$     |     | $b$ |
|:------:|:-----:|:--------------------------:|:---:|:-----:|
| $F'$ |       |     $-$ $0$ $+$      |     |       |
| $F$  |       | $\searrow$  $\nearrow$ |     |       |

よって，$x=\dfrac{a+b}{2}$ で最小となる．