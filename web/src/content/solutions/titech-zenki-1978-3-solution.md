---
university: "titech"
category: "zenki"
year: "1978"
question: "3"
type: "solution"
title: "TITECH 1978 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

1.  $L$ の方程式は $\dfrac{r}{\sqrt2}x+\dfrac{r}{\sqrt2}y=r^2$ $\therefore x+y=\sqrt2r$ だから，方向ベクトル $\vec v=\begin{pmatrix}1\\-1\end{pmatrix}$ で，$P$ が $L$ 上の点の時，$a+b=\sqrt2r$ で，これは $P'(b,a)$ が $L$ 上にあることも意味する．したがって，$t$ を実数として
  

$$
\begin{align*}
\begin{pmatrix}c\\d\end{pmatrix}=\begin{pmatrix}b\\a\end{pmatrix}+(a-b)t\begin{pmatrix}1\\-1\end{pmatrix}
\end{align*}
$$

  と表せる．（$\because P\ne\left(\dfrac{r}{\sqrt2},\dfrac{r}{\sqrt2}\right)$ より，$a\ne b$）したがって，
  

$$
\begin{align*}
\begin{cases}
  c=b+(a-b)t=at+(1-t)b \\
  d=a+(a-b)t(-1)=(1-t)a+tb
  \end{cases}
\end{align*}
$$

  と表せる．

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1978/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点$P$，$P'$と直線$y=x$の関係</figcaption>
</figure>

2.  $\begin{pmatrix}c\\d\end{pmatrix}=t\begin{pmatrix}a\\b\end{pmatrix}+(1-t)\begin{pmatrix}b\\a\end{pmatrix}$ より，$(c,d)$ は $\overline{PP'}$ 上にある時，$P'P$ の $t:1-t$ 内分点である．これと接点 $R$ が $\overline{PP'}$ の中点であることから，$t$ の条件は
  

$$
\begin{align*}
\frac12\le t\le1
\end{align*}
$$