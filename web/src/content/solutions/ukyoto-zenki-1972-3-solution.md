---
university: "ukyoto"
category: "zenki"
year: "1972"
question: "3"
type: "solution"
title: "UKYOTO 1972 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $x' = x-a, y' = y-a, z' = z-a$ とおく. 手をくわえて

$$
\begin{align*}
\begin{cases}
x' + y' + z' = -2a \quad \cdots \text{①} \\
(x'+a)^3 + (y'+a)^3 + (z'+a)^3 = a^3 \quad \cdots \text{②}
\end{cases}
\end{align*}
$$

ここで, $P = x'^2 + y'^2 + z'^2$, $Q = y'z' + z'x' + x'y'$ とおく. ①より $a = -\frac{1}{2}(x'+y'+z')$ だから, ②に代入

$$
\begin{align*}
r + \frac{3}{2} P (x'+y'+z') + \frac{3}{4} (x'+y'+z')^2 - \frac{1}{4} (x'+y'+z')^3 = 0
\end{align*}
$$

$$
\begin{align*}
(x'+y'+z')(P-Q) + 3x'y'z' + \frac{1}{2}(x'+y'+z') [ (x'+y'+z')^2 - 3P ] = 0
\end{align*}
$$

$$
\begin{align*}
(x'+y'+z')(P-Q) + 3x'y'z' + (x'+y'+z')(P + 2Q - 3P) = 0
\end{align*}
$$

$$
\begin{align*}
x'y'z' = 0
\end{align*}
$$

よって $x', y', z'$ のうち少なくとも1つは 0, つまり $x, y, z$ のうち少なくとも1つは $a$ である.

\bigskip

[**解2**] (直接示す)

$$
\begin{align*}
x^3 + y^3 + z^3 = (x+y+z)^3
\end{align*}
$$

展開する

$$
\begin{align*}
3x^2 y + 3x^2 z + 3y^2 x + 3y^2 z + 3z^2 x + 3z^2 y + 6xyz = 0
\end{align*}
$$

$$
\begin{align*}
(y+z)(z+x)(x+y) = 0
\end{align*}
$$

よって OK \hfill 終