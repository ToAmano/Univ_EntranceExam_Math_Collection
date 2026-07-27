---
university: "titech"
category: "zenki"
year: "2000"
question: "2"
type: "solution"
title: "TITECH 2000 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$\cos\theta=c,\ \sin\theta=s$と書く．

**(1)**

$$
\begin{align*}
\left|z+\frac12\right|<\frac12 \iff\left|(rc+\tfrac12)+irs\right|<\frac12 \iff\left(rc+\frac12\right)^2+(rs)^2<\frac14 \quad(\because\text{両辺}\ge0)
\end{align*}
$$

$$
\begin{align*}
\iff r^2+rc<0 \iff r(r+\cos\theta)<0
\end{align*}
$$

$r\ge0$だから，これは$r\ne0$かつ$r+\cos\theta<0$と同値．すなわち

$$
\begin{align*}
r>0\ \text{かつ}\ r<-\cos\theta\quad(\text{したがって}\ \cos\theta<0\ \text{も必要})
\end{align*}
$$

**(2)** $z\ne1$の時，$1+z+\cdots+z^n=\dfrac{z^{n+1}-1}{z-1}$だから

$$
\begin{align*}
\left|1+z+\cdots+z^n\right|^2=\frac{|z^{n+1}-1|^2}{|z-1|^2}
\end{align*}
$$

$|z-1|^2=(rc-1)^2+(rs)^2=r^2-2rc+1=r^2-2r\cos\theta+1$．

$$
\begin{align*}
|z^{n+1}-1|^2=\left(r^{n+1}\cos(n+1)\theta-1\right)^2+\left(r^{n+1}\sin(n+1)\theta\right)^2=r^{2n+2}-2r^{n+1}\cos(n+1)\theta+1
\end{align*}
$$

よって

$$
\begin{align*}
|1+z+\cdots+z^n|^2=\frac{r^{2n+2}-2r^{n+1}\cos(n+1)\theta+1}{r^2-2r\cos\theta+1}
\end{align*}
$$

（$z=1$（$r=1,\theta=0$）の時は直接$|1+z+\cdots+z^n|^2=(n+1)^2$．）

**(3)** $Z_n=1+z+\cdots+z^n$とおく．(1)の条件から$0<r<-\cos\theta$，特に$\cos\theta<0$．まず

$$
\begin{align*}
r^2-2r\cos\theta+1=(r-1)^2+2r(1-\cos\theta)>0 \quad(\because\cos\theta<0\ \text{より}\ 1-\cos\theta>0,\ r>0)
\end{align*}
$$

だから(2)の分母は正．$|Z_n|<1\iff|Z_n|^2<1\iff$（分母を払って）

$$
\begin{align*}
r^{2n+2}-2r^{n+1}\cos(n+1)\theta+1<r^2-2r\cos\theta+1
\end{align*}
$$

$$
\begin{align*}
\iff r^{2n+2}-2r^{n+1}\cos(n+1)\theta<r^2-2r\cos\theta
\end{align*}
$$

両辺を$r>0$で割って，示すべき式は

$$
\begin{align*}
r^{2n+1}-2r^n\cos(n+1)\theta<r-2\cos\theta\quad\cdots\text{①}
\end{align*}
$$

これを示す．$r+\cos\theta<0$（(1)）から$2\cos\theta<-2r$，よって

$$
\begin{align*}
r^{2n+1}-2r^n\cos(n+1)\theta-r+2\cos\theta<r^{2n+1}-2r^n\cos(n+1)\theta-r-2r
\end{align*}
$$

$$
\begin{align*}
=r\left(r^{2n}-2r^{n-1}\cos(n+1)\theta-3\right)
\end{align*}
$$

$|\cos(n+1)\theta|\le1$より$-\cos(n+1)\theta\le1$だから

$$
\begin{align*}
<r\left(r^{2n}+2r^{n-1}-3\right)
\end{align*}
$$

さらに$0<r<-\cos\theta\le1$から$0<r<1$，よって$r^{2n}<1,\ r^{n-1}\le1$（$n\ge1$）だから

$$
\begin{align*}
r^{2n}+2r^{n-1}-3<1+2-3=0
\end{align*}
$$

以上から

$$
\begin{align*}
r^{2n+1}-2r^n\cos(n+1)\theta-r+2\cos\theta<r\cdot(\text{負})<0
\end{align*}
$$

すなわち①が成り立ち，したがって$|Z_n|^2<1$，すなわち$|1+z+\cdots+z^n|<1$が全ての自然数$n$で成り立つ．