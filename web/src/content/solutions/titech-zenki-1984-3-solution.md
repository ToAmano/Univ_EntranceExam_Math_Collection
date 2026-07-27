---
university: "titech"
category: "zenki"
year: "1984"
question: "3"
type: "solution"
title: "TITECH 1984 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$P_1\left(t_1,\dfrac1{t_1}\right),\ P_2\left(t_2,-\dfrac1{t_2}\right)$とおく（$t_1>0,\ t_2<0$）．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1984/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 双曲線$C_1$，$C_2$と点$P_1$，$P_2$</figcaption>
</figure>

1.  対称性から，$P_1$で$\ell$と$C_1$が接する場合を考える．この時，
  

$$
\begin{align*}
\ell: y=-\frac{1}{t_1^2}x+\frac{2}{t_1}
\end{align*}
$$

  であるから，$P_2\left((1-\sqrt2)t_1,\ \frac{1}{(\sqrt2-1)t_1}\right)$となり，
  

$$
\begin{align*}
\triangle OP_1P_2=\frac12\left|(1-\sqrt2)t_1\cdot\frac{1}{t_1}-\frac{1}{(\sqrt2-1)t_1}\cdot t_1\right|=\frac12\left|(1-\sqrt2)-(\sqrt2+1)\right|=\sqrt2=\text{const.}
\end{align*}
$$

  よって示された．

2.  一般の場合，$P=\dfrac{t_1}{t_2}$とおくと，
  

$$
\begin{align*}
\triangle OP_1P_2=\frac12\left|\frac{t_1}{t_2}+\frac{t_2}{t_1}\right|=\frac12\left|P+\frac1P\right|=-\frac12\left(P+\frac1P\right)
\end{align*}
$$

  （$t_1>0,\ t_2<0$より，$P$は$P<0$なる任意の実数をとる．）
  

$$
\begin{align*}
\triangle OP_1P_2=\sqrt2 \iff P^2+2\sqrt2P+1=0 \quad\therefore\ P=-\sqrt2\pm1
\end{align*}
$$

  **$1^\circ$ $P=-\sqrt2+1$の時**

  $t_1=(1-\sqrt2)t_2$とおけるが，この時，
  

$$
\begin{align*}
\ell: y=\frac{1}{t_2^2}x-\frac{2}{t_2}
\end{align*}
$$

  となり，$\ell$は$C_2$の接線．

  **$2^\circ$ $P=-\sqrt2-1$の時**

  $t_1=-(1+\sqrt2)t_2$とおけるが，この時，
  

$$
\begin{align*}
\ell: y=-\frac{x}{t_1^2}+\frac{2}{t_1}
\end{align*}
$$

  となり，$\ell$は$C_1$の接線．

  以上から示された．