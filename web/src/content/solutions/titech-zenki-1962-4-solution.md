---
university: "titech"
category: "zenki"
year: "1962"
question: "4"
type: "solution"
title: "TITECH 1962 zenki Q4 (solution)"
---

{\bf［解］}

与式を $f(x,y)$ とおく．式を少し整理すると

$$
\begin{align}
f(x,y) = 2\sin x + \left(\cos y + \sqrt{3}\sin y\right)\cos x
\end{align}
$$

とかける．そこでまず$x$を固定して$y$を動かして最大最小を求めた後，$x$を動かして全体の最大最小を求める．新しく$y$に依存する部分だけを取り出して

$$
\begin{align}
g(y) = \cos y + \sqrt{3}\sin y
\end{align}
$$

とおくと，コーシーシュワルツの不等式から$g(y)$は

$$
\begin{align}
-2 \le\begin{pmatrix} 1 \\ \sqrt{3} \end{pmatrix}\cdot\begin{pmatrix} \cos y \\ \sin y \end{pmatrix}\le 2
\end{align}
$$

を満たす．左側の等号成立条件は

$$
\begin{align}
y = \frac{4\pi}{3}\label{eq:1}
\end{align}
$$

であり，右側の等号成立条件は

$$
\begin{align}
y = \frac{\pi}{3}\label{eq:2}
\end{align}
$$

である．

よって，$\cos x$の符号に応じて$x$を固定した時の$f(x,y)$の最大最小値は以下のように与えられる．
ただし三角関数の合成により

$$
\begin{align}
\begin{cases}
 2\sin x + 2 \cos x = 2\sqrt{2}\sin\left(x+\frac{\pi}{4}\right)\\
 2\sin x - 2 \cos x = 2\sqrt{2}\sin\left(x-\frac{\pi}{4}\right)
\end{cases}
\end{align}
$$

と書けることを利用した．

$$
\begin{align}
\max f(x,y) &= 
\begin{cases}
2\sqrt{2}\sin\left(x+\dfrac{\pi}{4}\right) & \left(0 \le x < \dfrac{\pi}{2}, \; \dfrac{3\pi}{2} < x \le 2\pi, y=\frac{\pi}{3} \text{ のとき}\right) \\[8pt]
2\sqrt{2}\sin\left(x-\dfrac{\pi}{4}\right) & \left(\dfrac{\pi}{2} \le x \le \dfrac{3\pi}{2}, y=\dfrac{4\pi}{3} \text{ のとき}\right)
\end{cases}\\[10pt]\min f(x,y) &= 
\begin{cases}
2\sqrt{2}\sin\left(x-\dfrac{\pi}{4}\right) & \left(0 \le x < \dfrac{\pi}{2}, \; \dfrac{3\pi}{2} < x \le 2\pi, y=\dfrac{4\pi}{3} \text{ のとき}\right) \\[8pt]
2\sqrt{2}\sin\left(x+\dfrac{\pi}{4}\right) & \left(\dfrac{\pi}{2} \le x \le \dfrac{3\pi}{2}, y=\frac{\pi}{3} \text{ のとき}\right)
\end{cases}
\end{align}
$$

この様子を図示すると以下のようになる．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1962/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $f$の最大最小の様子．</figcaption>
</figure>

従って最大最小を与える$x,y$は以下のようにまとめられる．

$$
\begin{align}
\begin{cases}
\max f = 2\sqrt{2} & \left( (x,y) = \left(\frac{\pi}{4}, \frac{\pi}{3}\right), \left(\frac{3}{4}\pi, \frac{4}{3}\pi\right) \right) \\[1ex]
\min f = -2\sqrt{2} & \left( (x,y) = \left(\frac{5}{4}\pi, \frac{\pi}{3}\right), \left(\frac{7}{4}\pi, \frac{4}{3}\pi\right) \right)
\end{cases}
\end{align}
$$