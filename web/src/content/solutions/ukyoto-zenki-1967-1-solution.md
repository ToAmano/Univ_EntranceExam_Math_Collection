---
university: "ukyoto"
category: "zenki"
year: "1967"
question: "1"
type: "solution"
title: "UKYOTO 1967 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

1.  $x = \pm 1$ は明らかに解でないから，
    

$$
\begin{align*}
k = \frac{-x(x-3)(x+3)}{3(x+1)(x-1)} = \frac{1}{3}\left[ -x + \frac{8x}{x^2-1} \right] \equiv f(x) \cdot \frac{1}{3}
\end{align*}
$$

    

$$
\begin{align*}
f'(x) = -1 + \frac{8(x^2-1) - 8x \cdot 2x}{(x^2-1)^2} = -1 + \frac{-8x^2-8}{(x^2-1)^2} = \frac{-(x^2+3)^2}{(x^2-1)^2} < 0
\end{align*}
$$

    から $f(x)$ は $x < -1, -1 < x < 1, 1 < x$ の各区間で単調減少。これと，
    

$$
\begin{align*}
\begin{aligned}
    f(x) &\longrightarrow \mp \infty \quad (x \to \pm \infty) \\
    f(x) &\longrightarrow \mp \infty \quad (x \to -1 \pm 0) \qquad (\text{複号同順}) \\
    f(x) &\longrightarrow \mp \infty \quad (x \to 1 \pm 0)
    \end{aligned}
\end{align*}
$$

    から $y=f(x)$ のグラフは下図．よって示すべきことは明らか．

    
    \begin{tikzpicture}[scale=1.0]
        \draw[->] (-4,0) -- (4,0) node[right]{$x$};
        \draw[->] (0,-3) -- (0,3) node[above]{$y$};
        
        \draw[dashed] (-1,-3) -- (-1,3);
        \draw[dashed] (1,-3) -- (1,3);
        \node[below left] at (-1,0) {$-1$};
        \node[below right] at (1,0) {$1$};
        \node[below left] at (-3,0) {$-3$};
        
        \draw[thick, domain=-3.8:-1.1, smooth] plot (\x, {(-\x*(\x-3)*(\x+3))/(3*(\x+1)*(\x-1))});
        \draw[thick, domain=-0.85:0.85, smooth] plot (\x, {(-\x*(\x-3)*(\x+3))/(3*(\x+1)*(\x-1))});
        \draw[thick, domain=1.15:3.8, smooth] plot (\x, {(-\x*(\x-3)*(\x+3))/(3*(\x+1)*(\x-1))});
        
        \draw[thick] (-0.2, 1.2) -- (3.5, 1.2) node[above]{$k$};
        \node[below] at (2.2, 0) {$1 + \frac{2}{k}$};
        \draw[dashed] (2.2,0) -- (2.2,1.2);
    \end{tikzpicture}

2.  (1)より，
    

$$
\begin{align*}
f\left(1+\frac{2}{k}\right) = \frac{-\left(1+\frac{2}{k}\right)\left(-2+\frac{2}{k}\right)\left(4+\frac{2}{k}\right)}{3\left(2+\frac{2}{k}\right)\frac{2}{k}} = \frac{-(2+k)(2-2k)(4+2/k)}{6(2k+2)}
\end{align*}
$$

    

$$
\begin{align*}
= \frac{-(k-1)(k+2)(2k+1)}{3k(k+1)}
\end{align*}
$$

    から
    

$$
\begin{align*}
k - \frac{(k-1)(k+2)(2k+1)}{3k(k+1)} = \frac{k^3+3k+2}{3k(k+1)} > 0 \quad (\because k > 0)
\end{align*}
$$

    より，$k > f\left(1+\frac{2}{k}\right)$ となり，$1 < 1+\frac{2}{k}$ とあわせて，正の解はただ1つあって
    

$$
\begin{align*}
1 < x < 1 + \frac{2}{k}
\end{align*}
$$

    をみたす．