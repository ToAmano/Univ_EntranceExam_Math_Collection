---
university: "utokyo"
category: "kouki"
year: "1996"
question: "3"
type: "solution"
title: "UTOKYO 1996 kouki Q3 (solution)"
---

## 【解】

  

<figure id="1996-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1996/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: タンクの様子</figcaption>
</figure>

  タンクの半径$R$, 長さ$L$, 流出開始を$t=0$として、
  時刻$t$における水面の高さ$h$,
  水面の面積$S$, 流出速度$v$とする。
  題意から $v$ は 比例
  定数$k$として
  

$$
\begin{align}
v = k\sqrt{h}\label{1996-3:eq:1}
\end{align}
$$

  とおける．

  一方流出する水に関して
  

$$
\begin{align}
v = -S \frac{dh}{dt}\label{1996-3:eq:2}
\end{align}
$$

  が成り立つ．

  

<figure id="1996-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1996/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 高さ$h$での円の切断線</figcaption>
</figure>

  さらに，タンクの高さ$h$での切断面は奥行き$L$，幅
  

$$
\begin{align*}
2\sqrt{R^2-(h-R)^2} = 2\sqrt{2Rh-h^2}
\end{align*}
$$

  の長方形だから
  

$$
\begin{align}
S = 2L\sqrt{2Rh - h^2}\label{1996-3:eq:3}
\end{align}
$$

  である．

  [(式3)](#1996-3:eq:1,1996-3:eq:3)を[(式2)](#1996-3:eq:2)に代入して
  

$$
\begin{align*}
k\sqrt{h} = -2L\sqrt{2Rh - h^2}\frac{dh}{dt}
\end{align*}
$$

  という微分方程式を得る．

  両辺$\sqrt{h}$で割って整理して
  

$$
\begin{align*}
k\,dt = -2L \sqrt{2R-h}\,dh
\end{align*}
$$

  だから，積分して
  

$$
\begin{align*}
-\frac{k}{2L} t = -\frac{2}{3}(2R-h)^{\frac{3}{2}} + C
\end{align*}
$$

  ただし、$C$は初期条件による定数である．

  初期条件は $t=0$ で $h=2R$ だから，$C=0$ が従う．
  

$$
\begin{align*}
-\frac{k}{2L} t = -\frac{2}{3}(2R-h)^{\frac{3}{2}}
\end{align*}
$$

  さらに題意の条件より$t=1\text{[h]}$で$h=R$だから
  

$$
\begin{align*}
\frac{k}{2L} = -\frac{2}{3} R^{\frac{3}{2}}\quad\cdots ⑤
\end{align*}
$$

  であるから
  

$$
\begin{align*}
& -\frac{2}{3} R^{\frac{3}{2}} t = -\frac{2}{3}(2R-h)^{\frac{3}{2}}\\\therefore& t = \left(2-\frac{h}{R}\right)^{\frac{3}{2}}
\end{align*}
$$

  $h=0$ になる時の $t=t_0$ をもとめるため
  $h=0$を代入すると
  

$$
\begin{align*}
t_0 = 2^{\frac{3}{2}} = 2\sqrt{2}
\end{align*}
$$

  である．

  よって，現在$t=1$から$h=0$になるまでの時間$T$は
  

$$
\begin{align}
T
     & = t_0 -1                            \\& = 2\sqrt{2} -1  \label{1996-3:eq:4}
\end{align}
$$

  である．

  ここで
  

$$
\begin{align*}
& (1.414)^2 = 1.999396 < 2\,(1.415)^2 = 2.002225 > 2 \\\therefore& 1.414 < \sqrt{2} < 1.415
\end{align*}
$$

  だから，[(式4)](#1996-3:eq:4)に代入して
  

$$
\begin{align*}
& 1.828 < T_0 < 1.83                                         \\\therefore& 1\text{時間}\,49.68\text{分} < T_o < 1\text{時間}\,49.8\text{分}
\end{align*}
$$

  である．従って，1分以下を切り捨てて
  

$$
\begin{align*}
T_0 = 1\text{時間}\,49\text{分}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】