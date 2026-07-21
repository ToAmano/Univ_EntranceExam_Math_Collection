---
university: "todai"
category: "kouki"
year: "2006"
question: "3"
type: "problem"
title: "TODAI 2006 kouki Q3 (problem)"
---

数列の和の公式
\begin{equation}
  \sum_{k=1}^{n}k=\frac{1}{2}n(n+1),  \sum_{k=1}^{n}k^2=\frac{1}{6}n(n+1)(2n+1), \sum_{k=1}^{n}k^3=\left\{\frac{1}{2}n(n+1)\right\}^2
\end{equation}
などについて，次のような一般的な考察をしてみよう．$p$，$n$を自然数とする．

1.  $p+1$次多項式$S_p(x)$があって，数列の和$\sum_{k=1}^{n}k^p$が$S_p(n)$と表されることを示せ．

2.  $q$を自然数とする．(1)の多項式$S_1(x), S_3(x),\cdots,S_{2q-1}(x)$に対して，
        \begin{equation}
          \sum_{j=1}^{q}a_{j}S_{2j-1}(x)=x^q(x+1)^q
        \end{equation}
        が恒等式となるような定数$a_1,\cdots,a_q$を$q$を用いてあらわせ．

3.  $q$を$2$以上の自然数とする．(1)の多項式$S_2(x),S_4(x),\cdots,S_{2q-2}(x)$に対して
        \begin{equation}
          \sum_{j=1}^{q-1}b_{j}S_{2j}(x)=x^{q-1}(x+1)^{q-1}(cx+q)
        \end{equation}
        が恒等式となるような定数$c$と$b_1,\cdots,b_{q-1}$を$q$を用いてあらわせ．

4.  $p$を$3$以上の奇数とする．このとき
        \begin{equation}
          \dv{x}S_{p}(x)=pS_{p-1}(x)
        \end{equation}
        を示せ．