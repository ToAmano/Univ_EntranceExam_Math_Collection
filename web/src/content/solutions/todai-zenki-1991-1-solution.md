---
university: "todai"
category: "zenki"
year: "1991"
question: "1"
type: "solution"
title: "TODAI 1991 zenki Q1 (solution)"
---

\input{macros}
     \begin{oframed}
     平面上に正四面体が置いてある．平面と接している面の$3$辺のひとつを任意に選び，これを軸と
     して正四面体を倒す．$n$回の操作の後に，最初に平面と接していた面が再び平面と接する確率を
     求めよ．
     \end{oframed}

## 【解】

題意の確率$p_n$とおくと，対称性から
    
$$
\begin{align*}
&p_{n+1}=\frac{1}{3}(1-p_n) \\\therefore&p_{n+1}-\frac{1}{4}=\frac{-1}{3}\left(p_n-\frac{1}{4}\right)
\end{align*}
$$

$p_0=1$だから，繰り返し用いて
     
$$
\begin{align*}
p_n=\frac{1}{4}\left\{1-\left(\frac{-1}{3}\right)^{n-1}\right\}\tag{答}
\end{align*}
$$

となる．