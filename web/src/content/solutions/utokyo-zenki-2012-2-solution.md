---
university: "utokyo"
category: "zenki"
year: "2012"
question: "2"
type: "solution"
title: "UTOKYO 2012 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{tabular}{|p{0.9\textwidth}|}
\hline
場合の数のこの手のヤツでは、

1.  対称性

2.  $\bmod$ で場合分け

ができないかまずチェックせよ。 \\
\hline
\end{tabular}

\bigskip

## 【解】

 $k \in \mathbb{N}$ とする。球は $2k$ 秒後にのみ $P, Q$ にある。右のように $R$ を定める。対称性から、$2k$ 秒後に球が $P, Q, R$ にある確率は、$b_k, b_k, b_k$ とおける。
又、題意から、以下の漸化式をうる。

$$
\begin{align*}
b_{k+1} = \frac{2}{3} b_k + \frac{1}{6} b_k + \frac{1}{6} a_k \quad \cdots \textcircled{1}
\end{align*}
$$

\begin{tikzpicture}[scale=1.2, >=stealth]
  \draw[thick] (0, 1.5) -- (-1.3, -0.7) -- (1.3, -0.7) -- cycle;
  \draw (0, 1.5) -- (0, -0.7);
  \draw (-1.3, -0.7) -- (0.65, 0.4);
  \draw (1.3, -0.7) -- (-0.65, 0.4);
  \node at (0, 0.7) {$P$};
  \node at (0.4, -0.2) {$Q$};
  \node at (-0.4, -0.2) {$R$};
\end{tikzpicture}
\quad\quad
\begin{tikzpicture}[scale=1.2, >=stealth]
  \node (P) at (0, 1) {$P$};
  \node (Q) at (2, 0) {$Q$};
  \node (R) at (0, -1) {$R$};
  \draw[->] (P) -- node[above right] {$1/6$} (Q);
  \draw[->] (Q) to[out=30,in=-30,loop] node[right] {$2/3$} (Q);
  \draw[->] (R) -- node[below right] {$1/6$} (Q);
\end{tikzpicture}

又、$a_k + 2b_k = 1$ から ① で $a_k$ をけして

$$
\begin{align*}
b_{k+1} = \frac{1}{2} b_k + \frac{1}{6}
\end{align*}
$$

$$
\begin{align*}
b_{k+1} - \frac{1}{3} = \frac{1}{2} \left( b_k - \frac{1}{3} \right)
\end{align*}
$$

$b_0 = 0$ だから、これをくり返し用いて、

$$
\begin{align*}
b_k = \left(\frac{1}{2}\right)^k \left(-\frac{1}{3}\right) + \frac{1}{3}
\end{align*}
$$

だから、もとめる確率は

$$
\begin{align*}
\begin{cases}
0 & (n \in \text{odd}) \\
\frac{1}{3} \left( 1 - \left(\frac{1}{2}\right)^{\frac{n}{2}} \right) & (n \in \text{even})
\end{cases}
\end{align*}
$$

\bigskip