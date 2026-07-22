---
university: "ukyoto"
category: "kouki"
year: "1998"
question: "6"
type: "solution"
title: "UKYOTO 1998 kouki Q6 (solution)"
---

## 【解】

  (1)
  半角公式により
  

$$
\begin{align*}
\cos 2\theta& = 2cos^2\theta - 1
\end{align*}
$$

  だから，$I_n$は
  

$$
\begin{align*}
I_n
     & = \int_0^{\pi/4}\cos^{n}2\theta\sin^3\theta d\theta\\& = \int_0^{\pi/4}\left(2\cos^2\theta - 1\right)^{n}\sin^3\theta d\theta\\& = \int_0^{\pi/4}\left(2\cos^2\theta - 1\right)^{n}\sin^2\theta\cdot\sin\theta d\theta\\& = \int_0^{\pi/4}\left(2\cos^2\theta - 1\right)^{n}\left(1-\cos^2\theta\right)\sin\theta d\theta
\end{align*}
$$

  と変形できる．$t = \cos\theta$とおくと$dt/d\theta = - \sin\theta$だから
  

$$
\begin{align*}
I_n = \int_{\sqrt{2}/2}^{1}\left(2t^2 - 1\right)^{n}\left(1-t^2\theta\right) dt
\end{align*}
$$

  と置換積分できる．

  ここに$n=2$を代入して$I_2$を計算すると，
  

$$
\begin{align*}
I_2
     & = \int_{\sqrt{2}/2}^{1}\left(2t^2 - 1\right)^{2}\left(1-t^2\theta\right) dt                                                                                                                 \\& = \int_{\sqrt{2}/2}^{1}\left(4t^4 - 4t^2 + 1\right)\left(1-t^2\theta\right) dt                                                                                                               \\& = \int_{\sqrt{2}/2}^{1}\left(4t^4 - 4t^2 + 1 - (4t^6 - 4t^4 +t^2)\right) dt                                                                                                                  \\& = \int_{\sqrt{2}/2}^{1}\left(-4t^6 + 8t^4 - 5t^2 + 1 \right) dt                                                                                                                              \\& = \left[-\frac{4}{7}t^7 + \frac{8}{5}t^5 - \frac{5}{3}t^3 + t \right]_{\sqrt{2}/2}^{1}\\& = \left[-\frac{4}{7} + \frac{8}{5} - \frac{5}{3} + 1 \right]\\& - \left[-\frac{4}{7}\left(\frac{1}{\sqrt{2}}\right)^7 + \frac{8}{5}\left(\frac{1}{\sqrt{2}}\right)^5 - \frac{5}{3}\left(\frac{1}{\sqrt{2}}\right)^3 + \left(\frac{1}{\sqrt{2}}\right)\right]\\& = \left[-\frac{4}{7} + \frac{8}{5} - \frac{5}{3} + 1 \right]\\& - \left[-\frac{4}{7}\left(\frac{1}{\sqrt{2}}\right)^7 + \frac{8}{5}\left(\frac{1}{\sqrt{2}}\right)^5 - \frac{5}{3}\left(\frac{1}{\sqrt{2}}\right)^3 + \left(\frac{1}{\sqrt{2}}\right)\right]\\& = \frac{38}{105} - \left(-\frac{4}{7\cdot 8}+\frac{8}{5\cdot 4}- \frac{5}{3\cdot 2}+1\right)\frac{1}{\sqrt{2}}\\& = \frac{38}{105} - \frac{26\sqrt{2}}{105}
\end{align*}
$$

  が求める値である．  $\cdots$(答)

  
  (2)
  まずは題意の曲線の軌跡を求める．
  $P(x(\theta),y(\theta))$を曲線上の点とすると，$r=\sin 2\theta$より
  

$$
\begin{align*}
\begin{pmatrix}x                            \\ y\end{pmatrix}
     & = r \begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix} \\& = \sin 2\theta\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix}
\end{align*}
$$

  と書ける．
  一階微分は，半角公式より
  

$$
\begin{align*}
x'(\theta)
               & = \cos 2\theta\cos\theta - \sin 2\theta\sin\theta\\& = 2\cos\theta(1-3\sin^2\theta)                    \\
    y'(\theta) & = \cos 2\theta\sin\theta + \sin 2\theta\cos\theta\\& = 2\sin\theta(2-3\sin^2\theta)
