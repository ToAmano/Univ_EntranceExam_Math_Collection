---
university: "kyodai"
category: "kouki"
year: "1990"
question: "2"
type: "solution"
title: "KYODAI 1990 kouki Q2 (solution)"
---

## 【解】

  $f(x)$の一階微分は
  

$$
\begin{align*}
f'(x) = \frac{x\sin x-2(a-\cos x)}{x^3}
\end{align*}
$$

  であり，これが$0 < x \le \pi/2$で非負である条件を求めれば良い．

  この範囲では，$f'(x)$の符号は分子の符号と等しい．
  これを$g(x)$とおく．
  

$$
\begin{align*}
g(x) & = x\sin x - 2(a-\cos x)
\end{align*}
$$

  一階，二階微分は
  

$$
\begin{align*}
g'(x)  & = \sin x + x\cos x - 2\sin x                    \\
    g''(x) & = -x\sin x < 0 \quad(\because 0 < x \le\pi/2)
\end{align*}
$$

  より $g'(x)$ は区間内で単調減少で，かつ $g'(0) = 0$ から，区間内で$g'(x) < 0$である．
  つまり $g(x)$ は単調減少である．

  従って，$g(x)\ge 0$が成り立つ条件は
  

$$
\begin{align*}
g(x)
      & \ge g(\pi/2)               \\& = \frac{\pi}{2} - 2a \ge 0 \\\iff
    a & \le\frac{\pi}{4}
\end{align*}
$$

  である．

  従って，求める最大値は
  

$$
\begin{align*}
a=\frac{\pi}{4}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】