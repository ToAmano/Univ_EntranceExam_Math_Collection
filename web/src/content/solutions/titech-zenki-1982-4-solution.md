---
university: "titech"
category: "zenki"
year: "1982"
question: "4"
type: "solution"
title: "TITECH 1982 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

もとの楕円を$\theta$だけ回転させた図形上の点$(X,Y)$とすると

$$
\begin{align*}
x+yi=(X+Yi)\left(\frac{\sqrt2}{2}-\frac{\sqrt2}{2}i\right)=\frac{\sqrt2}{2}(X+Y)+\frac{\sqrt2}{2}i(-X+Y)
\end{align*}
$$

から

$$
\begin{align*}
(x,y)=\left(\frac{\sqrt2}{2}(X+Y),\ \frac{\sqrt2}{2}(X-Y)\right)
\end{align*}
$$

とすれば，

$$
\begin{align*}
\frac{(X+Y)^2}{12}\cdot\frac12+\frac12\cdot\frac{(X-Y)^2}{4}\le1
\end{align*}
$$

である．したがって斜線の部分の概形は下図．

$$
\begin{align*}
\text{扇型}\ OCD=\frac12\cdot\frac{\pi}{4}\cdot(2\sqrt3)^2=\frac32\pi\quad\cdots\text{①}
\end{align*}
$$

又，$\triangle OBC$について，$X=\dfrac{x}{2\sqrt3},\ Y=\dfrac{y}{2}$なる変換をすれば下図斜線部の領域式（単位円）になるので，

$$
\begin{align*}
\triangle OBC=\frac12\cdot\frac{\pi}{3}\times2\sqrt3\cdot2=\frac{2}{3}\sqrt3\pi\quad\cdots\text{②}
\end{align*}
$$

①②から，もとめる面積$S$として

$$
\begin{align*}
S=\frac32\pi+\frac23\sqrt3\pi=\left(\frac32+\frac{2\sqrt3}{3}\right)\pi
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1982/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 面積$S$を求めるための図</figcaption>
</figure>