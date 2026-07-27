---
university: "titech"
category: "zenki"
year: "1970"
question: "5"
type: "solution"
title: "TITECH 1970 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

1.  帰納的に示す. $n=1$ の時は成立するので, 以下 $n=k \in \mathbb{N}$ での成立を仮定する.
    

$$
\begin{align*}
|\sin(k+1)\theta| \leqq |\sin k\theta||\cos\theta| + |\cos k\theta||\sin\theta| \leqq k\sin\theta + \sin\theta = (k+1)\sin\theta
\end{align*}
$$

    から $n=k+1$ でも成立. よって示された.

2.  $0 \leqq f(\theta) \quad \dots \text{\textcircled{1}}$
    

$$
\begin{align*}
\int_0^\pi f(\theta) \sin\theta\, d\theta = 1 \quad\dots\text{\textcircled{2}}
\end{align*}
$$

    (1)及び\textcircled{1}から, $0 \leqq \theta \leqq \pi$ の時
    

$$
\begin{align*}
f(\theta) \sin n\theta\leqq f(\theta) |\sin n\theta| \leqq n f(\theta) \sin\theta
\end{align*}
$$

    だから, 同区間で積分して, \textcircled{2}から,
    

$$
\begin{align*}
\int_0^\pi f(\theta) \sin n\theta\, d\theta\leqq n.
\end{align*}
$$