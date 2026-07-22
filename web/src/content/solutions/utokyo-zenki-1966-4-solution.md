---
university: "utokyo"
category: "zenki"
year: "1966"
question: "4"
type: "solution"
title: "UTOKYO 1966 zenki Q4 (solution)"
---

\input{macros}
     \begin{oframed}
     $x$に関する方程式$\dfrac{x}{9}-\sin\dfrac{\pi x}{6}=0$の最大の根に，もっとも近い整数を求めよ．
     \end{oframed}

## 【解】

$f(x)=\dfrac{x}{9}-\sin{\pi x}{6}$とおく．まず$6\le x$の時$f(x)=0$の解が存在しないことを示す．
     \begin{indentation}{2zw}{0pt}
     \underline{(ii)$6\le x\le12$の時} \\
     $\sin\dfrac{\pi x}{6}\le0<\dfrac{1}{9}x$より明らか．\\ \\
     \underline{(ii)$12\le x$の時} \\
     $\dfrac{1}{4}x>1\ge\sin\dfrac{\pi x}{6}$より明らか．\\
     \end{indentation}
以上から示された．$\Box$

さらに$f(x)$は$3\le x\le6$で単調減少であり($f(x)$は単調減少な関数の和)
\[f(4.5)=\frac{\sqrt{2}-1}{2}>0 , f(5)=\frac{-1}{18}<0\]
より，
中間値の定理から$4.5<x<5$に最大の解を持つ．よって求める整数は$5$である．$\cdots$(答)