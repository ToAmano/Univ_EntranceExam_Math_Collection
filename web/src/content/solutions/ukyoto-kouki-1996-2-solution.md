---
university: "ukyoto"
category: "kouki"
year: "1996"
question: "2"
type: "solution"
title: "UKYOTO 1996 kouki Q2 (solution)"
---

## 【解】

  表示の簡潔さのため
  

$$
\begin{align*}
A & =m^n+1 \\
    B & =n^m+1
\end{align*}
$$

  とおく．ただし
  

$$
\begin{align*}
& m,n \in\mathbb{N}\\& m<n
\end{align*}
$$

  とする．

  $n,m$が偶数とすると，$\mod 2$で考えると
  

$$
\begin{align*}
A & \equiv 1 \\
    B & \equiv 1
\end{align*}
$$

  となり，$A$も$B$も$10$の倍数にならず不適である．
  そこで$n,m$は共に奇数であり，この時$A,B$は
  

$$
\begin{align*}
A & = m^n+1 = (m+1)(m^{n-1}-m^{n-2}+\dots+1) \\
    B & = n^m+1 = (n+1)(n^{m-1}-n^{m-2}+\dots+1)
\end{align*}
$$

  のように分解できる．
  これらが共に$10$の倍数であるものの一つに，
  $m+1, n+1$が共に$10$の倍数であるような組がある．
  $m<n$から．$m=9, n=19$とすれば良い．  $\cdots$(答)

  
  

## 【解説】

  最初から$\mod 10$で考えても良い．$A,B$が$10$の倍数である時，
  

$$
\begin{align*}
m^n \equiv -1 \\
    n^m \equiv -1
\end{align*}
$$

  となる．一例として$(m,n)=(9,19)$とすると
  

$$
\begin{align*}
(-1)^19 \equiv -1 \\(-1)^9 \equiv -1
\end{align*}
$$

  となり条件を満たす．