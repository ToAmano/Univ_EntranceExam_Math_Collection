---
university: "kyodai"
category: "kouki"
year: "2001"
question: "6"
type: "solution"
title: "KYODAI 2001 kouki Q6 (solution)"
---

## 【解】

  

<figure id="2001-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2001/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円$C_1$の様子</figcaption>
</figure>

  点Pは$C_1$上にあるので$P(\cos\theta,\sin\theta)$とおく．
  ただし $0 \le \theta < 2\pi$ とする．
  点Pでの$C_1$の接線$l$の方程式は
  

$$
\begin{align*}
l: \cos\theta x+\sin\theta y=1
\end{align*}
$$

  である．この方向ベクトルは
  

$$
\begin{align*}
\begin{pmatrix}\sin\theta\\ -\cos\theta\end{pmatrix}
\end{align*}
$$

  だから，直線RQがこれと直交することにより
  

$$
\begin{align}
\vec{RQ}\parallel\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix} \label{2001-6:eq:1}
\end{align}
$$

  である．

  また，線分RQの長さは直線$l$と点Rの距離に等しく
  

$$
\begin{align*}
|RQ|
     & = \frac{|a\cos\theta  - 1|}{\cos^2\theta + \sin^2\theta}\\& = |a\cos\theta  - 1|
\end{align*}
$$

  である．ここで$-1\le\cos\theta \le 1$および，題意より$-1<a<-1/2$だから$-1<\cos\theta a < 1$となり，
  $|\cos\theta a -1 | = 1-\cos\theta$だから
  

$$
\begin{align}
|RQ|
     & = \left(1-a\cos\theta\right)\label{2001-6:eq:2}
\end{align}
$$

  である．

  [(式2)](#2001-6:eq:1,2001-6:eq:2)から，
  

$$
\begin{align*}
\vec{RQ}& = \left(a\cos\theta -1\right)\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix}
\end{align*}
$$

  であるから，点$Q(X,Y)$の座標は
  

$$
\begin{align}
\begin{pmatrix} X                                          \\ Y \end{pmatrix}
     & = \vec{OR} + \vec{RQ}\\& = \left(a\cos\theta -1\right)\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix} + \begin{pmatrix}a \\ 0\end{pmatrix} \\\therefore& \begin{dcases}
         X(\theta) = \cos\theta-a\cos^2\theta +a \\
         Y(\theta) = \sin\theta-a\cos\theta\sin\theta
       \end{dcases}\label{2001-6:eq:3}
\end{align}
$$

  となる．

  一階微分は
  

$$
\begin{align*}
\frac{dX}{d\theta}& = -\sin\theta+2a\cos\theta\sin\theta\\& = \sin\theta\left(2a\cos\theta-1\right)\\\frac{dY}{d\theta}& = \cos\theta-a\left(2\cos^2\theta-1\right)\\& = -2a\cos^2\theta+\cos\theta+a
\end{align*}
$$

  となる．$-1<a<-1/2$に注意して，$Q(X,Y)$の増減表は[表1](#2001-6:table:1)となる．
  ただし，$C_2$は$x$軸に関して対称だから，$0\le \theta \le \pi$についてのみ示している．
  また，$\alpha,\beta$は
  

$$
\begin{align*}
& 0 < \alpha < \beta < \pi\\& \cos\alpha = \frac{1-\sqrt{1+8a^2}}{4a}\\& \cos\beta = \frac{1}{2a}
\end{align*}
$$

  を満たす．

  

<figure id="2001-6:table:1" class="table-wrapper">

| $\theta$ | 0 | $\cdots$ | $\alpha$ | $\cdots$ | $\beta$ | $\cdots$ | $\pi$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $\dot{X}$ |  | $-$ | $-$ | $-$ | 0 | $+$ | $0$ |
| $\dot{Y}$ |  | $+$ | 0 | $-$ | $-$ | $-$ | $-$ |
| (X,Y) | $(1,0)$ | $\nwarrow$ |  | $\swarrow$ |  | $\searrow$ | $(-1,0)$ |

  <figcaption>表 1: $(X,Y)$の増減表</figcaption>
</figure>

  従って，$C_2$の軌跡の概形は[図2](#2001-6:fig:2)である．

  

<figure id="2001-6:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2001/6/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $C_2$の概形．$(1,0)$が$\theta=0$，$(-1,0)$が$\theta=\pi$に対応する．</figcaption>
</figure>

  したがって，たしかに$C_2$の$x$座標は $-1$より小さい値を取りうる．
  よって題意の前半は示された．$\cdots$(答)

  次に，$C_2$の囲む面積$S$を求める．
  $S$のうち$y \ge 0$の部分を $S'$として，$C_2$が$x$軸に関して対称だから
  

$$
\begin{align}
S = 2S' \label{2001-6:eq:4}
\end{align}
$$

  である．
  $y\ge 0$の部分でグラフの上側 $y_+$, 下側 $y_-$とすると
  

$$
\begin{align*}
S'
     & = \int_{x(\beta)}^{1} y_+ dx - \int_{x(\beta)}^{-1} y_- dx                                                \\& = \int_{\beta}^{0} y_{+}\frac{dx}{d\theta} d\theta - \int_{\beta}^{\pi} y_{-}\frac{dx}{d\theta} d\theta\\& = -\int_{0}^{\pi} y \frac{dx}{d\theta} d\theta\\
\end{align*}
$$

  である．
  ここに[(式3)](#2001-6:eq:3)を代入して
  

$$
\begin{align}
S'
     & = -\int_{0}^{\pi}\sin\theta\left(1-a\cos\theta\right)\sin\theta\left(2a\cos\theta-1\right) d\theta\\& = -\int_{0}^{\pi}\sin^2\theta\left[-2a^2\cos^2\theta + 3a\cos\theta -1 \right] d\theta\label{2001-6:eq:5}\\
\end{align}
$$

  である．これら各項を計算すると
  

$$
\begin{align*}
\int_{0}^{\pi}\sin^2\theta\cos^2\theta d\theta& =    \frac{1}{4}\int_{0}^{\pi}\sin^2 2\theta d\theta\\& =    \frac{1}{8}\int_{0}^{\pi}\left(1-\cos 4\theta\right) d\theta\\& =    \frac{1}{8}\left[\theta-\frac{\sin 4\theta}{4}\right]_{0}^{\pi}\\& =    \frac{\pi}{8}\\\int_{0}^{\pi}\sin^2\theta\cos\theta d\theta& = \left[\frac{1}{3}\sin^3\theta\right]_{0}^{\pi}\\& = 0                                                                    \\\int_{0}^{\pi}\sin^2\theta d\theta& =    \frac{1}{2}\int_{0}^{\pi}\left(1-\cos 2\theta\right) d\theta\\& =    \frac{1}{2}\int_{0}^{\pi}\left[1-\cos 2\theta\right] d\theta\\& =    \frac{1}{2}\left[\theta-\frac{1}{2}\sin 2\theta\right]_{0}^{\pi}\\& =    \frac{\pi}{2}
\end{align*}
$$

  だから，[(式5)](#2001-6:eq:5)に代入して
  

$$
\begin{align*}
S'
     & = 2a^2\frac{\pi}{8} + \frac{\pi}{2}\\& = \frac{\pi}{2}\left(\frac{a^2}{2}+1\right)
\end{align*}
$$

  だから，[(式4)](#2001-6:eq:4)に代入して
  

$$
\begin{align*}
S = \frac{\pi}{2}\left(a^2+2\right)
\end{align*}
$$

  が求める面積である．$\cdots$(答)

  
  

## 【解説】