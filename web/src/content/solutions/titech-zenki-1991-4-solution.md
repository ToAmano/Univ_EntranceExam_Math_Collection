---
university: "titech"
category: "zenki"
year: "1991"
question: "4"
type: "solution"
title: "TITECH 1991 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$f(x)=x^3+ax^2+(b-a-1)x$

**(1)** $f'(x)=3x^2+2ax+(b-a-1)$だから，これが$x\ge0$で0以上であるような$(a,b)$を求めれば良い（$a,b\in\mathbb{R}$）．軸$x=-\dfrac13a$で場合分け．

**$1^\circ$ $-\dfrac13a\le0\ \therefore\ a\ge0$の時**

条件は$f'(0)\ge0\iff b\ge a+1$

**$2^\circ$ $0\le-\dfrac13a\ \therefore\ a\le0$の時**

条件は$f'(-\tfrac13a)\ge0\iff b\ge\dfrac13a^2+a+1$

以上をまとめ，図示して下図斜線部

$$
\begin{align*}
\begin{cases}
a\le0\text{の時}\ b\ge\dfrac13a^2+a+1 \\
a\ge0\text{の時}\ b\ge a+1
\end{cases}
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1991/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 条件を満たす$(a,b)$の範囲（斜線部）</figcaption>
</figure>

**(2)** $(a,b)$が$G$をうごく時，$0\le x$で$f(x)$は単調増加かつ$f(1)=b$から，グラフの概形は右図で，斜線部が求める面積$K$に等しい．したがって，与式$S$として

$$
\begin{align*}
S=b-\int_0^1f(x)dx
\end{align*}
$$

$$
\begin{align*}
=b-\left(\frac14+\frac13a+\frac12(b-a-1)\right)
\end{align*}
$$

$$
\begin{align*}
=\frac12b+\frac16a+\frac14 \quad\cdots\text{①}
\end{align*}
$$

である．$a$を固定すると，①から，

**$a\le0$の時**

$$
\begin{align*}
\min S=\frac16a+\frac12\left(\frac13a^2+a+1\right)+\frac14
\end{align*}
$$

$$
\begin{align*}
=\frac16a^2+\frac23a+\frac34
\end{align*}
$$

$$
\begin{align*}
=\frac16(a+2)^2+\frac1{12}\ge\frac1{12}\quad(\text{等号成立は}a=-2)
\end{align*}
$$

**$a\ge0$の時**

$$
\begin{align*}
\min S=\frac16a+\frac12(a+1)+\frac14
\end{align*}
$$

$$
\begin{align*}
=\frac23a+\frac34\ge\frac34 \quad(\because a=0)
\end{align*}
$$

だから，$\min S=\dfrac1{12}$