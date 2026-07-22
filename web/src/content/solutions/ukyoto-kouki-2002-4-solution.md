---
university: "ukyoto"
category: "kouki"
year: "2002"
question: "4"
type: "solution"
title: "UKYOTO 2002 kouki Q4 (solution)"
---

## 【解】

    $x^n$ の係数が$1$である$n$次式を $f_n(x)$ と表す．

    

    $1^\circ n=1$ の時

    $f_1(x) = x+a$ とおけるから，$f_1(q_1) = q_1+a \in \mathbb{Q}$ ならば $a \in \mathbb{Q}$ であるから，
    条件は成立．

    

    $2^\circ n=k$ の時の成立を仮定する ($k \in \mathbb{N}$)

    異なる有理数 $q_1,q_2,\cdots, q_{k+1}$ に対し
    

$$
\begin{align*}
f_k(q_i) = r_i \quad(i=1, 2, \dots, k)
\end{align*}
$$

    と仮定する．ここで $r_i \in \mathbb{Q}$ である．
    すると，$f_{k+1}(r_{l+1})=r_{k*1}$より，因数定理から
    

$$
\begin{align}
f_{k+1}(x) = (x-q_{k+1})f_k(x) + r_{k+1}\label{2002-4:eq:1}
\end{align}
$$

    とおける．ここで最高次の係数比較より，右辺の$f_k$もまた最高次の係数$1$である．
    $x=r_i\, (i=1,2,\cdots,k)$ を代入して
    

$$
\begin{align*}
r_i - r_{k+1} = (q_i - q_{k+1}) f_{k}(q_i)
\end{align*}
$$

    を得る．題意より$q_{i} \neq q_{k+1}\, (i=1, 2, \dots, k)$だから
    両辺$q_i - q_{k+1}$で割れて，
    

$$
\begin{align*}
f_{k}(q_i) = \frac{r_i - r_{k+1}}{q_i - q_{k+1}}\in\mathbb{Q}
\end{align*}
$$

    となる．右辺は有理数だから，左辺も有理数である．
    従って$n=k$での仮定から，左辺の$k$次式$f_{k}$の係数は全て有理数である．
    従って，[(式1)](#2002-4:eq:1)から$f_{k+1}(x)$の係数も全て有理数である．
    従って$n=k+1$でも題意は成立．

    

    以上二つから，数学的帰納法により題意は示された．
    $\cdots$(答)
    

## 【解説】