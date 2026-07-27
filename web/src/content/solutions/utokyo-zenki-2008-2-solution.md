---
university: "utokyo"
category: "zenki"
year: "2008"
question: "2"
type: "solution"
title: "UTOKYO 2008 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 白のカードを白、黒のカードを黒と表す。

\bigskip

(1) 白のカードの枚数は、帰納的に奇回目の操作後には奇数枚である。$\cdots$ ① \\
そこで、$2k$ 回目の操作の後について、以下のようになる確率をおく。

$$
\begin{align*}
\begin{cases}
A_k \cdots \text{はじめて白4枚} \\
b_k \cdots \text{白2枚}
\end{cases}
\end{align*}
$$

すると、$2A_k$ をもとめれば良い。$\cdots$ ② 右図から

$$
\begin{align*}
\begin{cases}
A_{k+1} = \frac{1}{8} b_k \\
b_{k+1} = \frac{3}{4} b_k
\end{cases}
\end{align*}
$$

であり、初期条件から $b_0 = 1$ として、$b_k = \left(\frac{3}{4}\right)^k$ だから、$A_k = \frac{1}{8}\left(\frac{3}{4}\right)^{k-1}$ である。①, ②から

$$
\begin{align*}
p_n = \begin{cases}
0 & (n \text{ odd}) \\
\frac{1}{4}\left(\frac{3}{4}\right)^{\frac{n}{2}-1} & (n \text{ even})
\end{cases}
\hfill \text{\#}
\end{align*}
$$

\begin{tikzpicture}[scale=1.2, >=stealth]
  \node[draw, rectangle, inner sep=5pt] (b2_1) at (0, 0) {$2k$: 白2 ($b_k$)};
  
  \node[draw, rectangle, inner sep=5pt] (b4_2) at (4, 1) {$2k+2$: 白4 ($A_{k+1}$)};
  \node[draw, rectangle, inner sep=5pt] (b2_2) at (4, 0) {$2k+2$: 白2 ($b_{k+1}$)};
  \node[draw, rectangle, inner sep=5pt] (b0_2) at (4, -1) {$2k+2$: 白0};

  \draw[->] (b2_1) -- node[above, sloped] {$\frac{1}{8}$} (b4_2);
  \draw[->] (b2_1) -- node[above] {$\frac{3}{4}$} (b2_2);
  \draw[->] (b2_1) -- node[below, sloped] {$\frac{1}{8}$} (b0_2);
\end{tikzpicture}

\bigskip

(2) (1)と同じく、求める確率を $p_n$ とすると、$n \in \text{even}$ の時 $p_n = 0 \quad \cdots$ ③である。$2k+1$ 回目操作後について、以下のようにおく。

$$
\begin{align*}
A_k \cdots \text{白2枚}
\end{align*}
$$

対称性から、白4枚の確率も $A_k$ である。
右図から、

$$
\begin{align*}
\begin{cases}
A_{k+1} = \frac{11}{18} A_k + \frac{1}{3} A_k = \frac{17}{18} A_k \\
p_{k+1} = 2 \cdot \frac{1}{18} A_k = \frac{1}{9} A_k
\end{cases}
\end{align*}
$$

$A_0 = \frac{1}{2}$ だから、くり返し用いて $A_k = \frac{1}{2}\left(\frac{17}{18}\right)^k$ だから、$k \ge 1$ に対して $P_k = \frac{1}{18}\left(\frac{17}{18}\right)^{k-1}$。$k=0$ の時 $p_0 = 0$。③とあわせて、

$$
\begin{align*}
p_n = \begin{cases}
0 & (n \in \text{even}, n=1) \\
\frac{1}{18}\left(\frac{17}{18}\right)^{\frac{n-3}{2}} & (n \in \text{odd} \ge 3)
\end{cases}
\hfill \text{\#}
\end{align*}
$$

\begin{tikzpicture}[scale=1.2, >=stealth]
  \node[draw, rectangle, inner sep=4pt] (b2_1) at (0, 0.6) {$2k+1$: 白2 ($A_k$)};
  \node[draw, rectangle, inner sep=4pt] (b4_1) at (0, -0.6) {$2k+1$: 白4 ($A_k$)};

  \node[draw, rectangle, inner sep=4pt] (b0_2) at (4.5, 1.8) {$2k+3$: 白0 ($\frac{11}{18}$)};
  \node[draw, rectangle, inner sep=4pt] (b2_2) at (4.5, 0.6) {$2k+3$: 白2 ($\frac{1}{3}$)};
  \node[draw, rectangle, inner sep=4pt] (b4_2) at (4.5, -0.6) {$2k+3$: 白4 ($\frac{1}{9}$)};
  \node[draw, rectangle, inner sep=4pt] (b6_2) at (4.5, -1.8) {$2k+3$: 白6 ($\frac{11}{18}$)};

  \draw[->] (b2_1) -- node[above, sloped, pos=0.6] {$\frac{1}{18}$} (b0_2);
  \draw[->] (b2_1) -- (b2_2);
  \draw[->] (b2_1) -- node[above, sloped, pos=0.4] {$\frac{1}{3}$} (b4_2);

  \draw[->] (b4_1) -- node[below, sloped, pos=0.4] {$\frac{1}{3}$} (b2_2);
  \draw[->] (b4_1) -- (b4_2);
  \draw[->] (b4_1) -- node[below, sloped, pos=0.6] {$\frac{1}{18}$} (b6_2);
\end{tikzpicture}

\bigskip