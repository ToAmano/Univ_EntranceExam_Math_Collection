---
university: "todai"
category: "kouki"
year: "2004"
question: "1"
type: "solution"
title: "TODAI 2004 kouki Q1 (solution)"
---

## 【解】

### (1)

    

<figure id="2004-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2004/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 原点を$P_0$とする$xy$平面に，$P_1(1,0)$を配置する．</figcaption>
</figure>

    $y$軸を$\Im$軸, $x$軸を$\Re$軸とする複素平面で考え, $P_n, P_{n+1}$ を表す複素数を $\alpha_n$ と表す．
    また，
    
$$
\begin{align*}
e(\theta) = \cos\theta + i\sin\theta
\end{align*}
$$

    と置く．
    すると実数数列 $a_n (a_n > 0)$ と $\theta_n$ があって
    
$$
\begin{align}
\alpha_n = a_n e(i\theta_n) \label{2004-1:eq:1}
\end{align}
$$

    と表すことができる．

    条件(a)から
    
$$
\begin{align*}
a_{n+1} = r a_n
\end{align*}
$$

    であって，初期条件$a_0 = 1$ から, 等比数列の公式から
    
$$
\begin{align}
a_n = r^n \label{2004-1:eq:2}
\end{align}
$$

    である．

    

<figure id="2004-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2004/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 三角形$P_n P_{n+1} P_{n+2}$の様子．</figcaption>
</figure>

    次に(b)及び(c)から, $\triangle P_n P_{n+1} P_{n+2}$ は[図2](#2004-1:fig:2)のようになって，
    $\overline{P_{n+1} P_{n+2}}$ を2通りで表して
    
$$
\begin{align*}
& \overline{P_{n+1} P_{n+2}} = 2\overline{P_{n} P_{n+1}}\cos\theta\\\therefore& r^{n+1} = 2r^n \cos\theta
\end{align*}
$$

    である．$r \neq 0$ より
    
$$
\begin{align*}
r = 2 \cos\theta
\end{align*}
$$

    である．

### (2)

    [図2](#2004-1:fig:2)から$P_n P_{n+1}$ から $P_{n+1} P_{n+2}$ へは常に一定の角度だけ回転している．
    よって$\theta_n$ は以下のいずれか一方をみたす．
    
$$
\begin{align*}
\begin{dcases}
            \theta_{n+1} = \theta_n + (\pi - \theta) \\
            \theta_{n+1} = \theta_n + (\pi + \theta)
        \end{dcases}\label{2004-1:eq:3}
\end{align*}
$$

    また，初期条件は$\theta_0 = 0$ だから
    
$$
\begin{align}
\theta_n & = n(\pi\pm\theta)
\end{align}
$$

    である．

### (1)
の結果および$\eqref{2004-1:eq:1}$から
    
$$
\begin{align*}
\begin{aligned}
            \alpha_n
             & = r^n e(n\pi \pm n\theta)                 \\
             & = r^n \{e(\pi \pm \theta)\}^n             \\
             & = (2\cos\theta)^n \{e(\pi \pm \theta)\}^n
        \end{aligned}
\end{align*}
$$

    である．

    したがって$P_n$の表す点の複素数 $Z_n$ として
    
$$
\begin{align*}
Z_n
         & = \sum_{k=0}^{n-1}\alpha_k                                                                              \\& = \frac{1 - r^n \{e(\pi\pm \theta)\}^n}{1 - r e(\pi\pm \theta)}\\& = \frac{1 - (2\cos\theta)^n (\pm\cos\theta+i\sin\theta)^n}{1 \pm 2\cos\theta(\pm\cos\theta+i\sin\theta)}
\end{align*}
$$

    である．$\cdots$(答)

### (3)

### (2)
より$Z_n$が収束する必要十分条件は
    
$$
\begin{align*}
& |2\cos\theta| < 1                       \\\therefore& \frac{\pi}{3} < \theta < \frac{2\pi}{3}
\end{align*}
$$

    である．$\cdots$(答)

### (4)

### (3)
の条件のもとで，(2)の$Z_n$の極限値は
    
$$
\begin{align*}
Z_n
         & \xrightarrow{n \to \infty}\frac{1}{1+2\cos^2\theta \mp 2i\sin\theta\cos\theta}\\& = \frac{1+2\cos^2\theta \pm 2i\sin\theta\cos\theta}{(1+2\cos^2\theta)^2 + (2\sin\theta\cos\theta)^2}
\end{align*}
$$

    だから，実部が$\alpha(\theta)$，虚部が$\beta(\theta)$であって
    
$$
\begin{align*}
\alpha(\theta)
         & = \frac{\cos2\theta+2}{(\cos2\theta+2)^2 + \sin^2 2\theta}\\& = \frac{2+\cos2\theta}{5+4\cos2\theta}\\\beta(\theta)
         & = \frac{\pm \sin2\theta}{(\cos2\theta+2)^2 + \sin^2 2\theta}\\& = \frac{\pm \sin2\theta}{5+4\cos2\theta}
\end{align*}
$$

    と書ける．
    $\theta\to\frac{\pi}{3}+0$での極限は
    
$$
\begin{align*}
\begin{dcases}
            \lim_{\theta\to\frac{\pi}{3}+0} \alpha(\theta) =  \frac{1}{2} \\
            \lim_{\theta\to\frac{\pi}{3}+0} \beta(\theta)  =   \pm\frac{\sqrt{3}}{6}
        \end{dcases}
\end{align*}
$$

    である．$\cdots$(答)

### (5)

    $\frac{\pi}{3} < \theta < \frac{\pi}{2}$の範囲では$\beta(\theta)$の複合正は正の値をとり，複合負は負の値を取る．
    従って，$\beta(\theta)$が最大になるのは複合正の方である．
    そこでこれを$\beta_{+}(\theta)$と置く．
    
$$
\begin{align*}
\beta_{+}(\theta)
         & = \frac{\sin2\theta}{5+4\cos2\theta}\\& = \frac{1}{4}\frac{\sin2\theta}{\frac{5}{4}+\cos2\theta}
\end{align*}
$$

    である．
    この後半の分数は，単位円上の点 $(\cos 2\theta, \sin 2\theta)\, \left(\frac{2}{3}\pi < 2\theta < \pi\right)$
    と 点 $\left(-\frac{5}{4}, 0\right)$ との傾きを表すから，図より
    
$$
\begin{align*}
0 < k \le\frac{4}{3}
\end{align*}
$$

    である．右側の等号成立の条件は図で直線$l$と円が接する時である．

    

<figure id="2004-1:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2004/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 単位円上の点 $(\cos 2\theta, \sin 2\theta)\, \left(\frac{2}{3}\pi < 2\theta < \pi\right)$と点 $\left(-\frac{5}{4}, 0\right)$ との傾き</figcaption>
</figure>

    

<figure id="2004-1:fig:5">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2004/1/fig_4.svg" alt="図 4" />
  <figcaption>図 4: 単位円上の点 $(\cos 2\theta, \sin 2\theta)\, \left(\frac{2}{3}\pi < 2\theta < \pi\right)$と点 $\left(-\frac{5}{4}, 0\right)$ との傾きが最大となる時の様子．</figcaption>
</figure>

    従って，
    
$$
\begin{align*}
0 < \beta_{+}(\theta) \le\frac{1}{3}
\end{align*}
$$

    である．よって最大値は
    
$$
\begin{align*}
\max\beta(\theta) = \frac{1}{3}
\end{align*}
$$

    である．

    

## 【解説】