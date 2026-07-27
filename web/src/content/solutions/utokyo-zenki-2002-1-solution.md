---
university: "utokyo"
category: "zenki"
year: "2002"
question: "1"
type: "solution"
title: "UTOKYO 2002 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 まず、$0 \le \theta < 2\pi$ で考える。($\because$ 与式は $\theta$ について $2\pi$ 周期)

これが異2交点をもつので、$C = \cos\theta, S = \sin\theta$ として、

$$
\begin{align*}
2\sqrt{3}(x-C)^2 + S + 2\sqrt{3}(x+C)^2 + S = 0
\end{align*}
$$

$$
\begin{align*}
4\sqrt{3}(x^2 + C^2) + 2S = 0
\end{align*}
$$

$$
\begin{align*}
2\sqrt{3}x^2 + 2\sqrt{3}C^2 + S = 0
\end{align*}
$$

が $x$ について異2実解をもつので、

$$
\begin{align*}
2\sqrt{3}C^2 + S < 0
\end{align*}
$$

$$
\begin{align*}
2\sqrt{3}(1-S^2) + S < 0
\end{align*}
$$

$$
\begin{align*}
2\sqrt{3}S^2 - S - 2\sqrt{3} > 0 \quad \cdots \textcircled{1}
\end{align*}
$$

\textcircled{1} の左辺 $f(S)$ とおくと、$y = f(S)$ のグラフは右図で、$-1 \le S \le 1$ も考えて、\textcircled{1} をみたす条件は

$$
\begin{align*}
-1 \le S < -\frac{\sqrt{3}}{2}
\end{align*}
$$

$$
\begin{align*}
\therefore \quad \frac{4}{3}\pi < \theta < \frac{5}{3}\pi
\end{align*}
$$

したがって、一般角でまとめると、

$$
\begin{align*}
\frac{4}{3}\pi + 2n\pi < \theta < \frac{5}{3}\pi + 2n\pi \quad (n \in \mathbb{Z}) \hfill \text{\#}
\end{align*}
$$

\begin{tikzpicture}[scale=1.5, >=stealth]
  \draw[->] (-1.8, 0) -- (1.8, 0) node[right] {$S$};
  \draw[->] (0, -1.5) -- (0, 1.8) node[above] {$y$};
  \node[below left] at (0,0) {$O$};
  \draw[domain=-1.15:1.28, smooth, variable=\x, thick] plot ({\x}, {2*sqrt(3)*\x*\x - \x - 2*sqrt(3)});
  \draw[dashed] (-1,0) node[above] {$-1$} -- (-1,1) -- (0,1);
  \filldraw (-1,1) circle (1.2pt);
  \filldraw ({-sqrt(3)/2},0) circle (1.2pt) node[below left] {$-\frac{\sqrt{3}}{2}$};
  \filldraw ({2*sqrt(3)/3},0) circle (1.2pt) node[below right] {$\frac{2}{3}\sqrt{3}$};
  \draw[dashed] (1,0) node[above] {$1$} -- (1,-1) -- (0,-1);
  \filldraw (1,-1) circle (1.2pt);
\end{tikzpicture}