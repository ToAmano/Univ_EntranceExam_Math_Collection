---
university: "titech"
category: "zenki"
year: "1985"
question: "3"
type: "solution"
title: "TITECH 1985 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

円$O_k\ (k=1,2,\cdots,5)$の半径を$r_k$とすると，題意から

$$
\begin{align*}
r_1=1, \qquad r_2=a, \qquad r_3=r_4=\frac{1-a}{2}
\end{align*}
$$

である．又，$\angle DAB=\theta$とおく（$0<\theta<\pi/2\ \cdots$①）．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1985/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円$O_1\sim O_5$の配置</figcaption>
</figure>

$O_3$と$O_4$の接点を$E$とする．$E$は$AD$，$BC$の交点であることに注意する．

**(1)** ピタゴラスの定理から

$$
\begin{align*}
AE=\sqrt{\left(a+\frac{1-a}{2}\right)^2-\left(\frac{1-a}{2}\right)^2}=\sqrt{a}\quad\cdots *
\end{align*}
$$

$$
\begin{align*}
DE=\sqrt{\left(r_5+\frac{1-a}{2}\right)^2-\left(\frac{1-a}{2}\right)^2}=\sqrt{r_5^2+(1-a)r_5}
\end{align*}
$$

したがって，$r_1=1$を2通りで表して

$$
\begin{align*}
1=AE+DE+r_5=\sqrt a+\sqrt{r_5^2+(1-a)r_5}+r_5
\end{align*}
$$

$$
\begin{align*}
(1-\sqrt a)-r_5=\sqrt{r_5^2+(1-a)r_5}
\end{align*}
$$

$$
\begin{align*}
r_5^2-2(1-\sqrt a)r_5+(1-\sqrt a)^2=r_5^2+(1-a)r_5 \quad\cdots\text{②}, \qquad(1-\sqrt a)-r_5\ge0\quad\cdots\text{③}
\end{align*}
$$

②から

$$
\begin{align*}
r_5=\frac{(1-\sqrt a)^2}{2(1-\sqrt a)+(1-a)}=\frac{(1-\sqrt a)^2}{3-a-2\sqrt a}
\end{align*}
$$

である．$t=\sqrt a\ (0<t<1,\ \cdots$④$)$とおいて③に代入

$$
\begin{align*}
(1-t)+\frac{(1-t)^2}{t^2+2t-3}=(1-t)-\frac{1-t}{t+3}=\frac{(1-t)(t+2)}{t+3}\ge0\quad(\because④)
\end{align*}
$$

から，この$t$は③をみたして良い．この時，$*$から

$$
\begin{align*}
DE=\sqrt{\frac{1-t}{t+3}\left(\frac{1-t}{t+3}+1-t\right)}=\sqrt{\frac{(1-t)^2}{(t+3)^2}(t+2)^2}=\frac{(1-t)(t+2)}{t+3}\quad(\because④)
\end{align*}
$$

$$
\begin{align*}
AE=t
\end{align*}
$$

だから

$$
\begin{align*}
S(a)=\triangle ABD+\triangle ACD=AD\cdot BE=\left(t+\frac{(1-t)(t+2)}{t+3}\right)\cdot\frac{1-t^2}{2}
\end{align*}
$$

$$
\begin{align*}
=\frac{(t+1)(1-t)}{t+3}\cdot\frac{(\sqrt a+1)(1-\sqrt a)}{\sqrt a+3}
\end{align*}
$$

**(2)** $f(t)=\dfrac{(t+1)(1-t)^2}{t+3}$とおく．$f(t)$の$0<t<1$での最大値をもとめれば良い．

$p=t+3$とおくと，$3<p<4$で，

$$
\begin{align*}
f(t)=\frac{(p-2)^2(4-p)}{p}
\end{align*}
$$

$$
\begin{align*}
\frac{df}{dp}=\frac{p[2(p-2)(4-p)-(p-2)^2]-(p-2)^2(4-p)}{p^2}=\frac{-2(p-2)(p^2-2p-4)}{p^2}
\end{align*}
$$

より，下表をうる．

| $p$  | $3$ |              | $1+\sqrt5$ |              | $4$ |
|:------:|:-----:|:------------:|:------------:|:------------:|:-----:|
| $f'$ |       |    $+$     |    $0$     |    $-$     |       |
| $f$  |       | $\nearrow$ |              | $\searrow$ |       |

したがって，$p=1+\sqrt5$で最大値$10\sqrt5-22$をとる．