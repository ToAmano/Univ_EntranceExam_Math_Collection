---
university: "ukyoto"
category: "zenki"
year: "1967"
question: "3"
type: "solution"
title: "UKYOTO 1967 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $P$ での接線は $\frac{x_1}{a^2}x - \frac{y_1}{b^2}y = 1 \dots \text{①}$ であるから，$Q\left(\frac{a^2}{x_1}, 0\right)$ である．

1.  まず $\frac{y_1^2}{b^2} = \frac{x_1^2}{a^2} - 1$ 及び $y_1, b > 0$ から
    

$$
\begin{align*}
y_1 = b \sqrt{\frac{x_1^2}{a^2} - 1}
\end{align*}
$$

    だから
    

$$
\begin{align*}
\triangle OPQ = \frac{1}{2} \frac{a^2}{x_1} b \sqrt{\frac{x_1^2}{a^2} - 1}
\end{align*}
$$

2.  

$$
\begin{align*}
\begin{aligned}
    \triangle OPQ &= \frac{ab}{2} \sqrt{\frac{x_1^2 - a^2}{x_1^2}} \\
    &= \frac{ab}{2} \sqrt{1 - a^2 / x_1^2} \xrightarrow{x_1 \to \infty} \frac{ab}{2}
    \end{aligned}
\end{align*}
$$

\begin{tikzpicture}[scale=1.2]
    \draw[->] (-0.5,0) -- (4,0) node[right]{$x$};
    \draw[->] (0,-0.5) -- (0,3) node[above]{$y$};
    \node[below left] at (0,0) {$O$};
    
    \draw[thick, domain=1.21:3.5, smooth] plot (\x, {sqrt(max(\x*\x - 1.44, 0))});
    \node[below] at (1.2,0) {$a$};
    
    \coordinate (P) at (2.8, 2.53);
    \fill (P) circle (1.5pt) node[above left]{$P$};
    \draw[dashed] (2.8,0) node[below]{$x_1$} -- (P) -- (0,2.53) node[left]{$y_1$};
    
    \coordinate (Q) at (0.51, 0);
    \fill (Q) circle (1.5pt) node[below left]{$Q$};
    
    \draw[thick] (-0.2, -0.78) -- (3.3, 3.08);
    \draw[fill=gray!20, opacity=0.5] (0,0) -- (Q) -- (P) -- cycle;
\end{tikzpicture}