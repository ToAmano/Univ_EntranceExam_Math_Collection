---
university: "ukyoto"
category: "zenki"
year: "1995"
question: "2"
type: "solution"
title: "UKYOTO 1995 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $a, b \in \mathbb{N}, a > b \cdots \text{\textcircled{1}}$\\
$p, d \in \text{prime} \quad p > 2 \cdots \text{\textcircled{2}}$

$A = a^p - b^p$ とおく。\\
$A = (a - b)(a^{p-1} + \cdots + b^{p-1})$\\
であり、$a - b \in \mathbb{N}$、$a^{p-1} + \cdots + b^{p-1} \ge 2$（$\because \text{\textcircled{1}}$）から、$A \in \text{prime}$ には $a - b = 1 \iff a = b + 1$ が必要。以下、$A-1 = (b+1)^p - b^p - 1$ が $2p$ でわり切れることを示す。$\cdots \bigstar$

$1^\circ \ A - 1 \equiv 0 \pmod 2$ の証明\\
$(b+1)^p, (b^p)$ の偶奇は一致するから、$A - 1 \equiv 0 \pmod 2$ （終）

$2^\circ \ A - 1 \equiv 0 \pmod p$ の証明\\
$r = 1, 2, 3, \cdots, p-1$ の時、

$$
\begin{align*}
_p\mathrm{C}_r = \frac{p}{r}{}_{p-1}\mathrm{C}_{r-1} \in \mathbb{Z}
\end{align*}
$$

において、$r$ は $p$ と互いに素だから、${}_p\mathrm{C}_r$ は $p$ の倍数である。\\
から

$$
\begin{align*}
A - 1 = {}_p\mathrm{C}_1 b^{p-1} + \cdots + {}_p\mathrm{C}_{p-1} b \equiv 0 \pmod p \quad \text{（終）}
\end{align*}
$$

$1^\circ, 2^\circ, p>2$ から $A-1$ は $2p$ でわりきれる（終）

[別解]\\
（フェルマーの小定理を証明した上で）以下

$$
\begin{align*}
a^p - b^p \equiv a - b \equiv 1 \pmod p
\end{align*}
$$

\framebox{
\begin{minipage}{0.9\textwidth}[フェルマーの小定理の証明の再掲]\\
\textcircled{1} ウィルソンを経由

$$
\begin{align*}
a \cdot 2a \cdot 3a \cdots(p-1)a &\equiv 1 \cdot 2 \cdots(p-1) \pmod p \\(p-1)! \cdot a^{p-1}&\equiv(p-1)! \pmod p \\
a^{p-1}&\equiv 1 \pmod p
\end{align*}
$$

\textcircled{2} 帰納法（$n^p \equiv n$）\\
(ア) $(m+1)^p \equiv m^p + 1 \pmod p$ を用いる方法と\\
(イ) $(x+y)^p \equiv x^p + y^p \pmod p$ から

$$
\begin{align*}
a^p = (1 + \cdots + 1)^p \equiv \cdots \equiv 1 + 1 + \cdots + 1 = a
\end{align*}
$$

とする方法
\end{minipage}
}