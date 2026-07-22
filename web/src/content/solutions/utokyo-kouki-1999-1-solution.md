---
university: "utokyo"
category: "kouki"
year: "1999"
question: "1"
type: "solution"
title: "UTOKYO 1999 kouki Q1 (solution)"
---

## 【解】

    (1)
    $x \neq 0$の時，
    

$$
\begin{align*}
& \frac{\sin nx}{\sin x} = n\frac{\sin nx}{nx}\frac{x}{\sin x }\\\therefore& f_{n}(x) = n\frac{\sin nx}{nx}\frac{x}{\sin x }
\end{align*}
$$

    だから，両辺$n\to 0$の極限を取ると，
    

$$
\begin{align*}
& \lim_{x\to 0}f_{n}(x) = n \lim_{x\to 0}\frac{\sin nx}{nx}\frac{x}{\sin x }\\\therefore& c_{n} = n
\end{align*}
$$

    である．$\cdots$(答)

    
    （2）
    三倍角の公式より
    

$$
\begin{align*}
\sin 3x = (3-4\sin^2 x)\sin x = (4\cos^2 x - 1)\sin x
\end{align*}
$$

    だから$x\neq 0$の時，両辺$\sin x$で割って
    

$$
\begin{align*}
f_3(x) = 4\cos^2 x - 1
\end{align*}
$$

    である．$x=0$の時$f_3(0)=3$だからこの表現で良い．
    よって求める積分値は
    

$$
\begin{align*}
\int_{-\pi/2}^{\pi/2} f_3(x) dx
         & = \int_{-\pi/2}^{\pi/2}(4\cos^2 x - 1) dx \\& = 2\int_{0}^{\pi/2}(4\cos^2 x - 1) dx     \\& = 2\int_{0}^{\pi/2}(2(1+\cos 2x) - 1) dx  \\& = 2\int_{0}^{\pi/2}(1+2\cos 2x) dx        \\& = 2\left[x + \sin 2x\right]_{0}^{\pi/2}\\& = \pi
\end{align*}
$$

    である．$\cdots$(答)

    
    （3）
    分かりやすさのため
    

$$
\begin{align}
T_n = \int_{-\pi/2}^{\pi/2} f_n(x) dx \label{1999-1:eq:2}
\end{align}
$$

    とおく．加法定理および積和公式より
    

$$
\begin{align*}
\sin\left((2n+1)x\right)& = \sin 2nx \cos x + \cos 2nx \sin x                                   \\& = \frac{1}{2}\left(\sin(2n+1)x + \sin(2n-1)x\right) + \cos 2nx \sin x \\\therefore\sin\left((2n+1)x\right)& = \sin(2n-1)x + \cos 2nx \sin x
\end{align*}
$$

    だから，$x\neq 0$の時両辺を$\sin x$で割ることで
    

$$
\begin{align*}
f_{2n+1}(x) & = f_{2n-1}(x) + \cos 2nx
\end{align*}
$$

    である．$f_{n}(x)$の連続性より，$x= 0$の時もこの表現で良い．

    両辺を [- \pi/2, \pi/2]$ で積分して，$[(式2)](#1999-1:eq:2)より
    

$$
\begin{align*}
T_{n+1}& = T_n + \int_{-\pi/2}^{\pi/2}\cos 2nx dx                  \\& = T_n + \left[\frac{1}{2n}\sin 2nx\right]_{-\pi/2}^{\pi/2}\\& = T_n
\end{align*}
$$

    である．
    （3）より $T_1 = \pi$ だから漸化式を繰り返し用いることで，
    任意の自然数$n$について
    

$$
\begin{align*}
T_n=\pi
\end{align*}
$$

    である． $\cdots$(答)

    
    

## 【解説】

    (1)は以下のように，少し手間だが数学的帰納法によっても示せる．
    数学的帰納法により，
    

$$
\begin{align}
c_{n} = n \label{1999-1:eq:1}
\end{align}
$$

    であることを示す．

    まず，$n=1$のとき，
    

$$
\begin{align*}
f_{1}(x) = 1
\end{align*}
$$

    より
    

$$
\begin{align*}
c_{1} = 1
\end{align*}
$$

    である．

    次に，$n=k$での[(式1)](#1999-1:eq:1)の成立を仮定する．
    加法定理より
    

$$
\begin{align*}
\sin((k+1)x) = \sin kx \cos x + \cos kx \sin x
\end{align*}
$$

    だから，$-\pi/2 \le x \le \pi/2\, (x\neq 0)$の時両辺$\sin x$で割って，
    

$$
\begin{align*}
& \sin((k+1)x) = \sin kx \cos x + \cos kx \sin x \\\therefore& f_{k+1}(x) = \cos kx + f_{k}(x) \cos x
\end{align*}
$$

    である．$x\to 0$の極限を取ると，
    

$$
\begin{align*}
\lim_{x\to 0} f_{k+1}(x)
         & = \lim_{x\to 0}\left[\cos kx + f_{k}(x) \cos x\right]\\& = 1  + \lim_{x\to 0} f_{k}(x) \cos x
\end{align*}
$$

    だが，仮定より$\lim_{x\to 0} f_{k}(x)=k$だから
    

$$
\begin{align*}
\lim_{x\to 0} f_{k+1}(x)
         & = 1 + k
\end{align*}
$$

    となる．$f_{k+1}(x)$が$x=0$で連続であるから
    

$$
\begin{align*}
c_{k+1} = k+1
\end{align*}
$$

    である．従って[(式1)](#1999-1:eq:1)は$n=k+1$でも成立する．

    以上から，数学的帰納法により任意の自然数$n$について
    

$$
\begin{align*}
c_{n} = n
\end{align*}
$$

    である． $\cdots$(答)