---
university: "utokyo"
category: "kouki"
year: "1997"
question: "1"
type: "solution"
title: "UTOKYO 1997 kouki Q1 (solution)"
---

## 【解】

    (1)
    はじめの単位正三角形が一つの時，
    $n$ 回目に加えられる単位正三角形の数を $\alpha_n$ とおくと，
    

$$
\begin{align}
\alpha_n = 3n \label{1997-1:eq:1}
\end{align}
$$

    である．

    したがって$n$回目の操作で塗り潰されている正三角形の数は
    

$$
\begin{align*}
a_n
         & = 1 + \sum_{k=1}^{n}\alpha_{k}\\& = 1 + 3 \sum_{k=1}^{n} k        \\& = \frac{3}{2}n(n+1) + 1
\end{align*}
$$

    である．    $\cdots$(答)
    

    (2)
    まず自明な不等式
    

$$
\begin{align}
a_n \le b_n \label{1997-1:eq:2}
\end{align}
$$

    が成立する．
    次に十分大きな有限整数 $M$ があって，
    はじめに塗りつぶされている数が1つの状況からはじめて$M$回目の操作後に，
    はじめに塗りつぶされている数が2つ以上の場合の場合のはじめの単位正三角形が全てぬりつぶされているようにできる．
    この時
    

$$
\begin{align}
a_{n+M}\ge b_n \label{1997-1:eq:3}
\end{align}
$$

    が成立する．

    [(式3)](#1997-1:eq:2,1997-1:eq:3)から
    

$$
\begin{align}
& a_n \le b_n \le a_{n+M}\\\therefore& 1 \ge\frac{a_n}{b_n}\ge\frac{a_n}{a_{n+M}}\label{1997-1:eq:4}
\end{align}
$$

    である．

    右辺の$n\to\infty$での極限値は(1)の結果を代入して
    

$$
\begin{align*}
\lim_{n\to\infty}\frac{a_n}{a_{n+M}}& = \lim_{n\to\infty}\frac{\frac{3}{2}n(n+1)+1}{\frac{3}{2}(n+M)(n+M+1)+1}\\& = \lim_{n\to\infty} frac{1(1+\frac{1}{n})+\frac{1}{n^2}}{(1+\frac{M}{n})(1+\frac{M+1}{n})+\frac{2}{3n^2}}\\& = 1
\end{align*}
$$

    だから，[(式4)](#1997-1:eq:4)と挟み撃ちの定理より
    

$$
\begin{align*}
\lim_{n\to\infty}\frac{a_n}{b_n} = 1
\end{align*}
$$

    である．$\cdots$(答)

    vspace{10pt}

        

## 【解説】