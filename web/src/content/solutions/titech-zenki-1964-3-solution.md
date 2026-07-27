---
university: "titech"
category: "zenki"
year: "1964"
question: "3"
type: "solution"
title: "TITECH 1964 zenki Q3 (solution)"
---

## 【解】

内接円の中心 $O$ から $AB, BC, CA$ に下ろした垂足を順に $H_1, H_2, H_3$ とする. $AC, BC$ に接する円を, 内接円から順に $C_0, C_1, C_2, \dots$ とおく. $C_n$ の半径を $r_n$ とする. 題意から $r_0 = r$ で, 円 $C_n$ の中心を $O_n$ として右図から

$$
\begin{align*}
\sin \frac{C}{2} = \frac{r_n - r_{n+1}}{r_n + r_{n+1}}
\end{align*}
$$

$$
\begin{align*}
\therefore r_{n+1} = \frac{1 - \sin\frac{C}{2}}{1 + \sin\frac{C}{2}} r_n
\end{align*}
$$

だから, くり返し用いて,

$$
\begin{align*}
r_n = \left(\frac{1 - \sin\frac{C}{2}}{1 + \sin\frac{C}{2}}\right)^n r \qquad \dots \text{\textcircled{1}}
\end{align*}
$$

である. 同様にして, 他の2辺に接する円の半径 $s_n, t_n$ は,

$$
\begin{align*}
s_n = \left(\frac{1 - \sin\frac{A}{2}}{1 + \sin\frac{A}{2}}\right)^n r, \quad t_n = \left(\frac{1 - \sin\frac{B}{2}}{1 + \sin\frac{B}{2}}\right)^n r \qquad \dots \text{\textcircled{2}}
\end{align*}
$$

と書けるから, 全ての $C_n$ の面積和は ($C_0$ のぞく),

$$
\begin{align*}
\lim_{n \to \infty} \sum_{k=1}^n \pi r_k^2 = \pi r^2 \frac{1}{1 - \left(\frac{1-\sin\frac{C}{2}}{1+\sin\frac{C}{2}}\right)^2} = \pi r^2 \frac{(1 - \sin\frac{C}{2})^2}{4 \sin\frac{C}{2}} \equiv F_C \qquad \dots \text{\textcircled{3}}
\end{align*}
$$

と書けることから, 全ての面積和 $T$ は対称性から,

$$
\begin{align*}
T = F_A + F_B + F_C + \pi r^2 = \pi r^2 \left\{ 1 + \frac{(1-\sin\frac{A}{2})^2}{4\sin\frac{A}{2}} + \frac{(1-\sin\frac{B}{2})^2}{4\sin\frac{B}{2}} + \frac{(1-\sin\frac{C}{2})^2}{4\sin\frac{C}{2}} \right\}
\end{align*}
$$

$\triangle ABC$ が一辺 $a$ の正三角形の時, $A=B=C=\pi/3$, $r = \frac{\sqrt{3}}{6} a$ だから代入して,

$$
\begin{align*}
T = \frac{11}{96} \pi a^2
\end{align*}
$$

$$
\begin{align}

\begin{tikzpicture}[scale=1.2]
    \coordinate (C) at (0, 3);
    \coordinate (A) at (-2.5, 0);
    \coordinate (B) at (2.5, 0);

    \draw[thick] (A) node[left] {A} -- (B) node[right] {B} -- (C) node[above] {C} -- cycle;
    \draw (C) node[above right] {H_3};

    \draw (0, 0.9) circle (0.9);
    \node at (0.3, 0.9) {O_0};

    \draw (0, 2.1) circle (0.3);
    \node at (0.15, 2.1) {\tiny O_1};

    \node[left] at (-1.25, 1.5) {r};
    \node[below] at (0, 0) {H_2};

    \begin{scope}[shift={(3, 1)}]
        \draw[thick] (0,0) -- (1.5,0) node[midway, below] {r_n - r_{n+1}} -- (1.5, 1) -- cycle;
        \node[above left] at (0.75, 0.5) {r_n + r_{n+1}};
        \node[left] at (0.3, 0.15) {\frac{C}{2}};
        \node[above right] at (1.5, 1) {O_n};
        \node[below left] at (0, 0) {O_{n+1}};
    \end{scope}
\end{tikzpicture}

\end{align}
$$