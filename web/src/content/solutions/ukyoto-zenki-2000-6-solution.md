---
university: "ukyoto"
category: "zenki"
year: "2000"
question: "6"
type: "solution"
title: "UKYOTO 2000 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $2 \le n, \ 0 \le k \le 4, \ n, k \in \mathbb{Z}$ $\cdots$ ①
$1, 2, \dots, 6$ の中には、5でわって1あまるものが2つ、他が1つずつある。

(1) 

$$
\begin{align*}
P_{n+1}(0) &= \frac{1}{6}\{ P_n(0) + \dots + P_n(3) \} + \frac{1}{3} P_n(4) = \frac{1}{6}(1 + P_n(4)) \\
P_{n+1}(1) &= \frac{1}{6}\{ P_n(1) + \dots + P_n(4) \} + \frac{1}{3} P_n(0) = \frac{1}{6}(1 + P_n(0)) \\
P_{n+1}(2) &= \frac{1}{6}\{ P_n(0) + P_n(2) + \dots + P_n(4) \} + \frac{1}{3} P_n(1) = \frac{1}{6}(1 + P_n(1)) \\
P_{n+1}(3) &= \frac{1}{6}\{ P_n(0) + P_n(1) + P_n(3) + P_n(4) \} + \frac{1}{3} P_n(2) = \frac{1}{6}(1 + P_n(2)) \\
P_{n+1}(4) &= \frac{1}{6}\{ P_n(0) + P_n(1) + P_n(2) + P_n(4) \} + \frac{1}{3} P_n(3) = \frac{1}{6}(1 + P_n(3))
\end{align*}
$$

(2) $\sum_{k=0}^4 P_n(k) = 1$ だから、$m_n \le P_n(k) \le M_n$ を $k$ について足して

$$
\begin{align*}
5m_n \le 1 \le 5M_n
\end{align*}
$$

$$
\begin{align*}
\therefore m_n \le \frac{1}{5} \le M_n \quad (1)
\end{align*}
$$

又、(1)の式から、

$$
\begin{align*}
\frac{1}{6}(1 + m_n) \le P_{n+1}(k) \le \frac{1}{6}(1 + M_n)
\end{align*}
$$

だから、

$$
\begin{align*}
P_{n+1}(k) - P_{n+1}(l) \le \frac{1}{6}(M_n - m_n) \quad (2)
\end{align*}
$$

(3) (2)から、$a_n = M_n - m_n$ として、

$$
\begin{align*}
0 \le a_{n+1} \le \frac{1}{6} a_n
\end{align*}
$$

が成り立つ。くり返し用いて、

$$
\begin{align*}
0 \le a_n \le \left(\frac{1}{6}\right)^{n-1} a_1
\end{align*}
$$

はさみうちの定理より、$a_n \to 0 \ (n \to \infty)$ だから (2) (1) より、

$$
\begin{align*}
M_n, m_n \to \frac{1}{5} \ (n \to \infty)
\end{align*}
$$

さらに $m_n \le P_n(k) \le M_n$ だから、はさみうちより

$$
\begin{align*}
P_n(k) \to \frac{1}{5} \ (n \to \infty)
\end{align*}
$$