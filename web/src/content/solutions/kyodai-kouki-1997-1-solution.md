---
university: "kyodai"
category: "kouki"
year: "1997"
question: "1"
type: "solution"
title: "KYODAI 1997 kouki Q1 (solution)"
---

## 【解】

  題意より，$C_{p,q}$の方程式は
  
$$
\begin{align}
& C_{p,q}: y=a(x-p)^2+q & (a \neq 1) \label{1997-1:eq:1}
\end{align}
$$

  である．ここで，$(p,q)=(0,0)$は$C_{p,q}$と$C_{1}$が重なって題意の条件を満たさないので不適で，以下
  
$$
\begin{align*}
p \neq 0 \\
    q \neq 0
\end{align*}
$$

  とする．

  $C_{p,q}$の頂点は$(p,q)$である．
  この点で$C_1$および$C_{p,q}$が交わることから，
  $C_1$は$(p,q)$を通る．従って
  
$$
\begin{align}
q & = p^2\label{1997-1:eq:2}
\end{align}
$$

  である．
  この元で，$C_{p,q}$と$C_{1}$を連立した$x$の二次方程式
  
$$
\begin{align*}
x^2 = a(x-p)^2+q
\end{align*}
$$

  のもう一つの解の点で$C_1$,$C_{p,q}$の接線が直交する．
  $\eqref{1997-1:eq:2}$を代入すると
  
$$
\begin{align*}
& (a-1)x^2-2apx+(a+1)p^2 = 0                               \\& (a-1)\left(x-p\right)\left(x-\frac{a+1}{a-1}p\right) = 0
\end{align*}
$$

  となる．$a-1=0$の時は方程式が一次方程式となり，二点で交わる条件を満たさないので不適である．
  すなわち
  
$$
\begin{align}
a \neq 1 \label{1997-1:eq:3}
\end{align}
$$

  である．
  この元で，もう一つの解は
  
$$
\begin{align*}
x = \frac{a+1}{a-1}p
\end{align*}
$$

  である．この点で$C_1$, $C_{p,q}$の接線の傾きは
  
$$
\begin{align*}
& C_1: 2\frac{a+1}{a-1}p                     \\& C_{p,q}: 2a\left(\frac{a+1}{a-1}p-p\right)
\end{align*}
$$

  だから，これらが直交する条件より，
  
$$
\begin{align*}
& 2a\left(\frac{a+1}{a-1}p-p\right)\cdot 2\frac{a+1}{a-1}p = -1 \\& 8a \frac{a+1}{(a-1)^2} p^2 = -1
\end{align*}
$$

  $a=0, a=-1$はこの条件を満たさないので不適で，以下
  
$$
\begin{align}
\begin{dcases}
       & a \neq 0  \\
       & a \neq -1
    \end{dcases}\label{1997-1:eq:4}
\end{align}
$$

  として考えると，この方程式を$p$について解いて
  
$$
\begin{align*}
p^2 = -\frac{(a-1)^2}{8a(a+1)}
\end{align*}
$$

  このような実数$p\neq 0$が存在するには，右辺が$0$より大きければよく，
  
$$
\begin{align*}
-\frac{(a-1)^2}{8a(a+1)} > 0
\end{align*}
$$

  が求める$a$の条件である．
  $\eqref{1997-1:eq:3}$より$a\neq 1$だから分子は負であり，よってこの条件を満たすには
  分母が負であれば良い．
  
$$
\begin{align*}
& a(a+1) < 0 \\\therefore& -1 < a < 0
\end{align*}
$$

  これは$\eqref{1997-1:eq:3}$の条件を満たしているから，求める条件は
  
$$
\begin{align*}
-1 < a < 0
\end{align*}
$$

  である． $\cdots$(答)

  
  

## 【解説】