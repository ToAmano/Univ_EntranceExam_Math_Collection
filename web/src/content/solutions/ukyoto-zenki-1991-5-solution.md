---
university: "ukyoto"
category: "zenki"
year: "1991"
question: "5"
type: "solution"
title: "UKYOTO 1991 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $n$回目の試行前袋に赤玉が $i$ コ入っている確率 $P_{i,n}$ とおく。

$$
\begin{align*}
(1)\ \begin{cases}
n+1\text{回目の試行前に赤玉が1コ} \cdots \quad Q_{1,n} + P_{2,n} \\
\qquad \qquad \text{〃} \qquad \qquad 2\text{コ} \cdots \quad Q_{2,n} + P_{3,n} \\
\qquad \qquad \text{〃} \qquad \qquad 3\text{コ} \cdots \quad Q_{3,n}
\end{cases}
\end{align*}
$$

又

$$
\begin{align*}
Q_{1,n} = (N+2)P_{1,n} \quad Q_{2,n} = \frac{N+1}{2} P_{2,n} \quad Q_{3,n} = \frac{N}{3} P_{3,n}
\end{align*}
$$

だから

$$
\begin{align*}
\begin{cases}
P_{1,n+1} = \frac{1}{N+3} ( (N+2) P_{1,n} + P_{2,n} ) \\
P_{2,n+1} = \frac{2}{N+3} ( \frac{N+1}{2} P_{2,n} + P_{3,n} ) \\
P_{3,n+1} = \frac{3}{N+3} \cdot \frac{N}{3} P_{3,n} = \frac{N}{N+3} P_{3,n}
\end{cases} \cdots \#
\end{align*}
$$

(2) $p_n = P_{1,n} + P_{2,n} + P_{3,n}$ だから(1)より

$$
\begin{align*}
p_{n+1} = \frac{N+2}{N+3} p_n \quad \cdots \text{①}
\end{align*}
$$

又、$p_1 = \frac{3}{N+3}$ だから、①と等比数列の公式から

$$
\begin{align*}
p_n = \left(\frac{N+2}{N+3}\right)^{n-1} \frac{3}{N+3}
\end{align*}
$$