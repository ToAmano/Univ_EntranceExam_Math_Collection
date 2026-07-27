---
university: "titech"
category: "zenki"
year: "1981"
question: "1"
type: "solution"
title: "TITECH 1981 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$2^{n-1}\alpha=a_n+b_n$ の両辺に2をかけて，

$$
\begin{align*}
2^n\alpha=2a_n+2b_n=a_{n+1}+b_{n+1}\quad\cdots\text{①}
\end{align*}
$$

である．$n$の偶奇で場合分けして，$k\in\mathbb{N}$に対し，

**$1^\circ$ $n=2k$の時，$1<2b_n<2$だから，**

$$
\begin{align*}
\begin{cases}
a_{2k+1}=2a_{2k}+1 \\
b_{2k+1}=2b_{2k}-1
\end{cases}\quad\cdots\text{②}
\end{align*}
$$

**$2^\circ$ $n=2k-1$の時，$0\le2b_n<1$だから，**

$$
\begin{align*}
\begin{cases}
a_{2k}=2a_{2k-1} \\
b_{2k}=2b_{2k-1}
\end{cases}\quad\cdots\text{③}
\end{align*}
$$

となる．②，③から

$$
\begin{align*}
b_{2k+1}=4b_{2k-1}-1 \quad\therefore\ b_{2k+1}-\frac13=4\left(b_{2k-1}-\frac13\right)
\end{align*}
$$

$b_1=\alpha$ だから，くり返し用いて，

$$
\begin{align*}
\begin{cases}
b_{2k-1}=4^{k-1}\left(\alpha-\dfrac13\right)+\dfrac13 \\
b_{2k}=2\cdot4^{k-1}\left(\alpha-\dfrac13\right)+\dfrac23
\end{cases}
\end{align*}
$$

$0\le b_k<1$ が任意の$k$で成立するので，$\alpha=\dfrac13$ が必要で，逆にこの時，

$$
\begin{align*}
b_{2k-1}=\frac13,\quad b_{2k}=\frac23
\end{align*}
$$

で条件を満たす．よって $\alpha=\dfrac13$ である．この時，$b_n$と同様に$a_n$をもとめて（$a_1=0$より），

$$
\begin{align*}
a_{2k-1}=4^{k-1}\left(0+\frac13\right)-\frac13=\frac13\left(4^{k-1}-1\right)
\end{align*}
$$

$$
\begin{align*}
a_{2k}=\frac23\left(4^{k-1}-1\right)
\end{align*}
$$