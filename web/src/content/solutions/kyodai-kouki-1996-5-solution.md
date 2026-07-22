---
university: "kyodai"
category: "kouki"
year: "1996"
question: "5"
type: "solution"
title: "KYODAI 1996 kouki Q5 (solution)"
---

## 【解】

  （1）

  

<figure id="1996-5:fig:0">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1996/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形PQRの様子</figcaption>
</figure>

  直線 PQ と原点の距離 $r$ とおく．
  辺 PQの長さが$2a$だから，辺 PQが単位円の中を動く時
  
$$
\begin{align}
0 \le r \le\sqrt{1-a^2}\label{1996-5:eq:1}
\end{align}
$$

  である．

  

<figure id="1996-5:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1996/5/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 辺$PQ$が$y$軸に平行な場合のイメージ図．$r$は\cref{1996-5:eq:1}の範囲で動く．</figcaption>
</figure>

  また，点$R$の$z$座標は$\sqrt{3}$である．

  求める領域は$z$軸を中心に軸対称だから，
  辺 PQ が$y$軸に平行な場合を考えて，
  その領域を $z$ 軸まわりに回転した立体の体積を考えれば良い．
  $r$を固定して三角形PQRをこの条件で動かすと，
  三角形PQRの動く領域は[図3](#1996-5:fig:2)のような底辺$2\sqrt{1-r^2}$，
  上辺$\sqrt{1-r^2}-2a$，高さ$\sqrt{3}a$の台形になる．

  

<figure id="1996-5:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1996/5/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 辺$PQ$が$y$軸に平行な場合のイメージ図．$r$は\cref{1996-5:eq:1}の範囲で動く．</figcaption>
</figure>

  従って，この立体を$z=k\, (0 \le k \le \sqrt{3}a) $で切断した切り口は[図4](#1996-5:fig:3)の線分BCである．
  この図で正三角形ABCの垂線の長さは$\sqrt{3(1-r^2)}-k$だから，
  
$$
\begin{align*}
|BC| = \frac{2}{\sqrt{3}}\left(\sqrt{3(1-r^2)}-k\right)
\end{align*}
$$

  となる．従ってこれは
  
$$
\begin{align}
-\frac{\sqrt{3(1-r^2)}-k}{\sqrt{3}}\le y \le\frac{\sqrt{3(1-r^2)}-k}{\sqrt{3}}\label{1996-5:eq:2}
\end{align}
$$

  となり，$x=r$を動かして$z=k$平面に図示すると[図5](#1996-5:fig:4)のようになる．

  

<figure id="1996-5:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1996/5/fig_4.svg" alt="図 4" />
  <figcaption>図 4: 台形の$z=k$での切断面は線分BCである．正三角形ABCの垂線の長さから，BCの長さが求まる．</figcaption>
</figure>

  

<figure id="1996-5:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1996/5/fig_5.svg" alt="図 5" />
  <figcaption>図 5: $z=k$での切断面の様子．これをz軸周りに一回転したものが求める図形の断面に等しい．
      計算すると，$r(k)$を半径とする円になる．</figcaption>
</figure>

  従ってこれを$z$軸周りに一回転させたものが求める立体の$z=k$での切り口である．
  境界の曲線$\eqref{1996-5:eq:2}$上の点$(X,Y)$とすると，原点からの距離の二乗は
  
$$
\begin{align*}
X^2+Y^2
     & = X^2 + \frac{1}{3}\left(\sqrt{3(1-X^2)}-k\right)^2          \\& = X^2 + (1-X^2) -\frac{2k}{3}\sqrt{3(1-X^2)} + \frac{k^2}{3}\\& = 1 -\frac{2k}{3}\sqrt{3(1-X^2)} + \frac{k^2}{3}
\end{align*}
$$

  でこれは$X$の単調増加関数だから，$X=\sqrt{1-a^2}$で最大値
  
$$
\begin{align*}
r(k)                                                  \\& = \max(X^2+Y^2)
     & =  (1-a^2) + \frac{1}{3}\left(\sqrt{3}a-k\right)^2
\end{align*}
$$

  をとる．
  従って回転した領域は半径$r(k)$の円だから，
  この面積$S(k)$として，
  
$$
\begin{align*}
S(k)
     & = \pi r^2(k)                                                          \\& = \pi\left((1-a^2) + \frac{1}{3}\left(\sqrt{3}a-k\right)^2 \right)
\end{align*}
$$

  だから，求める体積$V$はこれを$0\le z\le \sqrt{3}a$で積分したもので
  
$$
\begin{align*}
V
     & = \int_0^{\sqrt{3}a} S(k) dk                                                         \\& = \pi\left[(1-a^2)k + \frac{1}{9}\left(k-\sqrt{3}a\right)^3 \right]_0^{\sqrt{3}a}\\& = \pi\left[\sqrt{3}a(1-a^2) + \frac{\sqrt{3}}{3}a^3 \right]\\& = \frac{\sqrt{3}\pi}{3}(3a-2a^3)
\end{align*}
$$

  が求める体積である．$\cdots$(答)

### (2)
 $\frac{dV}{da}\frac{1}{\pi} = \sqrt{3} (1 - 2a^2)$ から下表を得る
  

| $a$  | $0$ |  $\dots$   | $\frac{1}{\sqrt{2}}$ |  $\dots$   | $1$ |
|:------:|:-----:|:------------:|:----------------------:|:------------:|:-----:|
| $V'$ |       |    $+$     |         $0$          |    $-$     |       |
| $V$  |       | $\nearrow$ |                        | $\searrow$ |       |

  従って V は $a=\frac{1}{\sqrt{2}}$ の時，max $\frac{1}{3}\sqrt{6}\pi$ をとる．

  
  

## 【解説】

  解答ではかなり丁寧に$z=k$での断面図を求めたが，
  対称性からPQの中点が$x$軸にある場合だけを考えれば良いので，
  実践的にはそれで十分だと思われる．