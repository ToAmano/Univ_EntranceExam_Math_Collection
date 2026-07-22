---
university: "ukyoto"
category: "kouki"
year: "2000"
question: "1"
type: "solution"
title: "UKYOTO 2000 kouki Q1 (solution)"
---

## 【解】

  (1)
  複素数平面上で複素数$x$を点$X$と表す．
  

$$
\begin{align*}
\frac{\beta-z}{\alpha-z} = r(\cos\theta + i \sin\theta) & (r>0, 0 < \theta < 2\pi)
\end{align*}
$$

  とおくと，$\theta$は線分$ZA$から線分$ZB$への角度である．
  題意より，この虚数部分$r\sin\theta$が正だから，
  

$$
\begin{align*}
0 < \theta < \pi
\end{align*}
$$

  だから，$z$の存在する部分は下図斜線部 (境界含まず)である．
  点$A$から点$B$を見て，向かって左側の領域である．

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/2000/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点$z$の存在する領域は，$\alpha$ から $\beta$ を見て左側</figcaption>
</figure>

  
  (2)
  本題に入る前に(1)と似た状況として，
  

$$
\begin{align*}
\frac{\beta-z}{\alpha-z}
\end{align*}
$$

  の虚部が$0$，すなわち実数の場合を考える．
  この時，ある実数$r$を用いて
  

$$
\begin{align*}
& \beta - z = r(\alpha-z) \\
\end{align*}
$$

  と書けるから，$\alpha,\beta,z$は同一直線上にある．

  さて，以下題意を示す．
  与式から
  

$$
\begin{align*}
\begin{dcases}
      1 + \frac{z-\gamma}{z-\alpha} + \frac{z-\gamma}{z-\beta} = 0 \\
      1 + \frac{z-\alpha}{z-\gamma} + \frac{z-\alpha}{z-\beta} = 0 \\
      1 + \frac{z-\beta}{z-\gamma} + \frac{z-\beta}{z-\alpha}  = 0
    \end{dcases}
\end{align*}
$$

  であるから，両辺の虚部をとると
  

$$
\begin{align}
\begin{dcases}
      \Im \frac{z-\gamma}{z-\alpha} + \Im \frac{z-\gamma}{z-\beta} = 0 \\
      \Im \frac{z-\alpha}{z-\gamma} + \Im \frac{z-\alpha}{z-\beta} = 0 \\
      \Im \frac{z-\beta}{z-\gamma} +  \Im \frac{z-\beta}{z-\alpha}  = 0
    \end{dcases}\label{2000-1:eq:1}
\end{align}
$$

  を得る．
  まずこの第一式に注目すると，
  $\frac{z-\gamma}{z-\alpha}$, $\frac{z-\gamma}{z-\beta}$ の虚部は共に $0$ か, 互いに異符号である．
  虚部が共に$0$の場合は$\alpha,\beta,\gamma,z$が同一直線上にあって題意に反するから，互いに異符号であることが必要．
  $\alpha,\beta,\gamma$に関しての対称性から
  

$$
\begin{align}
\begin{dcases}
      \Im \frac{z-\gamma}{z-\alpha} > 0 \\
      \Im \frac{z-\gamma}{z-\beta} < 0
    \end{dcases}\label{2000-1:eq:2}
\end{align}
$$

  とおいて良い．
  ここで，実数でない複素数$x$に対して$1/x$の虚部は符号が逆であることに注意すると，
  

$$
\begin{align*}
\Im\frac{z-\beta}{z-\gamma} > 0
\end{align*}
$$

  だから[(式1)](#2000-1:eq:1)より
  

$$
\begin{align}
\Im\frac{z-\beta}{z-\alpha} < 0  \label{2000-1:eq:3}
\end{align}
$$

  である．以上[(式3)](#2000-1:eq:2,2000-1:eq:3)から
  

$$
\begin{align*}
\Im\frac{z-\gamma}{z-\alpha} > 0 \\\Im\frac{z-\beta}{z-\gamma} > 0  \\\Im\frac{z-\alpha}{z-\beta} > 0
\end{align*}
$$

  となる．

  従って（1）から，$z$の存在する範囲は直線$A\Gamma$，$\Gamma B$，$BA$によって規定される．
  これは点$\Gamma$がベクトルBAの向かって左手にあるか右手にあるかで異なる．
  向かって左手にある場合は$z$は三角形ABC内に存在し，向かって右手にある場合はそのような$z$は存在しない．
  [(式2)](#2000-1:eq:2)で逆の符号を採用した場合は逆の結果になる．

  

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/2000/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: ベクトル$BA$から見て$\Gamma$が左手にある場合は，点$z$は三角形$AB\Gamma$の内部に存在する</figcaption>
</figure>

  

<figure id="fig_3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/2000/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: ベクトル$BA$から見て$\Gamma$が右手にある場合は，そのような点$z$は存在しない．</figcaption>
</figure>

  以上から，確かに複素数$z$が存在して題意の方程式を満たす時，$z$は三角形$AB\Gamma$の内部にある．
  よって示された．$\cdots$(答)

  
  

## 【解説】