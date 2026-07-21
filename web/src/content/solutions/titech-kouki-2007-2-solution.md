---
university: "titech"
category: "kouki"
year: "2007"
question: "2"
type: "solution"
title: "TITECH 2007 kouki Q2 (solution)"
---

## 【解】

### (1)

  $f(x)$の一階微分は
  
$$
\begin{align*}
f'(x)
     & = \frac{\tan x - x/\cos^2 x}{\tan^2x}\\& = \frac{\sin x\cos x - x}{\sin^2 x}
\end{align*}
$$

  である．
  $0<x<\pi/2$では$\sin x < x$, $0<\cos x<1$より
  
$$
\begin{align}
f'(x)<0 \label{2007-2:eq:1}
\end{align}
$$

  が成立する．$\cdots$(答)

  次に$f(x)$の二階微分は
  
$$
\begin{align*}
f''(x)
     & = \frac{d}{dx}\left(\frac{1}{\tan x} - \frac{x}{\sin^2 x}\right)\\& = \left( -\frac{1}{\sin^2x} - \frac{\sin^2x-2x\sin x\cos x}{\sin^4 x}\right)\\& = \frac{2\cos x(x-\tan x)}{\sin^3 x}
\end{align*}
$$

  である．$0<x<\pi/2$では$x < \tan x$より
  
$$
\begin{align}
f''(x) < 0 \label{2007-2:eq:2}
\end{align}
$$

  となる．$\cdots$(答)

  $\eqref{2007-2:eq:1,2007-2:eq:2}$より，$0<x<\pi/2$で$f(x)$は上に凸で単調減少する．
  また，極限値は
  
$$
\begin{align*}
\begin{dcases}
      f(x) \xrightarrow{x \to 0} 1 \\
      f(x) \xrightarrow{x \to \pi/2} 0
    \end{dcases}
\end{align*}
$$

  だから，グラフの概形は[図1](#2007-2:fig:1)である．

  

<figure id="2007-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2007/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $f(x)$の概形.</figcaption>
</figure>

### (2)

  $g(x) = f(x) + \frac{1}{f(x)}$ だから
  $g(x)$の一階微分は
  
$$
\begin{align*}
g'(x)
     & = f'(x) - \frac{f'(x)}{f^2(x)}\\& = f'(x)\left(1 - \frac{1}{f^2(x)}\right)
\end{align*}
$$

  である．$\eqref{2007-2:eq:1}$および$0<f(x)<1$より，
  
$$
\begin{align}
g'(x)>0 \label{2007-2:eq:3}
\end{align}
$$

  である．$\cdots$(答)

  次に$g(x)$の二階微分は
  
$$
\begin{align*}
g''(x)
     & = f''(x)\left(1 - \frac{1}{f(x)^2}\right) + 2 \frac{f'(x)^2}{f(x)^3}
\end{align*}
$$

  であり，$\eqref{2007-2:eq:1,2007-2:eq:2}$および$0<f(x)<1$から
  
$$
\begin{align}
g''(x)>0 \label{2007-2:eq:4}
\end{align}
$$

  である．$\cdots$(答)

  従って，$g(x)$は下に凸で単調増加する．
  また，極限値は
  
$$
\begin{align*}
\begin{dcases}
      g(x) \xrightarrow{x \to 0} 2 \\
      g(x) \xrightarrow{x \to \pi/2} \infty
    \end{dcases}
\end{align*}
$$

  であるから，グラフの概形は[図2](#2007-2:fig:2)である．

  

<figure id="2007-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2007/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $g(x)$の概形.</figcaption>
</figure>

### (3)

  新しく
  
$$
\begin{align*}
h(x) = \log\frac{a}{f(x)} - g(x)
\end{align*}
$$

  とおく．
  $0 < x < \pi/2$ で $h(x)=0$ が実解を持つ条件をもとめれば良い．
  $h(x)$ の一階微分は$\eqref{2007-2:eq:3}$より
  
$$
\begin{align*}
h'(x)
     & = - \frac{f'(x)}{f(x)} - g'(x)                                                       \\& = - \frac{f'(x)}{f(x)} - f'(x)\left(1 - \frac{1}{f(x)^2}\right)\quad(\because(3)) \\& = \frac{f'(x)}{f(x)^2}(f(x)^2 + f(x)-1)
\end{align*}
$$

  である．
  
$$
\begin{align*}
f(x)^2 + f(x) -1 = 0 \\\iff
    f(x) = \frac{-1 \pm \sqrt{5}}{2}
\end{align*}
$$

  だが，$0<f(x)<1$よりあり得るのは複号が正の場合で
  
$$
\begin{align*}
f(x) = \frac{-1 + \sqrt{5}}{2}
\end{align*}
$$

  である．(1)より$f(x)$は単調減少だから，これを満たす$x$がただ一つあるから，
  それを$x=\alpha$とおくと，
  $h(x)$の増減表は$\eqref{2007-2:table:1}$となる．

  \begin{table}[H]
    \centering
    \caption{$h(x)$の増減表}
    \label{2007-2:table:1}
    

| $x$ | $(0)$ | $\cdots$ | $\alpha$ | $\cdots$ | $(\pi/2)$ |
|:----:|:------------:|:----------:|:--------:|:----------:|:-----------:|
| $h'$ | | $+$ | $0$ | $-$ | |
| $h$ | $(\log a-2)$ | $\nearrow$ | | $\searrow$ | $(-\infty)$ |

  \end{table}
  ここで，
  
$$
\begin{align*}
f(\alpha)
     & = \frac{-1+\sqrt{5}}{2}\\
    g(\alpha)
     & = f(\alpha) + \frac{1}{f(\alpha)}\\& = \frac{-1+\sqrt{5}}{2} + \frac{2}{-1+\sqrt{5}}\\& = \sqrt{5}
\end{align*}
$$

  より，
  
$$
\begin{align*}
h(\alpha)
     & = \log a - \log f(\alpha) - g(\alpha)                           \\& = \log a - \log\frac{-1+\sqrt{5}}{2} - \sqrt{5}\\& = \log a - \log\left[\frac{-1+\sqrt{5}}{2} e^{\sqrt{5}}\right]
\end{align*}
$$

  である．したがって，増減表とあわせて$h(x)=0$が実数解を持つ条件は
  $h(\alpha)\ge 0$であり，求める$a$の条件は
  
$$
\begin{align*}
& h(\alpha) \ge 0                                                 \\\iff& \log a \ge\log\left[\frac{-1+\sqrt{5}}{2} e^{\sqrt{5}}\right]\\\iff& a \ge\frac{-1+\sqrt{5}}{2} e^{\sqrt{5}}
\end{align*}
$$

  となる．
  ただし$\log x$が単調増加であることを利用した．$\cdots$(答)

  
  

## 【解説】

  比較的単純な関数の問題．

### (1)
および(2)は単に二階微分まで計算するだけなので難しいところはない．
  答案中でやっているように，(2)は$g(x)$と$f(x)$の関係を使えば多少計算量を低減できる．

### (3)
は「交点を持つ」を「方程式が解をもつ」と言い換えて，$y$を消去した式（$h(x)$）の様子を考えるだけである．
  増減表を書くと$h(x)$は極大値を持つことがわかるのでそれが$0$以上をとると言い換えて条件を求めれば良い．
  接する場合も含めて等号を入れているが，「交わる」なので人によっては等号なしとするかもしれない．
  不安ならば答案にその旨記載すると良いだろう．