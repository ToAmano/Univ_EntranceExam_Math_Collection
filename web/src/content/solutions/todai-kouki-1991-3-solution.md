---
university: "todai"
category: "kouki"
year: "1991"
question: "3"
type: "solution"
title: "TODAI 1991 kouki Q3 (solution)"
---

## 【解】

### (1)

  

<figure id="1991-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1991/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 五角形ARPQBの様子</figcaption>
</figure>

  $AP = x, BP = y$ とおく($0<x,y<2$)．
  $\triangle ABP$に余弦定理を用いて
  
$$
\begin{align}
4 = x^2 + y^2 - 2xy\cos\theta\label{1991-3:eq:1}
\end{align}
$$

  である．

  三角形APR，APB，PBQの面積は
  
$$
\begin{align*}
\triangle APR
     & = \frac{1}{2}|AR|RP|                             \\& = \frac{1}{2}x^2\sin(\pi-\theta)\cos(\pi-\theta) \\& = -\frac{1}{2}x^2\sin\theta\cos\theta\\\triangle APB
     & = \frac{1}{2}|AP||BP|                            \\& = \frac{1}{2}xy\sin\theta\\\triangle PBQ
     & = \frac{1}{2}|PQ||QB|                            \\& = \frac{-1}{2}y^2\sin\theta\cos\theta
\end{align*}
$$

  だから，五角形ARPQBの面積はこれら3つの面積の和で
  
$$
\begin{align}
S
     & = \triangle APR + \triangle APB + \triangle PBQ                                                 \\& = \frac{1}{2}\left(-x^2\sin\theta\cos\theta + \sin\theta xy - \sin\theta\cos\theta y^2\right)\\& = \frac{1}{2}\sin\theta\left(-\cos\theta x^2+xy-\cos\theta y^2\right)\label{1991-3:eq:2}
\end{align}
$$

  である．

  よって$\eqref{1991-3:eq:2}$の元での$\eqref{1991-3:eq:1}$のとりうる範囲を求めれば良い．
  $\eqref{1991-3:eq:1}$を$\eqref{1991-3:eq:2}$に代入して$xy$だけを残すと
  
$$
\begin{align}
S
     & =\frac{1}{2}\sin\theta\left[xy-\cos\theta\left(4 + 2xy\cos\theta\right)\right]\\& =\frac{1}{2}\sin\theta\left[xy-\cos\theta\left(4 + 2xy\cos\theta\right)\right]\\& =\frac{1}{2}\sin\theta\left[-4\cos\theta + (1-2\cos^2\theta)xy \right]\label{1991-3:eq:3}
\end{align}
$$

  となる．これを$f(xy)$と置く．

  ここで$\alpha=x+y, \beta=xy$とすると、まず$x,y$は$t$の2次方程式 $t^2 - \alpha t + \beta = 0$ の $0<t<2$ をみたす
  2実解(重解含む)だから
  
$$
\begin{align}
& \begin{dcases}
         \text{端点}: \beta > 0, 4-2\alpha+\beta>0 \\
         \text{判別式}: \alpha^2-4\beta \ge 0       \\
         \text{軸}: 0 < \frac{\alpha}{2} < 2
       \end{dcases}\\\iff& \begin{dcases}
         \beta > 0                     \\
         \beta > 2\alpha-4             \\
         \beta \le \frac{1}{4}\alpha^2 \\
         0 < \alpha < 4
       \end{dcases}\label{1991-3:eq:4}
\end{align}
$$

  である．

  また，$\eqref{1991-3:eq:1}$を$\alpha,\beta$で書き換えると
  
$$
\begin{align}
4 = \alpha^2 - 2(1+\cos\theta)\beta\label{1991-3:eq:5}
\end{align}
$$

  である．

  $\eqref{1991-3:eq:4,1991-3:eq:5}$を図示すると下図太線部(境界含む)だから
  
$$
\begin{align*}
0 < \beta\le\frac{\alpha^2-4}{2(1+c)}\\\therefore
    0 < \beta\le\frac{2}{1-\cos\theta}
\end{align*}
$$

  となる．

  

<figure id="1991-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1991/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $\alpha,\beta$の存在領域</figcaption>
</figure>

  $\eqref{1991-3:eq:3}$は$\beta=xy$についての一次式だから，とりうる範囲は$\frac{\pi}{2} < \theta < \pi$より
  
$$
\begin{align*}
\begin{dcases}
      \frac{\pi}{2} < \theta < \frac{3\pi}{4} \text{の時, } f(0) < S \le f\left(\frac{2}{1-\cos\theta}\right) \\
      \theta = \frac{3\pi}{4} \text{の時, } S=1                                                               \\
      \frac{3\pi}{4} < \theta < \pi \text{の時, } f\left(\frac{2}{1-\cos\theta}\right) \le S < f(0)
    \end{dcases}
