---
university: "titech"
category: "zenki"
year: "1963"
question: "6"
type: "solution"
title: "TITECH 1963 zenki Q6 (solution)"
---

## 【解】

題意より$g(x) = \alpha x + \beta \quad (\alpha \ne 0, \, \alpha, \beta \in \mathbb{R})$ とおける．条件より

$$
\begin{align}
\alpha\int_0^a f(x) x \, dx + \beta\int_0^a f(x) \, dx = 0 \label{eq:1}
\end{align}
$$

が $\alpha \ne 0$ をみたす任意の $(\alpha, \beta)$ で成立するので[(式1)](#eq:1)が $\alpha, \beta$ についての恒等式となる．従って

$$
\begin{align}
\int_0^a f(x) \, dx &= 0 \label{eq:2}\\\int_0^a f(x) x \, dx &= 0 \label{eq:3}
\end{align}
$$

である．以下この条件を満たす$f(x)$について考える．

### $f(x)=0$が実数解を持たない時

$f(x) = 0$ が実解を持たない時$f(x)$ の符号は一定となり[(式2)](#eq:2)はみたされず不適．

### $f(x)=0$がただ一つの実数解を持つ時

$f(x)=0$がただ一つの実数解$t$を持つ時，$f(x) = (x-t)^2 \ge 0$と書けるが，これは[(式2)](#eq:2) を満たさず不適．

### $f(x)=0$が二つの異なる実数解を持つ時

$f(x)=0$が二つの異なる実数解を持つ時，$f(x) = (x-t)(x-s) \quad (t, s \in \mathbb{R}, t\neq s)$ と書ける．
「$t, s$ の少なくとも一方が $x \le 0, a \le x$ にある」と仮定する．
$t,s$の対称性からこれが $t$ だとして良い．この時 $g(x) = x - s$ とすると

$$
\begin{align}
f(x)g(x) = (x-t)(x-s)^2
\end{align}
$$

の符号は $[0, a]$ で一定であり題意の条件式をみたさず矛盾．
よって背理法より $0 < t, s < a$ となる．

以上3つの場合分けから，$f(x)=0$が二つの異なる実数解を$0<x<a$に持つことが示された．