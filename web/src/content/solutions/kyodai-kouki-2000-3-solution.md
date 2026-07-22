---
university: "kyodai"
category: "kouki"
year: "2000"
question: "3"
type: "solution"
title: "KYODAI 2000 kouki Q3 (solution)"
---

## 【解】

  (1)
  $a,k$は整数だから，$(-ak, k)$は一つの格子点である．  $\cdots$(答)

  
  (2)

  

<figure id="2000-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2000/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 直線$L$の様子</figcaption>
</figure>

  $L$上 $x, y > 0$ の部分に格子点 $( \alpha, \beta )\, (\alpha,\beta>0)$ があると仮定して，背理法によって題意を示す．
  $L$の方程式に$(x,y)=(\alpha, \beta)$を代入して
  

$$
\begin{align*}
a\alpha + (a^2+1)\beta& = a(a^2+1)
\end{align*}
$$

  両辺$a^2+1>0$で割って，
  

$$
\begin{align*}
& \frac{a\alpha}{(a^2+1)} + \beta = a              \\& \beta = a\left( 1 - \frac{\alpha}{a^2+1}\right)
\end{align*}
$$

  を得る．$\beta$は整数だから，
  

$$
\begin{align*}
\frac{a\alpha}{a^2+1}
\end{align*}
$$

  が整数でなければならない．
  $a, a^2+1$ は互いに素だから $\alpha$ が $a^2+1$ を割り切る必要がある．
  しかし，$\alpha,\beta>0$だから，
  

$$
\begin{align*}
0 < \alpha < a^2+1
\end{align*}
$$

  であり，$\alpha$ が $a^2+1$ を割り切ることはない．
  よって矛盾した．
  従って背理法により，$L$上 $x, y > 0$ には格子点は存在しない．$\cdots$(答)

  
  (3)

  

<figure id="2000-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2000/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 直線$L$の様子</figcaption>
</figure>

  (2)と同様に，$(\alpha, \beta)$を$L$上の格子点として，$\alpha,\beta>0$とする．
  このような点が存在することを示す．

  $L$の方程式に$(x,y)=(\alpha, \beta)$を代入して
  

$$
\begin{align}
& a\alpha + (a^2+1)\beta  = k                         \\& \beta = \frac{k-a\alpha}{a^2+1}\label{2000-3:eq:1}
\end{align}
$$

  である．$k$は整数だから，$a^2+1$で割った商を$p$，余りを$q$とすると
  

$$
\begin{align}
k = p(a^2+1) + q \quad(0 \leq q \le a^2) \label{2000-3:eq:2}
\end{align}
$$

  と表せる．

  次に，$a$と$a^2+1$は互いに素だから，
  $a, 2a, \dots, (a^2)a, (a^2+1)a$ を $a^2+1$ でわったあまりの集合は $0, 1, 2, \dots, a^2$ である．
  従って，$\alpha a$を$a^2+1$で割ったあまりが$q$となるような$\alpha$が$1,2,\cdots a^2+1$の中に必ず存在し，
  $r$を整数として
  

$$
\begin{align}
\alpha a = r(a^2+1) + q \quad(1 \le\alpha\le a^2+1) \label{2000-3:eq:3}
\end{align}
$$

  と書ける．

  以上[(式3)](#2000-3:eq:2,2000-3:eq:3)を[(式1)](#2000-3:eq:1)に代入して
  

$$
\begin{align*}
\beta& = \frac{(p(a^2+1) + q) - (r(a^2+1)+q)}{a^2+1}\\& = p - r
\end{align*}
$$

  となり，$p,r$が整数だから$\beta$も整数である．

  また，[(式3)](#2000-3:eq:3)の$\alpha$の値域と，$k>a(a^2+1)$から
  

$$
\begin{align*}
\beta& = \frac{k-a\alpha}{a^2+1}\\& > \frac{a(a^+1)-a(a^2+1)}{a^2+1}\\& = 0                              \\\therefore\beta& > 0
\end{align*}
$$

  だから，$\beta$は正の整数である．

  以上から，$(\alpha, \beta)$ は $L$上 $x, y > 0$ をみたす格子点であるから，題意は示された．$\cdots$(答)

  
  

## 【解説】

  $a$と$a^2+1$が互いに素であることが問題の肝である．
  このことを生かしてより直接的に式変形をする方法もあるので紹介しよう．

  (2)
  $L$の方程式で$k=a(a^2+1)$を代入して
  

$$
\begin{align*}
ax + (a^2+1)y = a(a^2+1) \\
    a\left( x - a^2 - 1 \right) + (a^2+1)y = 0
\end{align*}
$$

  を得る．
  $a, a^2+1$ は互いに素であるから，これをみたす $x, y \in \mathbb{N}$ があると仮定すると，
  $y$は $a$ の倍数で、$y=al$ なる $l \in \mathbb{N}$ がある．
  この時
  

$$
\begin{align*}
x = (1-l)(a^2+1)
\end{align*}
$$

  ここで$l$が自然数だから，これは$x\le 0$となり，$x>0$を満たすことはなく，矛盾する．$\cdots$(答)

  
  (3)
  $L$の方程式を整理すると
  

$$
\begin{align*}
a(x+ak) + (a^2+1)(y-k) = 0
\end{align*}
$$

  となる．$x,y$が自然数とすると，
  $a, a^2+1$は互いに素だから，$x+ak$は$(a^2+1)$の倍数であり，$y-k$は$-a$の倍数である．
  すなわち，
  

$$
\begin{align*}
& \begin{dcases}
         x + ak = l(a^2+1) \\
         y - k = -la
       \end{dcases}\\\therefore& \begin{dcases}
         x = l(a^2+1) -ak \\
         y = -la + k
       \end{dcases}
\end{align*}
$$

  ここで$l$は整数である．

  従って，あとは$x,y>0$を満たすような$l$が存在すれば良い．
  $x,y>0$にこの式を代入して
  

$$
\begin{align}
\frac{ak}{a^2+1} < l < \frac{k}{a}\label{2000-3:eq:4}
\end{align}
$$

  となるが，$k> a(a^2+1)$ のとき，両端の値の差は
  

$$
\begin{align*}
\frac{k}{a} - \frac{ak}{a^2+1}& = \frac{k(a^2+1) - a^2k}{a(a^2+1)}\\& = \frac{k}{a(a^2+1)}\\& > 1
\end{align*}
$$

  となり，確かに[(式4)](#2000-3:eq:4)を満たす $l \in \mathbb{Z}$ は存在する．
  よって示された．$\cdots$(答)