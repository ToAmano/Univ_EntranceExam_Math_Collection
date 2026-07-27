---
university: "titech"
category: "zenki"
year: "1994"
question: "5"
type: "solution"
title: "TITECH 1994 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$f(x)=x^2$，$g(x)=-x^2-16x-65=-(x+8)^2-1$とおく．$P,Q$の$x$座標を$\alpha$，$\beta-8$とする．

$$
\begin{align*}
\overrightarrow{PQ}=\begin{pmatrix}\beta-8\\g(\beta-8)\end{pmatrix}-\begin{pmatrix}\alpha\\\alpha^2\end{pmatrix}=\begin{pmatrix}\beta-\alpha-8\\-\alpha^2-\beta^2-1\end{pmatrix}
\end{align*}
$$

だから，$a=\beta-\alpha,\ b=\beta+\alpha$とすると

$$
\begin{align*}
\alpha^2+\beta^2=\frac{a^2+b^2}{2}
\end{align*}
$$

に注意して

$$
\begin{align*}
|\overrightarrow{PQ}|^2=(a-8)^2+\left(\frac{a^2+b^2}{2}+1\right)^2
\end{align*}
$$

$$
\begin{align*}
=\frac14\left\{b^2+(a^2+2)\right\}^2+(a-8)^2 \quad\cdots\text{①}
\end{align*}
$$

$\alpha,\beta$は$x$の2次式$x^2-bx+\dfrac{b^2-a^2}{4}=0$の2実解だから，判別式$D$として，

$$
\begin{align*}
D=b^2-(b^2-a^2)\ge0 \quad\therefore\ a^2\ge0
\end{align*}
$$

これは$a\in\mathbb{R}$から常に成立．よって①の$\min$をかんがえれば良い．$a$を固定すると$b=0$で$\min$で，

$$
\begin{align*}
\min|\overrightarrow{PQ}|^2=\frac14(a^2+2)^2+(a-8)^2\ (\equiv f(a))
\end{align*}
$$

とすると

$$
\begin{align*}
f'(a)=\frac12(a^2+2)\cdot2a+2(a-8)=a^3+4a-16=(a-2)(a^2+2a+8)
\end{align*}
$$

から下表をうる．

| $a$  |     |              | $2$ |              |     |
|:------:|:---:|:------------:|:-----:|:------------:|:---:|
| $f'$ |     |    $-$     | $0$ |    $+$     |     |
| $f$  |     | $\searrow$ |       | $\nearrow$ |     |

よって$a=2$で$|\overrightarrow{PQ}|^2$は$\min$をとる．$|\overrightarrow{PQ}|\ge0$から，この時$|\overrightarrow{PQ}|$も最小で，

$$
\begin{align*}
\min|\overrightarrow{PQ}|=\sqrt{45}=3\sqrt5
\end{align*}
$$