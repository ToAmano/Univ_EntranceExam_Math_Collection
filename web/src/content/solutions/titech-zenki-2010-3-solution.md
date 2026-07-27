---
university: "titech"
category: "zenki"
year: "2010"
question: "3"
type: "solution"
title: "TITECH 2010 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$n$枚から2枚を取り出す場合の数は$\binom n2$通りで，これらは同様に確からしい．

$n=3k+2$（$k\in\mathbb N$）のとき，2枚のうち小さい方が$3t$（$t=1,\dots,k$）である場合，大きい方は$3t+1,3t+2,\dots,3k+2$のいずれかだから，その場合の数は

$$
\begin{align*}
P_k(t)=(3k+2)-3t.
\end{align*}
$$

よって，小さい方が3の倍数であるすべての場合の数$N_k$は

$$
\begin{align*}
N_k=\sum_{t=1}^kP_k(t)=k(3k+2)-3\cdot\frac{k(k+1)}2=\frac12k(3k+1)
\end{align*}
$$

となり，もとめる確率は

$$
\begin{align*}
p(3k+2)=\frac{N_k}{\binom{3k+2}2}=\frac{\frac12k(3k+1)}{\frac{(3k+2)(3k+1)}2}=\frac k{3k+2}.
\end{align*}
$$

**(1)** $n=8=3\cdot2+2$より$k=2$として

$$
\begin{align*}
p(8)=\frac2{3\cdot2+2}=\frac28=\frac14.
\end{align*}
$$

**(2)** 上で示した通り

$$
\begin{align*}
p(3k+2)=\frac k{3k+2}.
\end{align*}
$$