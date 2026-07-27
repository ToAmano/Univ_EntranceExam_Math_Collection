---
university: "ukyoto"
category: "zenki"
year: "1989"
question: "3"
type: "solution"
title: "UKYOTO 1989 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $f(x)$ はモニック多項式であるとしてよく、$f(x) = x^3 + ax^2 + bx + c$ とおける。
$f'(x) = 3x^2 + 2ax + b$ より、

$$
\begin{align*}
f(x) = \frac{1}{3}\left(x + \frac{1}{3}a\right)f'(x) + \left(\frac{2}{3}b - \frac{2}{9}a^2\right)x + (c - ab)
\end{align*}
$$

題意から、

$$
\begin{align*}
\frac{2}{3}b - \frac{2}{9}a^2 = 0 \quad \therefore \quad b = \frac{1}{3}a^2
\end{align*}
$$

だから

$$
\begin{align*}
f(x) = x^3 + ax^2 + \frac{1}{3}a^2 x + c
\end{align*}
$$

$$
\begin{align*}
f'(x) = 3x^2 + 2ax + \frac{1}{3}a^2 = 3\left(x + \frac{1}{3}a\right)^2 \ge 0
\end{align*}
$$

より、$f(x)$ は単調増加。これと $f(x) \to \pm\infty \ (x \to \pm\infty)$ から、$f(x) = 0$ をみたす実数 $x$ がただ1つある。($f$ は連続) //