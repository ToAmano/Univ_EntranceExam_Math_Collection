---
university: "kyodai"
category: "kouki"
year: "1998"
question: "5"
type: "solution"
title: "KYODAI 1998 kouki Q5 (solution)"
---

## 【解】

  まず，明らかに
  

$$
\begin{align*}
Q_1 = 1
\end{align*}
$$

  である．$A_i,B_i$を図示すると[図1](#1998-5:fig:1)のようになる．

  

<figure id="1998-5:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1998/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $A_i,B_i$の様子</figcaption>
</figure>

  (1)
  **$n=2$ の時**

  

<figure id="1998-5:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1998/5/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $n=2$の時の様子</figcaption>
</figure>

  $A_1 \to A_2 \to B_2$, 又は $A_1 \to B_1 \to B_2$ と行けば良い．
  排反事象を考えると，これは$A_1A_2$にも$B_1B_2$にも×がついている時以外である．
  従って，求める確率は
  

$$
\begin{align*}
Q_2 & = 1 - (1-p)^2 \\& = p(2-p)
\end{align*}
$$

  である．$\cdots$(答)
  

  **$n=3$ の時**

  

<figure id="1998-5:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1998/5/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $n=3$の時の様子</figcaption>
</figure>

  $A_1$ から右方向へ出発し，どこではじめて上方へ移動しなければならないか
  ($A_k A_{k+1}$ が $\times$ となっている最小の$k \in \mathbb{N}$) で場合分けする．
  

1.  $A_1 A_2$ が $\times$ の時，$A_1 \to B_1$ へ行くルートで確率は $p^2 (1-p)$ \\

2.  $A_2 A_3$ が $\times$ の時，$B_2 B_3$ が矢印になっていれば良く，確率は $p^2 (1-p)$ \\

3.  $A_1 A_2, A_2 A_3$ とも通過できる時，必ずルートがあって確率は $p^2$

  以上三つの場合は互いに排反だから，求める確率は
  

$$
\begin{align*}
Q_3
     & = 2p^2 (1-p) + p^2 \\& = p^2 (3-2p)
\end{align*}
$$

  である．$\cdots$(答)
  

  (2) (1)の $n=3$ の時と同様の場合分けをする．
  つまり，$A_1$ から右へ進んでいって，はじめて行き止まり ($\times$) になっている所が
  $A_k A_{k+1}$ の時を考える($k=1, 2, \dots, n-1$)．
  (以下 $n \ge 4$ とする．

  この時．$B_n$ まで行ける確率は $C_n(k)$ とおく．
  この確率は$A_1 \to \dots \to A_k$まで行き，そのあと$B_k \to \dots \to B_n$
  が行き止まりになっておらず矢印になっており，$A_k A_{k+1}$ が $X$ になっている時で，
  

$$
\begin{align*}
a_n(k) = p^{n-1}\cdot(1-p)
\end{align*}
$$

  である．

  また，Aの横道に一つも行き止まりがない時を便宜上$k=n$とおくと
  

$$
\begin{align*}
a_n(n) = p^{n-1}
\end{align*}
$$

  である．

  従って，各$a_{n}(k)$は排反事象であることより，求める確率は
  

$$
\begin{align*}
Q_n
     & = \sum_{k=1}^{n} a_n(k)            \\& = \sum_{k=1}^{n-1} a_n(k) + a_n(n) \\& = (n-1) ^{n-1}(1-p) + p^{n-1}\\& = p^{n-1}\{ n - (n-1)p \}
\end{align*}
$$

  である．(1)より，これは$n=2,3$ でも成立するから，求める確率は
  

$$
\begin{align*}
Q_n = p^{n-1}\{ n - (n-1)p \}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】