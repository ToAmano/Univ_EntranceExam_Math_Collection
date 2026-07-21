---
university: "sample_titech"
category: "kouki"
year: "1995"
question: "1"
type: "solution"
title: "SAMPLE_TITECH 1995 kouki Q1 (solution)"
---

**【解】**

### (1)

  [図1](#1995-1:fig:1)のように，立方体の頂点A, B, C, D, E, F, G, Hに対し題意の3面を
  ABCD, AEFB, AEHDとする. 各球の中心は
  立方体及び球の対称性から対角線AG上にある．
  $S_n$の中心を$O_n$，半径を$r_n$とおく．
  断面AEGCを[図2](#1995-1:fig:2)に示す．$AC=2\sqrt{2}$,$AE=2$より，$\angle\mathrm{GAC}=\theta$と置くと
  
$$
\begin{align}
\sin\theta& = \frac{\mathrm{AE}}{\mathrm{AG}} = \frac{1}{\sqrt{3}}\label{1995-1:eq:1}\\\cos\theta& = \frac{\mathrm{AC}}{\mathrm{AG}} = \frac{\sqrt{2}}{\sqrt{3}}\label{1995-1:eq:2}
\end{align}
$$

  が成り立つことに注意する．

  
<figure id="1995-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1995/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 立方体と頂点の定義</figcaption>
</figure>

  
<figure id="1995-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1995/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 断面AEGC</figcaption>
</figure>

  半径$r_n$に関する漸化式を導出することで$r_n$の一般項を求める．
  円$S_n$と$S_{n+1}$に着目して[図3](#1995-1:fig:3)を考える．

  
<figure id="1995-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1995/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: \(S_n\)と\(S_{n+1}\)の関係</figcaption>
</figure>

  $O_n$から$AC$に引いた垂線と$AC$との交点を$T_n$と置くと，その定義より$O_nT_n$の長さは$r_n$に等しい．
  一方で，$O_{n+1}$から$O_nT_n$に引いた垂線と$O_nT_n$の交点を$R_n$と置くと，
  
$$
\begin{align*}
O_nT_n
     & =O_{n+1}T_{n+1}+O_nR_n                        \\& =O_{n+1}+O_nO_{n+1}\sin\theta\\& =r_{n+1}+\left(r_{n}+r_{n+1}\sin\theta\right)
\end{align*}
$$

  と表されるので，$r_n$と$r_{n+1}$の関係は
  
$$
\begin{align}
r_{n}& =r_{n+1}+(r_{n}+r_{n+1}\sin\theta)        \\\therefore
    r_{n+1}& = \frac{1-\sin\theta}{1+\sin\theta} r_{n}
\end{align}
$$

  となる．$r_0=1$と合わせると，この等比級数の解は
  
$$
\begin{align}
r_{n}& = \left(\frac{1-\sin\theta}{1+\sin\theta}\right)^n \\& = (2-\sqrt{3})^n
\end{align}
$$

  となる．ただし，$\eqref{1995-1:eq:1}$を用いた．$\cdots$(答)

### (2)

  立方体 $C$ の中でどの $S_k$ ($k=0,1,\ldots, n$) にも含まれない部分の体積を$V_n$とする．
  求めるべき値は$\displaystyle V = \lim_{n\to\infty}V_n$である．
  $S_k\, (k=0,1,\cdots,n)$同士は互いに体積を共有することはないから，
  体積$V_n$は立方体$C$の体積から，$S_k\, (k=0,1,\cdots,n)$の体積を減じたものに等しく，
  
$$
\begin{align*}
V_n & = 8 - \frac{4}{3}\pi\sum_{k=0}^{n} r_k^3                             \\& = 8 - \frac{4}{3}\pi\sum_{k=0}^{n}(2-\sqrt{3})^{3k}\\& = 8 - \frac{4}{3}\pi\frac{1-(2-\sqrt{3})^{3(n+1)}}{1-(2-\sqrt{3})^3}
\end{align*}
$$

  となる．

  $0<(2-\sqrt{3})^3 < 1$ だから求める体積$V$は
  
$$
\begin{align*}
V & = \lim_{n \to \infty} V_n                       \\& = 8 - \frac{4}{3}\pi\frac{1}{1-(2-\sqrt{3})^3}\\& = 8 - \frac{6\sqrt{3}+10}{15}\pi
\end{align*}
$$

  である．$\cdots$(答)

  **【解説】**

  空間図形と数列や極限をうまく融合した問題である．

### (1)
の漸化式さえもとまればあとは機械的な計算で解けるため，(1)の前半がポイントだろう．
  逆に(1)がとければ(2)はボーナス問題であり，点差がつきやすいと言えるかもしれない．

  問題としては球を考えているが，結局全ての球の中心は四角形$ACGE$上にあるからこの断面で考えればよく，平面図形の問題に帰着する．
  その上で，漸化式を求める部分では$S_n$と$S_{n+1}$を考えて二つの関係をなんとか導出すれば良い．
  解答中では$O_nT_n$を考えたが，他に$O_nO_{n+1}$を考えるなど，（本質的には同じ）いくつかのやり方がある．
  いずれも計算時間は大差ないだろう．

  解答中の細かい計算上のポイントとしては，$\theta$を導入して極力代入を遅らせている点が挙げられる．
  この問題に限らず，入試で部分点を極力取りにいくという姿勢にたつと，先に代入すると計算ミスが発生しやすい上に，ミスが追いにくいという問題がある．
  $\sin\theta$も$\cos\theta$も値としては簡単な値だが，最後の最後$r_n$を求めるところまでは代入の必要がないのでわざわざ文字でおいている．