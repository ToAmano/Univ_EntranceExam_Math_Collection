---
university: "titech"
category: "zenki"
year: "1996"
question: "4"
type: "solution"
title: "TITECH 1996 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$x\ge0$で$f'(x)>0\ \cdots\bigstar$，$f(0)=a\ (a>1)$

$P$での接線$\ell: y=f'(t)(x-t)+f(t)$，法線$m: y=-\dfrac1{f'(t)}(x-t)+f(t)$だから，

$$
\begin{align*}
Q\left(-\frac{f(t)}{f'(t)}+t,0\right), \qquad R(f(t)f'(t)+t,0)
\end{align*}
$$

とおける．$f(x)$は単調増加なことから，

$$
\begin{align*}
F(t)=f(t)f'(t)+\frac{f(t)}{f'(t)}
\end{align*}
$$

したがって，(ハ)から

$$
\begin{align*}
f'(t)+\frac1{f'(t)}=\frac{f(t)}{f'(t)}\quad\cdots\text{①}
\end{align*}
$$

**(1)** ①から

$$
\begin{align*}
\{f'(t)\}^2=f(t)-1 \quad\cdots\text{☆}
\end{align*}
$$

両辺$t$で微分して，

$$
\begin{align*}
2f'(t)f''(t)=f'(t)
\end{align*}
$$

$$
\begin{align*}
f''(t)=\frac12 \quad(\because f'(t)>0) \quad\cdots\text{②}
\end{align*}
$$

したがって，$f'(t)$は単調増加で，②の両辺積分して

$$
\begin{align*}
f'(t)=\frac12t+C \quad\cdots\text{③}
\end{align*}
$$

とおける．$\bigstar$から，$f'(0)=C>0\ \cdots$④である．③の両辺積分して

$$
\begin{align*}
f(t)=\frac14t^2+Ct+a \quad\cdots\text{⑤}
\end{align*}
$$

とおける（$\bigstar$，$f(0)=a$）．③，⑤を☆に代入

$$
\begin{align*}
\left(\frac12t+C\right)^2=\frac14t^2+Ct+a-1
\end{align*}
$$

$$
\begin{align*}
C^2=a-1
\end{align*}
$$

④から，$C=\sqrt{a-1}$である．$f(x)$の$[x,x+h]$に平均値の定理を適用して（微分可能かつ連続），

$$
\begin{align*}
f(x+h)-f(x)=f'(p)\cdot h
\end{align*}
$$

となる$p\ (x<p<x+h)$がある．②とあわせて

$$
\begin{align*}
f(x+h)-f(x)\ge\sqrt{a-1}\cdot h
\end{align*}
$$

**(2)** (1)から，$f(t)=\dfrac14t^2+\sqrt{a-1}\,t+a$である．$F(t)=\dfrac{\{f(t)\}^2}{f'(t)}$から

$$
\begin{align*}
F'(t)=\frac{2f(t)\{f'(t)\}^2-f''(t)\{f(t)\}^2}{\{f'(t)\}^2}=\frac{f(t)}{\{f'(t)\}^2}\left\{2\{f'(t)\}^2-f(t)f''(t)\right\}
\end{align*}
$$

の符号は$t\ge0$の時，$\{\ \}$部の符号に等しい．

$$
\begin{align*}
\{\ \}=2\left\{\frac12t+\sqrt{a-1}\right\}^2-\left(\frac14t^2+\sqrt{a-1}\,t+a\right)\cdot\frac12
\end{align*}
$$

$$
\begin{align*}
=2\left[\frac14t^2+\sqrt{a-1}\cdot t+(a-1)\right]-\frac18t^2-\frac12\sqrt{a-1}\cdot t-\frac12a
\end{align*}
$$

$$
\begin{align*}
=\frac38t^2+\frac32\sqrt{a-1}\cdot t+\frac32a-2\equiv g(t)
\end{align*}
$$

$g(t)=0$の2解を$\alpha,\beta$として，下表を得る（$\alpha<\beta$）．

**$1^\circ$ $\alpha<\beta\le0$つまり$\dfrac43\le a$の時**

$t\ge0$で$F(t)$は単調増加で，$\min F(t)=F(0)=\dfrac{a^2}{\sqrt{a-1}}$

**$2^\circ$ $\alpha<0\le\beta$つまり$1<a\le\dfrac43$の時**

| $t$  | $0$ |              | $\beta$ |              |     |
|:------:|:-----:|:------------:|:---------:|:------------:|:---:|
| $F'$ |       |    $-$     |   $0$   |    $+$     |     |
| $F$  |       | $\searrow$ |           | $\nearrow$ |     |

$g(\beta)=0$と☆から，$f'(\beta)^2=1/3$，$f(\beta)=4f'(\beta)^2=4/3$となり，

$$
\begin{align*}
\min F(t)=F(\beta)=\frac{16}9\sqrt3
\end{align*}
$$

以上まとめて，

$$
\begin{align*}
\min F(t)=
\begin{cases}
\dfrac{16}9\sqrt3 & \left(1<a\le\dfrac43\right) \\
\dfrac{a^2}{\sqrt{a-1}} & \left(\dfrac43\le a\right)
\end{cases}
\end{align*}
$$