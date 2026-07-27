---
university: "ukyoto"
category: "zenki"
year: "1968"
question: "2"
type: "solution"
title: "UKYOTO 1968 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] 3辺の長さ $a, b, c$ ($a \leqq b \leqq c$) とすると, 三角不等式から

$$
\begin{align*}
a \leqq b \leqq c < a + b
\end{align*}
$$

が成り立つ.

$$
\begin{align*}
a + b - c \geqq 20 + 20 - 36 \geqq 0
\end{align*}
$$

だから, 問題文の中にある長さのうち任意に3つ持ってくると, 三角形をつくることができる. から, 9つの辺の長さから3つをえらぶ方法を考えて

1.  3辺とも違う長さ $\dots{}_9\mathrm{C}_3 = 84$ 通り

2.  2等辺三角形 $\dots 2 \cdot{}_9\mathrm{C}_2 = 72$ 通り

3.  正三角形 $\dots 9$ 通り

よって

$$
\begin{align*}
84 + 72 + 9 = 165 \text{ 通り}
\end{align*}
$$

### [本番のミス]

“相似”と“合同”をまちがえていた