---
university: "titech"
category: "zenki"
year: "1969"
question: "1"
type: "solution"
title: "TITECH 1969 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解]

$$
\begin{align*}
\begin{cases}
a^2 - b^2 - c^2 > 0 & \dots \text{①} \\
ap < 0, \quad x > 0 & \dots \text{②} \\
ax + by + cz = p & \dots \text{③}
\end{cases}
\end{align*}
$$

$yz$平面で③の表す直線を $l$ と考える．まず，$(b, c) = (0, 0)$ とすると，$ax = p$ となるが，これは②に反する．よって $(b, c) \neq (0, 0)$ である．このもとで

$$
\begin{align*}
\min(y^2 + z^2) = \left(\frac{|p - ax|}{\sqrt{b^2 + c^2}}\right)^2 = \frac{(p - ax)^2}{b^2 + c^2}
\end{align*}
$$

だから，

$$
\begin{align*}
x^2 - (y^2 + z^2) &\le x^2 - \frac{(p - ax)^2}{b^2 + c^2} < x^2 - \frac{(p - ax)^2}{a^2}\quad(\because\text{①}) \\&= + 2 \frac{p}{a} x - \left(\frac{p}{a}\right)^2 = \left(\frac{p}{a}\right)\left( 2x - \frac{p}{a}\right) < 0 \quad(\because\text{②より}, \frac{p}{a} < 0, x > 0)
\end{align*}
$$

となり，

$$
\begin{align*}
x^2 - y^2 - z^2 < 0
\end{align*}
$$

である．