---
university: "todai"
category: "zenki"
year: "1967"
question: "1"
type: "solution"
title: "TODAI 1967 zenki Q1 (solution)"
---

\input{macros}
     \begin{oframed}
     $a$が正の定数，$n$が正の整数ならば，$x\ge0$において不等式
     $ax^{n+1}+\dfrac{1}{\sqrt[n]{a}}>x$が成り立つことを証明せよ．
     \end{oframed}

## 【解】

$a,n,x>0$だから，AM-GMより
     
$$
\begin{align*}
ax^{n+1}+\dfrac{1}{\sqrt[n]{a}}&=ax^{n+1}+n\frac{1}{n\sqrt[n]{a}}\\&\ge(n+1)\sqrt[n+1]{\frac{x^{n+1}}{n^n}}\\&=\frac{n+1}{n^{\frac{n}{n+1}}}x  \\&>\frac{n+1}{n}x  \\&>x
\end{align*}
$$

となって題意の不等式が示された．$\Box$