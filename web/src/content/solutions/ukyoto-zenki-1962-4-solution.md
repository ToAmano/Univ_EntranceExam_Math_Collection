---
university: "ukyoto"
category: "zenki"
year: "1962"
question: "4"
type: "solution"
title: "UKYOTO 1962 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

| $\begin{cases} C < a+b \text{ の時，} (p, q) \text{ は存在する} \\ C \ge a+b \text{ の時，} \quad \text{＂} \quad \text{しない} \end{cases}$ |
|:---|

［解］$f(x) = x(x-a)(b-x) - px^2 + qx$ に対し，$x \le C$ で常に $f(x) \ge 0$ となる $(p, q)$ をさがせばよい。

$$
\begin{align*}
f'(x) = -3x^2 + 2(a+b-p)x - ab + q \quad \dots \text{①}
\end{align*}
$$

さて，2つの関数の解は $x = 0, a, b$ と $x = 0, \frac{q}{p}$ だからグラフは右のようになる。したがって，$x=0$ で接することが必要で，

$$
\begin{align*}
-q = -ab \iff q = ab \quad \dots \text{②}
\end{align*}
$$

だから①に代入して

$$
\begin{align*}
f'(x) = x [ -3x + 2(a+b-p) ]
\end{align*}
$$

従って $0 < a+b-p$ となる $p$ をとると極大を与える。

\begin{tikzpicture}[scale=0.8]
  \draw[->] (-0.5,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
  \draw[domain=0:2.5, samples=50, smooth, thick] plot (\x, {\x*(\x-1)*(2-\x)});
\end{tikzpicture}

| $x$  |    $0$     | $\dots$ | $\frac{2}{3}(a+b-p)$ | $\dots$ |              |
|:------:|:------------:|:---------:|:----------------------:|:---------:|:------------:|
| $f'$ |    $-$     |   $0$   |         $+$          |   $0$   |    $-$     |
| $f$  | $\searrow$ |   $0$   |      $\nearrow$      |           | $\searrow$ |

ア $C < \frac{2}{3}(a+b)$ の時，

$C \le \frac{2}{3}(a+b-p)$ となるよう $p (>0)$ がとれて，この時 $f(x)$ は $x=0$ で $\min 0$ をとるから，題意を満たす $p, q$ が存在する。

イ $C \ge \frac{2}{3}(a+b)$ の時，

$\frac{2}{3}(a+b-p) < C$ から $f(x)$ は，$x=0$ 又は $x=C$ で $\min$ ををとる。

$$
\begin{align*}
f(C) &= -C(C-a)(C-b) - pC^2 + abC \\&= C [ -(C-a)(C-b) - pC + ab ]\\&= C^2 [ -C + (a+b-p) ]
\end{align*}
$$

だから，

1.  $C < a+b$ の時，$f(C) \ge 0$ となる $p$ がとれて，題意を満たす $(p, q)$ が存在。

2.  $C \ge a+b$ の時，$f(C) < 0$ から不適。

一方，$a+b-p \le 0$ となる $p$ をとったとき $0 \le x \le C$ で $f(x)$ は単調減少。かつ $f(0) = 0$ から，これは不適。

従って，コタエは

$$
\begin{align*}
\begin{cases}
C < a+b \text{ の時，} (p, q) \text{ は存在する} \\
C \ge a+b \text{ の時，存在しない}
\end{cases}
\end{align*}
$$