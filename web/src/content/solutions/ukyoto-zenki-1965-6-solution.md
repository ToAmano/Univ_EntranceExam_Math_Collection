---
university: "ukyoto"
category: "zenki"
year: "1965"
question: "6"
type: "solution"
title: "UKYOTO 1965 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

$$
\begin{align*}
\int_1^x (x - t) f(x) \, dt = x^4 - 2x^2 + 1 \dots \text{①}
\end{align*}
$$

$$
\begin{align*}
(\text{左辺}) &= x f(x) \int_1^x dt - f(x) \int_1^x t \, dt \\&= x f(x) (x - 1) - f(x) \frac{1}{2}(x^2 - 1) \\&= \frac{1}{2} f(x) (x - 1)^2
\end{align*}
$$

$$
\begin{align*}
(\text{右辺}) = (x + 1)^2 (x - 1)^2
\end{align*}
$$

だから、①が $1 < x$ の全ての $x$ で成立する時

$$
\begin{align*}
f(x) = 2(x + 1)^2
\end{align*}
$$

であるから、$f(x) = 2(x + 1)^2$ \hfill $\mathbin{/\mkern-5mu/}$

\bigskip

|  |
|:---|
| 問題文の $f(x)$ が $f(t)$ の可能性が有り、その場合は微分をくり返せばよい。 |
| $\Rightarrow$ 確認したところ、$f(t)$ だったので以下に解答をのせておく。 |

\bigskip

[**解2**]

$$
\begin{align*}
\int_1^x (x - t) f(t) \, dt = x^4 - 2x^2 + 1
\end{align*}
$$

$$
\begin{align*}
\iff \int_1^x f(t) \, dt + x f(x) - x f(x) = 4x^3 - 4x \quad (x = 1 \text{で与式が成立})
\end{align*}
$$

両辺 $x$ で微分して

$$
\begin{align*}
f(x) = 12x^2 - 4 \quad \mathbin{/\mkern-5mu/}
\end{align*}
$$