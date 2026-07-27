---
university: "utokyo"
category: "zenki"
year: "1997"
question: "2"
type: "solution"
title: "UTOKYO 1997 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

**[解1]** 

$$
\begin{align*}
(\text{与式}) \iff \left( \frac{n^2}{2n+1} - m \right) a + m^2 + m > 0 \quad \cdots \text{①}
\end{align*}
$$

ここで, $f(m) = -\frac{m^2+m}{A-m} \quad \left(A = \frac{n^2}{2n+1}\right)$ とおく.

$$
\begin{align*}
f(m) = +\left( m+A+1 + \frac{A(A+1)}{m-A} \right)
\end{align*}
$$

$$
\begin{align*}
f'(m) = +\left( \frac{m^2-2Am+A}{(m-A)^2} \right)
\end{align*}
$$

より, 下表を与える.

| $m$ | $\dots$ | $-\frac{n}{2n+1}$ | $\dots$ | $A$ | $\dots$ | $n$ | $\dots$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $f'$ | $+$ | $0$ | $-$ | / | $-$ | $0$ | $+$ |
| $f$ | $\nearrow$ | $\frac{1}{2n+1}$ | $\searrow$ | / | $\searrow$ | $2n+1$ | $\nearrow$ |

\bigskip

①が全ての $m \in \mathbb{Z}$ で成り立つ条件は

$$
\begin{align*}
\begin{cases}
A - m > 0 \iff A > m \text{ を満たす任意の } m \text{ で } a > f(m) \\
A - m = 0 \text{ の時, } m > 0 \text{ だから ①は必ず成立} \\
A - m < 0 \iff A < m \text{ を満たす任意の } m \text{ で } a < f(m)
\end{cases}
\end{align*}
$$

したがって, $y=f(x)$ のグラフから

$$
\begin{align*}
0 < a < 2n+1
\end{align*}
$$

\begin{tikzpicture}[scale=1.0, >=stealth]
\draw[->] (-2.5,0) -- (3.5,0) node[right] {$x$};
\draw[->] (0,-2.5) -- (0,3.5) node[above] {$y$};
\node[below left] at (0,0) {$O$};

\draw[dashed] (1.2,-2.5) -- (1.2,3.5) node[above] {$A$};
\draw[domain=-2.3:0.7, samples=50, smooth, thick] plot (\x, {(\x*\x+\x)/(\x-1.2)});
\draw[domain=1.6:3.2, samples=50, smooth, thick] plot (\x, {(\x*\x+\x)/(\x-1.2)});

\node[below] at (-1,0) {$-\frac{n}{2n+1}$};
\node[above left] at (0, 0.3) {$\frac{1}{2n+1}$};
\node[below] at (2.2,0) {$n$};
\node[right] at (0, 2.2) {$2n+1$};
\draw[dotted] (2.2,0) -- (2.2,2.2) -- (0,2.2);
\end{tikzpicture}

\bigskip

**[解2]** $f(x) = x^2 - (a-1)x + Aa$ とおく $\left(A = \frac{n^2}{2n+1}\right)$. $f(x)=0$ の判別式 $D$ として

$$
\begin{align*}
D = (a-1)^2 - 4Aa = a^2 - 2(1+2A)a + 1
\end{align*}
$$

から, $D < 0 \iff (1+2A) - \sqrt{4A^2+4A} < a < (1+2A) + \sqrt{4A^2+4A}$

$$
\begin{align*}
\iff \frac{1}{2n+1} < a < 2n+1
\end{align*}
$$

の時, 任意の $x$ に対し $f(x) > 0$ となる. その他の時, $f(x)=0$ は

$$
\begin{align*}
x = \frac{1}{2}\left[ (a-1) \pm \sqrt{(a-1)^2 - 4Aa} \right] = \frac{1}{2}\left[ (a-1) \pm \sqrt{a^2 - 2(1+2A)a + 1} \right]
\end{align*}
$$

を解に持つ. これらを $\alpha, \beta$ ($\alpha \le \beta$) とする.

\bigskip

$1^\circ \ 0 < a \le \frac{1}{2n+1}$ の時

$$
\begin{align*}
\alpha = \frac{1}{2}\left[ (a-1) - \sqrt{a^2-2(1+2A)a+1} \right] > -1
\end{align*}
$$

$$
\begin{align*}
\iff (a+1)^2 > a^2 - 2(1+2A)a + 1 \iff 2(1+A)a > 0 \quad \cdots \text{③}
\end{align*}
$$

③は成立するので, $\alpha > -1$. 同様に $\beta < 0$ だから, $-1 < \alpha < \beta < 0$.
したがって任意の $m \in \mathbb{Z}$ に対し $f(m) > 0$.

\bigskip

$2^\circ \ 2n+1 \le a$

$$
\begin{align*}
f(n) = (A-n)a + n^2 + n = \frac{-(n^2+n)}{2n+1} a + n^2 + n \le 0
\end{align*}
$$

から不適.

\bigskip

以上まとめて $0 < a < 2n+1$.