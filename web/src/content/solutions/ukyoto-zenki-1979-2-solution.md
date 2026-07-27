---
university: "ukyoto"
category: "zenki"
year: "1979"
question: "2"
type: "solution"
title: "UKYOTO 1979 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $x=0, \pi, \pi/2$での成立が必要。又、$0 \le C < 2\pi$とする.

$$
\begin{align}
3a + b(1+2\cos C - 3\sin C) &= 1 \label{eq2_1}\\
  -a + b(1-2\cos C + 3\sin C) &= 1 \label{eq2_2}\\
  4a + b(1+2\sin C + 3\cos C) &= 1 \label{eq2_3}
\end{align}
$$

以下$\sin C = \alpha$, $\cos C = \beta$とおく. [(式eq2_1)](#eq2_1)+[(式eq2_2)](#eq2_2)から
\begin{equation}
  a + b = 1 \label{eq2_4}
\end{equation}
[(式eq2_4)](#eq2_4)を[(式eq2_1)](#eq2_1), [(式eq2_3)](#eq2_3)に代入

$$
\begin{align}
b(-2 + 2\beta - 3\alpha) + 2 &= 0 \label{eq2_5}\\
  b(-3 + 3\beta + 2\alpha) + 3 &= 0 \label{eq2_6}
\end{align}
[(式eq2_5)](#eq2_5)\times 3 - [(式eq2_6)](#eq2_6)\times 2から
$$

\begin{align*}
b[-6 + 6\beta - 9\alpha + 6 - 6\beta - 4\alpha] = 0
\end{align*}

$$

$$

\begin{align*}
\alpha b = 0
\end{align*}

$$
したがって, b=0又は\alpha=0 \iff C=0, \pi (\because 0 \le C < 2\pi) である.

1^\circ \ b=0の時\\
af(x)=1が任意のxで成立するようなaは存在せず, 不適.

2^\circ \ C=0の時 (この時\alpha=0, \beta=1)\\
[(式eq2_5)](#eq2_5)から2=0となり不適

3^\circ \ C=\piの時 (\alpha=0, \beta=-1)\\
[(式eq2_5)](#eq2_5)からb=\frac{1}{2}, [(式eq2_4)](#eq2_4)からa=\frac{1}{2}である. 逆にこの時
$$

\begin{align*}
\frac{1}{2}f(x) + \frac{1}{2}f(x-\pi) = 1
\end{align*}

$$
は任意のxについて成立し, 十分

以上を, Cを一般角に直して
$$

\begin{align*}
(a, b, C) = \left(\frac{1}{2}, \frac{1}{2}, \pi + 2n\pi\right) \ (n \in \mathbb{Z})
\end{align*}
$$