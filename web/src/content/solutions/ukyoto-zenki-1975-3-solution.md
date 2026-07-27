---
university: "ukyoto"
category: "zenki"
year: "1975"
question: "3"
type: "solution"
title: "UKYOTO 1975 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] 題意から

$$
\begin{align*}
\begin{cases}
2\beta = \alpha + \gamma \quad \dots \text{①} \\
\sin^2\beta = \sin\alpha \sin\gamma \quad \dots \text{②}
\end{cases}
\end{align*}
$$

①を②に代入

$$
\begin{align*}
\sin^2 \frac{\alpha+\gamma}{2}&= 2\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}\sin\frac{\gamma}{2}\cos\frac{\gamma}{2}\\&= \frac{1}{2}\left[\sin\frac{\alpha+\gamma}{2} + \sin\frac{\alpha-\gamma}{2}\right]\left[\sin\frac{\alpha+\gamma}{2} - \sin\frac{\alpha-\gamma}{2}\right]
\end{align*}
$$

$t = \frac{\alpha+\gamma}{2}, s = \frac{\alpha-\gamma}{2}$ とおく。

$$
\begin{align*}
\sin^2 t + \sin^2 s = 0 \quad \dots \text{③}
\end{align*}
$$

$\sin t, \sin s \in \mathbb{R}$ から、③が成立するのは

$$
\begin{align*}
\sin t = \sin s = 0
\end{align*}
$$

$$
\begin{align*}
\therefore \frac{\alpha+\gamma}{2} = n\pi, \quad \frac{\alpha-\gamma}{2} = k\pi \quad (n, k \in \mathbb{Z})
\end{align*}
$$

の時である。解いて

$$
\begin{align*}
\alpha = (n+k)\pi, \quad \gamma = (n-k)\pi
\end{align*}
$$

①に代入して

$$
\begin{align*}
\beta = n\pi
\end{align*}
$$

従って、題意のようになるのは、$n, k \in \mathbb{Z}$ として

$$
\begin{align*}
(\alpha, \beta, \gamma) = ((n+k)\pi, n\pi, (n-k)\pi)
\end{align*}
$$