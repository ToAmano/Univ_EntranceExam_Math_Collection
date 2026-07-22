---
university: "todai"
category: "kouki"
year: "2004"
question: "3"
type: "solution"
title: "TODAI 2004 kouki Q3 (solution)"
---

## 【解】

  (1)
  

<figure id="2004-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2004/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円$A,B$と接線$m,l$の様子</figcaption>
</figure>

  $m \perp l$ および$l$が$(-1+\cos\theta,\sin\theta)$での接点であることから，$m$はB上の点 $(1+\cos(\theta+\frac{\pi}{2}), \sin(\theta+\frac{\pi}{2}))$、又は $(1+\cos(\theta-\frac{\pi}{2}), \sin(\theta-\frac{\pi}{2}))$ での接線である．
  これら二つの接線を順に$m_{+}, m_{-}$とすると
  

$$
\begin{align}
& \begin{dcases}
         m_{+}  : \cos(\theta+\frac{\pi}{2})(x-1) + \sin(\theta+\frac{\pi}{2})y = 1 \\
         m_{-}  : \cos(\theta-\frac{\pi}{2})(x-1) + \sin(\theta-\frac{\pi}{2})y = 1
       \end{dcases}\\& \begin{dcases}
         m_{+} : -\sin\theta (x-1) + \cos\theta y = 1 \\
         m_{-} : \sin\theta(x-1) - \cos\theta y = 1
       \end{dcases}\\& m_{\pm}: \sin\theta(x-1) - \cos\theta y \pm 1 = 0 \label{2004-3:eq:1}
\end{align}
$$

  と求まる．

  これらの接線と$l$の交点は，二つの方程式を連立して求めることができる．
  $l$の方程式は
  

