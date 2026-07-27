---
university: "titech"
category: "zenki"
year: "1983"
question: "4"
type: "solution"
title: "TITECH 1983 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$A+B+C=\pi,\ A,B,C>0\ \cdots$①

$$
\begin{align*}
F=\sin3A+\sin3B+\sin3(\pi-A-B) \quad(\because①)
\end{align*}
$$

$$
\begin{align*}
=\sin3A+\sin3B+\sin3(A+B)
\end{align*}
$$

対称性から$A=B$として良い．$0<A<\dfrac{\pi}{2}\ \cdots$②であり，

$$
\begin{align*}
F=2\sin3A+\sin6A
\end{align*}
$$

$$
\begin{align*}
\frac{dF}{dA}=6\cos3A+6\cos6A \quad\cdots\text{③}
\end{align*}
$$

$t=\cos3A$とおくと，

$$
\begin{align*}
\frac{③}{6}=2t^2+t-1=(t+1)(2t-1)
\end{align*}
$$

下表を得る．

| $A$  | $0$ |              | $20^\circ$ |              | $\frac{\pi}{2}$ |
|:------:|:-----:|:------------:|:------------:|:------------:|:-----------------:|
| $t$  | $1$ |              | $\frac12$  |              |       $0$       |
| $F'$ |       |    $+$     |    $0$     |    $-$     |                   |
| $F$  |       | $\nearrow$ |              | $\searrow$ |                   |

$A=20^\circ$の時，$\max F=\dfrac{3\sqrt3}{2}$

$A\to0$の時，$F\to0$

$A\to\dfrac{\pi}{2}$の時，$F\to-2$

以上から

$$
\begin{align*}
\text{(1)}\quad\frac{3\sqrt3}{2}\qquad\qquad\text{(2)}\quad -2<F\le\frac{3\sqrt3}{2}
\end{align*}
$$