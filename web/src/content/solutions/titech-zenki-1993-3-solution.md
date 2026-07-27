---
university: "titech"
category: "zenki"
year: "1993"
question: "3"
type: "solution"
title: "TITECH 1993 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$f(x)=x^4-2ax^2$とおく．$x=t$での接線は$\ell_t: y=(4t^3-4at)x-3t^4+2at^2$であるから，$C$と$\ell_t$の交点の$x$座標は（$P$のぞく）

$$
\begin{align*}
x^4-2ax^2=(4t^3-4at)x-3t^4+2at^2
\end{align*}
$$

$$
\begin{align*}
x^4-2ax^2-4t(t^2-a)x+3t^4-2at^2=0
\end{align*}
$$

$$
\begin{align*}
(x-t)^2\{x^2+2tx+(3t^2-2a)\}=0
\end{align*}
$$

のうち$x\ne t$のもの，すなわち

$$
\begin{align*}
x^2+2tx+3t^2-2a=0 \quad(\text{左辺}g(x)\text{とする}) \quad\cdots\text{①}
\end{align*}
$$

の解である．この判別式$D$として，$-\sqrt a\le t\le\sqrt a$から

$$
\begin{align*}
D/4=t^2-(3t^2-2a)=2a-t^2\ge0
\end{align*}
$$

となり，①は異2実解（重解含む）を持つ．したがって，①の2解が$\alpha,\beta$で，

$$
\begin{align*}
\alpha+\beta=-2t, \qquad\alpha\beta=3t^2-2a
\end{align*}
$$

**(2)** $\alpha\le\beta$だから，題意の条件は（重なる場合をのぞいて）

$$
\begin{align*}
\alpha<t<\beta\quad\cdots\text{②}
\end{align*}
$$

である．すなわち，①の解が$x<t$に1つ，$t<x$に1つある時で，この条件は

$$
\begin{align*}
g(t)<0 \iff 6t^2-2a<0 \iff -\sqrt{\frac{a}{3}}<t<\sqrt{\frac{a}{3}}
\end{align*}
$$

である．

**(3)** $\ell$の傾きは$4t^3-4at$だから，位置関係は右図のようになる．したがってピタゴラスの定理から

$$
\begin{align*}
L^2=(\beta-\alpha)^2+(\beta-\alpha)^2(4t^3-4at)^2
\end{align*}
$$

$$
\begin{align*}
=\{1+16t^2(t^2-a)^2\}\{(\alpha+\beta)^2-4\alpha\beta\}
\end{align*}
$$

$$
\begin{align*}
=\{1+16t^2(t^2-a)^2\}\{(-2t)^2-4(3t^2-2a)\}\quad(\because(1))
\end{align*}
$$

$$
\begin{align*}
=\{1+16t^2(t^2-a)^2\}(8a-8t^2)
\end{align*}
$$

**(4)** $L^2\equiv h(p)\ (p=t^2)$とすると，$-\sqrt a\le t\le\sqrt a$から$0\le p\le a\ \cdots$③である（(3)より）．

$$
\begin{align*}
h(p)=\{1+16p(p-a)^2\}(8a-8p)=-8(p-a)\{1+16p(p-a)^2\}
\end{align*}
$$

だから，

$$
\begin{align*}
-\frac18h'(p)=1+16p(p-a)^2+(p-a)\cdot16(3p^2-4ap+a^2)
\end{align*}
$$

$$
\begin{align*}
=16(p-a)\{p(p-a)+3p^2-4ap+a^2\}+1
\end{align*}
$$

$$
\begin{align*}
=16(p-a)^2(4p-a)+1
\end{align*}
$$

$a=\dfrac{7}{12}$の時，$p=\dfrac1{12}$を代入すると，$p-a=-\dfrac12,\ 4p-a=-\dfrac14$から

$$
\begin{align*}
16\left(-\frac12\right)^2\left(-\frac14\right)+1=16\cdot\frac14\cdot\left(-\frac14\right)+1=-1+1=0
\end{align*}
$$

となり，$h'(1/12)=0$である．$0\le p\le a=7/12$での$h'(p)$の符号を調べると，下表のようになり，

| $p$  | $0$ |              | $1/12$ |              | $7/12$ |
|:------:|:-----:|:------------:|:--------:|:------------:|:--------:|
| $h'$ |       |    $+$     |  $0$   |    $-$     |          |
| $h$  |       | $\nearrow$ |          | $\searrow$ |          |

したがって，$h(p)$は$p=\dfrac1{12}$でmaxで，

$$
\begin{align*}
\max L^2=-8\left(\frac1{12}-\frac{7}{12}\right)\left\{1+16\cdot\frac1{12}\left(\frac1{12}-\frac{7}{12}\right)^2\right\}
\end{align*}
$$

$$
\begin{align*}
=4\left(1+\frac43\cdot\frac14\right)=\frac{16}{3}
\end{align*}
$$

これから

$$
\begin{align*}
\max L=\sqrt{\frac{16}{3}}=\frac{4\sqrt3}{3}
\end{align*}
$$