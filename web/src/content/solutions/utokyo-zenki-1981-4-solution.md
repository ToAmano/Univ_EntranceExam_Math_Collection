---
university: "utokyo"
category: "zenki"
year: "1981"
question: "4"
type: "solution"
title: "UTOKYO 1981 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $0 \le \alpha < \pi/2 \quad \dots \text{①}$

$Z > 0 \quad \dots \text{②}$ から, $P$ は $A, B, C$ であることに適する。

$$
\begin{align*}
\vec{AP} = \begin{pmatrix} x-1 \\ y-1 \\ Z \end{pmatrix}, \quad 
\vec{BP} = \begin{pmatrix} x-1 \\ y+1 \\ Z \end{pmatrix}, \quad 
\vec{CP} = \begin{pmatrix} x \\ y \\ Z \end{pmatrix}
\end{align*}
$$

(ロ)～(ニ)より, $\vec{n} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$ として,

$$
\begin{align*}
\begin{cases}
\vec{n} \cdot \vec{AP} = |\vec{n}| |\vec{AP}| \cos\pi/4 \\
\vec{n} \cdot \vec{BP} = |\vec{n}| |\vec{BP}| \cos\pi/4 \\
\vec{n} \cdot \vec{CP} = |\vec{n}| |\vec{CP}| \cos\alpha
\end{cases}
\iff
\begin{cases}
Z = \sqrt{(x-1)^2 + (y-1)^2 + Z^2} \cdot \frac{1}{\sqrt{2}} \\
Z = \sqrt{(x-1)^2 + (y+1)^2 + Z^2} \cdot \frac{1}{\sqrt{2}} \\
Z = \sqrt{x^2 + y^2 + Z^2} \cos\alpha
\end{cases}
\end{align*}
$$

①②から, 両辺 2 乗しても同値。

$$
\begin{align*}
\begin{cases}
Z^2 = (x-1)^2 + (y+1)^2 = (x-1)^2 + (y-1)^2 & \dots \text{②} \\
Z^2 \cdot \tan^2\alpha = x^2 + y^2 & \dots \text{③}
\end{cases}
\end{align*}
$$

②の右側の不等式から, $(y+1)^2 = (y-1)^2 \iff y=0 \quad \dots \text{④}$ だから, ②③に代入して

$$
\begin{align*}
\begin{cases}
Z^2 = (x-1)^2 + 1 = x^2 - 2x + 2 & \dots \text{⑤} \\
Z^2 \cdot \tan^2\alpha = x^2 & \dots \text{⑥}
\end{cases}
\end{align*}
$$

したがって, ①～② $\land$ ④ $\land$ ⑤ $\land$ ⑥ をみたす $P$ の数をもとめれば良い。⑤から,

$1^\circ$ $\alpha \neq 0$ の時

⑥から $Z^2 = \left( \frac{x}{\tan\alpha} \right)^2$ だから, ⑤に代入して, $t = \tan\alpha$ とおくと,

$$
\begin{align*}
\begin{cases}
x \neq 0 \\
(t^2-1) x^2 - 2t^2 x + 2t^2 = 0 \quad \dots \text{⑦}
\end{cases}
\end{align*}
$$

⑦をみたす $x$ に対し, ⑥から $Z$ が $Z = \left|\frac{x}{\tan\alpha}\right|$ と一意に定まり, $y=0$ だから, ⑦をみたす $x$ の数が $P$ の数に等しい。$t^2 - 1 \neq 0$ の時, ⑦の判別式 $D$ として

$$
\begin{align*}
D/4 = t^4 - (t^2-1) \cdot 2t^2 = t^2 (2 - t^2)
\end{align*}
$$

だから,

$$
\begin{align*}
\begin{cases}
D/4 > 0 \iff 2 > t^2 \text{ の時 } 2 \text{ 個} \\
D/4 = 0 \iff 2 = t^2 \text{ の時 } 1 \text{ 個} & \dots A_1 \\
D/4 < 0 \iff 2 < t^2 \text{ の時 } 0 \text{ 個}
\end{cases}
\end{align*}
$$

である ($\alpha \neq 0$ から, $x=0$ は解にならない)。

一方, $t^2 - 1 = 0 \iff \alpha = \pi/4$ ($\because$ ①) の時, ⑦ $\to x = 1$, ⑥から $Z=1$ となって $1$ 個。

$2^\circ$ $\alpha = 0$ の時

⑥から $x=0$ だから ⑤より $Z = \sqrt{2}$ となる。

以上まとめて, ⑦の解が ($D \ge 0$ の時) $x = \frac{t^2 \pm \sqrt{t^2(2-t^2)}}{t^2 - 1}$ であるから

$$
\begin{align*}
Z = \left| \frac{x}{t} \right| = \left| \frac{t \pm \sqrt{2-t^2}}{t^2 - 1} \right|
\end{align*}
$$

であることをあわせて,

$$
\begin{align*}
\begin{cases}
\alpha = 0 \text{ の時}, Z = \sqrt{2} \text{ の } 1 \text{ つ} \\
0 < \tan\alpha < \sqrt{2} \land \alpha \neq \pi/4 \text{ の時}, Z = \left| \frac{t \pm \sqrt{2-t^2}}{t^2 - 1} \right| \text{ の } 2 \text{ つ} \\
\tan\alpha = \sqrt{2} \text{ の時}, Z = \sqrt{2} \text{ の } 1 \text{ つ} \\
\sqrt{2} < \tan\alpha \text{ の時}, 0 \text{ 個} \\
\alpha = \pi/4 \text{ の時}, Z = 1 \text{ の } 1 \text{ つ}
\end{cases}
\end{align*}
$$

\begin{tikzpicture}[scale=1.5, >=stealth]
  \draw[->] (0,0,0) -- (2.5,0,0) node[right] {$y$};
  \draw[->] (0,0,0) -- (0,2.5,0) node[above] {$z$};
  \draw[->] (0,0,0) -- (0,0,2.5) node[below left] {$x$};

  \node[below left] at (0,0,0) {$C$};

  \coordinate (C) at (0,0,0);
  \coordinate (A) at (1,0,1);
  \coordinate (B) at (-1,0,1);
  \coordinate (P) at (0,1.8,0.8);

  \draw[dashed] (C) -- (P) node[midway, right] {$\alpha$};
  \draw[dashed] (A) -- (P);
  \draw[dashed] (B) -- (P);
  \draw (0,0,0) -- (1,0,1) node[right] {$A$};
  \draw (0,0,0) -- (-1,0,1) node[left] {$B$};

  \fill (P) circle (1.5pt) node[above] {$P$};
  \fill (A) circle (1.5pt);
  \fill (B) circle (1.5pt);
  \fill (C) circle (1.5pt);
\end{tikzpicture}