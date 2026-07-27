---
university: "utokyo"
category: "zenki"
year: "1981"
question: "5"
type: "solution"
title: "UTOKYO 1981 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (1) 図のような展開図での頂点を $A_1, A_2, \dots, A_n$ とする。
又, 底面の各点を $B_1 \dots B_n$ とする。$A_k$ から $B_k B_{k+1}$ ($k=1, 2 \dots n, B_{n+1} = B_1$) に下ろした垂足を $H_k$ とする。
$OH_1 = x, A_1 H_1 = y$ とおく ($0 < x < y$)。

$B_k B_{k+1} = 2x \tan \frac{\pi}{n}$

さて, 展開図が円に内接するとき

$$
\begin{align*}
A_1 O = -x + y = 1 \iff y = 1 - x \quad \left(0 < x < \frac{1}{2}\right)
\end{align*}
$$

である。立体の高さとして

$$
\begin{align*}
h = \sqrt{y^2 - x^2} = \sqrt{1 - 2x}
\end{align*}
$$

又, 底面積 $S$ は

$$
\begin{align*}
S = n \times (\triangle O B_1 B_2) = n \times \frac{1}{2} \cdot x \cdot \left(2x \tan\frac{\pi}{n}\right) = n x^2 \tan\frac{\pi}{n}
\end{align*}
$$

だから体積 $V$ は

$$
\begin{align*}
V = \frac{1}{3} S \cdot h = \frac{1}{3} n \tan\frac{\pi}{n} \, x^2 \sqrt{1 - 2x}
\end{align*}
$$

$x$ の部分を $f(x)$ とおくと, $f(x) \ge 0$ から $f(x)^2$ が最大の時 $f(x)$ も最大。

$$
\begin{align*}
(f(x))^2 = 4x^3 - 10x^4 = 2x^3 (2 - 5x)
\end{align*}
$$

より下表を考える。

$$
\begin{align*}
\begin{array}{c|c|c|c|c|c}
x & 0 & \dots & \frac{2}{5} & \dots & \frac{1}{2} \\ \hline
f' & & + & 0 & - & \\ \hline
f^2 & & \nearrow & \text{極大} & \searrow &
\end{array}
\end{align*}
$$

よって $x = 2/5$ の時 $f(x)$ も最大で

$$
\begin{align*}
V = V_n = \frac{1}{3} n \tan\frac{\pi}{n} \cdot \left(\frac{2}{5}\right)^2 \sqrt{\frac{1}{5}} = \frac{4\sqrt{5}}{375} n \tan\frac{\pi}{n}
\end{align*}
$$

(2) $t = \frac{\pi}{n}$ とおくと $n \to \infty$ で $t \to 0$ で

$$
\begin{align*}
V_n = \frac{4\sqrt{5}}{375} \pi \frac{\tan t}{t} \longrightarrow \frac{4\sqrt{5}}{375} \pi \quad (n \to \infty, t \to 0)
\end{align*}
$$

\begin{tikzpicture}[scale=1.3]
  \coordinate (O) at (0,0);
  \coordinate (A1) at (90:2);
  \coordinate (A2) at (30:2);
  \coordinate (A3) at (-30:2);

  \coordinate (B1) at (120:0.8);
  \coordinate (B2) at (60:0.8);
  \coordinate (B3) at (0:0.8);

  \draw (O) circle (2);

  \draw (A1) -- (B1) -- (B2) -- cycle;
  \draw (A2) -- (B2) -- (B3) -- cycle;
  \draw (O) -- (B1);
  \draw (O) -- (B2);

  \coordinate (H1) at ($(B1)!0.5!(B2)$);
  \draw[dashed] (O) -- (H1) node[midway, left] {$x$};
  \draw[dashed] (A1) -- (H1);

  \node[above] at (A1) {$A_1$};
  \node[above right] at (A2) {$A_2$};
  \node[right] at (A3) {$A_3$};
  \node[left] at (B1) {$B_1$};
  \node[above] at (B2) {$B_2$};
  \node[right] at (B3) {$B_3$};
  \node[below left] at (O) {$O$};
  \node[above right] at (H1) {$H_1$};
\end{tikzpicture}
\qquad
\begin{tikzpicture}[scale=1.3]
  \draw (0,0) node[below left] {$O$} -- (1.5,0) node[below right] {$H_1$} node[midway, below] {$x$} -- (1.5,2.5) node[above] {頂点} -- cycle node[midway, above left] {$y$};
  \node[right] at (1.5,1.25) {$h$};
  \draw (1.3,0) -- (1.3,0.2) -- (1.5,0.2);
\end{tikzpicture}