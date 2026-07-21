---
university: "kyodai"
category: "kouki"
year: "2001"
question: "3"
type: "solution"
title: "KYODAI 2001 kouki Q3 (solution)"
---

## 【解】

  （1）
  複素数$z$の表す点を$Z$と大文字で書いて区別する．
  座標原点を$O$とする．

  また，表記の簡潔さのため
  
$$
\begin{align}
e(x)   & = \cos x + i\sin x                   \\\theta& = \frac{2\pi}{5}\label{2001-3:eq:1}
\end{align}
$$

  とおく．$e(x)$は
  
$$
\begin{align*}
e(x+y) = e(x)e(y)
\end{align*}
$$

  が成り立つことに注意する．
  題意の$\alpha$は
  
$$
\begin{align*}
\alpha = e\left(\theta\right)
\end{align*}
$$

  である．
  題意の正五角形の頂点の座標は$\alpha^{k}\, (k=0,1,2,3,4)$である．
  これらの点を$A_k$とおく．
  すると，題意の点$Z$は直線 $A_1A_2$ と $A_0A_4$ の交点であり，
  概形は[図1](#2001-3:fig:1)のようになる．

  

<figure id="2001-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2001/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 正五角形と$Z$の関係</figcaption>
</figure>

  

<figure id="2001-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2001/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 三角形$ZA_0A_2$と$A_0A_1A_2$の相似関係</figcaption>
</figure>

  ここで，三角形$A_0A_1Z$は$A_0A_1A_2$と相似で，後者が$|A_1A_0|=|A_1A_2|$の二等辺三角形だから前者も二等辺三角形であり，
  
$$
\begin{align*}
|A_0A_2|         & = |A_0Z|                      \\\angle A_0A_1A_2 & = \angle ZA_0A_2 = \pi-\theta
\end{align*}
$$

  であり，よって$Z$は$A_2$を$A_0$を中心として$-\pi + \theta$回転したもので
  
$$
\begin{align}
z-1
      & = e\left(-\pi + \theta\right)(\alpha^2-1) \\& = e(-\pi)e\left(\theta\right)(\alpha^2-1) \\& = -\alpha(\alpha^2-1)                     \\\therefore
    z & = -\alpha^3+\alpha+1  \label{2001-3:eq:2}
\end{align}
$$

  である．  $\cdots$(答)

### (2)

  題意の円$C$は，要するに三角形$ZA_0A_2$の外接円である．
  三角形$ZA_0A_2$が$|ZA_0|=|A_0A_2|$の二等辺三角形であることから
  $C$の中心$B$は線分 $ZA_2$ の 2 等分線上にある．

  

<figure id="2001-3:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2001/3/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 円$C$の中心$B$と，$A_0,A_2,Z$の関係．</figcaption>
</figure>

  次に，三角形$OA_0A_2$が二等辺三角形であることと，
  $B$が$C$の中心ゆえ$|BA_2|=|BA_0|$であることから，
  線分$OB$は$A_0A_2$と直交する二等分線である．これらの交点を$H$とおく．

  題意の条件，点$O$も$C$上にあることを示すには
  
$$
\begin{align*}
|BO| = |BA_0|
\end{align*}
$$

  を示せば良い．
  すなわち，三角形$OA_0B$が$|BO| = |BA_0|$の二等辺三角形であることを示せば良い．

  まず，$\angle BOA_0$について，線分$OA_1$も線分$A_0A_1$の二等分線だから
  直線$OA_1$と直線$OB$は等しく
  
$$
\begin{align*}
\angle BOA_0
     & = \angle BOA_1 \\& = \theta
\end{align*}
$$

  である．

  次に$\angle BA_0O$について，
  
$$
\begin{align*}
\angle BA_0O
     & = \angle OA_0A_2 + \angle A_2A_0B              \\& = \angle OA_0A_2 + \frac{\angle A_2A_0Z}{2}\\& = \frac{\pi-2\theta}{2} + \frac{\pi-\theta}{2}\\& = \pi-\frac{3\theta}{2}\\& = \frac{2\pi}{5}\\& = \theta
\end{align*}
$$

  である．

  以上から$\angle BOA_0=\angle BA_0O$であり，従って
  
$$
\begin{align*}
|BO| = |BA_0|
\end{align*}
$$

  となり，$O$も確かに円$C_1$上にあるから題意は示された．$\cdots$(答)

  
  

## 【解説】

### (1)
は導出によって，いくつか見た目の異なる表現が得られる．
  その一つが
  
$$
\begin{align*}
z = \frac{\alpha(\alpha+1)}{\alpha^2+1}
\end{align*}
$$

  である．これは$Z$ を $A_0$ のまわりに $\frac{2}{5}\pi$ だけ回転し，$A_0$ からの距離を $\frac{A_1A_0}{A_0Z}$ 倍したものが $A_1$ である．
  として立式したときにこの形になる．
  解答の表現と同一の値を与えることは以下のように確認できる．
  
$$
\begin{align*}
(-\alpha^3+\alpha+1)(\alpha^2+1)
     & = -\alpha^5+\alpha^3+\alpha^2-\alpha^3+\alpha+1 \\& = -1 +\alpha^2+\alpha+1                         \\& = \alpha(\alpha+1)
\end{align*}
$$

  より，この両辺を$\alpha^2+1$で割れば良い．
  ただし，二行目で$\alpha^5=1$を利用した．

### (2)
はより複素数チックに解く方法として，
  円周角の定理を用いて$\angle A_2OZ=\angle A_2A_0Z$を示す方針でも良い．
  以下これを示そう．
  そこで
  
$$
\begin{align*}
& \angle A_2OZ  = \theta_1  \\& \angle A_2A_0Z = \theta_2
\end{align*}
$$

  とおく．

  

<figure id="2001-3:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2001/3/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $\angle ZA_0A_2$と$\angle ZOA_2$の様子．</figcaption>
</figure>

  まず$\theta_1$は
  
$$
\begin{align*}
\theta_1
     & = \arg\frac{\alpha^2}{z}\\& = 2\arg\alpha - \arg z
\end{align*}
$$

  である．ここで$A_3,O,Z$がこの順で同一直線上にあることから
  
$$
\begin{align*}
\arg z
     & = \arg\alpha^3 - \pi\\& = 3\arg\alpha - \pi
\end{align*}
$$

  であるから，
  
$$
\begin{align*}
\theta_1
     & = 2 \arg\alpha - (3\arg\alpha - \pi) \\& = \pi - \arg\alpha
\end{align*}
$$

  ここで$\eqref{2001-3:eq:1}$より$\arg\alpha=2\pi/5$だから，
  
$$
\begin{align*}
\theta_1 = \frac{3\pi}{5}
\end{align*}
$$

  である．

  次に$\theta_2$は
  
$$
\begin{align*}
\theta_2
     & =\arg\frac{\alpha^2-1}{z-1}\\& =\arg\frac{\alpha^2-1}{-\alpha^3+\alpha}\\& =\arg\frac{\alpha^2-1}{\alpha(-\alpha^2+1)}\\& =\arg\frac{\alpha^2-1}{\alpha(-\alpha^2+1)}\\& =\arg\frac{1}{-\alpha}\\& =2\pi-\arg(-\alpha)                         \\& =2\pi-(\arg(-1)+\arg\alpha)                 \\& =\pi-\arg\alpha\\& = \frac{3\pi}{5}
\end{align*}
$$

  となり，よって$\theta_1=\theta_2$であり題意は示された．