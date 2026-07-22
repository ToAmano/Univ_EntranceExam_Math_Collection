---
university: "utokyo"
category: "zenki"
year: "1995"
question: "2"
type: "solution"
title: "UTOKYO 1995 zenki Q2 (solution)"
---

\input{macros}
\begin{oframed}
$f(x)=1-\sin x$に対し，$g(x)=\int_0^x(x-t)f(t)dt$ とおく．このとき,任意の実数$x$，$y$について
\[g(x+y)+g(x-y)\ge 2g(x)\]
が成り立つことを示せ．
\end{oframed}

## 【解】

与式を変形して
     

$$
\begin{align*}
g(x)=x\int_0^xf(t)dt-\int_0^xtf(t)dt
\end{align*}
$$

だから
     

$$
\begin{align*}
g'(x)&=\int_0^xf(t)dt+xf(x)-tf(t) \\&=\int_0^xf(t)dt \\\therefore g''(x)&=f(t)\ge0 \\
\end{align*}
$$

したがって，$g(x)$は下に凸な関数であるから，凸不等式から
     

$$
\begin{align*}
g(x+y)+g(x-y)\ge 2g(x)
\end{align*}
$$

となる．