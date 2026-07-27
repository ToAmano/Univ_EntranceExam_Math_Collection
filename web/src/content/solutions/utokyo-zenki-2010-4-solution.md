---
university: "utokyo"
category: "zenki"
year: "2010"
question: "4"
type: "solution"
title: "UTOKYO 2010 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $f(x) = \frac{1}{2}x + \sqrt{\left(\frac{1}{2}x\right)^2 + 2}$ とおく。
(1) 題意の直線は、各々 $y=y_1, y=y_2$ であるから、$H_1(y_1, y_1)$ となる。$\triangle OP_1 H_1$ の面積 $S_1$ とする。サラスの公式から

$$
\begin{align*}
S_1 = \frac{1}{2} | x_1 y_1 - y_1 y_1 | = \frac{1}{2} | y_1 | \left| \sqrt{\left(\frac{1}{2}x_1\right)^2+2} - \frac{1}{2}x_1 \right| = \frac{1}{2} | y_1 | \frac{2}{|y_1|} = 1
\end{align*}
$$

となり、$S_1$ は $i$ によらない一定値だから、$\triangle OP_1 H_1 = \triangle OP_2 H_2$ 固

(2) $C$ の概形は右図である。$y = \frac{1}{2}x + \sqrt{\left(\frac{1}{2}x\right)^2 + 2}$ を逆に解く。

$$
\begin{align*}
y - \frac{1}{2}x = \sqrt{\left(\frac{1}{2}x\right)^2 + 2}
\end{align*}
$$

図から $y - \frac{1}{2}x > 0$ だから両辺 $0$ 以上なので2乗して

$$
\begin{align*}
y^2 - xy = 2 \implies x = \frac{y^2 - 2}{y} = y - \frac{2}{y} \cdots \text{①}
\end{align*}
$$

(1)から、もとめる面積は右図斜線部で、

$$
\begin{align*}
S &= \text{(台形)} - \text{(積分)}\\&= \frac{1}{2}(y_1 + y_2)(y_2 - y_1) - \int_{y_1}^{y_2} x dy \\&= \frac{1}{2}(y_2^2 - y_1^2) - \left[\frac{1}{2}y^2 - 2\log y \right]_{y_1}^{y_2}\quad(\because\text{①}) \\&= 2\log\frac{y_2}{y_1}
\end{align*}
$$

となる。