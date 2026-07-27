---
university: "titech"
category: "zenki"
year: "1980"
question: "2"
type: "solution"
title: "TITECH 1980 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$|BD|=x$ とする．$\angle CBD=\theta$ とする．この時題意から $\angle ACB=2\theta$ である．$|CD|=y$ とする．まず，$\triangle ABC$ の成立条件から

$$
\begin{align*}
0<2\theta<\frac{\pi}{2}\quad\therefore\ 0<\theta<\frac{\pi}{4}\quad\cdots\text{①}
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1980/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $\triangle ABC$と点$D$の位置関係</figcaption>
</figure>

$\triangle BCD$ に正弦定理を用いて，

$$
\begin{align*}
\frac{x}{\sin2\theta}=\frac{1}{\sin(\pi-3\theta)}=\frac{1}{\sin3\theta}\quad\therefore\ x=\frac{\sin2\theta}{\sin3\theta}\quad\cdots\text{②}
\end{align*}
$$

以下 $S=\sin\theta,\ C=\cos\theta$ とする．$\sin2\theta=2SC,\ \sin3\theta=3S-4S^3$ より，②から

$$
\begin{align*}
x=\frac{2SC}{3S-4S^3}=\frac{2C}{3-4S^2}=\frac{2C}{4C^2-1}
\end{align*}
$$

これは $C$ の単調減少関数であり，①とあわせて，

$$
\begin{align*}
\frac23<x<\sqrt2 \quad\left(\because\ \frac{2C}{4C^2-1}\xrightarrow{C\to\frac{\sqrt2}{2}+0}\sqrt2,\quad\frac{2C}{4C^2-1}\xrightarrow{C\to1-0}\frac23\right)
\end{align*}
$$