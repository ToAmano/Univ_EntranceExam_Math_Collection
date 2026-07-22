---
university: "utokyo"
category: "zenki"
year: "1971"
question: "6"
type: "solution"
title: "UTOKYO 1971 zenki Q6 (solution)"
---

\input{macros}
     \begin{oframed}
     $3$人で'ジャンケン'をして勝者を決めることにする．例えば，$1$人が'紙'を出し，他の$2$人
     が'石'を出せば，ただ一回で丁度一人の勝者が決まることになる．$3$人で'ジャンケン'をして，
     負けた人は次の解に参加しないことにして丁度$1$人の勝者がきまるまで'ジャンケン'を繰り
     返すことにする．この，$k$回目に，はじめて丁度一人の勝者が決まる確率を求めよ．
     \end{oframed}

## 【解】

$n$回目に$3$人，$2$人でジャンケンする確率をそれぞれ$a_n$，$b_n$とおく．
また，求める確率を$c_n$とおく．ジャンケンの推移する確率は以下の通り．
     
          

|                       |         |
|:---------------------:|:-------:|
| 3人$\to$<!-- -->3人 | $1/3$ |
| 3人$\to$<!-- -->2人 | $1/3$ |
| 3人$\to$<!-- -->1人 | $1/3$ |
| 2人$\to$<!-- -->2人 | $1/3$ |
| 2人$\to$<!-- -->1人 | $2/3$ |

        
よって，ジャンケンの推移から以下の漸化式を得る．
     

$$
\begin{cases}
c_n=\frac{1}{3}a_n+\frac{2}{3}b_n \\
     a_{n+1}=\frac{1}{3}a_n  \\
     b_{n+1}=\frac{1}{3}a_n+\frac{1}{3}b_n 
\end{cases}
$$

さらに，初期条件は$a_1=1$，$b_1=0$である．従って[2](#2)から
     

$$
\begin{align}
a_n=\left(\frac{1}{3}\right)^{n-1}\label{4}
\end{align}
$$

となる．さらにこれを[3](#3)に代入して
     

$$
\begin{align*}
b_{n+1}&=\frac{1}{3}b_n+\left(\frac{1}{3}\right)^n \\
     d_{n+1}&=d_n+1          \\
     d_n&=n-1+d_1\\&=n-1+3b_1 \\&=n-1  \tag{\because b_1=0}\\\therefore  b_n&=(n-1)\left(\frac{1}{3}\right)^{n-1}
\end{align*}
$$

を得る．ただし$d_n=3^nb_n$である．これを[1](#1)に代入すれば，求める確率は     
     

$$
\begin{align*}
c_k=(2k-1)\left(\frac{1}{3}\right)^n\tag{答}
\end{align*}
$$

である．
 \\
 \\
 
{\bf[解$2$]}まず$k\ge2$とする．事象$A$，$B$を
     
          

|             |                             |
|:------------|:----------------------------|
| $A\cdots$ | $3$人でジャンケンする．　 |
| $B\cdots$ | $2$人でジャンケンする．   |

     
と定める．$k$回目に一人の勝者が決まるのは以下のいずれかである．
     

1.  $A\to \dots\to \stackrel{a回目}{A}\to B\to \dots \to \stackrel{k回目}{B}$

2.  $A\to\dots\to \stackrel{k回目}{A}$

(i)で$A$を行う回数$a$，$B$を行う回数を$b$とすると，
     

$$
\begin{align}
a+b=k\label{1}
\end{align}
$$

      
が成り立つ．ただし$a,b>0$である．[解] でのジャンケンの推移の確率から，(i)となる確率は
     

$$
\begin{align*}
p(a)=\left(\frac{1}{3}\right)^{a-1}\frac{1}{3}\left(\frac{1}{3}\right)^{b-1}\frac{2}{3}
     =2\left(\frac{1}{3}\right)^k\tag{\because[1](#1)}
\end{align*}
$$

   
同様に(ii)となる確率は
     

$$
\begin{align*}
q=\left(\frac{1}{3}\right)^{k-1}\frac{1}{3}=\left(\frac{1}{3}\right)^k
\end{align*}
$$

 となる．故に求める確率は
      

$$
\begin{align*}
\sum_{a=0}^{k-1}p(a)+q=(2k-1)\left(\frac{1}{3}\right)^n\tag{答}
\end{align*}
$$

 となる．