---
university: "ukyoto"
category: "zenki"
year: "1981"
question: "1"
type: "solution"
title: "UKYOTO 1981 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解答] 題意の直線$\ell$は$y$軸と平行でないので、その傾きを$m$とする。$\ell$と$y=\frac{1}{4}x^2$の交点の$x$座標を$\left(\alpha, \frac{1}{4}\alpha^2\right)$, $\left(\beta, \frac{1}{4}\beta^2\right)$とおく。($\alpha < \beta$)
ここで、$\ell : y = m(x-4)+5$ だから、$\alpha, \beta$は次の2次方程式

$$
\begin{align*}
\frac{1}{4}x^2 - m(x-4) - 5 = 0 \cdots \text{①}
\end{align*}
$$

の2解である。(図形的に2解持つことは明らかである) $|PQ|^2$ を $f(m)$ とおく。

$$
\begin{align*}
f(m) = (\beta - \alpha)^2 + \left( \frac{1}{4}\beta^2 - \frac{1}{4}\alpha^2 \right)^2 = \left( 1 + \frac{1}{16}(\beta + \alpha)^2 \right)(\beta - \alpha)^2 \cdots \text{②}
\end{align*}
$$

①から、

$$
\begin{align*}
\alpha + \beta&= 4m \\\beta - \alpha&= 2 \sqrt{(2m)^2 - 16m + 20}\quad(\because\beta > \alpha) \\&= 4 \sqrt{m^2 - 4m + 5}
\end{align*}
$$

だから、②に代入して

$$
\begin{align*}
f(m) &= \left\{ 1 + \frac{1}{16}(4m)^2 \right\} 16(m^2 - 4m + 5) \\&= 16(1+m^2)(m^2 - 4m + 5)
\end{align*}
$$

この$\min$を求める。

$$
\begin{align*}
f'(m) &= 16 \left[ 2m(m^2-4m+5) + (1+m^2)(2m-4) \right]\\&= 16 \left[ 4m^3 - 12m^2 + 12m - 4 \right]\\&= 64 (m-1)^3
\end{align*}
$$

よって下表をうる。

| $m$  |  $\cdots$  | $1$ |  $\cdots$  |
|:------:|:------------:|:-----:|:------------:|
| $f'$ |    $-$     | $0$ |    $+$     |
| $f$  | $\searrow$ |       | $\nearrow$ |

$|PQ| \ge 0$ より、$|PQ|^2$ が$\min$のとき $|PQ|$ も$\min$であることから、もとめるカタムキは$1$である。