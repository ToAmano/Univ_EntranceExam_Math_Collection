---
university: "todai"
category: "kouki"
year: "1999"
question: "2"
type: "solution"
title: "TODAI 1999 kouki Q2 (solution)"
---

## 【解】

### (1)

  

<figure id="1999-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1999/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円と直線，点$Q(t)$の様子</figcaption>
</figure>

  点 P $(−1, 0)$ を通り，傾きが $t$ の直線は
  
$$
\begin{align*}
y = t(x+1)
\end{align*}
$$

  だから，これと円$x^2+y^2=1$の交点の$x$座標は$y$を消去して
  
$$
\begin{align*}
& x^2 + \left(t(x+1)\right)^2 = 1         \\\therefore& x^2-1 +  \left(t(x+1)\right)^2 = 0      \\\therefore& (x+1)(x-1) +  \left(t(x+1)\right)^2 = 0 \\\therefore& (x+1)\left(x-1 + t^2(x+1)\right) = 0    \\\therefore& (x+1)\left((1+t^2)x+t^2-1\right) = 0
\end{align*}
$$

  より
  
$$
\begin{align*}
x = \frac{1-t^2}{1+t^2}
\end{align*}
$$

  である．従って$y$座標は$2t/(1+t^2)$となり，求める交点は
  
$$
\begin{align}
Q(t) = \left(\frac{1-t^2}{1+t^2}, \frac{2t}{1+t^2}\right)\label{1999-2:eq:1}
\end{align}
$$

  である．

  次に，線分$Q(t)Q(s)$の長さを求める．
  新しく傾き$t,s$に対して
  
$$
\begin{align*}
& t = \tan\theta_{t}&                                               \\& s = \tan\theta_{s}& 0 \le\theta_{s} < \theta_{t} < \frac{\pi}{2}
\end{align*}
$$

  とおくと，$\eqref{1999-2:eq:1}$および$\tan$の倍角公式
  
$$
\begin{align}
\begin{dcases}
      \cos \theta = \frac{1-\tan^2\theta}{1+\tan^2\theta} \\
      \sin \theta = \frac{2\tan\theta}{1+\tan^2\theta}
    \end{dcases}\label{1999-2:eq:3}
\end{align}
$$

  より
  
$$
\begin{align*}
Q(t) & = \left(\cos\theta_{t},\sin\theta_{t}\right)\\
    Q(s) & = \left(\cos\theta_{s},\sin\theta_{s}\right)
\end{align*}
$$

  だから，線分$Q(t)Q(s)$の長さの二乗は
  
$$
\begin{align}
\overline{Q(t)Q(s)}^2
     & = (\cos 2\theta_{t} - \cos 2\theta_{s})^2 + (\sin 2\theta_{t} - \sin 2\theta_{s})^2        \\& = 2 - 2 \left[\cos 2\theta_{t}\cos 2\theta_{s} - \sin 2\theta_{t}\sin 2\theta_{s}\right]\\& = 2 - 2 \cos(2\theta_{t} - 2\theta_{s}) \label{1999-2:eq:2}
\end{align}
$$

  である．ここに$t,s$を代入して
  
$$
\begin{align*}
\overline{Q(t)Q(s)}^2
     & = 2 - 2 \left\{\frac{1-t^2}{1+t^2}\frac{1-s^2}{1+s^2} + \frac{2t}{1+t^2}\frac{2s}{1+s^2}\right\}\\& = 2 \left\{\frac{(1+t^2)(1+s^2)-(1-t^2)(1-s^2)-4ts}{(1+t^2)(1+s^2)}\right\}\\& = \frac{4(t-s)^2}{(1+t^2)(1+s^2)}
\end{align*}
$$

  だから，$(1+t^2)(1+s^2)>0$，$t-s>0$より両辺ルートを取って
  
$$
\begin{align*}
\overline{Q(t)Q(s)} = \frac{2(t-s)}{\sqrt{(1+t^2)(1+s^2)}}
\end{align*}
$$

  である．  $\cdots$(答)

### (2)

  題意より，$\theta_{s} = \alpha$，$\theta_{t} = \beta$ である．
  $\eqref{1999-2:eq:2}$を$\alpha,\beta$で書き直して半角公式を用いると
  
$$
\begin{align*}
\overline{Q(t)Q(s)}^2
     & = 2 - 2 \cos(2\beta - 2\alpha) \\& = 4\sin^2(\beta-\alpha)
