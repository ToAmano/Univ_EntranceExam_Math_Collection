---
university: "kyodai"
category: "kouki"
year: "1991"
question: "2"
type: "solution"
title: "KYODAI 1991 kouki Q2 (solution)"
---

## 【解】

    (1)
    四面体の頂点をP，Q，R，Sとする．
    各辺の中点を図のようにA，B，C，D，E，Fとする．

    

<figure id="1991-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1991/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 正四面体PQRSと正八面体ABCDEFの様子．</figcaption>
</figure>

    正八面体の高さHは四面体の高さの$1/2$であるから，四面体の高さを求めよう．
    四面体の底面QRSの重心Gとすると，四面体の高さは線分PGの長さに等しいから
    

$$
\begin{align}
h_0 = \frac{1}{2}PG \label{1991-2:eq:1}
\end{align}
$$

    である．

    

<figure id="1991-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1991/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 底面QRSとその重心Gの様子．QGの長さはQEと$\angle GQE$から求まる．</figcaption>
</figure>

    

<figure id="1991-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1991/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 断面PQG(F)の様子</figcaption>
</figure>

    四面体の底面QRSは正三角形であるから，QGの長さは（[図2](#1991-2:fig:2)）
    

$$
\begin{align*}
|QG|
         & = \frac{|QE|}{\cos \frac{\pi}{6}}\\& = \frac{2}{\sqrt{3}}
\end{align*}
$$

    である．

    $\triangle PQG$ にピタゴラスの定理を用いて
    

$$
\begin{align}
& |PQ|^2 = |PG|^2 + |QG|^2                         \\& 2^2 = |PG|^2 + \left(\frac{2}{\sqrt{3}}\right)^2 \\\therefore& |PQ| = \frac{2\sqrt{6}}{3}\label{1991-2:eq:3}
\end{align}
$$

    でる．
    これを[(式1)](#1991-2:eq:1)に代入して，求めるHの高さは
    

$$
\begin{align*}
h_0 = \frac{\sqrt{6}}{3}
\end{align*}
$$

    である．$\cdots$(答)

    
    (2)
    水面の高さ$h$の時の水面積$S(h)\,\mathrm{cm^2}$とすると，題意の条件より
    

$$
\begin{align}
1 = S(h) \frac{dh}{dt}\label{1991-2:eq:2}
\end{align}
$$

    が成り立つ．

    

<figure id="1991-2:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1991/2/fig_4.svg" alt="図 4" />
  <figcaption>図 4: 高さ$h$でのHの切り口．外側の正三角形の頂点は，辺PQ，PR，PS上にとる．</figcaption>
</figure>

    

<figure id="1991-2:fig:5">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1991/2/fig_5.svg" alt="図 5" />
  <figcaption>図 5: 面PQRを例に，底面からの高さ$h$での切断面での各種長さを求める．
            赤の点線が底面からの高さ$h$の線とする．</figcaption>
</figure>

    また，底面からの高さ$h$における正八角体Hの切り口は[図4](#1991-2:fig:4)のような六角形である．

    ここで，六角形の外側の正三角形の一辺の長さ$s$は，一辺$2$の正三角形QRSとの相似比が
    

$$
\begin{align*}
|PG|:|PG|-h
\end{align*}
$$

    だから，[(式3)](#1991-2:eq:3)を代入して
    

$$
\begin{align*}
\frac{2\sqrt{6}}{3} : \frac{2\sqrt{6}}{3} -h
\end{align*}
$$

    となり，
    

$$
\begin{align*}
s
         & = 2\cdot\frac{\frac{2\sqrt{6}}{3} -h}{\frac{2\sqrt{6}}{3}}\\& = 2 - \frac{\sqrt{6}h}{2}
\end{align*}
$$

    である．

    切り取る部分の正三角形の一辺の長さ$t$は，一辺$1$の正三角形DFSとの相似比が
    

$$
\begin{align*}
\frac{1}{2}|PG| : \frac{1}{2}|PG| - h
\end{align*}
$$

    だから，[(式3)](#1991-2:eq:3)を代入して
    

$$
\begin{align*}
\frac{\sqrt{6}}{3} : \frac{\sqrt{6}}{3} -h
\end{align*}
$$

    となり，
    

$$
\begin{align*}
t
         & = 1\cdot\frac{\frac{\sqrt{6}}{3} -h}{\frac{\sqrt{6}}{3}}\\& = 1 - \frac{\sqrt{6}h}{2}
\end{align*}
$$

    である．

    従って，この面積$S(h)$は一辺$2-\sqrt{6}h/2$の正三角形の面積から，3つの一辺$1-\sqrt{6}h/2$の正三角形の面積を引いたものに等しい．
    

$$
\begin{align*}
S
         & = \frac{1}{2}\frac{\sqrt{3}}{2}\left(2-\frac{\sqrt{6}}{2}h\right)^2 - 3\frac{1}{2}\frac{\sqrt{3}}{2}\left(1-\frac{\sqrt{6}}{2}h\right)^2 \\& = \frac{\sqrt{3}}{4}\left[\left(4+\frac{3h^2}{2}-2\sqrt{6}h\right) -3 \left(1-\sqrt{6}h+\frac{3h^2}{2}\right)\right]\\& = \frac{\sqrt{3}}{4}\left[ -3h^2 + \sqrt{6}h + 1 \right]
\end{align*}
$$

    だから，微分方程式[(式2)](#1991-2:eq:2)に代入して整理すると，
    

$$
\begin{align*}
dt & = \frac{\sqrt{3}}{4}[-3h^2 + \sqrt{6}h+1 ] dh
\end{align*}
$$

    となる．両辺積分すると，積分定数$C$として
    

$$
\begin{align*}
t = \frac{\sqrt{3}}{4}(-h^3 + \frac{\sqrt{6}}{2}h^2+h) + C
\end{align*}
$$

    である．初期条件は$t=0$で$h=0$だから積分定数は$C=0$であり，
    高さが$h$になるまでに要する時間は
    

$$
\begin{align*}
t = \frac{\sqrt{3}}{4}\left(-h^3 + \frac{\sqrt{6}}{2}h^2+h\right)
\end{align*}
$$

    である．$\cdots$(答)

    
    

## 【解説】