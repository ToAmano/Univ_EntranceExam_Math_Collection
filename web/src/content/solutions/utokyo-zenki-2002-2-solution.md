---
university: "utokyo"
category: "zenki"
year: "2002"
question: "2"
type: "solution"
title: "UTOKYO 2002 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 $x^{n+1} = (x^2-x-1) P_n(x) + a_n x + b_n \quad \cdots \textcircled{1}$ とおく。

\bigskip

(1) \textcircled{1} の両辺に $x$ をかけて

$$
\begin{align*}
x^{n+2}&= x(x^2-x-1) P_n(x) + a_n x^2 + b_n x \\&= (x^2-x-1) [x P_n(x) + a_n] + (a_n + b_n) x + a_n
\end{align*}
$$

一方、この右辺は $(x^2-x-1) P_{n+1}(x) + a_{n+1} x + b_{n+1}$ だから 係数比較して

$$
\begin{align*}
\begin{cases}
a_{n+1} = a_n + b_n \\
b_{n+1} = a_n
\end{cases} \quad \text{\#}
\end{align*}
$$

\bigskip

(2) $x^2 = (x^2-x-1) + x + 1$ から、$a_1 = b_1 = 1$ であり、(1)から

$$
\begin{align*}
\begin{cases}
a_{n+2} = a_{n+1} + a_n \\
b_{n+1} = a_n
\end{cases}
\end{align*}
$$

であるから、帰納的に $a_n, b_n \in \mathbb{Z}_{>0}$ である。

\begin{quote}
\small
［帰納法を使ってもいいけど、自明と言ってもいい気がする。一応「書き漏らしていること」を言う方が良いかも\dots{}］
\end{quote}

次に、「$a_n$ と $b_n$ が互いに素」 $\iff$ 「$a_{n+1}$ と $a_n$ が互いに素」であるから ($\because a_1 = b_1 = 1$) 以下これを帰納的に示す。

1.  $n=1$ の時\\
  $a_1=1, a_2=2$ から成立

2.  $n=k$ での成立仮定\\
  $a_{k+2} = a_{k+1} + a_k$ と $a_{k+1}$ が互いに素であることを示す。
  

$$
\begin{align*}
(a_{k+1} + a_k, a_{k+1}) = (a_{k+1}, a_k) = 1 \quad (\because \text{仮定})
\end{align*}
$$

  から示された。よって $n=k+1$ で成立

以上から示された。 \hfill \text{固}