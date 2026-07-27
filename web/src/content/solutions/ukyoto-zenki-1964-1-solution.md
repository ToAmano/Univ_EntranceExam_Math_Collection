---
university: "ukyoto"
category: "zenki"
year: "1964"
question: "1"
type: "solution"
title: "UKYOTO 1964 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解]
(イ) まず、2正数 $a, b$ に対し、$a+b \geqq 2\sqrt{ab}$ であることを示す。両辺正から2乗して良く、

$$
\begin{align*}
a+b \geqq 2\sqrt{ab} \iff (a-b)^2 \geqq 0
\end{align*}
$$

より、示された。$a = a_1+a_2$, $b = a_3+a_4$ として ($\because a_k > 0$)

$$
\begin{align*}
\frac{1}{2}(a_1+a_2+a_3+a_4) \geqq \sqrt{(a_1+a_2)(a_3+a_4)} \quad \cdots \text{①}
\end{align*}
$$

ここでさらに、

$$
\begin{align*}
\sqrt{(a_1+a_2)(a_3+a_4)} \geqq \sqrt{2\sqrt{a_1 a_2} \cdot 2\sqrt{a_3 a_4}} = 2 \sqrt[4]{a_1 a_2 a_3 a_4} \quad \cdots \text{②}
\end{align*}
$$

だから、①, ②から

$$
\begin{align*}
\frac{1}{4}(a_1+a_2+a_3+a_4) \geqq \sqrt[4]{a_1 a_2 a_3 a_4}_{\text{\fbox{同}}}
\end{align*}
$$

(ロ) $\frac{a_k}{b_k} > 0$ のため、(1) で $a_k$ に $\frac{a_k}{b_k}$ を代入して、

$$
\begin{align*}
\sum_{k=1}^4 \frac{a_k}{b_k} \geqq 4 \sqrt[4]{\frac{a_1 a_2 a_3 a_4}{b_1 b_2 b_3 b_4}} = 4 \quad (\because \{a_1, \dots, a_4\} = \{b_1, b_2, b_3, b_4\})
\end{align*}
$$

よって示された。$_{\text{\fbox{同}}}$