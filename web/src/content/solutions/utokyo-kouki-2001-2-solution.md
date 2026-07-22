---
university: "utokyo"
category: "kouki"
year: "2001"
question: "2"
type: "solution"
title: "UTOKYO 2001 kouki Q2 (solution)"
---

## 【解】

  (1)

  

<figure id="2001-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 座標系と格子</figcaption>
</figure>

  [図1](#2001-2:fig:1)のように座標を定めて円の中心を$P(X,Y)$とおく．
  ここで格子の方程式が
  

$$
\begin{align*}
& x=kh, y=kh & (k \in\mathbb{Z})
\end{align*}
$$

  となっている．

  格子の間隔が$x,y$軸方向に等しいことから，円が2直線とのみ交わるときx軸平行及びy軸平行と1本ずつ交わる．
  また，$h<1$の時は必ず3本以上の直線と交わるため以下
  

$$
\begin{align}
1 \le h \label{2001-2:eq:0}
\end{align}
$$

  として考える．

  

<figure id="2001-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 考える領域$D_{0,0}$の様子</figcaption>
</figure>

  格子は$k, l \in \mathbb{Z}$ として
  

$$
\begin{align}
D_{k,l} =
    \begin{dcases}
      (k-\frac{1}{2})h \le x \le (k+\frac{1}{2})h \\
      (l-\frac{1}{2})h \le y \le (l+\frac{1}{2})h
    \end{dcases}\label{2001-2:eq:1}
\end{align}
$$

  なる領域（いずれも合同）の集合とみなせるから，このうちの一つ $D_{0,0}$ 中に円の中心$P(X,Y)$がある時のみを考えれば良い．
  この時円が$x=0, y=0$ の２本の格子と交わり，$x=\pm h, y=\pm h$ の格子と交わらなければ良い．
  このようなX,Yの条件は，円の半径が$1$だから，
  

$$
\begin{align}
& \begin{dcases}
         -h < X-1 \le 0 \le X+1 < h \\
         -h < Y-1 \le 0 \le Y+1 < h
       \end{dcases}\\\therefore& 1-h < X,Y < 1+h \land
    -1 \le X,Y \le 1
    \label{2001-2:eq:2}
\end{align}
$$

  となる．

  

<figure id="2001-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $h$のとりうる領域</figcaption>
</figure>

  [(式1)](#2001-2:eq:1)と合わせて，
  $1 \le h$での$h$の挙動を示した図から，この条件は
  

$$
\begin{align}
\begin{dcases}
      1-h < X,Y < h-1  & 1 \le h \le 2 \\
      -1 \le X,Y \le 1 & 2 \le h
    \end{dcases}\label{2001-2:eq:3}
\end{align}
$$

  である．

  $D_{0,0}$の面積$h^2$に対する[(式3)](#2001-2:eq:3)の領域の面積が求める確率$P(h)$であって，[(式0)](#2001-2:eq:0)と合わせて
  

$$
\begin{align*}
P(h) =
     & \begin{dcases}
         0                             & (0 < h \le 1)   \\
         \frac{\{(h-1)-(1-h)\}^2}{h^2} & (1 \le h \le 2) \\
         (\frac{2}{h})^2               & (2 \le h)
       \end{dcases}\\& \begin{dcases}
         0                    & (0 < h \le 1)   \\
         \frac{4(h-1)^2}{h^2} & (1 \le h \le 2) \\
         (\frac{2}{h})^2      & (2 \le h)
       \end{dcases}
\end{align*}
$$

  である．$\cdots$(答)
  

  (2)

  

<figure id="2001-2:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/2/fig_4.svg" alt="図 4" />
  <figcaption>図 4: 座標平面に半径$\sqrt{2}+1$の円を敷き詰めた様子．</figcaption>
</figure>

  (1)と同様に一つの円の中心が原点となるように座標平面をおく．
  この円と隣り合う円のうち，一部が第一章限にある二つの円の中心までの位置ベクトルを$\vec{a},\vec{b}$とすると
  

$$
\begin{align*}
\vec{a} = \begin{pmatrix}2(\sqrt{2}+1\end{pmatrix} \\ 0), \quad\vec{b} = (\sqrt{2}+1)\begin{pmatrix}1 \\\sqrt{3}\end{pmatrix}
\end{align*}
$$

  である．

  

<figure id="2001-2:fig:5">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/2/fig_5.svg" alt="図 5" />
  <figcaption>図 5: $D$は三角形OABの内部である．</figcaption>
</figure>

  (1)と同じく，座標平面は$\vec{a},\vec{b}$の張る三角形によって埋め尽くすことができるから，
  その一つである領域$D$
  

$$
\begin{align*}
D: \{m\vec{a} + n\vec{b}\mid 0 \le m, n, m+n \le 1\}
\end{align*}
$$

  の内部に円$C$の中心 $P(X,Y)$ がある時のみを考えれば良い．
  この時Cの半径が$1$だから，Cは[図5](#2001-2:fig:5)の3円とのみ交わりうる．
  したがって，Cが3円とのみ交わることはこれら全ての円と交わることと同値である．
  3円の中心をO，A，Bとして，中心同士の距離を
  

$$
\begin{align*}
PO=l_1, PA=l_2, PB=l_3
\end{align*}
$$

  とおくと，このような条件は
  

$$
\begin{align*}
& \left((\sqrt{2}+1)-1\right)\le l_k \le\left((\sqrt{2}+1)+1\right)& (k=1,2,3) \\\therefore& \sqrt{2}\le l_k \le\sqrt{2}+2                                     & (k=1,2,3)
\end{align*}
$$

  である．
  各辺正だから2乗してよく，
  

$$
\begin{align*}
& 2 \le l_k^2 \le 6+4\sqrt{2}& (k=1,2,3)
\end{align*}
$$

  を得る．
  これをみたす$P(X,Y)$の領域は[図6](#2001-2:fig:6)の斜線部である．

  

<figure id="2001-2:fig:6">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/2/fig_6.svg" alt="図 6" />
  <figcaption>図 6: $P(X,Y)$の領域は斜線部</figcaption>
</figure>

  この領域の面積$S$は
  

$$
\begin{align}
S = 3 \times\text{図形}SU + \triangle STU \label{2001-2:eq:4}
\end{align}
$$

  と書ける．そこでこれらの扇形SUと正三角形STUの面積を求める．

  

<figure id="2001-2:fig:7">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/2/fig_7.svg" alt="図 7" />
  <figcaption>図 7: 扇形SUの様子</figcaption>
</figure>

  簡単のため
  

$$
\begin{align}
r=\sqrt{2}+2 \label{2001-2:eq:8}
\end{align}
$$

  とおく．
  点Sの座標は$S(\sqrt{2}+1,\sqrt{2}+1)$だから$\angle AOS=\frac{\pi}{4}$であり，
  対称性から扇形SUの見込む角度は$\frac{\pi}{4}-\frac{\pi}{12}=\frac{\pi}{3}$である．

  従って
  

$$
\begin{align}
\text{図形}SU
     & = \triangle OSU - \text{扇形}OSU                                   \\& = \frac{\pi}{12}r^2 - \frac{1}{2}r^2\sin\frac{\pi}{6}\\& = \left(\frac{\pi}{12}-\frac{1}{4}\right)r^2 \label{2001-2:eq:5}
\end{align}
$$

  である．

  次に正三角形の一辺の長さ$\alpha$とおくと
  

$$
\begin{align*}
\alpha = 2r \sin\frac{\pi}{12}
\end{align*}
$$

  だから，この面積は
  

$$
\begin{align}
\triangle& = \frac{\sqrt{3}}{4}\alpha^2                                         \\& = \sqrt{3}r^2\sin^2\frac{\pi}{12}\\& = \sqrt{3}r^2\frac{1-\cos\frac{\pi}{12}}{2}\\& = \frac{\sqrt{3}}{2}\left(1-\frac{\sqrt{3}}{2}\right)r^2             \\& = \left(\frac{\sqrt{3}}{2}-\frac{3}{4}\right)r^2 \label{2001-2:eq:6}
\end{align}
$$

  である．

  [(式6)](#2001-2:eq:5,2001-2:eq:6)を[(式4)](#2001-2:eq:4)に代入して
  

$$
\begin{align}
S
     & = 3\left(\frac{\pi}{12}-\frac{1}{4}\right)r^2 +\left(\frac{\sqrt{3}}{2}-\frac{3}{4}\right)r^2 \\& = \left(\frac{\pi}{4} + \frac{\sqrt{3}}{2}-\frac{3}{2}\right)r^2 \label{2001-2:eq:7}
\end{align}
$$

  を得る．

  一方で領域$D$の面積は
  

$$
\begin{align*}
D\text{の面積}& = \triangle OAB                              \\& = \frac{\sqrt{3}}{4}(2(\sqrt{2}+1))^2        \\& = \frac{\sqrt{3}}{4}(\sqrt{2}(\sqrt{2}+2))^2 \\& = \frac{\sqrt{3}}{2}r^2
\end{align*}
$$

  である．ただしし最終行で[(式8)](#2001-2:eq:8)を用いた．

  問題文で与えられている確率の求め方を利用して，求める確率$q$は領域$D$の面積に対する$S$の比率であって，
  

$$
\begin{align*}
q
     & = \frac{S}{D\text{の面積}}\\& = \frac{\left(\frac{\pi}{4} + \frac{\sqrt{3}}{2} - \frac{3}{2}\right)r^2}{\frac{\sqrt{3}}{2}r^2}\\& = \frac{2}{\sqrt{3}}\left(\frac{\pi}{4} + \frac{\sqrt{3}}{2} - \frac{3}{2}\right)\\& = \frac{\sqrt{3}}{3}\left(\frac{1}{2}\pi + \sqrt{3} - 3\right)
\end{align*}
$$

  である．$\cdots$(答)
  

  

## 【解説】