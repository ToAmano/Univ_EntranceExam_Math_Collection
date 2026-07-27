---
university: "titech"
category: "zenki"
year: "1974"
question: "1"
type: "solution"
title: "TITECH 1974 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$f(x)=\dfrac{3}{4}x^2-3x+4=\dfrac{3}{4}(x-2)^2+1$ とおく．
$y=x$ と $y=f(x)$ の交点は $x=\dfrac{4}{3},4$ でグラフは右図．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1974/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=x$と$y=f(x)$のグラフ</figcaption>
</figure>

したがって，$4<b$ の時，$f(b)>b$ で不適．次に $[a,b]$ に $2$ を含むかで場合分けする．

**$1^\circ\ a\le2\le b$ の時**

$[a,b]$ での $\min f=f(2)=1$ だから，$a=1$ である．$f(1)=\dfrac{7}{4}$ だから $b=4$ のみ適する．

**$2^\circ\ a\ge2$ の時**

$[a,b]$ では $f(a)\le f(x)\le f(b)$ だから，$f(a)=a$ かつ $f(b)=b$ とならば良いが，図からこれをみたす $(a,b)$ はない．

**$3^\circ\ b<2$ の時**

$[a,b]$ では $f(b)\le f(x)\le f(a)$ だから $f(b)=a$ かつ $f(a)=b$ となる．

$$
\begin{align*}
f(b)-f(a)=\frac{3}{4}(b^2-a^2)-3(b-a)=(a-b)
\end{align*}
$$

$a\ne b$ から

$$
\begin{align*}
\frac{3}{4}(a+b)-3=-1 \quad\therefore\ a+b=\frac{8}{3}
\end{align*}
$$

これを $f(a)=b$ に代入すると $a=b=\dfrac{4}{3}$ となり，$a=b$ に反し矛盾．

以上から，もとめるのは $(a,b)=(1,4)$ である．