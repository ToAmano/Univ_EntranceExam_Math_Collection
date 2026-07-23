---
university: "utokyo"
category: "zenki"
year: "1971"
question: "2"
type: "solution"
title: "UTOKYO 1971 zenki Q2 (solution)"
---

\input{macros}
     \begin{oframed}
     正数$x$を与えて，
          

$$
\begin{align*}
2a_1=x，2a_2=a_1^2+1，\cdots，2a_{n+1}=a_n^2+1，\cdots
\end{align*}
$$

     のように数列$\{a_n\}$を定める時，
          

1.  

2.  $x\not=2$ならば，$a_1<a_2<\cdots<a_n<\cdots$となることを証明せよ．

3.  $x<2$ならば，$a_n<1$となることを証明せよ．このとき，正数$\epsilon$を$1-x/2$より
          小となるようにとって，$a_1，a_2，\cdots，a_n$までが$1-\epsilon$以下となったとすれば，
          個数$n$について次の不等式が成り立つことを証明せよ．
               

$$
\begin{align*}
2-x>n\epsilon^2
\end{align*}
$$

     \end{oframed}

## 【解】

 

1.  

2.  与えられた漸化式より，
     

$$
\begin{align}
&a_n<a_{n+1}\nonumber\\\Longleftrightarrow&2a_n<a_n^2+1\nonumber\\\Longleftrightarrow&(a_n-1)^2>0\nonumber\\\Longleftrightarrow&a_n\not=1\label{1}
\end{align}
$$

である．$x\not=2$ならば，$a_1\not=1$だから，漸化式より帰納的に
$a_n\not=1$である．これと[1](#1)より題意は示された．$\Box$

3.  漸化式および$x>0$から，$a_n>0$であることに注意すると，$a_{n+1}$は$a_n$の単調増加関数である．
$x<2$ならば$a_1<1$である．そこで以下$k\in\mathbb{N}$に対して$a_k<1$が成立すると仮定すると
     

$$
\begin{align*}
a_{k+1}=\frac{a_k^2+1}{2}<\frac{1+1}{2}=1
\end{align*}
$$

故に帰納法により$\forall n,a_n<1$となる．$\Box$

次に，後半部分を考える．題意より
     

$$
\begin{align}
\left\{\begin{array}{ll}
          1-\dfrac{x}{2}>\epsilon\\
          a_k<1-\epsilon&k=1,2,\cdots,n
          \end{array}\right.\label{2}
\end{align}
$$

である．第一式から，$a_1<1-\epsilon$が保証される．

ここで，漸化式より，$k\le n$のとき，
     

$$
\begin{align*}
&2(a_{k+1}-a_k)=(a_k-1)^2>\epsilon^2&(\because[2](#2))
\end{align*}
$$

     
となる．$k$について和をとって，
     

$$
\begin{align*}
2(a_{n+1}-a_1)=\sum_{k=1}^n (a_k-1)^2>n\epsilon^2 \\
     a_{n+1}-\frac{x}{2}>\frac{n\epsilon^2}{2}
\end{align*}
$$

前半部分から$a_{n+1}<1$だから，    
     

$$
\begin{align*}
1-\frac{x}{2}>\frac{n\epsilon^2}{2}\\
     2-x>n\epsilon^2
\end{align*}
$$

となって，題意の不等式を得る．$\Box$