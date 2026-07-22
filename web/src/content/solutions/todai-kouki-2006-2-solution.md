---
university: "todai"
category: "kouki"
year: "2006"
question: "2"
type: "solution"
title: "TODAI 2006 kouki Q2 (solution)"
---

## 【解】

  (1)

  

<figure id="2006-2:fig:0">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2006/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 題意の線分</figcaption>
</figure>

  

<figure id="2006-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2006/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 題意の円錐面$S$</figcaption>
</figure>

  まずは$S$の方程式を求める．
  原点$O(0,0,0)$，$A(a,0,0)$，$S$上の点$P(X,Y,Z)$，Pの$x$軸への射影$P'(X,0,0)$とする．
  題意の条件から，$\vec{AP}$と$x$軸のなす角が$\theta$である．
  従って
  

$$
\begin{align*}
\tan\theta& = \frac{|\vec{AP'}|}{|\vec{P'P}|}\\& = \frac{(X-a)}{\sqrt{Y^2+Z^2}}
\end{align*}
$$

  を得る．$X-a>0$だから両辺 2乗して整理すると
  

$$
\begin{align}
& Y^2+Z^2 = (X-a)^2\tan^2\theta& (a<X)  \label{2006-2:eq:1}
\end{align}
$$

  なる円錐側面の方程式を得る．

  従って，この図形$S$を$y$軸周りに一回転してできる立体の体積を求めれば良い．
  図形の対称性から，$S$のうち$0\le y$の部分を$y$軸周りに回転してできる立体の体積$V'$とすると
  

$$
\begin{align}
V = 2V' \label{2006-2:eq:2}
\end{align}
$$

  である．
  そこで$y=t\, (0 \le t \le \sin\theta)$における切断面を考えると
  [(式1)](#2006-2:eq:1)に$Y=t$を代入して
  

$$
\begin{align}
& \tan^2\theta(X-a)^2-Z^2 = t^2 & (a<X)
\end{align}
$$

  を得る．これは双曲線の方程式であり，図示すると[図3](#2006-2:fig:1)となる．

  

<figure id="2006-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2006/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $y=t$における立体の断面</figcaption>
</figure>

  

<figure id="2006-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2006/2/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $y=t$における回転体の面積</figcaption>
</figure>

  この図形は$x$軸に関して対称である．また，図形の端点を
  

$$
\begin{align*}
& A(a+\cos\theta,t, \sqrt{\sin^2\theta-t^2}) \\& B(a+\frac{\cos\theta |t|}{\sin\theta},t,0)
\end{align*}
$$

  とおくと，この図形を$y$軸周りに回転した図形は，外側を半径$|OA|$，内側を半径$|OB|$とする二つの円で囲まれば部分である．
  この面積$f(t)$とすると
  

$$
\begin{align*}
f(t)
     & = \pi\left(|OA|^2-|OB|^2\right)\\& = \pi\left\{(a+\cos\theta)^2+(\sin^2\theta-t^2) - (a+\frac{\cos\theta |t|}{\sin\theta})^2\right\}\\& = \pi\left\{ -\left(1+\frac{\cos^2\theta}{\sin^2\theta}\right)t^2 - 2a\frac{\cos\theta}{\sin\theta}t + \cos^2\theta + \sin^2\theta +2a\cos\theta\right\}
\end{align*}
$$

  となる．$\sin^2\theta+\cos^2\theta=1$を利用してさらに整理すると
  

$$
\begin{align*}
f(t)
     & = \pi\left\{\frac{-1}{\sin^2\theta}t^2 -  2a\frac{\cos\theta}{\sin\theta}t + 1 + 2a\cos\theta\right\}
\end{align*}
$$

  となる．

  従って，$V'$は
  

$$
\begin{align*}
V'
     & = \pi\int_0^{\sin\theta} f(t) dt                                                                                      \\& = \pi\left[ -\frac{1}{3\sin^2\theta}t^3 - a\frac{\cos\theta}{\sin\theta}t^2 + (1+2a\cos\theta)t \right]_0^{\sin\theta}\\& = \pi\left(\frac{2}{3}\sintheta + a\cos\theta\sin\theta\right)
\end{align*}
$$

  となり，[(式2)](#2006-2:eq:2)に代入して
  

$$
\begin{align}
V = 2\pi\left(\frac{2}{3}\sintheta + a\cos\theta\sin\theta\right)\label{2006-2:eq:3}
\end{align}
$$

  を得る．$\cdots$(答)
  

  (2)
  $a=4$を[(式3)](#2006-2:eq:3)に代入して，これを$f(\theta)$とおくと
  

$$
\begin{align*}
f(\theta)
     & = 2\pi(4\cos\theta\sin\theta+\frac{2}{3}\sin\theta) \\& = \frac{4}{3}\pi(6\cos\theta+1)\sin\theta
\end{align*}
$$

  だから，一階微分は変形すると$\cos\theta$のみでかけて，
  

$$
\begin{align*}
f'(\theta)
     & = \frac{4}{3}\pi(6\cos^2\theta - 6\sin^2\theta + \cos\theta)         \\& = \frac{4}{3}\pi(12\cos^2\theta+\cos\theta-6)                         \\& = \frac{4}{3}\pi\left(3\cos\theta-2\right)\left(4\cos\theta+3\right)
\end{align*}
$$

  となる．従って，$0 \le \theta_0 \le \frac{\pi}{2}$の範囲で
  

$$
\begin{align*}
\cos\theta_0 = \frac{2}{3}
\end{align*}
$$

  を満たすような$\theta_0$を用いて，$f(\theta)$の増減表は[表1](#2006-2:table:1)となる．
  

<figure id="2006-2:table:1" class="table-wrapper">

|   $\theta$   | $0$ |              | $\theta_0$ |              | $\pi/2$ |
|:--------------:|:-----:|:------------:|:------------:|:------------:|:---------:|
| $\cos\theta$ | $1$ |              |   $2/3$    |              |   $0$   |
|     $f'$     |       |    $+$     |    $0$     |    $-$     |           |
|     $f$      |       | $\nearrow$ |              | $\searrow$ |           |

  <figcaption>表 1: $f(\theta)$の増減表</figcaption>
</figure>

  したがって$f(\theta)$が最大値を取るのは$\theta=\theta_0$の時で，この時
  

$$
\begin{align*}
\max V
     & = f(\theta_0)                                             \\& = \frac{4}{3}\pi(6\cos\theta_0+1)\sin\theta_0            \\& = \frac{4}{3}\pi(6\cos\theta_0+1)\sqrt{1-\cos^2\theta_0}\\& =\frac{20\sqrt{5}\pi}{3}
\end{align*}
$$

  である．$\cdots$(答)
  

  

## 【解説】

  解答中では律儀に円錐の方程式を求めたが，実際にはここまでしなくても良いだろうと思う．
  $y=t$の切断面の概形がわかっていれば，回転した時の面積は$\pi(|OA|^2-|OB|^2)$と図から判断が着くのでその程度の記述でも大丈夫だと思われる．
  この場合，$A$および$B$の座標は幾何学的あるいは座標計算から求まるため，わざわざ円錐の方程式は不要，というわけだ．

  また，円錐側面の方程式は，以下のような導出の方が簡単だろう．
  すなわち，$S$の方程式は$x=a+k$と固定した時，半径$k \tan \theta$の円が現れるから，
  

$$
\begin{align*}
y^2+z^2 = (x-a)^2\tan^2\theta
\end{align*}
$$

  となる．