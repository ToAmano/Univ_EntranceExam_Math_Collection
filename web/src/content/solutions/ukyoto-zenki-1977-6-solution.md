---
university: "ukyoto"
category: "zenki"
year: "1977"
question: "6"
type: "solution"
title: "UKYOTO 1977 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] (1) (2) (3) に代入して
\begin{equation}
\begin{cases}
-f''(x) \ge f(x) & \dots \text{①} \\
f'(0) = 0 & \dots \text{②} \\
0 \le x \le a \implies f(x) > 0 & \dots \text{③}
\end{cases}
\end{equation}

1.  $0 \le t \le a$ の時、①, ③から
    

$$
\begin{align*}
-f''(t) > 0
\end{align*}
$$

    $[0, x]\ (0 \le x \le a)$ で積分して
    

$$
\begin{align*}
f'(0) - f'(x) > 0 \iff 0 > f'(x) \quad (\because \text{②}) \quad \dots \text{④}
\end{align*}
$$

    だから $x = a$ として
    

$$
\begin{align*}
0 > f'(a) \iff 0 < g(a)
\end{align*}
$$

2.  $a \le y \le a + \frac{f(a)}{-f'(a)}$ で常に $f(y) > 0$ ($f(0) > 0$ と仮定する。③とあわせて
    

$$
\begin{align*}
\text{「 } 0 \le x \le a - \frac{f(a)}{f'(a)} \text{ で常に } f(x) > 0 \text{ 」} \quad \dots \text{⑤}
\end{align*}
$$

    である。①から、同区間で
    

$$
\begin{align*}
f''(t) < 0 \quad \therefore f(t) \text{ は単調減少} \quad \dots \text{⑥}
\end{align*}
$$

    となり、④から、$f'(t) \le 0$ つまり $f(t)$ は単調減少である。ここで $f(x)$ には平均値の定理が適用できて、
    

$$
\begin{align*}
f\left(a - \frac{f(a)}{f'(a)}\right) - f(0) = -\frac{f(a)}{f'(a)} f'(c) \quad \left(a < c < a - \frac{f(c)}{f'(c)}\right)
\end{align*}
$$

    なる $c$ が存在する。変形して
    

$$
\begin{align*}
f\left(a - \frac{f(a)}{f'(a)}\right) = \frac{f(a)}{f'(a)} \{ f'(a) - f'(c) \} \quad \dots \text{⑦}
\end{align*}
$$

    ここで、⑤, ⑥から
    

$$
\begin{align*}
f\left(a - \frac{f(a)}{f'(a)}\right) > 0, \quad f(a) > 0, \quad f'(a) < 0
\end{align*}
$$

    だから ⑦より
    

$$
\begin{align*}
f'(a) - f'(c) < 0 \iff f'(a) < f'(c)
\end{align*}
$$

    しかし、これは ⑥及び $a < c$ に反し矛盾。以上から $a \le y \le a - \frac{f(a)}{f'(a)}$ に $f(y) = 0$ なる $y$ がある。