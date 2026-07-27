---
university: "titech"
category: "zenki"
year: "1976"
question: "4"
type: "solution"
title: "TITECH 1976 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$A=\displaystyle\int_0^1 f(t)e^{-t}dt$ とおく．与式の両辺は $x$ で微分できる．

$$
\begin{align*}
f(x)=e^x-2aA\,e^{2x}\quad\cdots\text{①}
\end{align*}
$$

$A$ の式に代入して

$$
\begin{align*}
A=\int_0^1(e^t-2aA\cdot e^{2t})e^{-t}dt=\int_0^1(1-2aA\cdot e^t)dt=\left[t-2aA\cdot e^t\right]_0^1=1-2aA(e-1)
\end{align*}
$$

$$
\begin{align*}
\therefore\ A=\frac{1}{1+2a(e-1)}\quad(\because 1+2a(e-1)=0\text{ は }a=1\text{ で不適}) \quad\cdots\text{②}
\end{align*}
$$

次に，与式に $x=0$ を代入すると，

$$
\begin{align*}
0=1-Aa \quad\therefore\ Aa=1 \quad\cdots\text{③}
\end{align*}
$$

である．②，③から

$$
\begin{align*}
(A,a)=\left(3-2e,\ \frac{1}{3-2e}\right)
\end{align*}
$$

だから，

$$
\begin{align*}
f(x)=e^x-2e^{2x}, \quad a=\frac{1}{3-2e}
\end{align*}
$$