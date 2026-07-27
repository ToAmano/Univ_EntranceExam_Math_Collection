---
university: "ukyoto"
category: "zenki"
year: "1973"
question: "2"
type: "solution"
title: "UKYOTO 1973 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $e(\theta) = \cos\theta + i\sin\theta$ とする。1以外の2根を $\alpha, \beta$ とすると、

$$
\begin{align*}
\alpha = e(\theta_1), \quad \beta = e(\theta_2) \qquad (0 \le \theta_1 \le \theta_2 < 2\pi)
\end{align*}
$$

とおける。解と係数の関係から、

$$
\begin{align*}
p &= -(1 + e(\theta_1) + e(\theta_2)) \quad\dots\text{①}\\
q &= e(\theta_1) + e(\theta_2) + e(\theta_1)e(\theta_2) \quad\dots\text{②}\\
r &= -e(\theta_1)e(\theta_2) = -e(\theta_1 + \theta_2) \quad\dots\text{③}
\end{align*}
$$

1.  $\alpha, \beta \in \mathbb{R}$ の時\\
    $(\alpha, \beta) = (1, 1), (1, -1), (-1, -1)$ で、①〜③より、
    

$$
\begin{align*}
(p, q, r) = (1, -1, -1), (-1, -1, 1), (-3, 3, -1)
\end{align*}
$$

2.  $\alpha, \beta \notin \mathbb{R}$ の時\\
    $p, q, r \in \mathbb{R}$ から $\beta = \bar{\alpha}$ となり、$0 \le \theta_1 \le \theta_2 < 2\pi$ とあわせて、$\theta_2 = 2\pi - \theta_1$, $0 < \theta_1 < \pi$ とできる。
    この時
    

$$
\begin{align*}
\begin{cases}
    r = -e(2\pi) = -1 \\
    p = -(1 + 2\cos\theta_1) \\
    q = 1 + 2\cos\theta_1
    \end{cases}
\end{align*}
$$

    だから、
    

$$
\begin{align*}
p = -q, \quad r = -1, \quad -1 \le q \le 3
\end{align*}
$$

以上から

$$
\begin{align*}
(p = -q, \ r = -1, \ -1 \le q \le 3) \quad \text{or} \quad (p, q, r) = (-1, -1, 1)
\end{align*}
$$