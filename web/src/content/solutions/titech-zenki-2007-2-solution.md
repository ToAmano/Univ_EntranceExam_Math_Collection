---
university: "titech"
category: "zenki"
year: "2007"
question: "2"
type: "solution"
title: "TITECH 2007 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

**(1)** $A=(a,a^2)$における$y=x^2$の接線は$y-a^2=2a(x-a)$である．この接線を$A$を中心に$-30^\circ$回転した直線が$l$である．$l$上の点$(x,y)$を$+30^\circ$回転すると接線上の点$(x',y')$に戻るから

$$
\begin{align*}
\begin{pmatrix}x'-a\\y'-a^2\end{pmatrix}=\begin{pmatrix}\cos\frac\pi6&-\sin\frac\pi6\\\sin\frac\pi6&\cos\frac\pi6\end{pmatrix}\begin{pmatrix}x-a\\y-a^2\end{pmatrix}
=\begin{pmatrix}\dfrac{\sqrt3}2(x-a)-\dfrac12(y-a^2)\\[4pt]\dfrac12(x-a)+\dfrac{\sqrt3}2(y-a^2)\end{pmatrix}
\end{align*}
$$

であり，これが接線上の点であることから$y'-a^2=2a(x'-a)$，すなわち

$$
\begin{align*}
\frac12(x-a)+\frac{\sqrt3}2(y-a^2)=2a\Bigl(\frac{\sqrt3}2(x-a)-\frac12(y-a^2)\Bigr).
\end{align*}
$$

整理すると，$l$の方程式は

$$
\begin{align*}
(\sqrt3+2a)y=(2\sqrt3a-1)x+a+2a^3-\sqrt3a^2\tag{①}
\end{align*}
$$

**(2)** $a>0$のとき，①と$y=x^2$の交点の$x$座標は

$$
\begin{align*}
(\sqrt3+2a)x^2=(2\sqrt3a-1)x+a+2a^3-\sqrt3a^2
\end{align*}
$$

の解であり，一方は$x=a$（点$A$）．解と係数の関係（積）より，他方の解$\alpha$（点$B$の$x$座標）は

$$
\begin{align*}
a\alpha=\frac{-(a+2a^3-\sqrt3a^2)}{\sqrt3+2a}\quad\therefore\ \alpha=\frac{-2a^2+\sqrt3a-1}{2a+\sqrt3}\qquad(<a).
\end{align*}
$$

直線と$y=x^2$で囲む面積の公式$\int_p^q\{(\text{直線})-x^2\}dx=\frac16(q-p)^3$（係数1の放物線に対する標準公式）を用いると，

$$
\begin{align*}
a-\alpha=\frac{4a^2+1}{2a+\sqrt3},\qquad T(a)=\frac16(a-\alpha)^3=\frac16\Bigl(\frac{4a^2+1}{2a+\sqrt3}\Bigr)^3.
\end{align*}
$$

一方，線分$OC$，$CA$と$y=x^2$で囲まれる面積は

$$
\begin{align*}
S(a)=\int_0^ax^2dx=\frac13a^3.
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/2007/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $S(a)$（斜線部）と$T(a)$（青色部），$a=1.3$の場合の概形</figcaption>
</figure>

よって

$$
\begin{align*}
\frac{T(a)}{S(a)}=\frac36\Bigl(\frac{4a^2+1}{2a+\sqrt3}\Bigr)^3\Big/a^3
=\frac12\Bigl(\frac{4a^2+1}{a(2a+\sqrt3)}\Bigr)^3
=\frac12\Bigl(\frac{4+\frac1{a^2}}{2+\frac{\sqrt3}a}\Bigr)^3.
\end{align*}
$$

$a\to\infty$のとき括弧内は$\dfrac42=2$に収束するから

$$
\begin{align*}
\lim_{a\to\infty}\frac{T(a)}{S(a)}=\frac12\cdot2^3=4.
\end{align*}
$$