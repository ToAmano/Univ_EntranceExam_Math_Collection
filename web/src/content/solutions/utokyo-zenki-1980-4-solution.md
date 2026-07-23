---
university: "utokyo"
category: "zenki"
year: "1980"
question: "4"
type: "solution"
title: "UTOKYO 1980 zenki Q4 (solution)"
---

\input{macros}
     \begin{oframed}
     $xy$平面上の動点$P$の座標$(x,y)$は，時刻$t$を用いて
     

$$
\begin{align*}
\left\{
          \begin{array}{l}
          x=\sin t+\cos t  \\
          y=k\sin^2 t\cos^2 t
          \end{array}
     \right.(-\infty<t<\infty)
\end{align*}
$$

     と表されるものとする．ただし$k$は正の定数である．このとき原点と$P$との距離の二乗
     の最大値及び最小値を，$k$を用いて表せ．
     \end{oframed}

## 【解】

\2 ただし，周期性から$0\le t<2\pi$としてよい．$f(t)=|OP|^2$とすると
     

$$
\begin{align*}
f(t)&=x^2+y^2 \\&=(s+c)^2+(ks^2c^2)^2 \\&=k^2p^4+2p+1\equiv g(p)
\end{align*}
$$

である．ただし$p=sc$とした．このとき$\left(\dfrac{-1}{2}\le p\le\dfrac{1}{2}\right)$である．
ここで$a=\sqrt[3]{\dfrac{1}{2k^2}}$とおけば
     

$$
\begin{align*}
g'(p)&=4k^2p^3+2  \\&=4k^2(p+a)(p^2-ap+a^2)
\end{align*}
$$

から下表を得る．$(\because k>0)$ \\
     \begin{indentation}{2zw}{0pt}
     \underline{(i)$\dfrac{1}{2}\ge a$つまり$2\le k$の時} \\
          

$$
\begin{align*}
\begin{array}{|c|c|c|c|c|c|} \hline
          p & -1/2                  &     &-a                     &      &1/2                        \\ \hline
          g'&                         &  -  & 0                      &  +  &                             \\ \hline
          g &  \dfrac{k^2}{16}&\se&-\dfrac{3a}{2}+1&\ne &\dfrac{k^2}{16}+2  \\ \hline
          \end{array}
\end{align*}
$$

    
    従って
          

$$
\begin{align*}
\left\{
               \begin{array}{l}
               \max g=\dfrac{k^2}{16}+2  \\
               \min g=1-\dfrac{3}{2}\sqrt[3]{\dfrac{1}{2k^2}}
               \end{array}
          \right.
\end{align*}
$$

     
     である．
     \\ 
     \\
     \underline{(ii)$\dfrac{1}{2}\le a$つまり$2\ge k>0$の時} \\
     $g'(p)\ge0$より，$g(p)$は単調増加だから
          

$$
\begin{align*}
\begin{array}{ll}
               \max g=g\left(\dfrac{1}{2}\right) &  
               \min g=g\left(\dfrac{-1}{2}\right)
               \end{array}
\end{align*}
$$

     である．  \\   
     \end{indentation}
   
以上から求める最大小値は，
     

$$
\begin{align*}
\left\{
          \begin{array}{lll}
          0<k\le 2\text{の時}　& \max g=\dfrac{k^2}{16}+2 &  \min g=\dfrac{k^2}{16}  \\
          2\le k\text{の時} & \max g=\dfrac{k^2}{16}+2 & \min g=1-\dfrac{3}{2}\sqrt[3]
          {\dfrac{1}{2k^2}}
          \end{array}
     \right.
\end{align*}
$$

である．