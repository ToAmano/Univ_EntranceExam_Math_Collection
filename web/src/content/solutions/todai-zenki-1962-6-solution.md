---
university: "todai"
category: "zenki"
year: "1962"
question: "6"
type: "solution"
title: "TODAI 1962 zenki Q6 (solution)"
---

\input{macros}
     \begin{oframed}
     曲線$y=6\sin(x/6)$の上で$x=2\pi$，$x=6\pi$なる点をそれぞれ$P$，$Q$とし，点$P$，$Q$における曲線の接線の交点を$R$とする．
     このとき
          

1.  $R$の座標を求めよ．

2.  線分$PR$，$QR$と上の曲線とで囲まれる図形の面積を求めよ．

     \end{oframed}

## 【解】

 
     

1.  $h(x)=6\sin(x/6)$とおく．
          \[h'(x)=\cos(x/6)\]
     だから，$P$ ，$Q$における接線$l_p$，$l_q$は，
          \begin{align*}
               \begin{cases}
               l_p&:y=\dfrac{1}{2}(x-2\pi)+3\sqrt{3}\equiv f(x) \\
               l_q&:y=-(x-6\pi)\equiv g(x)
               \end{cases}
          \end{align*}
     だから，$R$はこれらの交点で，
          \[R(14\pi/3-2\sqrt{3},4\pi/3+2\sqrt{3})\]
     である．$\cdots$(答)

2.  グラフの概形は下図である．ただし，
          \[t=14\pi/3-2\sqrt{3}\]
     である．
          
          \scalebox{1}{\input{ut-62-6p}}
          
     従って，求める面積$S$として，
          \begin{align}
          S&=\int_{2\pi}^tfdx+\int_t^{6\pi}gdx-\int_{2\pi}^{6\pi}hdx \nonumber\\
          &=\frac{8}{3}\pi^2+8\sqrt{3}\pi-63\nonumber
          \end{align}
     である．$\cdots$(答)