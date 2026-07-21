---
university: "todai"
category: "kouki"
year: "2003"
question: "1"
type: "solution"
title: "TODAI 2003 kouki Q1 (solution)"
---

## 【解】

### (1)

    関数$f(x)$および$g(x)$を
    
$$
\begin{align*}
& f(x) = \sin x - \left(x - \frac{x^3}{3!}\right)\\& g(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \sin x
\end{align*}
$$

    とおく．
    $0 \leq x$ で $f(x) \geq 0$, $g(x) \geq 0$ を示せば良い．
    以下 $x \geq 0$ とする．

    まず$f(x)$について考える．
    一階，二階微分は
    
$$
\begin{align*}
f'(x)  & = \cos x - 1 + \frac{1}{2}x^2 \\
        f''(x) & = -\sin x + x \geq 0
\end{align*}
$$

    より，$f'' \geq 0$より $f'(x)$ は単調増加であって
    
$$
\begin{align*}
f'(x) \geq f'(0) = 0
\end{align*}
$$

    となる．
    したがって $f(x)$ も単調増加で，
    
$$
\begin{align*}
f(x) \geq f(0) = 0
\end{align*}
$$

    である．よって題意の下側の不等式は示された．

    次に$g(x)$について考える．一階，二階微分は
    
$$
\begin{align*}
g'(x)  & = 1 - \frac{1}{2}x^2 + \frac{1}{24}x^4 - \cos x \\
        g''(x) & = -x + \frac{1}{3}x^3 + \sin x                  \\
\end{align*}
$$

    となる．ここで式を見比べると$g''(x)=f(x)$だから，
    
$$
\begin{align*}
g''(x) = f(x) \ge 0
\end{align*}
$$

    となり，$g'(x)$は単調増加で
    
$$
\begin{align*}
g'(x) \geq g'(0)=0
\end{align*}
$$

    を満たす．
    従って$g(x)$も単調増加で
    
$$
\begin{align*}
g(x) \geq g(0)=0
\end{align*}
$$

    である．よって題意の右側の不等式が示された．

    以上より題意は示された．$\cdots$(答)

### (2)

    まず，$\sin^2x$の不定積分は積分定数$C$として
    
$$
\begin{align}
\int\sin^2 x dx = \frac{x}{2} - \frac{1}{4}\sin(2x) + C \label{2003-1:eq:1}
\end{align}
$$

    で与えられることに注意する．

    立体の体積 $V$ とすると
    
$$
\begin{align}
V & = \pi\int_0^x (\sin x)^2 dx                               \\& = \pi\left[\frac{x}{2} - \frac{1}{4}\sin(2x) \right]_0^x \\& = \frac{1}{2}\pi^2 \label{2003-1:eq:2}
\end{align}
$$

    である．

    

<figure id="2003-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2003/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=\sin x$と$a_n,b_n$の様子</figcaption>
</figure>

    
    (a)
    題意の条件及び$y = \sin x$ が $x = \pi/2$ を軸に対称なことから，
    $x=a_n$ から $x = \pi/2$ までが$2n$個に分割されたうちの一つの部分である．
    よって
    
$$
\begin{align}
\pi\int_{a_n}^{\pi/2}(\sin x)^2 dx & = \frac{1}{2n}V \label{2003-1:eq:3}
\end{align}
$$

    が成り立つ．

    平均値の定理から，$a_n < c_n < \pi/2$ をみたす $c_n$ で
    
$$
\begin{align*}
\int_{a_n}^{\pi/2}(\sin x)^2 dx = \left(\frac{\pi}{2}-a_n\right)\sin^2 c_n
\end{align*}
$$

    を満たすものが存在する．
    $\eqref{2003-1:eq:2}$に代入して
    
$$
\begin{align*}
& \pi\left(\frac{\pi}{2} - a_n\right)\sin^2 c_n  = \frac{1}{2n}V                 \\\therefore& \pi\left(\frac{\pi}{2} - a_n\right)\sin^2 c_n  = \frac{1}{2n}\frac{1}{2}\pi^2 \\& n \left(\frac{\pi}{2} - a_n\right)   = \frac{\pi}{4\sin^2 c_n}\\
\end{align*}
$$

    である．
    $n \to \infty$の時$a_n \to \pi/2$であり，従ってはさみうちの定理から$n \to \infty$ では $c_n \to \pi/2$ だから，
    
$$
\begin{align*}
\lim_{n \to \infty} n(\pi/2 - a_n)
         & = \lim_{n \to \infty}\frac{\pi}{4 \sin^2 c_n}\\& = \frac{\pi}{4 \sin^2(\pi/2)}\\& = \frac{\pi}{4}
\end{align*}
$$

    が求める極限値である．$\cdots$(答)
    

    (b) 題意より$0 \le x \le b_n$の領域が$2n$個に分割されたうちの一つの部分であるから
    
$$
\begin{align}
& \pi\int_0^{b_n}(\sin x)^2 dx                                = \frac{1}{2n}V                        \\\therefore& \pi\left[\frac{1}{2}x - \frac{1}{4}\sin 2x \right]_0^{b_n}  = \frac{1}{2n}V                        \\\therefore& \pi\left(\frac{1}{2}b_n - \frac{1}{4}\sin 2b_n \right)      = \frac{1}{2n}\frac{\pi^2}{2}\\\therefore& \frac{1}{4}\left(2b_n - \sin 2b_n\right)                        = \frac{\pi}{4n}\label{2003-1:eq:4}
\end{align}
$$

    である．

    ここで$b_n \to 0$ だから，(1) の不等式に$x=2b_n$を代入して
    
$$
\begin{align*}
& 2b_n - \frac{4}{3}b^3_n \leq\sin 2b_n \leq 2b_n - \frac{4}{3}b^3_n + \frac{4}{15}b^5_n                   \\\therefore& \frac{1}{3}b^3_n - \frac{1}{15}b^5_n  \leq\frac{1}{4}\left(2b_n - \sin 2b_n\right)\leq\frac{1}{3}b^3_n
\end{align*}
$$

    である．
    $\eqref{2003-1:eq:4}$に代入して
    
$$
\begin{align*}
\frac{1}{3}b^3_n - \frac{1}{15}b^5_n \leq\frac{\pi}{4n}\leq\frac{1}{3}b^3_n \\
\end{align*}
$$

    である．ここで，$n\to\infty$のとき$b_n\to 0$だから，$n$が十分大きい時
    
$$
\begin{align*}
0 < b^3_n - \frac{1}{5}b^5_n
\end{align*}
$$

    が成り立つ．このもとで変形を続けると
    
$$
\begin{align*}
& \frac{3\pi}{4}\leq nb^3_n \leq\frac{1}{ 1 - \frac{b^2_n}{5}}\frac{3\pi}{4}\\\therefore& \sqrt[3]{\frac{3\pi}{4}}\leq n^{1/3}b_n \leq\sqrt[3]{\frac{1}{1 - b^2_n/5}}\sqrt[3]{\frac{3\pi}{4}}
\end{align*}
$$

    を得る．
    $n>0$より両辺に$n^{p-1/3}$をかけると
    
$$
\begin{align}
\sqrt[3]{\frac{3\pi}{4}}n^{p-1/3}\leq n^{p}b_n \leq n^{p-1/3}\sqrt[3]{\frac{1}{1 - b^2_n/5}}\sqrt[3]{\frac{3\pi}{4}}\label{2003-1:eq:5}
\end{align}
$$

    となる．

    $p$の値によって$n^{p}b_n$の挙動がどう変化するかを調べる．

    
    \textbf{ア: $P < \frac{1}{3}$ の時}

    $n \to \infty$ で $b_n \to 0$ だから，$\eqref{2003-1:eq:5}$ の左辺，右辺共に $0$ に収束するからはさみうちの定理より
    
$$
\begin{align*}
\lim_{n\to\infty} n^p \cdot b_n = 0
\end{align*}
$$

    である．

    
    \textbf{イ: $P > \frac{1}{3}$ の時}

    $\eqref{2003-1:eq:5}$ の左辺が発散するから，追い出しの定理より
    
$$
\begin{align*}
\lim_{n\to\infty} n^p \cdot b_n = \infty
\end{align*}
$$

    
    \textbf{ウ: $P = \frac{1}{3}$ の時}

    $n \to \infty$ で $b_n \to 0$ だから $\eqref{2003-1:eq:5}$ の両辺共に $\left(\frac{3}{4}\pi\right)^{\frac{1}{3}}$ に収束する．
    従って挟み撃ちの定理より
    
$$
\begin{align*}
\lim_{n\to\infty} n^p \cdot b_n = \sqrt[3]{\frac{3\pi}{4}}
\end{align*}
$$

    である．

    
    以上の場合わけで全ての場合が尽くされた．
    よって求める$p$の値とその時の$n^{p}b_n$の収束値は
    
$$
\begin{align*}
\begin{dcases}
            p = \frac{1}{3} \\
            \lim_{n\to\infty} n^p \cdot b_n = \sqrt[3]{\frac{3\pi}{4}}
        \end{dcases}
\end{align*}
$$

    である．$\cdots$(答)
    

    

## 【解説】