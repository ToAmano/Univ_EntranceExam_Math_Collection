---
university: "ukyoto"
category: "zenki"
year: "1989"
question: "6"
type: "solution"
title: "UKYOTO 1989 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 高さ $y$ の時の表面の面積 $S$、円錐の半径を $r$ とすると

$$
\begin{align*}
10 - y = S \frac{dy}{dt} \cdots \text{①}
\end{align*}
$$

$\therefore S = \pi \left( \frac{r(10-y)}{10} \right)^2$ を代入してセイリ

$$
\begin{align*}
dt = \frac{\pi r^2}{100}(10-y)dy
\end{align*}
$$

両辺積分して

$$
\begin{align*}
t = \frac{\pi r^2}{100}\left(10y - \frac{1}{2}y^2\right) + C
\end{align*}
$$

$t=0$ で $y=0$ から $C=0$。$(t, y) = (540, 2), y=10$ を各々代入

$$
\begin{align*}
\begin{cases} 540 = \frac{\pi r^2}{100} \cdot 18 \\ t = \frac{\pi r^2}{100} \cdot 50 \end{cases}
\end{align*}
$$

辺々わって

$$
\begin{align*}
\frac{t}{540} = \frac{50}{18} \cdot 54
\end{align*}
$$

$$
\begin{align*}
\therefore t = 1500
\end{align*}
$$

だから、タンクがいっぱいになるのは、あと

$$
\begin{align*}
\frac{1500}{60} - 9 \text{ (h)} = 16 \text{ (h)}
\end{align*}
$$

後である。