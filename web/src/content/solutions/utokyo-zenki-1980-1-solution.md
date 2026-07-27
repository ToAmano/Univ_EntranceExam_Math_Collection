---
university: "utokyo"
category: "zenki"
year: "1980"
question: "1"
type: "solution"
title: "UTOKYO 1980 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 $0 < x < \frac{1}{2} \quad \cdots \text{①}$

\begin{tikzpicture}[scale=2.0]
  \coordinate (A) at (60:3);
  \coordinate (B) at (0,0);
  \coordinate (C) at (3,0);

  \coordinate (P) at (0.8,0);
  \coordinate (Q) at ($(C)!0.267!(A)$);
  \coordinate (R) at ($(A)!0.267!(B)$);

  \coordinate (A') at (intersection of A--P and C--R);
  \coordinate (B') at (intersection of A--P and B--Q);
  \coordinate (C') at (intersection of B--Q and C--R);

  \draw[thick] (A) -- (B) -- (C) -- cycle;

  \draw (A) -- (P);
  \draw (B) -- (Q);
  \draw (C) -- (R);

  \node[above] at (A) {$A$};
  \node[below left] at (B) {$B$};
  \node[below right] at (C) {$C$};

  \node[below] at (P) {$P$};
  \node[right] at (Q) {$Q$};
  \node[left] at (R) {$R$};

  \node[above right] at (A') {$A'$};
  \node[left] at (B') {$B'$};
  \node[below] at (C') {$C'$};

  \node[below] at ($(B)!0.5!(P)$) {$x$};
  \node[right] at ($(C)!0.5!(Q)$) {$x$};
  \node[left] at ($(A)!0.5!(R)$) {$x$};

  \node[right] at ($(A)!0.5!(A')$) {$p$};
  \node[right] at ($(A')!0.5!(B')$) {$r$};
  \node[right] at ($(B')!0.5!(P)$) {$q$};

  \node[above] at ($(B)!0.5!(B')$) {$p$};
  \node[above] at ($(B')!0.5!(C')$) {$r$};
  \node[above] at ($(C')!0.5!(Q)$) {$q$};

  \node[left] at ($(C)!0.5!(C')$) {$p$};
  \node[left] at ($(C')!0.5!(A')$) {$r$};
  \node[left] at ($(A')!0.5!(R)$) {$q$};
\end{tikzpicture}

1.  対称性から $\overline{BB'} = \overline{CC'} = \overline{AA'} = p$,
  $\overline{PB'} = \overline{QC'} = \overline{RA'} = q$, $\overline{AB'} = \overline{BC'} = \overline{CA'} = r$
  とおける。メネラウスの定理から
  

$$
\begin{align*}
\frac{B'C'}{BB'} \cdot \frac{A'R}{C'A'} \cdot \frac{AB}{RA} = 1 \quad \cdots \text{②}
\end{align*}
$$

  

$$
\begin{align*}
\frac{QA}{CQ} \cdot \frac{B'P}{AB'} \cdot \frac{BC}{PB} = 1 \quad \cdots \text{③}
\end{align*}
$$

  まず ③ から
  

$$
\begin{align*}
\frac{1-x}{x} \cdot \frac{q}{p+r} \cdot \frac{1}{x} = 1
\end{align*}
$$

  ② から
  

$$
\begin{align*}
\frac{r}{p} \cdot \frac{q}{r} \cdot \frac{1}{x} = 1
\end{align*}
$$

  したがって
  

$$
\begin{align*}
\begin{cases}
  q = xp \\
  r = \frac{1-2x}{x} p
  \end{cases}
  \quad \cdots \text{④}
\end{align*}
$$

  一方, $\triangle BCR$ に余弦定理を用いて,
  

$$
\begin{align*}
p + q + r = \sqrt{x^2 - x + 1} \quad \cdots \text{⑤}
\end{align*}
$$

  ④ を ⑤ に代入して,
  

$$
\begin{align*}
\left( 1 + x + \frac{1-2x}{x} \right) p = \sqrt{x^2 - x + 1} \quad \therefore p = \frac{x}{\sqrt{x^2 - x + 1}}
\end{align*}
$$

  ④ から
  

$$
\begin{align*}
r = \frac{1-2x}{\sqrt{x^2 - x + 1}}, \quad q = \frac{x^2}{\sqrt{x^2 - x + 1}}
\end{align*}
$$

  以上から, $\overline{BB'} = p = \frac{x}{\sqrt{x^2 - x + 1}}$, $\overline{PB'} = q = \frac{x^2}{\sqrt{x^2 - x + 1}}$

2.  $\triangle A'B'C'$ は一辺の長さ $r$ の正三角形でその面積 $T$ は
  

$$
\begin{align*}
T = \frac{\sqrt{3}}{4} r^2 = \frac{\sqrt{3}}{4} \cdot \frac{4x^2 - 4x + 1}{x^2 - x + 1}
\end{align*}
$$

  と表せる。これが $\frac{1}{2} \cdot \frac{\sqrt{3}}{4}$ に等しいので
  

$$
\begin{align*}
\frac{1}{2} = \frac{4x^2 - 4x + 1}{x^2 - x + 1}
\end{align*}
$$

  

$$
\begin{align*}
8x^2 - 8x + 2 = x^2 - x + 1
\end{align*}
$$

  

$$
\begin{align*}
7x^2 - 7x + 1 = 0
\end{align*}
$$

  

$$
\begin{align*}
\therefore x = \frac{7 \pm \sqrt{21}}{14}
\end{align*}
$$

  $0 < x < \frac{1}{2}$ から複号負を採用して,
  

$$
\begin{align*}
x = \frac{7 - \sqrt{21}}{14}
\end{align*}
$$