---
university: "todai"
category: "kouki"
year: "2001"
question: "1"
type: "solution"
title: "TODAI 2001 kouki Q1 (solution)"
---

## 【解】

    表現の簡潔さのため
    
$$
\begin{align*}
& f(n) = \sum_{k=2}^{n}\frac{k}{\sqrt{k^2-1}}\\& g(x) = \frac{x}{\sqrt{x^2-1}}& (x>1)
\end{align*}
$$

    とおくと，
    
$$
\begin{align}
f(n) = \sum_{k=2}^{n} g(k) \label{2001-1:eq:2}
\end{align}
$$

    である．さらに
    
$$
\begin{align*}
A(n) = n-f(n)
\end{align*}
$$

    とおく．
    $A(n)$の評価をすることで，題意の不等式が成り立つ$i$を求める．

    まず$y=g(x)$のグラフの概形を調べる．
    一階，二階微分は
    
$$
\begin{align*}
g'(x)
         & = -1(x^2-1)^{-3/2} < 0 \\
        g''(x)
         & =3x(x^2-1)^{-5/2} > 0
\end{align*}
$$

    だから，$g(x)$は下に凸で，
    
$$
\begin{align*}
& \lim_{x\to 1} g(x) \to\infty\\& \lim_{x\to \infty} g(x) \to 1
\end{align*}
$$

    だから，$y=g(x)$のグラフは[図1](#2001-1:fig:1)のようになる．

    

<figure id="2001-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2001/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=g(x)$のグラフの概形．</figcaption>
</figure>

    面積を比較するため，
    
$$
\begin{align}
S_n = \int_{3}^{n}g(x) dx \label{2001-1:eq:3}
\end{align}
$$

    とおくと，$\eqref{2001-1:eq:2}$に注意して$S_n,f(n)$の示す面積は[図2](#2001-1:fig:2)の斜線部である．
    以下$n \ge 3$として考える．

    

<figure id="2001-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2001/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $S_n$の面積を図示したもの．</figcaption>
</figure>

    

<figure id="2001-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2001/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $f_n$の上からの評価．斜線部の面積が$f_n$を表し，グレーアウトの部分が$S_n$を表す．</figcaption>
</figure>

    従って，まず[図3](#2001-1:fig:3)から，$f(n)$を上から評価すると
    
$$
\begin{align}
f(n) < S_n + g(2) + g(3) \label{2001-1:eq:4}
\end{align}
$$

    である．

    

<figure id="2001-1:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2001/1/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $f_n$の下からの評価．斜線部の面積が$f_n$を表し，グレーアウトの部分が$S_n$を表す．厳しく評価をするため，$f_n$の上の三角形部分も評価に含める．</figcaption>
</figure>

    次に[図4](#2001-1:fig:4)で$y \ge g(x)$の三角形部分の面積が
    
$$
\begin{align*}
& \frac{g(3)-g(4)}{2} + \frac{g(4)-g(5)}{2} + \cdots + \frac{g(n-1)-g(n)}{2}\\& = \frac{g(3)-g(n)}{2}
\end{align*}
$$

    だから，
    
$$
\begin{align}
& S_n + g(2) + g(n) + \frac{g(3)-g(n)}{2} < f(n)                           \\& S_n + g(2) + \frac{g(3)}{2} + \frac{g(n)}{2} < f(n)  \label{2001-1:eq:5}
\end{align}
$$

    である．

    以上$\eqref{2001-1:eq:4,2001-1:eq:5}$をまとめて
    
$$
\begin{align*}
S_n + g(2) + \frac{g(3)}{2} + \frac{g(n)}{2} < f(n) < S_n + g(2) + g(3)
\end{align*}
$$

    である．よって$A(n) = n-f(n)$より
    
$$
\begin{align*}
n-S_n - \left(g(2) + g(3)\right) < A(n) < n - S_n - \frac{g(n)}{2} - \left(g(2) + \frac{g(3)}{2}\right)
\end{align*}
$$

    である．以下これを評価する．
    まず$S_n$は
    
$$
\begin{align*}
S_n = [\sqrt{x^2-1}]_3^{n} = \sqrt{n^2-1} - 2\sqrt{2}
\end{align*}
$$

    だから，
    
$$
\begin{align}
n-\sqrt{n^2-1} + \left(2\sqrt{2}-g(2)-g(3)\right) < A(n) < n - \sqrt{n^2-1} - \frac{n}{2\sqrt{n^2-1}} + \left(2\sqrt{2}-g(2)-\frac{g(3)}{2}\right)\label{2001-1:eq:6}
\end{align}
$$

    となる．

    ここで新しく
    
$$
\begin{align*}
h(x) = x -\sqrt{x^2-1}
\end{align*}
$$

    とおくと，
    
$$
\begin{align*}
h(x) = \frac{1}{x+\sqrt{x^2-1}}
\end{align*}
$$

    より$2 \le x$では$h(x)$は単調減少である．
    そこで$n\to\infty$での$\eqref{2001-1:eq:6}$の両辺の振る舞いを考えると，
    
$$
\begin{align*}
\lim_{n\to\infty}\left[n-\sqrt{n^2-1}\right]& = \lim_{n\to\infty}\frac{1}{n+\sqrt{n^2-1}}\\& = 0                                          \\\lim_{n\to\infty}\left[n - \sqrt{n^2-1} - \frac{n}{2\sqrt{n^2-1}}\right]& = \frac{-1}{2}
\end{align*}
$$

    だから，

    
$$
\begin{align*}
\left(2\sqrt{2}-g(2)-g(3)\right) < \lim_{n\to\infty}A(n) < \frac{-1}{2}+ \left(2\sqrt{2}-g(2)-\frac{1}{2}g(3)\right)
\end{align*}
$$

    である．ここに
    
$$
\begin{align*}
g(2) & = \frac{2\sqrt{3}}{3}\\
        g(3) & = \frac{3\sqrt{2}}{4}
\end{align*}
$$

    を代入して
    
$$
\begin{align*}
\frac{5\sqrt{2}}{4} - \frac{2\sqrt{3}}{3} < \lim_{n\to\infty}A(n) < \frac{-1}{2} + \frac{13\sqrt{2}}{8} - \frac{2\sqrt{3}}{3}
\end{align*}
$$

    である．
    
$$
\begin{align*}
\sqrt{2}& = 1.414... \\\sqrt{3}& = 1.732...
\end{align*}
$$

    だから，
    
$$
\begin{align*}
\frac{5\sqrt{2}}{4} - \frac{2\sqrt{3}}{3}& >  \frac{5\cdot 1.414}{4} - \frac{2\cdot 1.733}{3}\\& = 0.612...
\end{align*}
$$

    および
    
$$
\begin{align*}
\frac{-1}{2} + \frac{13\sqrt{2}}{8} - \frac{2\sqrt{3}}{3}& < \frac{-1}{2} + \frac{13\cdot 1.415}{8} - \frac{2\cdot 1.732}{3}\\& = 0.644...
\end{align*}
$$

    だから，
    
$$
\begin{align*}
0.612 < \lim_{n\to\infty}A(n) < 0.645
\end{align*}
$$

    である．

    従って，任意の自然数$n$で$A_n \ge i/10$を満たすためには，
    
$$
\begin{align*}
i\le 6
\end{align*}
$$

    が必要．

    また，$h(x)$の単調減少性から，
    
$$
\begin{align*}
A(n)
         & > h(n) + \left(2\sqrt{2}-g(2)-g(3)\right)\\& > \lim_{n\to\infty}h(n) + \left(2\sqrt{2}-g(2)-g(3)\right)\\& = \left(2\sqrt{2}-g(2)-g(3)\right)\\& > 0.612...
\end{align*}
$$

    だから，$i\le 6$であれば常に$A(n) \ge i/10$を満たし十分である．
    以上から求める最大の$i$は
    
$$
\begin{align*}
i=6
\end{align*}
$$

    である．$\cdots$(答)

    
    

## 【解説】