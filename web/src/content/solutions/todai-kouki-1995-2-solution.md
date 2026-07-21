---
university: "todai"
category: "kouki"
year: "1995"
question: "2"
type: "solution"
title: "TODAI 1995 kouki Q2 (solution)"
---

## 【解】

### (1)

  

<figure id="1995-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1995/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点ABCの様子</figcaption>
</figure>

  $\mathrm{PQ}=1$ だから， $\mathrm{P}(0,0)$, $\mathrm{Q}(1,0)$ とし,
  $\triangle \mathrm{ABC}$ が $xy$ 平面にあるとする.
  (条件)をみたす時,$A,B,C$ は[図1](#1995-2:fig:1)の斜線部分内にある.

  もし $A,B,C$ が[図1](#1995-2:fig:1)で斜線部で, 境界を含まない部分にあるとすると $C$ から $AB$ に下ろした垂線と $E,F$ との交点のうち, 垂足 $H$ との距離が $\overline{CH}$ よりも大きいもの $C'$ が存在し
  $\triangle \mathrm{ABC} < \triangle \mathrm{ABC'}$ となる.
  したがって, $\triangle \mathrm{ABC}$ が最大の時, $C$ は $E$ 又は $F$ にある.
  他の頂点についても同様のことがいえるから題意は示された.

  $\cdots$(答)

### (2)

  Pを固定した時, ABにPから下した垂足をHとする.
  Hは $x^2+y^2=p^2$ 上を動く.
  この時三角形PAHを考えると
  
$$
\begin{align*}
\overline{AB}& = 2\overline{AH}\\& = 2\sqrt{1-p^2}
\end{align*}
$$

  で一定である．

  従って，この時E，F上でABからの距離が最大の点がCの時, $\triangle \mathrm{ABC}$ は最大である.
  そこで$0\le \theta < 2\pi$に対して
  
$$
\begin{align*}
\vec{\mathrm{PH}} = p \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}
\end{align*}
$$

  と置く．

  

<figure id="1995-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1995/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 点A，B，Cの様子</figcaption>
</figure>

  点CがE，F上でABからの距離が最大のとき，点Cでの円の接線の法線ベクトルも
  
$$
\begin{align}
\begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}\label{1995-2:eq:1}
\end{align}
$$

  である．
  このような点はE上に2点, F上に2点あるので，E上のものを$X_1, X_2$，F上のものを$X_3, X_4$とすると
  $X_1,X_2$について
  
$$
\begin{align}
\begin{dcases}
      \overline{HX_1} = 1 + p \\
      \overline{HX_2} = 1 - p
    \end{dcases}\label{1995-2:eq:2}
\end{align}
$$

  であり，$X_3, X_4$については$\eqref{1995-2:eq:1}$より
  
$$
\begin{align*}
& X_3(1+\cos\theta, \sin\theta) \\& X_4(1-\cos\theta, \sin\theta)
\end{align*}
$$

  として良い．
  $X_3,X_4$と線分ABの距離を$L_3,L_4$とすると
  
$$
\begin{align}
\begin{dcases}
      L_3 = |\cos\theta(1+\cos\theta)+\sin^2\theta-p| = |1-p+\cos\theta| \\
      L_4 = |\cos\theta(1-\cos\theta)-\sin^2\theta-p| = |-1-p+\cos\theta|
    \end{dcases}\label{1995-2:eq:3}
\end{align}
$$

  である．$0 \le p \le 1$および$-1 \le \cos\theta \le 1$から，$\eqref{1995-2:eq:2,1995-2:eq:3}$のうちで最大のものは
  $L_4$において$\cos\theta = -1$として時で
  
$$
\begin{align*}
\max L_4 = (p+2)
\end{align*}
$$

  である．

  この時，$\cos\theta=-1$より$\theta=\pi$となって，確かに$\mathrm{PQ} \perp \mathrm{AB}$ である．
  よって題意は示された．
  $\cdots$(答)

### (3)

### (2)
の結果から $p$を固定した時に $S$を最大にするのは
  [図3](#1995-2:fig:3)のようにHが$x$軸上に存在する時である．

  

<figure id="1995-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1995/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $p$を固定した時，三角形ABCの面積が最大になるような場合．</figcaption>
</figure>

  この時の面積$S(p)$として，
  
$$
\begin{align*}
S(p)
     & = \frac{1}{2}\overline{AB}\cdot\overline{HC}\\& = \frac{1}{2}\cdot 2 \sqrt{1-p^2}\cdot(p+2) \\& = \sqrt{(1-p^2)(p+2)^2}\\& \equiv\sqrt{f(p)}
\end{align*}
$$

  である．
  以下この最大値を求める．
  $f(p)$が最大の時$S(p)$も最大だから，$f(p)$の増減表を書く．
  一階微分は
  
$$
\begin{align*}
f'(p)
     & = 2(p+2)(1-p^2) - 2p(p+2)^2 \\& = 2(p+2)(1-2p-2p^2)
\end{align*}
$$

  より，$\eqref{1995-2:table:1}$を得る．
  \begin{table}[H]
    \centering
    \caption{$f(p)$の増減表．}
    \label{1995-2:table:1}
    

| $p$ | $0$ | $\cdots$ | $\frac{-1+\sqrt{3}}{2}$ | $\cdots$ | $1$ |
|:----:|:---:|:----------:|:-----------------------:|:----------:|:---:|
| $f'$ | | $+$ | $0$ | $-$ | |
| $f$ | | $\nearrow$ | | $\searrow$ | |

  \end{table}

  したがって，$f$および$S$は$p=\frac{-1+\sqrt{3}}{2}$で最大値
  
$$
\begin{align*}
\max S
     & = \sqrt{\max f(p)}\\& = \sqrt{f\left(\frac{-1+\sqrt{3}}{2}\right)}\\& = \sqrt{\frac{1+2p}{2}}\frac{3+\sqrt{3}}{2}\\& = \sqrt{\frac{\sqrt{3}}{2}}\frac{3+\sqrt{3}}{2}
\end{align*}
$$

  をとる．

  

## 【解説】

### (2)
の別解を紹介する．
  ABとPQのなす角を$\theta$とする. ABと平行に, Fの接線を引き, 接点をCとする.
  右図から, ABとCのキョリ$h$は
  $$ h = p + \sin\theta + 1 $$
  $\overline{AB}=\text{const}, p=\text{const}$から,
  $\triangle \mathrm{ABC}$が最大になるとき
  $h$が最大で $\theta = \pi/2$. (了)