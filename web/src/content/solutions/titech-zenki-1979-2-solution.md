---
university: "titech"
category: "zenki"
year: "1979"
question: "2"
type: "solution"
title: "TITECH 1979 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$s=\sin x$ とおく．$f(s)=s\left(1-\dfrac a2(1-s^2)\right)$ の $\max$ が1となる $a$ の値域をもとめれば良い．$f'(s)=\dfrac32as^2+\left(-\dfrac a2+1\right)$ より，$a$ によって下表を得る．

**ア．$a\ge0$ の時$1^\circ$ $-\dfrac a2+1\ge0\ \therefore\ 0\le a\le2$ の時**

$f'(s)\ge0$ から，$f(s)$ は $s=1$ で $\max\ 1$

**$2^\circ$ $1-\dfrac a2\le0\le a+1\ \therefore\ 2\le a$ の時**

| $s$  | $-1$ | $-\sqrt{\frac{a-2}{3a}}$ |     | $\sqrt{\frac{a-2}{3a}}$ | $1$ |
|:------:|:------:|:--------------------------:|:---:|:-------------------------:|:-----:|
| $f'$ |        |     $+$ $0$ $-$      |     |        $0$ $+$        |       |
| $f$  |        |   $\nearrow\ \searrow$   |     |       $\nearrow$        | $1$ |

（$f'(s)=0$ の時，$s^2=\dfrac{a-2}{3a}$，$\alpha=\sqrt{\dfrac{a-2}{3a}}$ とおく）

$$
\begin{align*}
f(-\alpha)=-\alpha\cdot\frac{2-a}{3}\ge0 \quad(\because 2\le a)
\end{align*}
$$

であり，$f(-\alpha)\le1$ の時 $(\alpha+1)(\alpha-8)\le0$ で，$2\le a\le8$ の時である． $\cdots$①

**イ．$a=0$ の時**

$f'(s)=1>0$ から，$\max f=f(1)=1$

**ウ．$a<0$ の時**（$1-\dfrac a2>0$）

**$1^\circ$ $a+1\le0\ \therefore\ a\le-1$ の時**

| $s$  | $-1$ |      $-\alpha$       |     |  $\alpha$  | $1$ |
|:------:|:------:|:----------------------:|:---:|:------------:|:-----:|
| $f'$ |        |      $-$ $+$       |     |    $-$     |       |
| $f$  | $-1$ | $\searrow\ \nearrow$ |     | $\searrow$ |       |

$$
\begin{align*}
f(\alpha)=\alpha\cdot\frac{2-a}{3}\le1
\end{align*}
$$

の時（①より）$a=-1$

**$2^\circ$ $a+1\ge0\ \therefore\ -1\le a<0$ の時**

$f'(s)>0$ から $s=1$ で $\max\ 1$

以上ア〜ウより，$-1\le a\le8$