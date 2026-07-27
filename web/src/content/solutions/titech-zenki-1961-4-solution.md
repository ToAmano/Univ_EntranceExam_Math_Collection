---
university: "titech"
category: "zenki"
year: "1961"
question: "4"
type: "solution"
title: "TITECH 1961 zenki Q4 (solution)"
---

## 【解】

$A(1,0), B(-1,0), C(t,0)$ ($0 \le t \le 1$) とおくと，与えられた図形は以下のようになる．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1961/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 題意の状況</figcaption>
</figure>

題意の2円の方程式は

$$
\begin{align}
\begin{cases}
    \left(x - \dfrac{1+t}{2}\right)^2 + y^2 = \left(\dfrac{1-t}{2}\right)^2 \\[8pt]
    \left(x - \dfrac{-1+t}{2}\right)^2 + y^2 = \left(\dfrac{1+t}{2}\right)^2
  \end{cases}\label{eq:1}
\end{align}
$$

で与えられる．対称性から，$P, Q$ の $y$ 座標が正である時のみを考えよう．
題意より，各円の中心から点$P, Q$に向かう角度は等しいので，これを図のように $\theta\, (0\le\theta\le \pi)$ とおく．
また簡単のため$c = \cos\theta, s = \sin\theta$ とおく．
点$P, Q$における円の接線はそれぞれ

$$
\begin{align}
\begin{cases}
    c\left(x - \dfrac{1+t}{2}\right) + sy = \dfrac{1-t}{2} \\
    c\left(x - \dfrac{-1+t}{2}\right) + sy = \dfrac{1+t}{2}
  \end{cases}
\end{align}
$$

で与えられる．これら二つの直線が等しいから定数項を比較して

$$
\begin{align}
& c \frac{1+t}{2} + \frac{1-t}{2} = c \frac{-1+t}{2} + \frac{1+t}{2}\\\therefore& c = t \label{eq:2}
\end{align}
$$

を得る．$0\le\theta\le\pi$より$s\ge 0$だから

$$
\begin{align}
s = \sqrt{1-t^2}
\end{align}
$$

であって，点$P, Q$の座標は

$$
\begin{align*}
P\left(\frac{1-t}{2}\cdot t + \frac{1+t}{2}, \frac{1+t}{2}\sqrt{1-t^2}\right)\\
  Q\left(\frac{1+t}{2}\cdot t + \frac{1-t}{2}, \frac{1-t}{2}\sqrt{1-t^2}\right)
\end{align*}
$$

と書ける．
よって線分 $PQ$ の中点 $M(X,Y)$ は

$$
\begin{align}
\begin{cases}
    X = \dfrac{1}{2}\left\{\dfrac{t^2+2t-1}{2} + \dfrac{-t^2+2t+1}{2}\right\} = t \\
    Y = \dfrac{1}{2}\left\{\dfrac{1+t}{2} + \dfrac{1-t}{2}\right\}\sqrt{1-t^2} = \dfrac{1}{2}\sqrt{1-t^2} = \dfrac{1}{2}\sqrt{1-X^2}
  \end{cases}
\end{align}
$$

と書ける．$P, Q$の$y$座標が負の場合は同様に

$$
\begin{align}
\begin{cases}
    X = t \\
    Y = -\dfrac{1}{2}\sqrt{1-X^2}
  \end{cases}
\end{align}
$$

だから，[(式2)](#eq:2)より$-1\le t\le 1$であることと合わせて

$$
\begin{align}
X^2 + 4Y^2 = 1
\end{align}
$$

が求める軌跡である．

## 【解説】

軌跡を求める問題で素直に立式していけば解ける．出てきた答えが正しそうなことは$t$の極限を考えると割と理解しやすい．
まず$t=1$の極限，すなわち右側の円が潰れる時は中点$M$は$(1,0)$であり，逆に$t=-1$の時は$(-1,0)$である．
一方$t=0$の時すなわち二つの円がそれぞれ半径$1/2$の時は$M$は$\left(0,\pm \dfrac{1}{2}\right)$である．
出てきた楕円の方程式はこれらの場合を全て満たしているから，そんなに外してなさそうだということがわかる．

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1961/4/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $M$の軌跡．</figcaption>
</figure>