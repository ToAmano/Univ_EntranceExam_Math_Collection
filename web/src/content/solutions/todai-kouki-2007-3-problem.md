---
university: "todai"
category: "kouki"
year: "2007"
question: "3"
type: "problem"
title: "TODAI 2007 kouki Q3 (problem)"
---

$N$を$2$以上の自然数とする．$x_1\le \cdots \le x_N$をみたす実数$x_1,\cdots,x_N$に対し実数$k_n$，$p_n$，$q_n\, (n=0,1,2,\cdots)$を次の手続きで定める．
\begin{itemize}
  \item[A] $k_0=1$，$p_0=x_1$，$q_0=x_N$
  \item[B] $n$が奇数のとき$k_n$は$x_i\le \frac{p_{n-1}+q_{n-1}}{2}$をみたす$x_i$の個数，$p_n=p_{n-1}$，$q_n=q_{n-1}$
  \item[C] $n$が偶数$(n\ge 2)$のとき$k_n=k_{n-1}$，$p_n=\frac{1}{k_n}\sum_{i=1}^{k_n}x_i$，$q_n=\frac{1}{N-k_n}\sum_{i=k_n+1}^{N}x_i$．
\end{itemize}
ただし$k_n=0$または$k_n=N$となったら，その時点で手続きを終了する．$x_1<x_N$であるとき，次の問に答えよ．

1.  すべての自然数$n$について$1\le k_n\le N-1$かつ$x_1\le p_n<q_n\le x_N$が成り立つことを示せ．

2.  実数$J_n\,(n=0,1,2,\cdots)$を$J_n=\sum_{i=1}^{k_n}(x_i-p_n)^2+\sum_{i=k_n+1}^{N}(x_i-q_n)^2$と定めると，全ての自然数$n$に対して$J_n\le J_{n-1}$が成り立つことを示せ．

3.  $n$が十分大きいとき，$J_n=J_{n-1}$，$p_n=p_{n-1}$，$q_n=q_{n-1}$，$k_n=k_{n-1}$が成り立つことを示せ．