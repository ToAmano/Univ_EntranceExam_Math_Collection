---
university: "ukyoto"
category: "kouki"
year: "1993"
question: "6"
type: "solution"
title: "UKYOTO 1993 kouki Q6 (solution)"
---

## 【解】

  与えられた不等式を通分すると
  

$$
\begin{align}
\frac{(a_1 x + b_1)(x + c_2) - (a_2 x + b_2)(x + c_1)}{(x + c_1)(x + c_2)} > 0 \label{1993-6:eq:1}
\end{align}
$$

  である．これが$x\neq -c_1,-c_2$で常に成り立つような条件を考える．
  この分子を $f(x)$ とおくと，
  

$$
\begin{align}
f(x) = (a_1 - a_2)x^2 + (a_1 c_2 + b_1 - b_2 - a_2 c_1)x + b_1 c_2 - b_2 c_1
\end{align}
$$

  であり，これは$x$の二次以下の式である．
  まず，$a_1-a_2=0$の時は$f(x)$は一次式となり，[(式1)](#1993-6:eq:1)が成り立たない$x$が必ず存在するから，
  

$$
\begin{align}
a_1-a_2 \neq 0\label{1993-6:eq:3}
\end{align}
$$

  であることが必要．
  この元で，[(式1)](#1993-6:eq:1)は分母分子ともに二次式であり，さらに分母が$x=-c_1,-c_2$を根をもつ．
  よって[(式1)](#1993-6:eq:1)が$x\neq -c_1,-c_2$の全ての実数$x$で成り立つには，
  分子の二次係数が正であり，かつ分子が分母の定数倍になっていなければならない．
  

$$
\begin{align*}
\begin{dcases}
      a_1-a_2 > 0 \\
      f(x) = (a_1-a_2)(x+c_1)(c_2)
    \end{dcases}
\end{align*}
$$

  $f(x)$の一次と零次の係数比較すると
  

$$
\begin{align*}
\begin{dcases}
      a_1 c_2 + b_1 - b_2 - a_2 c_1 & = (a_1 - a_2)(c_1 + c_2) \\
      b_1 c_2 - b_2 c_1             & = (a_1 - a_2)c_1 c_2
    \end{dcases}
\end{align*}
$$

  整理すると，
  

$$
\begin{align}
& \begin{dcases}
         a_1 c_1 + a_2 c_2 = b_1 - b_2 \\
         (a_1 - a_2)c_1 c_2 = b_1 c_2 - b_2 c_1
       \end{dcases}& \begin{dcases}
         b_1 - a_1 c_1 = b_2 - a_2 c_2 \\
         c_1(b_2 - a_2 c_2) = c_2(b_1 - a_1 c_1)
       \end{dcases}\label{1993-6:eq:2}
\end{align}
$$

  となる．
  [(式2)](#1993-6:eq:2)を$c_1 = c_2$ か否かで場合分けすると，

  **1$^\circ$ $c_1 = c_2$の時**
  

$$
\begin{align*}
b_2 - a_2 c_2 = b_1 - a_1 c_1
\end{align*}
$$

  が求める条件となる．

  **2$^\circ$ $c_1 \ne c_2$の時**
  

$$
\begin{align*}
b_2 - a_2 c_2 = b_1 - a_1 c_1 = 0
\end{align*}
$$

  が求める条件となる．

  以上から，題意が成立する条件は[(式3)](#1993-6:eq:3)と合わせて，
  

$$
\begin{align*}
c_1 = c_2 \land b_2 - a_2 c_2 = b_1 - a_1 c_1 \land a_1 > a_2
\end{align*}
$$

  又は
  

$$
\begin{align*}
c_1 \ne c_2 \land b_2 = a_2 c_2 \land b_1 = a_1 c_1 \land a_1 > a_2
\end{align*}
$$

  である．  $\cdots$(答)

  

## 【解説】