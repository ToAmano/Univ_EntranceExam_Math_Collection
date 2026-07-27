---
university: "ukyoto"
category: "zenki"
year: "1983"
question: "6"
type: "solution"
title: "UKYOTO 1983 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 時刻 $t$ での水面の面積 $P$ とすると、

$$
\begin{align*}
-S v = P \frac{dx}{dt} \quad \cdots \text{①}
\end{align*}
$$

ここで、

$$
\begin{align*}
P = \pi \left( \frac{x}{h} R \right)^2 = \frac{\pi R^2}{h^2} x^2 \quad \cdots \text{②}
\end{align*}
$$

及び

$$
\begin{align*}
v = k x
\end{align*}
$$

を①に代入して

$$
\begin{align*}
-S k x = \frac{\pi R^2}{h^2} x^2 \frac{dx}{dt}
\end{align*}
$$

$x > 0$ より、

$$
\begin{align*}
-S k = \frac{\pi R^2}{h^2} x \frac{dx}{dt}
\end{align*}
$$

両辺積分して、$t = 0$ で $x = h$ より、

$$
\begin{align*}
-S k t + \frac{1}{2} \pi R^2 = \frac{1}{2} \frac{\pi R^2}{h^2} x^2
\end{align*}
$$

$x > 0$ より、

$$
\begin{align*}
x(t) = \sqrt{\frac{2h^2}{\pi R^2} \left( \frac{1}{2} \pi R^2 - Skt \right)}
\end{align*}
$$

\begin{tikzpicture}
\draw (0,0) ellipse (2cm and 0.5cm);
\draw (-2,0) -- (0,-3) -- (2,0);
\draw[dashed] (0,-3) -- (0,0);
\draw[dashed] (-1.33,-1) arc (180:360:1.33cm and 0.33cm);
\draw (-1.33,-1) arc (180:0:1.33cm and 0.33cm);
\node[above right] at (1,0) {$R$};
\node[right] at (1.33,-1) {$\frac{x}{h}R$};
\draw[<->] (-0.5,-3) -- (-0.5,-1) node[midway, left] {$x$};
\draw[<->] (-1,-3) -- (-1,0) node[midway, left] {$h$};
\end{tikzpicture}