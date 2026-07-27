---
university: "utokyo"
category: "zenki"
year: "2009"
question: "5"
type: "solution"
title: "UTOKYO 2009 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (1) $-1 < x < 1, \ x \ne 0 \cdots (1)$ から、与式の両辺正だから、

$$
\begin{align*}
(与式) \iff 1 - x < (1+x)^{\frac{1}{x}}(1-x)^{\frac{1}{x}} \quad \cdots (2)
\end{align*}
$$

与式の両辺対数をとって、

$$
\begin{align*}
(1 - \frac{1}{x}) \log(1-x) < \frac{1}{x} \log(1+x) \quad \cdots (3)
\end{align*}
$$

である。$f(x) = \log(1+x) - (x-1)\log(1-x)$ とおく。

$1^\circ \ 0 < x < 1$

(3)の両辺に $x$ をかけて

$$
\begin{align*}
(x-1) \log(1-x) < \log(1+x) \quad \cdots (4)
\end{align*}
$$

である。よって $f(x) > 0$ を示せば良い。

$$
\begin{align*}
\begin{cases}
f'(x) = \frac{1}{x+1} - \log(1-x) - 1 \\
f''(x) = \frac{1}{1-x} - \frac{1}{(x+1)^2} = \frac{x(x+3)}{(x+1)^2(1-x)} \quad \cdots (5)
\end{cases}
\end{align*}
$$

だから、$f''(x) > 0$ となって $f'(x)$ は単調増加。これと $f'(0) = 0$ から、$f'(x) > 0$ つまり
$f(x)$ も単調増加。よって、

$$
\begin{align*}
f(x) > \lim_{x \to +0} f(x) = 0
\end{align*}
$$

だから(4)は示された。

$2^\circ \ -1 < x < 0$

両辺に $x$ をかけて、

$$
\begin{align*}
(x-1) \log(1-x) > \log(1+x) \quad \cdots (6)
\end{align*}
$$

だから、$f(x) < 0$ を示せば良い。(5)から

$$
\begin{align*}
f''(x) < 0
\end{align*}
$$

となり、$f'(x)$ は単調減少。これと $f'(0) = 0$ から、$f'(x) > 0$ つまり $f(x)$ は単調増加。
したがって

$$
\begin{align*}
f(x) < \lim_{x \to -0} f(x) = 0
\end{align*}
$$

だから(6)は示された。

$1^\circ, 2^\circ$ から、与式は示された。\fbox{終}

(2) まず、(1)に $x = \frac{1}{100}$ ((1)をみたす) を代入して、

$$
\begin{align*}
0.99 < 0.9999^{100} \quad \cdots (7)
\end{align*}
$$

又、与式の両辺に $(1+x)^{1-\frac{1}{x}}$ をかけて、

$$
\begin{align*}
(1-x^2)^{1-\frac{1}{x}} < 1+x
\end{align*}
$$

$x = -\frac{1}{100}$ ((1)をみたす) として、

$$
\begin{align*}
0.9999^{101} < 0.99 \quad \cdots (8)
\end{align*}
$$

(7)(8)から示された \fbox{終}