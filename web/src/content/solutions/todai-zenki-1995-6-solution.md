---
university: "todai"
category: "zenki"
year: "1995"
question: "6"
type: "solution"
title: "TODAI 1995 zenki Q6 (solution)"
---

\input{macros}
\begin{oframed}
原点を$O$とする$xy$平面上の双曲線
     \[\frac{x^2}{a^2}-\frac{y^2}{b^2}=1 \ \ \ \ \ (a>0,b>0) \]
上の点$P$における接線と$2$つの漸近線との交点を$Q$，$R$とする．このとき以下の問いに答えよ．
     

1.  三角形$QOR$の面積$S$は，点$P$の取り方にはよらず，$a$，$b$によって定まることを
     示せ．

2.  $a=5e^{2t}+e^{-t}$，$b=e^{2t}+e^{-t}$として実数$t$を変化させるときの$S$の最小値を求め
     よ．

\end{oframed}

## 【解】

     

1.  $2$本の漸近線は$y=\pm\dfrac{b}{a}x$であり，$P(X,Y)$での双曲線の接線$l$は
          \[\frac{Xx}{a^2}-\frac{Yy}{b^2}=1 \]
     である．故にこれらの交点は
          \[A=\dfrac{X}{a}+\dfrac{Y}{b} , B=\dfrac{X}{a}-\dfrac{Y}{b} \]
     として
          \[ \left(\frac{a}{A},\frac{-b}{A}\right),\left(\frac{a}{B},\frac{b}{B}\right)\]
     である．したがってサラスの公式から
          \begin{align}
          S&=\frac{1}{2}\left|\frac{ab}{AB}+\frac{ab}{AB}\right|  \nonumber\\   
          &=\frac{ab}{AB}  \nonumber\\
          &=ab \ \ \ \left(\because AB=\frac{X^2}{a^2}-\frac{Y^2}{b^2}=1\right)  \label{1}
          \end{align}
     となる．これは$X$，$Y$によらない定数である．$\Box$

2.  $p=e^t$とする．$t$が任意実数だから$p>0$である．[1](#1)に値を代入して
          \begin{align}
          S&=(5p^2+p^{-1})(p^2+p^{-1})\nonumber \\
          &=5p^4+6p+p^{-2} \label{2}
          \end{align}
     であるから，
          \begin{align*}
          \frac{dS}{dp}&=20p^3+6=\frac{2}{p^3} \\
          &=\frac{2}{p^3}(5p^3-1)(2p^3+1) 
          \end{align*}
     となって，下表をうる．          
          \begin{align*}
               \begin{array}{|c|c|c|c|c|} \hline
               p & 0 &   & \left(\dfrac{1}{5}\right)^{1/3} &   \\ \hline
               S' &   & - & 0                          & + \\ \hline
               S  &   & \se&                          &\ne \\ \hline
               \end{array}
          \end{align*}
     したがって[2](#2)とあわせて
          \begin{align*}
          \min S&=5\left(\frac{1}{5}\right)^{4/3}+6\left(\frac{1}{5}\right)^{1/3}+5^{2/3} \\
          &=7\left(\frac{1}{5}\right)^{1/3}+5^{2/3}\cdots\text{(答)}
          \end{align*}
     となる．