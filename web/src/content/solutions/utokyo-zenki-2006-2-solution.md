---
university: "utokyo"
category: "zenki"
year: "2006"
question: "2"
type: "solution"
title: "UTOKYO 2006 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解]
(1) $n=2$の時.

1.  $\times$が1つの時, $\times\bigcirc\bigcirc$ となり, $p(1-p)$

2.  $\times$が2つの時, $\times\times\bigcirc\bigcirc$, $\times\bigcirc\times\bigcirc$ となり, $p^2(1-p) + (1-p)^3$

以上から,

$$
\begin{align*}
p_2 = p(1-p) + p^2(1-p) + (1-p)^3 = (1-p)(2p^2-p+1)
\end{align*}
$$

(2) $n \ge 3$の時. $\times$が1つの時, $\times\underbrace{\bigcirc\cdots\bigcirc}_{n\text{コ}}$ となり, 確率 $(1-p) \cdot p^{n-1}$ である. $\cdots$ ①

$\times$が2つの時.

$$
\begin{align*}
\begin{cases}
\times\times\bigcirc\cdots\bigcirc \text{ となる時, 確率 } p(1-p)p^{n-1} = (1-p)\cdot p^n \\
\times\bigcirc\cdots\times\cdots\bigcirc \quad \text{"} \quad \text{ 確率 } (n-1)(1-p)^2 \cdot p^{n-2}
\end{cases} \cdots \text{②}
\end{align*}
$$

①, ②から

$$
\begin{align*}
p_n = (1-p) \cdot p^{n-1} + (1-p) \cdot p^n + (n-1) \cdot (1-p)^2 p^{n-2}
\end{align*}
$$