---
university: "titech"
category: "zenki"
year: "1986"
question: "2"
type: "solution"
title: "TITECH 1986 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$E(t,-1-t,0)$，$F(u,u,-2u+2)$（$t,u\in\mathbb{R}$とおく）．正四面体の性質上から，$EF$は$\ell_1,\ell_2$と垂直である．

$$
\begin{align*}
\overrightarrow{EF}=\begin{pmatrix}u-t\\u+t+1\\-2u+2\end{pmatrix}
\end{align*}
$$

だから

$$
\begin{align*}
\overrightarrow{EF}\cdot\begin{pmatrix}-1\\1\\0\end{pmatrix}=0, \qquad\overrightarrow{EF}\cdot\begin{pmatrix}1\\1\\-2\end{pmatrix}=0
\end{align*}
$$

$$
\begin{align*}
\begin{cases}
(u-t)-(u+t+1)=0 \\
(u-t)+(u+t+1)+4(u-1)=0
\end{cases}
\end{align*}
$$

$$
\begin{align*}
\begin{cases}
t=-\dfrac12 \\
u=\dfrac12
\end{cases}
\end{align*}
$$

となり，

$$
\begin{align*}
E\left(-\frac12,-\frac12,0\right), \qquad F\left(\frac12,\frac12,1\right)
\end{align*}
$$

**(2)** 1辺の長さを$d$とすると，正四面体の面（正三角形）の中線の長さから$BF=\dfrac{\sqrt3}{2}d$．だから$\triangle FEB$にピタゴラスを用いて，

$$
\begin{align*}
\left(\frac{\sqrt3}{2}d\right)^2=\overline{EF}^2+\left(\frac{d}{2}\right)^2
\end{align*}
$$

$$
\begin{align*}
\overline{EF}=\frac{\sqrt2}{2}d \quad(\because d,\overline{EF}>0)
\end{align*}
$$

一方，(1)から$\overline{EF}=\sqrt3$だから，

$$
\begin{align*}
d=\sqrt6
\end{align*}
$$

**(3)** $A(p,-1-p,0)$とおくと，

$$
\begin{align*}
\overline{AF}=\sqrt{\left(p-\frac12\right)^2+\left(-p-\frac32\right)^2+1}=\sqrt{2p^2+2p+\frac72}
\end{align*}
$$

ここで，(2)から$\overline{AF}=\dfrac{\sqrt3}{2}d=\dfrac32\sqrt2$だから，といて

$$
\begin{align*}
p=\frac12(-1\pm\sqrt3)
\end{align*}
$$

題意から複号正に対応するのが$A$で，

$$
\begin{align*}
A\left(\frac{-1+\sqrt3}{2},\frac{-1-\sqrt3}{2},0\right)
\end{align*}
$$