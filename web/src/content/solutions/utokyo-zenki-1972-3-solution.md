---
university: "utokyo"
category: "zenki"
year: "1972"
question: "3"
type: "solution"
title: "UTOKYO 1972 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $C, C', C_n$ と $l$ の接点を $H, H', H_n$ とする。($C' = C_0, H' = H_0$ とする)

右図から, ピタゴラスの定理より, $|HH_n|$ を2通りで表して

$$
\begin{align*}
|HH_n| = \sqrt{(R+r_n)^2 - (R-r_n)^2}
\end{align*}
$$

$$
\begin{align*}
|HH_n| = |HH_{n+1}| + |H_{n+1}H_n| = \sqrt{(R+r_{n+1})^2 - (R-r_{n+1})^2} + \sqrt{(r_n+r_{n+1})^2 - (r_n-r_{n+1})^2}
\end{align*}
$$

だから,

$$
\begin{align*}
2\sqrt{Rr_n} = 2\sqrt{Rr_{n+1}} + 2\sqrt{r_n r_{n+1}} \quad \cdots \text{①}
\end{align*}
$$

$C_n = \frac{1}{\sqrt{r_n}}$ とする。①の両辺 $\sqrt{r_n r_{n+1}} \; (\neq 0)$ でわって,

$$
\begin{align*}
C_{n+1} = C_n + \sqrt{1/R}
\end{align*}
$$

$C_0 = \sqrt{1/R}$ とあわせて, くり返し用いて,

$$
\begin{align*}
C_n = n\sqrt{1/R} + \sqrt{1/R}
\end{align*}
$$

だから,

$$
\begin{align*}
r_n = \frac{1}{C_n^2} = \frac{1}{(n\sqrt{1/R} + \sqrt{1/R})^2}
\end{align*}
$$

より,

$$
\begin{align*}
n^2 r_n = \frac{1}{(\sqrt{1/R} + \frac{1}{n}\sqrt{1/R})^2} \to R \quad (n \to +\infty)
\end{align*}
$$

\begin{tikzpicture}[scale=1.5]
  \draw[thick] (-0.5,0) -- (4,0) node[right] {$l$};

  \draw (0,1) circle (1);
  \fill (0,0) circle (1pt) node[below] {$H$};
  \node at (0,1) {$R$};

  \draw (1.6,0.3) circle (0.3);
  \fill (1.6,0) circle (1pt) node[below] {$H_{n+1}$};

  \draw (2.8,0.5) circle (0.5);
  \fill (2.8,0) circle (1pt) node[below] {$H_n$};
  \node at (2.8,0.5) {$r_n$};
\end{tikzpicture}