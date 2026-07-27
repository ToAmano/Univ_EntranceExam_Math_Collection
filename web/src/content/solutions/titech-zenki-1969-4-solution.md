---
university: "titech"
category: "zenki"
year: "1969"
question: "4"
type: "solution"
title: "TITECH 1969 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $3a_n > 2a_{n-1} \quad \dots \text{①}$

与式から

$$
\begin{align*}
\begin{pmatrix} X \\ Y \end{pmatrix} = x \begin{pmatrix} a_n \\ a_{n-1} \end{pmatrix} + y \begin{pmatrix} 2 \\ 3 \end{pmatrix}
\end{align*}
$$

である．$\vec{a}_n = \begin{pmatrix} a_n \\ a_{n-1} \end{pmatrix}$, $\vec{\beta} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$ とおくと，$|x| + |y| \le 1$ から，$(X, Y)$ は右下斜線部内をうごく ($O$ に注意した)．この面積 $S$ は，

$$
\begin{align*}
\frac{1}{2} S &= (\text{\vec{\beta} と -\vec{a}_n でつくられる三角形}) + (\text{\vec{\beta} と \vec{a}_n でつくられる三角形}) \\&= \frac{1}{2} |-3a_n + 2a_{n-1}| + \frac{1}{2} |3a_n - 2a_{n-1}| \\&= |3a_n - 2a_{n-1}| \\&= 3a_n - 2a_{n-1}\quad(\because\text{①})
\end{align*}
$$

と表せる．$S = 2$ だから，

$$
\begin{align*}
1 = 3a_n - 2a_{n-1}\quad(n \ge 2)
\end{align*}
$$

$$
\begin{align*}
\therefore a_n - 1 = \frac{2}{3}(a_{n-1} - 1) \quad(n \ge 2)
\end{align*}
$$

くり返し用いて，

$$
\begin{align*}
a_n = \left(\frac{2}{3}\right)^{n-1}(a_1 - 1) + 1 \longrightarrow 1 \quad(n \to +\infty)
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1969/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点列$\vec a_n$の$\vec\beta$への収束の様子</figcaption>
</figure>