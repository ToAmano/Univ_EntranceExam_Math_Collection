---
university: "ukyoto"
category: "zenki"
year: "1969"
question: "1"
type: "solution"
title: "UKYOTO 1969 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

1.  $f(x)=0$ は実数範囲で少なくとも1つ解を持つことを示せば良い。\\
    $y=f(x)$ のグラフを考えると，$f(x) \to \pm \infty \ (x \to \pm \infty)$，\\
    $f(x)$ は連続だから，中間値の定理から $f(x)=0$ は実数範囲で少なくとも1つ解を持つ。
    [複素共役が解ならば (by (2))]

2.  (1)より，複素数 $\alpha$ に対して $f(\alpha)=0$ ならば $f(\bar{\alpha})=0$ であることから，$f(x)=0$ は複素数範囲で重根込めて3つの解しかないことから $f(x)=0$ の解は以下のいずれか。
    \begin{enumerate}

3.  3つとも実解

4.  1つ実解，2つが複素解

    
    
    $1^\circ$ の時\\
    3解 $\alpha, \beta, \gamma$ ($\alpha, \beta, \gamma < 0$) として $f(x)=(x-\alpha)(x-\beta)(x-\gamma)$ とおけるから，係数比較して
    

$$
\begin{align*}
\begin{aligned}
    -(\alpha+\beta+\gamma) &= a > 0 \\
    \alpha\beta+\beta\gamma+\gamma\alpha &= b > 0 \\
    -\alpha\beta\gamma &= c > 0
    \end{aligned}
\end{align*}
$$

    よって，$a, b, c > 0$。

    
    
    $2^\circ$ の時\\
    実解 $\alpha$，共役解を $p \pm qi$ ($p, q \in \mathbb{R}$, $p < 0, \alpha < 0$) とおくと，
    

$$
\begin{align*}
\begin{aligned}
    f(x) &= (x-\alpha)(x-(p+qi))(x-(p-qi)) \\
    &= (x-\alpha)(x^2 - 2px + (p^2+q^2))
    \end{aligned}
\end{align*}
$$

    と表せるから係数比較して
    

$$
\begin{align*}
\begin{aligned}
    -\alpha - 2p &= a > 0 \\
    p^2+q^2+2\alpha p &= b > 0 \\
    -\alpha(p^2+q^2) &= c > 0
    \end{aligned}
\end{align*}
$$

    よって $a, b, c > 0$。

    
    
    以上から，いずれの場合も $a, b, c > 0$ である。
\end{enumerate}