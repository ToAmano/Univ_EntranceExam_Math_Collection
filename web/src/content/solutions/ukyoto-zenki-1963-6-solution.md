---
university: "ukyoto"
category: "zenki"
year: "1963"
question: "6"
type: "solution"
title: "UKYOTO 1963 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $f(x) = \int_0^x \cos t \, dt - 2 \int_0^x \sin t \, dt$ とおく。

$f'(x) = \cos x - 2 \sin x$ で、これは区間 $[0, \pi/4]$ で単調減少かつ、$f'(\pi/6) = 0$ より、下表を与える

| $x$  | $0$ |  $\dots$   | $\pi/6$ |  $\dots$   | $\pi/4$ |
|:------:|:-----:|:------------:|:---------:|:------------:|:---------:|
| $f'$ |       |    $+$     |   $0$   |    $-$     |           |
| $f$  |       | $\nearrow$ |           | $\searrow$ |           |

これより、$f(0)=0$, $f(\pi/4) = [\sin t + 2 \cos t]_0^{\pi/4} = \frac{3}{\sqrt{2}} - 2 > 0$ から、$f(x) > 0 \ (0 < x < \pi/4)$ なので、題意は示された \quad \text{同}