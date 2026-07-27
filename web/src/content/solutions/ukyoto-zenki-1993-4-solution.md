---
university: "ukyoto"
category: "zenki"
year: "1993"
question: "4"
type: "solution"
title: "UKYOTO 1993 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解]
(1) $[0, 1]$ では $0 < (1+x)^{-n}, x e^{x^2} \le e$ だから\\
（$x e^{x^2}$ は単調、$x=1$ とすれば $e$）

$$
\begin{align*}
0 \le (1+x)^{-n} \cdot x e^{x^2} \le e(1+x)^{-n}
\end{align*}
$$

同じ区間で積分して

$$
\begin{align*}
0 \le b_n \le e \int_0^1 (1+x)^{-n} dx
\end{align*}
$$

右辺を計算する。

$$
\begin{align*}
0 \le b_n &\le e \left[\frac{1}{1-n}(1+x)^{-n+1}\right]_0^1 \\&= \frac{e}{1-n}\left[ 2^{1-n} - 1 \right]\to 0 \quad(n \to\infty)
\end{align*}
$$

はさみうちから $b_n \to 0 \quad (n \to \infty)$

(2)

$$
\begin{align*}
a_n &= \left[ -\frac{1}{n}(1+x)^{-n} e^{x^2}\right]_0^1 + \frac{1}{n}\int_0^1 (1+x)^{-n}\cdot 2x \cdot e^{x^2} dx \\&= -\frac{1}{n}\left[ e \cdot 2^{-n} - 1 \right] + \frac{2}{n} b_n
\end{align*}
$$

だから

$$
\begin{align*}
n a_n = \left( 1 - \frac{e}{2^n} \right) + 2 b_n \to 1 \quad (n \to \infty) \quad (\because (1))
\end{align*}
$$

より

$$
\begin{align*}
n a_n \to 1 \quad (n \to \infty)
\end{align*}
$$