---
university: "todai"
category: "zenki"
year: "1962"
question: "5"
type: "solution"
title: "TODAI 1962 zenki Q5 (solution)"
---

\input{macros}
     \begin{oframed}
     $1$つの頂点から出る$3$辺の長さが$x$，$y$，$z$であるような直方体において，
     $x$，$y$，$z$の和が$6$，全表面積が$18$であるとき，
          

1.  $x$のとりうる値の範囲を求めよ．

2.  このような直方体の体積の最大値を求めよ．

     \end{oframed}

## 【解】

まず題意から
     
$$
\begin{cases}
x,y,z>0 \label{1} \\
     x+y+z=6  \label{2}\\
     yz+zx+xy=9  \label{3}
\end{cases}
$$

となる．     
     

1.  まず$s=y+z$，$t=yz$として，$y$，$z$の存在条件を考える．\eqref{2}，\eqref{3}
     から
          \begin{align}
          \left\{
               \begin{array}{l}
               s=6-x \\
               t=x^2-6x+9
               \end{array}
          \right.\label{4}
          \end{align}
     となる．
     
     さて，\eqref{1}，\eqref{4}から$y$，$z$は$p$の$2$次方程式
          \begin{align*}
          &p^2-sp+t=0\\ 
          \Longleftrightarrow &p^2-(6-x)p+(x^2-6x+9)=0 
          \end{align*}
     の正$2$実解であるから，判別式$D$として     
          \begin{align*}
          &\left\{
               \begin{array}{l}
               D\ge0  \\
               s,t>0
               \end{array}
          \right.  \\
          \Longleftrightarrow&\left\{
               \begin{array}{l}
               (6-x)^2-4(x^2-6x+9)\ge0  \\
               6-x>0  \\
               x^2-6x+9>0
               \end{array}
          \right.\\
          \Longleftrightarrow&\left\{
               \begin{array}{l}
               (6-x)^2-4(x^2-6x+9)\ge0  \\
               6-x>0  \\
               x^2-6x+9>0
               \end{array}
          \right.\\
          \Longleftrightarrow&\left\{
               \begin{array}{l}
               0\le x\le 4  \\
               x<6  \\
               x\not=3
               \end{array}
          \right. \\
          \Longleftrightarrow&
               0\le x<3,3<x\le 4  \tag{答}
          \end{align*} 
となる．

2.  $a=x+y+z$，$b=yz+zx+xy$，$c=xyz$とおく．すると$x$，$y$，$z$は$p$の$3$次方程式
          \begin{align}
          &p^3-ap^2+bp-c=0  \nonumber\\
          \Longleftrightarrow&p^3-6p^2+9p-c=0 \label{5}
          \end{align}
     の正実解である．故にこれが正の$3$実解(重解含む)をもつ条件を求める．
                    
          \eqref{5}が正の$3$実解を持つ．\\
          $\Longleftrightarrow$$y=f(p)=p^3-6p^2+9p$と$y=c$が$0<p$に$3$つの共有点(重解含む)を持
          つ．
          
     である．
          \begin{align*}
          f'(p)&=3p^2-12p+9  \\
          &=3(p-1)(p-3)
          \end{align*}
     であるから下表を得る．
          \begin{align*}
               \begin{array}{|c|c|c|c|c|c|}  \hline
               p &    &  1  &      &  3  &     \\ \hline
               f' &+  &  0  & -    &  0  & +  \\ \hline     
               f &\ne&  4  &\se &  0  &\ne  \\ \hline
               \end{array}
          \end{align*}
     従って，$y=f(p)$のグラフは下のようになり，故に$c$の値域は$0\le c\le4$である．
          
          \scalebox{1}{\input{ut-62-5p}}
          
     さて，直方体の体積は$c$に等しいから$\max c=4\cdots$(答)である．

     

{\bf[別解]} 

[解]と同様に，$x$，$y$，$z$は$p$の$3$次方程式$p^3-6p^2+9p-c=0$の正の$3$実解であるから，$y=f(p)$と$y=c$の共有点の
$p$座標である．ゆえにグラフから，$x$の値域は$0<x\le4$である．$\cdots$(答)