---
university: "todai"
category: "kouki"
year: "1997"
question: "2"
type: "solution"
title: "TODAI 1997 kouki Q2 (solution)"
---

## 【解】

### (1)

  A$(x,y)$とおく．
  $y = \frac{1}{|x|}$の$x<0, 0<x$での接点を$D(t, -\frac{1}{t}), E(s, \frac{1}{s})$ とする．
  ただし
  
$$
\begin{align}
t<0<s \label{1997-2:eq:1}
\end{align}
$$

  である．

  

<figure id="1997-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1997/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形ABCと点D，Eの様子．</figcaption>
</figure>

  この時，$(\frac{1}{x})' = -\frac{1}{x^2}$だから，D，Eでの接線の方程式は
  
$$
\begin{align}
\begin{dcases}
      AB: & y = \frac{1}{t^2}x - \frac{2}{t}  \\
      AC: & y = -\frac{1}{s^2}x + \frac{2}{s}
    \end{dcases}\label{1997-2:eq:2}
\end{align}
$$

  と書ける．

  従ってこの接線と$x$軸の交点がB，Cなので
  
$$
\begin{align}
\begin{dcases}
       & B(2t,0) \\
       & C(2s,0)
    \end{dcases}\label{1997-2:eq:3}
\end{align}
$$

  である．

  また，Aは二つの接線の交点だから，$\eqref{1997-2:eq:2}$を連立して$X$は
  
$$
\begin{align*}
& \frac{1}{t^2}X - \frac{2}{t} = -\frac{1}{s^2}X + \frac{2}{s}\\& \left(\frac{1}{t^2}+\frac{1}{s^2}\right)X =  \frac{2}{s} +  \frac{2}{t}\\& \left(t^2+s^2\right)X =  2st(s+t)                                       \\& X = \frac{2st(s+t)}{s^2+t^2}
\end{align*}
$$

  と求まる．この時$Y$は
  
$$
\begin{align*}
Y
     & = \frac{1}{t^2}X - \frac{2}{t}\\& =\frac{1}{t^2}\frac{2st(s+t)}{s^2+t^2} -\frac{2}{t}\\& =\frac{2s(s+t)-2(s^2+t^2)}{t(s^2+t^2)}\\& =\frac{2(s-t) }{(s^2+t^2)}
\end{align*}
$$

  となり，結局Aの座標は
  
$$
\begin{align}
A(\frac{2t^2s(t+s)}{t^2+s^2}, \frac{2(s-t)}{t^2+s^2}) \label{1997-2:eq:4}
\end{align}
$$

  と表せる．

  従って$\triangle ABC$の面積$T_1$は
  
$$
\begin{align}
T_1
     & = \frac{1}{2} |BC|\cdot Y                      \\& = \frac{1}{2}(2s-2t)\frac{2(s-t)}{t^2+s^2}\\& = 2\frac{(s-t)^2}{t^2+s^2}\label{1997-2:eq:5}
\end{align}
$$

  である．以下，点Aが動いた時の$T_1$のとりうる範囲を求める．

  題意よりDが線分AB上に存在することから，$x$座標に注目して，
  
$$
\begin{align*}
& t < X                        \\\therefore& t < \frac{2ts(t+s)}{t^2+s^2}\\\therefore& t(t^2+s^2) < 2ts(t+s)
\end{align*}
$$

  $t<0$に注意して
  
$$
\begin{align}
2s(t+s) < t^2+s^2 \label{1997-2:eq:6}
\end{align}
$$

  である．
  同様にEが線分AC上に存在することから，
  
$$
\begin{align*}
& X < s                        \\\therefore& \frac{2ts(t+s)}{t^2+s^2} < s \\\therefore& 2ts(t+s) < s(t^2+s^2)
\end{align*}
$$

  $s>0$より
  
$$
\begin{align}
2t(t+s) < t^2+s^2 \label{1997-2:eq:7}
\end{align}
$$

  である．

  以上から，$\eqref{1997-2:eq:6,1997-2:eq:7}$の条件のもとで$\eqref{1997-2:eq:5}$のとりうる範囲を求める．
  新しく
  
$$
\begin{align*}
& x = \frac{s}{t}& (x<0)
\end{align*}
$$

  とおくと，
  
$$
\begin{align}
\begin{dcases}
       & T_1  = \frac{2(x-1)^2}{(x^2+1)} = 2\left(1-\frac{2x}{x^2+1}\right) \\
       & x^2 + 2x -1 < 0                                                    \\
       & x^2 - 2x -1 > 0
    \end{dcases}\label{1997-2:eq:8}
\end{align}
$$

  である．後ろ二つの不等式から$x$のとりうる範囲は
  
