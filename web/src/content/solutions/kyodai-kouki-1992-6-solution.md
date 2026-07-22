---
university: "kyodai"
category: "kouki"
year: "1992"
question: "6"
type: "solution"
title: "KYODAI 1992 kouki Q6 (solution)"
---

## 【解】

  A$(1,1,1)$, B$(-1,a,0)$, C$(-a,0,1)$, D$(0,1,a)$

### (1)

  題意を示すには，$|AB|=|AD|=|DC|$であることと，$\angle BAD = \angle ACD = \pi/2$であることを示せば良い．
  各辺をなすベクトルは
  
$$
\begin{align*}
\vec{\text{AB}}& = \begin{pmatrix} -\frac{1}{a}-1 \\ a-1 \\ -1\end{pmatrix} \\\vec{\text{AD}}& = \begin{pmatrix} -1             \\ -\frac{1}{a}-1 \\ a-1 \end{pmatrix} \\\vec{\text{DC}}& = \begin{pmatrix}-a              \\\frac{1}{a}\\\frac{1}{a}-a \end{pmatrix}
\end{align*}
$$

  となる．

  まず辺の長さについて，
  
$$
\begin{align*}
|\vec{\text{AB}}|
     & = |\vec{\text{AD}}|                                                   \\& = \sqrt{1+(a-1)^2+\left(-\frac{1}{a}-1\right)^2}\\& = \sqrt{a^2 -2a + 3 + \frac{2}{a} + \frac{1}{a^2}}\\& = \sqrt{\left(a-\frac{1}{a}\right)^2 - 2\left(a-\frac{1}{a}\right)+5}\\
\end{align*}
$$

  であり，
  
$$
\begin{align}
a-\frac{1}{a}& = \frac{1+\sqrt{5}}{2} - \frac{2}{1+\sqrt{5}}\\& = 1 \label{1992-6:eq:1}
\end{align}
$$

  を代入すると
  
$$
\begin{align*}
|\vec{\text{AB}}| = |\vec{\text{AD}}|   = 2
\end{align*}
$$

  である．ついで
  
$$
\begin{align*}
|\vec{\text{DC}}|
     & = \sqrt{a^2+\frac{1}{a^2}+\left(\frac{1}{a}-a\right)^2}\\& = \sqrt{2\left(a-\frac{1}{a}\right)^2+2}\\& = 2
\end{align*}
$$

  だから，
  
$$
\begin{align*}
|\vec{\text{AB}}| = |\vec{\text{AD}}| =|\vec{\text{DC}}| = 2
\end{align*}
$$

  となる．

  次に角度については，ベクトルの内積が$0$になれば良い．
  $\eqref{1992-6:eq:1}$を利用すると，
  
$$
\begin{align*}
\vec{\text{AB}}\cdot\vec{\text{AD}}& = 1+\frac{1}{a} + (a-1)\left(-\frac{1}{a}-1\right) -(a-1)                    \\& = 2\left(\frac{1}{a}-a+1\right)\\& = 0                                                                          \\\vec{\text{AD}}\cdot\vec{\text{DC}}& = a + \frac{1}{a}\left(-\frac{1}{a}-1\right)+(a-1)\left(\frac{1}{a}-a\right)\\& = 2a - \frac{1}{a^2} - \frac{2}{a} +1 -a^2                                   \\& = 2\left(a-\frac{1}{a}\right) - \left(a-\frac{1}{a}\right)^2 -1              \\& = 0
\end{align*}
$$

  より，確かに内積は$0$であり，
  
$$
\begin{align*}
\angle BAD = \angle ACD = \pi/2
\end{align*}
$$

  である．

  以上から，$\text{ABCD}$は一辺の長さ$2$の正方形である．$\cdots$(答)

### (2)

  点OとDは平面$x=0$上にあり，点AとBは平面$x=0$を挟んで両側に存在する．
  そこで，辺ABと平面$x=0$の交点を求める．
  辺ABの方程式は
  
$$
\begin{align*}
\begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}1 \\ 1 \\ 1\end{pmatrix} + t \begin{pmatrix}-1 \\ a-1 \\ -1\end{pmatrix}
\end{align*}
$$

  だから，$x=0$を代入して，交点を表す$t$は
  
$$
\begin{align*}
t
     & = \frac{1}{1/a+1}\\& = \frac{a}{a+1}
\end{align*}
$$

  である．従ってこの交点をEとすると，EはABを
  
$$
\begin{align*}
t: 1-t & = \frac{a}{a+1}: \frac{1}{a+1}
\end{align*}
$$

  に内分する点であり，(1)より$|AB|=2$だから
  
$$
\begin{align*}
|AE| & = \frac{2a}{a+1}\\
    |EB| & = \frac{2}{a+1}
\end{align*}
$$

  である．この様子を[図1](#1992-6:fig:1)に示す．

  

<figure id="1992-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1992/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 四角形ABCDの様子</figcaption>
</figure>

  題意の$W_1, W_2$ は各々 $\triangle \text{ADE}$, $\square \text{EBCD}$を底面とし，
  高さは同じ立体だから体積比は底面積比に等しく，
  求める体積の比は
  
$$
\begin{align*}
W_1:W_2
     & = \triangle\text{ADE} : \triangle\text{EBCD}& = \text{AE} : \text{EB}+\text{CD}\\& = \frac{2a}{a+1} : \frac{2}{a+1}+2             \\& = a : a+2                                      \\& = 1:\sqrt{5}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】