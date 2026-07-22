---
university: "utokyo"
category: "kouki"
year: "1991"
question: "2"
type: "solution"
title: "UTOKYO 1991 kouki Q2 (solution)"
---

## 【解】

  (1)
  xy平面で考える．
  

$$
\begin{align*}
& C_1: x^2+y^2=1                                      \\& C_2: (x-a)^2+y^2=r_1^2              & a> 0, r_1 > 0 \\& C_3: (x-\alpha)^2+(y-\beta)^2=r_2^2 & r_2 >0
\end{align*}
$$

  とおいて一般性を失わない．$k=1,2,3$に対して$C_k$の中心を$O_k$と置く．
  $y>0$にある$C_1$と$C_2$の交点をA，$y<0$にあるものをBとおく．

  $C_1, C_2$が2交点を持つので
  

$$
\begin{align*}
-1 < a-r_1 < 1
\end{align*}
$$

  である．

  

<figure id="1991-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1991/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円$C_1,C_2$の様子．</figcaption>
</figure>

  

<figure id="1991-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1991/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 円$C_3$の様子．</figcaption>
</figure>

  A，$O_3$から$x$軸に下ろした垂線の足をH$(h,0)$，R$(\alpha,0)$とすると，題意を示すには
  

$$
\begin{align*}
& H=R & \therefore h = \alpha
\end{align*}
$$

  を示せば良い．

  $C_1$と$C_3$, $C_2$と$C_3$の交点の1つをP，Qとする．
  題意より三角形$O_1PO_3$と$O_2QO_3$は直角三角形であり，三平方の定理から
  

$$
\begin{align}
& \begin{dcases}
         |PO_1|^2 + |PO_3|^2 = |O_1O_3|^2 \\
         |QO_2|^2 + |QO_3|^2 = |O_2O_3|^2
       \end{dcases}\\\therefore& \begin{dcases}
         1 + r_2^2     = |O_1O_3|^2 \\
         r_1^2 + r_2^2 = |O_2O_3|^2
       \end{dcases}\label{1991-2:eq:1}
\end{align}
$$

  である．

  点$R$の情報について，同様に直角三角形$O_1RO_3$，$O_2RO_3$にも三平方の定理を用いて
  

$$
\begin{align*}
& \begin{dcases}
         |O_1R|^2 + |RO_3|^2 = |O_1O_3|^2 \\
         |O_2R|^2 + |RO_3|^2 = |O_2O_3|^2
       \end{dcases}
\end{align*}
$$

  である．[(式1)](#1991-2:eq:1)を代入して右辺を書き直すと
  

$$
\begin{align*}
\begin{dcases}
      \alpha^2     + \beta^2 =  1 + r_2^2 \\
      |a-\alpha|^2 + \beta^2 = r_1^2 + r_2^2
    \end{dcases}
\end{align*}
$$

  二つの式を引いて
  

$$
\begin{align}
2a\alpha -a ^2 = 1 - r_1^2 \\\therefore\alpha = \frac{1+a^2-r_1^2}{2a}\label{1991-2:eq:2}
\end{align}
$$

  を得る．

  一方で，点$H$については直角三角形$O_1HA$，$O_2HA$にも三平方の定理を用いて
  

$$
\begin{align*}
& \begin{dcases}
         |O_1H|^2 + |HA|^2 = |O_1A|^2 \\
         |O_2H|^2 + |HA|^2 = |O_2A|^2
       \end{dcases}\\& \begin{dcases}
         h^2 + |RA|^2 = 1 \\
         |a-h|^2 + |RA|^2 = r_1^2
       \end{dcases}\\
\end{align*}
$$

  二つの式を引いて
  

$$
\begin{align}
2a h -a^2 = 1 -r_1^2 \\\therefore
    h = \frac{1+a^2-r_1^2}{2a}\label{1991-2:eq:3}
\end{align}
$$

  である．

  以上[(式3)](#1991-2:eq:2,1991-2:eq:3)から$\alpha=h$すなわち$R=H$だから，
  題意は示され，$C_3$の中心は直線AB上に存在する．$\cdots$(答)
  

  (2)
  $C_1, C_2$のx軸に関する対称性から$C_3$の中心が$y \ge 0$にあるとして良い．
  よって$\beta \ge 0$とする．

  新しく，$\angle AO_1R=\theta\, (0 <\theta < \pi/2)$とおくと，(1)より$R=H$であること[(式1)](#1991-2:eq:1)より
  

$$
\begin{align*}
\alpha& = |O_1A|\cos\theta = \cos\theta\\\beta& = \sqrt{|O_1O_3|^2 - |O_1R|^2}\\& = \sqrt{1 + r_2^2 - \cos^2\theta}\\& = \sqrt{r_2^2 + \sin^2\theta}
\end{align*}
$$

  である．

  また点A，Bの座標は
  

$$
\begin{align*}
& A(\cos\theta,\sin\theta)  \\& B(\cos\theta,-\sin\theta)
\end{align*}
$$

  である．

  ここで，円$C_3$の方程式は
  

$$
\begin{align*}
& f(x,y) = (x-\alpha)^2+(y-\beta)^2 - r_2^2 = 0                              \\\therefore& f(x,y) = (x-\cos\theta)^2 + (y - \sqrt{r_2^2 + \sin^2\theta})^2 -r_2^2 = 0
\end{align*}
$$

  とおける．
  点$(X,Y)$について$f(X,Y)>0$ならばこの点は$C_3$の外側，
  $f(X,Y)<0$ならば$C_3$の内側になる．

  実際に点A，Bの座標を代入すると
  

$$
\begin{align*}
f(A)
     & = f(\cos\theta,\sin\theta)                                         \\& = (\sin\theta - \sqrt{r_2^2 + \sin^2\theta})^2 - r_2^2             \\& = 2\sin^2\theta - 2\sin\theta\sqrt{r_2^2 + \sin^2\theta}\\& = 2\sin\theta\left(\sin\theta - \sqrt{r_2^2 + \sin^2\theta}\right)\\& < 0                                                                \\
    f(B)
     & = f(\cos\theta,-\sin\theta)                                        \\& = \left(-\sin\theta - \sqrt{r_2^2 + \sin^2\theta}\right)^2 - r_2^2 \\& = 2\sin^2\theta + 2\sin\theta\sqrt{r_2^2 + \sin^2\theta}\\& = 2\sin\theta\left(\sin\theta + \sqrt{r_2^2 + \sin^2\theta}\right)\\& > 0
\end{align*}
$$

  だから，確かに点Aは円$C_3$の内側にあり，Bは円$C_3$の外側にある．
  よって題意は示された．$\cdots$(答)

  

  

## 【解説】