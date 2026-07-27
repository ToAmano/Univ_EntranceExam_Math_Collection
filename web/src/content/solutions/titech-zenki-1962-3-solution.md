---
university: "titech"
category: "zenki"
year: "1962"
question: "3"
type: "solution"
title: "TITECH 1962 zenki Q3 (solution)"
---

{\bf ［解］}

題意の円を$C: (x - 2a)^2 + (y - a)^2 = 5a^2 - 20a + 25$ とおく．

まず前半部分，円$C$が二つの定点を通ることを示す．円の方程式を$a$について整理すると

$$
\begin{align}
(-4x - 2y + 20)a + (x^2 + y^2 - 25) = 0
\end{align}
$$

だから，これが $a$ についての恒等式の時，つまり

$$
\begin{align}
\begin{cases}
-4x - 2y + 20 = 0 \\
x^2 + y^2 = 25
\end{cases}\iff(x,y) = (3,4), (5,0)
\end{align}
$$

の時に与式は $a$ によらず成り立つから，もとめる $2$ 定点はこれである．

次に後半部分を考える．二つ目の円を$D: x^2+y^2=25$とする．
二つの円$C, D$の中心間距離 $d$ は 

$$
\begin{align}
d = \sqrt{(2a)^2 + a^2} = \sqrt{5}|a|
\end{align}
$$

である．
二つの円が接するパターンは外接と内接があるから場合分けして考える．

### $1^\circ$ 外接する時

二つの円の半径の和が中心間距離$d$に等しいから

$$
\begin{align}
& \sqrt{5} + \sqrt{5}\sqrt{a^2 - 4a + 5} = \sqrt{5}|a| \\& \sqrt{a^2 - 4a + 5} = |a| - 1
\end{align}
$$

である．$|a| \ge 1$ のもとで両辺二乗して整理すると $a = 2$ を得る．

### $2^\circ$ 内接する時

二つの円の半径の差が中心間距離$d$に等しいから

$$
\begin{align}
| \sqrt{5} - \sqrt{5}\sqrt{a^2 - 4a + 5} | = \sqrt{5}|a|
\end{align}
$$

両辺 $0$ 以上だから二乗して

$$
\begin{align}
a^2 - 4a + 5 + 1 - 2\sqrt{a^2 - 4a + 5} = a^2 \\\sqrt{a^2 - 4a + 5} = 3 - 2a
\end{align}
$$

$a \le \frac{3}{2}$ のもとで両辺二乗して

$$
\begin{align}
& a^2 - 4a + 5 = 4a^2 - 12a + 9 \\& 3a^2 - 8a + 4 = 0 \\& (3a - 2)(a - 2) = 0 \\\therefore& a = \frac{2}{3}, 2
\end{align}
$$

$a \le \frac{3}{2}$ をみたすのは $a = \frac{2}{3}$である．

以上から求める値は 

$$
\begin{align}
a = \frac{2}{3}, 2
\end{align}
$$

である．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1962/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $a=2$で二つの円が外接する場合</figcaption>
</figure>

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1962/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $a=\dfrac{2}{3}$で二つの円が内接する場合</figcaption>
</figure>