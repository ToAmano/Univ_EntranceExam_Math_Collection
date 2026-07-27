---
university: "ukyoto"
category: "zenki"
year: "1979"
question: "3"
type: "solution"
title: "UKYOTO 1979 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解]
(i) $t > 0$から, AM-GM

$$
\begin{align*}
f(t) \ge 2\sqrt{t \cdot \frac{1}{t}} + \sqrt{2\left(t \cdot \frac{1}{t} + 1\right)} = 2 + \sqrt{3}
\end{align*}
$$

(等号成立は$t=1$)

$$
\begin{align*}
f(t)g(t) = \left(t+\frac{1}{t}+2\right) - \left(t+\frac{1}{t}+1\right) = 1
\end{align*}
$$

$$
\begin{align*}
\therefore g(t) = \frac{1}{f(t)} \quad (\because f(t) \ge 2+\sqrt{3})
\end{align*}
$$

だから, (i)から, $g(t)$は$f(t) = 2+\sqrt{3}$の時, $\max \frac{2-\sqrt{3}}{1}$をとる. 終

(ii) $x, y > 0$から\\
「$a, b, c$を$3$辺とする三角形が常に存在」\\
$\iff$ 「$\frac{a}{\sqrt{xy}}, \frac{b}{\sqrt{xy}}, \frac{c}{\sqrt{xy}} \quad \text{〃}$」\\
である. ここで, $\frac{a}{\sqrt{xy}} = A$などとおき, $t = \frac{x}{y} \ (t>0)$とおくと

$$
\begin{align*}
A = \sqrt{t+\frac{1}{t}+1}, \ B = p, \ C = \sqrt{t} + \frac{1}{\sqrt{t}}
\end{align*}
$$

まず, (i)から
\begin{equation}
  \max(C-A) = 2-\sqrt{3}, \ \min(A+C) = 2+\sqrt{3} \label{eq3_1}
\end{equation}
だから, もとめる条件は[(式eq3_1)](#eq3_1)が成立するような$A, C$の時での成立が必要で,

$$
\begin{align*}
2-\sqrt{3} < p < 2+\sqrt{3}
\end{align*}
$$

逆にこの時, $A+C \ge 2+\sqrt{3}, \ C-A \le 2-\sqrt{3}$だから$0 < C-A < p < A+C$となり, たしかに$A, B, C$を3辺とする三角形をつくることが出来, ($\because$ 三角不等式) 十分である.

以上から

$$
\begin{align*}
2-\sqrt{3} < p < 2+\sqrt{3}
\end{align*}
$$