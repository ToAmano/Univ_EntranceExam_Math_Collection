---
university: "titech"
category: "zenki"
year: "1968"
question: "1"
type: "solution"
title: "TITECH 1968 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$$
\begin{align*}
\begin{cases}
ab+1 \le abc \le bc+ca+ab+1 & \cdots \text{①} \\
a > b > c & \cdots \text{②}
\end{cases}
\end{align*}
$$

①の両辺を $abc$ でわって

$$
\begin{align*}
\frac{1}{c} + \frac{1}{abc}\le 1 \le\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{abc}\quad\cdots\text{③}
\end{align*}
$$

$T = \frac{1}{abc}$ とおく．まず，$c=1$ は③の左側が成立せず不適だから，$c \ge 2$ である．③の右側から

$$
\begin{align*}
1 < \frac{3}{c} + \frac{1}{c^3}\quad\therefore c^3 - 3c^2 - 1 < 0 \quad(\because c > 0) \quad\cdots\text{④}
\end{align*}
$$

$f(x) = x^3 - 3x^2 - 1$ とおく．$f'(x) = 3x^2 - 6x = 3x(x-2)$ より増減表をつくる．

$$
\begin{align*}
\begin{array}{c|c|c|c|c|c|c|c}
x & 0 & \cdots & 2 & \cdots & 3 & \cdots & 4 \\ \hline
f' & 0 & - & 0 & + & + & + & + \\ \hline
f & -1 & \searrow & -5 & \nearrow & -1 & \nearrow & 15
\end{array}
\end{align*}
$$

したがって $y=f(x)$ のグラフは右上がりで，④には $c=1, 2, 3$ が必要．一方 $c \ge 2$ だったから，$c=2, 3$ である．

### $1^\circ \ c=2$

②，③に代入

$$
\begin{align*}
\begin{cases}
\frac{1}{2ab} \le \frac{1}{2} \le \frac{1}{a} + \frac{1}{b} + \frac{1}{2ab} & \cdots \text{⑤} \\
3 \le b < a
\end{cases}
\end{align*}
$$

再び右側から

$$
\begin{align*}
\frac{1}{2} < \frac{2}{b} + \frac{1}{2b^2}\quad\therefore b^2 - 4b - 1 < 0
\end{align*}
$$

$y = x^2 - 4x - 1$ のグラフから $b=3, 4$ である．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1968/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=x^2-4x-1$のグラフ</figcaption>
</figure>

#### (I) $b=4$

⑤から

$$
\begin{align*}
\frac{1}{8a}\le\frac{1}{2}\le\frac{1}{4} + \frac{1}{a} + \frac{1}{8a} = \frac{1}{4} + \frac{9}{8a}
\end{align*}
$$

$$
\begin{align*}
\therefore\frac{1}{4}\le a \le\frac{9}{2}
\end{align*}
$$

だが，$5 \le a$ とあわせて不適．

#### (II) $b=3$

⑤から

$$
\begin{align*}
\frac{1}{6a}\le\frac{1}{2}\le\frac{1}{3} + \frac{1}{a} + \frac{1}{6a} = \frac{1}{3} + \frac{7}{6a}
\end{align*}
$$

$$
\begin{align*}
\therefore\frac{1}{3}\le a \le 7
\end{align*}
$$

$4 \le a$ とあわせて，$a=4, 5, 6, 7$

### $2^\circ \ c=3$

②，③に代入

$$
\begin{align*}
\begin{cases}
\frac{1}{3ab} \le \frac{2}{3} \le \frac{1}{a} + \frac{1}{b} + \frac{1}{3ab} & \cdots \text{⑥} \\
4 \le b < a
\end{cases}
\end{align*}
$$

右側から

$$
\begin{align*}
\frac{2}{3} < \frac{2}{b} + \frac{1}{3b^2}\quad\therefore 2b^2 - 6b - 1 < 0
\end{align*}
$$

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1968/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $y=2x^2-6x-1$のグラフ</figcaption>
</figure>

$y = 2x^2 - 6x - 1$ のグラフから，これと⑥を満たす $b$ はなく，不適．

\paragraph{}
以上まとめて，

$$
\begin{align*}
(a,b,c) = (4,3,2), (5,3,2), (6,3,2), (7,3,2)
\end{align*}
$$