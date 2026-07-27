---
university: "titech"
category: "zenki"
year: "1968"
question: "5"
type: "solution"
title: "TITECH 1968 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$_{2n}P_n = \frac{(2n)!}{n!}$ だから，$A_n = \sqrt[n]{_{2n}P_n}$ とすると，$A_n > 0$ で

$$
\begin{align*}
\log A_n = \frac{1}{n}\log_{2n}P_n = \frac{1}{n}\sum_{k=n+1}^{2n}\log k
\end{align*}
$$

だから，

$$
\begin{align*}
\log\left(\frac{1}{n} A_n\right)&= -\log n + \frac{1}{n}\sum_{k=n+1}^{2n}\log k \\&= \frac{1}{n}\sum_{k=n+1}^{2n}\log\frac{k}{n}\\&\xrightarrow{n \to \infty}\int_{1}^{2}\log x \, dx = [x(\log x - 1)]_1^2 = 2(\log 2 - 1) - 1(-1) \\&= 2 \log 2 - 1 = \log\frac{4}{e}
\end{align*}
$$

となり，$\log x$ の連続性から，

$$
\begin{align*}
\frac{1}{n} A_n \longrightarrow\frac{4}{e}\quad(n \to +\infty)
\end{align*}
$$