---
university: "ukyoto"
category: "zenki"
year: "1995"
question: "6"
type: "solution"
title: "UKYOTO 1995 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 時刻 $t$ での水深 $h$、水表面積 $S$ とおくと

$$
\begin{align*}
V &= S \frac{dh}{dt}\cdots\text{\textcircled{1}}\\
S &= V t + \pi a^2 \\&= \pi f(h)^2 \cdots\text{\textcircled{2}}
\end{align*}
$$

\begin{tikzpicture}
  \draw[->] (-2.5, 0) -- (2.5, 0) node[right] {$x$};
  \draw[->] (0, -0.5) -- (0, 3.5) node[above] {$y$};
  
  \draw[domain=0:2.8, variable=\y, smooth] plot ({0.7*exp(\y/3)}, \y) node[right] {$x=f(y)$};
  \draw[domain=0:2.8, variable=\y, smooth] plot ({-0.7*exp(\y/3)}, \y);
  
  \draw (0,0) ellipse (0.7 and 0.15);
  \node[below right] at (0.7,0) {$a$};
  
  \draw (0, 1.8) ellipse ({0.7*exp(1.8/3)} and 0.25);
  \fill[pattern=horizontal lines, pattern color=gray!80] (0, 1.8) ellipse ({0.7*exp(1.8/3)} and 0.25);
  
  \draw[<-] (0, 1.8) -- (0.8, 1.8) node[right] {$h$};
  \draw[<-] (0, 1.0) -- (0.5, 1.0) node[right] {$h'$};
  \draw[dashed] ({-0.7*exp(1.0/3)}, 1.0) -- ({0.7*exp(1.0/3)}, 1.0);
\end{tikzpicture}

\textcircled{2} と $f(y) > 0$ から

$$
\begin{align*}
f(h) = \sqrt{a^2 + \frac{V}{\pi}t} \cdots \text{\textcircled{3}}
\end{align*}
$$

\textcircled{2} を \textcircled{1} に代入、セパレして

$$
\begin{align*}
\frac{V}{Vt + \pi a^2} dt = dh
\end{align*}
$$

積分して、$C$ を定数とすると

$$
\begin{align*}
\log \left( t + \frac{\pi}{V} a^2 \right) = h + C
\end{align*}
$$

$t=0$ で $h=0$ だから、$C = \log \frac{\pi}{V} a^2$ なので、代入して

$$
\begin{align*}
t &= e^h \cdot e^C - \frac{\pi}{V} a^2 \\&= \frac{\pi}{V} a^2 (e^h - 1) \cdots\text{\textcircled{4}}
\end{align*}
$$

$t=T$ で $h=h$ だから

$$
\begin{align*}
T = \frac{\pi}{V} a^2 (e^h - 1) \quad \text{（終）}
\end{align*}
$$

\textcircled{4} を \textcircled{3} に代入し、$h$ を $y$ でおきかえて

$$
\begin{align*}
f(y) = a e^{\frac{y}{2}} \quad \text{（終）}
\end{align*}
$$

\framebox{
\begin{minipage}{0.9\textwidth}
この時

$$
\begin{align*}
h' = \log \left( \frac{V t}{\pi a^2} + 1 \right), \quad S = \pi a^2 e^{h'} = \pi a^2 \left( \frac{V t}{\pi a^2} + 1 \right)
\end{align*}
$$

より \textcircled{1} に代入

$$
\begin{align*}
V = (V t + \pi a^2) \cdot \frac{\pi a^2}{Vt + \pi a^2} \cdot \frac{V}{\pi a^2} = V
\end{align*}
$$

$\implies$ あてそう
\end{minipage}
}