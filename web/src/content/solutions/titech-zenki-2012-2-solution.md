---
university: "titech"
category: "zenki"
year: "2012"
question: "2"
type: "solution"
title: "TITECH 2012 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

**(1)** $A=\displaystyle\sum_{n=0}^{99}3^n=\frac{3^{100}-1}{3-1}=\frac12(3^{100}-1)=\frac{3^{100}}2-\frac12$とおく．$3^{100}/2$は整数ではないが，桁数を考える上で$A$は$B:=3^{100}/2$とほぼ同じ大きさであり，$3^{100}/2$が$10^\ell$（$\ell\in\mathbb Z$）の形になることはないから，$A$の桁数は$B$の桁数と一致する．$B$が$m$桁とすると$10^{m-1}\le B<10^m$．常用対数をとって

$$
\begin{align*}
m-1\le\log_{10}B<m,\qquad\log_{10}B=100\log_{10}3-\log_{10}2=47.71-\log_{10}2.\tag{①}
\end{align*}
$$

$\log_{10}x$は単調増加関数であり$0=\log_{10}1<\log_{10}2<\log_{10}3=0.4771$だから

$$
\begin{align*}
47.71-0.4771<47.71-\log_{10}2<47.71-0,\quad\text{すなわち}\quad47.2329<\log_{10}B<47.71
\end{align*}
$$

となり，これは常に$47<\log_{10}B<48$の範囲にあるから，①をみたす$m$は$m=48$のみ．よって$A$は$\boxed{48}$桁である．

（別解：$0.4771<0.71<0.4771\times2=\log_{10}9$の各辺に$47$を加えて$\log_{10}10^{47}+\log_{10}3<47.71<\log_{10}10^{47}+\log_{10}9$，すなわち$3\cdot10^{47}<3^{100}<9\cdot10^{47}$（$\log_{10}x$は単調増加）．よって$\dfrac32\cdot10^{47}-\dfrac12<A<\dfrac92\cdot10^{47}-\dfrac12$となり，これより$A$は$48$桁．）

**(2)** $m^2\le n<(m+1)^2$（$m\in\mathbb N$）のとき$m\le\sqrt n<m+1$より$[\sqrt n]=m$．したがって，この範囲で$n$が$m$で割り切れるのは

$$
\begin{align*}
m=1\text{のとき}&:\ n=1,2,3\ \text{の}3\text{通り},\\
m\ge2\text{のとき}&:\ n=m^2,\ m(m+1),\ m(m+2)\ \text{の}3\text{通り}
\end{align*}
$$

である（区間$[m^2,m^2+2m]$内の$m$の倍数はこの3つに限る）．$10000=100^2$だから，$n=10000$（$m=100$のとき$n=m^2$）も条件をみたす．$m=1,\dots,99$については各々$3$通りずつ，$m=100$については$n=10000$の$1$通りのみ（範囲が$n\le10000$で打ち切られるため）．よって求める個数は

$$
\begin{align*}
\sum_{m=1}^{99}3+1=297+1=298.
\end{align*}
$$