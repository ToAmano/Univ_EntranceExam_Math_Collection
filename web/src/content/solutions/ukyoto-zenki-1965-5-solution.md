---
university: "ukyoto"
category: "zenki"
year: "1965"
question: "5"
type: "solution"
title: "UKYOTO 1965 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $g(x) = \dfrac{f(x) - f(a)}{x - a}$ とおく。\\
$\displaystyle \lim_{x \to a+0} g(x)$ と $\displaystyle \lim_{x \to a-0} g(x)$ が一致する時、$\displaystyle \lim_{x \to a} g(x)$ を $f(x)$ の $x = a$ における微分係数という。

### (ア)

 $f(x) = \dfrac{1}{x^3}$, $g(x) = \dfrac{\frac{1}{x^3} - 1}{x - 1}$ の時、

$$
\begin{align*}
g(x) = \frac{1 - x^3}{x^3} \frac{1}{x - 1} = \frac{-1}{x^3}(x^2 + x + 1)
\end{align*}
$$

より、

$$
\begin{align*}
\lim_{x \to 1+0} g(x) = \lim_{x \to 1-0} g(x) = -3 \quad \mathbin{/\mkern-5mu/}
\end{align*}
$$

### (イ)

 $f(x) = \sqrt{x^2 + x + 1}$, $g(x) = \dfrac{\sqrt{x^2 + x + 1} - \sqrt{3}}{x - 1}$ の時、

$$
\begin{align*}
g(x) &= \frac{1}{x - 1}\frac{(x^2 + x - 2)}{\sqrt{x^2 + x + 1} + \sqrt{3}}\\&= \frac{x + 2}{\sqrt{x^2 + x + 1} + \sqrt{3}}
\end{align*}
$$

から

$$
\begin{align*}
\lim_{x \to 1+0} g(x) = \lim_{x \to 1-0} g(x) = \frac{3}{2\sqrt{3}} = \frac{1}{2}\sqrt{3} \quad \mathbin{/\mkern-5mu/}
\end{align*}
$$