---
university: "utokyo"
category: "zenki"
year: "1987"
question: "3"
type: "solution"
title: "UTOKYO 1987 zenki Q3 (solution)"
---

\input{macros}
\begin{oframed}
$xyz$空間内の点$P(0,0,1)$を中心とする半径$1$の球面$K$がある．

$K$上の点$Q(a,b,c)$が条件$a>0,b>0,c>1$のもとで$K$上を動く時，$Q$において$K$に接する平面を$L$とし，$L$が$x$軸，$y$軸，$z$軸と交わる点をそれぞれ$A$，$B$，$C$とする．このような三角形$ABC$の面積の最小値を求めよ． 
\end{oframed}

## 【解】

$Q$は$K$上の点であるから
     

$$
\begin{align}
a^2+b^2+(c-1)^2=1 \label{1}
\end{align}
$$

が成り立つ．$L$は$\vector{PQ}=(a,b,c-1)$に垂直で点$Q$を通るので，その方程式は
     

$$
\begin{align*}
&a(x-a)+b(y-b)+(c-1)(z-c)=0 \\\therefore\ &ax+by+(c-1)z-c=0　\tag{\because[1](#1)}
\end{align*}
$$

となる．ゆえに$a>0,b>0,c>1$から
     

$$
\begin{align*}
A\left(\frac{c}{a},0,0\right) , B\left(0,\frac{c}{b},0\right) , C\left(0,0,\frac{c}{c-1}\right)
\end{align*}
$$

     
である．そこで
     

$$
\begin{align}
p=\frac{c}{a} , q=\frac{c}{b} , r=\frac{c}{c-1}\label{2}
\end{align}
$$

とおけば     
     

$$
\begin{align*}
&\vector{CA}=(p,0,-r) , \vector{CB}=(0,q,-r) \\&|\vector{CA}|^2=p^2+r^2 ,  
     |\vector{CB}|^2=q^2+r^2 \\&\vector{CA}\cdot\vector{CB}=r^2
\end{align*}
$$

である．よって三角形$ABC$の面積$S$は
     

$$
\begin{align*}
S&=\frac{1}{2}\sqrt{|\vector{CA}|^2|\vector{CB}|^2-(\vector{CA}\cdot\vector{CB})^2}\\&=\frac{1}{2}\sqrt{(p^2+r^2)(q^2+r^2)-r^4}\\&=\frac{1}{2}\sqrt{(pqr)^2(\frac{1}{p^2}+\frac{1}{q^2}+\frac{1}{r^2})}\\&=\frac{1}{2}\frac{pqr}{c}\tag{\because[1](#1),[2](#2)}
\end{align*}
$$

である．[2](#2)の値を代入して$S=\dfrac{c^2}{2ab(c-1)}$だから，以下この最小値を求める.
$a,b>0$から，[1](#1)にAM-GMを用いて
     

$$
\begin{align*}
2ab\le a^2+b^2=1-(c-1)^2=2c-c^2
\end{align*}
$$

である．等号成立は$a=b$の時．したがって$c-1>0$に注意して
     

$$
\begin{align}
S&=\frac{c^2}{ab(c-1)}\nonumber\\&\ge\frac{1}{2c-c^2}\frac{c^2}{c-1}\nonumber\\&=\frac{1}{3-(c+2/c)}\nonumber\\&\ge\frac{1}{3-2\sqrt{2}}\tag{\becauseAM-GM}\\&=3+2\sqrt{2}\label{3}
\end{align}
$$

等号成立は$c=2/c$つまり$c=\sqrt{2}$のときである($c>0$)．以上の等号成立条件を[1](#1)
に代入すれば$(a,b,c)=(\sqrt{\sqrt{2}-1},\sqrt{\sqrt{2}-1},\sqrt{2})$となって条件$a>0,b>0,c>1$を満たす．故に求める最小値は[3](#3)の$\min S=3+2\sqrt{2}\cdots$(答)である．