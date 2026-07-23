---
university: "utokyo"
category: "kouki"
year: "2004"
question: "2"
type: "problem"
title: "UTOKYO 2004 kouki Q2 (problem)"
---

集合$A$,$B$を$A=\{0,1,2,3,4,5,6,7\}$，$B=\{0,1\}$とし，$N$を$3$以上の整数とする．また，各項が$0$または$1$からなる数列を$01$数列と呼ぶことにする．
$01$数列$a_1,a_2,\cdots.a_N$に対し，$A$から$B$への写像$f$を用いて，新しい$01$数列$b_1,b_2,\cdots,b_N$を，

$$
\begin{align*}
b_1=f(a_1),b_2=f(2a_1+a_2),b_k=f(4a_{k-2}+2a_{k-1}+a_k)\,(k=3,4,\cdots, N)
\end{align*}
$$

と定め，$b_1$,$b_2$,$\cdots$,$b_N$は$a_1$,$a_2$,$\cdots$,$a_N$から$f$によって得られるという．ただし，$A$から$B$への写像$f$とは，$A$の各要素$x$にたいして$B$の要素$f(x)$をただひとつ対応させる規則をさすものとする．次の問に答えよ．

\begin{enumerate}
\item $A$から$B$への写像は，全部で何通りあるか．
  \item $f(0)=f(3)=f(4)=f(7)=0$，$f(1)=f(2)=f(5)=f(6)=1$，であるとき，
        

$$
\begin{align*}
b_k=\frac{1}{2}\left\{1+(-1)^k\right\}\,(k=1,2,\cdots,N)
\end{align*}
$$

        となるような$01$数列$a_1$，$a_2$，$\cdots$，$a_N$を求めよ．
  \item $A$から$B$への写像$f$が，条件
        

$$
\begin{align*}
(P)\,\, f(2m)\neq f(2m+1)\,\,(m=0,1,2,3)
\end{align*}
$$

        を満たすとする．このような$f$は何通りあるか．
  \item $A$から$B$への写像$f$が条件(P)をみたすならば，どのような$N$項からなる$01$数列も，ある$01$数列$a_1$,$a_2$,$\cdots$,$a_N$から$f$によって得られることを示せ．
\end{enumerate}