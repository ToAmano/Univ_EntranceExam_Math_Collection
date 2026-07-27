---
university: "titech"
category: "zenki"
year: "2005"
question: "3"
type: "solution"
title: "TITECH 2005 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$D$の中心は$C:x^2+y^2=1$上にあるから，$C=\cos\theta,\ S=\sin\theta$として$P(C,S,0)$（$0\le\theta<2\pi$）とかける．$D$のある平面は常に$(0,1,0)$と直交するので，平面$y=S$内にあり

$$
\begin{align*}
D:\ (x-C)^2+z^2\le1,\quad y=S
\end{align*}
$$

平面$y=k$（$-1\le k\le1$）による断面を考える．$\sin\theta=k$をみたす$\theta\in[0,\pi]$に対応して$\cos\theta=\pm\sqrt{1-k^2}$の2値をとり得るが，対称性からどちらも同じ形の断面を与える．$c=\sqrt{1-k^2}\ (=|\cos\theta|)$とすると，断面は$xz$平面内の2つの単位円板（中心$(\pm c,0)$）の和集合であり，この面積を$V(\theta)$とおく（$c=\cos\theta$，$0\le\theta\le\pi/2$として良い）．

2円板の共通部分（レンズ形）の面積は，対称性から

$$
\begin{align*}
4\int_c^1\sqrt{1-x^2}\,dx
\end{align*}
$$

に等しいから

$$
\begin{align*}
V(\theta)=2\pi-4\int_c^1\sqrt{1-x^2}\,dx
\end{align*}
$$

$x=\cos\alpha$（$\alpha:\theta\to0$として$x:c\to1$）とおくと，$dx=-\sin\alpha\,d\alpha$，$\sqrt{1-x^2}=\sin\alpha$（$0\le\alpha\le\pi/2$）だから

$$
\begin{align*}
\int_c^1\sqrt{1-x^2}\,dx=\int_0^\theta\sin^2\alpha\,d\alpha=\left[\frac\alpha2-\frac{\sin2\alpha}4\right]_0^\theta=\frac\theta2-\frac{\sin2\theta}4
\end{align*}
$$

したがって

$$
\begin{align*}
V(\theta)=2\pi-4\left(\frac\theta2-\frac{\sin2\theta}4\right)=2\pi+\sin2\theta-2\theta
\end{align*}
$$

もとめる体積$V$は，$y=\sin\theta$の対称性（$0\le\theta\le\pi/2$で$y:0\to1$，残りは対称）から

$$
\begin{align*}
\frac V2=\int_0^1V(\theta)\,dy=\int_0^{\pi/2}V(\theta)\cdot\frac{dy}{d\theta}\,d\theta=\int_0^{\pi/2}(2\pi+\sin2\theta-2\theta)\cos\theta\,d\theta
\end{align*}
$$

$$
\begin{align*}
=\int_0^{\pi/2}\bigl(2\pi C+C\sin2\theta-2C\theta\bigr)d\theta\quad(C=\cos\theta) \quad\cdots\text{①}
\end{align*}
$$

各項を計算する．

$$
\begin{align*}
\int_0^{\pi/2}C\,d\theta=\bigl[\sin\theta\bigr]_0^{\pi/2}=1
\end{align*}
$$

$$
\begin{align*}
\int_0^{\pi/2}C\theta\,d\theta=\bigl[\theta\sin\theta+\cos\theta\bigr]_0^{\pi/2}=\left(\frac\pi2+0\right)-(0+1)=\frac\pi2-1
\end{align*}
$$

$$
\begin{align*}
\int_0^{\pi/2}C\sin2\theta\,d\theta=2\int_0^{\pi/2}\sin\theta\cos^2\theta\,d\theta=2\left[-\frac{\cos^3\theta}3\right]_0^{\pi/2}=2\cdot\frac13=\frac23
\end{align*}
$$

①に代入して

$$
\begin{align*}
\frac V2=2\pi\cdot1+\frac23-2\left(\frac\pi2-1\right)=2\pi+\frac23-\pi+2=\pi+\frac83
\end{align*}
$$

$$
\begin{align*}
\therefore\ V=2\pi+\frac{16}3
\end{align*}
$$