\end{align*}
$$

  である．

  ここで
  
$$
\begin{align*}
f(0)
     & = -2\sin\theta\cos\theta = -2\sin 2\theta\\
    f\left(\frac{2}{1-\cos\theta}\right)& = \frac{1}{2}\sin\theta\left[-4\cos\theta + (1-2\cos^2\theta)\frac{2}{1-\cos\theta}\right]\\& = \frac{\sin\theta}{1-\cos\theta}\left[-2\cos\theta(1-\cos\theta) + (1-2\cos^2\theta) \right]\\& = \frac{\sin\theta(1-2\cos\theta)}{1-\cos\theta}
\end{align*}
$$

  だから，
  
$$
\begin{align*}
\begin{dcases}
      -\sin2\theta < S \le \frac{\sin\theta(1-2\cos\theta)}{1-\cos\theta} & (\frac{\pi}{2} < \theta < \frac{3\pi}{4}) \\
      S=1                                                                 & (\theta = \frac{3\pi}{4})                 \\
      \frac{\sin\theta(1-2\cos\theta)}{1-\cos\theta} \le S < -\sin2\theta & (\frac{3\pi}{4} < \theta < \pi)
    \end{dcases}
\end{align*}
$$

  となる．$\cdots$(答)

### (2)

  $\theta$が$\frac{\pi}{2}<\theta<\pi$を満たして動く時の$S$の範囲を求めれば良い．
  そこで，$S$の上限下限を表す関数を
  
$$
\begin{align*}
g(\theta) & = \frac{\sin\theta(1-2\cos\theta)}{1-c-\theta}\\
    h(\theta) & = -\sin 2\theta
\end{align*}
$$

  とする．

  $g(\theta)$の概形を求めるため，一階微分を計算すると
  
$$
\begin{align*}
g'(\theta)
     & = \frac{(1-\cos\theta)(\cos\theta-2\cos^2\theta+2\sin^2\theta)-\sin^2\theta(1-2\cos\theta)}{(1-\cos\theta)^2}\\& = \frac{(1-\cos\theta)(2+\cos\theta-4\cos^2\theta)-(1-\cos^2\theta)(1-2\cos\theta)}{(1-\cos\theta)^2}\\& = \frac{-2\cos^2\theta+2\cos\theta+1}{1-\cos\theta}
\end{align*}
$$

  だから，$\theta_0 $を $\frac{\pi}{2}<\theta_0<\pi $かつ$ \cos\theta_0 = \frac{1-\sqrt{3}}{2} $をみたすようにとって
  $g(\theta)$の増減表は$\eqref{1991-3:table:1}$となる．

  \begin{table}[H]
    \centering
    \caption{$g(\theta)$の増減表}
    \label{1991-3:table:1}
    

| $\theta$ | $\frac{\pi}{2}$ | | $\theta_0$ | | $\frac{3\pi}{4}$ | | $\pi$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $c$ | $0$ | $+$ | $0$ | $-$ | $-$ | $-$ | $-1$ |
| $g'$ | | $+$ | $0$ | $-$ | $-$ | $-$ | |
| $g$ | $(1)$ | $\nearrow$ | | $\searrow$ | $\searrow$ | $\searrow$ | $(0)$ |

  \end{table}

  したがって$g(\theta)$は$\theta = \theta_0$で最大である．
  この時$\sin\theta_0 = \sqrt{1 - \left(\frac{1-\sqrt{3}}{2}\right)^2} = \frac{\sqrt{3}}{2}$だから
  
$$
\begin{align*}
g(\theta_0)
     & = \frac{\frac{\sqrt{3}}{2}(1-1+\sqrt{3})}{1-\frac{1-\sqrt{3}}{2}}\\& = \frac{2\sqrt{3}\frac{\sqrt{3}}{2}}{1+\sqrt{3}}\\& = 2^{-\frac{1}{2}}\cdot 3^{\frac{3}{4}}(3^{\frac{1}{2}}-1)
\end{align*}
$$

  である．

  よってSのとりうる領域は[図3](#1991-3:fig:3)の斜線部である(境界は実線部含む．白点は含まず．)．
  
$$
\begin{align*}
0 < S \le 2^{-\frac{1}{2}}\cdot 3^{\frac{3}{4}}\left(3^{\frac{1}{2}}-1\right)
\end{align*}
$$

  が求める$S$の範囲である．$\cdots$(答)

  

<figure id="1991-3:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1991/3/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $S$のとりうる領域</figcaption>
</figure>

  

  

## 【解説】