\end{align*}
$$

  である．
  $0 < \alpha < \beta < \pi/2$ だから, $\sin(\beta-\alpha)>0$ より
  
$$
\begin{align*}
\overline{Q(t)Q(s)}& = 2\sin(\beta-\alpha)                          \\& = 2(\sin\beta\cos\alpha - \cos\beta\sin\alpha)
\end{align*}
$$

  である．$\eqref{1999-2:eq:3}$より，これを$u,v$で表すと
  
$$
\begin{align}
\overline{Q(t)Q(s)}& = 2\left[\frac{2v}{1+v^2}\frac{1-u^2}{1+u^2} - \frac{1-v^2}{1+v^2}\frac{2u}{1+u^2}\right]\label{1999-2:eq:4}
\end{align}
$$

  だから，$u,v$が有理数なら$\overline{Q(t)Q(s)}$もまた有理数である．$\cdots$(答)
  

  （3）
  自然数$k$が$k=1,2,\cdots, n$をとるとして，直線の傾きが$t=k$の場合を考える．
  この時の対応する$\theta$を$\theta_{k}/2$とする，すなわち
  
$$
\begin{align}
& k = \tan\frac{\theta_{k}}{2}& \left(0 < \theta_{k} < \pi\right)\label{1999-2:eq:5}
\end{align}
$$

  とする．
  すると$\eqref{1999-2:eq:1}$より$Q(k)$の座標は
  
$$
\begin{align}
Q(k) & = \left(\cos\theta_{k}, \sin\theta_{k}\right)\\& = \left(\frac{1-\tan^2\frac{\theta_{k}}{2}}{1+\tan^2\frac{\theta_{k}}{2}}, \frac{2\tan\frac{\theta_{k}}{2}}{1+\tan^2\frac{\theta_{k}}{2}}\right)\label{1999-2:eq:6}
\end{align}
$$

  である．これらは$n=1,2,\cdots,n$に対して全て異なる点である．
  次に$\eqref{1999-2:eq:4}$より，$k=i,j\, (i<j)$に対して$Q(i)Q(j)$の長さは
  
$$
\begin{align}
\overline{Q(i)Q(j)}& = 2\left[\frac{2\tan\frac{\theta_{j}}{2}}{1+\tan^2\frac{\theta_{j}}{2}}\frac{1-\tan^2\frac{\theta_{i}}{2}}{1+ \tan^2\frac{\theta_{i}}{2}} - \frac{1-\tan^2\frac{\theta_{j}}{2}}{1+\tan^2\frac{\theta_{j}}{2}}\frac{2\tan\frac{\theta_{i}}{2}}{1+\tan^2\frac{\theta_{i}}{2}}\right]\label{1999-2:eq:7}
\end{align}
$$

  である．
  $\eqref{1999-2:eq:6,1999-2:eq:7}$に$\eqref{1999-2:eq:5}$を代入して
  
$$
\begin{align*}
Q(k) & = \left(\frac{1-k^2}{1+k^2}, \frac{2k}{1+k^2}\right)\\\overline{Q(i)Q(j)}& = 2\left[\frac{2j}{1+j^2}\frac{1-i^2}{1+i^2} - \frac{1-j^2}{1+j^2}\frac{2i}{1+i^2}\right]
\end{align*}
$$

  であり，$Q(k)$の座標および線分$Q(i)Q(j)$の長さは全て有理数である．

  従って，$1 \le i<j \le n$に対して全ての$\overline{Q(i)Q(j)}$の分母，および$k=1,2,\cdots, n$に対して$Q(k)$の全ての分母の積を$A$とすると，
  $A\in\mathbb{Z}$であり，点$C_{k}$を
  
$$
\begin{align*}
\vec{OA}_{k} = A\vec{OQ}_{k}
\end{align*}
$$

  によって定めれば，$A_{k}$は全て相異なる格子点であり（C1），かつ$i<j$に対して$\overline{A(i)A(j)}\in\mathbb{Z}$である（C3）．
  さらに，$A_{k}$は全て円$x^y+y^2=A^2$上にあるから，どの相異なる三点も同一直線上には存在しない（C2）．

  以上より，実際に条件(C1)，(C2)，(C3)を満たす点$A_1,\cdots,A_n$が存在することが示された．$\cdots$(答)
  
  

## 【解説】