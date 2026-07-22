---
university: "utokyo"
category: "zenki"
year: "1962"
question: "4"
type: "solution"
title: "UTOKYO 1962 zenki Q4 (solution)"
---

\input{macros}
     \begin{oframed}
     無限級数$\dfrac{r}{1-r^2}+\dfrac{r^2}{1-r^4}+\dfrac{r^4}{1-r^8}
     +\dots+\dfrac{r^{2^{n-1}}}{1-r^{2^n}}+\dots$の和を求めよ．ただし
     $|r|\not=0$とする．
     \end{oframed}

## 【解】

題意の無限級数$S$の第$n$部分和を$S_n$とおく．
     

$$
\begin{align*}
\dfrac{r^{2^{n-1}}}{1-r^{2^n}}=\frac{1}{1-r^{2^{n-1}}}-
     \frac{1}{1-r^{2^n}}
\end{align*}
$$

だから
     

$$
\begin{align*}
S_n&=\sum_{k=1}^n\frac{1}{1-r^{2^{k-1}}}-\frac{1}{1-r^{2^k}}\\&=\frac{1}{1-r}-\frac{1}{1-r^{2^n}}
\end{align*}
$$

である．故に$|r|$で場合分けして
     

$$
\begin{align*}
S=\left\{\begin{array}{ll}
          \dfrac{1}{1-r} & (|r|>1) \\
          \dfrac{r}{1-r}  & (|r|<1)
          \end{array}\right.\tag{答}
\end{align*}
$$

   
となる．