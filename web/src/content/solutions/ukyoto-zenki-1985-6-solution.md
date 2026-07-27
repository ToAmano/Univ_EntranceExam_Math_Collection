---
university: "ukyoto"
category: "zenki"
year: "1985"
question: "6"
type: "solution"
title: "UKYOTO 1985 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (2)で、$x=a$として、

$$
\begin{align*}
a f(a) = 0 \quad \cdots \text{①}
\end{align*}
$$

又、(1)から、(2)の両辺 $x$ で微分できて、

$$
\begin{align*}
b f(x) = f(x) + x f'(x)
\end{align*}
$$

$$
\begin{align*}
\therefore (b-1) f(x) = x f'(x) \quad \cdots \text{②}
\end{align*}
$$

$y = f(x)$ として②に代入すると、

$$
\begin{align*}
(b-1) y = x \frac{dy}{dx}
\end{align*}
$$

まず $y \neq 0$ とする。

$$
\begin{align*}
\frac{b-1}{x} dx = \frac{1}{y} dy
\end{align*}
$$

両辺積分して、$C_0$ を定数として、

$$
\begin{align*}
(b-1) \log x = \log y + C_0
\end{align*}
$$

$$
\begin{align*}
\therefore y = C \cdot x^{b-1} \quad (C\text{：定数}) \quad \cdots \text{③}
\end{align*}
$$

ここで、$y=0$ の時もこの表式で良い。①から、

$$
\begin{align*}
a \cdot C \cdot a^{b-1} = 0 \iff C = 0 \text{ or } a = 0
\end{align*}
$$

に注意すると、$C$ を定数として、

$$
\begin{align*}
y = C x^{b-1} \quad \text{//}
\end{align*}
$$

である。\\
{[解注]}\\
さらにこまかく分類すれば、（(1)に注意して）

$$
\begin{align*}
\begin{cases}
a=0 \wedge 1 \le b \text{ の時 } & y = C x^{b-1} \\
a \neq 0 \text{ or } b < 1 \text{ の時 } & y = 0
\end{cases}
\end{align*}
$$

となる。