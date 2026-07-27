---
university: "titech"
category: "zenki"
year: "2004"
question: "4"
type: "solution"
title: "TITECH 2004 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

2球は$x^2+y^2+z^2=r^2$，$(x-1)^2+y^2+z^2=1-r^2$．辺々引くと，交面は$x=r^2$である（$0<r<1$より$0<r^2<r<1$）．

**(1)** 交わりの立体は，球1（中心$0$，半径$r$）の$x\ge r^2$の部分（球欠）と，球2（中心$1$，半径$\sqrt{1-r^2}$）の$x\le r^2$の部分（球欠）の和である．球$i$を単位球に正規化した時の対応する球欠の体積（$\pi$倍する前）を$V_i$とすると，スケーリングにより

$$
\begin{align*}
V(r)=r^3V_1+(1-r^2)^{3/2}V_2 \quad\cdots\text{①}
\end{align*}
$$

球1の交面$x=r^2$は，半径$r$で正規化すると$x'=r^2/r=r$（単位球上）に対応するので

$$
\begin{align*}
V_1=\int_r^1(1-x^2)\,dx=\left[x-\frac{x^3}3\right]_r^1=\frac23-r+\frac13r^3
\end{align*}
$$

球2の交面$x=r^2$は，中心$1$，半径$d:=\sqrt{1-r^2}$で正規化すると，中心からの距離が$1-r^2=d^2$，正規化座標で$-d$に対応するので，対称性から同じ形で

$$
\begin{align*}
V_2=\frac23-d+\frac13d^3 \quad(d=\sqrt{1-r^2})
\end{align*}
$$

①に代入して（$d^2=1-r^2,\ d^4=(1-r^2)^2,\ d^6=(1-r^2)^3$に注意）

$$
\begin{align*}
V(r)=r^3\left(\frac23-r+\frac13r^3\right)+d^3\left(\frac23-d+\frac13d^3\right)
\end{align*}
$$

$$
\begin{align*}
=\frac23r^3-r^4+\frac13r^6+\frac23d^3-(1-r^2)^2+\frac13(1-r^2)^3
\end{align*}
$$

整理して（$\pi$倍を忘れずに）

$$
\begin{align*}
V(r)=\left(-r^4+\frac23r^3+r^2-\frac23+\frac23(1-r^2)^{3/2}\right)\pi
\end{align*}
$$

**(2)**

$$
\begin{align*}
\frac{V'(r)}\pi=-4r^3+2r^2+2r+\frac23\cdot\frac32(1-r^2)^{1/2}\cdot(-2r)=-4r^3+2r^2+2r-2r(1-r^2)^{1/2}
\end{align*}
$$

$$
\begin{align*}
=-2r\left[2r^2-r-1+(1-r^2)^{1/2}\right]
\end{align*}
$$

$0<r<1$では$-2r<0$だから，$f(r):=2r^2-r-1+\sqrt{1-r^2}$とおくと，$V'(r)$の符号は$-f(r)$の符号に等しい．

$f(r)\ge0\iff\sqrt{1-r^2}\ge1+r-2r^2$．$0<r<1$で右辺が正であることを確かめた上で両辺を2乗すると

$$
\begin{align*}
1-r^2\ge(1+r-2r^2)^2=4r^4-4r^2(r+1)+(r+1)^2=4r^4-4r^3-3r^2+2r+1
\end{align*}
$$

$$
\begin{align*}
\iff4r^4-4r^3-2r^2+2r\le0\iff2r(2r^3-2r^2-r+1)\le0\iff2r(r-1)(2r^2-1)\le0
\end{align*}
$$

（$2r^3-2r^2-r+1=(r-1)(2r^2-1)$は$r=1$が根であることを確認して因数分解）．$0<r<1$では$2r>0,\ (r-1)<0$だから$2r(r-1)<0$，したがって

$$
\begin{align*}
2r(r-1)(2r^2-1)\le0\iff2r^2-1\ge0\iff r\ge\frac1{\sqrt2}
\end{align*}
$$

すなわち，$f(r)\ge0\iff r\ge1/\sqrt2$．下表を得る．

| $r$  | $0$ |              | $1/\sqrt2$ |              | $1$ |
|:------:|:-----:|:------------:|:------------:|:------------:|:-----:|
| $f$  |       |    $-$     |    $0$     |    $+$     |       |
| $V'$ |       |    $+$     |    $0$     |    $-$     |       |
| $V$  |       | $\nearrow$ |              | $\searrow$ |       |

よって$V(r)$は$r=1/\sqrt2=\sqrt2/2$で最大．この時$r^2=1/2,\ r^3=\sqrt2/4,\ r^4=1/4,\ 1-r^2=1/2,\ (1-r^2)^{3/2}=\sqrt2/4$だから

$$
\begin{align*}
\frac{V(1/\sqrt2)}\pi=-\frac14+\frac23\cdot\frac{\sqrt2}4+\frac12-\frac23+\frac23\cdot\frac{\sqrt2}4=\left(-\frac14+\frac12-\frac23\right)+\frac{4}{3}\cdot\frac{\sqrt2}4=-\frac5{12}+\frac{\sqrt2}3
\end{align*}
$$

したがって，$r=\dfrac{\sqrt2}2$で最大値

$$
\begin{align*}
\max V=\left(\frac{\sqrt2}3-\frac5{12}\right)\pi
\end{align*}
$$

をとる．