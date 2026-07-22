---
university: "titech"
category: "kouki"
year: "2007"
question: "1"
type: "solution"
title: "TITECH 2007 kouki Q1 (solution)"
---

## 【解】

  表記の簡潔さのため
  

$$
\begin{align*}
f(x) = x^3 - n_1 x + (-1)^{n_2} n_3
\end{align*}
$$

  とおく．方程式$f(x)=0$について考える．

  
  (1)

  $f(x)$のグラフの概形を調べるため，一階微分を計算すると
  

$$
\begin{align*}
f'(x) = 3x^2 - n_1
\end{align*}
$$

  だから，$n_1>0$より$f(x)$の増減表は[表1](#2007-1:table:1)となる．

  

<figure id="2007-1:table:1" class="table-wrapper">

| $x$ | $-\infty$ | $\cdots$ | $-\sqrt{\frac{n_1}{3}}$ | $\cdots$ | $\sqrt{\frac{n_1}{3}}$ | $\cdots$ | $\infty$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $f'$ |  | $+$ | $0$ | $-$ | $0$ | $+$ |  |
| $f$ | ($-\infty$) | $\nearrow$ | 極大 | $\searrow$ | 極小 | $\nearrow$ | $(\infty)$ |

  <figcaption>表 1: $f(x)$の増減表</figcaption>
</figure>

  したがって，$f(x)=0$ が $3$ 実数解を持つ条件は
  

$$
\begin{align}
& f(\sqrt{n_1/3}) f(-\sqrt{n_1/3}) < 0                                                                          \nonumber\\\therefore& \left(-\frac{2n_1}{3}\sqrt{\frac{n_1}{3}} + (-1)^{n_2}n_3\right)\left(\frac{2n_1}{3}\sqrt{\frac{n_1}{3}} + (-1)^{n_2}n_3\right) < 0 \nonumber\\\therefore& -\frac{2}{3}n_1\sqrt{\frac{n_1}{3}} <(-1)^{n_2}n_3 < \frac{2}{3}n_1\sqrt{\frac{n_1}{3}}\nonumber\\\therefore& n_3 < \frac{2}{3}n_1\sqrt{\frac{n_1}{3}}\label{2007-1:eq:1}
\end{align}
$$

  と表せる．ただし，最終行で$n_3>0$を利用した．
  以下，[(式1)](#2007-1:eq:1)を満たす整数$(n_1,n_2,n_3)$を考える．
  まず，$n_2$については任意であり，$n_1$と$n_3$のみ考えれば良い．
  表記の簡潔さのため
  

$$
\begin{align*}
A & = \frac{2}{3}n_1\sqrt{\frac{n_1}{3}}
\end{align*}
$$

  とおくと，$n_1=1,2,\cdots,6$に対して値は以下のようになる．
  

<figure id="tab_2" class="table-wrapper">

| $n_1$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $A$ | $\frac{2}{9}\sqrt{3}$ | $\frac{4}{9}\sqrt{6}$ | $2$ | $\frac{16}{9}\sqrt{3}$ | $\frac{10}{9}\sqrt{15}$ | $4\sqrt{2}$ |

  <figcaption>表 2: $A$の$n_1$による値の変化</figcaption>
</figure>

  これらの値は
  

$$
\begin{align*}
\frac{2}{9}\sqrt{3} < 1 < \frac{4}{9}\sqrt{6} < 2 < 3 < \frac{16}{9}\sqrt{3} < 4 < \frac{10}{9}\sqrt{15} < 5 < 4\sqrt{2} < 6
\end{align*}
$$

  という大小関係にあるから，$n_1$ に対応して[(式1)](#2007-1:eq:1)を満たす$n_3$をリストアップすると[表3](#2007-1:table:2)のようになる．
  

<figure id="2007-1:table:2" class="table-wrapper">

|   $n_1$   | $1$ | $2$ | $3$ |    $4$     |    $5$     |    $6$     |
|:-----------:|:-----:|:-----:|:-----:|:------------:|:------------:|:------------:|
|   $n_3$   | 無し  | $1$ | $1$ | $1 \sim 3$ | $1 \sim 4$ | $1 \sim 5$ |
| $n_3$の数 | $0$ | $1$ | $1$ |    $3$     |    $4$     |    $5$     |

  <figcaption>表 3: [(式1)](#2007-1:eq:1)を満たす$n_1,n_3$の一覧</figcaption>
</figure>

  したがって求める確率は
  

$$
\begin{align*}
\frac{1}{6}\cdot\frac{1}{6}
    + \frac{1}{6}\cdot\frac{1}{6}
    + \frac{1}{6}\cdot\frac{3}{6}
    + \frac{1}{6}\cdot\frac{4}{6}
    + \frac{1}{6}\cdot\frac{5}{6} = \frac{7}{18}
\end{align*}
$$

  である．$\cdots$(答)

  
  (2) 題意の自然数解を $k\in\mathbb{N}$ とおくと，$f(k)=0$ゆえ
  

$$
\begin{align*}
k(k^2 - n_1) = (-1)^{n_2+1} n_3
\end{align*}
$$

  だから，両辺絶対値を取ると
  

$$
\begin{align*}
k \left|k^2 - n_1\right| = n_3
\end{align*}
$$

  である．すなわち$k$と$|k^2-n_1|$の積が$n_3$であることが必要である．
  まずはこの必要条件を満たす$(k,k^2-n_1)$を$n_3$に応じてリストアップする．
  $k$に対して，$n_1=1,2,\cdots,6$より
  

$$
\begin{align*}
|k^2-n_1| \le |k^2-1| \\
    |k^2-n_1| \le |k^2-6|
\end{align*}
$$

  であるから，この上限によって一定の制限があることに注意すると，一覧は[表4](#2007-1:table:3)となる．
  

<figure id="2007-1:table:3" class="table-wrapper">

|     $n_3$     |   $1$    |     $2$     |   $3$    |
|:---------------:|:----------:|:-------------:|:----------:|
| $(k,k^2-n_1)$ | $(1,-1)$ |  $(1,-2)$   | $(1,-3)$ |
|                 |            | $(2,\pm 1)$ |            |

  <figcaption>表 4: $k|k^2-n_1|=n_3$を満たす$(n_3,k,k^2-n_1)$の組</figcaption>
</figure>

  これを満たす$(k,n_1)$を一覧化すると
  

<div id="tab_5" class="table-wrapper">

|   $n_3$    |   $1$   |   $2$   |   $3$   |   $4$   |   $5$   |   $6$   |
|:------------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| $(k, n_1)$ | $(1,2)$ | $(1,3)$ | $(1,4)$ | $(1,5)$ | $(1,6)$ | $(2,1)$ |
|              |           | $(2,3)$ |           | $(2,2)$ |           |           |
|              |           | $(2,5)$ |           | $(2,6)$ |           |           |

</div>

  である．それぞれの組に対して$n_2$は3通り（偶数か奇数）が対応するので，$(n_1,n_2,n_3)$の場合の数は
  

$$
\begin{align*}
10*3 = 30
\end{align*}
$$

  通りであり，求める確率は
  

$$
\begin{align*}
\frac{30}{6^3} = \frac{5}{36}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】

  整数と確率の融合問題．
  おそらくあまり綺麗な解法は存在せず，地道な数え上げが必要な問題である．