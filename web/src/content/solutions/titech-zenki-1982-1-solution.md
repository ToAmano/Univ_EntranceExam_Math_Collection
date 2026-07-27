---
university: "titech"
category: "zenki"
year: "1982"
question: "1"
type: "solution"
title: "TITECH 1982 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

図のように$\theta$をおく．又，$a_n$個の円の中心を$O_1\sim O_n$とする．半径1の円の中心を$O$として，図から，

$$
\begin{align*}
\sin\theta=\frac{\frac1n}{1+\frac1n}=\frac{1}{n+1}\quad\cdots\text{①}
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1982/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円の配置と角$\theta$</figcaption>
</figure>

又，題意から

$$
\begin{align*}
2a_n\cdot\theta\le2\pi<2(a_n+1)\theta
\end{align*}
$$

$$
\begin{align*}
\frac{\pi}{n\theta}-\frac1n\le\frac{a_n}{n}<\frac{\pi}{n\theta}\quad\cdots\text{②}\ (\because n>0)
\end{align*}
$$

ここで①から$n\to\infty$の時$\theta\to0$で，これと①から

$$
\begin{align*}
\frac{1}{n\theta}=\frac{1}{n\sin\theta}\cdot\frac{\sin\theta}{\theta}=\frac{n+1}{n}\cdot\frac{\sin\theta}{\theta}=\frac{1+\frac1n}{1}\cdot\frac{\sin\theta}{\theta}\longrightarrow1 \quad(n\to\infty)
\end{align*}
$$

だから②とはさみうちから

$$
\begin{align*}
\frac{a_n}{n}\longrightarrow\pi
\end{align*}
$$