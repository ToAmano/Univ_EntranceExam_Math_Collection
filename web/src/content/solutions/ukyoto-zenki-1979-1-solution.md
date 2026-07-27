---
university: "ukyoto"
category: "zenki"
year: "1979"
question: "1"
type: "solution"
title: "UKYOTO 1979 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (i) $p_1(x) = x + a$とおける. (i)に代入して

$$
\begin{align*}
\int_{-1}^1 C(x+a) dx = 0 \quad \therefore a = 0
\end{align*}
$$

より $p_1(x) = x$

(ii) $p_2(x) = x^2 + ax + b, \ f(x) = \alpha x + \beta$とおく.

$$
\begin{align*}
&\int_{-1}^1 (x^2+ax+b)(\alpha x+\beta) dx \\&= 2\alpha\int_0^1 ax^2 dx + 2\beta\int_0^1 (x^2+b) dx \\&= \frac{2}{3}a\alpha + 2\left(\frac{1}{3}+b\right)\beta = 0
\end{align*}
$$

が任意の$\alpha, \beta$で成立するので, $a=0, b=-\frac{1}{3}$となり

$$
\begin{align*}
p_2(x) = x^2 - \frac{1}{3}
\end{align*}
$$

(iii) $p_3(x) = x^3 + ax^2 + bx + c, \ f(x) = \alpha x^2 + \beta x + \gamma$とおく.

$$
\begin{align*}
&\int_{-1}^1 p_3(x) f(x) dx \\&= 2\alpha\int_0^1 (ax^4+cx^2) dx + 2\beta\int_0^1 (x^4+bx^2) dx + 2\gamma\int_0^1 (ax^2+c) dx \\&= 2\left(\frac{1}{5}a+\frac{1}{3}c\right)\alpha + 2\left(\frac{1}{5}+\frac{1}{3}b\right)\beta + 2\left(\frac{1}{3}a+c\right)\gamma\\&= 0
\end{align*}
$$

これが全ての$\alpha, \beta, \gamma$で成立するので,

$$
\begin{align*}
\begin{cases}
    \frac{1}{5}a + \frac{1}{3}c = 0 \\
    \frac{1}{5} + \frac{1}{3}b = 0 \\
    \frac{1}{3}a + c = 0
  \end{cases}
  \iff
  \begin{cases}
    a=c=0 \\
    b=-\frac{3}{5}
  \end{cases}
\end{align*}
$$

だから

$$
\begin{align*}
p_3(x) = x^3 - \frac{3}{5}x
\end{align*}
$$