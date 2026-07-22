---
university: "ukyoto"
category: "kouki"
year: "1989"
question: "3"
type: "solution"
title: "UKYOTO 1989 kouki Q3 (solution)"
---

## 【解】

    原点O$(0,0)$とおく．
    Bが第一象限にあるとして一般性を失わない．
    そこでB$(X,Y)$ $(X,Y>0)$とし，BからX軸に下した垂足M$(X,0)$とする．
    すると，直線ABの方程式は
    

$$
\begin{align*}
y = \frac{Y}{X+1}(x+1)
\end{align*}
$$

    となり，これと$y$軸の交点である$D$の座標は
    

$$
\begin{align*}
D(0, \frac{Y}{X+1})
\end{align*}
$$

    となる．この様子を[図1](#1989-3:fig:1)に示す．

    

<figure id="1989-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1989/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形ABCの様子</figcaption>
</figure>

    題意の条件$DB=2\sqrt{3} \iff DB^2=12$より，$X,Y>0$に注意して
    

$$
\begin{align*}
& 12 = X^2 + (Y - \frac{Y}{X+1})^2               \\\therefore& Y = \frac{X+1}{X}\sqrt{12-X^2}(0<X<2\sqrt{3})
\end{align*}
$$

    である．

    このもとで，Hと$\triangle ABC$の共通部分の面積$S(X)$を求める．
    $S(X)$は上辺OD，底辺BM，高さOMの台形の面積の2倍であるから，
    

$$
\begin{align*}
S(X)
         & = \frac{1}{2}\left(|OD|+|BM|\right)|OM|               \\& = 2 \cdot\frac{1}{2}(\frac{Y}{X+1} + Y) \cdot X     \\& = \frac{X(X+2)}{X+1}\cdot\frac{X+1}{X}\sqrt{12-X^2}\\& = (X+2)\sqrt{12-X^2}\\& = \sqrt{(X+2)^2(12-X^2)}\\& \equiv\sqrt{f(X)}
\end{align*}
$$

    と計算できる．

    以下$S(X)$の最大値を求める．
    $y=\sqrt{x}$は$x$の増加関数であるから，
    $f(X)$が最大の時 $S(X)$も最大である．
    $f(X)$の一階微分は
    

$$
\begin{align*}
f'(X)
         & = 2(X+2)(12-X^2) + (-2X)(X+2)^2 \\& = 2(X+2) [(12-X^2) - X(X+2) ]\\& = 2(X+2) (-2X^2-2X+12)          \\& = -4(X+2) (X^2+X-6)             \\& = -4(X+2) (X+3)(X-2)
\end{align*}
$$

    となり，$f(X)$の増減表は[表1](#1989-3:table:1)となる．
    

<figure id="1989-3:table:1" class="table-wrapper">

| $X$  |  0  |      …       |  2  |      …       | $2\sqrt{3}$ |
|:------:|:---:|:------------:|:---:|:------------:|:-------------:|
| $f'$ |     |    $+$     |  0  |    $-$     |               |
| $f$  |     | $\nearrow$ |     | $\searrow$ |               |

  <figcaption>表 1: $f(X)$の増減表</figcaption>
</figure>

    従って，$f(X)$よって$S(X)$は$X=2$で最大値をとり，
    

$$
\begin{align*}
\max S(X)=S(2)=8\sqrt{2}
\end{align*}
$$

    である．$\cdots$(答)

    
    

## 【解説】

    最大の時，$Y=3\sqrt{2}$である．