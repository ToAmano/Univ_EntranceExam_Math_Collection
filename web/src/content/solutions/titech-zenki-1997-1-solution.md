---
university: "titech"
category: "zenki"
year: "1997"
question: "1"
type: "solution"
title: "TITECH 1997 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

**$1^\circ$ $(a,b)=(0,0)$の時**

題意は成立．

**$2^\circ$ $a=0,\ b\ne0$の時**

$a^2x^2+b^2y^2\le1$をみたす$(x,y)$は，$x$：任意，$|y|\le1/|b|$であり，$1\le b$であれば良い．

**$3^\circ$ $a\ne0,\ b=0$**

$2^\circ$と同様に$1\le a$であれば良い．

以下，$ab\ne0$のもとで考える．この時，$xy$平面上で$a^2x^2+b^2y^2\le1$のグラフ上の点が$a(x-1)+b(y-1)\le0$をみたすような$(a,b)$の範囲をもとめれば良い．$(x,y)=\left(\dfrac{r}{a}C,\dfrac{r}{b}S\right)$（$C=\cos\theta,\ S=\sin\theta,\ 0\le\theta<2\pi,\ 0\le r\le1$）とおける．これに代入して

$$
\begin{align*}
rC-a+rS-b\le0
\end{align*}
$$

$$
\begin{align*}
r\sqrt2\sin\left(\theta+\frac{\pi}{4}\right)\le a+b
\end{align*}
$$

が任意の$\theta,r$で成立すれば良く，その条件は

$$
\begin{align*}
a+b\ge\sqrt2
\end{align*}
$$

以上まとめて，

$$
\begin{align*}
a=b=0 \ \text{or}\ (ab\ne0\wedge a+b\ge\sqrt2)\ \text{or}\ (a=0\wedge b\ge1)\ \text{or}\ (b=0\wedge a\ge1)
\end{align*}
$$

図示して下図斜線部（境界，$\bullet$を含む）．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1997/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 条件を満たす$(a,b)$の領域（斜線部）</figcaption>
</figure>

\bigskip
**[別解]**

{\bf[別解]}
同様に$a\ne0,b\ne0$で考える．$X=ax,\ Y=by$とおく．$x^2+y^2\le1$をみたす全ての$X,Y$が$X+Y\le a+b$をみたせば良く，

$$
\begin{align*}
a+b\ge\sqrt2
\end{align*}
$$

である．