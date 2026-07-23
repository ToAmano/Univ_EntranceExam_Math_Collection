---
university: "utokyo"
category: "kouki"
year: "1990"
question: "1"
type: "solution"
title: "UTOKYO 1990 kouki Q1 (solution)"
---

## 【解】

    まずはPの存在する領域を求める．そのために排反事象である
    「点$P'$を通って，$Q$ の面積$4$を$1$と$3$に切り分けるような直線$l$を引くことができる」
    ような点$P'$の領域を求める．

    以下の2パターンを考えれば良い．
    

1.  $l$が隣り合う二辺を通る．

2.  $l$が向かい合う二辺を通る．

    対称性から，前者の代表として
    「1. OA,OCを通る」
    場合を，後者の代表として
    「2. OC,ABを通る」
    ものを調べる．あとはこうして求めた領域に平行移動，回転等の操作をすることによって$P'$の領域を求める．

    
    **1. OA,OCを通る時（隣り合う二辺）**

    

<figure id="1990-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1990/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: OA,OCを通る時（隣り合う二辺）</figcaption>
</figure>

    $l$の$x$切片，$y$切片を$S(a,0)$，$T(0,b)$とおく．ただし
    

$$
\begin{align}
0<a,b \le 2 \label{1990-1:eq:1}
\end{align}
$$

    とする．
    この時、三角形OSTの面積は$2$以下なので，これが$1$になれば条件を満たす．
    よって
    

$$
\begin{align}
& \frac{ab}{2} = 1         \\& ab=2 \label{1990-1:eq:2}
\end{align}
$$

    である．
    この元で直線$l$
    

