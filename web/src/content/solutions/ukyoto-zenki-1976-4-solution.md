---
university: "ukyoto"
category: "zenki"
year: "1976"
question: "4"
type: "solution"
title: "UKYOTO 1976 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{proof}[解]
$a_n > 0$

$$
\begin{align*}
a_n^3 + 3 a_n^2 - \left(9 + \frac{1}{n}\right) a_n + 5 < 0 \quad \cdots \text{①}
\end{align*}
$$

①を変形して

$$
\begin{align*}
(a_n - 1)^2 < \frac{1}{n} \frac{a_n}{a_n + 5} \quad (\because a_n > 0) \quad \cdots \text{②}
\end{align*}
$$

又、$f_n(x) = x^3 + 3x^2 - \left(9 + \frac{1}{n}\right) x + 5$ とおくと

$$
\begin{align*}
f_n'(x) = 3x^2 + 6x - \left(9 + \frac{1}{n}\right)
\end{align*}
$$

より、$f_n'(x) = 0$ の2根 $\alpha, \beta \ (\alpha < \beta)$ として下表を与える.

|  $x$   |  $\dots$   | $\alpha$ |  $\dots$   | $\beta$ |  $\dots$   |
|:--------:|:------------:|:----------:|:------------:|:---------:|:------------:|
| $f_n'$ |    $+$     |   $0$    |    $-$     |   $0$   |    $+$     |
| $f_n$  | $\nearrow$ |            | $\searrow$ |           | $\nearrow$ |

\begin{tikzpicture}[scale=0.8]
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-4) -- (0,6) node[above] {$y$};
  \draw[domain=-2.8:1.8, smooth, variable=\x, blue, thick] plot ({\x}, {\x*\x*\x + 3*\x*\x - 9.1*\x + 5});
  \node[above left] at (-2.1, 15) {};
  \draw[dashed] (1.1, 0) node[below] {$\beta$} -- (1.1, -1.8);
  \draw[dashed] (-3.1, 0) node[above] {$\alpha$} -- (-3.1, 20);
  \node[right] at (1.1, -1.8) {$(\beta = -1 + \sqrt{4 + \frac{1}{3n}})$};
\end{tikzpicture}

従ってグラフは右上図のようになる. から、$\beta < x$ では $x$ は単調増加, $0 < x < \beta$ では $x$ は単調減少である. よって明らかに $0 < a_n < \frac{5}{3}$.

$y = \frac{x}{x+5}$ のグラフを考えてこの時

\begin{tikzpicture}[scale=0.8]
  \draw[->] (-1,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,1.5) node[above] {$y$};
  \draw[domain=0:3.5, smooth, variable=\x, red, thick] plot ({\x}, {\x/(\x + 5)});
  \draw[dashed] (0, 0.25) -- (4, 0.25) node[right] {$y = 1/4$};
\end{tikzpicture}

$$
\begin{align*}
0 < \frac{1}{n} \frac{a_n}{a_n + 5} < \frac{1}{n} \cdot \frac{1}{4}
\end{align*}
$$

だから②より

$$
\begin{align*}
(a_n - 1)^2 < \frac{1}{4n}
\end{align*}
$$

したがってはさみうちの原理から

$$
\begin{align*}
a_n \to 1 \quad (n \to \infty)
\end{align*}
$$

\end{proof}