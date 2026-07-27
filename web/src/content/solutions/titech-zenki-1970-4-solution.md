---
university: "titech"
category: "zenki"
year: "1970"
question: "4"
type: "solution"
title: "TITECH 1970 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

円の半径を $1$ とする. この円に内接する正 $k$ 角形の面積 $S_k$ は,

$$
\begin{align*}
S_k = k \cdot\sin\frac{\pi}{k}\cos\frac{\pi}{k} = \frac{k}{2}\sin\frac{2\pi}{k}.
\end{align*}
$$

だから,

$$
\begin{align*}
&\frac{2}{3} S_{3n} < S_n < \frac{\sqrt{3}}{2} S_{2n}\\\iff&\frac{2}{3}\cdot\frac{3n}{2}\sin\frac{2\pi}{3n} < \frac{n}{2}\sin\frac{2\pi}{n} < \frac{\sqrt{3}}{2}\cdot\frac{2n}{2}\sin\frac{2\pi}{2n}\\\iff&\sin\frac{2\pi}{3n} < \frac{1}{2}\sin\frac{2\pi}{n} < \frac{\sqrt{3}}{2}\sin\frac{2\pi}{2n}\qquad\dots\text{\textcircled{1}}
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1970/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 角度の大小関係を示す図</figcaption>
</figure>

$t = \sin \frac{2\pi}{3n}$ とおく. \textcircled{1}の左側から

$$
\begin{align*}
t < \frac{1}{2}(3t - 4t^3)
\end{align*}
$$

$t > 0$ から,

$$
\begin{align*}
2 < 3 - 4t^2 \quad\therefore 0 < t < \frac{1}{2} = \sin\frac{\pi}{6}\qquad\dots\text{\textcircled{2}}
\end{align*}
$$

\textcircled{1}の右側から

$$
\begin{align*}
2 \sin\frac{\pi}{n}\cos\frac{\pi}{n} < \sqrt{3}\sin\frac{\pi}{n}
\end{align*}
$$

$\sin \frac{\pi}{n} > 0$ から

$$
\begin{align*}
\cos\frac{\pi}{n} < \frac{\sqrt{3}}{2}\qquad\dots\text{\textcircled{3}}
\end{align*}
$$

\textcircled{2}, \textcircled{3}を満たすのは,

$$
\begin{align*}
\frac{2\pi}{3n} < \frac{\pi}{6}\quad\land\quad\frac{\pi}{6} < \frac{\pi}{n}
\end{align*}
$$

$$
\begin{align*}
\iff 4 < n < 6 \quad(\because n \in\mathbb{N})
\end{align*}
$$

$$
\begin{align*}
\iff n = 5.
\end{align*}
$$