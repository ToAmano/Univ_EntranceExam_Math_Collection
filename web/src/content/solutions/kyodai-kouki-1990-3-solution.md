---
university: "kyodai"
category: "kouki"
year: "1990"
question: "3"
type: "solution"
title: "KYODAI 1990 kouki Q3 (solution)"
---

## 【解】

### (1)

  点Pでの$y=\log x$での接線は
  
$$
\begin{align*}
l: y
     & = f_s(x)                  \\& = \frac{1}{s}(x-s)+\log s \\& = \frac{1}{s}x+\log s-1
\end{align*}
$$

  である．

  従って，$l$と$y$軸の交点である$Q$の座標は
  
$$
\begin{align*}
Q (0, \log s-1)
\end{align*}
$$

  である．

  これらの曲線の様子を[図1](#1990-3:fig:1)に示す．

  

<figure id="1990-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1990/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=\log x$とその接線の様子</figcaption>
</figure>

  よって線分PQの長さは
  
$$
\begin{align}
\overline{PQ}& = \sqrt{s^2+1}\label{1990-3:eq:1}
\end{align}
$$

  であり，曲線APの長さは
  
$$
\begin{align}
AP
     & = \int_1^s \sqrt{1+y'^2} dx                             \\& =\int_1^s \sqrt{1+\frac{1}{x^2}} dx \label{1990-3:eq:2}
\end{align}
$$

  であるから，求める量$t\equiv g(s)$は
  
$$
\begin{align}
t
     & = g(s)
     & = |PQ| - AP                                                             \\& = \sqrt{s^2+1} - \int_1^s \sqrt{1+\frac{1}{x^2}} dx \label{1990-3:eq:4}
\end{align}
$$

  となる．
  両辺$s$で微分して，$s\ge 1$に注意すると
  
$$
\begin{align*}
\frac{dt}{ds}& = \frac{s}{\sqrt{s^2+1}} - \sqrt{1+\frac{1}{s^2}}\\& =  \frac{-1}{s\sqrt{s^2+1}}
\end{align*}
$$

  が求める量である．  $\cdots$(答)

### (2)

  微分の連鎖律と(1)の結果から$u=1/s$に対して
  
$$
\begin{align}
\frac{du}{dt}& = \frac{du}{ds}\frac{ds}{dt}\\& = -s\sqrt{1+s^2}\cdot\left(-\frac{1}{s^2}\right)\\& = \sqrt{1+\frac{1}{s^2}}& = \sqrt{1+u^2}\label{1990-3:eq:3}
\end{align}
$$

  を得る． $\cdots$(答)

  次に$v=\sqrt{1+u^2}$に対しても同様に
  
$$
\begin{align*}
\frac{dv}{dt}& = \frac{dv}{du}\frac{du}{dt}\\& = \frac{u}{\sqrt{1+u^2}}\cdot\sqrt{1+u^2}\\& = u
\end{align*}
$$

  となる． $\cdots$(答)

### (3)

  $\eqref{1990-3:eq:3}$は変数分離型の微分方程式
  
$$
\begin{align*}
dt & = \frac{1}{\sqrt{1+u^2}} du
\end{align*}
$$

  だから積分できて，積分定数を$C$とすると
  
$$
\begin{align}
t = \log(u+\sqrt{1+u^2}) + C \label{1990-3:eq:5}
\end{align}
$$

  である．
  ここで$s=1$のとき$\eqref{1990-3:eq:4}$から
  
$$
\begin{align*}
t & = \sqrt{2}\\
    u & = 1/s = 1
\end{align*}
$$

  だから，$\eqref{1990-3:eq:5}$に代入すると，
  
$$
\begin{align}
\sqrt{2}& = \log(\sqrt{2}+1)+C                            \\\therefore
    C
     & = \sqrt{2}-\log(\sqrt{2}+1) \label{1990-3:eq:6}
\end{align}
$$

  である．

  以下，$\eqref{1990-3:eq:5}$を$u$についてとく．
  
$$
\begin{align}
& t - C =  \log(u+\sqrt{1+u^2})                \\\therefore& e^{t-C} = u+\sqrt{1+u^2}\\& e^{t-C}-u = \sqrt{1+u^2}\label{1990-3:eq:8}
\end{align}
$$

  である．以下ここから$u$を$t$の関数として表す．
  両辺二乗して，
  
$$
\begin{align}
& e^{2(t-C)} -2e^{t-C}u + u^2 = 1 + u^2                        \\\therefore& e^{2(t-C)}-2ue^{t-C}-1    = 0                                \\\therefore& u
    = \frac{e^{2(t-C)}-1}{2e^{t-C}}\\& = \frac{e^{t-C}}{2} - \frac{e^{-t+C}}{2}\label{1990-3:eq:7}
\end{align}
$$

  である．
  ここで$\eqref{1990-3:eq:6}$から
  
$$
\begin{align*}
e^{-C}& = e^{\log(\sqrt{2}+1)-\sqrt{2}}\\& = (\sqrt{2}+1)e^{-\sqrt{2}}
\end{align*}
$$

  なので，$\eqref{1990-3:eq:7}$に代入して
  
$$
\begin{align*}
u & = \frac{\sqrt{2}+1}{2}e^{t-\sqrt{2}} - \frac{1}{2(\sqrt{2}+1)}e^{-t+sqrt{2}}\\& = \frac{\sqrt{2}+1}{2}e^{t-\sqrt{2}} - \frac{\sqrt{2}-1}{2}e^{-t+sqrt{2}}
\end{align*}
$$

  を得る．これは$\eqref{1990-3:eq:8}$を満たしており十分である．

  以上から，求める関数は
  
$$
\begin{align*}
u & = = \frac{\sqrt{2}+1}{2}e^{t-\sqrt{2}} - \frac{\sqrt{2}-1}{2}e^{-t+sqrt{2}}
\end{align*}
$$

  である．  $\cdots$(答)
  

  

## 【解説】

  双曲線関数の問題．

### (2)
で登場した$u$と$v$は
  
$$
\begin{align*}
v^2-u^2 = 1
\end{align*}
$$

  と書ける．これはまさに双曲線関数の満たす方程式であり，
  
$$
\begin{align*}
u \sim\sinh s \\
    v \sim\cosh s
\end{align*}
$$

  のように関連しているだろうということがわかる．
  実際(3)の$u$の表式も細かい係数の違いはあれど$\sinh$の形になっており，計算があっていそうという検算になる．

### (3)
の解答では誘導をほぼ無視して$u$の微分方程式のみから解答を導いた．
  双曲線関数の知識があれば，$u$と$v$を用いてもう少し綺麗に解けるので見ていこう．

  与えられた微分方程式は
  
$$
\begin{align*}
\begin{dcases}
      \frac{du}{dt} & =v \\
      \frac{dv}{dt} & =u
    \end{dcases}
\end{align*}
$$

  の形だから，両辺足し引きして，
  
$$
\begin{align*}
\begin{cases}
      \frac{d}{dt}(u+v) = u+v \\
      \frac{d}{dt}(v-u) = -(v-u)
    \end{cases}
\end{align*}
$$

  である．
  この形は指数関数型の微分方程式だから，積分して
  
$$
\begin{align*}
\begin{dcases}
      u+v & = C_1 e^t    \\
      v-u & = C_2 e^{-t}
    \end{dcases}
\end{align*}
$$

  と書ける．ただし$C_1,C_2$は積分定数である．
  $s=1$の時，$t=\sqrt{2}$，$u=1$，$v=\sqrt{2}$だから，
  
$$
\begin{align*}
\begin{dcases}
      1+\sqrt{2} & = C_1 e^{\sqrt{2}}  \\
      \sqrt{2}-1 & = C_2 e^{-\sqrt{2}}
    \end{dcases}
\end{align*}
$$

  だから，
  
$$
\begin{align*}
u
     & = \frac{1}{2}\left\{(u+v) - (v-u) \right\}\\& = \frac{1}{2}\left\{(1+\sqrt{2})e^{t-\sqrt{2}} - (-1+\sqrt{2})e^{-t+\sqrt{2}}\right\}
\end{align*}
$$

  と求まる．計算量としてはこちらの方が多少楽だろう．