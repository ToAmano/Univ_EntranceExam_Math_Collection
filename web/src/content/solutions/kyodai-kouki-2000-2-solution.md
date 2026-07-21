---
university: "kyodai"
category: "kouki"
year: "2000"
question: "2"
type: "solution"
title: "KYODAI 2000 kouki Q2 (solution)"
---

## 【解】

### (1)

  簡潔さのため，
  
$$
\begin{align*}
f(x) = e^x - \frac{1}{2}x^2-1
\end{align*}
$$

  とおく．一回微分は
  
$$
\begin{align*}
f'(x) = e^x - x > e^x - (x+1) \geq 0
\end{align*}
$$

  だから，$f'(x)>0$より$f(x)$ は単調増加である．
  したがって，$0 \leq x$ の時，
  
$$
\begin{align*}
f(x) \geq f(0) = 0
\end{align*}
$$

  となり，題意の条件は示された．  $\cdots$(答)

### (2)

  $f_n(x)$の一階微分は
  
$$
\begin{align*}
f'_n(x) =
     & n^2e^{-nx}\left[1-n(x-1)\right]\\& = n^2e^{-nx}(-nx+n+1)
\end{align*}
$$

  であるから，$f_n(x)$の増減表は$\eqref{2000-2:table:1}$となる．
  \begin{table}[H]
    \centering
    \caption{$f_n(x)$の増減表}
    \label{2000-2:table:1}
    

| $x$ | $0$ | $\cdots$ | $\frac{n+1}{n}$ | $\cdots$ | $\infty$ |
|:------:|:------:|:----------:|:---------------:|:----------:|:--------:|
| $f'_n$ | | $+$ | | $-$ | |
| $f_n$ | $-n^2$ | $\nearrow$ | | $\searrow$ | $0$ |

  \end{table}
  従って，$f_n(x)$は$x=(n+1)/n$で最大値を取るから，
  
$$
\begin{align*}
M_n
     & = f_n\left(\frac{n+1}{n}\right)\\& = n^2 \frac{1}{n} e^{-(n+1)}\\& = n e^{-(n+1)}
\end{align*}
$$

  となる．従って，$M_k$の$k=1,2,\cdots,n$での和を
  
$$
\begin{align*}
S_n= \sum_{k=1}^{n}M_k
\end{align*}
$$

  とおく．
  $S_n$および$S_n/e$を書き下して
  
$$
\begin{align*}
& S = e^{-2} + 2 \cdot e^{-3} + \cdots + n e^{-(n+1)}\\& \frac{1}{e}S = e^{-3} + \cdots + (n-1) e^{-(n+1)} + n e^{-(n+2)}
\end{align*}
$$

  だから，これらを辺々引いて
  
$$
\begin{align*}
\left(1-\frac{1}{e}\right)S_n
     & = \sum_{k=2}^{n+1} e^{-(k+1)} - n e^{-(n+2)}\\& = e^{-2}\frac{1-(1/e)^n}{1-1/e} - n e^{-(n+2)}\\\therefore& S_n = \frac{e}{e-1}\left[ e^{-2}\frac{1-(1/e)^n}{1-1/e} - n e^{-(n+2)}\right]\\
\end{align*}
$$

  を得る．求める極限値は
  
$$
\begin{align*}
S
     & = \lim_{n\to\infty}S_n                                                                        \\& = \lim_{n\to\infty}\frac{e}{e-1}\left[ e^{-2}\frac{1-(1/e)^n}{1-1/e} - n e^{-(n+2)}\right]\\& =\frac{1}{(e-1)^2}
\end{align*}
$$

  である．  $\cdots$(答)

  
  

## 【解説】