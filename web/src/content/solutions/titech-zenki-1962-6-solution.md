---
university: "titech"
category: "zenki"
year: "1962"
question: "6"
type: "solution"
title: "TITECH 1962 zenki Q6 (solution)"
---

{\bf[解］}

以下$a<x<b$で考える．簡単のため

$$
\begin{align}
h(x) = \frac{f(x) - f(a)}{x - a}
\end{align}
$$

とおくと，この区間で$h'(x)>0$であることを示せば良い．

さて，平均値の定理から$h(x) = f'(c)$ なる $c$ が $a < c < x$ に存在する．
これに注意して$a < x < b$ のとき，

$$
\begin{align*}
h'(x) 
  &= f'(x)(x-a) - \left[f(x) - f(a)\right]\\&= \left(x-a\right)\left[f'(x)-\frac{f(x) - f(a)}{x - a}\right]\\&= \left(x-a\right)\left[f'(x)-f'(c)\right]
\end{align*}
$$

と変形できる．ただし最後の行で平均値の定理を利用した．
ここで題意より$f''(x) > 0$ だから $f'(x)$ は単調増加である．
従って$f'(x)-f'(c)>0$だから，

$$
\begin{align}
h'(x)>0
\end{align}
$$

である．よって$h(x)$は単調増加であり，題意は示された．
]}