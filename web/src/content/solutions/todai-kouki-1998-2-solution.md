---
university: "todai"
category: "kouki"
year: "1998"
question: "2"
type: "solution"
title: "TODAI 1998 kouki Q2 (solution)"
---

## 【解】

### (1)
 (E)を変形して，
  
$$
\begin{align}
\int_0^{2\pi}\left\{[f(x)]^2 - 2f(x)\sin\theta\right\}dx = 0 \label{1998-2:eq:1}
\end{align}
$$

  である．ここに
  
$$
\begin{align*}
f(x) = r\sin(x+\theta)
\end{align*}
$$

  を代入して各項計算すると
  
$$
\begin{align*}
\int_0^{2\pi}\{f(x)\}^2dx
     & = \int_0^{2\pi} r^2 \sin^2(x+\theta) dx                                                 \\& = \frac{r^2}{2}\left[(x+\theta) - \frac{1}{2}\sin 2(x+\theta) \right]_0^{2\pi}\\& = \pi r^2                                                                               \\\int_0^{2\pi} f(x)\sin\theta dx
     & = r \int_0^{2\pi}\sin^2(x+\theta)\sin\theta dx                                         \\& = \frac{r}{2}\int_0^{2\pi}\{-\cos(2x+2\theta) + \cos\theta\} dx                       \\& = \frac{r}{2}\left[-\frac{1}{2}\sin(2x+2\theta) +  x \cdot\cos\theta\right]_0^{2\pi}\\& = \pi r \cos\theta
\end{align*}
$$

  だから，$\eqref{1998-2:eq:1}$に代入すると
  
$$
\begin{align*}
& \pi r^2 = 2\pi r \cos\theta\\\therefore& r = 2\cos\theta
\end{align*}
$$

  を得る．$\cdots$(答)

### (2)

  まず，パラメータの範囲
  
$$
\begin{align*}
\begin{dcases}
      0 < r \\
      0 \le \theta \le \frac{\pi}{4}
    \end{dcases}
\end{align*}
$$

  に(1)の$r=2\cos\theta$を代入すると，
  
$$
\begin{align}
0 \le\theta\le\frac{\pi}{4}\label{1998-2:eq:2}
\end{align}
$$

  の範囲では常に成立している．

  そこで，$\eqref{1998-2:eq:2}$のもとで
  
$$
\begin{align*}
f(x) = 2\cos\theta\sin(x+\theta) & \left(0 \le x \le\frac{\pi}{4}, 0 \le x \le\pi\right)
\end{align*}
$$

  の軌跡を求めれば良い．
  積和公式から
  
$$
\begin{align*}
f(x) = \sin(2\theta+x) + \sin x \equiv g(x, \theta)
\end{align*}
$$

  であり, $x$ を固定して $\theta$ を動かすと，$\eqref{1998-2:eq:2}$より
  
$$
\begin{align}
x \leq 2\theta+x \leq x+\frac{\pi}{2}\label{1998-2:eq:3}
\end{align}
$$

  である．

  

<figure id="1998-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1998/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $2\theta+x$の存在する領域．</figcaption>
</figure>

  $x$を動かした時のこの領域は[図1](#1998-2:fig:1)の斜線部（境界含む）だから，$\sin(2\theta+x)$の最大最小を考えて
  
$$
\begin{align*}
\begin{dcases}
      g(x, 0) \leq g(x, \theta) \leq g(x,\theta)|_{2\theta+x=\pi/2}       & 0 \leq x \leq \pi/4     \\
      g(x, \pi/4) \leq g(x, \theta) \leq g(x,\theta)|_{2\theta+x=x+\pi/2} & \pi/4 \leq x \leq \pi/2 \\
      g(x, \pi/4) \leq g(x, \theta) \leq g(x, 0)                          & \pi/2 \leq x \leq \pi
    \end{dcases}
\end{align*}
$$

  である．各点計算すると
  
$$
\begin{align*}
\begin{dcases}
      g(x, 0) = 2\sin x             \\
      g(x, \pi/4) = \sin x + \cos x \\
      g(x,\theta)|_{2\theta+x=x+\pi/2} = \sin x + 1
    \end{dcases}
\end{align*}
$$

  だから，求める領域は
  
$$
\begin{align*}
\begin{dcases}
      2\sin x \leq f(x) \leq  \sin x + 1         & 0 \leq x \leq \pi/4     \\
      \sin x + \cos x \leq f(x)  \leq \sin x + 1 & \pi/4 \leq x \leq \pi/2 \\
      \sin x + \cos x \leq f(x)  \leq 2\sin x    & \pi/2 \leq x \leq \pi
    \end{dcases}
\end{align*}
$$

  となり，図示すると[図2](#1998-2:fig:2)の斜線部(境界含む)である．
  $\cdots$(答)

  

<figure id="1998-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1998/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 求める領域は斜線部（教会含む）．</figcaption>
</figure>

### (3)

  求める面積$S$として, 図より
  
$$
\begin{align*}
S
     & = \int_0^{\pi/2}(1+\sin x)dx + \int_{\pi/2}^\pi(2\sin x)dx - \int_0^{\pi/4}(2\sin x)dx - \int_{\pi/4}^\pi(\sin x + \cos x)dx \\
\end{align*}
$$

  である．三角関数の対称性を用いて積分区間を変形すると
  
$$
\begin{align}
S
     & = \int_0^{\pi/2} dx + \int_0^{\pi/2} 3\sin x dx - \int_0^{\pi/4}\sin x dx -  \int_{0}^\pi\sin x dx   - \int_{\pi/4}^\pi\cos x dx \\& = \int_0^{\pi/2} dx + \int_0^{\pi/2}\sin x dx - \int_0^{\pi/4}\sin x dx - \int_{\pi/4}^\pi\cos x dx   \label{1998-2:eq:4}\\
\end{align}
$$

  だから，各項積分すると
  
$$
\begin{align*}
& \int_0^{\pi/2} dx = \frac{\pi}{2}\\& \int_{0}^{\pi/2}\sin x dx = \left[-\cos x\right]_{0}^{\pi/2} = 1                      \\& \int_{0}^{\pi/4}\sin x dx = \left[-\cos x\right]_{0}^{\pi/4} = 1-\frac{\sqrt{2}}{2}\\& \int_{\pi/4}^{\pi}\cos x dx = \left[\sin x\right]_{\pi/4}^{\pi} = -\frac{\sqrt{2}}{2}\\
\end{align*}
$$

  だから，$\eqref{1998-2:eq:4}$に代入して
  
$$
\begin{align*}
S
     & = \frac{\pi}{2} + 1 - \left(1-\frac{\sqrt{2}}{2}\right) +\frac{\sqrt{2}}{2}\\& =\frac{\pi}{2} + \sqrt{2}
\end{align*}
$$

  である．  $\cdots$(答)
  

  

## 【解説】