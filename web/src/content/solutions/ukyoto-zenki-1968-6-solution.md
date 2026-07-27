---
university: "ukyoto"
category: "zenki"
year: "1968"
question: "6"
type: "solution"
title: "UKYOTO 1968 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $0 < x < 1 \dots \text{①}$

$$
\begin{align*}
\frac{1}{x} \int_0^x \frac{1}{\sqrt{1-t}} \, dt = \frac{1}{\sqrt{1-y}} \quad \dots \text{②}
\end{align*}
$$

$$
\begin{align*}
\frac{1}{x} \int_0^x \frac{1}{\sqrt{1-t}} \, dt = \frac{1}{x} \left[ -2(1-t)^{\frac{1}{2}} \right]_0^x = \frac{-2}{x} \left(\sqrt{1-x} - 1\right)
\end{align*}
$$

を②に代入

$$
\begin{align*}
\frac{2}{x} \left(1 - \sqrt{1-x}\right) = \frac{1}{\sqrt{1-y}}
\end{align*}
$$

①では両辺正だから2乗して

$$
\begin{align*}
\frac{4}{x^2} \left(1 - \sqrt{1-x}\right)^2 = \frac{1}{1-y}
\end{align*}
$$

同じく逆数をとって

$$
\begin{align*}
\frac{x^2}{4\left(1 - \sqrt{1-x}\right)^2} = 1 - y
\end{align*}
$$

$$
\begin{align*}
\therefore y = 1 - \frac{x^2}{4\left(1 - \sqrt{1-x}\right)^2} \equiv f(x) \quad \dots \text{③}
\end{align*}
$$

さて,

$$
\begin{align*}
\begin{aligned}
4 f'(x) &= -\frac{2x\left(1-\sqrt{1-x}\right)^2 - x^2 \cdot 2\left(1-\sqrt{1-x}\right) \frac{-1}{2\sqrt{1-x}}}{\left(1-\sqrt{1-x}\right)^4} \\
&= \frac{-2x}{\left(1-\sqrt{1-x}\right)^3} \left[ \left(1-\sqrt{1-x}\right) - \frac{x}{2\sqrt{1-x}} \right] \\
&= \frac{-x}{\left(1-\sqrt{1-x}\right)^3 \sqrt{1-x}} \left[ 2\sqrt{1-x} - (2-x) \right] \\
&= \frac{1}{\left(1-\sqrt{1-x}\right)^3 \sqrt{1-x}} \frac{x^3}{2\sqrt{1-x} + (2-x)} > 0 \quad (\because 0 < x < 1)
\end{aligned}
\end{align*}
$$

から, $y$ は $x$ の単調増加であり, 又, ③の表すから

$$
\begin{align*}
y \longrightarrow \frac{3}{4} \quad (x \to 1)
\end{align*}
$$

である.