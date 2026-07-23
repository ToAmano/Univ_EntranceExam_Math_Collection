---
university: "utokyo"
category: "zenki"
year: "1982"
question: "3"
type: "solution"
title: "UTOKYO 1982 zenki Q3 (solution)"
---

\input{macros}
     \begin{oframed}
     $xy$平面において，点$A$は原点$O$を中心とする半径$1$の円周の第一象限にある部分を動き，
     点$B$は$x$軸上を動く．ただし線分$AB$の長さは$1$であり，線分$AB$は両端$A$，$B$以外の
     点$C$で円周と交わるものとする．
          

1.  

2.  $\theta=\angle AOB$の取りうる値の範囲を求めよ．

3.  $BC$の長さを$\theta$で表せ．

4.  線分$OB$の中点を$M$とするとき，線分$CM$の長さの範囲を求めよ．

     \end{oframed}

## 【解】

1.  

2.  \1 ただし，題意から$0<\theta<\pi/2$である．また$A(c,s)$である．
この時$\triangle ABO$は$OA=AB=1$の二等辺三角形だから$B(2c,0)$となる．故に線分$AB$の方程式は，$c\not=0$に注意して，
      

$$
\begin{align}
&(2c-c)(y-s)-(0-s)(x-s)=0     \nonumber\\&sx+cy-2sc=0                     \nonumber\\&y=\frac{s}{c}(-x+2c) \,\,\,\,\ (c\le x\le2c) \label{3}
\end{align}
$$

である．これが円周と交わるので，$y$を消した
     

$$
\begin{align}
&x^2+\left(\frac{s}{c}\right)^2(-x+2c)^2=1  \nonumber\\&c^2x^2+s^2(-x+2c)^2=c^2 \nonumber\\&x^2-4s^2cx+c^2(4s^2-1)=0  \nonumber\\&(x-c)\left(x-c(4s^2-1)\right)=0  \label{1}
\end{align}
$$

が$c\le x\le2c$に解を持つ．従って$0<\theta<\pi/2$に注意して
     

$$
\begin{align}
c<c(4s^2-1)<2c \nonumber\\
     1<4s^2-1<2 \nonumber\\\frac{1}{2}<s^2<\frac{3}{4}\label{4}\\\frac{\pi}{4}<\theta<\frac{\pi}{3}\label{2}
\end{align}
$$

である．$\cdots$(答)

3.  [1](#1)から$C$の$x$座標は$c(4s^2-1)$である．さらに$AB$の傾きは[3](#3)から
     $\dfrac{-s}{c}$であるから，
          

$$
\begin{align*}
|BC|=\sqrt{1+\left(\frac{s}{c}\right)^2}(2c-c(4s^2-1))=3-4s^2
\end{align*}
$$

     である．$\cdots$(答)

4.  $M(c,0)$である．故に$|MB|=c$．これと前問の結果，及び二等辺三角形の性質より
     $\angle ABO=\angle AOB=\theta$であることから，
     $\triangle BCM$に余弦定理を用いて
          

$$
\begin{align*}
&|MC|^2 \\
          =&|MB|^2+|BC|^2-2|MB||BC|\cos\angle MBC  \\
          =&c^2+(3-4s^2)^2-2c(3-4s^2)\cos\angle ABO \\
          =&c^2+(3-4s^2)^2-2c(3-4s^2)c　\\
          =&c^2(-5+8s^2)+(3-4s^2)^2 \\
          =&(1-p)(8p-5)+(4p-3)^2   \tag{p=s^2}\\ 
          =&8p^2+11p+4  \\
          =&8\left(p-\frac{11}{16}\right)^2+\frac{7}{32}
\end{align*}
$$

     
     である．[4](#4)から$\dfrac{1}{2}<p<\dfrac{3}{4}$であることを考慮すると，
          

$$
\begin{align*}
\left\{\begin{array}{l}
               p=11/16\text{で}\min7/32 \\
               p\to 1/2\text{で}\max 1/2
               \end{array}\right.
\end{align*}
$$

     である．$|MC|>0$から，
          

$$
\begin{align*}
&\sqrt{\frac{7}{32}}\le|MC|<\sqrt{\frac{1}{2}}\\\therefore\ &\frac{\sqrt{14}}{8}\le|MC|<\frac{\sqrt{2}}{2}
\end{align*}
$$

     である．$\cdots$(答)

{\bf[別解]}(1)について，$A(c,s)$での円の接線
     

$$
\begin{align*}
cx+sy=1
\end{align*}
$$

の$x$切片は$1/c$であるから，
円周と$AB$が交わるための条件は
      

$$
\begin{align*}
1<2c<\frac{1}{c}\Longleftrightarrow \frac{1}{2}<c<\frac{\sqrt{2}}{2}
\end{align*}
$$

であり，これを解いて
      

$$
\begin{align*}
\frac{\pi}{4}<\theta<\frac{\pi}{3}
\end{align*}
$$

となる．$\cdots$(答)