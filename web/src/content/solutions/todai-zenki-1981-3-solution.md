---
university: "todai"
category: "zenki"
year: "1981"
question: "3"
type: "solution"
title: "TODAI 1981 zenki Q3 (solution)"
---

\input{macros}
     \begin{oframed}
     放物線$y=x^2$を$C$で表す．$C$上の点$Q$を通り，$Q$における$C$の接線に垂直な直線
     を，$Q$における$C$の接線という．$0\le t\le1$とし，つぎの$3$条件をみたす点$P$を考える．
          \begin{itemize}
          \item[(イ)] $C$上の点$Q(t,t^2)$における$C$の法線上にある．
          \item[(ロ)] 領域$y\ge x^2$に含まれる．
          \item[(ハ)] $P$と$Q$の距離は$(t-t^2)\sqrt{1+4t^2}$である．
          \end{itemize}
     $t$が$0$から$1$まで嚥下する時，$P$の描く曲線を$C'$とする．このとき，$C$と$C'$とで囲ま
     れた部分の面積を求めよ．
     \end{oframed}

## 【解】

$(x^2)'=2x$だから，$Q$での法線方向のベクトル$\vec{l}$は，
     \[\vec{l}=\vtwo{-2t}{1}\]
と書ける．故に$P(X,Y)$は
     \[\vtwo{X}{Y}=\vtwo{t}{t^2}+s\vtwo{-2t}{1}\]
と書ける．(ハ)の条件から，
     

$$
\begin{align*}
&\left|s\vtwo{-2t}{1}\right|=(t-t^2)\sqrt{1+4t^2}\\\Longleftrightarrow&s=\pm(t-t^2)
\end{align*}
$$

である．条件(ロ)から複合正をとって，
      \[\vtwo{X}{Y}=\vtwo{t}{t^2}+(t-t^2)\vtwo{-2t}{1}\]
である．従って
     

$$
\begin{align*}
C: 
          &\begin{cases}
          X=2t^3-2t^2+t \\
          Y=t
          \end{cases}\\\Longleftrightarrow&X=2Y^3-2Y^2+Y&(0\le Y\le 1)
\end{align*}
$$

である．図示して右上図．
     
     \scalebox{.7}{\input{ut-81-3p}}
     

故に求める面積$S$は，上のように$S_1$，$S_2$をおいて，
     

$$
\begin{align}
S=1-S_1-S_2\label{1}
\end{align}
$$

と書ける．各項計算して
     

$$
\begin{align*}
S_1&=\int_0^1x^2dx=\frac{1}{3}\\
     S_2&=\int_0^1(2Y^3-2Y^2+Y)dY \\
     =&\left[\frac{Y^4}{2}-\frac{2Y^3}{3}+\frac{Y^2}{2}\right]_0^1 \\
     =&\frac{1}{3}
\end{align*}
$$

であるから，[1](#1)に代入して
     \[S=\frac{1}{3}\]
である．$\cdots$(答)