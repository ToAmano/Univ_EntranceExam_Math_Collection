---
university: "ukyoto"
category: "zenki"
year: "1983"
question: "1"
type: "solution"
title: "UKYOTO 1983 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $A, B, C$の勝つ確率は右図のようである。\\
\begin{minipage}{0.4\textwidth}

| 相手 |    A    |        B        |        C        |
|:----:|:-------:|:---------------:|:---------------:|
|  A   |         |      $p$      |      $q$      |
|  B   | $1-p$ |                 | $\frac{1}{2}$ |
|  C   | $1-q$ | $\frac{1}{2}$ |                 |

\end{minipage}

(1) もとめる確率を$P_a$とする。右図から、

$$
\begin{align*}
P_a = pq + p(1-q) \cdot \frac{1}{2} \cdot P_a
\end{align*}
$$

$$
\begin{align*}
\therefore P_a = \frac{2pq}{2-p(1-q)}
\end{align*}
$$

\begin{tikzpicture}[x=0.5cm, y=-0.5cm, baseline=(current bounding box.north)]
\node at (0,0) {A};
\node at (2,0) {B};
\node at (4,0) {C};
\node at (6,0) {B};
\node at (8,0) {A};
\draw (0,0.5) -- (0,1) -- (2,1) -- (2,0.5);
\draw (1,1) -- (1,1.5) -- (4,1.5) -- (4,0.5);
\draw (2.5,1.5) -- (2.5,2) -- (6,2) -- (6,0.5);
\draw (4.25,2) -- (4.25,2.5) -- (8,2.5) -- (8,0.5);
\draw[dashed] (6.125,2.5) -- (6.125,3.5);
\end{tikzpicture}

(2) もとめる確率を$P_b$とする。右図から、

$$
\begin{align*}
P_b = (1-p) \frac{1}{2} \cdot P_c
\end{align*}
$$

$P_c$は(1)で$p$と$q$を入れかえたものだから、

$$
\begin{align*}
P_b = \frac{pq(1-p)}{2-q(1-p)}
\end{align*}
$$

\begin{tikzpicture}[x=0.5cm, y=-0.5cm, baseline=(current bounding box.north)]
\node at (0,0) {A};
\node at (2,0) {B};
\node at (4,0) {C};
\node at (6,0) {A};
\draw (0,0.5) -- (0,1) -- (2,1) -- (2,0.5);
\draw (1,1) -- (1,1.5) -- (4,1.5) -- (4,0.5);
\draw (2.5,1.5) -- (2.5,2) -- (6,2) -- (6,0.5);
\draw[dashed] (4.25,2) -- (4.25,3);
\node[right] at (4.5, 3) {これ以降Aが優勝する確率が $P_c$ となる。};
\end{tikzpicture}

(3) もとめる確率を$R$とする。1回目でどちらが勝つかで場合分けして、

$$
\begin{align*}
R = \frac{1}{2} (P_a + P_c) = pq \left\{ \frac{1}{2-p(1-q)} + \frac{1}{2-q(1-p)} \right\}
\end{align*}
$$