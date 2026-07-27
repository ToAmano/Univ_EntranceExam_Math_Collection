---
university: "titech"
category: "zenki"
year: "1981"
question: "3"
type: "solution"
title: "TITECH 1981 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$P,Q$が線分$OR$上にある時を，時刻の基準として$t=0$とする．又この時の$R$の座標が$(3,0)$となるようにして考える．すると時刻$t$での各々の座標は

$$
\begin{align*}
P(\cos t,\sin t),\quad Q(2\cos2t,2\sin2t),\quad R(3\cos3t,3\sin3t)
\end{align*}
$$

とかける．以下$S=\sin t,\ C=\cos t$とする．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1981/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点$P$，$Q$，$R$の位置関係</figcaption>
</figure>

$$
\begin{align*}
\overrightarrow{PQ}=\begin{pmatrix}2\cos2t-C\\2\sin2t-S\end{pmatrix},\qquad\overrightarrow{PR}=\begin{pmatrix}3\cos3t-C\\3\sin3t-S\end{pmatrix}
\end{align*}
$$

だからサラスの公式より，時刻$t$での$\triangle PQR$の面積$T(t)$として，

$$
\begin{align*}
2T(t)=\left|(3\sin3t-S)(2\cos2t-C)-(3\cos3t-C)(2\sin2t-S)\right|
\end{align*}
$$

$$
\begin{align*}
=\bigl|6\sin3t\cos2t-2S\cos2t-3C\sin3t+SC-(6\sin2t\cos3t-3S\cos3t-2C\sin2t+SC)\bigr|
\end{align*}
$$

$$
\begin{align*}
=\bigl|6(\sin3t\cos2t-\sin2t\cos3t)-3(C\sin3t-S\cos3t)-2(S\cos2t-C\sin2t)\bigr|
\end{align*}
$$

$$
\begin{align*}
=\bigl|6\sin t-3\sin2t-2\sin(-t)\bigr|
=\bigl|8S-3\sin2t\bigr|
=\bigl|8S-6SC\bigr|=|S|\,|8-6C| \quad\cdots\text{①}
\end{align*}
$$

①の中身を$f(t)$とすると，

$$
\begin{align*}
f'(t)=8C-6\cos2t=8C-6(2C^2-1)=2(-6C^2+4C+3)
\end{align*}
$$

から，下表をうる（$|S|,C$の周期性から，$0\le t\le\pi$で考えれば良い）．ただし，$\alpha=\dfrac{2-\sqrt{22}}{6}$である．

| $t$  | $0$ |              |            |              | $\pi$ |
|:------:|:-----:|:------------:|:----------:|:------------:|:-------:|
| $C$  | $1$ |              | $\alpha$ |              | $-1$  |
| $f'$ |       |    $+$     |   $0$    |    $-$     |         |
| $f$  | $0$ | $\nearrow$ |            | $\searrow$ |  $0$  |

ここで，$C=\alpha$の時，

$$
\begin{align*}
|S|=\sqrt{1-\alpha^2}=\frac16\sqrt{10+4\sqrt{22}}
\end{align*}
$$

だから，①に代入して

$$
\begin{align*}
\max T(t)=\frac{\sqrt{10+4\sqrt{22}}}{6}\left|4-3\cdot\frac{2-\sqrt{22}}{6}\right|
=\frac{(6+\sqrt{22})\sqrt{10+4\sqrt{22}}}{12}\left(=\frac{\sqrt{409+88\sqrt{22}}}{6}\right)
\end{align*}
$$