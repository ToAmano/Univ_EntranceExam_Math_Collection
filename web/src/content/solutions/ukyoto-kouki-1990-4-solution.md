---
university: "ukyoto"
category: "kouki"
year: "1990"
question: "4"
type: "solution"
title: "UKYOTO 1990 kouki Q4 (solution)"
---

## 【解】

  題意より，時刻 $t\, (t>0)$ での P,Q,R の座標は
  

$$
\begin{align*}
& P(1,0,0) \\& Q(2,t,0) \\& R(2,2,t)
\end{align*}
$$

  だから
  

$$
\begin{align*}
\vec{\text{PQ}} = \begin{pmatrix}1 \\ t \\ 0 \end{pmatrix}, \quad\vec{\text{PR}} = \begin{pmatrix}1 \\ 2 \\ t\end{pmatrix}
\end{align*}
$$

  より
  

$$
\begin{align*}
|\vec{\text{PQ}}|^2                   & = (2-t)^2+t^2    = 1+t^2 \\
    |\vec{\text{PR}}|^2                   & = (2-t)^2+2^2+t^2= 5+t^2 \\\vec{\text{PQ}}\cdot\vec{\text{PR}}& = (2-t)^2+2t     = 1+2t
\end{align*}
$$

  だから，三角形PQRの面積は
  

$$
\begin{align*}
S
     & = \frac{1}{2}\sqrt{|\vec{\text{PQ}}|^2 |\vec{\text{PR}}|^2 - (\vec{\text{PQ}} \cdot \vec{\text{PR}})^2}\\& = \frac{1}{2}\sqrt{\left[(2-t)^2+t^2\right]\left[(2-t)^2+2^2+t^2\right] - \left[(2-t)^2+2t\right]^2}\\& = \frac{1}{2}\sqrt{\left[(2-t)^2+t^2\right]\left[2(2-t)^2+4t\right] - \left[(2-t)^2+2t\right]^2}\\& = \frac{1}{2}\sqrt{(2-t)^4+2t^2(2-t)^2+4t^3-4t^2}\\& = \frac{1}{2}\sqrt{3t^4-12t^3+28t^2-32t+16}\\& \equiv\frac{1}{2}\sqrt{f(t)}
\end{align*}
$$

  である．$\sqrt{x}$は$x$について単調増加だから，$f(t)$が最小のとき$S$も最小である．
  従って，以下$f(t)$を最小にする$t$を求める．
  

$$
\begin{align*}
f'(t)
     & = 12t^3-36t^2+56t-32 \\& = 4(3t^3-9t^2+14t-8) \\& = 4(t-1)(3t^2-6t+8)  \\& = 4(t-1)(3(t-1)^2+5)
\end{align*}
$$

  より，$f(t)$の増減表は[表1](#1990-4:table:1)となる．

  

<figure id="1990-4:table:1" class="table-wrapper">

|   $t$   | $0$ |  $\dots$   | $1$ |  $\dots$   |     |
|:---------:|:-----:|:------------:|:-----:|:------------:|:---:|
| $f'(t)$ |       |    $-$     | $0$ |    $+$     |     |
| $f(t)$  |       | $\searrow$ |       | $\nearrow$ |     |

  <figcaption>表 1: $f(t)$の増減表</figcaption>
</figure>

  よって $t=1$ で $S$ は最小となるから，求める$t$は
  

$$
\begin{align*}
t = 1
\end{align*}
$$

  である．$\cdots$(答)

  

## 【解説】