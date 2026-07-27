---
university: "titech"
category: "zenki"
year: "1962"
question: "2"
type: "solution"
title: "TITECH 1962 zenki Q2 (solution)"
---

{\bf ［解］}

長針，短針の長さを $R, r$ とする．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1962/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>

題意から，2時，2時半の状態に余弦定理を用いると，

$$
\begin{align}
\begin{cases}
4^2 = R^2 + r^2 - 2Rr \cos \frac{\pi}{3} = R^2 + r^2 - Rr  \\
6^2 = R^2 + r^2 - 2Rr \cos \frac{7\pi}{12}
\end{cases}\label{eq:1}
\end{align}
$$

である．

ここで$\cos \frac{7}{12}\pi < 0$ だから半角公式より

$$
\begin{align}
\cos\frac{7}{12}\pi&= -\sqrt{\frac{1 + \cos \frac{7\pi}{6}}{2}}\\&= -\sqrt{\frac{1 - \frac{\sqrt{3}}{2}}{2}}\\&= -\frac{\sqrt{3}-1}{2\sqrt{2}}
\end{align}
$$

だから，[(式1)](#eq:1)に代入して

$$
\begin{align}
36 
  &= R^2 + r^2 + 2Rr \frac{\sqrt{3}-1}{2\sqrt{2}}\\&= R^2 + r^2 + \frac{\sqrt{3}-1}{\sqrt{2}} Rr \label{eq:2}
\end{align}
$$

となる．[(式2)](#eq:1,eq:2)を辺々引くと

$$
\begin{align}
& 20 = \left(\frac{\sqrt{6}-\sqrt{2}}{2} + 1 \right) Rr \\\therefore& Rr = \frac{40}{\sqrt{6}-\sqrt{2}+2}\label{eq:3}
\end{align}
$$

である．

また[(式1)](#eq:1)を変形して

$$
\begin{align}
R^2 + r^2 = 16 + Rr \label{eq:4}
\end{align}
$$

である．

もとめる長さ $l\ (>0)$ として4時の状態に余弦定理を用いると

$$
\begin{align}
l^2 = R^2 + r^2 - 2Rr \cos\frac{2\pi}{3} = R^2 + r^2 + Rr
\end{align}
$$

だから，[(式4)](#eq:3,eq:4)を代入して

$$
\begin{align}
l^2 &= (16 + Rr) + Rr \quad(\because\text{[(式4)](#eq:4)}) \\&= 16 + 2Rr \\&= 16 + \frac{80}{\sqrt{6}-\sqrt{2}+2}\quad(\because\text{[(式3)](#eq:3)}) \\&= 16 + 20(\sqrt{3}+1-\sqrt{2}) \\&= 20(\sqrt{3}-\sqrt{2}) + 36 \label{eq:5}
\end{align}
$$

を得るから，この少数第一位までの評価を求めれば良い．

以下$(6.5)^2 < l^2 < (6.6)^2$ であることを示す．

$$
\begin{align*}
(1.73)^2 < 3 < (1.733)^2 \quad&\therefore 1.73 < \sqrt{3} < 1.733 \\(1.41)^2 < 2 < (1.42)^2 \quad&\therefore 1.41 < \sqrt{2} < 1.42
\end{align*}
$$

だから，[(式5)](#eq:5)に代入して

$$
\begin{align}
& 20(1.733 - 1.42) + 36 < l^2 < 20(1.74 - 1.41) + 36 \\\therefore&42.26 < l^2 < 42.6
\end{align}
$$

一方で$(6.5)^2 = 42.25$, $(6.6)^2 = 43.56$ だから，

$$
\begin{align}
(6.5)^2 < l^2 < (6.6)^2
\end{align}
$$

よって示された．$l > 0$ より，

$$
\begin{align}
6.5 < l < 6.6
\end{align}
$$

つまり求める近似値は

$$
\begin{align}
l \fallingdotseq 6.5
\end{align}
$$

である．