---
university: "todai"
category: "zenki"
year: "1991"
question: "6"
type: "solution"
title: "TODAI 1991 zenki Q6 (solution)"
---

\input{macros}
     \begin{oframed}
     $f(x)$は$x>0$で定義された連続な関数で，$0<x_1<x_2$ならば，つねに$f(x_1)>f(x_2)>0$であるものとし，
     $S(x)=\dint{x}{2x}f(t)dt$とおく．このとき，$S(1)=1$であり，さらに任意の$a>0$に対して，原点と点$(a,f(a))$，原点と点
     $(2a,f(2a))$を結ぶ$2$直線と曲線$y=f(x)$とで囲まれる部分の面積は$3S(x)$に等しいものとする．
          

1.  $S(x)$，$f(x)-2f(2x)$をそれぞれ$x$の関数として表せ．

2.  $x>0$に対して，$a(x)=\dlim{n}{\infty}2^nf(2^nx)$とおく．積分$\dint{x}{2x}a(t)dt$を求めよ．

3.  関数$f(x)$を決定せよ．

     \end{oframed}

## 【解】

 
     

1.  題意から，$f(x)$は区間内で単調減少である．また，
          \begin{align}
          S(x)=\int_x^{2x}f(t)dt\label{0}
          \end{align} 
     である．グラフの概形は下図．
          
          \scalebox{0.7}{\input{ut-91-6p}}
          
     故に，題意から
          \begin{align}
          3S(x)&=\int_x^{2x}f(t)dt+\frac{1}{2}xf(x)-\frac{1}{2}2xf(2x) \nonumber\\
          &=S(x)+\frac{1}{2}xf(x)-xf(2x) \nonumber\\
          S(x)&=\frac{1}{4}x(f(x)-2f(2x)) \label{1}
          \end{align}
     である．$g(x)=f(x)-2f(2x)$とおくと，[0](#0)，[1](#1)から
          \begin{align}
               \begin{array}{l}
               S'(x)=2f(2x)-f(x)=-g(x) \\
               S(x)=\dfrac{1}{4}xg(x) 
               \end{array}\label{2}
          \end{align}
     $g(x)$を消して，$S(x)=y$とすれば，
          \[4y=-x\frac{dy}{dx} \]
     となる．$0<x$で$0<f(x)$であるから，$y>0$となるので，変形して
          \[\frac{-4x}{dx}=\frac{y}{dy}\]
     積分して，$S(1)=1$より，
          \[y=S(x)=x^{-4}\]
     である．従って[2](#2)から，$g(x)=4x^{-5}$である．$\cdots$(答)

2.  $a_n(x)=2^nf(2^nx)$とおく．前問の結果で$x$に$2^nx$を代入して，
          \begin{align*}
          2f(2^{n+1}x)&=f(2^nx)-4(2^nx)^{-5} \\
          2^{n+1}f(2^{n+1}x)&=2^nf(2^nx)-2^{n+2}(2^nx)^{-5} \\
          a_{n+1}(x)&=a_n(x)-2^{2-4n}x^{-5}
          \end{align*}
     である．繰り返し用いて，$n\ge1$のとき，
          \begin{align*}
          a_n(x)=a_0(x)-\sum_{k=0}^{n-1}2^{2-4n}x^{-5} \\
          a_n(x)=f(x)-4x^{-5}\frac{1-2^{-4n}}{1-2^4} \\
          \limit{n}{\infty}f(x)-\frac{64}{15}x^{-5}=a(x)
          \end{align*}
     であるから，求める積分値は
           \begin{align*}
           \dint{x}{2x}a(t)dt&=S(x)+\left[\frac{16}{15}t^{-4}\right]_x^{2x} \\
           &=x^{-4}+\frac{16}{15}\left(\frac{1}{16}-1\right)x^{-4} \\
           &=0
           \end{align*}
      である．

3.  $f(x)>0$から，$a(x)>0$である．これと前問の積分計算から，被積分が恒等的に$0$である．
           \[a(x)\equiv0\Longleftrightarrow f(x)=\frac{64}{15}x^{-5}\]
      これは$x>0$で定義された，連続な単調減少関数であり，十分である．以上から，
           \[f(x)=\frac{64}{15}x^{-5}\]
      である．$\cdots$(答)