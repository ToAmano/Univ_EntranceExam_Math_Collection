---
university: "utokyo"
category: "kouki"
year: "1996"
question: "2"
type: "solution"
title: "UTOKYO 1996 kouki Q2 (solution)"
---

## 【解】

  まず四面体を$xyz$座標空間に配置することを考える．
  中点連結定理から，
  

$$
\begin{align*}
\begin{dcases}
      MN = a \\
      ML = c \\
      NL = b
    \end{dcases}
\end{align*}
$$

  であり，3辺の長さが等しいことから
  

$$
\begin{align*}
\triangle AMN \equiv\triangle MCL \equiv\triangle NLB \equiv\triangle LNM
\end{align*}
$$

  である．

  また，三角形ABCが鋭角三角形であることから
  

$$
\begin{align}
\begin{dcases}
      a^2 + b^2 > c^2 \\
      a^2 + c^2 > b^2 \\
      b^2 + c^2 > a^2
    \end{dcases}\label{1996-2:eq:1}
\end{align}
$$

  が成り立つ．

  

<figure id="1996-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1996/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 空間座標に四面体を配置した様子</figcaption>
</figure>

  ここで，座標空間において，
  8点 $O(0,0,0)$，$A'(X,0,0)$， $B'(0,Y,0)$， $C'(X,Y,0)$， $D'(0,0,Z)$，
  $E'(X,0,Z)$， $F'(X,Y,Z)$， $G'(0,Y,Z)$ を考える．
  ただし$X,Y,Z>0$とする．これら8点は辺の長さが$X，Y，Z$の直方体を形成する．
  面の対角線の長さについて
  

$$
\begin{align*}
\begin{dcases}
      AF' = B'D' = \sqrt{Y^2+Z^2} \\
      BF' = A'D' = \sqrt{X^2+Z^2} \\
      A'B' = D'F' = \sqrt{X^2+Y^2}
    \end{dcases}
\end{align*}
$$

  だから，四面体 $AF'DB'$ の4面は全て合同な三角形である．

  従って
  

$$
\begin{align}
& \begin{dcases}
         a = \sqrt{Y^2+Z^2} \\
         b = \sqrt{X^2+Z^2} \\
         c = \sqrt{X^2+Y^2}
       \end{dcases}\\\therefore& \begin{dcases}
         x = \sqrt{\frac{-a^2+b^2+c^2}{2}} \\
         y = \sqrt{\frac{a^2-b^2+c^2}{2}}  \\
         z = \sqrt{\frac{a^2+b^2-c^2}{2}}
       \end{dcases}\label{1996-2:eq:2}
\end{align}
$$

  となるよう$X,Y,Z$ を設定し，
  $F'$を$A(=B=C)$，
  $D'$を$N$，
  $A'$を$L$，
  $B'$を$M$
  でおきかえて考えれば良い．
  [(式1)](#1996-2:eq:1)から必ずこのような$x,y,z$が存在する．

  この時，$Q (X, \frac{Y}{2}, \frac{Z}{2})$
  $P (0, \frac{Y}{2}, \frac{Z}{2}) \cdots ②$

  (1)
  この座標系で考えると，$M(0,Y,0)$，$N(0,0,Z)$の中点Pは
  

$$
\begin{align*}
P\left(0,\frac{Y}{2},\frac{Z}{2}\right)
\end{align*}
$$

  であり，
  $B(X,Y,Z)$，$L(X,0,0)$の中点Qは
  

$$
\begin{align*}
Q\left(X,\frac{Y}{2},\frac{Z}{2}\right)
\end{align*}
$$

  だから，線分PQの長さは[(式2)](#1996-2:eq:2)から
  

$$
\begin{align*}
\overline{PQ} = X = \sqrt{\frac{-a^2+b^2+c^2}{2}}
\end{align*}
$$

  である．  $\cdots$(答)
  

  (2)
  四面体の体積Vは 立方体O'A'C'B'D'E'F'G'の体積からまわりの4つの三角錐の体積を引いたものである．
  よって
  

$$
\begin{align*}
V
     & = XYZ - 4 \cdot\frac{1}{6}XYZ \\& = \frac{1}{3}XYZ
\end{align*}
$$

  である．[(式2)](#1996-2:eq:2)を代入して
  

$$
\begin{align*}
V
     & = \frac{\sqrt{2}}{12}\sqrt{(-a^2+b^2+c^2)(a^2-b^2+c^2)(a^2+b^2-c^2)}
\end{align*}
$$

  である．$\cdots$(答)
  
  

## 【解説】