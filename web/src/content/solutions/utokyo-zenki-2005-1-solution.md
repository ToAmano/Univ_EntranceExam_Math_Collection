---
university: "utokyo"
category: "zenki"
year: "2005"
question: "1"
type: "solution"
title: "UTOKYO 2005 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 題意を M.I. で示す. $n=1$ の時

$$
\begin{align*}
f'(x) = \frac{1 - \log x}{x^2}
\end{align*}
$$

だから $a_1 = 1, b_1 = -1$ とすれば良い. $n=k$ での成立を仮定する.

$$
\begin{align*}
f^{(k+1)}(x) &= \frac{b_k \cdot x^k - (k+1) \cdot x^k (a_k + b_k \log x)}{(x^{k+1})^2}\\&= \frac{(b_k - (k+1) a_k) + (-(k+1) b_k) \log x}{x^{k+2}}
\end{align*}
$$

だから

$$
\begin{align*}
\begin{cases}
a_{k+1} = -(k+1) a_k + b_k \\
b_{k+1} = -(k+1) b_k
\end{cases}
\end{align*}
$$

とすれば $n=k+1$ でも成立.

\bigskip

以上より示された. 同漸化式は

$$
\begin{align*}
\begin{cases}
a_{n+1} = -(n+1) a_n + b_n &, a_1 = 1 \\
b_{n+1} = -(n+1) b_n &, b_1 = -1
\end{cases}
\end{align*}
$$

\bigskip

(2) (1)から, $b_n = (-1)^n n!$ であるから,

$$
\begin{align*}
a_{n+1} = -(n+1) a_n + (-1)^n \cdot n! \quad \cdots \textcircled{1}
\end{align*}
$$

$c_n = \frac{a_n}{(-1)^n n!}$ とおいて ($c_1 = -1$), \textcircled{1}の両辺を $(-1)^{n+1} (n+1)!$ で割ると

$$
\begin{align*}
c_{n+1} = c_n + \frac{1}{-(n+1)}
\end{align*}
$$

だから, 階差数列より $n \ge 2$ の時

$$
\begin{align*}
c_n &= c_1 + \sum_{k=2}^n \frac{1}{-k}\\&= -h_n
\end{align*}
$$

$n=1$ でもこれは成立するから

$$
\begin{align*}
a_n = (-1)^{n+1} \cdot n! \cdot h_n
\end{align*}
$$

である.