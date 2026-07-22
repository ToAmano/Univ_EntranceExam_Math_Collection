---
university: "kyodai"
category: "kouki"
year: "2004"
question: "1"
type: "solution"
title: "KYODAI 2004 kouki Q1 (solution)"
---

## 【解】

    新しく
    

$$
\begin{align*}
g_n(x) & = 4nx(1-x) \\
        j(x)   & = 4x(1-x)
\end{align*}
$$

    とおくと，$y=g_n(x)$ のグラフはのようになる．

    新しく実数$0< \alpha,\beta<1$を
    

$$
\begin{align*}
g_n(x) = 1
\end{align*}
$$

    の二つの解とし，$\alpha < \beta$ とする．
    二次方程式の解の公式から
    

$$
\begin{align*}
\alpha& = \frac{1-\sqrt{1-1/n}}{2}\\\beta& = \frac{1+\sqrt{1-1/n}}{2}\\
\end{align*}
$$

    であり，$n\to\infty$のとき
    

$$
\begin{align}
\begin{dcases}
            \lim_{n\to\infty} \alpha & = 0 \\
            \lim_{n\to\infty} \beta  & = 1
        \end{dcases}\label{2004-1:eq:1}
\end{align}
$$

    が極限値となる．

    また，$h(n)$ を
    

$$
\begin{align*}
h(n) = n \int_0^1 f(g_n(x)) \, dx
\end{align*}
$$

    で定める．
    $h(n)$の$n\to\infty$での極限値を求めれば良い．

    グラフおよび$f(x)$の定義から, $h(x)$を明示的に書き下すと
    

$$
\begin{align*}
h(n)
         & = n \int_0^\alpha g_n(x) \, dx + n \int_\beta^1 g_n(x) \, dx \\& = n^2 \int_0^\alpha j(x) \, dx + n^2 \int_\beta^1 j(x) \, dx \\& = 2n^2 \int_0^\alpha j(x) \, dx
\end{align*}
$$

    である．ただし，最後の行で$j(x)$が$x=1/2$を軸に対称なので二つの積分が等しくなることを利用した．
    $J(x)$を$j(x)$の原始関数
    

$$
\begin{align}
J(x) = 2x^2 - \frac{4}{3}x^3 \label{2004-1:eq:2}
\end{align}
$$

    とすると，
    

$$
\begin{align}
h(n)
         & = 2n^2\left(J(\alpha) - J(0) \right)\label{2004-1:eq:3}
\end{align}
$$

    である．
    [(式2)](#2004-1:eq:2)を代入すると
    

$$
\begin{align}
h(n)
         & = 2n^2\left(2\alpha^2 - \frac{4}{3}\alpha^3\right)\\& = 4(n\alpha)^2 - \frac{8}{3}n^2\alpha^3 \label{2004-1:eq:4}
\end{align}
$$

    だから，以下各項の$n\to\infty$での極限値を求める．
    

$$
\begin{align*}
\lim_{n\to\infty}(n\alpha)^2
         & = \lim_{n\to\infty}\frac{1}{4}n^2\left(1-\sqrt{1-\frac{1}{n}}\right)^2          \\& = \lim_{n\to\infty}\frac{1}{4}\left(n-\sqrt{n^2-n}\right)^2                     \\& = \lim_{n\to\infty}\frac{1}{4}\left(\frac{n^2-(n^2-n)}{n+\sqrt{n^2-n}}\right)^2 \\& = \lim_{n\to\infty}\frac{1}{4}\left(\frac{1}{1+\sqrt{1-1/n}}\right)^2          \\& = \frac{1}{16}
\end{align*}
$$

    だから，二つ目の極限値は
    

$$
\begin{align*}
\lim_{n\to\infty}n^2\alpha^3
         & = \lim_{n\to\infty}(n\alpha)^2\alpha\\& = 0
\end{align*}
$$

    となる．従って，[(式4)](#2004-1:eq:4)に代入すると
    

$$
\begin{align*}
\lim_{n\to\infty}h(n) = 4\cdot\frac{1}{16} = \frac{1}{4}
\end{align*}
$$

    が求める極限値である．$\cdots$(答)

    
    

## 【解説】

    今回の解答では，対称性を利用して評価する量を減らしたり，
    極力$\alpha$を用いた見通しの良い変形を行うことで，
    計算量の少ないものとした．

    このような工夫は，以下のような問題の図形的解釈がわかっていれば素直に発想できるだろう．
    $n\to\infty$の時，$y=g_n(x)$と$y=1$の交点$\alpha,\beta$がそれぞれ$0,1$に近づくが，この時
    

$$
\begin{align*}
h(n)
         & = n \int_0^\alpha g_n(x) \, dx + n \int_\beta^1 g_n(x) \, dx
\end{align*}
$$

    がどう振る舞うか，というのが問題である．
    すなわち，積分区間はほぼ$0$に近づくだが，
    一方で全体に$n$がかかっているので，そことの勝負ということになる．
    この構造がわかっていると，$\alpha$を使ったまま全体を見通しよく式変形できる．

    ちなみに，高校範囲ではこの程度の解答が限界だが，
    [(式3)](#2004-1:eq:3)以下，
    大学数学の範囲のTaylor展開を利用すればさらにエレガントに解くことができる．
    Taylor展開とは，適切な条件を満たす関数$f(x)$に対して
    

$$
\begin{align*}
f(x) = f(a) + \frac{df(a)}{dx}\left(x-a\right)+\frac{1}{2!}\frac{d^2f(a)}{dx^2}\left(x-a\right)^2+\cdots
\end{align*}
$$

    のような展開のことを指す．これを$J(x)$の$x=0$での展開に用いると
    

$$
\begin{align*}
J(\alpha)= J(0)+J'(0)\alpha+\frac{1}{2}J''(0)\alpha^2+\Delta(\alpha^3)
\end{align*}
$$

    と展開できるから，[(式3)](#2004-1:eq:3)に代入すると
    

$$
\begin{align*}
h(n)
         & = 2n^2\left(J(\alpha) - J(0) \right)\\& = 2n^2\left(J'(0)\alpha+\frac{1}{2}J''(0)\alpha^2+\Delta(\alpha^3)\right)\\& = 2J'(0)n^2\alpha + J''(0)n^2\alpha^2+\Delta(n^2\alpha^3)
\end{align*}
$$

    となる．ここで$J'(0)=j(0)=0$だから1項目は$0$であり，残りの部分は解答中の極限評価を利用して
    

$$
\begin{align*}
\lim_{n\to\infty}h(n)
         & = \frac{J''(0)}{16}\\& = \frac{4}{16}\\& = \frac{1}{4}
\end{align*}
$$

    である．
    今回の問題の場合，このように$J(x)$の二回微分までの評価が必要なので大学数学の範囲が必要になる，というのがポイントだろう．