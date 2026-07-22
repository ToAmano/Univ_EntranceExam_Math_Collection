---
university: "ukyoto"
category: "kouki"
year: "1997"
question: "6"
type: "solution"
title: "UKYOTO 1997 kouki Q6 (solution)"
---

## 【解】

  まずは曲線$C$の概形を求める．
  わかりやすさのため
  

$$
\begin{align*}
x = f(t) = e^{-t}\cos t \\
    y = g(t) = e^{-t}\sin t
\end{align*}
$$

  とおくと，
  

$$
\begin{align*}
f'(t) & = -e^{-t}\left(\sin t+\cos t\right) < 0 \\
    g'(t) & = e^{t}\left(\cos t - \sin t\right)
\end{align*}
$$

  である．従って，$f(t)$は区間内で単調に減少する．
  曲線$C$の増減表は[表1](#1997-1:table:1)となる．
  

<figure id="1997-1:table:1" class="table-wrapper">

| $t$ | $0$ | $\cdots$ | $\pi/4$ | $\cdots$ |   $\pi/2$    |
|:-----:|:-----:|:----------:|:---------:|:----------:|:--------------:|
| $x$ | $1$ |   $-$    |           |   $-$    |     $0$      |
| $y$ | $0$ |   $+$    |           |   $-$    | $e^{-\pi}/2$ |

  <figcaption>表 1: 曲線$C$の増減表</figcaption>
</figure>

  従って，グラフの概形は[図1](#1997-6:fig:1)となる．
  

<figure id="1997-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1997/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $C$の概形</figcaption>
</figure>

  
  (1)
  媒介表示曲線の長さの公式から，
  

$$
\begin{align*}
L
     & = \left|\int_0^{\pi/2}\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt\right|\\& = \left|\int_0^{\pi/2} e^{-t}\sqrt{(\sin t+\cos t)^2 + (\cos t-\sin t)^2} dt \right|\\& = \int_0^{\pi/2} e^{-t}\sqrt{2} dt                                                                 \\& = -\sqrt{2}\left[e^{-t}\right]_0^{\pi/2}\\& = \sqrt{2}\left(1-e^{\pi/2}\right)
\end{align*}
$$

  が求める長さである．$\cdots$(答)

  
  (2)
  求める面積$S$は[図1](#1997-6:fig:1)の斜線部であり
  

$$
\begin{align}
S & = \int_0^{1} y dx                                                           \\& = \int_{\pi/2}^{0} y \frac{dx}{dt} dt                                       \\& = \int_{\pi/2}^{0} e^{-t}\sin t \cdot e^{-t}(-\sin t-\cos t) dt             \\& = \int_0^{\pi/2} e^{-2t}\left(\frac{1-\cos 2t+\sin 2t}{2}\right) dt        \\& = \frac{1}{4}\int_0^{\pi} e^{-p}(1-\cos p + \sin p) dp \label{1997-6:eq:1}
\end{align}
$$

  ただし，最後の行では積分変数を$p=2t$に取り替えた．

  各項計算して
  

$$
\begin{align*}
\cdot& \int_0^{\pi} e^{p} dp
    = 1 - e^{-\pi}\\\cdot& \int_0^{\pi}\cos p e^{-p} dp
    = \frac{1}{2}\left[e^{-p}(-\cos p + \sin p)\right]_{0}^{\pi}\\& = \frac{1}{2}(e^{-\pi}+1)                             \\\cdot& \int_0^{\pi}\sin p e^{-p} dp
    = \frac{1}{2}\left[e^{-p}(-\sin p - \cos p)\right]_{0}^{\pi}\\& = \frac{1}{2}(e^{-\pi}+1)
\end{align*}
$$

  だから，[(式1)](#1997-6:eq:1)に代入して求める面積は
  

$$
\begin{align*}
T = \frac{1}{4}\left(1-e^{-\pi}\right)
\end{align*}
$$

  である．  $\cdots$(答)

  
  

## 【解説】