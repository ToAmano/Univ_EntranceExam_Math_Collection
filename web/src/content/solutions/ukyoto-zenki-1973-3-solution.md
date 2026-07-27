---
university: "ukyoto"
category: "zenki"
year: "1973"
question: "3"
type: "solution"
title: "UKYOTO 1973 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解1**] $O$ を原点とし、$B$ が $x$ 軸上、$A$ が第一象限になるよう $xy$ 平面をおく。
この時 $|\vec{a}| = a$, $|\vec{b}| = b$ とすると、$\angle AOB = \frac{\pi}{3}$ より、

$$
\begin{align*}
\vec{b} = b \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \vec{a} = \frac{a}{2} \begin{pmatrix} 1 \\ \sqrt{3} \end{pmatrix}
\end{align*}
$$

とおける。$AB$ の中点を $M$ とする。

$$
\begin{align*}
\vec{AB} = \begin{pmatrix} b - \frac{1}{2}a \\ -\frac{\sqrt{3}}{2}a \end{pmatrix}
\end{align*}
$$

だから、$|MC| = \frac{\sqrt{3}}{2}|AB|$, $MC \perp AB$, $C$ が $O$ と反対側であることをあわせて、

$$
\begin{align*}
\vec{MC} = \frac{\sqrt{3}}{2} \begin{pmatrix} \frac{\sqrt{3}}{2}a \\ b - \frac{1}{2}a \end{pmatrix}
\end{align*}
$$

となり、

$$
\begin{align*}
\vec{c}&= \vec{OM} + \vec{MC}\\&= a \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \frac{1}{2}b \begin{pmatrix} 1 \\ \sqrt{3} \end{pmatrix}\quad\dots\text{①}
\end{align*}
$$

一方、

$$
\begin{align*}
\frac{b}{a}\vec{a} + \frac{a}{b}\vec{b} = b \cdot \frac{1}{2} \begin{pmatrix} 1 \\ \sqrt{3} \end{pmatrix} + a \begin{pmatrix} 1 \\ 0 \end{pmatrix} \quad \dots \text{②}
\end{align*}
$$

①, ②から

$$
\begin{align*}
\vec{c} = \frac{b}{a}\vec{a} + \frac{a}{b}\vec{b}
\end{align*}
$$

となる。

\begin{tikzpicture}[scale=1.5]
    \draw[->] (-0.3,0) -- (3.2,0) node[right]{$x$};
    \draw[->] (0,-0.3) -- (0,2.5) node[above]{$y$};
    
    \coordinate (O) at (0,0);
    \coordinate (B) at (2,0);
    \coordinate (A) at (1, 1.732);
    \coordinate (M) at (1.5, 0.866);
    \coordinate (C) at (2.5, 1.732);
    
    \draw[thick] (O) node[below left]{$O$} -- (A) node[above left]{$A$} -- (B) node[below]{$B$} -- cycle;
    \draw[thick] (A) -- (C) node[above right]{$C$} -- (B);
    \draw[dashed] (M) node[above left]{$M$} -- (C);
    
    \fill (O) circle (1.5pt);
    \fill (A) circle (1.5pt);
    \fill (B) circle (1.5pt);
    \fill (C) circle (1.5pt);
    \fill (M) circle (1.5pt);
    
    \node at (0.4, 0.25) {$\pi/3$};
\end{tikzpicture}

[**解2**] $\vec{a}, \vec{b}$ に平行な単位ベクトルを $\vec{x}, \vec{y}$ とすると、これらは1次独立で、又 $\vec{x} \cdot \vec{y} = \frac{1}{2}$ となる。さらに

$$
\begin{align*}
\vec{c} = \alpha \vec{x} + \beta \vec{y}
\end{align*}
$$

とおける。

$$
\begin{align*}
\vec{AB}&= |\vec{b}|\vec{y} - |\vec{a}|\vec{x}\\\vec{AC}&= (\alpha - |\vec{a}|)\vec{x} + \beta\vec{y}\\\vec{BC}&= \alpha\vec{x} + (\beta - |\vec{b}|)\vec{y}
\end{align*}
$$

これらの大きさ2乗が全て等しいので、$k \ge 0$ として

$$
\begin{align*}
\begin{cases}
|\vec{b}|^2 + |\vec{a}|^2 - |\vec{a}||\vec{b}| = k \\
(\alpha - |\vec{a}|)^2 + \beta^2 + \beta(\alpha - |\vec{a}|) = k \\
\alpha^2 + (\beta - |\vec{b}|)^2 + \alpha(\beta - |\vec{b}|) = k
\end{cases}
\quad \dots (*)
\end{align*}
$$

$(\alpha, \beta) = (|\vec{b}|, |\vec{a}|)$ とすると、(*)は成立する。又、$\vec{x}, \vec{y}$ は1次独立であることから、コレ以外の解には他ならず、

$$
\begin{align*}
\vec{c}&= |\vec{b}|\vec{x} + |\vec{a}|\vec{y}\\&= |\vec{b}|\frac{\vec{a}}{|\vec{a}|} + |\vec{a}|\frac{\vec{b}}{|\vec{b}|}
\end{align*}
$$

である。