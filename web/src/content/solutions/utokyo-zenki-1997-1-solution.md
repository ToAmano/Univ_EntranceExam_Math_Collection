---
university: "utokyo"
category: "zenki"
year: "1997"
question: "1"
type: "solution"
title: "UTOKYO 1997 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

(1) $\triangle OAB$ の中点を $M$ とする. $MC = \frac{\sqrt{3}}{2} AB$ 及び $MC \perp AB$ だから, $\vec{AB} = \begin{pmatrix} -a \\ b \end{pmatrix}$ より

$$
\begin{align*}
\vec{MC} = \pm \frac{\sqrt{3}}{2} \begin{pmatrix} b \\ a \end{pmatrix}
\end{align*}
$$

となり,

$$
\begin{align*}
\vec{OC} = \vec{OM} + \vec{MC} = \frac{1}{2} \begin{pmatrix} a \\ b \end{pmatrix} \pm \frac{\sqrt{3}}{2} \begin{pmatrix} b \\ a \end{pmatrix} = \frac{1}{2} \begin{pmatrix} a \pm \sqrt{3}b \\ b \pm \sqrt{3}a \end{pmatrix} \quad (\text{複号同順})
\end{align*}
$$

$C$ は第1象限の点だから, 複号正を採用して, $C\left(\frac{a + \sqrt{3}b}{2}, \frac{b + \sqrt{3}a}{2}\right)$ である. $\triangle ABC$ が $D$ に含まれるには, $A, B, C$ が $D$ に含まれていれば良い. $a, b > 0$ とあわせて,

$$
\begin{align*}
\begin{cases}
0 < a \le 1, \quad 0 < b \le 1 \\
0 \le a + \sqrt{3}b \le 2, \quad 0 \le b + \sqrt{3}a \le 2
\end{cases} \quad \cdots *
\end{align*}
$$

これを図示して, 右図斜線部 (境界含む, が軸除く).

\begin{tikzpicture}[scale=2.0, >=stealth]
\begin{scope}[xshift=-2.5cm]
\draw[->] (-0.2,0) -- (1.5,0) node[right] {$x$};
\draw[->] (0,-0.2) -- (1.5,0) node[above] {$y$};
\node[below left] at (0,0) {$O$};
\coordinate (A) at (1,0);
\coordinate (B) at (0,0.8);
\coordinate (M) at (0.5,0.4);
\coordinate (C) at (1.1928, 1.266); 
\draw[thick] (0,0) -- (A) node[below] {$A$} -- (B) node[left] {$B$} -- cycle;
\draw[thick] (A) -- (C) node[above right] {$C$} -- (B);
\draw[dashed] (M) -- (C);
\node[below right] at (M) {$M$};
\node[below] at (0.5,0) {$a$};
\node[left] at (0,0.4) {$b$};
\end{scope}

\begin{scope}[xshift=1.5cm]
\draw[->] (-0.2,0) -- (1.6,0) node[right] {$a$};
\draw[->] (0,-0.2) -- (1.6,0) node[above] {$b$};
\node[below left] at (0,0) {$O$};

\draw[dashed] (1,0) node[below] {$1$} -- (1,1.2);
\draw[dashed] (0,1) node[left] {$1$} -- (1.2,1);

\draw[thick, domain=0.577:1.1547] plot (\x, {2 - 1.732*\x});
\draw[thick, domain=0.2:1.1547] plot (\x, {(2 - \x)/1.732});

\fill[pattern=north east lines, pattern color=gray!60] 
  (0,0) -- (0,1) -- (0.268,1) -- (0.732,0.732) -- (1,0.268) -- (1,0) -- cycle;

\draw[thick] (0,0) -- (0,1) -- (0.268,1) -- (0.732,0.732) -- (1,0.268) -- (1,0) -- cycle;

\filldraw (0.268,1) circle (1pt) node[above right] {$(2-\sqrt{3}, 1)$};
\filldraw (0.732,0.732) circle (1pt) node[above right] {$(\sqrt{3}-1, \sqrt{3}-1)$};
\filldraw (1,0.268) circle (1pt) node[right] {$(1, 2-\sqrt{3})$};

\node[left] at (0, 0.268) {$2-\sqrt{3}$};
\draw[dotted] (0,0.268) -- (1,0.268);
\node[below] at (0.268, 0) {$2-\sqrt{3}$};
\draw[dotted] (0.268,0) -- (0.268,1);

\node[right] at (1.1, 0.5) {$b = \frac{\sqrt{3}}{3}(2-a)$};
\node[right] at (0.6, 1.3) {$b = 2 - \sqrt{3}a$};
\end{scope}
\end{tikzpicture}

\bigskip

(2) $\triangle ABC$ の一辺は $\sqrt{a^2+b^2}$ だから

$$
\begin{align*}
S = \frac{\sqrt{3}}{4}(a^2+b^2) \quad \cdots \text{①}
\end{align*}
$$

となり, $a^2+b^2$ ($\equiv T$ とする)が最大の時 $S$ も最大. $T$ は $(a,b)$ と $(0,0)$ の距離の2乗に等しく, (1)の図から, 最大値の候補は $(1, 2-\sqrt{3})$, $(2-\sqrt{3}, 1)$, $(\sqrt{3}-1, \sqrt{3}-1)$ であり, 各々について $T$ を計算すると, 順に $8-4\sqrt{3}$, $8-4\sqrt{3}$, $8-4\sqrt{3}$ で全て等しいので, ①に代入して

$$
\begin{align*}
\max S = -3 + 2\sqrt{3}
\end{align*}
$$

この時, $(a,b) = (1, 2-\sqrt{3}), (2-\sqrt{3}, 1), (\sqrt{3}-1, \sqrt{3}-1)$ である.