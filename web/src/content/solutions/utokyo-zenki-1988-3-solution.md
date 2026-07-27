---
university: "utokyo"
category: "zenki"
year: "1988"
question: "3"
type: "solution"
title: "UTOKYO 1988 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $C$ を $\begin{pmatrix} a \\ b \end{pmatrix}$ だけ平行移動した図形は,

$$
\begin{align*}
y-b = (x-a)^3 - (x-a) \quad (-1+a \le x \le 1+a) \quad \dots \text{①}
\end{align*}
$$

である. これと $y=x^3-x$ との共有点がただ1つある時, まず $y$ を消去して,

$$
\begin{align*}
x^3 - x - b &= (x-a)^3 - (x-a) \\
-x - b &= -3a x^2 + (3a^2-1) x - a^3 + a \\
b &= 3a x^2 - 3a^2 x + a^3 - a \equiv f(x)
\end{align*}
$$

これが, $-1 \le x \le 1$ かつ $-1+a \le x \le 1+a$ にただ1つ解を持つ条件を調べる.
右図及び, $f(x)$ の軸が $x = \frac{a}{2}$ であることから, 条件は

$$
\begin{align*}
f\left(\frac{a}{2}\right) = b \iff b = \frac{1}{4}a^3 - a \quad \dots \text{②}
\end{align*}
$$

この時 $(a,b) \ne (0,0)$ だから $a \ne 0$ で, ①に代入して,

$$
\begin{align*}
y = (x-a)^3 - (x-a) + \frac{1}{4}a^3 - a \quad (-1+a \le x \le 1+a) \quad \dots \text{③}
\end{align*}
$$

で, $P(X, Y)$ とおくと ③が $P$ を通ることから,

$$
\begin{align*}
Y = (X-a)^3 - (X-a) + \frac{1}{4}a^3 - a \quad (-1+a \le X \le a+1) \quad \dots \text{④}
\end{align*}
$$

これをみたす $a(\ne 0)$ がただ1つ存在する条件を考える. ④の右辺を $g(a)$ とおく.

$$
\begin{align*}
g(a) &= -\frac{3}{4}a^3 + 3X a^2 - 3X^2 a + X^3 - X \\
g'(a) &= -\frac{9}{4}a^2 + 6X a - 3X^2 \\&= -\frac{3}{4}(3a-2X)(a-2X)
\end{align*}
$$

したがって, 右表とあわせて, ④が $a$ について3実解を持つには, $-1 < X < 1 \ (X \ne 0)$ が必要で, $X$ の正負で場合分けする.

### $1^\circ \ -1 < X < 0$

| $a$ | $X-1$ | $\dots$ | $2X$ | $\dots$ | $\frac{2}{3}X$ | $\dots$ | $X+1$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $g'$ |  | $-$ | $0$ | $+$ | $0$ | $-$ |  |
| $g$ |  | $\searrow$ | 極小 | $\nearrow$ | 極大 | $\searrow$ |  |

したがって, ④が $a \ne 0$ に3実解を持つ条件は, $\alpha, \beta$ のうち, 小さくない方 $\max(\alpha,\beta)$, 大きくない方 $\min(\alpha,\beta)$ として

$$
\begin{align*}
\min\left(g(2X), g(X+1)\right) \le Y \le \max\left(g(X-1), g\left(\frac{2}{3}X\right)\right) \land g(0) \ne Y \quad \dots \text{⑤}
\end{align*}
$$

ただし, $Y \ne g(2X), Y \ne g(X+1)$ である.

### $2^\circ \ 0 < X < 1$

| $a$ | $X-1$ | $\dots$ | $\frac{2}{3}X$ | $\dots$ | $2X$ | $\dots$ | $X+1$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $g'$ |  | $-$ | $0$ | $+$ | $0$ | $-$ |  |
| $g$ |  | $\searrow$ | 極小 | $\nearrow$ | 極大 | $\searrow$ |  |

したがって, ④が $a \ne 0$ に3実解を持つ条件は

$$
\begin{align*}
\min\left(g\left(\frac{2}{3}X\right), g(X+1)\right) \le Y \le \max\left(g(2X), g(X-1)\right) \land g(0) \ne Y \quad \dots \text{⑥}
\end{align*}
$$

ただし, $Y \ne g(2X), Y \ne g\left(\frac{2}{3}X\right)$ である.

$1^\circ$ および $2^\circ$:

$$
\begin{align*}
g(X+1) &= \frac{1}{4}(X+1)^3 - (X+1) + (-1)^3 - (-1) \\&= \frac{1}{4}(X+1)(X+3)(X-1) \quad\dots\text{⑦}\\
g(X-1) &= \frac{1}{4}(X-1)^3 - (X-1) \\&= \frac{1}{4}(X-1)(X+1)(X-3) \quad\dots\text{⑧}\\
g(2X) &= \frac{1}{4}\cdot 8 X^3 - 2X + (-X)^3 - (-X) \\&= X^3 - X \quad\dots\text{⑨}\\
g\left(\frac{2}{3}X\right)&= \frac{1}{4}\left(\frac{2}{3}X\right)^3 - \left(\frac{2}{3}X\right) + \left(\frac{1}{3}X\right)^3 - \left(\frac{1}{3}X\right)\\&= \frac{1}{9}X^3 - X \quad\dots\text{⑩}
\end{align*}
$$

又, $g(0) = X^3 - X$ から, もとめるのは下図斜線部 (境界は実線のみ含む).

\begin{tikzpicture}[scale=1.5, >=stealth]
  \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
  \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
  \node[below left] at (0,0) {$O$};

  \draw[domain=-1.2:1.2, samples=100, thick] plot (\x, {\x*\x*\x - \x}) node[right] {①};
  \draw[domain=-1.2:1.2, samples=100, dashed] plot (\x, {(1/9)*\x*\x*\x - \x}) node[right] {④};
  \draw[domain=-1.2:1.1, samples=100, dotted] plot (\x, {0.25*(\x+1)*(\x+3)*(\x-1)}) node[above] {③};
  \draw[domain=-1.1:1.2, samples=100, dash pattern=on 3pt off 2pt] plot (\x, {0.25*(\x-1)*(\x+1)*(\x-3)}) node[below] {②};
  
  \node at (-1,0) [below left] {$-1$};
  \node at (1,0) [below right] {$1$};
\end{tikzpicture}

### [解2] (前半部, ②をみちびく)

$\vec{A} = \begin{pmatrix} a \\ b \end{pmatrix}$ だけ平行移動とする. $OA$ の中点 $M\left(\frac{1}{2}a, \frac{1}{2}b\right)$ とする. $C$ の任意の点 $(x,y)$ の, $M$ に関する対称点を $(x',y')$ とすると,

$$
\begin{align*}
x = a - x', \quad y = b - y'
\end{align*}
$$

だから, $y = x^3 - x$ に代入して

$$
\begin{align*}
y - b = (x'-a)^3 - (x'-a)
\end{align*}
$$

つまり, $(x',y')$ は $C'$ 上の点である. したがって, $C, C'$ は $M$ を中心として点対称である.
よって, $C, C'$ の共有点も $M$ を中心として点対称だから,

$$
\begin{align*}
\text{「共有点がただ1つ} \iff \text{共有点が} M\text{」}
\end{align*}
$$

となり,

$$
\begin{align*}
\frac{b}{2} = f\left(\frac{a}{2}\right) \quad \therefore b = \frac{1}{4}a^3 - a
\end{align*}
$$

を得る.