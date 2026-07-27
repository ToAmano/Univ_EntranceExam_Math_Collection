---
university: "ukyoto"
category: "zenki"
year: "1971"
question: "4"
type: "solution"
title: "UKYOTO 1971 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

$y = \sqrt{|x^2 - 1|}$ のグラフは下図だから, 求める体積 $V$ のうち $x \ge 0$ でみた右部分の体積 $V'$ として

$$
\begin{align*}
V = 2 V' \quad \dots \text{①}
\end{align*}
$$

\begin{tikzpicture}[scale=1.0]
    \draw[->] (-3,0) -- (3,0) node[right]{$x$};
    \draw[->] (0,-0.5) -- (0,2.8) node[above]{$y$};
    
    \draw[thick,domain=-1:1,samples=100] plot (\x, {sqrt(1 - \x*\x)});
    \draw[thick,domain=1:2.236,samples=100] plot (\x, {sqrt(\x*\x - 1)});
    \draw[thick,domain=-2.236:-1,samples=100] plot (\x, {sqrt(\x*\x - 1)});
    
    \draw[dashed] (-2.236,2) -- (2.236,2);
    \draw[dashed] (2.236,0) -- (2.236,2);
    \draw[dashed] (-2.236,0) -- (-2.236,2);
    
    \node[below left] at (0,0) {$0$};
    \node[left] at (0,2) {$2$};
    \node[below] at (1,0) {$1$};
    \node[below] at (-1,0) {$-1$};
    \node[below] at (2.236,0) {$\sqrt{5}$};
    \node[below] at (-2.236,0) {$-\sqrt{5}$};
    
    \node[above] at (1.5,1.2) {\small $y = \sqrt{|x^2 - 1|}$};
    \node[below] at (0.5,0.5) {\small $x^2+y^2=1$};
\end{tikzpicture}

又,

$$
\begin{align*}
V' = 4 \sqrt{5}\pi - \frac{1}{2} \cdot \frac{4}{3}\pi - \int_1^{\sqrt{5}} \pi (x^2 - 1) \, dx
\end{align*}
$$

$$
\begin{align*}
= \pi \left[ 4\sqrt{5} - \frac{2}{3} - \left[ \frac{1}{3}x^3 - x \right]_1^{\sqrt{5}} \right]
\end{align*}
$$

$$
\begin{align*}
= \pi \left[ 4\sqrt{5} - \frac{2}{3} - \frac{2}{3}\sqrt{5} + \frac{2}{3} \right]
\end{align*}
$$

$$
\begin{align*}
= \pi \left( \frac{10}{3}\sqrt{5} - \frac{4}{3} \right)
\end{align*}
$$

だから①に代入

$$
\begin{align*}
V = \frac{4}{3}\pi (5\sqrt{5} - 2)
\end{align*}
$$