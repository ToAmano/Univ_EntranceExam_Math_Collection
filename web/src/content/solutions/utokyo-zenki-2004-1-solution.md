---
university: "utokyo"
category: "zenki"
year: "2004"
question: "1"
type: "solution"
title: "UTOKYO 2004 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{proof}[解]
P, Q, R の $x$ 座標を $\alpha, \beta, \gamma$ とおく. PQ の傾きが $\sqrt{2}$ だから,
\begin{equation}
\alpha + \beta = \sqrt{2} \quad \cdots ①
\end{equation}
このもとで $\vec{PQ} = \begin{pmatrix} \beta - \alpha \\ \beta^2 - \alpha^2 \end{pmatrix} = (\beta - \alpha) \begin{pmatrix} 1 \\ \sqrt{2} \end{pmatrix}$ となり, PQ の中点を M として, $MR \perp PQ$, $MR = \frac{\sqrt{3}}{2} PQ$ だから,

$$
\begin{align*}
\vec{MR} = \pm \frac{\sqrt{3}}{2} (\beta - \alpha) \begin{pmatrix} -\sqrt{2} \\ 1 \end{pmatrix}
\end{align*}
$$

とおける. したがって

$$
\begin{align*}
\vec{OR} = \frac{1}{2} \begin{pmatrix} \alpha + \beta \\ \alpha^2 + \beta^2 \end{pmatrix} \pm \frac{\sqrt{3}}{2} (\beta - \alpha) \begin{pmatrix} -\sqrt{2} \\ 1 \end{pmatrix}
\end{align*}
$$

R も $y = x^2$ 上にあるから

$$
\begin{align*}
\frac{1}{2} (\alpha^2 + \beta^2) \pm \frac{\sqrt{3}}{2} (\beta - \alpha) = \left\{ \frac{1}{2} \sqrt{2} \mp \frac{\sqrt{3}}{2} \sqrt{2} (\beta - \alpha) \right\}^2
\end{align*}
$$

$$
\begin{align*}
(\alpha^2 + \beta^2) \pm \sqrt{3}(\beta - \alpha) = (1 \mp \sqrt{3}(\beta - \alpha))^2 = 3(\beta - \alpha)^2 \mp 2\sqrt{3}(\beta - \alpha) + 1 \quad \cdots ②
\end{align*}
$$

である.

### $1^\circ$ 複号同順の時（上辺）

$$
\begin{align*}
\alpha^2 + \beta^2 - 3(\beta - \alpha)^2 + 3\sqrt{3}(\beta - \alpha) - 1 = 0
\end{align*}
$$

①から $\beta = \sqrt{2} - \alpha$ だから,

$$
\begin{align*}
(2\alpha^2 - 2\sqrt{2}\alpha + 2) - 3(\sqrt{2} - 2\alpha)^2 + 3\sqrt{3}(\sqrt{2} - 2\alpha) - 1 = 0
\end{align*}
$$

$$
\begin{align*}
(2\alpha^2 - 2\sqrt{2}\alpha + 2) - 3(4\alpha^2 - 4\sqrt{2}\alpha + 2) + 3\sqrt{6} - 6\sqrt{3}\alpha - 1 = 0
\end{align*}
$$

$$
\begin{align*}
-10\alpha^2 + (10\sqrt{2} - 6\sqrt{3})\alpha - 5 + 3\sqrt{6} = 0
\end{align*}
$$

$$
\begin{align*}
\alpha = \frac{(5\sqrt{2} - 3\sqrt{3}) \pm \sqrt{(5\sqrt{2} - 3\sqrt{3})^2 - 50 + 30\sqrt{6}}}{10} = \frac{5\sqrt{2} - 3\sqrt{3} \pm 3\sqrt{3}}{10}
\end{align*}
$$

### $2^\circ$ 複号異順の時

$$
\begin{align*}
\alpha^2 + \beta^2 - 3\sqrt{3}(\beta - \alpha) - 3(\beta - \alpha)^2 - 1 = 0
\end{align*}
$$

$\beta = \sqrt{2} - \alpha$ より

$$
\begin{align*}
(2\alpha^2 - 2\sqrt{2}\alpha + 2) - 3\sqrt{3}(\sqrt{2} - 2\alpha) - 3(\sqrt{2} - 2\alpha)^2 - 1 = 0
\end{align*}
$$

$$
\begin{align*}
(2\alpha^2 - 2\sqrt{2}\alpha + 2) - 3\sqrt{6} + 6\sqrt{3}\alpha - 3(4\alpha^2 - 4\sqrt{2}\alpha + 2) - 1 = 0
\end{align*}
$$

$$
\begin{align*}
-10\alpha^2 + (10\sqrt{2} + 6\sqrt{3})\alpha - 5 - 3\sqrt{6} = 0
\end{align*}
$$

$$
\begin{align*}
\alpha = \frac{(5\sqrt{2} + 3\sqrt{3}) \pm \sqrt{(5\sqrt{2} + 3\sqrt{3})^2 - 50 - 30\sqrt{6}}}{10} = \frac{5\sqrt{2} + 3\sqrt{3} \pm 3\sqrt{3}}{10}
\end{align*}
$$

したがって, $\alpha = \frac{5\sqrt{2}}{10}, \frac{5\sqrt{2} \pm 6\sqrt{3}}{10}$ となるから,

$$
\begin{align*}
a = |\vec{PQ}| = |\beta - \alpha|\sqrt{3} = |\sqrt{2} - 2\alpha|\sqrt{3}
\end{align*}
$$

に代入して,

$$
\begin{align*}
a = 0, \frac{18}{5}
\end{align*}
$$

$a = 0$ は不適だから, $a = \frac{18}{5}$ \quad \text{//}
\end{proof}

\begin{tikzpicture}[scale=1.5]
  \draw[->] (-1.5,0) -- (2,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,2.5) node[above] {$y$};
  \draw[domain=-1.3:1.3,smooth,variable=\x,blue,thick] plot ({\x},{\x*\x});
  \coordinate (P) at (-0.8,0.64);
  \coordinate (Q) at (1.2,1.44);
  \coordinate (M) at (0.2,1.04);
  \coordinate (R) at (0.8,0.64);
  \draw[thick] (P) -- (Q);
  \draw[thick,dashed] (M) -- (R);
  \fill (P) circle (1.5pt) node[left] {$P$};
  \fill (Q) circle (1.5pt) node[right] {$Q$};
  \fill (M) circle (1.5pt) node[above left] {$M$};
  \fill (R) circle (1.5pt) node[below right] {$R$};
  \node at (0,-0.2) {$O$};
\end{tikzpicture}