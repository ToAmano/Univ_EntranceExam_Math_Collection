---
university: "utokyo"
category: "zenki"
year: "2000"
question: "2"
type: "solution"
title: "UTOKYO 2000 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $OR \perp l$ から、

$$
\begin{align*}
\frac{w}{\alpha - \beta} \text{ は純虚数} \cdots \text{①}
\end{align*}
$$

さらに、Rは $l$ 上だから、$t \in \mathbb{R}$ として、

$$
\begin{align*}
(w - \beta) = t(\alpha - \beta)
\end{align*}
$$

$$
\begin{align*}
\therefore \frac{w-\beta}{\alpha-\beta} \in \mathbb{R} \cdots \text{②}
\end{align*}
$$

である。①、②から

$$
\begin{align*}
\begin{cases} \left( \frac{w}{\alpha-\beta} \right) + \overline{\left( \frac{w}{\alpha-\beta} \right)} = 0 \\ \left( \frac{w-\beta}{\alpha-\beta} \right) = \overline{\left( \frac{w-\beta}{\alpha-\beta} \right)} \end{cases}
\end{align*}
$$

$$
\begin{align*}
\begin{cases} w(\bar{\alpha}-\bar{\beta}) + \bar{w}(\alpha-\beta) = 0 \cdots \text{③} \\ (w-\beta)(\bar{\alpha}-\bar{\beta}) = (\bar{w}-\bar{\beta})(\alpha-\beta) \cdots \text{④} \end{cases}
\end{align*}
$$

まず、$w \neq 0$ だから、③から

$$
\begin{align*}
\bar{\alpha}-\bar{\beta} = -\frac{\bar{w}}{w}(\alpha-\beta)
\end{align*}
$$

だから、④に代入、セイリして、

$$
\begin{align*}
-(w-\beta)\frac{\bar{w}}{w}(\alpha-\beta) = (\bar{w}-\bar{\beta})(\alpha-\beta)
\end{align*}
$$

$\alpha \neq \beta, w \neq 0$ から、

$$
\begin{align*}
-(w-\beta)\bar{w} = w(\bar{w}-\bar{\beta})
\end{align*}
$$

$$
\begin{align*}
2|w|^2 - \bar{\beta}w - \beta\bar{w} = 0 \cdots \text{⑤}
\end{align*}
$$

同様にして、

$$
\begin{align*}
2|w|^2 - \bar{\alpha}w - \alpha\bar{w} = 0 \cdots \text{⑥}
\end{align*}
$$

を得る。

$1^\circ$ 十分性
$w = \alpha\beta$ の時、⑤、⑥から、

$$
\begin{align*}
\begin{cases} 2|\alpha|^2|\beta|^2 - \alpha|\beta|^2 - \bar{\alpha}|\beta|^2 = 0 \\ 2|\alpha|^2|\beta|^2 - \beta|\alpha|^2 - \bar{\beta}|\alpha|^2 = 0 \end{cases}
\end{align*}
$$

$\alpha, \beta \neq 0$ だから、

$$
\begin{align*}
\left|\alpha - \frac{1}{2}\right|^2 = \frac{1}{4}, \quad \left|\beta - \frac{1}{2}\right|^2 = \frac{1}{4} \cdots \text{⑦}
\end{align*}
$$

となり、各辺 $0$ 以上だから

$$
\begin{align*}
\left|\alpha - \frac{1}{2}\right| = \frac{1}{2}, \quad \left|\beta - \frac{1}{2}\right| = \frac{1}{2} \cdots \text{⑧}
\end{align*}
$$

より、$P(\alpha), Q(\beta)$ は題意の円周上にある。

$2^\circ$ 必要性
⑧が成立するので、両辺2乗して⑦を得る。変形して、

$$
\begin{align*}
\begin{cases} \bar{\alpha} = \frac{\alpha}{2\alpha-1} \\ \bar{\beta} = \frac{\beta}{2\beta-1} \end{cases} \quad \left(\because \alpha, \beta \neq \frac{1}{2}\right) \cdots \text{⑨}
\end{align*}
$$

$A = \alpha - \beta$ とおく。$\alpha \neq \beta$ より $A \neq 0$ だから③より

$$
\begin{align*}
\bar{w} = -\frac{\bar{A}}{A}w
\end{align*}
$$

だから④に代入、セイリして、

$$
\begin{align*}
\left(-\frac{\bar{A}}{A}w - \bar{\beta}\right)A = (w - \beta)\bar{A}
\end{align*}
$$

$$
\begin{align*}
-\bar{A}w - \bar{\beta}A = \bar{A}w - \beta\bar{A}
\end{align*}
$$

$$
\begin{align*}
\beta\bar{A} - \bar{\beta}A = 2\bar{A}w
\end{align*}
$$

$$
\begin{align*}
w = \frac{\beta\bar{A} - \bar{\beta}A}{2\bar{A}}
\end{align*}
$$

$$
\begin{align*}
= \frac{\beta}{2} - \frac{1}{2} \left( \frac{\beta}{2\beta-1} \right) \frac{\alpha-\beta}{\frac{\alpha}{2\alpha-1} - \frac{\beta}{2\beta-1}} \quad (\because \text{⑨})
\end{align*}
$$

$$
\begin{align*}
= \frac{\beta}{2} - \frac{1}{2} (2\alpha-1)\beta = \alpha\beta
\end{align*}
$$

を得る。
以上 $1^\circ$、$2^\circ$ から示された。
\begin{flushright}
$\blacksquare$
\end{flushright}

\begin{tikzpicture}
\draw[->] (-1,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,3) node[above] {$y$};
\node at (0,0) [below left] {O};
\draw (0.5,2.5) -- (3,0.5);
\node at (0.8,2.2) [above right] {$P(\alpha)$};
\fill (0.8,2.26) circle (1.5pt);
\node at (2.5,0.9) [above right] {$Q(\beta)$};
\fill (2.5,0.9) circle (1.5pt);
\draw (0,0) -- (1.5,1.7);
\node at (1.5,1.7) [above right] {$R(w)$};
\fill (1.5,1.7) circle (1.5pt);
\draw (1.3,1.55) -- (1.45,1.4) -- (1.6,1.6);
\end{tikzpicture}