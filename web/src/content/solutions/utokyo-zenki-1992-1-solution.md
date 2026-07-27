---
university: "utokyo"
category: "zenki"
year: "1992"
question: "1"
type: "solution"
title: "UTOKYO 1992 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 $S_1 - \int_1^a \log x \, dx = a(\log a - 1) + 1 \quad \dots \text{① である.}$

\bigskip

(1) $\square ABCD$ の面積を $S'$ とすると,

$$
\begin{align*}
S' = \triangle ABD D' + \triangle D' B C = \frac{1}{2}(\log a + \log b)(a - b) + \frac{1}{2} \log b \cdot (b - 1)
\end{align*}
$$

図より明らかに $S' < S_1$ だから, $S'$ の最大値こそ $S_2$ である.

\begin{tikzpicture}[scale=1.2, >=stealth]
\draw[->] (-0.5,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,2.5) node[above] {$y$};
\draw[domain=0.5:3.8, smooth, variable=\x, thick] plot ({\x}, {log2(\x)});
\node[above left] at (3.5, {log2(3.5)}) {$y = \log x$};
\coordinate (C) at (1,0);
\coordinate (Dp) at (2.2,0);
\coordinate (A) at (3.2,0);
\coordinate (D) at (2.2,{log2(2.2)});
\coordinate (B) at (3.2,{log2(3.2)});

\draw[dashed] (D) -- (Dp);
\draw[dashed] (B) -- (A);
\draw[thick] (C) -- (D) -- (B) -- (A) -- cycle;

\node[below] at (C) {$C$};
\node[below] at (Dp) {$D'$};
\node[below] at (A) {$A$};
\node[above left] at (D) {$D$};
\node[above left] at (B) {$B$};
\end{tikzpicture}

$$
\begin{align*}
\frac{d}{db} S' = \frac{1}{2b}(a - 1) - \frac{1}{2} \log a
\end{align*}
$$

より, 極大を与える $\left(\because \frac{a-1}{\log a} < a\right)$

| $b$  | $(1)$ |  $\dots$   | $\frac{a-1}{\log a}$ |  $\dots$   | $a$ |
|:------:|:-------:|:------------:|:----------------------:|:------------:|:-----:|
| $S'$ |         |    $+$     |         $0$          |    $-$     |       |
| $S$  |         | $\nearrow$ |          極大          | $\searrow$ |       |

従って,

$$
\begin{align*}
S_2 = S'\Big|_{b = \frac{a-1}{\log a}} = \frac{1}{2}(a \log a - a + 1) + \frac{1}{2} \frac{a-1}{\log a} \log\left(\frac{a-1}{\log a}\right)
\end{align*}
$$

\bigskip

(2)

$$
\begin{align*}
\frac{S_2}{S_1}&= \frac{\frac{1}{2}(a \log a - a + 1) + \frac{1}{2}(a-1)\{\log(a-1) - \log\log a\}}{a \log a - a + 1}\\&= \frac{1}{2} + \frac{1}{2}\underbrace{\frac{(a-1)\{\log(a-1) - \log\log a\}}{a \log a - a + 1}}_{T}
\end{align*}
$$

$$
\begin{align*}
T = \frac{\left(1 - \frac{1}{a}\right) \left\{ 1 + \frac{\log(1 - \frac{1}{a})}{\log a} - \frac{\log\log a}{\log a} \right\}}{1 - \frac{1}{\log a} + \frac{1}{a \log a}} \longrightarrow 1 \quad (a \to \infty)
\end{align*}
$$

$$
\begin{align*}
\left[ \log a = A \to \infty \text{ より } \frac{\log(\log a)}{\log a} = \frac{\log A}{A} \to 0 \right]
\end{align*}
$$

より,

$$
\begin{align*}
\frac{S_2}{S_1} \longrightarrow 1 \quad (a \to \infty) \text{ である.}
\end{align*}
$$