---
university: "titech"
category: "zenki"
year: "2010"
question: "2"
type: "solution"
title: "TITECH 2010 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

方程式

$$
\begin{align*}
x=\Bigl[\frac12\Bigl(x+\frac ax\Bigr)\Bigr]\tag{\ast}
\end{align*}
$$

の右辺は整数だから，解$x$は正の整数である．$x=k_a$（$k_a\in\mathbb N$）が解のとき，$k_a\le\dfrac12\Bigl(k_a+\dfrac a{k_a}\Bigr)<k_a+1$，すなわち

$$
\begin{align*}
k_a^2\le a<k_a^2+2k_a.
\end{align*}
$$

これは$a<(k_a+1)^2-1$と同値だから$k_a+1>\sqrt{a+1}$，すなわち$k_a>-1+\sqrt{a+1}$．まとめると

$$
\begin{align*}
-1+\sqrt{a+1}<k_a\le\sqrt a.\tag{P(a)}
\end{align*}
$$

したがって，$(\ast)$が解を持つことと，区間$(-1+\sqrt{a+1},\sqrt a\,]$に正の整数が存在することは同値である．

**(1)** $a=7$：$P(7)$は$-1+2\sqrt2<k_a\le\sqrt7$，すなわち$1.83\cdots<k_a\le2.64\cdots$．$k_a=2$が適し，解は$x=2$．

$a=8$：$P(8)$は$2<k_a\le2\sqrt2=2.82\cdots$．これをみたす整数はない．よって解なし．

$a=9$：$P(9)$は$-1+\sqrt{10}<k_a\le3$，すなわち$2.16\cdots<k_a\le3$．$k_a=3$が適し，解は$x=3$．

**(2)** $t\in\mathbb N$とする．$t^2\le a<(t+1)^2$のとき$[\sqrt a\,]=t$である．

1.  $t^2\le a\le(t+1)^2-1-1=t^2+2t-1$のとき，$1+a\le(t+1)^2-1<(t+1)^2$より$-1+\sqrt{1+a}<t$（等号は不成立）となり，$t$は$P(a)$をみたす．

2.  $a=(t+1)^2-1=t^2+2t$のとき，$-1+\sqrt{1+a}=-1+(t+1)=t$となり，$P(a)$の左側が等号（非成立）になるため，$t$は$P(a)$をみたさない．また$\sqrt a<t+1$より$P(a)$をみたす整数は$t$以外になく，この$a$では$(\ast)$は解を持たない．

よって，$(\ast)$が解を持たないのは$a=t^2+2t\ (=(t+1)^2-1)$（$t\in\mathbb N$）と表せるときであり，

$$
\begin{align*}
a_1=1^2+2\cdot1=3,\qquad a_2=2^2+2\cdot2=8.
\end{align*}
$$

（$a=8$が解なしという(1)の結果とも一致する．）一般に$a_n=n^2+2n=n(n+2)$．

**(3)** $S_n=\displaystyle\sum_{k=1}^n\frac1{a_k}$とおくと，$a_k=k(k+2)$より部分分数分解$\dfrac1{k(k+2)}=\dfrac12\Bigl(\dfrac1k-\dfrac1{k+2}\Bigr)$を用いて

$$
\begin{align*}
S_n=\sum_{k=1}^n\frac1{k(k+2)}=\frac12\sum_{k=1}^n\Bigl(\frac1k-\frac1{k+2}\Bigr)=\frac12\Bigl(1+\frac12-\frac1{n+1}-\frac1{n+2}\Bigr)\xrightarrow[n\to\infty]{}\frac12\Bigl(1+\frac12\Bigr)=\frac34.
\end{align*}
$$

よって$\displaystyle\sum_{n=1}^\infty\frac1{a_n}=\frac34$．