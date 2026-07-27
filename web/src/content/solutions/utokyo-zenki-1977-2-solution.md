---
university: "utokyo"
category: "zenki"
year: "1977"
question: "2"
type: "solution"
title: "UTOKYO 1977 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $a_1, a_2, b_1, b_2 \in \mathbb{Q} \quad \dots *$

1.  $a = \sqrt{a_1^2 + a_2^2}, \quad b = \sqrt{b_1^2 + b_2^2}, \quad c = \overline{AB} = \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2}$

2.  $\cos\theta = \frac{a^2 + b^2 - c^2}{2ab}, \quad \sin\theta = \frac{|a_1 b_2 - a_2 b_1|}{ab} \quad \dots \text{①}$

である。$a^2, b^2, c^2 \in \mathbb{Q}$ に

1.  $ab \in \mathbb{Q}$ の時、$a^2, b^2, c^2 \in \mathbb{Q}$ と ①から
  

$$
\begin{align*}
\text{(i)} \to \text{(ii)}, \quad \text{(i)} \to \text{(iii)}
\end{align*}
$$

  が成り立つ。

2.  $\cos\theta \in \mathbb{Q}$ の時
  \begin{enumerate}

3.  $\cos\theta \neq 0$ なら、①から $ab \in \mathbb{Q}$ である ($\because *$ )

4.  $\cos\theta = 0$ なら、$\sin\theta = \pm 1$ であり、①から $ab \in \mathbb{Q}$ である ($\because *$ )

  以上から $\text{(ii)} \to \text{(i)}$ が成り立つ。

  \item[(iii)] $\sin\theta \in \mathbb{Q}$ の時
  

1.  $\sin\theta \neq 0$ なら、同様に $ab \in \mathbb{Q}$

2.  $\sin\theta = 0$ なら、$\cos\theta = \pm 1$ となり、同様に $ab \in \mathbb{Q}$

  以上から、$\text{(iii)} \to \text{(i)}$ が成り立つ。
\end{enumerate}

したがって、$\text{(i)} \iff \text{(ii)}$, $\text{(i)} \iff \text{(iii)}$ だから、$\text{(ii)} \iff \text{(iii)}$ であり、示された。