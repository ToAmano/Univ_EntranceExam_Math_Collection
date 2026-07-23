---
university: "utokyo"
category: "zenki"
year: "1975"
question: "2"
type: "solution"
title: "UTOKYO 1975 zenki Q2 (solution)"
---

\input{macros}
     \begin{oframed}
     $k$，$l$，$m$，$n$は負でない整数とする．$0$でないすべての$x$に対して等式$\cfrac{(x+1)^k}{x^l}-1=\cfrac{(x+1)^m}{x^n}$
     を成り立たせるような$k$，$l$，$m$，$n$の組を求めよ．
     \end{oframed}

## 【解】

 $k,m\ge1$と仮定すると，与式に$x=-1$を代入して$0-1=0$となり不適．故に
     

$$
\begin{align}
km=0\label{1}
\end{align}
$$

である．さらに$x=1$を代入して
     

$$
\begin{align}
2^k-1=2^m\label{2}
\end{align}
$$

である．$k=0$とすると$2^m=0$となり不適だから，[1](#1)より$m=0$が従う．この時[2](#2)から$k=1$となる．

以上を与式に代入して
     

$$
\begin{align}
&\frac{x+1}{x^l}-1=\frac{1}{x^n}\nonumber\\&(x+1)x^n-x^{(n+l)}=x^l　\nonumber\\&x^{(n+l)}-x^{(n+1)}-x^n+x^l=0 \label{3}
\end{align}
$$

である．($\because x\not=0$)これが$\forall x_{\not=0}$で成立するので，[3](#3)は$x$の恒等式である．故に係数比較する.

まず左辺には$x^{(n+1)}$と$x^n$という次数の違う$2$つの項が存在するので，残りの$2$つの項の次数がどちらかに一致することが必要である．$n+l\ge l$だから，$n+l=n+1$，$n=l$が従い，これをといて$(n,l)=(1,1)$である．逆にこの時[3](#3)は成立し，十分．

以上より，求めるのは
     

$$
\begin{align*}
(k,l,m,n)=(1,1,0,1)
\end{align*}
$$

である．$\cdots$(答)