$$
\begin{align}
& \begin{dcases}
         -1 -\sqrt{2} < x < -1 + \sqrt{2} \\
         x < 1 - \sqrt{2}, 1+\sqrt{2} < x
       \end{dcases}\\&
    -1 -\sqrt{2} < x < 1 - \sqrt{2}\label{1997-2:eq:9}
\end{align}
$$

  である．これは$x<0$を満たす．

  この時，$T_1$の一階微分は
  
$$
\begin{align*}
\frac{d T_1}{dx}& =\frac{4(x^2-1)}{(x^2+1)^2}
\end{align*}
$$

  だから，$T_1$の増減表は$\eqref{1997-2:table:1}$となる．

  \begin{table}[H]
    \centering
    \caption{$T_1$の増減表}
    \label{1997-2:table:1}
    

| $x$ | $-1-\sqrt{2}$ | | $-1$ | | $1-\sqrt{2}$ | |
|:------:|:-------------:|:----------:|:----:|:----------:|:------------:|:---:|
| $T_1'$ | | $+$ | $0$ | $-$ | | |
| $T_1$ | | $\searrow$ | | $\nearrow$ | | |

  \end{table}

  ここで
  
$$
\begin{align*}
& T_1(x=-1-\sqrt{2}) = \frac{6+4\sqrt{2}}{2+\sqrt{2}} =  2+\sqrt{2}\\& T_1(x=-1)          = 4                                            \\& T_1(x=1-\sqrt{2})  = \frac{2}{2-\sqrt{2}} = 2+\sqrt{2}
\end{align*}
$$

  だから，求める$T_1$のとりうる範囲は
  
$$
\begin{align*}
2+ \sqrt{2} < T_1 \leq 4
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  三角形$ADE$をなすベクトルについて
  
$$
\begin{align*}
\vec{AD}& = \frac{t^2-2st-s^2}{t^2+s^2}\begin{pmatrix} t \\ \frac{1}{t} \end{pmatrix}\\\vec{AE}& = \frac{s^2-2st-t^2}{t^2+s^2}\begin{pmatrix} s \\ -\frac{1}{s} \end{pmatrix}
\end{align*}
$$

  だから，サラスの公式より、$\triangle APE$の面積$T_2$として
  
$$
\begin{align*}
T_2
     & = \frac{1}{2}\left|\frac{t^2-2st-s^2}{t^2+s^2}\frac{s^2-2st-t^2}{t^2+s^2}\right|\left|t(-\frac{1}{s}) - s(\frac{1}{t})\right|& = \frac{1}{2}\left|\frac{(t^2-2st-s^2)(s^2-2st-t^2)}{st(t^2+s^2)}\right|
\end{align*}
$$

  である．

### (1)
と同様の変数変換$x=s/t$を用いると
  
$$
\begin{align}
T_2
     & = \frac{1}{2}\left|\frac{(1-2x-x^2)(x^2-2x-1)}{x(x^2+1)}\right|\\& = \frac{1}{2}\left|\frac{x^4-6x^2+1}{x(x^2+1)}\right|\label{1997-2:eq:10}
\end{align}
$$

  を得る．この$\eqref{1997-2:eq:9}$のもとでのとりうる値を求めれば良い．

  新しく
  
$$
\begin{align*}
f(x) = \frac{x^4-6x^2+1}{x(x^2+1)}
\end{align*}
$$

  とおくと，
  
$$
\begin{align*}
T_2 = \frac{1}{2}\left|f(x)\right|
\end{align*}
$$

  であり，$f(x)$の一階微分は
  
$$
\begin{align*}
f'(x)
     & = \frac{4x^2(x^2-3)(x^2+1)-(3x^2+1)(x^4-6x^2+1)}{x^2(x^2+1)^2}\\& = \frac{4a(a-3)(a+1)-(3a+1)(a^2-6a+1)}{a(a+1)^2}\quad(a=x^2) \\& = \frac{a^3+9a^2-9a-1}{a(a+1)^2}\\& = \frac{(a-1)(a^2+10a+1)}{a(a+1)^2}
\end{align*}
$$

  である．$a\ge 0$より$a^2+10a+1>0$だから，$f(x)$の増減表は$\eqref{1997-2:table:2}$となる．
  \begin{table}[H]
    \centering
    \caption{$f(x)$の増減表}
    \label{1997-2:table:2}
    

| $x$ | $-(1+\sqrt{2})$ | | $-1$ | | $-1+\sqrt{2}$ |
|:----:|:---------------:|:----------:|:----:|:----------:|:-------------:|
| $f'$ | | $+$ | $0$ | $-$ | |
| $f$ | $(0)$ | $\nearrow$ | $2$ | $\searrow$ | $(0)$ |

  \end{table}
  従って，求める$T_2$のとりうる範囲は
  
$$
\begin{align*}
0 < T_2 \leq 1
\end{align*}
$$

  である．$\cdots$(答)
  

  

## 【解説】