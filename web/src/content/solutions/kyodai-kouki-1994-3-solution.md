---
university: "kyodai"
category: "kouki"
year: "1994"
question: "3"
type: "solution"
title: "KYODAI 1994 kouki Q3 (solution)"
---

## 【解】

  

<figure id="1994-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1994/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円Cと点PRの様子</figcaption>
</figure>

  

<figure id="1994-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1994/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 円Cと点PQの様子．線分PQが円の下側に来る場合．</figcaption>
</figure>

  題意の円の方程式は
  
$$
\begin{align*}
C:(x-1)^2+(y-1)^2=1
\end{align*}
$$

  である．
  また，題意の点PとQの座標を，$0<X,Y$として
  P$(X,0)$ Q$(0,Y)$とおく.
  すると，直線PQの方程式は
  
$$
\begin{align*}
\frac{x}{X} + \frac{y}{Y} = 1
\end{align*}
$$

  である．
  この直線PQが円Cの接線である時，直線PQとCの中心$(1,1)$の距離が$1$だから，
  点と直線の距離公式より
  
$$
\begin{align*}
\frac{|X+Y-XY|}{\sqrt{X^2+Y^2}} = 1
\end{align*}
$$

  両辺$0$以上だから$2$乗して
  
$$
\begin{align*}
& (X+Y-XY)^2 = X^2+Y^2                     \\\therefore& X^2+Y^2+X^2Y^2+2XY-2X^2Y-2XY^2 = X^2+Y^2 \\\therefore& X^2Y^2+2XY-2X^2Y-2XY^2 = 0
\end{align*}
$$

  $XY \ne 0$だから両辺$XY$で割ってよく，
  
$$
\begin{align}
XY+2-2X-2Y=0 \label{1994-3:eq:1}
\end{align}
$$

  を得る．

  

<figure id="1994-3:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1994/3/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 円Cと三角形PQRの様子．点Rが線分PQの上側にある場合のみ，Rが第一象限に存在する．</figcaption>
</figure>

  次に，点Rの座標を$X,Y$を用いて表す．
  線分PQの中点をMとすると，ベクトルMRはベクトルPQと直交して，長さは
  
$$
\begin{align*}
MR = \frac{\sqrt{3}}{2}PQ
\end{align*}
$$

  を満たすから，ベクトルPQの方向ベクトルが$(X,-Y)$と書けることより
  
$$
\begin{align*}
\vec{OR}& = \vec{OM} + \vec{MR}\\& = \frac{1}{2}\mqty(X  \\Y) \pm\frac{\sqrt{3}}{2}\mqty(Y \\ X) \\
\end{align*}
$$

  と書ける．従って，題意より点Rの座標が$(a,b)$であることから
  
$$
\begin{align}
\begin{dcases}
      a = \frac{1}{2}(X \pm \sqrt{3}Y) \\
      b = \frac{1}{2}(Y \pm \sqrt{3}X)
    \end{dcases}\quad\text{(複号同順)}\label{1994-3:eq:2}
\end{align}
$$

  となる．
  ここで，題意より点Rが第一象限にあることより$a,b>0$だから
  
$$
\begin{align*}
& \begin{dcases}
         X \pm \sqrt{3}Y > 0 \\
         Y \pm \sqrt{3}X > 0
       \end{dcases}\\\therefore& \begin{dcases}
         X > \mp \sqrt{3}Y \\
         Y > \mp \sqrt{3}X
       \end{dcases}
\end{align*}
$$

  であるが，複号負の時，
  
$$
\begin{align*}
& Y > \sqrt{3}X > \sqrt{3}\cdot\sqrt{3}Y \\\therefore& Y > 3Y
\end{align*}
$$

  となるが，これを満たす$X,Y>0$は存在しないから，
  取りうるのは複号正のみである．
  従って$\eqref{1994-3:eq:2}$で複号正をとって
  
$$
\begin{align}
\begin{dcases}
      a = \frac{1}{2}(X + \sqrt{3}Y) \\
      b = \frac{1}{2}(Y + \sqrt{3}X)
    \end{dcases}\label{1994-3:eq:3}
\end{align}
$$

  となる．逆にこの時，$X,Y>0$から自動的に$a,b>0$も満たされる．

  よって，以下$\eqref{1994-3:eq:1}$および$X,Y>0$のもとで$\eqref{1994-3:eq:3}$の満たす関係を調べれば良い．
  $\eqref{1994-3:eq:3}$を逆に解いて
  
$$
\begin{align*}
\begin{dcases}
      X = -a+\sqrt{3}b \\
      Y = \sqrt{3}a-b
    \end{dcases}
\end{align*}
$$

  だから，これを$\eqref{1994-3:eq:1}$および$X,Y>0$に代入して
  
$$
\begin{align*}
& \begin{dcases}
         \left(-a+\sqrt{3}b\right)\left(\sqrt{3}a-b\right) +2-2\left(-a+\sqrt{3}b+\sqrt{3}a-b\right)=0 \\
         -a+\sqrt{3}b > 0                                                                              \\
         \sqrt{3}a-b > 0
       \end{dcases}\\\therefore& \begin{dcases}
         \sqrt{3}(a^2+b^2)-4ab-2+2(1-\sqrt{3})(a-b) = 0 \\
         \sqrt{3}b > a                                  \\
         \sqrt{3}a > b
       \end{dcases}
\end{align*}
$$

  が求める関係式である．$\cdots$(答)

  
  

## 【解説】