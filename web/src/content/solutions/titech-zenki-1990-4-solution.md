---
university: "titech"
category: "zenki"
year: "1990"
question: "4"
type: "solution"
title: "TITECH 1990 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$0<x<\dfrac{\pi}{2}\ \cdots$①

$$
\begin{align*}
f(x)=\int_0^x\frac{d\theta}{\cos\theta}+\int_x^{\frac{\pi}{2}}\frac{d\theta}{\sin\theta}
\end{align*}
$$

$$
\begin{align*}
f'(x)=\frac{1}{\cos x}-\frac{1}{\sin x}=\frac{S-C}{CS}\quad(S=\sin x,\ C=\cos x\text{から，下表を得る})
\end{align*}
$$

| $x$  | $0$ |              | $\dfrac{\pi}{4}$ |              | $\dfrac{\pi}{2}$ |
|:------:|:-----:|:------------:|:------------------:|:------------:|:------------------:|
| $f'$ |       |    $-$     |       $0$        |    $+$     |                    |
| $f$  |       | $\searrow$ |                    | $\nearrow$ |                    |

したがって，$f(x)$は$x=\dfrac{\pi}{4}$で最小．

$$
\begin{align*}
\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\frac{d\theta}{\sin\theta}=\int_{\frac{\pi}{4}}^0\frac{-dt}{\sin\left(\frac{\pi}{2}-t\right)}\quad\left(t=\frac{\pi}{2}-\theta\right)
\end{align*}
$$

$$
\begin{align*}
=\int_0^{\frac{\pi}{4}}\frac{d\theta}{\cos\theta}
\end{align*}
$$

からこの時

$$
\begin{align*}
f\left(\frac{\pi}{4}\right)=2\int_0^{\frac{\pi}{4}}\frac{d\theta}{\cos\theta}
\end{align*}
$$

$$
\begin{align*}
=2\int_0^{\frac{\sqrt2}{2}}\frac{1}{1-x^2}dx
\end{align*}
$$

$$
\begin{align*}
=\left[\log(x+1)-\log(1-x)\right]_0^{\frac{\sqrt2}{2}}
\end{align*}
$$

$$
\begin{align*}
=\log\frac{1+\frac{\sqrt2}{2}}{1-\frac{\sqrt2}{2}}=\log\frac{2+\sqrt2}{2-\sqrt2}
\end{align*}
$$