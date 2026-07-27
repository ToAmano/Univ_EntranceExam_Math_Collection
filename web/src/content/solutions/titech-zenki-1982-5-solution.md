---
university: "titech"
category: "zenki"
year: "1982"
question: "5"
type: "solution"
title: "TITECH 1982 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

9つの数の平均の小数第1位が1になるのは，9つの数の和$A$が

$$
\begin{align*}
1,\ 10\ \text{の時}\quad(0\le A\le18)
\end{align*}
$$

**$A=1$の時**

1回だけ，他が0の時で，

$$
\begin{align*}
9\left(\frac13\right)^9=\left(\frac13\right)^7
\end{align*}
$$

**$A=10$の時**

| $2$の個数 | $1$の個数 | $0$の個数 |     |
|:-----------:|:-----------:|:-----------:|:---:|
|    $5$    |    $0$    |    $4$    |     |
|    $4$    |    $2$    |    $3$    |     |
|    $3$    |    $4$    |    $2$    |     |
|    $2$    |    $6$    |    $1$    |     |
|    $1$    |    $8$    |    $0$    |     |

上表から，

$$
\begin{align*}
\frac{{}_9C_5+{}_9C_4\cdot{}_5C_2+{}_9C_3\cdot{}_6C_4+{}_9C_2\cdot{}_7C_6+{}_9C_1}{3^9}
\end{align*}
$$

$$
\begin{align*}
=\left(\frac13\right)^9(126+1260+1260+252+9)=\left(\frac13\right)^9\cdot2907=\left(\frac13\right)^7\cdot323
\end{align*}
$$

以上から

$$
\begin{align*}
\left(\frac13\right)^7\cdot324=\frac{4}{3^3}=\frac{4}{27}
\end{align*}
$$