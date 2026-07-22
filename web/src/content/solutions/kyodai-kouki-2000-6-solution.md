---
university: "kyodai"
category: "kouki"
year: "2000"
question: "6"
type: "solution"
title: "KYODAI 2000 kouki Q6 (solution)"
---

## 【解】

  (1)
  $f(x)$の一階微分は
  

$$
\begin{align*}
f'(x) = \frac{1}{1+x^2}
\end{align*}
$$

  である．
  また，$f(x)$の積分は
  

$$
\begin{align*}
& t = \tan\theta& \left( -\frac{\pi}{2} < \theta < \frac{\pi}{2}\right)
\end{align*}
$$

  とおくと，$x=\tan\alpha\, (-\frac{\pi}{2} < \alpha < \frac{\pi}{2})$として
  

$$
\begin{align*}
f(x)
     & = \int_0^\alpha\cos^2\theta\frac{1}{\cos^2\theta} d\theta\\
    = \alpha
\end{align*}
$$

  と表せる．

  $x=1$ より $f'(1)=1/2$および$\alpha = \pi/4$ である．
  従って，法線は傾き$-2$で$(1,\pi/4)$を通る直線だから
  

$$
\begin{align*}
l: y & = -2(x-1) + \pi/4 \\& = -2x + 2 + \pi/4
\end{align*}
$$

  となる．

  
  (2)
  $f'(x) > 0$ より$f(x)$は単調増加であり, グラフの概形は[図1](#2000-6:fig:1)のようになる．

  

<figure id="2000-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2000/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 曲線$y=f(x)$と法線$l$の様子</figcaption>
</figure>

  題意の面積 $S$ のうち,
  $0 \le x \le 1$ のものを $S_1$,
  $1 \le x \le 1+\pi/8$ のものを $S_2$ とおくと，
  

$$
\begin{align}
S = S_1 + S_2 \label{2000-6:eq:1}
\end{align}
$$

  を満たす．以下$S_1$および$S_2$を個別に求める．

  まず，$S_2$は底辺$\pi/8$，高さ$\pi/4$の三角形だから
  

$$
\begin{align}
S_2 = \frac{1}{2}\frac{\pi}{8}\frac{\pi}{4} = \frac{\pi^2}{64}\label{2000-6:eq:2}
\end{align}
$$

  である．

  次に$S_1$は，$f(x)$が$y$軸方向の積分の方が容易なことから，四角形OABCの面積から図形OBCの面積を引けば良い．
  

$$
\begin{align}
S_1 & = \text{四角形} - \int_0^{\pi/4} x dy                      \\& = \pi/4 - \int_0^{\pi/4}\tan\alpha d\alpha\\& = \pi/4 - [-\log(\cos\alpha)]_0^{\pi/4}\\& = \pi/4 + \log\frac{\sqrt{2}}{2}\label{2000-6:eq:3}
\end{align}
$$

  [(式3)](#2000-6:eq:2,2000-6:eq:3)を[(式1)](#2000-6:eq:1)に代入して
  

$$
\begin{align*}
S & = \frac{\pi^2}{64} + \frac{\pi}{4} + \log\frac{\sqrt{2}}{2}
\end{align*}
$$

  が求める答えである．  $\cdots$(答)

  
  

## 【解説】