$$
\begin{align}
l: \cos\theta(x+1) + \sin\theta y = 1 \label{2004-3:eq:2}
\end{align}
$$

  だから，[(式1)](#2004-3:eq:1)と連立して$y$を消去すると
  

$$
\begin{align}
& \sin^2\theta(x-1) - \cos\theta\left(1-\cos\theta(x+1)\right)\pm\sin\theta = 0                       \\& \left(\sin^2\theta + \cos^2\theta\right) x -\sin^2\theta + \cos^2\theta -\cos\theta\pm\sin\theta = 0 \\& x = \sin^2\theta - \cos^2\theta + \cos\theta\mp\sin\theta\label{2004-3:eq:3}
\end{align}
$$

  だから，対応して$y$座標は$l$の方程式に代入すると
  

$$
\begin{align*}
& \cos\theta(\sin^2\theta - \cos^2\theta + \cos\theta\mp\sin\theta+1) + \sin\theta y = 1 \\& \cos\theta(2\sin^2\theta + \cos\theta\mp\sin\theta) + \sin\theta y = 1                 \\& 2\cos\theta\sin^2\theta + \cos^2\theta\mp\sin\theta\cos\theta + \sin\theta y = 1      \\& 2\cos\theta\sin^2\theta - \sin^2\theta\mp\sin\theta\cos\theta + \sin\theta y = 0
\end{align*}
$$

  まず$\sin\theta \neq 0$の場合を考えると，両辺$\sin\theta$で割って
  

$$
\begin{align}
& 2\cos\theta\sin\theta - \sin\theta\mp\cos\theta +  y = 0                  \\& y = - 2\cos\theta\sin\theta + \sin\theta\pm\cos\theta\label{2004-3:eq:4}
\end{align}
$$

  である．
  ついで$\sin\theta = 0$の場合，[(式3)](#2004-3:eq:3)に代入して$x = 0,-2$であり，この時[(式2)](#2004-3:eq:1,2004-3:eq:2)から$y=\pm 1$である．
  よってこの場合も[(式4)](#2004-3:eq:4)の表現で良い．

  以上より求める$l$と$m$の交点は
  

$$
\begin{align*}
\begin{dcases}
      m_{+} \text{と} l & : (\sin^2\theta-\cos^2\theta+\cos\theta - \sin\theta, -(2\cos\theta-1)\sin\theta+\cos\theta) \\
      m_{-} \text{と} l & : (\sin^2\theta-\cos^2\theta+\cos\theta + \sin\theta, -(2\cos\theta-1)\sin\theta-\cos\theta)
    \end{dcases}
\end{align*}
$$

  である．
  $\cdots$(答)

  

  (2)
  $m_1$と$l$の交点を$P(X,Y)$とする．
  題意のうち $x \ge 0,  y \ge 0$の部分は$y$軸，$B$およびPの軌跡で囲まれた部分である．
  この体積を$V_1$としてもとめる体積$V$は$x$軸に関する対称性から
  

$$
\begin{align}
V = 4V_1 + 2\pi\label{2004-3:eq:5}
\end{align}
$$

  である．ただし最後の$2\pi$はDおよびEの面積である．

  (1)の結果から$X,Y$は$\theta$を用いて
  

$$
\begin{align}
\begin{dcases}
      X = \sin^2\theta - \cos^2\theta - (\sin\theta-\cos\theta) \\
      Y = (\sin\theta+\cos\theta) - 2\sin\theta\cos\theta
    \end{dcases}\label{2004-3:eq:6}
\end{align}
$$

  と表せ，一階微分は
  

$$
\begin{align}
\frac{dX}{d\theta}& = 4\sin\theta\cos\theta - (\cos\theta+\sin\theta)                     \\& = 2t^2 - t - 2. \quad(t=\cos\theta+\sin\theta)   \label{2004-3:eq:7}\\\frac{dY}{d\theta}& = (\cos\theta-\sin\theta) - 2(\cos^2\theta-\sin^2\theta)              \\& = (\cos\theta-\sin\theta)(1-2t) \label{2004-3:eq:8}
\end{align}
$$

  となる．

  また，考えるべき$\theta$の範囲について考える．まず$0 \le \theta \le \frac{\pi}{2}$である．
  $P$がB上の点になる時，$l$がBの中心$(1,0)$を通るから[(式2)](#2004-3:eq:2)に$(1,0)$を代入して
  

$$
\begin{align*}
& 2 \cos\theta = 1       \\& \theta = \frac{\pi}{3}
\end{align*}
$$

  である．

  次に$P$が$y$軸上にある時つまり$X=0$の時，[(式6)](#2004-3:eq:6)より
  $\theta=\frac{\pi}{4}$である．

  以上から
  

$$
\begin{align*}
\frac{\pi}{4}\le\theta\le\frac{\pi}{3}
\end{align*}
$$

  の範囲で考えれば良い．

  

<figure id="2004-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2004/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 円$A,B$と接線$m,l$の様子．$\theta=\frac{\pi}{3}$のときで，この時$P$が円$B$軸上に存在する．</figcaption>
</figure>

  

<figure id="2004-3:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2004/3/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 円$A,B$と接線$m,l$の様子．$\theta=\frac{\pi}{4}$のときで，この時$P$が$y$軸上に存在する．</figcaption>
</figure>

  [(式7)](#2004-3:eq:6,2004-3:eq:7)より，この範囲で$dX/d\theta, dY/d\theta \ge 0$であるから
  $(X,Y)$の増減表は[表1](#2004-3:table:1)となる．

  

<figure id="2004-3:table:1" class="table-wrapper">

| $\theta$ | $\pi/4$ |  | $\pi/3$ |
|:--:|:--:|:--:|:--:|
| $X'$ | $+$ | $+$ | $+$ |
| $Y'$ | $+$ | $+$ | $+$ |
| $(X,Y)$ | $(0, \sqrt{2}-1)$ | $\nearrow$ | $\left(\frac{2-\sqrt{3}}{2}, \frac{1}{2}\right)$ |

  <figcaption>表 1: $P(X,Y)$の増減表</figcaption>
</figure>

  したがって、$P$の軌跡の概形は[図4](#2004-3:fig:4)のようになる．

  

<figure id="2004-3:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2004/3/fig_4.svg" alt="図 4" />
  <figcaption>図 4: 求める領域のうち第一章限にある部分$(V_1)$は斜線部．</figcaption>
</figure>

  斜線部の面積が$V_1$である．図から
  

$$
\begin{align}
V_1 = \text{図形}OFG + \triangle IGH - \text{扇形}IGO \label{2004-3:eq:9}
\end{align}
$$

  となるから，各項計算していく．

  まず第一項目は
  

$$
\begin{align}
& \text{図形}OFG                                                                                                                                                               \\& = \int_{\pi/4}^{\pi/3} Y \frac{dX}{d\theta} d\theta\\& = \int_{\pi/4}^{\pi/3}\left(\sin\theta+\cos\theta-2\sin\theta\cos\theta\right)\{4\sin\theta\cos\theta-(\cos\theta+\sin\theta)\} d\theta\\& = \int_{\pi/4}^{\pi/3}\left[-(\sin\theta+\cos\theta)^2 + 6\sin\theta\cos\theta(\sin\theta+\cos\theta) - 8\sin^2\theta\cos^2\theta\right] d\theta\\& = \int_{\pi/4}^{\pi/3}\left[ 6(\sin\theta\cos^2\theta+\cos\theta\sin^2\theta) - 2\sin\theta\cos\theta -8\sin^2\theta\cos^2\theta - 1 \right] d\theta\label{2004-3:eq:10}
\end{align}
$$

  と展開できるから，各項計算して
  

$$
\begin{align*}
\int_{\pi/4}^{\pi/3} 6(\sin\theta\cos^2\theta+\cos\theta\sin^2\theta) d\theta& = 6 \left[-\frac{1}{3}\cos^3\theta+\frac{1}{3}\sin^3\theta\right]_{\pi/4}^{\pi/3}\\& = 2\left(\frac{3\sqrt{3}}{8}-\frac{1}{8}\right)\\& = \frac{3\sqrt{3}-1}{4}\\\int_{\pi/4}^{\pi/3} 2\sin\theta\cos\theta d\theta& = -\frac{1}{2}[\cos 2\theta]_{\pi/4}^{\pi/3}\\& = \frac{1}{4}\\\int_{\pi/4}^{\pi/3} 8\sin^2\theta\cos^2\theta d\theta& = \int_{\pi/4}^{\pi/3} 2\sin^2 2\theta d\theta\\& = \left[\theta - \frac{1}{4}\sin 4\theta\right]_{\pi/4}^{\pi/3}\\& = \frac{\pi}{12} + \frac{\sqrt{3}}{8}\\\int_{\pi/4}^{\pi/3} d\theta& = \frac{\pi}{12}
\end{align*}
$$

  を[(式10)](#2004-3:eq:10)に代入して
  

$$
\begin{align}
\text{図形}OFG
     & = \frac{3\sqrt{3}-1}{4} - \frac{1}{4} - \frac{\pi}{12} - \frac{\sqrt{3}}{8} - \frac{\pi}{12}\\& = \frac{5}{8}\sqrt{3} - \frac{1}{2} - \frac{\pi}{6}\label{2004-3:eq:11}
\end{align}
$$

  を得る．

  次に[(式9)](#2004-3:eq:9)の第二，第三項について
  

$$
\begin{align}
\triangle IGH - \text{扇形}IGO
     & = \frac{1}{2}\frac{\pi}{6} - \frac{1}{2}\cdot\frac{1}{2}\cdot\frac{\sqrt{3}}{2}\\& = \frac{\pi}{12} - \frac{\sqrt{3}}{8}\label{2004-3:eq:12}
\end{align}
$$

  を得る．

  [(式12)](#2004-3:eq:11,2004-3:eq:12)を[(式9)](#2004-3:eq:9)に代入して
  

$$
\begin{align*}
V_1 = \frac{3}{4}\sqrt{3} - \frac{1}{2} - \frac{1}{4}\pi
\end{align*}
$$

  だから，[(式5)](#2004-3:eq:5)に代入して求める面積$V$は
  

$$
\begin{align*}
V
     &
    = 3\sqrt{3}-2-\pi+2\pi\\& = 3\sqrt{3}+\pi-2
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】

  非通過領域についての論述を解答ではさらっとで済ませた．
  後段の積分計算がそこそこ重いので前段はこれくらいで良いかとは思うが，
  一応ある程度厳密にやろうとすれば，以下のような議論をすれば良いだろう．

  \begin{itemize}
    \item 対称性から第1象限で考える。右図の部分のみかんがえれば良い。
    \item Pのキセキは[解]での考察から右下図のようになる。
          

1.  ①の部分は正方形を、Aで接するようにした状態から平行移動して通過しうる。

2.  ②の部分も同様

3.  ③の部分は、右下図で P, P' ($x$座標が同じ)に対し、A,Bへ接線を引き S, S', T, T'を定めると、
                  \[ \angle S'P'T' < \angle SPT = \pi/2 \]
                  となるので、P'は通りえない。

    \item 又、正方形の一辺が2であることとあわせて、[解]の部分が非通過領域である。
  \end{itemize}