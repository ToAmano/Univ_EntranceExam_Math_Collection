---
university: "titech"
category: "zenki"
year: "1999"
question: "1"
type: "solution"
title: "TITECH 1999 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$a,b,p>0$とし，$t=\dfrac ba$（$t>0$）とおく．$C=A-B$とおくと

$$
\begin{align*}
C=a^p\left[(1+t)^p-2^{p-1}(1+t^p)\right]
\end{align*}
$$

であり，この符号は$g(t)=(1+t)^p-2^{p-1}(1+t^p)$の符号に等しい．

$$
\begin{align*}
g'(t)=p(1+t)^{p-1}-p\cdot2^{p-1}t^{p-1}=p\left[(1+t)^{p-1}-(2t)^{p-1}\right]
\end{align*}
$$

**$1^\circ$ $0<p<1$の時**

$p-1<0$だから$x\mapsto x^{p-1}$は（$x>0$で）単調減少．$0<t<1$では$1+t>2t$だから$(1+t)^{p-1}<(2t)^{p-1}$，よって$g'(t)<0$．$t>1$では$1+t<2t$だから$g'(t)>0$．$t=1$で$g'(1)=0$．

| $t$  | $0$ |              | $1$ |              |     |
|:------:|:-----:|:------------:|:-----:|:------------:|:---:|
| $g'$ |       |    $-$     | $0$ |    $+$     |     |
| $g$  |       | $\searrow$ | $0$ | $\nearrow$ |     |

（$g(1)=2^p-2^{p-1}\cdot2=0$）より，$g(t)\ge0$（$t>0$）で等号は$t=1$のみ．したがって$C\ge0$，すなわち$A\ge B$，等号は$a=b$の時のみ．

**$2^\circ$ $p=1$の時**

$A,B$の表式から明らかに$A=B$．

**$3^\circ$ $1<p$の時**

$p-1>0$だから$x\mapsto x^{p-1}$は単調増加．$1^\circ$と逆に，$0<t<1$で$1+t>2t$より$(1+t)^{p-1}>(2t)^{p-1}$，$g'(t)>0$．$t>1$で$g'(t)<0$．

| $t$  | $0$ |              | $1$ |              |     |
|:------:|:-----:|:------------:|:-----:|:------------:|:---:|
| $g'$ |       |    $+$     | $0$ |    $-$     |     |
| $g$  |       | $\nearrow$ | $0$ | $\searrow$ |     |

より$g(t)\le0$（$t>0$）で等号は$t=1$のみ．したがって$C\le0$，すなわち$A\le B$，等号は$a=b$の時のみ．

以上をまとめて，

$$
\begin{align*}
p=1\ \text{または}\ a=b\ \text{の時}\ A=B,\qquad
0<p<1\ \text{かつ}\ a\ne b\ \text{の時}\ A>B,\qquad
1<p\ \text{かつ}\ a\ne b\ \text{の時}\ A<B
\end{align*}
$$