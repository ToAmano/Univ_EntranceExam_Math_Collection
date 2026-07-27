---
university: "utokyo"
category: "zenki"
year: "2007"
question: "5"
type: "solution"
title: "UTOKYO 2007 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{proof}[解]
$n \in \mathbb{N}, 0 \le m \le n, m \in \mathbb{Z} \quad \cdots ①$

(1) $n$ 回投げて $m$ となるのは以下の時. ($1 \le m \le n-1$)

$$
\begin{align*}
\circ \quad \dots \quad \underbrace{\circ}_{\text{↑ } n-m-1 \text{ 回目ウラ}} \quad \underbrace{\circ}_{\text{↑ } n-m \text{ 回目表}} \quad \dots \quad \circ
\end{align*}
$$

$m=n$ の時, $n$ 回とも表で, $P_n = p^n$. $m=0$ の時, $n$ 回目がウラで, $P_0 = 1-p$.
$1 \le m \le n-1$ の時, 上図から $P_m = (1-p) p^m$ で, $m=0$ の時もこれで良い.

$$
\begin{align*}
P_m = \begin{cases} p^n & (m = n) \\ (1-p) p^m & (m \neq n) \end{cases}
\quad \text{\#}
\end{align*}
$$

(2) $q_m = \sum_{k=0}^m P_k$ である. $m=0$ の時, $q_0 = 1-p$. $m \ge 1$ の時,

$$
\begin{align*}
q_m = \sum_{k=0}^{m-1} P_k + P_m = (1-p) \frac{1-p^m}{1-p} + P_m
\end{align*}
$$

だから, $m=n$ か否かで場合分けし, $m=0$ の時もこれで良いから

$$
\begin{align*}
q_m = \begin{cases} 1 - p^{m+1} & (m \neq n) \\ 1 & (m = n) \end{cases}
\quad \text{\#}
\end{align*}
$$

(3) 2つのブロックを $A, B$ とおく. また, $A, B$ の高さを $a, b$ で表す. 包除原理から,

$$
\begin{align*}
r_m = P(a=m \cap b \le m) + P(b=m \cap a \le m) - P(a=b=m)
\end{align*}
$$

$$
\begin{align*}
= 2 P_m q_m - P_m P_m \quad \cdots ②
\end{align*}
$$

である.

$\cdot$ $m=n$ の時
②及び(1),(2)から

$$
\begin{align*}
r_n = p^n (2 - p^n)
\end{align*}
$$

$\cdot$ $m \neq n$ の時
$1^\circ$ と同様にして

$$
\begin{align*}
r_m = (1-p)p^m \{ 2(1 - p^{m+1}) - (1-p)p^m \} = (1-p)p^m (2 - p^m - p^{m+1})
\end{align*}
$$

以上から,

$$
\begin{align*}
r_m = \begin{cases} p^n (2 - p^n) & (m = n) \\ (1-p)p^m (2 - p^m - p^{m+1}) & (m \neq n) \end{cases}
\quad \text{\#}
\end{align*}
$$

\end{proof}

### [(3) 別解]

$$
\begin{align*}
r_m = \begin{cases} q_m^2 - q_{m-1}^2 & (m \ge 1) \\ q_0^2 & (m = 0) \end{cases}
\end{align*}
$$

だから, (2) から計算できる (以下略).