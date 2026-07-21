---
university: "kyodai"
category: "kouki"
year: "1991"
question: "1"
type: "solution"
title: "KYODAI 1991 kouki Q1 (solution)"
---

## 【解】

### (1)

    条件1で$y=f(x)$とおくと，
    
$$
\begin{align}
& x = \pm\sqrt{1-\sin y}& ( \because -1 \le\sin y \le 1 ) \label{1991-1:eq:1}
\end{align}
$$

    である．$\cdots$(答)

    次に，グラフは$y$軸対称なので，複号正の部分を考えて$x\ge 0$に折り返せば良い．
    $\eqref{1991-1:eq:1}$の複号正を両辺を$x$で微分すると
    
$$
\begin{align*}
& 1 = \frac{-\cos y}{2\sqrt{1-\sin y}}\frac{dy}{dx}\\\therefore& \frac{dy}{dx} = \frac{-2\sqrt{1-\sin y}}{\cos y}\le 0
\end{align*}
$$

    だから，$0\le x , 0 \le y\le \pi/2$の区間で$y$は単調減少である．
    端点での値は
    
$$
\begin{align*}
f(0) & =\pi/2 \\
        f(1) & =0
\end{align*}
$$

    だから，グラフは[図1](#1991-1:fig:1)のようになる．$\cdots$(答)

    

<figure id="1991-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1991/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 曲線$y=f(x)$の様子</figcaption>
</figure>

### (2)

    題意の面積 $S$ は[図2](#1991-1:fig:2)の斜線部の面積 $S'$ として，対称性より
    
$$
\begin{align}
S = 2S' \label{1991-1:eq:2}
\end{align}
$$

    で与えられる．

    

<figure id="1991-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1991/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 曲線$y=f(x)$と$x$軸で囲まれた部分</figcaption>
</figure>

    $S'$は$y$軸方向の積分とみなすことで，
    
$$
\begin{align*}
S'
         & = \int_0^{\pi/2}\sqrt{1-\sin y}\, dy                \\& = \int_0^{\pi/2}\frac{\cos y}{\sqrt{1+\sin y}}\, dy \\& = \left[ 2(1+\sin y)^{1/2}\right]_0^{\pi/2}\\& = 2(\sqrt{2}-1)
\end{align*}
$$

    だから$\eqref{1991-1:eq:2}$に代入して
    
$$
\begin{align*}
S = 4(\sqrt{2}-1)
\end{align*}
$$

    が求める面積である．$\cdots$(答)

    
    

## 【解説】