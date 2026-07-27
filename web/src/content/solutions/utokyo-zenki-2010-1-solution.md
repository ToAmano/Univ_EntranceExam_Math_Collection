---
university: "utokyo"
category: "zenki"
year: "2010"
question: "1"
type: "solution"
title: "UTOKYO 2010 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (1) 右のように回転軸 $l$ をとる。(図1)、(図2) のどちらのように回転させても、

$$
\begin{align*}
V = (ac + \frac{1}{4} \pi (a^2 c)) b
\end{align*}
$$

(2) $\alpha = a+c$, $\beta = ac$ とおく。$a, c$ は0より大きい実数だから、

$$
\begin{align*}
\begin{cases} \alpha^2 - 4\beta \ge 0 \\ 0 < \alpha \\ \beta > 0 \end{cases} \cdots \text{①}
\end{align*}
$$

である。$a+b+c = 1$ から $b = 1 - \alpha$ で、$0 < b$ から

$$
\begin{align*}
\alpha < 1 \cdots \text{②}
\end{align*}
$$

となる。$V$ に代入して

$$
\begin{align*}
V &= (\beta + \frac{1}{4}\pi(\alpha^2 - 2\beta))(1-\alpha) \\&= (1-\alpha) \left\{(1 - \frac{1}{2}\pi)\beta + \frac{1}{4}\pi\alpha^2 \right\}\cdots\text{③}
\end{align*}
$$

である。① $\land$ ②を図示すると右図斜線部で、③から $V$ は $\beta$ の単調減少関数だから、$\alpha$ を固定すると、

$$
\begin{align*}
(1-\alpha) \left\{ (1-\frac{1}{2}\pi)\frac{1}{4}\alpha^2 + \frac{1}{4}\pi \alpha^2 \right\} \le V < \frac{1}{4}\pi \alpha^2 (1-\alpha) \cdots \text{④}
\end{align*}
$$

である。④の左辺 $f(\alpha)$、右辺 $g(\alpha)$ とおく。(境界は $\beta = \frac{1}{4}\alpha^2$ のみ含む)

$$
\begin{align*}
\begin{cases} f(\alpha) = (1 + \frac{1}{8}\pi) \alpha^2 (1-\alpha) \\ g(\alpha) = \frac{1}{4}\pi \alpha^2 (1-\alpha) \end{cases} \cdots \text{⑤}
\end{align*}
$$

であり、$h(\alpha) = \alpha^2 (1-\alpha)$ とすると、$h'(\alpha) = 2\alpha - 3\alpha^2 = \alpha(2-3\alpha)$ から下表をうる。

| $\alpha$ |  0  |  $\cdots$  | $2/3$  |  $\cdots$  |  1  |
|:----------:|:---:|:------------:|:--------:|:------------:|:---:|
|   $h'$   |     |    $+$     |    0     |    $-$     |     |
|   $h$    |  0  | $\nearrow$ | $4/27$ | $\searrow$ |  0  |

したがって、$0 < h(\alpha) \le \frac{4}{27}$ だから ④、⑤とあわせて、

$$
\begin{align*}
0 < V < \frac{1}{4}\pi \frac{4}{27} = \frac{\pi}{27}
\end{align*}
$$

$$
\begin{align*}
\therefore 0 < V < \frac{\pi}{27}
\end{align*}
$$

\begin{tikzpicture}
\draw[->] (-0.5,0) -- (2,0) node[right] {$\alpha$};
\draw[->] (0,-0.5) -- (0,2) node[above] {$\beta$};
\draw[domain=0:1, smooth, variable=\x] plot ({\x}, {\x*\x/4});
\node at (1.5, 1) {$\beta = \frac{1}{4}\alpha^2$};
\fill[pattern=north east lines] (0,0) -- plot[domain=0:1] ({\x}, {\x*\x/4}) -- (1,0) -- cycle;
\end{tikzpicture}