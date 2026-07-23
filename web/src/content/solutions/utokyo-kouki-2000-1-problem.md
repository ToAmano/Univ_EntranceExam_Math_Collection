---
university: "utokyo"
category: "kouki"
year: "2000"
question: "1"
type: "problem"
title: "UTOKYO 2000 kouki Q1 (problem)"
---

$k$ を正整数とし, $x$ を変数とする $k$ 次多項式 $P_k(x)$ について次の条件
\[
  (C) \quad
  \begin{cases}
    P_k(x) - P_k(x-1) = x^{k-1} \\
    P_k(0) = 0
  \end{cases}
\]
を考える. ただし, $x^0 = 1$ と定める. このとき, 次の問に答えよ.

\begin{enumerate}
\item $k = 1, 2$ に対し, $P_k(x)$ を求めよ.
  \item すべての $k \ge 3$ に対し, 条件 $(C)$ を満たす $P_k(x)$ が存在し, しかもただ一つであることを示せ.
  \item 正整数 $k$ に対し, $k$ 次の多項式 $Q_k(x)$ を次の条件が成立するように定める.
        \[
          \begin{cases}
            Q_k(0) = Q_k(1) = \cdots = Q_k(k-1) = 0 \\
            Q_k(k) = 1
          \end{cases}
        \]
        このとき, $k$ 個の整数 $c_1, c_2, \dots, c_k$ がそれぞれただ一つ存在して,
        \[
          P_k(x) = \sum_{j=1}^k c_j Q_j(x)
        \]
        と表されることを示せ.
\end{enumerate}