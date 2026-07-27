---
university: "titech"
category: "zenki"
year: "1969"
question: "2"
type: "solution"
title: "TITECH 1969 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $\triangle BCD$ は右下図

1.  余弦定理より $\overline{BC}^2 = 16 + 9 - 2 \cdot 4 \cdot 3 \cdot \frac{1}{2} = 13$

2.  $\overline{BD} = \sqrt{41}$, $\overline{CD} = \sqrt{34}$

$BE = x$ とおく．($x$ は符号付き, $E$ が $BC$ 上の時正)

$$
\begin{align*}
DE^2 = 41 - x^2 = 34 - (\sqrt{13} - x)^2 \quad\dots\text{①}
\end{align*}
$$

で

$$
\begin{align*}
41 - x^2 = -x^2 + 2\sqrt{13}x + 21
\end{align*}
$$

$$
\begin{align*}
\therefore x = \frac{10}{\sqrt{13}}
\end{align*}
$$

だから①より

$$
\begin{align*}
\overline{DE}^2 = 41 - x^2 = \frac{433}{13}
\end{align*}
$$

$$
\begin{align*}
\therefore\overline{DE} = \sqrt{\frac{433}{13}}\quad(> 0) \quad\text{\dots (1)}
\end{align*}
$$

(2) $\triangle BCD$ の面積は $S = \frac{1}{2} \overline{BC} \cdot \overline{DE} = \frac{1}{2}\sqrt{433}$ だから $ABCD$ の体積を 2通りで表して，

$$
\begin{align*}
\frac{\sqrt{433}}{2}\cdot\frac{1}{3}\cdot\overline{AF} = \frac{1}{2}\cdot\frac{1}{3}\cdot 3 \cdot 4 \cdot 5 \sin\frac{\pi}{3}
\end{align*}
$$

$$
\begin{align*}
\therefore\overline{AF} = 30 \sqrt{\frac{3}{433}}
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1969/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 四面体$ABCP$の辺の長さ</figcaption>
</figure>