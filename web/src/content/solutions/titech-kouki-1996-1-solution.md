---
university: "titech"
category: "kouki"
year: "1996"
question: "1"
type: "solution"
title: "TITECH 1996 kouki Q1 (solution)"
---

## 【解】

### (1)

  $C$,$C_{\theta}$の中心をそれぞれ$O$,$O_{\theta}$とする．
  [図1](#1996-1:fig:1)に概形を示す．
  題意より，点$P$での接線$OP$と$O'P$が直交し，
  また点$Q$での接線$OQ$と$QO'$が直交する．

  

<figure id="1996-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1996/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円$C$と$C_{\theta}$</figcaption>
</figure>

  したがって，$O'(X,Y)$とおくと,
  
$$
\begin{align}
& \begin{dcases}
         \va*{OP}\cdot \va*{PO'} = 0 \\
         \va*{OQ}\cdot \va*{QO'} = 0
       \end{dcases}\\\therefore& \begin{dcases}
         \begin{pmatrix}1          \\0\end{pmatrix}\cdot \begin{pmatrix}X-1\\Y\end{pmatrix} = 0 \\
         \begin{pmatrix}\cos\theta \\ \sin\theta\end{pmatrix}\cdot \begin{pmatrix}X-\cos\theta\\ \sin\theta\end{pmatrix} = 0
       \end{dcases}\\\therefore& \begin{dcases}
         X=1 \\
         Y = \frac{1-\cos\theta}{\sin\theta} \quad (\because 0 < \theta < \pi) \quad \cdots\text{②}
       \end{dcases}
\end{align}
$$

  である. したがって, $C_{\theta}$の半径$R_{\theta}$は
  
$$
\begin{align}
R_{\theta}& = \mathrm{PO'}\\& = Y                                                 \\& = \frac{1-\cos\theta}{\sin\theta}\\& = \frac{\sin\frac{\theta}{2}}{\cos\frac{\theta}{2}}\\& = \tan\frac{\theta}{2}
\end{align}
$$

  である．ただし，最後の行で倍角公式を利用した．
  したがって，
  
$$
\begin{align*}
\tan\angle POO'
     & = \frac{PO'}{OP}\\& =\tan\frac{\theta}{2}
\end{align*}
$$

  となり，$\angle POO'=\theta/2$であることがわかる．

  

<figure id="1996-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1996/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 円$C$と$C_{\theta}$，および求める共通領域の面積．</figcaption>
</figure>

  求める共通領域の面積$S_\theta$は, 扇形$OPQ$と扇形$O'PQ$の面積の和から，四角形$OPO'Q$を引いたものに等しい．
  $\angle PO'Q=\pi-\theta$に注意して，
  
$$
\begin{align*}
\text{扇形}OPQ    & = \frac{1}{2}\theta\\\text{扇形}O'PQ   & = \frac{1}{2}\left(\pi-\theta\right)\tan^2\frac{\theta}{2}\\\text{四角形}OPO'Q & = 2\triangle OPO'                                          \\& = 2 \frac{1}{2} |OP| |PO'|                                 \\& = \tan\frac{\theta}{2}
\end{align*}
$$

  より，求める面積$S_{\theta}$は
  
$$
\begin{align*}
S_{\theta}& = \text{扇形}OPQ + \text{扇形}O'PQ -\text{四角形}OPO'Q                                                      \\& = \frac{1}{2}\theta + \frac{1}{2}\left(\pi-\theta\right)\tan^2\frac{\theta}{2} -\tan\frac{\theta}{2}
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  線分$OO'$の長さは，倍角公式より
  
$$
\begin{align*}
OO'
     & = \sqrt{1+\frac{(1-\cos\theta)^2}{\sin^2\theta}}\\& = \sqrt{\frac{1+\sin^2\theta + \cos^2\theta -2\cos\theta}{\sin^2\theta}}\\& = \sqrt{\frac{2 -2\cos\theta}{\sin^2\theta}}\\& = \sqrt{\frac{4\sin^2\frac{\theta}{2}}{4\sin^2\frac{\theta}{2}\cos^2\frac{\theta}{2}}}\\& = \sqrt{\frac{4\sin^2\frac{\theta}{2}}{4\sin^2\frac{\theta}{2}\cos^2\frac{\theta}{2}}}\\& = \frac{1}{\cos\frac{\theta}{2}}
\end{align*}
$$

  と表せる．

  

<figure id="1996-1:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1996/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 円$C$と$C_{\theta}$，および$A_{\theta}$の様子．</figcaption>
</figure>

  $A_{\theta}$は線分$OO'$上にあって，線分$OA_{\theta}$の長さは
  
$$
\begin{align*}
OA_{\theta}& = OO' - O'A_{\theta}\\& = OO' - R_{\theta}\\& = \frac{1}{\cos\frac{\theta}{2}} -  \frac{\sin\frac{\theta}{2}}{\cos\frac{\theta}{2}}\\& = \frac{1-\sin\frac{\theta}{2}}{\cos\frac{\theta}{2}}
\end{align*}
$$

  だから，
  
$$
\begin{align*}
\va*{OA_{\theta}}& =  \frac{1-\sin\frac{\theta}{2}}{\cos\frac{\theta}{2}}\begin{pmatrix}\cos\frac{\theta}{2}\\\sin\frac{\theta}{2}\end{pmatrix} \\& \equiv\begin{pmatrix}x                                                                    \\ y\end{pmatrix}
\end{align*}
$$

  とかける．
  
$$
\begin{align}
x & = 1-\sin\frac{\theta}{2}\\
    y & = \frac{\sin\frac{\theta}{2}\left(1-\sin\frac{\theta}{2}\right)}{\cos\frac{\theta}{2}}
\end{align}
$$

  において，$0<\theta<\pi$より，$\cos\theta/2>0$だから，
  
$$
\begin{align}
\cos\frac{\theta}{2} = \sqrt{1-\sin^2\frac{\theta}{2}}
\end{align}
$$

  を代入して
  
$$
\begin{align}
x & = 1-\sin\frac{\theta}{2}\\
    y & = \frac{\sin\frac{\theta}{2}\left(1-\sin\frac{\theta}{2}\right)}{\sqrt{1-\sin^2\frac{\theta}{2}}}
\end{align}
$$

  1つ目の式から$\sin(\theta/2)$を消去して
  
$$
\begin{align*}
& \sin\frac{\theta}{2} = 1-x & (0<x<1)
\end{align*}
$$

  を2つ目の式に代入して
  
$$
\begin{align*}
Y
     & = \frac{(1-x)\cdot x}{\sqrt{1-(1-x)^2}}\\& = \frac{x(1-x)}{\sqrt{2x-x^2}}\quad(0<x<1)
\end{align*}
$$

  がもとめる軌跡である．$\cdots$(答)

### (3)

### (2)
でもとめたグラフは$0<x<1$で$y>0$であり，[図4](#1996-1:fig:3)のようになる．

  

<figure id="1996-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1996/1/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $A_{\theta}$の軌跡．</figcaption>
</figure>

  したがってもとめる体積は
  
$$
\begin{align*}
V
     & = \pi\int_0^1 y^2 dx                                   \\& = \pi\int_0^1 \frac{x^2(1-x)^2}{x(2-x)} dx             \\& = \pi\int_0^1 \left(-x^2 - 1 + \frac{2}{2-x}\right) dx \\& = \pi\left[-\frac{1}{3}x^3 - x - 2\log|2-x|\right]_0^1 \\& = \pi\left(2\log 2 - \frac{4}{3}\right)
\end{align*}
$$

  となる．$\cdots$(答)

  

## 【解説】

  平面図形の問題．
  ポイントは対称性から$\angle POO'=\theta/2$と，直線$OO'$が$\angle POQ$を半分に分割する直線になっていることである．
  本解答では座標からこの事実を導出したが，対称性からこの事実を認めてしまえば，$O'$の座標は直線
  
$$
\begin{align*}
y = \tan\frac{\theta}{2} x
\end{align*}
$$

  と$x=1$の交点であるから$O'=(1,\tan(\theta/2))$と求まる．
  以降の計算も$\theta/2$を用いて行ったほうが見通しが良いため，そのように変形している．