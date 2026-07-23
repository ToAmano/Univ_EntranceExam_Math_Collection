---
university: "utokyo"
category: "zenki"
year: "2005"
question: "6"
type: "solution"
title: "UTOKYO 2005 zenki Q6 (solution)"
---

\input{macros}
     \begin{oframed}
     $r$を正の実数とする．$xyz$空間において，
          

$$
\begin{align*}
&x^2+y^2\le r^2 \\&y^2+z^2\ge r^2 \\&z^2+x^2\le r^2
\end{align*}
$$

     を満たす点全体からなる立体の体積を求めよ．
     \end{oframed}

## 【解】

 各軸を$1/r$倍して考える．題意の体積を$V$とする．
          

$$
\begin{align*}
\begin{cases}
               &x^2+y^2\le1 \\
               &y^2+z^2\ge1 \\
               &z^2+x^2\le1 
               \end{cases}
\end{align*}
$$

を満たす立体の体積を$V'$とすると，
     

$$
\begin{align}
V=r^3V'\label{1}
\end{align}
$$

である．対称性から，さらに$x\ge0$，$0\le y\le z$を満たす部分の体積$v$とすると，     
     

$$
\begin{align}
V'=16v\label{2}
\end{align}
$$

である．

\1 ただし，$0\le\theta\le\pi/4$である．$x=s$での切断面は，
          

$$
\begin{align*}
\begin{cases}
               &y^2\le1-s^2=c^2 \\ 
               &y^2+z^2\ge1 \\
               &z^2\le1-s^2=c^2 
               \end{cases}
\end{align*}
$$

     
であって，下図である．
     
     \scalebox{1}{\input{ut-05-6p}}
     
この平面での$v$の面積$S(\theta)$として，
     

$$
\begin{align*}
S(\theta)=\frac{1}{2}(c-s)c-\frac{1}{2}\left(\frac{\pi}{4}-\theta\right)
\end{align*}
$$

であるから，
     

$$
\begin{align*}
v&=\int_0^{\sqrt{2}/2}S(\theta)ds \\&=\int_0^{\pi/4}S(\theta)\frac{ds}{d\theta}d\theta\\&=\frac{1}{2}\int_0^{\pi/4}\left\{(c-s)c^2-c\left(\frac{\pi}{4}-\theta\right)\right\}d\theta
\end{align*}
$$

各項計算して，
     

$$
\begin{align*}
&\int_0^{\pi/4}c^3d\theta=\left[s-\frac{1}{3}s^3\right]_0^{\pi/4}\\&=\frac{5\sqrt{2}}{12}\\&\int_0^{\pi/4}sc^2d\theta=\frac{-1}{3}[c^3]_0^{\pi/4}\\&=\frac{1}{3}\left(1-\frac{\sqrt{2}}{4}\right)\\&\int_0^{\pi/4}cd\theta=\frac{\sqrt{2}}{2}\\&\int_0^{\pi/4}c\theta d\theta=[s\theta+c]_0^{\pi/4}=\frac{\sqrt{2}\pi}{8}+\frac{\sqrt{2}}{2}-1
\end{align*}
$$

であるから，代入して，
     

$$
\begin{align*}
v&=\frac{1}{2}\left[\frac{5\sqrt{2}}{12}-\frac{1}{3}\left(1-\frac{\sqrt{2}}{4}\right)-\frac{\sqrt{2}\pi}{8}+\frac{\sqrt{2}\pi}{8}+
     \frac{\sqrt{2}}{2}-1 \right]\\&=\frac{1}{2}\left(\sqrt{2}-\frac{4}{3}\right)
\end{align*}
$$

これを[1](#1)，[2](#2)に代入して，
     

$$
\begin{align*}
V=8\left(\sqrt{2}-\frac{4}{3}\right)r^3
\end{align*}
$$

である．$\cdots$(答)