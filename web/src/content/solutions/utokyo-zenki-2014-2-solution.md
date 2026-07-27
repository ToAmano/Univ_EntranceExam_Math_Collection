---
university: "utokyo"
category: "zenki"
year: "2014"
question: "2"
type: "solution"
title: "UTOKYO 2014 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

$\triangleright$ はじめは...

\begin{tikzpicture}[x=2cm, y=-1.5cm, >={stealth}]
\node at (1, 0) {\textcircled{1}};
\node at (2, 0) {\textcircled{2}};
\node at (3, 0) {\textcircled{3}};

\node (init) at (0, 1) {

|         |       |
|:-------:|:-----:|
| 白  赤  |       |
| $a+2$ | $1$ |

};

\node (1_top) at (1, 0.5) {

|         |
|:-------:|
|   白    |
| $a+2$ |

};
\node (1_bot) at (1, 1.5) {

|        |       |
|:------:|:-----:|
| 白  赤 |       |
| $a$  | $1$ |

};
\draw[->] (init) -- node[above] {$\frac{1}{a+3}$} (1_top);
\draw[->] (init) -- node[below left] {$\frac{a+2}{a+3}$} (1_bot);

\node (2_top) at (2, 0.5) {

|        |       |
|:------:|:-----:|
| 白  赤 |       |
| $a$  | $1$ |

};
\node (2_mid) at (2, 1.5) {

|       |
|:-----:|
|  白   |
| $a$ |

};
\node (2_bot) at (2, 2.5) {

|        |       |
|:------:|:-----:|
| 白  赤 |       |
| $a$  | $1$ |

};

\draw[->] (1_top) -- node[above] {$1$} (2_top);
\draw[->] (1_bot) -- node[above] {$\frac{1}{a+1}$} (2_mid);
\draw[->] (1_bot) -- node[below left] {$\frac{a}{a+1}$} (2_bot);

\node (3_top1) at (3, 0.2) {白・赤};
\node (3_top2) at (3, 0.8) {白};
\node (3_mid) at (3, 1.5) {

|        |       |
|:------:|:-----:|
| 白  赤 |       |
| $a$  | $1$ |

};
\node (3_bot1) at (3, 2.2) {白・赤};
\node (3_bot2) at (3, 2.8) {白};

\draw[->] (2_top) -- node[above left] {$\frac{a}{a+1}$} (3_top1);
\draw[->] (2_top) -- node[below left] {$\frac{1}{a+1}$} (3_top2);
\draw[->] (2_mid) -- node[above] {$1$} (3_mid);
\draw[->] (2_bot) -- node[above left] {$\frac{a}{a+1}$} (3_bot1);
\draw[->] (2_bot) -- node[below left] {$\frac{1}{a+1}$} (3_bot2);

\end{tikzpicture}

$$
\begin{align*}
p_1 = \frac{1}{a+3}, \quad p_2 = \frac{a+2}{a+3} \frac{1}{a+1}, \quad p_3 = \frac{1}{(a+1)(a+3)} + \frac{a(a+2)}{(a+1)^2(a+3)} = \frac{a^2+3a+1}{(a+1)^2(a+3)}
\end{align*}
$$

[解] (1) $p_1 = \frac{1}{a+3}, p_2 = \frac{a+2}{(a+3)(a+1)}$

(2) 2回目の操作後以降、$n$回目の操作後の箱の状態は以下のいずれか。

1.  白$a$、赤1 （$n$回目に白を引く）

2.  白$a$ （$n$回目に赤を引く）

したがって、$n+1$回目に赤を引くのは、

$$
\begin{align*}
p_{n+1} = \frac{1}{a+1} (1-p_n) \quad (n \ge 2)
\end{align*}
$$

である。変形して

$$
\begin{align*}
p_{n+1} - \frac{1}{a+2} = \frac{-1}{a+1} \left( p_n - \frac{1}{a+2} \right)
\end{align*}
$$

くり返し用いて、$n \ge 2$のとき、

$$
\begin{align*}
p_n &= \left(-\frac{1}{a+1}\right)^{n-2}\left( p_2 - \frac{1}{a+2}\right) + \frac{1}{a+2}\\&= (-1)^{n-2}\left(\frac{1}{a+1}\right)^{n-1}\frac{1}{(a+2)(a+3)} + \frac{1}{a+2}\\&= \frac{1}{a+2}\left\{ 1 - \left(-\frac{1}{a+1}\right)^{n-1}\frac{1}{a+3}\right\}
\end{align*}
$$

(3) (2)の表式は$n=1$でも成立する。 $A_m = \sum_{n=1}^m p_n$ とすると、

$$
\begin{align*}
(a+2) A_m &= \sum_{n=1}^m \left\{ 1 - \frac{1}{a+3}\left(-\frac{1}{a+1}\right)^{n-1}\right\}\\&= m - \frac{1}{a+3}\frac{1 - \left(-\frac{1}{a+1}\right)^m}{1 - \left(-\frac{1}{a+1}\right)}\\&= m - \frac{1}{a+3}\frac{a+1}{a+2}\left\{ 1 - \left(-\frac{1}{a+1}\right)^m \right\}
\end{align*}
$$

だから、$a \in \mathbb{N}$より、

$$
\begin{align*}
\frac{1}{m} A_m = \frac{1}{a+2} - \frac{1}{m} \frac{a+1}{(a+2)(a+3)} \left\{ 1 - \left(-\frac{1}{a+1}\right)^m \right\} \to \frac{1}{a+2}
\end{align*}
$$