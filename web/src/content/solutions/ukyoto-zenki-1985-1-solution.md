---
university: "ukyoto"
category: "zenki"
year: "1985"
question: "1"
type: "solution"
title: "UKYOTO 1985 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $AB=b, AC=c$ とおく。\\
($b, c > 0, q < b+c$) と、余弦定理から

$$
\begin{align*}
q^2 = b^2 + c^2 - 2p
\end{align*}
$$

$b+c = \alpha, bc = \beta$ とおくと

$$
\begin{align*}
\begin{cases}
q < \alpha & \cdots \text{①} \\
\alpha^2 - 2\beta = 2p + q^2 & \cdots \text{②}
\end{cases}
\end{align*}
$$

で、$b, c$ は $t$ の2次式 $t^2 - \alpha t + \beta = 0$ の2正実解である。以下、$b, c$ の存在条件をもとめる。まず、この判別式を $D$ として $b, c > 0$ から

$$
\begin{align*}
\begin{cases}
D \ge 0 \\
\alpha > 0 \\
\beta > 0
\end{cases} \iff
\begin{cases}
\alpha^2 - 4\beta \ge 0 & \cdots \text{③} \\
\alpha > 0 & \cdots \text{④} \\
\beta > 0 & \cdots \text{⑤}
\end{cases}
\end{align*}
$$

②から $\beta = \frac{1}{2}(\alpha^2 - 2p - q^2)$ だから、③⑤に代入して、

$$
\begin{align*}
\begin{cases}
\alpha^2 - 2(\alpha^2 - 2p - q^2) \ge 0 & \cdots \text{⑥} \\
\alpha^2 - 2p - q^2 > 0 & \cdots \text{⑦}
\end{cases}
\end{align*}
$$

$q>0$ から、①$\wedge$④$\wedge$⑦をみたす $\alpha$ の存在条件をもとめればよいことになる。\\
⑥$\wedge$⑦ $\iff 2p + q^2 < \alpha^2 \le 4p + 2q^2 \quad \cdots \text{⑧}$\\
より $2p + q^2 < 4p + 2q^2 \iff 2p + q^2 > 0 \cdots \text{⑨}$が必要（この時 $4p + 2q^2 > 0$ で十分）。この時各辺正から、\\
⑧ $\iff \sqrt{2p + q^2} < \alpha \le \sqrt{4p + 2q^2} \quad \cdots \text{⑩}$\\
で、①、⑩をみたす $\alpha$ が存在する条件は

$$
\begin{align*}
q < \sqrt{4p + 2q^2} \iff 0 < 4p + q^2 \quad (\because \text{両辺正}) \quad \cdots \text{⑪}
\end{align*}
$$

以上からもとめる条件は⑨$\wedge$⑪で、

$$
\begin{align*}
4p + q^2 > 0 \quad (4p + q^2 > 0 \text{の時 } 2p + q^2 > 0) \quad \star
\end{align*}
$$

逆にこの時、$b^2 + c^2 = 2p + q^2$ となる $b, c \in \mathbb{R}_{>0}$ をとることができて、\\
($\because 2p + q^2 > 0$) $\alpha = b+c$, $\beta = bc$ とおくと

$$
\begin{align*}
\alpha^2 - 2\beta = 2p + q^2
\end{align*}
$$

$b, c$ は $t$ の2次式 $t^2 - \alpha t + \beta = 0$ の2正実解で、$\alpha^2 - 4\beta \ge 0, \alpha, \beta > 0$\\
だから代入して

$$
\begin{align*}
\begin{cases}
\alpha^2 - 2(\alpha^2 - 2p - q^2) \ge 0 \\
\alpha > 0 \\
\alpha^2 - 2p - q^2 > 0
\end{cases}
\end{align*}
$$

$\therefore 2p + q^2 < \alpha^2 \le 4p + 2q^2$\\
$4p + 2q^2 - q^2 > 0$ から $q^2 < 4p + 2q^2$ なので、$\alpha = b+c > q$ をみたすような $(b, c)$ が存在し十分。\\
以上から

$$
\begin{align*}
4p + q^2 > 0 \quad \text{//}
\end{align*}
$$

[別解] [多変数でのベクトルの強さ、、]\\
\fbox{\parbox{\textwidth}{B, Cを固定し、Aを動かして考える。この時Aがあるような$p, q$をもとめると考えて、$\overrightarrow{a}$についてとく。点の存在条件をベクトルのそれに換算するというのが大切。}}\\
点Xに対し、$\overrightarrow{OX} = \vec{x}$ とおく。\\
② $\iff (\vec{b} - \vec{a}) \cdot (\vec{c} - \vec{a}) = p$\\
$\iff |\vec{a}|^2 - (\vec{b} + \vec{c}) \cdot \vec{a} + \vec{b} \cdot \vec{c} - p = 0$\\
$\iff \left| \vec{a} - \frac{\vec{b} + \vec{c}}{2} \right|^2 = \left| \frac{\vec{b} - \vec{c}}{2} \right|^2 + p$\\
$= \frac{q^2}{4} + p$\\
より、$\frac{q^2}{4} + p > 0$ (逆にこの時、BC上にないAがとれる！！)

\begin{tikzpicture}
\draw (0,0) -- (4,0) node[midway, below] {$q$};
\draw (0,0) -- (1.5, 2.5) node[midway, above left] {$b$};
\draw (4,0) -- (1.5, 2.5) node[midway, above right] {$c$};
\node at (-0.2, -0.2) {B};
\node at (4.2, -0.2) {C};
\node at (1.5, 2.7) {A};
\end{tikzpicture}