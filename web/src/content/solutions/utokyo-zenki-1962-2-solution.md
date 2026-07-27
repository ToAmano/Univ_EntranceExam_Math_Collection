---
university: "utokyo"
category: "zenki"
year: "1962"
question: "2"
type: "solution"
title: "UTOKYO 1962 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

［解］$\mathrm{PQ} \mathbin{/\!/} \mathrm{BC}$ より，$\angle \mathrm{BQP} = \frac{\pi}{4}$ だから，

$$
\begin{align*}
\cos \angle \mathrm{AQR} = \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} = \frac{1}{2} \quad \therefore \angle \mathrm{AQR} = \frac{\pi}{3} \quad \left(0 < \angle \mathrm{AQR} < \pi\right)
\end{align*}
$$

従って，$\angle \mathrm{BRQ} = \angle \mathrm{CRS}$ より $\triangle \mathrm{CSR} \mathbin{\sim} \triangle \mathrm{BQR}$ なので，

$$
\begin{align*}
\angle \mathrm{ASR} = \angle \mathrm{AQR} = \frac{\pi}{3}
\end{align*}
$$

となり，最後の条件から $\angle \mathrm{CST} = \frac{5}{6}\pi$ となる。図は下図。

\begin{tikzpicture}[scale=2, >=stealth]
  \coordinate (A) at (0,0);
  \coordinate (B) at (2,0);
  \coordinate (C) at (0,2);

  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \node[below left] at (A) {A};
  \node[below right] at (B) {B};
  \node[above left] at (C) {C};

  \draw (0,0.15) -- (0.15,0.15) -- (0.15,0);

  \coordinate (Q) at (1.1, 0);
  \coordinate (S) at (0, 1.1);
  \coordinate (R) at (0.68, 0.72);
  \coordinate (H) at (0, 0.72);
  \coordinate (Hp) at (0.68, 0);
  \coordinate (T) at (-0.3, 1.4);
  \coordinate (D) at (1.5, -0.3);

  \draw (R) -- (Q);
  \draw (R) -- (S);
  \draw[dashed] (R) -- (H);
  \draw[dashed] (R) -- (Hp);
  \draw (S) -- (T);
  \draw (B) -- (D);
  \draw (Q) -- (D);

  \node[below] at (Q) {Q};
  \node[left] at (S) {S};
  \node[above right] at (R) {R};
  \node[left] at (H) {H};
  \node[below] at (Hp) {H'};
  \node[above left] at (T) {T};
  \node[below right] at (D) {D};

  \node at (0.78, 0.25) {\small $60^\circ$};
  \node at (0.22, 0.85) {\small $60^\circ$};

  \node[above right] at (0.89, 0.36) {$\alpha$};
  \node[above left] at (0.34, 0.91) {$\beta$};
  \node[below] at (1.5, 0) {$x$};
  \node[right] at (2.0, 1.0) {$\sqrt{2}$};
  \node[below] at (0.6, -0.1) {$2-\sqrt{2}x$};
\end{tikzpicture}

$\mathrm{R}$ から $\mathrm{AC}, \mathrm{AB}$ に下ろした垂足を $\mathrm{H}, \mathrm{H'}$ とおき，$\overline{\mathrm{RQ}} = \alpha, \overline{\mathrm{SR}} = \beta$ とおく。$\overline{\mathrm{AB}} = 2$ だから，

$$
\begin{align*}
\begin{cases}
\mathrm{H'Q} = \frac{1}{2}\alpha, & \mathrm{RH'} = \mathrm{H'B} = \frac{\sqrt{3}}{2}\alpha \\[1ex]
\mathrm{HR} = \frac{\sqrt{3}}{2}\beta, & \mathrm{HS} = \frac{1}{2}\beta
\end{cases}
\end{align*}
$$

$$
\begin{align*}
\therefore \begin{cases}
2 - \sqrt{2}x = \frac{1}{2}\alpha + \frac{\sqrt{3}}{2}\beta & \dots \text{①} \\[1ex]
2 - \sqrt{2}y = \frac{\sqrt{3}}{2}\alpha + \frac{1}{2}\beta & \dots \text{②} \\[1ex]
\frac{\sqrt{3}}{2}\alpha + \frac{\sqrt{3}}{2}\beta = 2 & \dots \text{③}
\end{cases}
\end{align*}
$$

③より，$\alpha + \beta = \frac{4}{\sqrt{3}} = \frac{4}{3}\sqrt{3}$ だから，①+②に代入して求める関係式は

$$
\begin{align*}
4 - \sqrt{2}x - \sqrt{2}y &= \left(\frac{\sqrt{3}}{2} + \frac{1}{2}\right)\cdot\frac{4}{3}\sqrt{3}\\\therefore x + y &= \frac{1}{\sqrt{2}}\left\{ 4 - \frac{2}{3}(3+\sqrt{3}) \right\}\\
x + y &= \sqrt{2}\left( 1 - \frac{\sqrt{3}}{3}\right)\quad(x, y > 0)
\end{align*}
$$

\bigskip

［＊以降］$\mathrm{A}$ を原点とし，$\mathrm{AB}$ を $x$ 軸とする座標を設定すると

$$
\begin{align*}
\mathrm{RQ}&: y = -\sqrt{3}(x - A) \quad(A = 2 - \sqrt{2}x) \\\mathrm{RS}&: y = -\frac{1}{\sqrt{3}}x + B \quad(B = 2 - \sqrt{2}y)
\end{align*}
$$

この交点 $\left( \frac{3A - \sqrt{3}B}{2}, \frac{-\sqrt{3}A + 3B}{2} \right)$ が $x + y = 2$ 上にあることが必要十分．

$$
\begin{align*}
\frac{3A - \sqrt{3}B}{2} + \frac{-\sqrt{3}A + 3B}{2} = 2
\end{align*}
$$

$$
\begin{align*}
(3 - \sqrt{3})(A + B) = 4
\end{align*}
$$

$$
\begin{align*}
\therefore x + y = \sqrt{2} \left( 1 - \frac{\sqrt{3}}{3} \right)
\end{align*}
$$