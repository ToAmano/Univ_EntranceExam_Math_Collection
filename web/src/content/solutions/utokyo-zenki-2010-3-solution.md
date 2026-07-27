---
university: "utokyo"
category: "zenki"
year: "2010"
question: "3"
type: "solution"
title: "UTOKYO 2010 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (1) はじめの操作で場合分けする。
$1^\circ \ 0 \le x \le 15$
$P_m(x) = \frac{1}{2} P_{m-1}(2x) + \frac{1}{2} P_{m-1}(0)$ であり、$P_{m-1}(0) = 0$ だから、

$$
\begin{align*}
P_m(x) = \frac{1}{2} P_{m-1}(2x)
\end{align*}
$$

$2^\circ \ 16 \le x \le 30$
$P_m(x) = \frac{1}{2} P_{m-1}(2x-30) + \frac{1}{2} P_{m-1}(30)$ であり、$P_{m-1}(30) = 1$ から、

$$
\begin{align*}
P_m(x) = \frac{1}{2} P_{m-1}(2x-30) + \frac{1}{2}
\end{align*}
$$

以上まとめて、

$$
\begin{align*}
P_m(x) = \begin{cases} \frac{1}{2} P_{m-1}(2x) & (0 \le x \le 15) \\ \frac{1}{2} P_{m-1}(2x-30) + \frac{1}{2} & (16 \le x \le 30) \end{cases}
\end{align*}
$$

(2) (1)から、

$$
\begin{align*}
P_{2n+2}(10) = \frac{1}{2} P_{2n+1}(20) = \frac{1}{2}\left(\frac{1}{2} P_{2n}(10) + \frac{1}{2}\right) = \frac{1}{4} P_{2n}(10) + \frac{1}{4}
\end{align*}
$$

であり、

$$
\begin{align*}
P_{2n+2}(10) - \frac{1}{3} = \frac{1}{4} \left(P_{2n}(10) - \frac{1}{3}\right)
\end{align*}
$$

となる。$P_2(10) = \frac{1}{4}$ だから、くり返し用いて、

$$
\begin{align*}
P_{2n}(10) = \left(\frac{1}{4}\right)^{n-1} \left(\frac{1}{4} - \frac{1}{3}\right) + \frac{1}{3} = \frac{1}{3} \left\{ 1 - \left(\frac{1}{4}\right)^n \right\}
\end{align*}
$$

(3) (1) から

$$
\begin{align*}
P_{4n+4}(6) &= \frac{1}{2} P_{4n+3}(12) = \frac{1}{4} P_{4n+2}(24) = \frac{1}{4}\left(\frac{1}{2} P_{4n+1}(18) + \frac{1}{2}\right)\\&= \frac{1}{8}\left(\frac{1}{2} P_{4n}(6) + \frac{1}{2}\right) + \frac{1}{8} = \frac{1}{16} P_{4n}(6) + \frac{3}{16}
\end{align*}
$$

$$
\begin{align*}
\therefore P_{4n+4}(6) - \frac{1}{5} = \frac{1}{16} \left(P_{4n}(6) - \frac{1}{5}\right)
\end{align*}
$$

となる。$P_4(6) = \frac{3}{16}$ だから、くり返し用いて、

$$
\begin{align*}
P_{4n}(6) = \left(\frac{1}{16}\right)^{n-1} \left(\frac{3}{16} - \frac{1}{5}\right) + \frac{1}{5} = \frac{1}{5} \left\{ 1 - \left(\frac{1}{16}\right)^n \right\}
\end{align*}
$$