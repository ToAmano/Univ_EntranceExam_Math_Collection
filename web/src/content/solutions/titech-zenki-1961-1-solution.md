---
university: "titech"
category: "zenki"
year: "1961"
question: "1"
type: "solution"
title: "TITECH 1961 zenki Q1 (solution)"
---

## 【解】

定数$p$, $q$の条件

$$
\begin{align}
&0 < p,q \label{eq:1}\\&p+q = 1 \label{eq:2}
\end{align}
$$

に注意する．2変数$(A,B)$に対して方程式 

$$
\begin{align}
Ap + Bq = 1
\end{align}
$$

を考えると，[(式2)](#eq:2)より$(A,B)=(1,1)$は解であり，$AB$平面上でこの直線は$(1,1)$を通る．
これを図示したのが下図である．
[(式1)](#eq:1)より，この直線は$0\le A\le 1$および$0\le B\le 1$なる正方形（以下これを$T$とおく）と点$(1,1)$のみ共有することに注意する．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1961/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 直線の様子．</figcaption>
</figure>

さて，$A=\cos ax$, $B=\cos bx$とおいて題意のように方程式が$x=u,v$に対して成立すると仮定すると，この直線は二つの点

$$
\begin{align}
(A, B) = (\cos au, \cos bu), (\cos av, \cos bv)
\end{align}
$$

も通過する．ここで三角関数の性質から

$$
\begin{align}
-1 \le\cos au, \cos bu, \cos av, \cos bv \le 1
\end{align}
$$

なので，直線と$T$の共有点の議論から，$2$点が直線上であるためにはこの2点が$(1,1)$である必要がある．

したがって，

$$
\begin{align}
\begin{cases}
    \cos au = \cos av = 1 \\
    \cos bu = \cos bv = 1
  \end{cases}
\end{align}
$$

だから，整数 $k_1,k_2,k_3,k_4$ を用いて

$$
\begin{align}
\begin{cases}
    au = 2k_1 \pi, & bu = 2k_2 \pi \\
    av = 2k_3 \pi, & bv = 2k_4 \pi
  \end{cases}
\end{align}
$$

と書ける．

ここで$a \neq 0$ と仮定すると，$u = \dfrac{2k_1 \pi}{a}, v = \dfrac{2k_3 \pi}{a}$ から $\dfrac{v}{u} = \dfrac{k_3}{k_1} \in \mathbb{Q}$ となり$\dfrac{v}{u}$が無理数となる仮定と矛盾するから，背理法により$a = 0$である．

同様に $b = 0$ だから題意は示された．