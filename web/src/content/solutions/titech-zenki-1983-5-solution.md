---
university: "titech"
category: "zenki"
year: "1983"
question: "5"
type: "solution"
title: "TITECH 1983 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$$
\begin{align*}
\ell_1: y=-x-2, \qquad\ell_2: y=-\frac{1}{t^2}x+\frac{2}{t}
\end{align*}
$$

$\ell_1$と$y=-\dfrac3x$の交点のうち$A(1,-3)$，$\ell_2$と$y=-\dfrac3x$の交点のうち$B\left(3t,-\dfrac1t\right)$，$\ell_1$と$\ell_2$の交点$C\left(-\dfrac{2t}{t-1},\dfrac{2}{t-1}\right)$とおく．$S(t)$は，直線$AC$，$BC$と曲線$AB$（$y=-3/x$）とで囲まれた図形の面積であり，右のように分割できる．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1983/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 面積$S(t)$を求めるための図形の分割</figcaption>
</figure>

補助点$D\left(1,-\dfrac1t\right)$をとると，

$$
\begin{align*}
\triangle ADB=\frac12(3t-1)\left(3-\frac1t\right)=\frac{(3t-1)^2}{2t}
\end{align*}
$$

$$
\begin{align*}
\text{（曲線と弦}DB\text{の間の面積）}=\int_1^{3t}\frac3x\,dx-(3t-1)\cdot\frac1t=3\log3t-\frac{3t-1}{t}
\end{align*}
$$

であり，$\triangle ABC$の面積は

$$
\begin{align*}
\triangle ABC=\frac12\left|(3t-1)\left(\frac{2}{t-1}+3\right)-\left(-\frac1t+3\right)\left(-\frac{2t}{t-1}-1\right)\right|=\frac12\cdot\frac{(3t-1)^2}{t-1}\cdot\frac{t+1}{t}
\end{align*}
$$

これらを合わせて計算すると，

$$
\begin{align*}
S(t)=\frac{2(3t-1)}{t-1}+3\log3t
\end{align*}
$$

を得る．よって

$$
\begin{align*}
S'(t)=\frac3t-\frac{4}{(t-1)^2}=\frac{(3t-1)(t-3)}{t(t-1)^2}
\end{align*}
$$

$t>1$において下表を得る．

| $t$  | $1$ |              | $3$ |              |     |
|:------:|:-----:|:------------:|:-----:|:------------:|:---:|
| $S'$ |       |    $-$     | $0$ |    $+$     |     |
| $S$  |       | $\searrow$ |       | $\nearrow$ |     |

したがって，

$$
\begin{align*}
\min S(t)=S(3)=8+6\log3
\end{align*}
$$