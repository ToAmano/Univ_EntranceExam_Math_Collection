---
university: "ukyoto"
category: "zenki"
year: "1988"
question: "6"
type: "solution"
title: "UKYOTO 1988 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 題意から$y = \frac{a}{x} + b$の\\
グラフは右のようである\\
（対称性から$a>0$のみ考える）\\
よって、$y = \frac{a}{x} + b$ が$(1, 8), (5, 0)$を通る\\
から

$$
\begin{align*}
\begin{cases}
8 = a + b \\
0 = \frac{a}{5} + b
\end{cases}
\Leftrightarrow
\begin{cases}
b = -2 \\
a = 10
\end{cases}
\end{align*}
$$

である。以下 $f(x) = \frac{10}{x} - 2$ とおく。

\begin{tikzpicture}[scale=0.5]
    \draw[->] (-1, 0) -- (7, 0) node[right] {$x$};
    \draw[->] (0, -3) -- (0, 9) node[above] {$y$};
    \draw[domain=1:6, smooth, variable=\x] plot ({\x}, {10/\x - 2});
    \draw[dashed] (1, 0) -- (1, 8) -- (0, 8) node[left] {$8$};
    \node[below] at (5, 0) {$5$};
\end{tikzpicture}

(1) 高さ$h$ ($0 \le h \le 8$) の時の水の体積\\
$V(h)$とおくと

$$
\begin{align*}
V(h) &= \int_0^h \pi\left(\frac{10}{y+2}\right)^2 dy \\&= 100\pi\left[ -\frac{1}{y+2}\right]_0^h \\&= 100\pi\left(\frac{1}{2} - \frac{1}{h+2}\right)
\end{align*}
$$

だから

$$
\begin{align*}
V(6) = \frac{75}{2}\pi \quad //
\end{align*}
$$

(2) $\left. \frac{dh}{dt} \right|_{h=3}$ をもとめれば良い。題意から $\frac{dV}{dt} = k$ であって、
$\frac{dh}{dt} = h'$ とおくと、

$$
\begin{align*}
k = 100\pi \frac{1}{(h+2)^2} h'
\end{align*}
$$

だから$h=3$として、

$$
\begin{align*}
\left. h' \right|_{h=3} = \frac{25}{100\pi}k = \frac{k}{4\pi} \text{ [cm/s]} \quad //
\end{align*}
$$

[解 2(2)] エースを使ってみる。\\
(2) （$y = \frac{10}{x} - 2$まで同じ）時刻$t$での表面積$S$、高さ$h$とすると

$$
\begin{align*}
k = S \frac{dh}{dt} \quad \cdots \text{①}
\end{align*}
$$

$$
\begin{align*}
S = \pi \left(\frac{10}{h+2}\right)^2 \quad \cdots \text{②}
\end{align*}
$$

②を①に代入

$$
\begin{align*}
\frac{dh}{dt} = \frac{k}{\left(\frac{10}{h+2}\right)^2 \cdot \pi}
\end{align*}
$$

$h=3$として

$$
\begin{align*}
\frac{dh}{dt} = \frac{k}{4\pi} \quad //
\end{align*}
$$

{\color{cyan}
\fbox{エースのすばらしさ!! これはとんでもない}
}