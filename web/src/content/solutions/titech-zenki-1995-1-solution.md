---
university: "titech"
category: "zenki"
year: "1995"
question: "1"
type: "solution"
title: "TITECH 1995 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$$
\begin{align*}
a(n)=\frac{(n+2)(n+3)(n+4)}{n!}
\end{align*}
$$

**(1)** $a(n)>0$であり，

$$
\begin{align*}
\frac{a(n+1)}{a(n)}=\frac{(n+3)(n+4)(n+5)/(n+1)!}{(n+2)(n+3)(n+4)/n!}=\frac{n+5}{(n+1)(n+2)}\longrightarrow0 \quad(n\to\infty)
\end{align*}
$$

となり，$n$が十分大きい所で比が$1/2$未満になることから，$a(n)\to0$である．

**(2)** $a(1)$から書き出す．

$$
\begin{align*}
a(1)=a(2)=60
\end{align*}
$$

$$
\begin{align*}
a(3)=35,\quad a(4)=14,\quad a(5)=\frac{21}{5},\quad a(6)=1
\end{align*}
$$

$$
\begin{align*}
a(7)<1
\end{align*}
$$

以下，$a(n)$が$n\ge2$で単調減少であることを示す．

$$
\begin{align*}
a(n)-a(n+1)=\frac{(n+3)(n+4)}{(n+1)!}\left[(n+1)(n+2)-(n+5)\right]
\end{align*}
$$

$$
\begin{align*}
=\frac{(n+3)(n+4)}{(n+1)!}(n^2+2n-3)>0 \quad(\because n\ge2)
\end{align*}
$$

より，示された．これと$a(7)<1$，$a_n\to0\ (n\to\infty)$から，$7\le n$なる$n\in\mathbb{N}$に対し，$0<a(n)<1$となり，$a(n)\notin\mathbb{Z}$．以上から，

$$
\begin{align*}
n=1,2,3,4,6
\end{align*}
$$

**(3)** (2)から，$S_n=\displaystyle\prod_{k=1}^na(k)$とおくと，$n\ge7$の時，$S_n$は単調減少である．(2)から，$n=1,2,\cdots,7$の時，$S_n\in\mathbb{Z}$である．

$$
\begin{align*}
S_7=a(1)\cdots a(7)=2^2\cdot3^3\cdot5^2\cdot7^2\cdot11=1455300\in\mathbb{Z}
\end{align*}
$$

$n\ge8$の時

$$
\begin{align*}
S(8)=S_7\cdot a(8)=\frac{3^2\cdot5^2\cdot7\cdot11^2}{2^2}\notin\mathbb{Z}
\end{align*}
$$

$$
\begin{align*}
S(9)=S(8)\cdot a(9)=\frac{5\cdot11^3\cdot13}{2^7\cdot3}\notin\mathbb{Z}
\end{align*}
$$

$$
\begin{align*}
S(10)=S(9)\cdot a(10)=\frac{11^3\cdot13^2}{2^{12}\cdot3^4\cdot5}\notin\mathbb{Z}<1
\end{align*}
$$

より，$10\le n$の時，$0<S(n)<1$で$S(n)\notin\mathbb{Z}$．以上から，

$$
\begin{align*}
n=1,2,3,4,5,6,7
\end{align*}
$$