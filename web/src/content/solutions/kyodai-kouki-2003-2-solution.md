---
university: "kyodai"
category: "kouki"
year: "2003"
question: "2"
type: "solution"
title: "KYODAI 2003 kouki Q2 (solution)"
---

## 【解】

  三角形ABCにおいて
  
$$
\begin{align}
& \angle ADB = \theta& \left(\frac{\pi}{3} < \theta < \frac{\pi}{2}\right)\label{2003-2:eq:1}
\end{align}
$$

  とおく．
  C から直線 BD に下ろした垂線 H とおく．

  

<figure id="2003-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2003/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形ABCと点D, Hの様子</figcaption>
</figure>

  四面体 $ABCD$ の体積が最大の時
  の $\triangle ABD$ を底面とみた時の高さは $CH$ である．

  従って，四面体ABCDは底面が三角形ABD，高さCHの錐体で，
  その体積$V(\theta)$は，
  
$$
\begin{align*}
V(\theta)
     & = \frac{1}{3}(\triangle ABD) |CH|          \\& = \frac{1}{6}|CH||AD||AB|\sin\frac{\pi}{3}\\& = \frac{\sqrt{3}}{12}|CH||AD||AB|
\end{align*}
$$

  である．

  以下CH,AD,ABの長さを計算する．
  まず，題意より三角形ABCは一辺の長さ$1$だから
  
$$
\begin{align*}
|AB| = 1
\end{align*}
$$

  である．

  次にBDは，三角形ABDに正弦定理を用いて
  
$$
\begin{align*}
AD = \frac{\sin(\pi-\theta)}{\sin\theta}
\end{align*}
$$

  である．

  最後にCH については，三角形BCHを考えて
  
$$
\begin{align*}
CH
     & = |BC|\sin\angle HBC  \\& = \sin(\theta - \pi/3)
\end{align*}
$$

  である．

  以上から，四面体 $ABCD$ の体積 $V(\theta)$ は
  
$$
\begin{align*}
V(\theta)
     & = \frac{\sqrt{3}}{12}|CH||AD||AB|                                                      \\& = \frac{\sqrt{3}}{12}\frac{\sin(\pi-\theta)}{\sin\theta}\sin(\theta - \frac{\pi}{3}) \\
\end{align*}
$$

  である．
  積和公式を用いてさらに変形して
  
$$
\begin{align*}
V(\theta)
     & = \frac{\sqrt{3}}{12}\frac{-1}{2}\frac{\cos\frac{\pi}{3}-\cos(\pi-2\theta)}{\sin\theta}\\& = \frac{-\sqrt{3}}{24}\frac{\frac{1}{2}+\cos 2\theta}{\sin\theta}\\
\end{align*}
$$

  さらに倍角公式から$\cos 2\theta = 1-2\sin^2\theta$だから，全体を$\sin\theta$だけでかけて
  
$$
\begin{align*}
V(\theta)
     & = -\frac{\sqrt{3}}{48}\frac{1+2(1-2\sin^2\theta)}{\sin\theta}\\& = -\frac{\sqrt{3}}{48}\frac{3-4\sin^2\theta}{\sin\theta}\\& = \frac{\sqrt{3}}{48}\left(4\sin\theta - \frac{3}{\sin\theta}\right)\\
\end{align*}
$$

  となる．
  ここで，$\eqref{2003-2:eq:1}$から，区間内で$\frac{\sqrt{3}}{2}<\sin\theta\le 1$であり，
  この区間で$\sin\theta$も$-1/\sin\theta$も$\sin\theta$に関する単調増加関数だから，
  $V(\theta)$は$\sin\theta$ の単調増加関数で，$\sin\theta=1$ すなわち $\theta=\pi/2$
  の時に最大値を取る．
  この時$D$ が $AC$ の中点の時となる．
  求める最大値は
  
$$
\begin{align*}
\max V
     & = V(\pi/2)            \\& = \frac{\sqrt{3}}{48}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】