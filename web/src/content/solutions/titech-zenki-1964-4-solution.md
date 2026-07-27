---
university: "titech"
category: "zenki"
year: "1964"
question: "4"
type: "solution"
title: "TITECH 1964 zenki Q4 (solution)"
---

## 【解】

$\angle AOQ = \theta \quad (0 < \theta \leqq \pi/2)$ とおく. この時, かかる時間 $f(\theta)$ は

$$
\begin{align}
f(\theta) = \frac{\breve{AQ}}{2} + \frac{\overline{BQ}}{1}\qquad\dots\text{\textcircled{1}}
\end{align}
$$

である.

$$
\begin{align*}
\breve{AQ} = \sqrt{3} \theta \qquad \dots \text{\textcircled{2}}
\end{align*}
$$

で, $\triangle OBQ$ に余弦定理を用いて,

$$
\begin{align*}
\overline{BQ}^2 = 1 + 3 - 2\sqrt{3} \cos\left(\frac{\pi}{2} - \theta\right) = 4 - 2\sqrt{3} \sin\theta
\end{align*}
$$

$$
\begin{align*}
\therefore \overline{BQ} = \sqrt{4 - 2\sqrt{3} \sin\theta} \qquad \dots \text{\textcircled{3}}
\end{align*}
$$

だから, \textcircled{2}\textcircled{3}を\textcircled{1}に代入して

$$
\begin{align*}
f(\theta) = \frac{\sqrt{3}}{2} \theta + \sqrt{4 - 2\sqrt{3} \sin\theta}
\end{align*}
$$

$$
\begin{align*}
f'(\theta) = \frac{\sqrt{3}}{2} + \frac{-2\sqrt{3}\cos\theta}{2\sqrt{4 - 2\sqrt{3}\sin\theta}}
\end{align*}
$$

とする.

$$
\begin{align*}
f'(\theta) \geqq 0 \iff \sqrt{4 - 2\sqrt{3} \sin\theta} \geqq 2 \cos\theta
\end{align*}
$$

$0 \leqq \theta \leqq \pi/2$ から両辺 $0$ 以上だから2乗して,

$$
\begin{align*}
4 - 2\sqrt{3} \sin\theta \geqq 4 \cos^2\theta = 4 - 4 \sin^2\theta
\end{align*}
$$

$$
\begin{align*}
\therefore \frac{\sqrt{3}}{2} \leqq \sin\theta \leqq 1 \quad (\because 0 \leqq \sin\theta \leqq 1)
\end{align*}
$$

$$
\begin{align*}
\therefore \frac{\pi}{3} \leqq \theta \leqq \frac{\pi}{2}
\end{align*}
$$

となるので, 下表をうる.

<div id="tab_1" class="table-wrapper">

| $\theta$ | $0$ |  $\dots$   | $\pi/3$ |  $\dots$   | $\pi/2$ |
|:----------:|:-----:|:------------:|:---------:|:------------:|:---------:|
|   $f'$   |       |    $-$     |   $0$   |    $+$     |           |
|   $f$    |       | $\searrow$ |           | $\nearrow$ |           |

</div>

したがって, もとめる $Q$ の位置は, $\angle QOA = \dfrac{\pi}{3}$ となる場所.

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1964/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>