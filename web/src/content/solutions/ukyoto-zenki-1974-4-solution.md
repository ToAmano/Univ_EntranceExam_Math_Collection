---
university: "ukyoto"
category: "zenki"
year: "1974"
question: "4"
type: "solution"
title: "UKYOTO 1974 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] (イ)から $F(x)$ は $m+1$ 次だから, $a \neq 0, a, b \in \mathbb{R}$ として
\begin{equation}
F(x) = (ax+b) g(x) \quad \cdots \text{①}
\end{equation}
とおける. ((ロ)) 両辺微分して
\begin{equation}
g(x) = a g(x) + (ax+b) g'(x) \quad \cdots \text{②}
\end{equation}

又, (ハ)から, $g(x) = x^n + a_{n-1} x^{n-1} + \dots$ となるから $g'(x) = n x^{n-1} + (n-1) a_{n-1} x^{n-2} + \dots$ となる. ②において $x^n, x^{n-1}$ の項を比較して
\begin{equation}
\begin{cases}
x^n = a x^n + a n x^n \quad \cdots \text{③} \\
0 = 0 + b n x^{n-1} \quad \cdots \text{④}
\end{cases}
\end{equation}
$n > 0$ と ③, ④ から, $b = 0, \, a = \frac{1}{1+n}$ となるので $g(x) = y$ として ②に代入

$$
\begin{align*}
\frac{n}{1+n} y = \frac{1}{n+1} x \frac{dy}{dx}
\end{align*}
$$

$$
\begin{align*}
\frac{n}{x} dx = \frac{1}{y} dy
\end{align*}
$$

両辺積分して

$$
\begin{align*}
n \log x + C_1 = \log y \quad (C_1: \text{定数})
\end{align*}
$$

$$
\begin{align*}
y = e^{C_1} x^n
\end{align*}
$$

$g(x)$ の $x^n$ の係数は 1 だから $e^{C_1} = 1$ となり

$$
\begin{align*}
g(x) = x^n \quad /\!/
\end{align*}
$$

①から

$$
\begin{align*}
F(x) = \frac{1}{n+1} x^{n+1} \quad /\!/
\end{align*}
$$