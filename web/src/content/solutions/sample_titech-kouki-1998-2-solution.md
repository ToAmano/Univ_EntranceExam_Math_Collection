---
university: "sample_titech"
category: "kouki"
year: "1998"
question: "2"
type: "solution"
title: "SAMPLE_TITECH 1998 kouki Q2 (solution)"
---

\tdplotsetmaincoords{70}{100}

  

## 【解】

  

<figure id="1998-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1998/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $l_1$,$l_2$の様子</figcaption>
</figure>

  

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1998/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $C$上の点$P$と直線$l_1$の距離．</figcaption>
</figure>

### (1)

  まず、$Z = k$ での $C$ の切断面を求める．(1)の答えは最後に$k=0$とすれば求まる．
  対称性から $0 \le k$ とする.
  $l_1$と$l_2$の様子を[図1](#1998-2:fig:1)に示す．
  $l_1$ と $l_2$ の距離が $1$ だから, $C$ 上の点 $P(X,Y,Z)$ のみたす条件は,
  $P$ と $l_1$ の距離が $1$ であることである．
  $P$ から $l_1$ に下ろした垂足 $H$ とすると,
  $\vec{OH}$ は $\vec{OP}$ の $l_1$ への射影だから,
  $l_1$の方向ベクトルを$\vec{n}=(0,1,1)$ として
  
$$
\begin{align}
\vec{OH}& = \frac{\vec{OP} \cdot \vec{n}}{|\vec{n}|^2}\vec{n}\nonumber\\\therefore\left|\vec{OH}\right|& = \frac{|\vec{OP}\cdot\vec{n}|}{|\vec{n}|}\nonumber\\& = \frac{(Y+Z)^2}{2}\label{1998-2:eq:1}
\end{align}
$$

  である．$\triangle OPH$ にピタゴラスの定理を用いて$\eqref{1998-2:eq:1}$を代入すると
  
$$
\begin{align*}
PH^2 = OP^2 - OH^2 = (X^2+Y^2+Z^2) - \frac{(Y+Z)^2}{2}
\end{align*}
$$

  これが $1$ に等しいので,
  
$$
\begin{align}
2(X^2+Y^2+Z^2) - (Y+Z)^2 = 2 \label{1998-2:eq:2}
\end{align}
$$

  を得る．これが$C$ の方程式である．

  $Z=k$での切断面は，$\eqref{1998-2:eq:2}$に$Z=k$を代入して
  
$$
\begin{align}
2X^2 + Y^2 - 2kY + k^2 - 2 = 0 \nonumber\\
    2X^2 + (Y-k)^2 = 2 \label{1998-2:eq:3}
\end{align}
$$

  という楕円である. 図示すると[図3](#1998-2:fig:2)のようになる．

  

<figure id="1998-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1998/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 楕円: $2x^2 + (y-k)^2 = 2$の様子</figcaption>
</figure>

  従って，$\eqref{1998-2:eq:3}$に$k=0$を代入して，$xy$平面での断面は
  
$$
\begin{align*}
2x^2+y^2=2
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  次に，$C$を$z$軸周りに回転させた$R$の方程式について考える．

### (2)
の答えは，最後に$x=0$を代入すれば求まる．

  $C$ の $z=k$ での切断面 $C_k$ を原点$O_{k}(0,0,k)$中心に回転させたものが$R$である．
  従って，$C_k$上の点で, 原点からの距離が最大の点を $A_k$, 最小の点 $B_k$ とおくと,
  この平面での回転体$R$の範囲は
  
$$
\begin{align*}
O_KB_k^2 \le x^2+y^2 \le O_kA_k^2
\end{align*}
$$

  であり，面積 $S_k$ は
  
$$
\begin{align}
S_k = \pi(O_kA_k^2 - O_kB_k^2)\label{1998-2:eq:4}
\end{align}
$$

  で与えられる.$R$の様子を[図4](#1998-2:fig:3)に示す．

  

<figure id="1998-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1998/2/fig_4.svg" alt="図 4" />
  <figcaption>図 4: 回転体$R$の$z=k$での断面</figcaption>
</figure>

  $k \ge \sqrt{2}$ の時は明らかに $A_k(0, k+\sqrt{2}), B_k(0, k-\sqrt{2})$ である.
  以下 $0 \le k \le \sqrt{2}$ の時を考える.
  $C_k$ 上の点 $Q$ は, $Q(\cos\theta, k+\sqrt{2}\sin\theta)$ とおける.
  ただし$-\pi \le \theta \le \pi$ とする.
  この時の$OQ$を考えると
  
$$
\begin{align*}
\overline{\text{OQ}}^2
     & = \cos\theta^2+2\sin\theta^2+\sqrt{2}k\sin\theta+k^2 \\& = \sin\theta^2+2\sqrt{2}k\sin\theta+k^2+1            \\& = (\sin\theta+\sqrt{2}k)^2+1-k^2
\end{align*}
$$

  であり，$-1 \le \sin\theta \le 1$だから,
  $\overline{\text{OQ}}^2$の最小値，最大値は$k$によって以下のようになる.
  まず最小値は
  
$$
\begin{align}
\label{1998-2:eq:5}\begin{dcases}
      0 \le k \le \frac{\sqrt{2}}{2}, & \min \overline{\text{OQ}}^2 = 1-k^2, (\sin\theta=-\sqrt{2}k)                     \\
      \frac{\sqrt{2}}{2} < k \le 1,   & \min \overline{\text{OQ}}^2 = \left(k-\sqrt{2}\right)^2, (\sin\theta>-\sqrt{2}k)
    \end{dcases}
\end{align}
$$

  であり，一方最大値は$\theta=\pi/2$のときで，$A_k(0, k+\sqrt{2})$で一定である．
  この時$\max \overline{\text{OQ}}^2 = \overline{\mathrm{OA_k}}^2 = (k+\sqrt{2})^2$である．
  したがって, $\eqref{1998-2:eq:4,1998-2:eq:5}$から$Z=k$での$R$の領域及び面積$S_k$は以下のようになる.
  
$$
\begin{align}
& R =      \nonumber\\& \begin{dcases}
          1-k^2 \le x^2+y^2 \le (k+\sqrt{2})^2                        & \left(0 \le k \le \frac{\sqrt{2}}{2}\right) \\
          \left(k-\frac{1}{2}\right)^2 \le x^2+y^2 \le (k+\sqrt{2})^2 & \left(\frac{\sqrt{2}}{2} \le k \le 1\right)
        \end{dcases}\label{1998-2:eq:6}\\& S_k               \nonumber\\
    = & \begin{dcases}
          \pi \left\{ \left(k+\sqrt{2}\right)^2 + k^2 - 1 \right\} & \left(0\le k\le \frac{\sqrt{2}}{2}\right) \\
          \pi \left\{ (k+\sqrt{2})^2-(k-\sqrt{2})^2 \right\}       & \left(\frac{\sqrt{2}}{2} \le k\right)
        \end{dcases}\nonumber\\
    = & \begin{dcases}
          \pi (2k^2+2\sqrt{2}k+1) & \left(0\le k\le \frac{\sqrt{2}}{2}\right) \\
          4\sqrt{2}\pi k          & \left(\frac{\sqrt{2}}{2} \le k\right)
        \end{dcases}\label{1998-2:eq:7}
\end{align}
$$

  従って，求める$R$の$yz$平面での断面は，$\eqref{1998-2:eq:6}$に$k=z,x=0$を代入して
  
$$
\begin{align*}
R & =
    \begin{dcases}
      1-z^2 \le y^2 \le (z+\sqrt{2})^2          & \left(0 \le z \le \frac{\sqrt{2}}{2}\right) \\
      (z-\sqrt{2})^2 \le y^2 \le (z+\sqrt{2})^2 & \left(\frac{\sqrt{2}}{2} \le z \le 1\right)
    \end{dcases}
\end{align*}
$$

  であり，図示すると[図5](#1998-2:fig:4)のようになる．ただし境界を含む．$\cdots$(答)

  

<figure id="1998-2:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1998/2/fig_5.svg" alt="図 5" />
  <figcaption>図 5: (2)の回答の領域，すなわち$R$ の $yz$ 平面での断面．</figcaption>
</figure>

### (3)

  対称性から，$\eqref{1998-2:eq:7}$を$0\le k \le 2$で積分したものの2倍が求める体積である．
  
$$
\begin{align}
\frac{1}{2}V
     & = \int_0^2 S_k dk                                                                                       \nonumber\\& = \int_0^{\sqrt{2/2}}\pi(2k^2+2\sqrt{2}k+1)dk + \int_{\sqrt{2}/2}^{2} 4\sqrt{2}\pi k dk \label{1998-2:eq:8}
\end{align}
$$

  である。各項積分すると
  
$$
\begin{align*}
\int_0^{\sqrt{2}/2}(2k^2+2\sqrt{2}k+1)dk
     & = \left[\frac{2}{3}k^3+\sqrt{2}k^2 + k \right]_0^{1/2}\\& = \frac{7}{6}\sqrt{2}\\\int_{\sqrt{2}/2}^{\sqrt{2}} 4\sqrt{2}kdk
     & = 2\sqrt{2}\biggr[k^2\biggr]_{\sqrt{2}/2}^{2}\\& = 7\sqrt{2}
\end{align*}
$$

  だから$\eqref{1998-2:eq:8}$に代入して
  
$$
\begin{align*}
V
     & = 2\pi\left\{\frac{7}{6}\sqrt{2} + 7\sqrt{2}\right\}\\& = \frac{49}{3}\sqrt{2}\pi
\end{align*}
$$

  が求める体積である．$\cdots$(答)

  
  

## 【解説】

  空間図形の問題．回転体の回転体という面白いコンセプトである．
  まずは$C$の方程式を導出できるかどうかが分水嶺だが，
  その後も場合わけがあったり計算強度もそこそこ高いので最後まで気が抜けない．

  まず$C$の方程式を求める部分だが，これは空間における点と直線の距離を求める問題と言える．
  空間中の直線$l$が方程式$\vec{x}=\vec{x}_{0}+t\vec{a}$と表されている時，空間内の点$P$の位置ベクトル$\vec{p}$とすると
  $P$と$l$の距離は
  
$$
\begin{align*}
d = \frac{\sqrt{|\vec{p}-\vec{x}_0|^2|\vec{a}|^2-\left[(\vec{p}-\vec{x}_{0})\cdot \vec{a}\right]^2}}{|\vec{a}|}
\end{align*}
$$

  で与えられる．

  もちろんこの公式は覚えている必要はなく，必要になったら解答のように導けば良い．
  そのため，導出方法をここであらためて紹介しよう．

  点$P$から$l$におろした垂線の足を$H$とすると，$\vec{X_0H}$は$\vec{X_0P}$の$l$への正射影だから
  
$$
\begin{align*}
\vec{X_0H} = \frac{\vec{X_0P}\cdot \vec{a}}{|\vec{a}|^2}\vec{a}
\end{align*}
$$

  であり，
  
$$
\begin{align*}
\vec{HP} = \vec{X_0P} -\vec{X_0H}
\end{align*}
$$

  の大きさを求めれば良い．
  変形すると
  
$$
\begin{align*}
d
     & = \left|\vec{HP}\right|\\& = \left|\vec{X_0P}-\vec{X_0H}\right|\\& = \left|\vec{X_0P}-\frac{\vec{X_0P}\cdot \vec{a}}{|\vec{a}|^2}\vec{a}\right|\\& = \left|\left(\vec{p}-\vec{x}_0\right)-\frac{(\vec{p}-\vec{x}_0)\cdot \vec{a}}{|\vec{a}|^2}\vec{a}\right|\\& = \frac{\left|\left(\vec{p}-\vec{x}_0\right)|\vec{a}|^2-\left[(\vec{p}-\vec{x}_0)\cdot \vec{a}\right]\vec{a}\right|}{|\vec{a}|^2}\\& = \frac{\sqrt{\left|\vec{p}-\vec{x}_0\right|^2|\vec{a}|^4+\left[(\vec{p}-\vec{x}_0)\cdot \vec{a}\right]^2|\vec{a}|^2-2\left[(\vec{p}-\vec{x}_0)\cdot \vec{a}\right]^2|\vec{a}|^2}}{|\vec{a}|^2}\\& = \frac{\sqrt{\left|\vec{p}-\vec{x}_0\right|^2|\vec{a}|^2-\left[(\vec{p}-\vec{x}_0)\cdot \vec{a}\right]^2}}{|\vec{a}|}\\
\end{align*}
$$

  となり示された．

  次の(2)は楕円を回転させたときの図形がどうなるかを考えれば良い．
  この手の回転の問題は，単に原点から最も近い点と最も遠い点だけわかれば良いことに注意しよう．
  すると，原点から最も遠い点は常に一定だが，原点から近い点は$k$の値によって変化し，場合わけが必要になる．

  解答中の工夫としては，(1)も(2)も$xy$平面や$yz$平面といった特殊な場合を考えさせているが，これらを全て一般的に求めている点である．
  こうすることで(3)の負担が軽く，さらに全体としても見通し良いものになっているだろう．
  この手の誘導問題は，誘導に乗っても乗らなくても良い（自分の好きなように解けば良い）ということはあらためて覚えておきたい．