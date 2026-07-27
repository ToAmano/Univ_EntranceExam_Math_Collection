---
university: "titech"
category: "zenki"
year: "1982"
question: "3"
type: "solution"
title: "TITECH 1982 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$C: y=f(x)=x^4-6x^2$とおく．$f'(x)=4x^3-12x$より，$x=t$における$C$の接線$\ell$は

$$
\begin{align*}
\ell: y=(4t^3-12t)x-3t^4+6t^2
\end{align*}
$$

これが$P$を通る時，

$$
\begin{align*}
\beta=(4t^3-12t)\alpha-3t^4+6t^2 \quad\cdots\text{①}
\end{align*}
$$

$C$の2重接線は$y=-9$だけであるから，①が$t$に関して4実解を持てば良い．そこで，$g(t)=3t^4-4\alpha t^3-6t^2+12\alpha t+\beta$とおく．

$$
\begin{align*}
g'(t)=12t^3-12\alpha t^2-12t+12\alpha=12(t-\alpha)(t+1)(t-1)
\end{align*}
$$

より，$\alpha$において下表を得る．まず，$t=0$が解でないので$\beta\ne0$．

| $t$ |  | $\alpha$ |  | $-1$ |  | $1$ |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $g'$ | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $g$ | $\searrow$ |  | $\nearrow$ |  | $\searrow$ |  | $\nearrow$ |

\quad ($1^\circ\ \alpha\le-1$)

条件は $g(\alpha)<0,\ g(1)<0,\ g(-1)>0$

| $t$ |  | $-1$ |  | $\alpha$ |  | $1$ |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $g'$ | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $g$ | $\searrow$ |  | $\nearrow$ |  | $\searrow$ |  | $\nearrow$ |

\quad ($2^\circ\ -1\le\alpha\le1$)

条件は $g(-1)<0,\ g(1)<0,\ g(\alpha)>0$

| $t$ |  | $-1$ |  | $1$ |  | $\alpha$ |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $g'$ | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $g$ | $\searrow$ |  | $\nearrow$ |  | $\searrow$ |  | $\nearrow$ |

\quad ($3^\circ\ 1\le\alpha$)

条件は $g(-1)<0,\ g(\alpha)<0,\ g(1)>0$

ここで

$$
\begin{align*}
g(1)=\beta+8\alpha-3,\qquad g(-1)=\beta-8\alpha-3,\qquad g(\alpha)=-\alpha^4+6\alpha^2+\beta
\end{align*}
$$

である．$g(\alpha)=\beta-f(\alpha)$であり，$P$は$y>x^4-6x^2$の領域にあるから，常に$g(\alpha)>0$である．よって$1^\circ,3^\circ$（$g(\alpha)<0$を要求する）は起こりえず，$2^\circ$（$-1\le\alpha\le1$）のみが可能で，条件は$g(\alpha)>0$が自動的にみたされることから

$$
\begin{align*}
g(-1)<0\ \text{かつ}\ g(1)<0 \iff\beta<3-8\alpha\ \text{かつ}\ \beta<3+8\alpha
\end{align*}
$$

に帰着する．以上から，もとめる領域$D$は

$$
\begin{align*}
D=\left\{(\alpha,\beta)\ \middle|\ -1<\alpha<1,\ \ \alpha^4-6\alpha^2<\beta<3-8|\alpha|\right\}
\end{align*}
$$

であり，図示すると下図（境界含まず）．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1982/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 領域$D$の図示</figcaption>
</figure>