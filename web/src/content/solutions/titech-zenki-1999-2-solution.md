---
university: "titech"
category: "zenki"
year: "1999"
question: "2"
type: "solution"
title: "TITECH 1999 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$O$から底面へ下ろした垂線の足を$H$（正$n$角形$A_1\cdots A_n$の中心）とし，$A_1H=x$（$0<x<1$）とおく．対称性から，

$$
\begin{align*}
V_n=n\times(\text{三角錐 } O\text{-}HA_1A_2) \quad\cdots\text{①}
\end{align*}
$$

である．$\triangle OHA_1$は$H$が直角，斜辺$OA_1=1$だから，ピタゴラスの定理より

$$
\begin{align*}
OH=\sqrt{1-x^2}\quad\cdots\text{②}
\end{align*}
$$

また，$\angle A_1HA_2=2\pi/n$（$H$を中心とした隣接2頂点のなす角）で，二等辺三角形$A_1A_2H$（$HA_1=HA_2=x$）の面積は

$$
\begin{align*}
\triangle A_1A_2H=\frac12x^2\sin\frac{2\pi}n=x^2\sin\frac\pi n\cos\frac\pi n \quad\cdots\text{③}
\end{align*}
$$

$OH$は底面に垂直だから，三角錐$O$-$HA_1A_2$の高さは$OH$であり，②③から

$$
\begin{align*}
(O\text{-}HA_1A_2)=\frac13\sqrt{1-x^2}\cdot x^2\sin\frac\pi n\cos\frac\pi n \quad\cdots\text{④}
\end{align*}
$$

①④から

$$
\begin{align*}
V_n=\frac n3\sin\frac\pi n\cos\frac\pi n\cdot x^2\sqrt{1-x^2}
\end{align*}
$$

$x^2\sqrt{1-x^2}$を$x\in(0,1)$で最大化する．$t=x^2\in(0,1)$とおくと$x^2\sqrt{1-x^2}=\sqrt{t^2(1-t)}=\sqrt{t^2-t^3}$だから，$f(t)=t^2-t^3$の最大値を考えれば良い．$f'(t)=2t-3t^2=t(2-3t)$より，

| $t$  | $0$ |              | $2/3$ |              | $1$ |
|:------:|:-----:|:------------:|:-------:|:------------:|:-----:|
| $f'$ |       |    $+$     |  $0$  |    $-$     |       |
| $f$  |       | $\nearrow$ |         | $\searrow$ |       |

より$t=2/3$（$x^2=2/3$）で最大．この時

$$
\begin{align*}
x^2\sqrt{1-x^2}=\sqrt{f(2/3)}=\frac23\sqrt{1-\frac23}=\frac23\cdot\frac1{\sqrt3}=\frac{2\sqrt3}9
\end{align*}
$$

したがって，

$$
\begin{align*}
V_n=\frac n3\sin\frac\pi n\cos\frac\pi n\cdot\frac{2\sqrt3}9=\frac{2\sqrt3}{27}\,n\sin\frac\pi n\cos\frac\pi n
\end{align*}
$$

**(2)** $n\sin(\pi/n)=\pi\cdot\dfrac{\sin(\pi/n)}{\pi/n}\to\pi$（$n\to\infty$），$\cos(\pi/n)\to1$だから，

$$
\begin{align*}
\lim_{n\to\infty}V_n=\frac{2\sqrt3}{27}\cdot\pi\cdot1=\frac{2\sqrt3\,\pi}{27}
\end{align*}
$$