---
university: "titech"
category: "zenki"
year: "1971"
question: "6"
type: "solution"
title: "TITECH 1971 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$0<\alpha,\beta<1 \quad \cdots \text{①}$

1.  
$$
\begin{align*}
p_{n+1} = \alpha p_n + (1-\beta)(1-p_n)
\end{align*}
$$

2.  (1)から
  

$$
\begin{align*}
p_{n+1} = (\alpha+\beta-1)p_n + (1-\beta)
\end{align*}
$$

  

$$
\begin{align*}
t = \frac{1-\beta}{2-(\alpha+\beta)}
\end{align*}
$$

  とすると
  

$$
\begin{align*}
p_{n+1}-t = (\alpha+\beta-1)(p_n-t)
\end{align*}
$$

  等比数列の公式から
  

$$
\begin{align*}
p_n = (\alpha+\beta-1)^{n-1}(p_1-t)+t
\end{align*}
$$

  $-1<\alpha+\beta-1<1$（$\because$①）から，
  

$$
\begin{align*}
p_n \to t = \frac{1-\beta}{2-(\alpha+\beta)}
\end{align*}
$$