\end{align*}
$$

  となるから，$0 \le \theta \le \pi/2$の範囲での増減表は[表1](#1998-6:table:1)となる．
  ただし，$\alpha, \beta$ は
  

$$
\begin{align}
\begin{dcases}
      \sin\alpha & = \sqrt{\frac{1}{3}} \\
      \sin\beta  & = \sqrt{\frac{2}{3}}
    \end{dcases}\label{1998-6:eq:1}
\end{align}
$$

  をみたす角度とする．
  

<figure id="1998-6:table:1" class="table-wrapper">

| $\theta$ | $0$ |  | $\alpha$ |  | $\beta$ |  | $\pi/2$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $x'$ |  | $+$ | $0$ | $-$ | $-$ | $-$ |  |
| $y'$ |  | $+$ | $+$ | $+$ | $+$ | $0$ |  |
| $(x,y)$ | $(0,0)$ | $\nearrow$ |  | $\nwarrow$ |  | $\swarrow$ | $(0,0)$ |

  <figcaption>表 1: $(x,y)$の増減表</figcaption>
</figure>

  また，$\theta=\alpha,\beta$の時の$(x,y)$の値は[(式1)](#1998-6:eq:1)より
  

$$
\begin{align*}
x(\alpha)
     & = 2\sin\alpha\cos^2\alpha\\& = 2\sin\alpha(1-\sin^2\alpha) \\& = \frac{4\sqrt{3}}{9}\\
    x(\beta)
     & = 2\sin\beta(1-\sin^2\beta)   \\& = \frac{2\sqrt{6}}{9}\\
    y(\alpha)
     & =  2\sin^2\alpha\cos\alpha\\& = \frac{2\sqrt{6}}{9}\\
    y(\beta)
     & =  2\sin^2\beta\cos\beta\\& = \frac{4\sqrt{3}}{9}
\end{align*}
$$

  である．
  従って，$P(x,y)$の軌跡の概形は[図1](#1998-6:fig:1)のようになる．

  

<figure id="1998-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1998/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: パラメータ表示された曲線 $X(t) = \sin 2t \cos t$, $Y(t) = \sin 2t \sin t$の軌跡．</figcaption>
</figure>

  さて，以下この軌跡を$y=x$周りに回転して得られる立体の体積$V$を求める．
  求める体積は，図形全体を$-pi/4$回転させたものを$x$軸周りに回転した体積と等しいのでそれを求める．
  まず，この領域が$y=x$を軸として（回転後は$x$軸を軸として）対称であることを示す．

  そこで，点$(x(\theta), y(\theta))$を負の方向に$\pi/4$回転させた点を$X(\theta), Y(\theta)$とおくと，
  

$$
\begin{align*}
\begin{dcases}
      X(\theta) = \sin 2\theta \cos\left(\theta - \frac{\pi}{4}\right) \\
      Y(\theta) = \sin 2\theta \sin\left(\theta - \frac{\pi}{4}\right)
    \end{dcases}\\\therefore\begin{dcases}
      X(\theta) = \cos 2\left(\theta - \frac{\pi}{4}\right) \cos\left(\theta - \frac{\pi}{4}\right) \\
      Y(\theta) = \cos 2\left(\theta - \frac{\pi}{4}\right) \sin\left(\theta - \frac{\pi}{4}\right)
    \end{dcases}
\end{align*}
$$

  と書き直せる．
  ここで，$t = \theta - \frac{\pi}{4}$とおくと，$0 \le \theta \le \pi/2$より
  

$$
\begin{align*}
-\frac{\pi}{4}\le t \le\frac{\pi}{4}
\end{align*}
$$

  であり，$X(t), Y(t)$は
  

$$
\begin{align*}
\begin{dcases}
      X(t) = \cos 2t \cos t \\
      Y(t) = \cos 2t \sin t
    \end{dcases}
\end{align*}
$$

  となる．これは$t=0$を中心として$x$軸対称だから，
  元の領域は$y=x$を軸として対称である．（[図2](#1998-6:fig:2)）

  

<figure id="1998-6:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1998/6/fig_2.svg" alt="図 2" />
  <figcaption>図 2: パラメータ表示された曲線 $X(t) = \cos 2t \cos t$, $Y(t) = \cos 2t \sin t$と，$Y\ge 0$の領域．</figcaption>
</figure>

  従って，体積$V$はこの$-pi/4$回転した領域で，$Y(t) \ge 0$をみたす部分（$0\le t\le \pi/4$）のみを考えればよい．
  

$$
\begin{align*}
V & = \int_0^{1}\pi Y^2 dX                                                                 \\& = \int_{\pi/4}^{0}\pi Y^2(t) \frac{dX}{dt} dt                                          \\& = \int_{\pi/4}^{0}\pi(\cos 2t)^2 \sin^2 t (-2\sin 2t\cos t-\cos 2t\sin t ) dt         \\& = \int_{\pi/4}^{0}\pi(\cos 2t)^2 \sin^2 t (-4\sin t \cos^2 t - \sin t (1-2\sin^2)) dt \\& = \int_{0}^{\pi/4}\pi(\cos 2t)^2 \sin^3 t (4(1-\sin^2 t) + (1-2\sin^2 t) ) dt         \\& = \int_{0}^{\pi/4}\pi(\cos 2t)^2 \sin^3 t (5-6\sin^2 t) dt                            \\& = \int_{0}^{\pi/4}\pi(\cos 2t)^2 (5\sin^3 t-6\sin^5 t) dt
\end{align*}
$$

  と変形できる．
  倍角公式$\cos 2\theta = 1-2\sin^2\theta$を用いて$\sin^5 t$を書き直すと
  

$$
\begin{align*}
V
     & = \int_{0}^{\pi/4}\pi(\cos 2t)^2 (5\sin^3 t-3\sin^3 t(1-\cos 2t)) dt    \\& = \int_{0}^{\pi/4}\pi\left[3(\cos 2t)^3+2(\cos 2t)^2\right]\sin^3 t dt \\& = 3\pi I_3 + 2\pi I_2
\end{align*}
$$

  である．よって題意は示された．$\cdots$(答)

  
  

## 【解説】