---
university: "ukyoto"
category: "kouki"
year: "2006"
question: "3"
type: "solution"
title: "UKYOTO 2006 kouki Q3 (solution)"
---

## 【解】

  $n \le 3$の時と$n \ge 4$の時で場合分けする．

  まず，$n \ge 4$の時を考える．
  サイコロの目は$1$以上だから, 和が$n+3$になるのは以下のいずれかである．
  \begin{itemize}
    \item[A] 1つが$4$, 他が$1$のとき
    \item[B] 2つが$(3,2)$, 他が$1$のとき
    \item[C] 3つが$(2,2,2)$, 他が$1$のとき
  \end{itemize}
  これら三つの事象は排反であり，それぞれの事象の確率$P(X=A,B,C)$は以下のように与えられる．
  

$$
\begin{align*}
P(A) & = n\left(\frac{1}{6}\right)^n                     \\
    P(B) & = n(n-1)\left(\frac{1}{6}\right)^n                \\
    P(C) & = \frac{n(n-1)(n-2)}{6}\left(\frac{1}{6}\right)^n
\end{align*}
$$

  従って，求める確率$P(n)$は
  

$$
\begin{align}
P(n)
     & = P(A)+P(B)+P(C)                                                             \\& = \left[n + n(n-1) + \frac{n(n-1)(n-2)}{6}\right]\left(\frac{1}{6}\right)^n \\& = \left(n^ + 3n^ + 2\right) n \left(\frac{1}{6}\right)^{n+1}\\& = n(n+1)(n+2) \left(\frac{1}{6}\right)^{n+1}\label{2006-3:eq:1}
\end{align}
$$

  である．

  
  次に$n \le 3$のとき，$n=1$では一つの目が$4$になる場合のみ，
  $n=2$では二つの組み合わせが$(1,4),(2,3)$となる場合のみ，
  $n=3$では三つの組み合わせが$(1,1,4),(1,2,3),(2,2,2)$となる場合のみで，
  これらの確率は
  

$$
\begin{align*}
P(1) & = \frac{1}{6}\\
    P(2) & = \frac{4}{36} = \frac{1}{9}\\
    P(3) & = \frac{3+6+1}{216} = \frac{5}{108}
\end{align*}
$$

  であり，[(式1)](#2006-3:eq:1)で表現できている．

  以上から求める確率は
  

$$
\begin{align*}
P(n) = n(n+1)(n+2) \left(\frac{1}{6}\right)^{n+1}
\end{align*}
$$

  である． $\cdots$(答)

  
  

## 【解説】