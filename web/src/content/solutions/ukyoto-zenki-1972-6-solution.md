---
university: "ukyoto"
category: "zenki"
year: "1972"
question: "6"
type: "solution"
title: "UKYOTO 1972 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] まず, $A = \sum_{k=1}^n a_k$ とおいて, $E = \frac{1}{n} A$ である $\cdots$ ①. 次に $F$ について, 取り出した2枚を区別して考える. 1枚目の数 $X$, 2枚目の数 $Y$ とおくと

$$
\begin{align*}
F = E(X+Y) = E(X) + E(Y)
\end{align*}
$$

である. 明らかに $E(X) = E \cdots$ ② である. 以下 $E(Y)$ について

$$
\begin{align*}
E(Y) = \frac{1}{n} \cdot \left( \sum_{k=1}^n \frac{A - a_k}{n-1} \right) = \frac{1}{n} \cdot \frac{n-1}{n-1} A = \frac{1}{n} A \quad \cdots \text{③}
\end{align*}
$$

①, ②, ③から

$$
\begin{align*}
F = \frac{1}{n} A + \frac{1}{n} A = 2E \quad \text{答}
\end{align*}
$$