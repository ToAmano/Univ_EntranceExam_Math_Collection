---
university: "utokyo"
category: "zenki"
year: "1995"
question: "5"
type: "solution"
title: "UTOKYO 1995 zenki Q5 (solution)"
---

\input{macros}
\begin{oframed}
サイコロを$n$回投げて，$xy$平面上の点$P_0$，$P_1$，$\dots$，$P_n$を次の規則(a)，(b)によって定める．
     

1.  $P_0=(0,0)$

2.  $1\le k\le n$のとき，$k$回目に出た目の数が$1,2,3,4$のときには，$P_{k-1}$をそれぞれ
     東，北，西，南に$\left(\dfrac{1}{2}\right)^k$だけ動かした点を$P_k$とする．また$k$回目に出た
     目の数が$5,6$のときには$P_k=P_{k-1}$とする．ただし$y$軸の正の向きを北と定める．

このとき以下の問いに答えよ．
     

1.  $P_n$が$x$軸上にあれば$P_0$，$P_1$，$\dots$，$P_{n-1}$もすべて$x$軸上にあること
     を示せ．

2.  $P_n$が第一象限$\{(x,y)|x>0,y>0\}$にある確率を$n$で示せ．

\end{oframed}

## 【解】

     

1.  $l$回目$(a\le l\le n-1,l\in\mathbb{N})$にはじめて南北方向に動いたとすると，移動量は
     $\left(\frac{1}{2}\right)^l$である．ここで$l+1$回目から$n$回目まで全て$l$回目と逆向きに動い
     たとしても，その合計の移動量は
          \begin{align*}
          \left(\frac{1}{2}\right)^{l+1}+ \dots+\left(\frac{1}{2}\right)^n \\
          =\left(\frac{1}{2}\right)^l-\left(\frac{1}{2}\right)^n<\left(\frac{1}{2}\right)^l
          \end{align*}
     だから，$P_n$は$x$軸上には存在しない．以上から題意の対偶が示された．$\Box$

2.  $P_n$が$x$軸上にあるという事象を$X$，$y$軸上にあるという事象を$Y$とする．
     求める確率$a_n$とすると，対称性から他の象限にある確率も$a_n$であるから，
          \begin{align}
          4a_n+P(X\cup Y)=1 \label{1}
          \end{align}
     が成立する．前問の結果から$P_n$が軸上に有るとき，
     $P_k(1\le k\le n)$も軸上にある$x$軸上にあるのは常にサイコロが$2,4,5,6$のとき，
     $y$軸上にあるのは常にサイコロが$1,3,5,6$のときである．したがって
          \begin{align}
           P(X)=P(Y)=\left(\frac{2}{3}\right)^n  \label{2}    
          \end{align}
     また，原点にあるのは，(1)と同様に考えれば常にサイコロが$5,6$であるときだから，
          \begin{align}
          P(X\cap Y)=\left(\frac{1}{3}\right)^n \label{3}
          \end{align}
     である．
          \[P(X\cup Y)=P(X)+P(Y)-P(X\cap Y) \]
     に注意して     
     [2](#2)，[3](#3)を[1](#1)に代入すれば
          \begin{align*}
          a_n=\frac{1}{4}\left(1-2\left(\frac{2}{3}\right)^n+\left(\frac{1}{3}\right)^n\right)\cdots\text{(答)}
          \end{align*}
     となる．