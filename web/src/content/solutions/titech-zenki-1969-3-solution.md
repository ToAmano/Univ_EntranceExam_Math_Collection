---
university: "titech"
category: "zenki"
year: "1969"
question: "3"
type: "solution"
title: "TITECH 1969 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $\alpha = x + y, \beta = xy$ とすると，存在条件 ($x, y$ の実数条件) から $\alpha^2 - 4\beta \ge 0 \quad \dots \text{①}$ である．

$$
\begin{align*}
u = \alpha + 1, \quad v = 1 - 2\beta\quad\dots\text{②}
\end{align*}
$$

であり，$x^2 + y^2 = a^2$ から

$$
\begin{align*}
\alpha^2 - 2\beta = a^2 \quad\dots\text{③}
\end{align*}
$$

②から $\alpha = u - 1, \beta = \frac{1}{2}(1 - v)$ だから，①, ③に代入して

$$
\begin{align*}
\begin{cases}
(u-1)^2 - 2(1-v) \ge 0 \\
(u-1)^2 - (1-v) = a^2
\end{cases}\iff\begin{cases}
v \ge \frac{1}{2}(-u^2 + 2u + 1) \\
v = -u^2 + 2u + a^2
\end{cases}\quad\text{\dots (1)}
\end{align*}
$$

(2) $\frac{1}{\sqrt{2}} \le a \le 1$ の時，$\frac{1}{2} \le a^2 \le 1$ だから，(1)から

$$
\begin{align*}
\begin{cases}
-u^2 + 2u + \frac{1}{2} \le v \le -u^2 + 2u + 1 \\
v \ge \frac{1}{2}(-u^2 + 2u + 1)
\end{cases}
\end{align*}
$$

図示して下図斜線部

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1969/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 条件を満たす$(u,v)$の範囲（斜線部）</figcaption>
</figure>