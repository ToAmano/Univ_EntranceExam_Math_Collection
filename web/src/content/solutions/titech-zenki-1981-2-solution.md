---
university: "titech"
category: "zenki"
year: "1981"
question: "2"
type: "solution"
title: "TITECH 1981 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$f(x)=x^3+3x^2$ とする．グラフの概形は右図．

$$
\begin{align*}
f'(x)=3x^2+6x
\end{align*}
$$

から，$x=t$ での接線は

$$
\begin{align*}
y=(3t^2+6t)x-2t^3-3t^2
\end{align*}
$$

となる．これが$O$を通る時，

$$
\begin{align*}
2t^3+3t^2=0 \iff t=0,\ -\frac32
\end{align*}
$$

であることに注意すると，線分$OT$が$D$に含まれるような点$T$の領域は下図斜線部（境界含む）である．辺$OR$，$OS$がこの領域内にあることが必要で，逆にこの時$\triangle ORS$は$D$に含まれる．よって$R$，$S$は下図斜線部内をうごく．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1981/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点$T$が動く領域$D$（斜線部）</figcaption>
</figure>

さて，$\triangle ORS$の$\max$を与える$R,S$の候補を考えよう．まず，$S$を固定し，$R$を$y=kx\ (k\ge0)$上で固定し，この上で動かす．$OR$を底辺とみれば，$\triangle ORS$が$\max$となるのは$OR$が最大，つまり$R$がこの領域$E$の境界上をうごく時である．

同様に考えれば，$S$も$E$の境界上の時，$\triangle ORS$は$\max$となる．そこでまず$\max$を与える$R$をもとめる．$S$を境界上で動かし，$OS: y=kx\ (k\le0)$とする．この時，$OS$と$R$の距離は$R(x_1,y_1)$として

$$
\begin{align*}
\ell=\frac{|kx_1+y_1|}{\sqrt{k^2+1}}=\frac{-kx_1+y_1}{\sqrt{k^2+1}}\quad(\because\ x_1,y_1\ge0,\ -k\ge0)
\end{align*}
$$

これは$x_1,y_1$について単調増加だから，$\max\triangle ORS$を与える$R$の1つに$R(1,4)$がある．この時$S$と$OR$の距離を$\max$にする$S$をもとめれば良い．$S(x_2,y_2)$として，この距離を$\ell_2$とすると，$OR: y=4x$だから

$$
\begin{align*}
\ell_2=\frac{|4x_2-y_2|}{\sqrt{17}}=\frac{-4x_2+y_2}{\sqrt{17}}\quad(\because\ x_2<0,\ y_2>0)
\end{align*}
$$

となり，同様に，これを$\max$にする$S$は$S\left(-\dfrac{16}{9},4\right)$である．

以上から，$S\left(-\dfrac{16}{9},4\right)$，$R(1,4)$の時，$\triangle ORS$は$\max$で，

$$
\begin{align*}
\frac12\left|1\cdot4+\frac{16}{9}\cdot4\right|=\frac{50}{9}
\end{align*}
$$

となる．