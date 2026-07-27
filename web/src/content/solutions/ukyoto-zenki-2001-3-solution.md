---
university: "ukyoto"
category: "zenki"
year: "2001"
question: "3"
type: "solution"
title: "UKYOTO 2001 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $a_{n+k} = p^{\frac{(n+k)(n+k-1)}{2}}, a_n = p^{\frac{n(n-1)}{2}}$ だから

$$
\begin{align*}
\frac{a_{n+k}}{a_n} = p^{\frac{(n+k)(n+k-1)-n(n-1)}{2}} = 1
\end{align*}
$$

したがって任意の $n \in \mathbb{Z}$ に対し、$f(n) = \frac{1}{2} [ (n+k)(n+k-1)-n(n-1) ]$ が $8$ の倍数なら良い。

$$
\begin{align*}
f(n) = 2kn + k^2 - k
\end{align*}
$$

まず $n=0, 1$ での成立が必要で、以下合同式の法を $8$ として

$$
\begin{eqnarray*}
f(0) &=& k(k-1) \equiv 0 \\
f(1) &=& k(k+1) \equiv 0
\end{eqnarray*}
$$

$k$ と $k-1$ 、$k$ と $k+1$ は互いに素で、この中に $8$ の倍数は多くとも $1$ つしかないから、
$k \equiv 0$ が必要。逆にこの時、$f(n) \equiv 0$ で十分。以上から

$$
\begin{align*}
k = 8m \ (m \in \mathbb{Z})
\end{align*}
$$