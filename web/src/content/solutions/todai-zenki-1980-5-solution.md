---
university: "todai"
category: "zenki"
year: "1980"
question: "5"
type: "solution"
title: "TODAI 1980 zenki Q5 (solution)"
---

\input{macros}
     \begin{oframed}
     $1$辺の長さが$1$の正四面体$A_0A_1A_2A_3$がある．点$P$はこの正四面体の返上を毎秒
     $1$の速さで動き，各頂点にたっしたとき，そこから出る$3$辺のうちの$1$辺を$\dfrac{1}{3}$
     ずつの確率で選んで進む，$P$は時刻$0$において頂点$A_0$にあるとする．また$n$を$0$または
     正の整数とし，点$P$が時刻$t=n$において頂点$A_i$にある確率を$p_i(n)$で表す．$(i=0,1,2,3)$．
          

1.  数学的昨日法を用いて，$p_1(n)=p_2(n)=p_3(n)$を証明せよ．

2.  $p_0(n)$と$p_1(n)$の値を求めよ．

     \end{oframed}

## 【解】

まず，題意から以下の漸化式を得る．
     

$$
\begin{align}
p_i(n+1)=\dfrac{1}{3}(1-p_i(n)) \label{1}
\end{align}
$$

     

1.  題意から$p_1(0)=p_2(0)=p_3(0)$であるから$n=0$では成立．次に$n=k$での成立を仮定すれ
     ば[1](#1)から$n=k+1$でも成立．以上から示された．$\Box$

2.  [1](#1)から，
          \begin{align*}
          p_i(n+1)-\frac{1}{4}=\frac{-1}{3}\left(p_i(n)-\frac{1}{4}\right)
          \end{align*}
     だから，繰り返し用いて
          \begin{align*}
          p_i(n)=\left(\frac{-1}{3}\right)^n\left(p_i(0)-\frac{1}{4}\right)+\frac{1}{4}
          \end{align*}
     となる．初期条件$p_1(0)=0$，$p_0(1)=1$から
          \begin{align*}
          \left\{
               \begin{array}{l}
               p_0(n)=\dfrac{3}{4}\left(\dfrac{-1}{3}\right)^n+\dfrac{1}{4} \\
               p_1(n)=\dfrac{1}{4}\left\{1-\left(\dfrac{-1}{3}\right)^n\right\}
               \end{array}
          \right.
          \end{align*}
     が求める値である．$\cdots$(答)