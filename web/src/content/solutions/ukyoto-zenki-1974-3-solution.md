---
university: "ukyoto"
category: "zenki"
year: "1974"
question: "3"
type: "solution"
title: "UKYOTO 1974 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $f_q(x) = x^4 - 6p^2 x^2 - 8q^3 x$ とおく. ($p > 0, q \ge 0$)

$f_q'(x) = 4x^3 - 12p^2 x - 8q^3$ だから, $q=0$ の時, 下表を得る

| $x$ | $\dots$ | $-\sqrt{3}p$ | $\dots$ | $0$ | $\dots$ | $\sqrt{3}p$ | $\dots$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $f'$ | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $f$ | $\searrow$ |  | $\nearrow$ |  | $\searrow$ |  | $\nearrow$ |

従って, $A$ の $x$ 座標は $-\sqrt{3}p \; (\equiv x_0)$ である. 又, $f_q''(x) = 12(x^2 - p^2)$ から下表を得る

|  $x$  |  $\dots$   |     $-p$     |  $\dots$   | $p$ |  $\dots$   |
|:-------:|:------------:|:--------------:|:------------:|:-----:|:------------:|
| $f''$ |    $+$     |     $0$      |    $-$     | $0$ |    $+$     |
| $f'$  | $\nearrow$ | 8($p^3-q^3$) | $\searrow$ |  負   | $\nearrow$ |

従って $q$ の値により下表をえる

\bigskip

$1^\circ$ $p > q$ の時

$f_q'(-p) > 0$ から, $f_q'(x) = 0$ となる $x$ が 3つある ($\alpha < \beta < \gamma$ とする)

| $x$ | $\dots$ | $\alpha$ | $\dots$ | $\beta$ | $\dots$ | $\gamma$ | $\dots$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $f'$ | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $f$ | $\searrow$ |  | $\nearrow$ |  | $\searrow$ |  | $\nearrow$ |

この時 $A$ が右のくぼみに落ちるのは, $\beta \le -\sqrt{3}p \le \gamma$ の時である. $\quad \cdots \text{①}$

しかし, 本から $-p < \beta$ であり, 又 $p > 0$ から $-\sqrt{3}p < -p$ だから ①がみたされることはなく, 矛盾.

\bigskip

$2^\circ$ $p \le q$ の時

$f_q'(-p) \le 0$ から, $f_q'(x) = 0$ となる $x$ が唯一存在する ($\alpha$ とする)

| $x$  |  $\dots$   | $\alpha$ |  $\dots$   |
|:------:|:------------:|:----------:|:------------:|
| $f'$ |    $-$     |   $0$    |    $+$     |
| $f$  | $\searrow$ |            | $\nearrow$ |

よって, $A$ が右のくぼみに落ちるのは $-\sqrt{3}p \le \alpha$ つまり $f_q'(-\sqrt{3}p) \le 0$ の時,

$$
\begin{align*}
f_q'(-\sqrt{3}p) = -8q^3 \le 0 \quad \therefore q \ge 0
\end{align*}
$$

したがって, $0 < p$ から $p \le q$ の時, $A$ が右のくぼみにおちる.

以上 $1^\circ, 2^\circ$ から求める $\min q = p$ である.

\begin{tikzpicture}[scale=0.8]
    \draw[->] (-3,0) -- (3,0) node[right] {$x$};
    \draw[->] (0,-4) -- (0,2) node[above] {$y$};
    \draw[domain=-2.1:2.1,smooth,variable=\x,thick,blue] plot ({\x}, {0.3*(\x+1.5)*(\x+1.5)*(\x-1.8)});
    \fill (-2,0) circle (1.5pt) node[below] {$-\sqrt{3}p$};
    \fill (-1.5,0) circle (1.5pt) node[below] {$-p$};
    \fill (1.8,0) circle (1.5pt) node[below] {$2p$};
    \node[below right] at (0,0) {$O$};
\end{tikzpicture}

$\left[\text{この時, } f'(x) = 4(x^3 - 3p^2 x - 2p^3) = 4(x+p)^2 (x-2p) \text{ となり,}\right]$ $\Rightarrow$ 予想通り!