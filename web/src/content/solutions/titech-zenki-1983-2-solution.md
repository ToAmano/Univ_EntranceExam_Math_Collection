---
university: "titech"
category: "zenki"
year: "1983"
question: "2"
type: "solution"
title: "TITECH 1983 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$0<t\le\dfrac12\ \cdots$①，$y=f(t)=\dfrac12\left\{t+\dfrac{x(2-x)}{t}\right\}$とおく．

$$
\begin{align*}
f'(t)=\frac12\left\{1+\frac{x(x-2)}{t^2}\right\}
\end{align*}
$$

であり，以下のようになる．

**$1^\circ$ $x\le0,\ 2\le x$の時**

$f'(t)>0$から，$\displaystyle\lim_{t\to0}f(t)<y\le f\left(\frac12\right)$

\textbf{$2^\circ$ $0<x<1-\dfrac{\sqrt3}{2},\ 1+\dfrac{\sqrt3}{2}<x<2$の時}

下表を得る．

| $t$  | $0$ |              | $\sqrt{x(2-x)}$ |              | $\frac12$ |
|:------:|:-----:|:------------:|:-----------------:|:------------:|:-----------:|
| $f'$ |       |    $-$     |       $0$       |    $+$     |             |
| $f$  |       | $\searrow$ |                   | $\nearrow$ |             |

したがって，$\displaystyle\lim_{t\to0}f(t)>f\left(\frac12\right)$から

$$
\begin{align*}
f(\sqrt{x(2-x)})\le f(t)<\lim_{t\to0}f(t)
\end{align*}
$$

\textbf{$3^\circ$ $1-\dfrac{\sqrt3}{2}\le x\le1+\dfrac{\sqrt3}{2}$の時}

$f'(t)<0$から $\displaystyle f\left(\frac12\right)\le y<\lim_{t\to0}f(t)$

ここで

$$
\begin{align*}
f\left(\frac12\right)=-x^2+2x+\frac14=-(x-1)^2+\frac54, \qquad f(\sqrt{x(2-x)})=\sqrt{x(2-x)}
\end{align*}
$$

図示して，下図斜線部（境界は$x=0,2$を除く）．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1983/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 条件を満たす領域の図示（斜線部）</figcaption>
</figure>

（$0<x<2$の部分は上側の曲線・放物線の下側包絡線から上方に無限に広がる領域，$x\le0,2\le x$の部分は放物線$y=-(x-1)^2+\frac54$の下方に無限に広がる領域．灰色部は図の枠内で切り取って表示している．）