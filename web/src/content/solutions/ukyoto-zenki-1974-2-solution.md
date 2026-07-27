---
university: "ukyoto"
category: "zenki"
year: "1974"
question: "2"
type: "solution"
title: "UKYOTO 1974 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{tikzpicture}[scale=0.25]
    \draw[thick] (-10,0) arc (180:360:10);
    \draw[thick] (-10,0) -- (10,0);
    \draw[dashed] (0,0) -- (10,0);
    \node[above] at (5,0) {$10\text{ cm}$};
    \draw[dashed] (-8,-6) -- (8,-6);
    \draw[dashed] (0,0) -- (0,-10);
    \draw[<-] (8,-6) -- (12,-4) node[right] {$\sqrt{20h-h^2}$};
    \draw[<->] (0,-10) -- (0,-6) node[midway,right] {$h$};
\end{tikzpicture}

[**解**] 時刻 $t$ での水面の面積 $S$, 水深を $h$ とすると, 水の流出速度 $k$ として
\begin{equation}
-k = S \frac{dh}{dt} \quad \cdots \text{①}
\end{equation}
ここで,
\begin{equation}
S = \pi (20h - h^2) \quad \cdots \text{②}
\end{equation}
又, 題意から,

$$
\begin{align*}
-v = \frac{dh}{dt}
\end{align*}
$$

であり, 両辺積分して, $t=0$ で $h=10$ より,
\begin{equation}
h = 10 - vt \quad \cdots \text{③}
\end{equation}

(1) 題意の水量 $V(t)$ とすると,

$$
\begin{align*}
V(t) = \pi \int_0^{vt} (100 - x^2) dx = \pi \left[ 100x - \frac{1}{3}x^3 \right]_0^{vt} = \pi \left( 100vt - \frac{1}{3}v^3 t^3 \right) \quad /\!/
\end{align*}
$$

(2) ①, ②, ③から

$$
\begin{align*}
k = S v = \pi v (20-h) h = \pi v (10+vt)(10-vt) = \pi v (100 - v^2 t^2) \quad /\!/
\end{align*}
$$