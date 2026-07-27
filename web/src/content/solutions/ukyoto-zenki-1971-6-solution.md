---
university: "ukyoto"
category: "zenki"
year: "1971"
question: "6"
type: "solution"
title: "UKYOTO 1971 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

時刻 $t$ の $P, Q$ の座標は

$$
\begin{align*}
P_t (\cos \pi t, \sin \pi t), \quad Q_t (a, vt) \quad (0 < v < a\pi)
\end{align*}
$$

である.

1.  $\vec{OP_t} \parallel \vec{O Q_t} \iff v t \cos \pi t - a \sin \pi t = 0 \quad \dots \text{① である.}$

    ①の左辺を $f(t)$ とおくと
    

$$
\begin{align*}
f'(t) = v \cos \pi t - \pi v t \sin \pi t - \pi a \cos \pi t
\end{align*}
$$

    

$$
\begin{align*}
= -(\pi a - v) \cos \pi t - \pi v t \sin \pi t
\end{align*}
$$

    である. $A = \sqrt{(\pi a - v)^2 + (\pi v t)^2} \ (>0)$ とおくと
    

$$
\begin{align*}
f'(t) = -A \sin(\pi t + \alpha)
\end{align*}
$$

    とおける. ただし $\alpha$ は $\cos \alpha = \frac{\pi v t}{A} (>0)$, $\sin \alpha = \frac{\pi a - v}{A} (>0)$ をみたす $0 < \alpha < \frac{\pi}{2}$ なる角であって, $n < t \le n+1$ の時,
    

$$
\begin{align*}
n\pi + \alpha \le \pi t + \alpha \le (n+1)\pi + \alpha
\end{align*}
$$

    となり, $f'(t)$ は区間内で唯一, 符号をかえる点を持つ.

    従ってこの時の $t$ を $t'$ として下表をえる ($k \in \mathbb{Z}_{\ge 0}$).

    
    

| $t$  | $2k$ |  $\dots$   | $t'$ |  $\dots$   | $2k+1$ |
|:------:|:------:|:------------:|:------:|:------------:|:--------:|
| $f'$ |        |    $-$     | $0$  |    $+$     |          |
| $f$  |   正   | $\searrow$ |        | $\nearrow$ |    負    |

    
    

| $t$  | $2k+1$ |  $\dots$   | $t'$ |  $\dots$   | $2k+2$ |
|:------:|:--------:|:------------:|:------:|:------------:|:--------:|
| $f'$ |          |    $+$     | $0$  |    $-$     |          |
| $f$  |    負    | $\nearrow$ |        | $\searrow$ |    正    |

    

    従って, $n \le t_n \le n+1$ の間に $f(t_n) = 0$ をみたす $t_n$ が唯一ある. \hfill 固

2.  $n \le t_n \le n+1 \quad \dots \text{②である((1)から)}$

    

$$
\begin{align*}
v t_n \cos \pi t_n - a \sin \pi t_n = 0
\end{align*}
$$

    

$$
\begin{align*}
\cos \pi t_n = \frac{a \sin \pi t_n}{v t_n} \to 0 \quad (n \to \infty, \text{②から})
\end{align*}
$$

    ②からしたがって
    

$$
\begin{align*}
t_n \to n + \frac{1}{2} \quad (n \to \infty)
\end{align*}
$$

    だから $t_n - n \to \frac{1}{2} \quad (n \to \infty)$ である.