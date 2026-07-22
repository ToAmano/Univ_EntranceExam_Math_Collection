---
university: "todai"
category: "zenki"
year: "1967"
question: "5"
type: "solution"
title: "TODAI 1967 zenki Q5 (solution)"
---

\input{macros}
     \begin{oframed}
     $y=ax^2$のグラフが$y=\log x$のグラフに接するように定数$a$の値を求めよ．
     なお，このときこれらのグラフと$x$軸とで囲まれる図形の面積を求めよ．
     \end{oframed}

## 【解】

$x=t(t>0)$で接するとすると，$(ax^2)'=2ax$，$(\log x)'=\dfrac{1}{x}$故
     

$$
\begin{align}
\left\{\begin{array}{l}
          at^2=\log t  \\
          2at=\dfrac{1}{t}
          \end{array}\right.\Longleftrightarrow
     at^2=\log t=\frac{1}{2}\nonumber\\\Longleftrightarrow\left\{\begin{array}{l}
          t=\sqrt{e}
          a=\dfrac{1}{2e}
          \end{array}\right.\label{1}
\end{align}
$$

故に$a=\dfrac{1}{2e}$である．$\cdots$(答)　
 \\ \\
このとき，求める面積$S$は
     

$$
\begin{align*}
S&=\int_0^t(ax^2)dx-\int_1^t\log xdx \\&=\left[\frac{a}{3}x^3\right]_0^t-\left[x(\log x-1)\right]_1^t  \\&=\frac{at^3}{3}-t(\log t-1)-1  \\&=\frac{1}{6}\sqrt{e}+\frac{1}{2}\sqrt{e}-1 \tag{\because[1](#1)}\\&=\frac{2}{3}\sqrt{e}-1\cdots\text{(答)}
\end{align*}
$$

である．