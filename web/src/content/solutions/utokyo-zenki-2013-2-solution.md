---
university: "utokyo"
category: "zenki"
year: "2013"
question: "2"
type: "solution"
title: "UTOKYO 2013 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 $C = \cos x, S = \sin x$ とする。$x > 0$ から

$$
\begin{align*}
f(x) = g(x) \iff \frac{C - S x}{x^2} = a \quad \cdots \textcircled{1}
\end{align*}
$$

である。この左辺を $h(x)$ とする。$(C - S x)' = (-S - S - C x) = -(2S + C x)$ から、

$$
\begin{align*}
h'(x) &= \frac{-(2S + C x) \cdot x^2 - 2x (C - S x)}{x^4}\\&= \frac{-(x^2 + 2)}{x^3} C
\end{align*}
$$

だから、下表をうる。

| $x$ | $0$ | $\cdots$ | $\frac{\pi}{2}$ | $\cdots$ | $\frac{3}{2}\pi$ | $\cdots$ | $2\pi$ | $\cdots$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $h'$ |  | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ |  |
| $h$ |  | $\searrow$ |  | $\nearrow$ |  | $\searrow$ |  |  |

これと、$h(x) = \frac{C}{x^2} - \frac{S}{x} \to +\infty \; (x \to +0)$ から、グラフの概形は右図

\begin{tikzpicture}[scale=1.0, >=stealth]
  \draw[->] (-0.5,0) -- (8.5,0) node[right] {$x$};
  \draw[->] (0,-2.0) -- (0,3.0) node[above] {$y$};
  \node[below left] at (0,0) {$O$};
  
  \draw[domain=0.35:8.0, samples=200, smooth, thick, variable=\x] 
    plot ({\x}, {(cos(\x r) - sin(\x r)*\x)/(\x*\x)});
    
  \draw[dashed] ({pi/2}, 0) -- ({pi/2}, {-2/pi});
  \node[above] at ({pi/2}, 0) {$\frac{\pi}{2}$};
  \node[left] at (0, {-2/pi}) {$-\frac{2}{\pi}$};
  \draw[dashed] (0, {-2/pi}) -- ({pi/2}, {-2/pi});
  \fill ({pi/2}, {-2/pi}) circle (1.5pt);

  \draw[dashed] ({3*pi/2}, 0) -- ({3*pi/2}, {2/(3*pi)});
  \node[below] at ({3*pi/2}, 0) {$\frac{3}{2}\pi$};
  \node[left] at (0, {2/(3*pi)}) {$\frac{2}{3\pi}$};
  \draw[dashed] (0, {2/(3*pi)}) -- ({3*pi/2}, {2/(3*pi)});
  \fill ({3*pi/2}, {2/(3*pi)}) circle (1.5pt);

  \draw[dashed] ({5*pi/2}, 0) -- ({5*pi/2}, {-2/(5*pi)});
  \node[above] at ({5*pi/2}, 0) {$\frac{5}{2}\pi$};
  \node[left] at (0, {-2/(5*pi)}) {$-\frac{2}{5\pi}$};
  \draw[dashed] (0, {-2/(5*pi)}) -- ({5*pi/2}, {-2/(5*pi)});
  \fill ({5*pi/2}, {-2/(5*pi)}) circle (1.5pt);

  \draw[dashed] ({7*pi/2}, 0) -- ({7*pi/2}, {2/(7*pi)});
  \node[below] at ({7*pi/2}, 0) {$\frac{7}{2}\pi$};
  \fill ({7*pi/2}, {2/(7*pi)}) circle (1.5pt);
\end{tikzpicture}

ここで、極値について、

$$
\begin{align*}
h\left( 2m\pi + \frac{1}{2}\pi \right) = \frac{-1}{2m\pi + \frac{1}{2}\pi}
\end{align*}
$$

$$
\begin{align*}
h\left( 2m\pi + \frac{3}{2}\pi \right) = \frac{1}{2m\pi + \frac{3}{2}\pi}
\end{align*}
$$

だから、商の絶対値は $m$ について単調減少である。したがって、図から

$$
\begin{align*}
a = -\frac{2}{5\pi}, \quad \frac{2}{5\pi} < a < \frac{2}{3\pi} \hfill \text{固}
\end{align*}
$$

\bigskip