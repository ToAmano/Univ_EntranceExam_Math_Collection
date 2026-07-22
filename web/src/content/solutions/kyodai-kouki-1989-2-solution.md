---
university: "kyodai"
category: "kouki"
year: "1989"
question: "2"
type: "solution"
title: "KYODAI 1989 kouki Q2 (solution)"
---

## 【解】

  立体を $xy$平面で切断すると ($r>1/2$に注意) と
  対称性より図は[図1](#1989-2:fig:1)のようになる．$\star$

  

<figure id="1989-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1989/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $xy$平面での図形の切断面．題意の立体の領域を斜線で塗りつぶしている．</figcaption>
</figure>

  放物線と円の二接点を，正のパラメータ$t>0$を用いてP$(-t,t^2)$,Q$(t,t^2)$とおく．
  球の中心を$O'(0,Y)$ とおくと点Qが接点である条件は，
  $\vec{l}=(1,2t)$を点Qでの $y=x^2$の接線ベクトルとして
  

$$
\begin{align}
& \begin{dcases}
         \vec{O'Q}^2=r^2 \\
         \vec{O'Q} \perp \vec{l}
       \end{dcases}\\\therefore& \begin{dcases}
         t^2 + (t^2-Y)^2 = r^2 & \quad \dots \textcircled{1} \\
         \begin{pmatrix}t                                             \\ t^2-Y\end{pmatrix} \cdot \begin{pmatrix}1 \\ 2t\end{pmatrix} = 0 & \quad \dots \textcircled{2}
       \end{dcases}\\\therefore& \begin{dcases}
         t^2 + (t^2-Y)^2 = r^2                   \\
         1 + 2(t^2-Y) = 0 & \quad (\because t>0)
       \end{dcases}\\\therefore& \begin{dcases}
         t^2 + \frac{1}{4} = r^2 \\
         t^2-Y = -\frac{1}{2}
       \end{dcases}\label{1989-2:eq:1}\\\therefore& \begin{dcases}
         t = \sqrt{r^2-\frac{1}{4}} & \quad (\because t>0) \\
         Y = r^2+\frac{1}{4}
       \end{dcases}
\end{align}
$$

  となる．

  以下，回転体の体積を求める．
  求める体積は図の斜線部の領域を$y$軸周りに回転させた立体の体積 $V$ に等しい．
  これは二つの部分に分割して考えることができて
  

$$
\begin{align}
V = & (\text{放物線} POQ \text{を} y \text{軸回りに回転した体積 } V_1)                           \\& - (\text{円弧} PQ \text{を} y \text{軸回りに回転した体積 }\quad V_2) \label{1989-2:eq:2}
\end{align}
$$

  となる．以下$V_1,V_2$を別個に求める．

  まず$V_1$にはバームクーヘン積分法を用いると
  

$$
\begin{align*}
V_1
     & = \int_0^t 2\pi x \cdot x^2 dx       \\& = \frac{1}{2}\pi t^4                 \\& = \frac{1}{2}\pi(r^2-\frac{1}{4})^2
\end{align*}
$$

  である．

  次に$V_2$は[(式1)](#1989-2:eq:1)から，図のように円$x^2+y^2=r^2$の$1/2\le x\le r$の部分を回転させた体積に等しい．

  

<figure id="1989-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1989/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 求める回転体の部分</figcaption>
</figure>

  従って
  

$$
\begin{align*}
V_2
     & = \int_{\frac{1}{2}}^r \pi(r^2-x^2) dx                             \\& = \pi\left[ r^2x - \frac{1}{3}x^3 \right]_{\frac{1}{2}}^r          \\& = \pi\left(\frac{2}{3}r^3 - \frac{1}{2}r^2 + \frac{1}{24}\right)
\end{align*}
$$

  となる．

  以上$V_1$と$V_2$の表現を[(式2)](#1989-2:eq:2)に代入して
  

$$
\begin{align*}
V
     & = \pi\left[\frac{1}{2}\left(r^2-\frac{1}{4}\right)^2 - \left(\frac{2}{3}r^3 - \frac{1}{2}r^2 + \frac{1}{24}\right)\right]\\& = \pi\left[\frac{1}{2}r^4 - \frac{1}{4}r^2 + \frac{1}{32} - \frac{2}{3}r^3 + \frac{1}{2}r^2 - \frac{1}{24}\right]\\& = \pi\left[\frac{1}{2}r^4 - \frac{2}{3}r^3 + \frac{1}{4}r^2 - \frac{1}{96}\right]
\end{align*}
$$

  が求める面積である．$\cdots$(答)

  
  

## 【解説】

  球について時間\underline{に}余裕があれば，$x^2+(y-r)^2=r^2$が \\
  が不適切ということは言った方がよいかもしれない．すぐ言えるし