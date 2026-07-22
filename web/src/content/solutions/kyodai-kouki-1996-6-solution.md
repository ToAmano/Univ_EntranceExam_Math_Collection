---
university: "kyodai"
category: "kouki"
year: "1996"
question: "6"
type: "solution"
title: "KYODAI 1996 kouki Q6 (solution)"
---

## 【解】

  (1) $p_{n+2}$ について$1$回目に出たコインで場合分けすると
  \begin{itemize}
    \item $1$回目に表で，出発点をとびこすとき，$p_{n+1}$  \\
    \item $1$回目に裏で，出発点をとびこすとき，$p_n$
  \end{itemize}
  だから，
  

$$
\begin{align}
p_{n+2} = \frac{p_{n+1} + p_n}{2}\label{1996-6:eq:1}
\end{align}
$$

  である．初期条件は
  

$$
\begin{align*}
p_3 & =\frac{3}{8}\\
    p_4 & =\frac{5}{16}
\end{align*}
$$

  である．以下[(式1)](#1996-6:eq:1)を解く．変形して
  

$$
\begin{align*}
p_{n+2}+\frac{1}{2}p_{n+1}& = p_{n+1}+\frac{1}{2}p_{n}
\end{align*}
$$

  だから初期条件の元で解いて，$n\ge 3$に対して
  

$$
\begin{align*}
p_{n+1} = -\frac{1}{2}p_{n}+\frac{1}{2}
\end{align*}
$$

  となる．さらに変形すると
  

$$
\begin{align*}
p_{n+1}-\frac{1}{3} = -frac{1}{2}\left(p_{n}-\frac{1}{3}\right)
\end{align*}
$$

  だから，$n\ge 3$に対して
  

$$
\begin{align*}
p_n
     & = \frac{1}{3} + \frac{1}{6}\left(\frac{-1}{2}\right)^{n-1}\\& = \frac{1}{3}\left(1-\left(\frac{-1}{2}\right)^{n}\right)
\end{align*}
$$

  が求める答えである．$\cdots$(答)

  
  (2)
  $k-1$周目までとびこす時，まず$1$回目をとびこす確率は$P_n$である．
  $2$周目以降でとびこす確率は，とびこした後の点が$1$周目の出発点より$1$つだけ進んだ点であることから$p_{n-1}$である．
  又，$k$回目に出発点を踏む確率は排反を考えて$(1-p_{n-1})$である．
  以上から，$\alpha=-1/2$とおいて
  

$$
\begin{align*}
q_{n,k}& =  p_n \cdot(p_n)^{k-2}\cdot(1-p_n)                                                                                    \\& =  \frac{1}{3}(1-\alpha^n) \left\{\frac{1}{3}(1-\alpha^{n-1}) \right\}^{k-2}\cdot\left(\frac{2}{3}+\alpha^{n-1}\right)\\& =  \left(\frac{1}{3}\right)^{k-1}(1-\alpha^n)(1-\alpha^{n-1})^{k-2}\left(\frac{2}{3}+\alpha^{n-1}\right)\\\rightarrow& 2\left(\frac{1}{3}\right)^k \quad(n \rightarrow\infty)
\end{align*}
$$

  が求める極限である．$\cdots$(答)

  
  

## 【解説】