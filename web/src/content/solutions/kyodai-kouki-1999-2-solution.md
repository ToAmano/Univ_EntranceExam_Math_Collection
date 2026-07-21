---
university: "kyodai"
category: "kouki"
year: "1999"
question: "2"
type: "solution"
title: "KYODAI 1999 kouki Q2 (solution)"
---

## 【解】

  変数を減らして解くことを考える．
  $\alpha + \beta + \gamma = \pi$ より$\gamma$を削除して
  
$$
\begin{align*}
\gamma = \pi - (\alpha + \beta)
\end{align*}
$$

  だから，これを他の条件に代入して
  
$$
\begin{align}
& \begin{dcases}
         \sin\alpha\sin\beta\sin\gamma = \sin\alpha\sin\beta\sin(\alpha+\beta) \\
         0 < \alpha, \beta, \pi - (\alpha + \beta) < \pi
       \end{dcases}\\\therefore& \begin{dcases}
         \sin\alpha\sin\beta\sin\gamma = -\frac{1}{2}\{\cos(2\alpha+\beta)-\cos\beta\}\sin\beta \\
         0 < \alpha, \beta, \alpha+\beta < \pi
       \end{dcases}\label{1990-2:eq:1}
\end{align}
$$

  を得る．そこで以下，
  
$$
\begin{align*}
f(\alpha,\beta) =  -\frac{1}{2}\{\cos(2\alpha+\beta)-\cos\beta\}\sin\beta
\end{align*}
$$

  の最大値を求める．

  そのため$\beta$を固定し, $\alpha$をうごかす．
  この時$\eqref{1990-2:eq:1}$より$\alpha$の値域は
  
$$
\begin{align}
0 < \alpha < \pi-\beta\label{1990-2:eq:2}
\end{align}
$$

  である．
  $\sin\beta > 0$ から $f$は $\cos(2\alpha+\beta)$の単調減少関数で,
  $\cos(2\alpha+\beta)$が最小のとき$f$は最大値をとる．
  $2\alpha+\beta$のとりうる値は，$\eqref{1990-2:eq:2}$より
  
$$
\begin{align*}
\beta < 2\alpha+\beta < 2\pi-\beta
\end{align*}
$$

  だから，
  
$$
\begin{align*}
2\alpha+\beta = \pi\\\therefore\alpha = \frac{\pi-\beta}{2}
\end{align*}
$$

  の時に$f$は最大値をとる．その最大値は
  
$$
\begin{align}
\max f(\alpha,\beta)
     & = f\left(\frac{\pi-\beta}{2}\right)\\& = -\frac{1}{2}\sin\beta(-1-\cos\beta) \\& = \frac{1}{2}\sin\beta(1+\cos\beta)   \\& \equiv g(\beta)
\end{align}
$$

  である．

  そこで，次に $\beta$ を $0 < \beta < \pi$ でうごかして$g(\beta)$の最大値を求める．
  一階微分は
  
$$
\begin{align*}
g'(\beta)
     & = \frac{1}{2}\left[\cos\beta(1+\cos\beta)-\sin^2\beta\right]\\& = \frac{1}{2}\left[2\cos^2\beta + \cos\beta -1\right]\\& = \frac{1}{2}(2\cos\beta-1)(\cos\beta+1)
\end{align*}
$$

  となるから，$g(\beta)$の増減表は$\eqref{1999-2:table:1}$となる．

  \begin{table}[H]
    \centering
    \caption{$f(x)$の増減表}
    \label{1999-2:table:1}
    

| $\beta$ | 0 | $\cdots$ | $\pi/3$ | $\cdots$ | $\pi$ |
|:-----------:|:---:|:----------:|:-------:|:----------:|:-----:|
| $\cos\beta$ | 1 | $+$ | $1/2$ | $-$ | $-1$ |
| $g'(\beta)$ | | $+$ | 0 | $-$ | |
| $g(\beta)$ | 0 | $\nearrow$ | | $\searrow$ | 0 |

  \end{table}

  従って, $S(\beta)$は $\beta = \pi/3$ の時最大値
  
$$
\begin{align*}
\max S(\beta)
     & = S\left(\frac{\pi}{3}\right)\\& = \frac{3}{8}\sqrt{3}
\end{align*}
$$

  をとる．
  （解答としては求められないが）この時$\alpha = \beta = \gamma = \pi/3$である．$\cdots$(答)

  
  

## 【解説】

  この問題は，有名不等式を用いてかなりエレガントに解くことができるので紹介しよう．
  まず，相加相乗平均の不等式より
  
$$
\begin{align*}
\sqrt[3]{\sin\alpha\sin\beta\sin\gamma}\le\frac{\sin\alpha+\sin\beta+\sin\gamma}{3}
\end{align*}
$$

  である．ここで等号成立は
  
$$
\begin{align*}
\sin\alpha=\sin\beta=\sin\gamma
\end{align*}
$$

  の時である．

  次に，$y=\sin x$は$0\le x\le \pi$で上に凸だから，イェンゼンの不等式より
  
$$
\begin{align*}
\frac{\sin\alpha+\sin\beta+\sin\gamma}{3}& \le\sin\left(\frac{1}{3}\alpha+\frac{1}{3}\beta+\frac{1}{3}\gamma\right)\\& = \sin\frac{\pi}{3}\\& = \frac{\sqrt{3}}{2}
\end{align*}
$$

  と上側から評価できる．等号成立は
  
$$
\begin{align*}
\alpha=\beta=\gamma
\end{align*}
$$

  の時である．

  以上二つの不等式の評価より，
  
$$
\begin{align*}
\sin\alpha\sin\beta\sin\gamma\le\left(\frac{\sqrt{3}}{2}\right)^3 = \frac{3}{8}\sqrt{3}
\end{align*}
$$

  であり，等号成立は
  
$$
\begin{align*}
& \sin\alpha=\sin\beta=\sin\gamma\land\alpha=\beta=\gamma\\\therefore& \alpha=\beta=\gamma = \frac{\pi}{3}
\end{align*}
$$

  の時である．

  このように，等号成立条件が同一になる場合は，複数の不等式を重ねて利用して評価していける．