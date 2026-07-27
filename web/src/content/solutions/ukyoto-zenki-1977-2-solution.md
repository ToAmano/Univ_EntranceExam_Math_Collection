---
university: "ukyoto"
category: "zenki"
year: "1977"
question: "2"
type: "solution"
title: "UKYOTO 1977 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $a > 0$。$f(x) = x[a - (1+a^4)x^2]$ から、$y = f(x)$ と $x$ 軸の交点のうち、$x$ 座標正のもののそれを $c = \sqrt{\frac{a}{1+a^4}}$ である。

$$
\begin{align*}
S_a &= -a^4 \int_0^c x^3 dx + a \int_0^c x dx - \int_0^c x^3 dx \\\frac{d}{da} S_a &= -a^4 c^3 c' - 4a^3 \int_0^c x^3 dx + \int_0^c x dx + a c c' - c^3 c' \\&= -(a^4+1)c^3 c' + a c c' + \frac{1}{2}c^2 - a^3 c^4 \quad\dots\text{①}
\end{align*}
$$

又、$a - (a^4+1)c^2 = 0$ だから

$$
\begin{align*}
\frac{dS_a}{da}&= c^2 \left(\frac{1}{2} - \frac{a^4}{1+a^4}\right)\\&= \frac{-c^2}{2(1+a^4)}(a^2+1)(a^2-1)
\end{align*}
$$

より下表を得る。

| $a$  | $0$ |  $\dots$   | $1$ |  $\dots$   |     |
|:------:|:-----:|:------------:|:-----:|:------------:|:---:|
| $S'$ |       |    $+$     | $0$ |    $-$     |     |
| $S$  |       | $\nearrow$ |       | $\searrow$ |     |

よって $S_a$ を最大にする $a$ は $a = 1$。