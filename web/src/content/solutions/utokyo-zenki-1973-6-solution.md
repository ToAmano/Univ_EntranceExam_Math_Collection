---
university: "utokyo"
category: "zenki"
year: "1973"
question: "6"
type: "solution"
title: "UTOKYO 1973 zenki Q6 (solution)"
---

\input{macros}
\begin{oframed}
$x$のある$2$次関数のグラフが，原点において直線$y=x$に接するという．このグラフ上の点
$(u,v)$における接線の傾きを$u$，$v$で表せ．ただし$(u,v)$は原点ではないとする．
\end{oframed}

## 【解】

題意の放物線を$y=f(x)=ax^2+bx$とおく$(\because f(0)=0)$．ただし$a\not=0$である．
$f'(0)=1$だから$b=1$である．故に
     

$$
\begin{align*}
&f(x)=ax^2+x \\\therefore&f'(x)=2ax+1
\end{align*}
$$

となる．また$(u,v)$が放物線上にあることから$a=\dfrac{v-u}{u^2}$である．
故にグラフ上の点$(u,f(u))$での接線の傾きは
     

$$
\begin{align*}
f'(u)&=2ua+1 \\&=2u\frac{v-u}{u^2}+1 \\&=\frac{2v-u}{u}\dots\text{(答)}
\end{align*}
$$

である．