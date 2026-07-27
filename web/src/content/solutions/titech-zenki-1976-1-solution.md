---
university: "titech"
category: "zenki"
year: "1976"
question: "1"
type: "solution"
title: "TITECH 1976 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$x^4$ を $P(x)$ でわった商を $A(x)$，あまりを $Q(x)$ とする．又，$x^5$ を $P(x)$ でわった商を $B(x)$ とする．

$$
\begin{align*}
\begin{cases}
x^4=A(x)\cdot P(x)+Q(x) \\
x^5=B(x)\cdot P(x)+Q(x)
\end{cases}
\end{align*}
$$

したがって，辺々引いて，

$$
\begin{align*}
x^4(x-1)=\{B(x)-A(x)\}P(x)
\end{align*}
$$

だから $x^4(x-1)$ は $P(x)$ で割り切れるので，$a$ を係数として

$$
\begin{align*}
P(x)=ax^3, \quad a(x-1)\cdot x^2
\end{align*}
$$

である．題意から，$Q(x)\ne0$ だから前者は不適で，$P(x)=a(x-1)\cdot x^2$ である． $\cdots$①

次に，$f(x)$ を $P(x)$ でわった商 $C(x)$，$f(x)\cdot x$ を $P(x)$ でわった商を $D(x)$ とする．

$$
\begin{align*}
\begin{cases}
f(x)=C(x)\cdot P(x)+r(x) & \cdots \text{②} \\
xf(x)=D(x)\cdot P(x) & \cdots \text{③}
\end{cases}
\end{align*}
$$

②$\times x$ と③を辺々引いて，

$$
\begin{align*}
0=\{x\cdot C(x)-D(x)\}\cdot P(x)+x\cdot r(x)
\end{align*}
$$

より，$r(x)\cdot x$ は $P(x)$ で割り切れ，かつ①より，$r(x)$ は2次以下だから，

$$
\begin{align*}
r(x)=ax(x-1)
\end{align*}
$$

である．$r(x)$ の最高次係数1から，$a=1$ として，

$$
\begin{align*}
r(x)=x(x-1)
\end{align*}
$$