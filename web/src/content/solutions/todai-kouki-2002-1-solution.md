---
university: "todai"
category: "kouki"
year: "2002"
question: "1"
type: "solution"
title: "TODAI 2002 kouki Q1 (solution)"
---

## 【解】

### (1)

    $f(x)=xe^{-x^3}$の一階および二階微分は
    
$$
\begin{align*}
f'(x)  & =e^{-x^3}(1-3x^3)          \\
        f''(x) & =e^{-x^3}(-9x^2-3x^2+9x^5) \\& =e^{-x^3}3x^2(3x^3-4)
\end{align*}
$$

    だから，増減表は[表1](#2002-1:table:1)となる．
    

<figure id="2002-1:table:1" class="table-wrapper">

| $x$ | $-\infty$ |  | 0 |  | $\sqrt[3]{\frac{1}{3}}$ |  | $\sqrt[3]{\frac{4}{3}}$ |  | $\infty$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $f'$ |  | $+$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ |  |
| $f''$ |  | $+$ | $0$ | $-$ | $-$ | $-$ | $0$ | $+$ |  |
| $f$ | $-\infty$ |  | $0$ |  |  |  |  |  | $0$ |

  <figcaption>表 1: $f(x)$の増減表</figcaption>
</figure>

    また，極限値および極値は以下のとおりである．
    
$$
\begin{align*}
& f\left(\sqrt[3]{1/3}\right) = \sqrt[3]{1/3}e^{-1/3}\\& f\left(\sqrt[3]{4/3}\right) = \sqrt[3]{4/3}e^{-4/3}\\& \lim_{x\to -\infty}f(x) = -\infty\\& \lim_{x\to \infty}f(x) = 0
\end{align*}
$$

    従って，グラフの概形は[図1](#2002-1:fig:1)である．$\cdots$(答)

    

<figure id="2002-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2002/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $f(x)$のグラフの概形</figcaption>
</figure>

### (2)

    題意より
    
$$
\begin{align*}
V_1(C) = \pi\int_0^c \{f(x)\}^2 dx
\end{align*}
$$

    であり，積分部分を評価して
    
$$
\begin{align*}
V_1(C)
         & = \pi\int_0^c \{f(x)\}^2 dx          \\& = \int_0^c x^2 e^{-2x^3} dx           \\& = [-\frac{1}{6}e^{-2x^3}]_0^c         \\& = \frac{1}{6}\left(1-e^{-2c^3}\right)
\end{align*}
$$

    だから、$C\to\infty$の極限を取って
    
$$
\begin{align*}
\lim_{C\to\infty} V_1(C)
         & = \lim_{C\to\infty}\frac{\pi}{6}(1-e^{-2c^3}) \\& = \frac{\pi}{6}
\end{align*}
$$

    が求める極限値である．$\cdots$(答)

### (3)

    

<figure id="2002-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2002/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 斜線部が回転する領域</figcaption>
</figure>

### (1)
より，
    
$$
\begin{align}
p=\sqrt[3]{\frac{1}{3}}\label{2002-1:eq:0}
\end{align}
$$

    とおくと
    
$$
\begin{align}
M = p e^{-\frac{1}{3}}\label{2002-1:eq:1}
\end{align}
$$

    である．
    $f(x)$の$x \sim x+\Delta x \, (\Delta x << 1)$の部分をy軸まわりに回転した立体の体積は、
    幅$\Delta x$、高さ$f(x)$、長さ$2\pi x$の直方体の体積で近似できるから（バームクーヘン公式），
    $p=\sqrt[3]{\frac{1}{3}}$が積分区間の上端だから，
    
$$
\begin{align}
V_2
         & = \int_0^p 2\pi x(M-f(x))dx                                        \\& = 2\pi M\int_0^p x dx - 2\pi\int_0^p xf(x) dx \label{2002-1:eq:2}
\end{align}
$$

    である．各項積分すると
    
$$
\begin{align*}
\int_0^p xf(x)dx
                     & = \int_0^p x^2 e^{-x^3} dx              \\& = \left[-\frac{1}{3}e^{-x^3}\right]_0^p \\& = \frac{1}{3}\left(1-e^{-p^3}\right)\\\int_0^p xdx & = \frac{1}{2}p^2
\end{align*}
$$

    だから，$\eqref{2002-1:eq:2}$に代入して
    
$$
\begin{align*}
V_2
         & = 2\pi\left[\frac{1}{2}Mp^2 - \frac{1}{3} + \frac{1}{3}e^{-p^3}\right]
\end{align*}
$$

    ここに$\eqref{2002-1:eq:0,2002-1:eq:1}$を代入すると
    
$$
\begin{align*}
V_2
         & = 2\pi\left[\frac{p^3}{2} e^{-\frac{1}{3}} - \frac{1}{3} + \frac{1}{3}e^{-p^3}\right]\\& = 2\pi\left[\frac{1}{6} e^{-\frac{1}{3}}  - \frac{1}{3} + \frac{1}{3}e^{-\frac{1}{3}}\right]\\& = 2\pi\left[\frac{1}{2} e^{-\frac{1}{3}}  - \frac{1}{3}\right]
\end{align*}
$$

    が求める体積である．$\cdots$(答)

    

## 【解説】