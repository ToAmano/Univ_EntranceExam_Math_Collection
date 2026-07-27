---
university: "ukyoto"
category: "zenki"
year: "1975"
question: "2"
type: "solution"
title: "UKYOTO 1975 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

1.  $x \ge 0$ から AM-GMより
    

$$
\begin{align*}
\frac{x+1}{2} \ge \sqrt{x} \quad \dots \text{①}
\end{align*}
$$

2.  ①から $[0, k]$ の時
    

$$
\begin{align*}
\sqrt{x}\left(1 - \frac{x}{k}\right)^k \le \frac{1}{2}(x+1)\left(1 - \frac{x}{k}\right)^k
\end{align*}
$$

    両辺同じ区間で積分し、与式左辺を $A$ として
    

$$
\begin{align*}
A < \frac{1}{2}\int_0^k (x+1)\left(1 - \frac{x}{k}\right)^k dx
\end{align*}
$$

    $t = 1 - \frac{x}{k}$ とおくと $\frac{dt}{dx} = -\frac{1}{k}$、$x : 0 \to k$ で $t : 1 \to 0$ だから
    

$$
\begin{align*}
A &< \frac{1}{2}\int_1^0 \{1 + k(1-t)\} t^k \cdot(-k) dt \\&= \frac{1}{2} k \int_0^1 \{(1+k)t^k - k t^{k+1}\} dt \\&= \frac{1}{2} k \left[ t^{k+1} - \frac{k}{k+2} t^{k+2}\right]_0^1 \\&= \frac{1}{2} k \cdot\frac{2}{k+2} = \frac{1}{1 + 2/k} < 1 \quad(\because k \in\mathbb{N})
\end{align*}
$$