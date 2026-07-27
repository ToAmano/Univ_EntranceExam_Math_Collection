---
university: "titech"
category: "zenki"
year: "1996"
question: "1"
type: "solution"
title: "TITECH 1996 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

**(1)** $n=2$の時

$$
\begin{align*}
x_1+x_2=x_1x_2
\end{align*}
$$

$$
\begin{align*}
(x_1-1)(x_2-1)=1
\end{align*}
$$

$x_1-1\ge0,\ x_2-1\ge0\in\mathbb{Z}$から

$$
\begin{align*}
(x_1-1,x_2-1)=(1,1) \quad\therefore\ (x_1,x_2)=(2,2)
\end{align*}
$$

$n=3$の時

$$
\begin{align*}
x_1+x_2+x_3=x_1x_2x_3 \quad\cdots\text{①}
\end{align*}
$$

対称性からまず$x_1\ge x_2\ge x_3$とすると，

$$
\begin{align*}
x_1x_2x_3\le3x_1
\end{align*}
$$

$$
\begin{align*}
x_2x_3\le3
\end{align*}
$$

これをみたす組をかんがえて，

$$
\begin{align*}
(x_2,x_3)=(1,1),(2,1),(3,1)
\end{align*}
$$

このうち①をみたすのは$(x_1,x_2,x_3)=(3,2,1)$だから，

$$
\begin{align*}
(x_1,x_2,x_3)=(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)
\end{align*}
$$

**(2)** $n\ge3$とする．$(x_1,x_2,\cdots,x_n)=(n,2,1,\cdots,1)$は解であったから，これらから得られる${}_nP_2=n(n-1)$通りも解．したがって，(1)とあわせて，解がちょうど1となるのは

$$
\begin{align*}
n=2
\end{align*}
$$

の時

**(3)** (2)から任意の$n$に対し解は少なくとも1つ存在．次に有限性を示す．まず，$x_1\ge x_2\ge\cdots$の時をかんがえる．

$$
\begin{align*}
x_1x_2\cdots x_n\le nx_1
\end{align*}
$$

$$
\begin{align*}
x_2\cdots x_n\le n
\end{align*}
$$

だから，$x_2\le n$が必要で，$(x_2,\cdots,x_n)$の組は高々$n^{n-1}$通りしかない．$x_1x_2\cdots x_n=x_1+\cdots+x_n$は$x_1$の1次方程式だから定まる．すなわち，$(x_2,\cdots,x_n)$に対し$x_1$は高々1通りしかない．したがって，$x_1\ge x_2\ge\cdots$以外の時もかんがえて解は高々$n^{n-1}\cdot n!$通りしかない．したがって有限である．