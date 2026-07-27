---
university: "titech"
category: "zenki"
year: "1964"
question: "1"
type: "solution"
title: "TITECH 1964 zenki Q1 (solution)"
---

## 【解】

以下

$$
\begin{align}
0 \leqq x \leqq 1, 0 \leqq y \leqq 1, 2 \leqq z \leqq 3 \label{eq:1}
\end{align}
$$

で考える．

(1)
題意の時

$$
\begin{align}
w = 3 \iff 3(z-y) = z-x \iff 2z = 3y-x
\end{align}
$$

が成り立つ．これを仮定すると，[(式1)](#eq:1)から 

$$
\begin{align}
4 \leqq 2z \leqq 6, -1 \leqq 3y-x \leqq 3
\end{align}
$$

となり矛盾．よって背理法により$w=3$ となることはない.

(2)
$z-x \ge 0, z-y \ge 0$より$w\ge 0$であるから，$z$を固定して$w$が最大になるのは$x$を最大，$y$を最小にとった時．よって

$$
\begin{align}
\max w =  \frac{z}{z-1}\label{eq:2}
\end{align}
$$

である．

(3)
[(式2)](#eq:2)で$w$を動かした時の最大値が求める$w$の最大値である．[(式2)](#eq:2)を変形すると

$$
\begin{align}
w = 1 + \frac{1}{z-1}
\end{align}
$$

だからこれは[(式1)](#eq:1)の範囲で$z$について単調減少で，$w$は$z=2$の時に

$$
\begin{align}
\max w = 2
\end{align}
$$

となる．

(4)
(2)と同様に$z$が一定の時の$w$の最小値は$x$が最大，$y$を最小にした時で

$$
\begin{align}
\min w = \frac{z-1}{z} = 1-\frac{1}{z}
\end{align}
$$

である．$w$は連続だから，$\min w$と$\max w$の間は全て取る．よって$z$が一定の時に$w$がとりうる範囲は

$$
\begin{align}
&\min w \le w \max w \\&1-\frac{1}{z}\le w \le\frac{z}{z-1}
\end{align}
$$

である．

これを$zw$平面に図示すると$w$ の存在範囲は下図斜線部（境界含む）だから, もとめる $\max k$ は $k = \frac{3}{2}$ である.

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1964/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>