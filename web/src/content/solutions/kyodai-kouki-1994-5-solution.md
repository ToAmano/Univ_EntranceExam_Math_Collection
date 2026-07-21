---
university: "kyodai"
category: "kouki"
year: "1994"
question: "5"
type: "solution"
title: "KYODAI 1994 kouki Q5 (solution)"
---

## 【解】

  

<figure id="1994-5:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1994/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 座標平面上の半径$r$の円と点P,Qの様子</figcaption>
</figure>

  座標平面で原点Oを中心とする半径$r$の円を置く．
  P$(r,0)$として考えて良い．
  線分OPから線分OQに向かう角度を$\theta$とおく．
  弧PQの長さが$1$だから，
  
$$
\begin{align}
r\theta = 1 \label{1994-5:eq:1}
\end{align}
$$

  を満たす．ここで題意より$1<2\pi r$だから，
  
$$
\begin{align}
0 < \theta < 2\pi\label{1994-5:eq:2}
\end{align}
$$

  が成り立っていることに注意する．

  $\theta$の値によって場合分けして$S(r)$を考える．

  **1$^\circ$ $0 < \theta \leq \pi$ の時 (①から$r \leq 1$) **

  $S(\theta)$は[図2](#1994-5:fig:2)の斜線部の面積に等しく，
  
$$
\begin{align*}
S(\theta)
     & = \text{扇形}OPQ - \triangle OPQ                        \\& = \frac{1}{2}\theta r^2 - \frac{1}{2} r^2 \sin\theta
\end{align*}
$$

  となる．

  

<figure id="1994-5:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1994/5/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $0<\theta \le \pi$の時の領域の様子</figcaption>
</figure>

  
  **2$^\circ$ $\pi < \theta < 2\pi$ の時**

  $S(\theta)$は[図3](#1994-5:fig:3)の斜線部の面積に等しく，
  
$$
\begin{align*}
S(\theta)
     & = \text{扇形}OPQ + \triangle OPQ
     & = \frac{1}{2}\theta r^2 + \frac{1}{2} r^2 \sin(2\pi - \theta) \\& = \frac{1}{2}\theta r^2 - \frac{1}{2} r^2 \sin\theta
\end{align*}
$$

  となる．

  

<figure id="1994-5:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1994/5/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $\pi \le \theta < 2 \pi$の時の領域の様子</figcaption>
</figure>

  
  以上から，全ての場合で
  
$$
\begin{align*}
S(\theta) = \frac{1}{2}\theta r^2 - \frac{1}{2}r^2\sin\theta
\end{align*}
$$

  と書ける．
  $\eqref{1994-5:eq:1}$を代入して変数を$\theta$に取り替えると
  
$$
\begin{align*}
S(\theta) = \frac{1}{2}\frac{1}{\theta} - \frac{1}{2}\frac{1}{\theta^2}\sin\theta
\end{align*}
$$

  である．この$\eqref{1994-5:eq:2}$での最大値を求めれば良い．
  一階微分は
  
$$
\begin{align*}
\frac{dS}{d\theta}& = -\frac{1}{2\theta^2} - \frac{1}{2}\frac{1}{\theta^4}(\cos\theta\cdot\theta^2 - \sin\theta\cdot 2\theta)     \\& = -\frac{1}{2\theta^3}[\theta + \theta\cos\theta - 2\sin\theta]\\& = -\frac{1}{2\theta^3}[\theta(1+\cos\theta) - 2\sin\theta]\\& = -\frac{1}{2\theta^3}[2\theta\cos^2\frac{\theta}{2} - 4\sin\frac{\theta}{2}\cos\frac{\theta}{2}]\\& = -\frac{2\cos\frac{\theta}{2}}{\theta^3}\left[\frac{\theta}{2}\cos\frac{\theta}{2} - \sin\frac{\theta}{2}\right]
\end{align*}
$$

  ここで，$\theta=\pi$を代入すると$dS/d\theta=0$であり，それ以外の時は
  
$$
\begin{align*}
\frac{dS}{d\theta}= -\frac{2\cos^2\frac{\theta}{2}}{\theta^3}\left[\frac{\theta}{2} - \tan\frac{\theta}{2}\right]
\end{align*}
$$

  となり，これは$0<\theta<\pi$で正，$\pi<\theta<2\pi$で負だから，
  $S(\theta)$の増減表は$\eqref{1994-5:table:1}$のようになる．

  \begin{table}[H]
    \centering
    \caption{$S(\theta)$の増減表}
    \label{1994-5:table:1}
    

| $\theta$ | $0$ | | $\pi$ | | $2\pi$ |
|:--------:|:-----:|:----------:|:-----:|:----------:|:----------:|
| $S'$ | | $+$ | $0$ | $-$ | |
| $S$ | $(0)$ | $\nearrow$ | | $\searrow$ | $(1/4\pi)$ |

  \end{table}

  よって$S$は$\theta=\pi$で最大値をとり，その最大値は
  
$$
\begin{align*}
\max S(\theta)
     & = S(\theta)      \\& = \frac{1}{2\pi}
\end{align*}
$$

  である．$\cdots$(答)
  

  

## 【解説】

  解答中では半角，倍角公式をうまく使って$dS/d\theta$の正負を判定したが，
  普通にもう一度微分することでも増減表を求められる．
  計算量はこちらの方が多くなるが，一般的な方法でテクニックが不要なので採用しやすいだろう．
  $dS/d\theta$の式において，正負は分子
  
$$
\begin{align*}
f(\theta) = -(\theta + \theta\cos\theta - 2\sin\theta)
\end{align*}
$$

  の正負と等しい．そこで$f(\theta)$の一階，二階微分から$f$の正負を求める．
  
$$
\begin{align*}
f'(\theta)
     & = -(1+\cos\theta - \theta\sin\theta - 2\cos\theta) \\& = -(1 - \theta\sin\theta - \cos\theta)             \\
    f''(\theta)
     & = \theta\cos\theta
\end{align*}
$$

  より，まず$f'$の増減表は$\eqref{1994-5:table:2}$となる．

  \begin{table}[H]
    \centering
    \caption{$f'(\theta)$の増減表}
    \label{1994-5:table:2}
    

| $\theta$ | $0$ | | $\pi/2$ | | $3\pi/2$ | | $2\pi$ |
|:--------:|:---:|:----------:|:-------:|:----------:|:--------:|:----------:|:------:|
| $f''$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
| $f'$ | $0$ | $\nearrow$ | \| | $\searrow$ | \| | $\nearrow$ | $0$ |

  \end{table}

  増減表より，$\pi/2 < \alpha < 3\pi/2$で$f'(\alpha)=0$をみたす$\alpha$が唯一つある．
  従って$f(\theta)$の増減表は$\eqref{1994-5:table:3}$となる．ただし，$f(\pi)=0$に注意する．

  \begin{table}[H]
    \centering
    \caption{$f(\theta)$の増減表}
    \label{1994-5:table:3}
    

| $\theta$ | $0$ | | $\alpha$ | | $\pi$ | | $2\pi$ |
|:--------:|:---:|:----------:|:--------:|:----------:|:-----:|:----------:|:-------:|
| $f'$ | $0$ | $+$ | $0$ | $-$ | | $-$ | |
| $f$ | $0$ | $\nearrow$ | | $\searrow$ | $0$ | $\searrow$ | $-2\pi$ |

  \end{table}

  従って，$f(\theta)$は$0<\theta<\pi$で正，$\pi<\theta<2\pi$で負であり，解答中の増減表に一致する．