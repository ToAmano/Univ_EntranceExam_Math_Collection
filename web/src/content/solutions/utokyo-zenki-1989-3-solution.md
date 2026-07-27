---
university: "utokyo"
category: "zenki"
year: "1989"
question: "3"
type: "solution"
title: "UTOKYO 1989 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

$$
\begin{align*}
H = \{ z = x + y i \mid x, y \in \mathbb{R}, y > 0 \}. \text{ 以下, } z \text{ を } H \text{ に属する複素数とする. } q \in \mathbb{R}_{>0} \text{ とし, } f(z) = \frac{z+1-q}{z+1} \text{ とおく.}
\end{align*}
$$

1.  $f(z) \in H$ を示せ.

2.  $f_1(z) = f(z)$ とおき, $n = 2, 3, \dots$ に対し $f_n(z) = f(f_{n-1}(z))$ とおく. 全ての $H$ の元 $z$ に対し, $f_{10}(z) = f_1(z)$ が成立するような $q$ は?

\bigskip

$\triangleright$ "$x + y i$" 形だから基本コレ

(1) では, $f(z)$ の虚部が正を示せば OK

$$
\begin{align*}
\operatorname{Im} f(z) = \frac{1}{2i} \{ f(z) - \overline{f(z)} \} > 0
\end{align*}
$$

(2) は関数の問題. $f_{10} = f_1$ となる条件をもとめれば良いが, さすがに計はキツイから, $f_9 = z$ となる条件をもとめるか, 逆関数に注目.