---
university: "titech"
category: "zenki"
year: "1971"
question: "4"
type: "solution"
title: "TITECH 1971 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$0<\theta<\dfrac{\pi}{2}$ 以下 $C=\cos\theta, S=\sin\theta$ と書く．

1.  
$$
\begin{align*}
\begin{cases}
  0\le x\le C \\
  0\le y\le S
  \end{cases}
\end{align*}
$$

  のもとで $Q(u,v)$ ($u=x+y, v=xy$) の軌跡をもとめる．対称性からまず，$0\le\theta\le\dfrac{\pi}{4}$ でかんがえる．$u,v$ は $t$ の2次方程式 $t^2-ut+v=0$ の上記をみたす2実解である．$f(t)=t^2-ut+v$ とおく．$0<\theta\le\dfrac{\pi}{4}$ より $C\ge S$ だから，以下のいずれかである．

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1971/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $1^\circ$，$2^\circ$の場合分けにおける$t$の範囲</figcaption>
</figure>

  **$1^\circ$ の時** \quad $f(t)=0$ の判別式を $D$ とする．
  

$$
\begin{align*}
\begin{cases}
  D\ge0 \\
  f(0), f(S)\ge0 \\
  0\le \dfrac{u}{2}\le S
  \end{cases}\iff\begin{cases}
  u^2-4v\ge0 \\
  0\le u\le 2S \\
  v\ge0 \\
  S^2-uS+v\ge0
  \end{cases}
\end{align*}
$$

  **$2^\circ$ の時** \quad $f(0)\ge0,\ f(S)\le0,\ f(C)\ge0$
  

$$
\begin{align*}
\iff\begin{cases}
  v\ge0 \\
  S^2-uS+v\le0 \\
  C^2-uC+v\ge0
  \end{cases}
\end{align*}
$$

  $\dfrac{\pi}{4}\le\theta<\dfrac{\pi}{2}$ の時，$C$ と $S$ を入れかえれば良いから，これらを図示して下図斜線部（境界含む）．

  

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1971/4/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $(u,v)$の軌跡の図示（斜線部）</figcaption>
</figure>

  この面積は，$0<\theta\le\dfrac{\pi}{4}$ の時
  

$$
\begin{align*}
S(\theta) = \int_0^{2S}\frac{1}{4}u^2du + \frac{1}{2}(C-S)(S^2+CS)-\frac{1}{2}CS^2 = \frac{2}{3}S^3+\frac{1}{2}S(C^2-S^2)-\frac{1}{2}CS^2
\end{align*}
$$

  $\dfrac{\pi}{4}<\theta<\dfrac{\pi}{2}$ の時，$S$ と $C$ を入れかえれば良く，$\theta=\dfrac{\pi}{4}$ の時，
  

$$
\begin{align*}
S(\theta)=\int_0^{\frac{\sqrt2}{2}}\frac{1}{4}u^2du - \frac{1}{2}\cdot\frac{\sqrt2}{2}\cdot\frac{1}{2}=\frac{\sqrt2}{24}
\end{align*}
$$

  で，これは $0<\theta<\dfrac{\pi}{4}$ の時の式に $\theta=\dfrac{\pi}{4}$ を代入したものにひとしい．
  

$$
\begin{align*}
S(\theta)=
  \begin{cases}
  \dfrac{1}{6}S^3+\dfrac{1}{2}SC^2-\dfrac{1}{2}CS^2 & \left(0<\theta\le\dfrac{\pi}{4}\right) \\[2mm]
  \dfrac{1}{6}C^3+\dfrac{1}{2}S^2C-\dfrac{1}{2}SC^2 & \left(\dfrac{\pi}{4}<\theta\le\dfrac{\pi}{2}\right)
  \end{cases}
\end{align*}
$$

2.  $0<\theta<\dfrac{\pi}{4}$ とする．
  

$$
\begin{align*}
S\left(\frac{\pi}{2}-\theta\right) = \frac{1}{6}S^3+\frac{1}{2}CS^2-\frac{1}{2}CS^2 \cdots
\end{align*}
$$

  たから示された．