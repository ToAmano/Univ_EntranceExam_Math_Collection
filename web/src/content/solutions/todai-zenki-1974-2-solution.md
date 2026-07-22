---
university: "todai"
category: "zenki"
year: "1974"
question: "2"
type: "solution"
title: "TODAI 1974 zenki Q2 (solution)"
---

\input{macros}
     \begin{oframed}
     長さ$l$の線分が，その両端を放物線$y=x^2$の上にのせて動く．この線分の中点$M$が$x$軸に
     もっとも近い場合の$M$の座標を求めよ．ただし$l\ge1$とする．
     \end{oframed}

## 【解】

線分の両端を$A(a,a^2)$，$B(b,b^2)$とする．ただし
     

$$
\begin{align}
a<b\label{1}
\end{align}
$$

     とする．$l$の長さが$l$であるから
     

$$
\begin{align}
|AB|=l \Longleftrightarrow |AB|^2=l^2  \nonumber\\(b-a)^2+(b^2-a^2)^2=l^2  \nonumber\\(b-a)^2\left(1+(a+b)^2\right)=l^2 \label{2}
\end{align}
$$

となる．ここで$t=a+b$，$s=b-a$とおいて，$a$，$b$の存在条件を調べる．     
まずは[1](#1)，[2](#2)に代入して
     

$$
\begin{cases}
s>0 \\
     s^2(1+t^2)=l^2 
\end{cases}
$$

次に，$ab=\dfrac{t^2-s^2}{4}$であるから，$a$，$b$は$x$の$2$次方程式$x^2-tx+\dfrac{t^2-s^2}{4}=0$の異$2$実解であるから，判別式$D$として
     

$$
\begin{align*}
&D>0\\\Longleftrightarrow&t^2-4\frac{t^2-s^2}{4}>0\\\Longleftrightarrow&s^2>0
\end{align*}
$$

これは[3](#3)から常に成立する．よって$s$，$t$の条件式は[3](#3)，[4](#4)である．
このもとで$M(X,Y)$として$Y$が最小となる場合を考えれば良い($\because Y\ge0$)．
     

$$
\begin{align*}
\left\{\begin{array}{l}
          X=\dfrac{a+b}{2}=\dfrac{t}{2}  \\
          Y=\dfrac{a^2+b^2}{2}=\dfrac{t^2+s^2}{4}
          \end{array}\right.
\end{align*}
$$

であるから，[4](#4)を用いて$t$を消去して
     

$$
\begin{align*}
Y&=\frac{t^2+s^2}{4}\\&=\frac{1}{4}\left(s^2+\frac{l^2}{s^2}-1\right)\\&\ge\frac{1}{4}\left(2\sqrt{l^2}-1\right)\tag{s,l>0故AM-GM}\\&=\frac{1}{4}\left(2l-1\right)\tag{l>0}
\end{align*}
$$

である．等号成立は
     \[s^2=\frac{l^2}{s^2}\Longleftrightarrow s=\sqrt{l},t=\pm\sqrt{l-1}\]
のときで，$l\ge1$からこのような$(s,t)$は必ず存在する．又この時$X=\dfrac{\pm\sqrt{l-1}}{2}$である．
よって求める座標は$\left(\dfrac{\pm\sqrt{l-1}}{2},\dfrac{1}{4}\left(2l-1\right)\right)\cdots$(答) である．