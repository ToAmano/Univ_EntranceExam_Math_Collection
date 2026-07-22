---
university: "kyodai"
category: "kouki"
year: "1993"
question: "2"
type: "solution"
title: "KYODAI 1993 kouki Q2 (solution)"
---

## 【解】

  $f(x)=x^3-3ax$の一階微分は
  

$$
\begin{align*}
f'(x)=3(x^2-a)
\end{align*}
$$

  だから，$a\le 0$の時$f'(x)\ge 0$となり$f(x)$は単調増加である．
  よってこの時$f(x)=t$は一つしか解を持たず，題意の条件を満たさない．

  そこで以下
  

$$
\begin{align*}
a > 0
\end{align*}
$$

  として考える．
  $f(x)$の増減表は[表1](#1993-2:table:1)となる．

  

<figure id="1993-2:table:1" class="table-wrapper">

| $x$  |  $\cdots$  | $-\sqrt{a}$  |  $\cdots$  |  $\sqrt{a}$   |  $\cdots$  |
|:------:|:------------:|:--------------:|:------------:|:---------------:|:------------:|
| $f'$ |    $+$     |     $0$      |    $-$     |      $0$      |    $+$     |
| $f$  | $\nearrow$ | $2a\sqrt{a}$ | $\searrow$ | $-2a\sqrt{a}$ | $\nearrow$ |

  <figcaption>表 1: $f(x)$の増減表</figcaption>
</figure>

  従って，$y=f(x)$のグラフは[図1](#1993-2:fig:1)のようになる．
  

<figure id="1993-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1993/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=f(x)$の概形</figcaption>
</figure>

  $f(x)=t$ の解が $y=f(x)$ と $y=t$ の交点の $x$ 座標に対応していることから
  $f(x)=t$が三つの解を持つ条件は
  

$$
\begin{align*}
a>0 \land -2a\sqrt{a} < t < 2a\sqrt{a}
\end{align*}
$$

  である．$\cdots$(答)

  

  (2)
  (1)の考察から，$a \le 0$の時，$f(x)$は単調増加であるから，
  $g(x) = f(f(x))$も単調増加となり，$g(x)=0$が9つの異なる実数解を持つことはない．
  従って
  

$$
\begin{align*}
a > 0
\end{align*}
$$

  が必要．以下この条件で考える．

  $X=f(x)$とおくと，$g(x)=0$はすなわち$f(X)=0$であるから，
  $y=f(X)$のグラフを考えると，(1)と同様に[図2](#1993-2:fig:2)のようになる．
  

<figure id="1993-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1993/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $y=f(X)$の概形</figcaption>
</figure>

  $f(x)$ は3次関数であるから$f(x)=t$ をみたす $x$ は高々3つしかないこととグラフの概形から，
  $f(X)=0$の3つの解
  

$$
\begin{align*}
X = 0, \pm\sqrt{3a}
\end{align*}
$$

  にそれぞれ3つずつの $x$ が対応している時のみ, $f(f(x))=0$ は9つの異なる実数解を持つ.
  (1)の結果から，求める条件は$a>0$の元で
  

$$
\begin{align*}
& -2a\sqrt{a} < 0, \pm\sqrt{3a} < 2a\sqrt{a}\\\therefore& a > \frac{\sqrt{3}}{2}
\end{align*}
$$

  である．これは$a>0$を満たしているから，求める条件は
  

$$
\begin{align*}
a > \frac{\sqrt{3}}{2}
\end{align*}
$$

  である．$\cdots$(答)

  

  

## 【解説】