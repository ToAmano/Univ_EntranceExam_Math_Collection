---
university: "titech"
category: "zenki"
year: "1984"
question: "4"
type: "solution"
title: "TITECH 1984 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$F=\displaystyle\int_0^1e^x|x-a|dx$とおく．

**⑦ $a\le0$の時**

$$
\begin{align*}
F=-a\int_0^1e^xdx+\int_0^1xe^xdx, \qquad\frac{dF}{da}=-\int_0^1e^xdx<0
\end{align*}
$$

より，$F$は$a$の単調減少関数

**⑦ $a\ge1$の時**

⑦と同じく，$F$は$a$の単調増加関数

従って，$0\le a\le1$の時$F$は最小値をとる．$f(x)=e^x(x-a)$とおく．

$$
\begin{align*}
F=-\int_0^af(x)dx+\int_a^1f(x)dx
\end{align*}
$$

$g(x)=e^x(x-a-1)$とおくと$g'(x)=f(x)$であって，

$$
\begin{align*}
F=g(1)+g(0)-2g(a)
\end{align*}
$$

$$
\begin{align*}
=-ea-a-1+2e^a
\end{align*}
$$

$$
\begin{align*}
\frac{dF}{da}=-e-1+2e^a
\end{align*}
$$

より，下表を得る．

| $a$  | $0$ |              | $\log\dfrac{e+1}{2}$ |              | $1$ |
|:------:|:-----:|:------------:|:----------------------:|:------------:|:-----:|
| $F'$ |       |    $-$     |         $0$          |    $+$     |       |
| $F$  |       | $\searrow$ |                        | $\nearrow$ |       |

したがって，$a=\log\dfrac{e+1}{2}$で$\min F$をとる．