---
university: "titech"
category: "zenki"
year: "1979"
question: "4"
type: "solution"
title: "TITECH 1979 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$C: y=\log x$，$(\log x)'=\dfrac1x$ より，$C$ 上 $x=t$ での接線は

$$
\begin{align*}
\ell_t: y=\frac1t(x-t)+\log t
\end{align*}
$$

だから

$$
\begin{align*}
\ell_a: y=\frac1a(x-a)+\log a, \qquad\ell_c: y=\frac1c(x-c)+\log c
\end{align*}
$$

とおり，$\ell_a,\ell_c$ の交点 $R$ の $x$ 座標は

$$
\begin{align*}
x_R=\frac{ac(\log c-\log a)}{c-a}
\end{align*}
$$

である．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1979/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 接線$\ell_a$，$\ell_c$の交点$R$</figcaption>
</figure>

$$
\begin{align*}
S=\int_a^c\log x\,dx=\left[x(\log x-1)\right]_a^c=c(\log c-1)-a(\log a-1) \quad\cdots\text{①}
\end{align*}
$$

$P'Q'$ を底辺，$R$ の $y$ 座標を高さとする三角形として，$f(x)=x\log x$ とおくと，$T=\dfrac12(c-a)\cdot(R\text{の}y\text{座標})$ であり，接線の性質から

$$
\begin{align*}
T=\frac12\left(f(c)-f(a)\right)=\frac12(c\log c-a\log a) \quad\cdots\text{②}
\end{align*}
$$

①②から，もとめる比は

$$
\begin{align*}
S:T=\bigl\{c(\log c-1)-a(\log a-1)\bigr\}:\frac12(c\log c-a\log a)
\end{align*}
$$