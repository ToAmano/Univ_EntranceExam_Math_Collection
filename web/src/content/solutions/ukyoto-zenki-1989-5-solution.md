---
university: "ukyoto"
category: "zenki"
year: "1989"
question: "5"
type: "solution"
title: "UKYOTO 1989 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 立方体の6面をA, B, C, D, E, Fとする。Aにぬる色を固定すると、対面も同じ色でぬらなければならない。のこりの側面の色のぬり方は、
2色 $\alpha, \beta$ とすると Cにどちらをぬるかの2通りである。以上から

$$
\begin{align*}
P(N) = \left(\frac{1}{N}\right)^5 {}_{N-1}P_2 = \frac{(N-1)(N-2)}{N^5} \quad \text{//}
\end{align*}
$$

さて、$x = \frac{1}{N} \ (0 < x \le \frac{1}{3})$ とすると、

$$
\begin{align*}
P(N) = x^3(1-x)(1-2x)
\end{align*}
$$

$$
\begin{align*}
\frac{dP}{dx} = 10x^4 - 12x^3 + 3x^2 = 10x^2 \left(x - \frac{6+\sqrt{6}}{10}\right)\left(x - \frac{6-\sqrt{6}}{10}\right)
\end{align*}
$$

で、$0 < x \le \frac{1}{3}$ より、$\frac{dP}{dx} > 0$ つまり $P$ は $x$ について単調増加だから、$N$ について単調減少。
したがって、

$$
\begin{align*}
\begin{cases} a < b \text{ のとき } P(a) > P(b) \\ a > b \text{ のとき } P(b) > P(a) \end{cases} \quad \text{//}
\end{align*}
$$