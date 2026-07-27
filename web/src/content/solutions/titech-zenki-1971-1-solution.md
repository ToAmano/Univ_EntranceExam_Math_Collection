---
university: "titech"
category: "zenki"
year: "1971"
question: "1"
type: "solution"
title: "TITECH 1971 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$(p, q)$ を直線 $2x+y=1$ 上の格子点とすると $q = 1-2p$ である．また

$$
\begin{align*}
A = \sum_{k=-10}^{10} f(k, pk+q)
\end{align*}
$$

とおく．

$$
\begin{align*}
f(k, pk+q) = f(k, p(k-2)+1)
\end{align*}
$$

$p \to \infty$ の時，$k \neq 2$ に対して $|p(k-2)+1| \to \infty$ となるから $f(k, p(k-2)+1) = 0$ となる．したがって

$$
\begin{align*}
\lim_{p \to \infty} A = f(2, 1)
\end{align*}
$$