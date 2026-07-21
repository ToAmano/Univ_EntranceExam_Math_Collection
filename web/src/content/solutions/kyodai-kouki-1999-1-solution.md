---
university: "kyodai"
category: "kouki"
year: "1999"
question: "1"
type: "solution"
title: "KYODAI 1999 kouki Q1 (solution)"
---

## 【解】

    表現の簡潔さのため
    
$$
\begin{align*}
f(x)     & = x|x+2|  \\
        f_{+}(x) & = x(x+2)  \\
        f_{-}(x) & = -x(x+2)
\end{align*}
$$

    とおくと，$y=f(x)$ のグラフは[図1](#1999-1:fig:1)のようになる.

    

<figure id="1999-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1999/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=f(x)$と題意の領域$S_1,S_2$の様子．</figcaption>
</figure>

    $y=f(x)$ と3点で交わり,かつ原点を通る直線は[図1](#1999-1:fig:1)から明らかに$y$軸平行でないから,
    
$$
\begin{align*}
y=g(x) = mx
\end{align*}
$$

    とおける.
    $y=f(x)$と$y=g(x)$は原点$(0,0)$でまじわっているから，残りの二点の$x$座標を$\alpha,\beta\, (\alpha<\beta)$とおく．
    図から，これらの交点は
    
$$
\begin{align*}
\alpha < -2 \\
        -2 < \beta < 0
\end{align*}
$$

    を満たすから，それぞれ
    
$$
\begin{align*}
& f_{-}(x) = mx \\& f_{+}(x) = mx
\end{align*}
$$

    の解であり，
    
$$
\begin{align}
\begin{dcases}
            \alpha & = -2 -m \\
            \beta  & = -2 +m
        \end{dcases}\label{1999-1:eq:4}
\end{align}
$$

    である．

    また，$m$ の条件は，$y=f_{+}(x)$ での $x=0$ での傾きが$2$だから
    
$$
\begin{align}
0   < m < 2 \label{1999-1:eq:5}
\end{align}
$$

    である．

    以上の条件を元に，$S_1$および$S_2$を求める．
    まず$S_1$は$y=g(x)$と$y=f_{+}(x)$の囲む面積であり，$1/6$公式から
    
$$
\begin{align}
S_1
         & = \int_{\beta}{0}\left(mx - f_{+}(x)\right) dx \\& = \frac{1}{6}(-\beta)^3\label{1999-1:eq:1}
\end{align}
$$

    となる．

    次に$S_2$は，
    $y=g(x)$と$y=f_{-}(x)$の囲む面積$S_3$，
    $y=g(x)$と$y=f_{+}(x)$の囲む面積$S_1$，
    $y=0$と$y=f_{-}(x)$の囲む面積$S_4$
    を用いて図形的に
    
$$
\begin{align}
S_2 & = S_3+S_1 - 2S_4 \label{1999-1:eq:2}
\end{align}
$$

    と書ける．$S_3,S_4$も$1/6$公式により
    
$$
\begin{align*}
S_3
         & = \int_{\alpha}{0}\left(f_{-}-mx \right) dx \\& = \frac{1}{6}(-\alpha)^3                     \\
        S_4
         & = \int_{-2}{0} f_{-} dx                      \\& = \frac{1}{6}(2)^3                           \\& = \frac{4}{3}
\end{align*}
$$

    だから，$\eqref{1999-1:eq:2}$に代入して
    
$$
\begin{align}
S_2 = \frac{1}{6}(-\alpha)^3 + S_1 -\frac{8}{3}\label{1999-1:eq:3}
\end{align}
$$

    である．

    題意の通り$S_1 : S_2 = 9:8$となるとき，$S_1 : S_2 - S_1 = 9:-1$ より，
    $\eqref{1999-1:eq:1,1999-1:eq:3}$を代入して
    
$$
\begin{align*}
& \frac{1}{6}(-\beta)^3 : \left(\frac{1}{6}(-\alpha)^3 - \frac{8}{3}\right)  = 9:-1 \\\therefore& -(-\beta)^3 = 9\left\{(-\alpha)^3 - 16 \right\}\\& \beta^3  = -9(\alpha^3 + 16)
\end{align*}
$$

    となる．
    $\eqref{1999-1:eq:4}$を代入して
    
$$
\begin{align*}
& (m-2)^3                  = -9\{ -(m+2)^3 + 16 \}\\& m^3 - 6m^2 + 12m - 8     = -9[ -(m^3 + 6m^2 + 12m + 8) + 16]\\& m^3 - 6m^2 + 12m - 8     = 9m^3 + 54m^2 + 108m - 72          \\& 2m^3 + 15m^2 + 24m - 16  = 0                                 \\& (m+4)^2 (2m-1)           = 0                                 \\& m = -4, \frac{1}{2}
\end{align*}
$$

    となる．
    このうち$\eqref{1999-1:eq:5}$の条件を満たすのは
    
$$
\begin{align*}
m=\frac{1}{2}
\end{align*}
$$

    である．$\cdots$(答)

    
    

## 【解説】