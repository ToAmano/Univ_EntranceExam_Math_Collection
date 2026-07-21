---
university: "todai"
category: "zenki"
year: "1970"
question: "1"
type: "solution"
title: "TODAI 1970 zenki Q1 (solution)"
---

\input{macros}
     \begin{oframed}
     $i$を虚数単位とし$a=\cos\frac{\pi}{3}+i\sin\frac{\pi}{3}$とおく．また$n$はすべての自然数にわた
     って動くとする．このとき，
         

1.  $a^n$は何個の異なる値をとり得るか．

2.  $\frac{(1-a^n)(1-a^{2n})(1-a^{3n})(1-a^{4n})(1-a^{5n})}{(1-a)(1-a^2)(1-a^3)(1-a^4)(1-a^5)}$
         の値を求めよ

     \end{oframed}

## 【解】

ドモアブルの定理から$a^n=1$だから，$k=0,1,2,\dots,5$に対して
     
$$
\begin{align}
a^{6n+k}=a^k\label{1}
\end{align}
$$

となる．
     

1.  \eqref{1}から$a^k$についてのみ考えればよいが，このとき$0\le i<j\le5$に対して
     $a^i=a^j$と仮定すると$a^{j-i}=1$となって矛盾．故に$a^i\not=a^j$だから$a^k$はすべて
     異なり，求めるのは$6$個である．

2.  合同式の法を$6$とする．
          \begin{indentation}{2zw}{0pt}
          \underline{(i)$n\equiv \pm1$の時} 
          \[\{n,2n,3n,4n,5n\}\equiv\{1,2,3,4,5\}\]
         であるから，\eqref{1}から(与式)$=1$である．
         
         \underline{(ii)otherwise}　\\
         $\{n,2n,3n,4n,5n\}$の中に合同式で$0$に等しいものがあるので，(与式)$=0$となる．
         \end{indentation}
    以上から
         \begin{align*}
         \text{(与式)}=\left\{
              \begin{array}{ll}
              1 &  (n\equiv \pm1)     \\
              0 &  (otherwise)
              \end{array}
         \right.\tag{答}
         \end{align*}
    となる．