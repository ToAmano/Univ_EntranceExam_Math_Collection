---
university: "utokyo"
category: "zenki"
year: "1993"
question: "4"
type: "solution"
title: "UTOKYO 1993 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 $p,q \in \mathbb{R}$ とする。

$$
\begin{align*}
(f(x))^2 = x^{2n} + p^2 x^2 + q^2 + 2(p x^{n+1} + q x^n + pq x)
\end{align*}
$$

だから,

$$
\begin{align*}
I = \int_0^1 (x^{2n} + p^2 x^2 + q^2) \, dx + \int_{-1}^1 (p x^{n+1} + q x^n) \, dx \quad \dots \text{①}
\end{align*}
$$

である。

\bigskip

$1^\circ$ $n \in \text{odd}$ の時\\
①から

$$
\begin{align*}
I &= \int_0^1 (x^{2n} + p^2 x^2 + q^2) \, dx + 2 \int_0^1 p x^{n+1}\, dx \\&= p^2 \int_0^1 x^2 \, dx + 2p \int_0^1 x^{n+1}\, dx + q^2 \int_0^1 1 \, dx + \int_0^1 x^{2n}\, dx \\&= \frac{1}{3} p^2 + \frac{2}{n+2} p + q^2 + \frac{1}{2n+1}\\&= \frac{1}{3}\left( p + \frac{3}{n+2}\right)^2 + q^2 - \frac{3}{(n+2)^2} + \frac{1}{2n+1}
\end{align*}
$$

だから、$n \in \mathbb{N}$ より $(p,q) = \left(-\frac{3}{n+2}, 0\right)$ で $\min I = \frac{1}{2n+1} - \frac{3}{(n+2)^2}$

\bigskip

$2^\circ$ $n \in \text{even}$ の時\\
①から

$$
\begin{align*}
I &= \int_0^1 (x^{2n} + p^2 x^2 + q^2 + 2q x^n) \, dx \\&= q^2 + \frac{2q}{n+1} + \frac{1}{3} p^2 + \frac{1}{2n+1}\\&= \left( q + \frac{1}{n+1}\right)^2 + \frac{1}{3} p^2 + \frac{1}{2n+1} - \frac{1}{(n+1)^2}
\end{align*}
$$

から $(p,q) = \left(0, -\frac{1}{n+1}\right)$ で $\min I = \frac{1}{2n+1} - \frac{1}{(n+1)^2}$

\bigskip

以上まとめて,

$$
\begin{align*}
\begin{cases}
n \in \text{odd} \dots (p,q) = \left(-\frac{3}{n+2}, 0\right) \text{の時} \quad \min I = \frac{(n-1)^2}{(2n+1)(n+2)^2} \\[1.5ex]
n \in \text{even} \dots (p,q) = \left(0, -\frac{1}{n+1}\right) \text{の時} \quad \min I = \frac{n^2}{(2n+1)(n+1)^2}
\end{cases}
\quad \text{\#\#}
\end{align*}
$$