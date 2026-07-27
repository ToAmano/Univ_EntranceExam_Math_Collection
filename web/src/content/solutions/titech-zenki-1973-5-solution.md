---
university: "titech"
category: "zenki"
year: "1973"
question: "5"
type: "solution"
title: "TITECH 1973 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$x, y$ 軸のまわりにまわして得られる立体の体積 $V_x, V_y$ とする.

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1973/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 回転体の体積を求めるための図</figcaption>
</figure>

$$
\begin{align*}
V_x = \pi\int_0^{b/a}(ax-b)^4 dx
\end{align*}
$$

$$
\begin{align*}
V_y = 2\pi\int_0^{b/a} x(ax-b)^2 dx
\end{align*}
$$

から,

$$
\begin{align*}
V_x = V_y &\iff\int_0^{b/a}\{(ax-b)^4 - 2x(ax-b)^2 \} dx = 0 \\&\iff\left[\frac{1}{5a}(ax-b)^5 - \frac{2}{4}a^2 x^4 + \frac{4}{3}ab x^3 - b^2 x^2 \right]_0^{b/a} = 0 \\&\iff -\frac{1}{5a}(-b)^5 - \frac{2}{4}a^2 \left(\frac{b}{a}\right)^4 + \frac{4}{3}ab \left(\frac{b}{a}\right)^3 - b^2 \left(\frac{b}{a}\right)^2 = 0 \\&\iff\frac{b^5}{5a} - \frac{2}{4}\frac{b^4}{a^2} + \frac{4}{3}\frac{b^4}{a^2} - \frac{b^4}{a^2} = 0 \\&\iff ab\frac{1}{5} - \frac{1}{2} + \frac{4}{3} - 1 = 0 \qquad(\because a, b \neq 0) \\&\iff ab = \frac{5}{6} = \text{const}\quad\text{答}
\end{align*}
$$