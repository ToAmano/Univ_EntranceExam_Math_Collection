---
university: "titech"
category: "zenki"
year: "1995"
question: "2"
type: "solution"
title: "TITECH 1995 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

5点$A,B,C,D,E$を，$A$を原点，$AB$を$x$軸正方向にとり，$AB=BC=CD=DE=1$，各頂点での外角を$\theta$として配置する．すなわち

$$
\begin{align*}
A(0,0),\ B(1,0),\ C(1+\cos\theta,\sin\theta),
\end{align*}
$$

$$
\begin{align*}
D(1+\cos\theta+\cos2\theta,\ \sin\theta+\sin2\theta),
\end{align*}
$$

$$
\begin{align*}
E(1+\cos\theta+\cos2\theta+\cos3\theta,\ \sin\theta+\sin2\theta+\sin3\theta)
\end{align*}
$$

とおける．五角形$ABCDE$の面積$S$は，座標による面積公式（シューレースの公式）から

$$
\begin{align*}
2S=\sum(x_iy_{i+1}-x_{i+1}y_i)
\end{align*}
$$

であり，$A\to B$，$E\to A$の寄与は0，$B\to C$の寄与は$\sin\theta$，$C\to D$の寄与は

$$
\begin{align*}
(1+\cos\theta)(\sin\theta+\sin2\theta)-(1+\cos\theta+\cos2\theta)\sin\theta=\sin2\theta+(\cos\theta\sin2\theta-\cos2\theta\sin\theta)=\sin2\theta+\sin\theta
\end{align*}
$$

$D\to E$の寄与は

$$
\begin{align*}
(1+\cos\theta+\cos2\theta)\sin3\theta-(\sin\theta+\sin2\theta)\cos3\theta=\sin3\theta+\sin2\theta+\sin\theta
\end{align*}
$$

だから，

$$
\begin{align*}
2S=3\sin\theta+2\sin2\theta+\sin3\theta
\end{align*}
$$

$$
\begin{align*}
S=\frac12\sin3\theta+\sin2\theta+\frac32\sin\theta
\end{align*}
$$

$$
\begin{align*}
\frac{dS}{d\theta}=\frac32\cos3\theta+2\cos2\theta+\frac32\cos\theta
\end{align*}
$$

$$
\begin{align*}
=\frac32(\cos3\theta+\cos\theta)+2\cos2\theta=3\cos2\theta\cos\theta+2\cos2\theta=\cos2\theta(3\cos\theta+2)
\end{align*}
$$

$0<\theta<\pi/2$から$\cos\theta\in(0,1)$で$3\cos\theta+2>0$だから，$dS/d\theta$の符号は$\cos2\theta$と一致し，下表を得る．

| $\theta$ | $0$ |              | $\pi/4$ |              | $\pi/2$ |
|:----------:|:-----:|:------------:|:---------:|:------------:|:---------:|
|   $S'$   |       |    $+$     |   $0$   |    $-$     |           |
|   $S$    |       | $\nearrow$ |           | $\searrow$ |           |

従って，$S$は$\theta=\pi/4$の時，最大値

$$
\begin{align*}
S\left(\frac{\pi}{4}\right)=\frac32\cdot\frac{\sqrt2}{2}+1+\frac12\cdot\frac{\sqrt2}{2}=\sqrt2+1
\end{align*}
$$

をとる．