$$
\begin{align*}
l: \frac{x}{a}+\frac{y}{b}=1
\end{align*}
$$

    の通過領域を求める．

    以下$a$を消去して計算を進める．
    [(式2)](#1990-1:eq:2)から$b=2/a$だから$l$の方程式は
    

$$
\begin{align}
y
         & = b\left(1-\frac{x}{a}\right)\\& = \frac{-b^2}{2}x + b  \label{1990-1:eq:3}\\& \equiv f(b)
\end{align}
$$

    であり，[(式1)](#1990-1:eq:1)より$b$のとりうる値は
    

$$
\begin{align}
& 0<b \le 2, 0<\frac{2}{b}\le 2    \\\therefore& 1 \le b \le 2 \label{1990-1:eq:4}
\end{align}
$$

    である．

    

<figure id="1990-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1990/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $x$の値による$b$の端点と$f(b)$の軸の関係．</figcaption>
</figure>

    [(式3)](#1990-1:eq:3)の[(式4)](#1990-1:eq:4)の元での最大最小を求めればよい．
    $x=0$の時は$f(0) = b$であり，$x\neq 0$の時は
    

$$
\begin{align*}
f(b)
         & =- \frac{x}{2}\left(b-\frac{1}{x}\right)^2 +\frac{1}{2x}
\end{align*}
$$

    だから，[図2](#1990-1:fig:2)より
    

$$
\begin{align*}
& \begin{dcases}
               x = 0 \text{の時}                   & 1 \le y \le 2                         \\
               0 < x \le \frac{1}{2} \text{の時}   & f(b=1) \le y \le f(b=2)               \\
               \frac{1}{2} \le x \le 1 \text{の時} & \min(f(b=1),f(b=2)) \le y \le f(1/2x) \\
               1 \le x \le 2 \text{の時}           & f(b=2) \le y \le f(b=1)
           \end{dcases}\\\therefore& \begin{dcases}
               1-\frac{x}{2} \le y \le 2(1-x)       & 0 \le x \le \frac{1}{2}           \\
               1-\frac{x}{2} \le y \le \frac{1}{2x} & \frac{1}{2} \le x \le \frac{2}{3} \\
               2(1-x)  \le y \le \frac{1}{2x}       & \frac{2}{3} \le x \le 1           \\
               2(1-x) \le y \le 1-\frac{x}{2}       & 1 \le x \le 2
           \end{dcases}
\end{align*}
$$

    が求める$l$の存在領域である．この様子を[図3](#1990-1:fig:3)に示す．

    

<figure id="1990-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1990/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $P'$の存在領域は斜線部（境界含む）．</figcaption>
</figure>

    
    **2. OC,ABを通る時（向かい合う二辺）**

    

<figure id="1990-1:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1990/1/fig_4.svg" alt="図 4" />
  <figcaption>図 4: OC,ABを通る時（向かい合う二辺）</figcaption>
</figure>

    $l$とOC,ABの交点を各々$S(0,a)$,$T(2,b)$とする．
    ただし
    

$$
\begin{align}
0 \le a,b \le 2 \label{1990-1:eq:5}
\end{align}
$$

    である．
    この時、Qのうち$l$の下側の部分の面積は，
    

$$
\begin{align*}
\frac{1}{2}\cdot 2 \cdot(a+b) = a+b
\end{align*}
$$

    である．

    対称性から
    

$$
\begin{align}
a+b \le 2 \label{1990-1:eq:6}
\end{align}
$$

    の時のみ考える．

    この時題意の条件は
    

$$
\begin{align}
a+b=1 \label{1990-1:eq:7}
\end{align}
$$

    である．
    直線$l$の方程式は
    

$$
\begin{align}
l: y
         & = \frac{b-a}{2}x+a \label{1990-1:eq:8}
\end{align}
$$

    とかける．

    以下$b$を消去して計算を進める．
    [(式7)](#1990-1:eq:7)を[(式8)](#1990-1:eq:5,1990-1:eq:8)に代入して
    

$$
\begin{align*}
\begin{dcases}
            y = \frac{1-a-a}{2}x+a = (1-x)a + \frac{x}{2} \equiv g(a) \\
            0 \le a \le 1
        \end{dcases}
\end{align*}
$$

    であるから$x = 1$の時は$y=1/2$である．
    $x\neq 1$の時は$y$は$a$の一次関数で
    

$$
\begin{align*}
& \begin{dcases}
               0 \le x < 1 \text{の時}   & g(a=0) \le y \le g(a=1) \\
               x = 1 \text{の時}         & y = 1/2                 \\
               1 \le x \le 2 \text{の時} & g(a=1) \le y \le g(a=0)
           \end{dcases}\\\therefore& \begin{dcases}
               \frac{x}{2} \le y \le 1-\frac{x}{2} & 0 \le x \le 1 \\
               1-\frac{x}{2} \le y \le \frac{x}{2} & 1 \le x \le 2
           \end{dcases}
\end{align*}
$$

    となる．この様子を[図5](#1990-1:fig:5)に示す．

    

<figure id="1990-1:fig:5">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1990/1/fig_5.svg" alt="図 5" />
  <figcaption>図 5: $P'$の存在領域は斜線部（境界含む）．</figcaption>
</figure>

    
    対称性から他のパターンについても考えると，[図6](#1990-1:fig:6)の斜線部（境界含む）が$P'$の存在領域である．

    

<figure id="1990-1:fig:6">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1990/1/fig_6.svg" alt="図 6" />
  <figcaption>図 6: 点P'の存在条件は斜線部（境界含む）</figcaption>
</figure>

    従って，$P'$が存在しない部分が$P$の存在領域であり，図示すると[図7](#1990-1:fig:7)となる．

    

<figure id="1990-1:fig:7">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1990/1/fig_7.svg" alt="図 7" />
  <figcaption>図 7: 点Pの存在条件は斜線部（境界含まず）</figcaption>
</figure>

    以上で点Pの存在領域がもとまったので，以下その面積$V$を求める．
    対称性から，$V$のうち$x,y \le 1$の領域の面積の4倍が$V$であるから
    

$$
\begin{align*}
V
         & = 4 \int_{\frac{1}{2}}^{1}(1-\frac{1}{2x}) dx \\& = [x - \frac{1}{2}\log x]_{\frac{1}{2}}^2     \\& = 2(1-\log 2)
\end{align*}
$$

    と求まる．$\cdots$(答)

    

## 【解説】