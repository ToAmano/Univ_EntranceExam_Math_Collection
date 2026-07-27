---
university: "titech"
category: "zenki"
year: "1965"
question: "3"
type: "solution"
title: "TITECH 1965 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $0 \le x < \pi, 0 \le y < \pi \dots \text{①} \quad \alpha = x + y, \beta = x - y$ とおくと条件から

$$
\begin{align*}
\sin\alpha\cos\beta = \frac{1}{2}\quad\dots\text{②}
\end{align*}
$$

$x = \frac{\alpha+\beta}{2}, y = \frac{\alpha-\beta}{2}$ を①に代入して

$$
\begin{align*}
\begin{cases}
0 \le \alpha + \beta < 2\pi \\
0 \le \alpha - \beta < 2\pi
\end{cases}\quad\dots\text{③}
\end{align*}
$$

③を図示すると右図で，この対称性および $\cos(-\beta) = \cos\beta$ から，$\beta \ge 0$ で考えれば良い．この時

$$
\begin{align*}
0 \le\beta < \pi, \quad\beta\le\alpha < -\beta + 2\pi\quad\dots\text{④}
\end{align*}
$$

まず，$|\beta|$ の最小値について考える．等号成立時，$0 \le \alpha < 2\pi$ で，$\alpha = \frac{\pi}{6}, \frac{5}{6}\pi$ とすれば②をみたす．
この時 $(x, y) = (\frac{\pi}{12}, \frac{\pi}{12}), (\frac{5}{12}\pi, \frac{5}{12}\pi)$ である $\dots \text{⑤}$

次に，$|\beta|$ の最大値について考える．④の区間内では

$$
\begin{align*}
\begin{cases}
0 \le \beta \le \frac{\pi}{2} \text{ の時} \quad \frac{1}{2} < \sin\alpha \le 1 \quad \dots \text{⑥} \\
\frac{\pi}{2} \le \beta < \pi \text{ の時} \quad -\sin\beta < \sin\alpha \le \sin\beta \quad \dots \text{⑦}
\end{cases}
\end{align*}
$$

となる．⑥の時 $\cos\beta = \frac{1}{2} \therefore \beta = \frac{\pi}{3}, \alpha = \frac{\pi}{2}$ の時 $|\beta|$ は最大である． $\dots \text{⑧}$

⑦の時 $\sin\alpha \cos\beta$ の値域は

$$
\begin{align*}
\frac{1}{2}\sin 2\beta\le\sin\alpha\cos\beta < -\frac{1}{2}\sin 2\beta
\end{align*}
$$

だから②から

$$
\begin{align*}
\sin 2\beta\le 1 < -\sin 2\beta
\end{align*}
$$

これを満たす $\beta$ は存在しない． $\dots \text{⑨}$

⑧, ⑨および対称性から，$|\beta|$ が最大の時 $(\alpha, \beta) = (\frac{\pi}{2}, \pm \frac{\pi}{3})$ でこの時

$$
\begin{align*}
(x, y) = (\frac{5}{12}\pi, \frac{1}{12}\pi), (\frac{1}{12}\pi, \frac{5}{12}\pi) \text{ である．}\quad\dots\text{⑩}
\end{align*}
$$

⑤, ⑩から，もとめるのは

$$
\begin{align*}
(x, y) = \left(\frac{1}{12}\pi, \frac{1}{12}\pi\right), \left(\frac{5}{12}\pi, \frac{5}{12}\pi\right), \left(\frac{1}{12}\pi, \frac{5}{12}\pi\right), \left(\frac{5}{12}\pi, \frac{1}{12}\pi\right)
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1965/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $(\alpha,\beta)$平面における条件の図示</figcaption>
</figure>