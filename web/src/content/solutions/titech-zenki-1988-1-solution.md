---
university: "titech"
category: "zenki"
year: "1988"
question: "1"
type: "solution"
title: "TITECH 1988 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$$
\begin{align*}
a_{n+1}=\frac{1}{(n+1)^2}a_n^2+1, \qquad a_1=1 \quad\cdots\text{①}
\end{align*}
$$

$n\ge2$の時，$a_n<1+\dfrac1n$であることを帰納的に示す．$a_2=\dfrac54$，$1+\dfrac12=\dfrac32=\dfrac64$より，$n=2$で成立．以下$n=k\ (\in\mathbb{N}_{\ge2})$での成立を仮定し，$n=k+1$での成立を示す．①より

$$
\begin{align*}
a_{k+1}<\frac{(1+\frac1k)^2}{(k+1)^2}+1=1+\frac{1}{k^2}<1+\frac{1}{k+1}\quad(\because k\ge2より)
\end{align*}
$$

$$
\begin{align*}
\left(k^2-k-1=\left(k-\frac{1+\sqrt5}{2}\right)\left(k-\frac{1-\sqrt5}{2}\right),\ \ 2>\frac{1+\sqrt5}{2}より\right)
\end{align*}
$$

だから，$n=k+1$でも成立．以上から，$a_n<1+\dfrac1n$．一方，①から$1\le a_n$だから

$$
\begin{align*}
1\le a_n<1+\frac1n \quad(a_1=1,\ 1+1=2より)
\end{align*}
$$

はさみうちから$a_n\to1$