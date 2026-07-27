---
university: "utokyo"
category: "zenki"
year: "1989"
question: "2"
type: "solution"
title: "UTOKYO 1989 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 題意の放物線は $y = \frac{1}{4} x^2$ である.

この上の点 $(a, \frac{1}{4} a^2)$ を中心とし, $y = -1$ に接する, つまり半径 $r$ として $r = 1 + \frac{1}{4} a^2$ の円 $C$ は

$$
\begin{align*}
C : (x - a)^2 + \left(y - \frac{1}{4} a^2\right)^2 = \left(1 + \frac{1}{4} a^2\right)^2
\end{align*}
$$

である. $GF$ の中点 $I$ とすると, $PI \perp GF$ になっていることに注意して,

$$
\begin{align*}
T(a) = \frac{1}{2} \cdot IP \cdot GF = \frac{1}{2} \cdot IP \cdot (2 FI) \quad \dots \text{①}
\end{align*}
$$

\begin{tikzpicture}[scale=1.2, >=stealth]
  \draw[->] (-1.5,0) -- (4,0) node[right] {$y$};
  \draw[->] (0,-1.5) -- (0,4) node[above] {$z$};
  \node[below left] at (0,0) {$O$};

  \draw[dashed] (-1.5,-1) -- (4,-1);
  \node[left] at (0,-1) {$-1$};

  \draw[domain=-1.2:3.2, smooth, variable=\x] plot ({\x}, {0.25*\x*\x});

  \coordinate (P) at (2.4, 1.44);
  \coordinate (F) at (0, 1);
  \coordinate (H) at (2.4, -1);

  \fill (P) circle (1.5pt) node[above right] {$P$};
  \fill (F) circle (1.5pt) node[left] {$F$};
  \fill (H) circle (1.5pt) node[below] {$H$};

  \draw (P) circle (2.44);

  \draw (P) -- (H);
  \draw (P) -- (F);

  \draw (2.4,0.94) arc (-90:-168.6:0.5);
  \node at (2.1, 0.7) {$\theta$};

  \coordinate (I) at ($(F)!0.5!(P)$);
  \fill (I) circle (1.2pt) node[below right] {$I$};

  \node[above left] at (0.2, 3.8) {$G$};
  \node[above] at (1.5, 3.8) {$C$};
  \node[above right] at (3.2, 3.8) {$D$};

  \draw (F) -- (-0.2, 3.5);
\end{tikzpicture}

又, $PH$ と $PF$ のなす角 $\theta$ とすると, $\vec{PH} = \begin{pmatrix} 0 \\ -r \end{pmatrix}$, $\vec{PF} = \begin{pmatrix} -a \\ 1 - \frac{1}{4} a^2 \end{pmatrix}$ より,

$$
\begin{align*}
\cos\theta = \frac{\vec{PH} \cdot \vec{PF}}{|\vec{PH}| |\vec{PF}|} = \frac{-r \left(1 - \frac{1}{4} a^2\right)}{r^2} = \frac{-1 + \frac{1}{4} a^2}{r} = \frac{-4 + a^2}{4 + a^2} \quad \dots \text{②}
\end{align*}
$$

この時, $\angle IPF = \frac{\pi}{2} - \theta$ にも注意して ①より

$$
\begin{align*}
T(a) = r \sin\left(\frac{\pi}{2} - \theta\right) r \cos\left(\frac{\pi}{2} - \theta\right) = r^2 \sin\theta \cos\theta
\end{align*}
$$

$$
\begin{align*}
S(a) = \frac{1}{2} r^2 \theta
\end{align*}
$$

だから,

$$
\begin{align*}
\frac{T(a)}{S(a)} = \frac{r^2 \sin\theta \cos\theta}{\frac{1}{2} r^2 \theta} = \frac{2 \sin\theta \cos\theta}{\theta} \quad \dots \text{③}
\end{align*}
$$

ここで, ②より, $a \to \infty$ の時, $\cos\theta = \frac{-4/a^2 + 1}{4/a^2 + 1} \to 1$ より $\theta \to 0$ であるので, ③から,

$$
\begin{align*}
\frac{T(a)}{S(a)} = \frac{\sin 2\theta}{2\theta} \cdot 2 \to 2 \quad (a \to \infty)
\end{align*}
$$

である.