---
university: "utokyo"
category: "zenki"
year: "1993"
question: "2"
type: "solution"
title: "UTOKYO 1993 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 (1) $a_n$ を 2 でわったあまりを $b_n$ とすると、

$$
\begin{align*}
\begin{cases}
b_1 = 1, \quad b_2 = 1 \\
b_{n+2} \equiv 3b_{n+1} - 7b_n \equiv b_{n+1} - b_n
\end{cases}
\end{align*}
$$

である。「$a_n$ が偶数 $\iff n \equiv 0 \pmod 3$」を帰納的に示す。

$1^\circ$ $n=1,2,3$ の時,

$$
\begin{align*}
b_1 = 1, \quad b_2 = 1, \quad b_3 = 0 \quad \text{より、成立}
\end{align*}
$$

$2^\circ$ $n = 3k-2, 3k-1, 3k$ ($k \in \mathbb{N}$) の時 成立とすると,

$$
\begin{align*}
b_{3k+1} = 1, \quad b_{3k+2} = 1, \quad b_{3k+3} = 0 \quad \text{より},
\end{align*}
$$

$n = 3k+1 \sim 3k+3$ でも成立。

以上より示された。(逆も成立).

\bigskip

(2) $a_n$ が 5 の倍数になる条件を調べる。$a_n$ を 5 でわったあまりを $c_n$ とおく。

$$
\begin{align*}
\begin{cases}
c_1 = 1, \quad c_2 = 3 \\
c_{n+2} \equiv 3c_{n+1} - 2c_n
\end{cases}
\end{align*}
$$

より、$c_n$ は、$\{1, 3, 2, 0\}$ のくり返しであるから,

$$
\begin{align*}
\text{「} c_n = 0 \iff n \text{ が 4 の倍数} \text{」} \quad \dots \text{①}
\end{align*}
$$

である。(1) と ① より,

$$
\begin{align*}
\text{「} a_n \text{ が 10 の倍数} \iff n \text{ が 12 の倍数} \text{」} \quad \text{\#\#}
\end{align*}
$$