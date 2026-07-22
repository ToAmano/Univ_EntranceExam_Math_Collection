---
university: "kyodai"
category: "kouki"
year: "2002"
question: "2"
type: "solution"
title: "KYODAI 2002 kouki Q2 (solution)"
---

## 【解】

    

<figure id="2002-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2002/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 楕円と円の様子</figcaption>
</figure>

    楕円と円を$C_1$, $C_2$とする．
    

$$
\begin{align}
& C_1: \frac{x^2}{1} + \frac{y^2}{4} = 1 \label{2002-2:eq:1}\\& C_2: (x-a)^2 + y^2 = b \quad(b>0) \label{2002-2:eq:2}
\end{align}
$$

    すると$C_1,C_2$は$x$軸に関して対称だから，
    [(式2)](#2002-2:eq:1,2002-2:eq:2)が$(\alpha,\beta)$ $(\beta>0)$を
    交点に持てば, $(\alpha,-\beta)$も交点になる.
    従って, [(式1)](#2002-2:eq:1)を[(式2)](#2002-2:eq:2)に代入して得られる$x$の2次方程式
    

$$
\begin{align}
(x-a)^2 + 4(1-x^2) = b \label{2002-2:eq:3}
\end{align}
$$

    が $C_1$の$x$の範囲である$-1< x< 1$ に2異解を持てば良い.
    $x=\pm 1$の時は交点が$4$つにならず二つになるから不適である．

    [(式3)](#2002-2:eq:3)を展開して
    

$$
\begin{align*}
& -3x^2 - 2ax + a^2 - 4 - b = 0 \\\therefore& 3x^2 + 2ax - a^2 + 4 + b = 0
\end{align*}
$$

    だから，左辺を$f(x)$
    

$$
\begin{align*}
f(x) = 3x^2 + 2ax - a^2 + 4 + b
\end{align*}
$$

    とおいて，$f(x)=0$の判別式を$D$として
    $f(x)=0$が$-1<x<1$に2異解を持つための条件は以下の通り．

    

$$
\begin{align*}
& \begin{dcases}
               D/4>0                        \\
               \text{端点:} f(1)> 0, f(-1)> 0 \\
               \text{軸:}   -1 < -a/3 < 1
           \end{dcases}\\\therefore& \begin{dcases}
               a^2 - 3(-a^2-4+b) > 0 \\
               -a^2 + 2a - 1 + b > 0 \\
               -a^2 - 2a - 1 + b > 0 \\
               -3 < a < 3
           \end{dcases}
\end{align*}
$$

    この領域を図示して[図2](#2002-2:fig:2)斜線部(境界含まず)

    

<figure id="2002-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2002/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 楕円と円が$4$つの交点を持つための$a,b$の範囲．境界は含まない．</figcaption>
</figure>

    $\cdots$(答)
    

## 【解説】