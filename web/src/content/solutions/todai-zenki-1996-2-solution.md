---
university: "todai"
category: "zenki"
year: "1996"
question: "2"
type: "solution"
title: "TODAI 1996 zenki Q2 (solution)"
---

\input{macros}
\preEqlabel{$\cdots$}
     \begin{oframed}
     $a$，$b$，$c$，$d$を正の数とする．不等式
          

$$
\begin{align*}
\begin{cases}
               s(1-a)-tb>0 \\
               -sc+t(1-d)>0
               \end{cases}
\end{align*}
$$

     を同時に満たす正の数$s$，$t$があるとき，$2$次方程式
          \[x^2-(a+d)x+(ad-bc)=0\]
     は$-1<x<1$の範囲に異なる$2$つの実数解を持つことを示せ．
     \end{oframed}

## 【解】

 与方程式の左辺$f(x)$とする．また
               
<span id="1"></span><span id="2"></span>

$$
\begin{cases}
s(1-a)-tb>0 \tag{1} \\
-sc+t(1-d)>0 \tag{2}
\end{cases}
$$

とする．

$1-a\le 0$つまり$1\le a$の時，[1](#1)が満たされず不適．故に
     

$$
\begin{align}
0<a<1\label{5}
\end{align}
$$

このもとで，[1](#1)を変形して
     

$$
\begin{align}
s>\frac{b}{1-a}t\label{3}
\end{align}
$$

また，$c>0$だから，[2](#2)を変形して
     

$$
\begin{align}
s<\frac{1-d}{c}t\label{4}
\end{align}
$$

である．ここで，$s>0$だから，
     

$$
\begin{align}
1-d>0 \nonumber\\
     0<d<1\label{6}
\end{align}
$$

である．

以上から
      

$$
\begin{align*}
&\exists s_{>0},\exists t_{>0}，[1](#1)\land[2](#2)\\\Longleftrightarrow&\exists s_{>0},\exists t_{>0}，[3](#3)\land[4](#4)\land[5](#5)\\\Longleftrightarrow&\exists t_{>0}，\frac{b}{1-a}t<\frac{1-d}{c}t \land[5](#5)\\\Longleftrightarrow& \frac{b}{1-a}<\frac{1-d}{c}\land[5](#5)\\\Longleftrightarrow& bc<(1-a)(1-d) \land[5](#5)&(\because c>0)
\end{align*}
$$

である．

故に，$a$から$d$までが正であることと併せて，
     

$$
\begin{align*}
f(\pm 1)&=(1+ad-bc)\mp(a+d) \\&>(a+d)\mp(a+d)>0 \\
     f(a)&=-bc<0&(-1<a<1)
\end{align*}
$$

であるから，題意は示された．$\Box$