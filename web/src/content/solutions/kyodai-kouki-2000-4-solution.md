---
university: "kyodai"
category: "kouki"
year: "2000"
question: "4"
type: "solution"
title: "KYODAI 2000 kouki Q4 (solution)"
---

## 【解】

### (1)

  $C'$を原点とする座標空間で考える．
  四角形A'B'C'D'を$z=0$の平面上に配置して，
  A'$(\sqrt{2},1,0)$，B'$(\sqrt{2},0,0)$，C'$(0,0,0)$，D'$(0,1,0)$とする．
  四角形ABCDを$z=1$平面に配置して，
  A$(\sqrt{2},1,1)$，B$(\sqrt{2},0,1)$，C$(0,0,1)$，D$(0,1,1)$とする．

  

<figure id="2000-4:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2000/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 直方体ABCD-A'B'C'D'を座標空間に置いた様子．</figcaption>
</figure>

  題意の直線AC'に垂直で，AC'上の点Pを通る切断面を$\pi(P)$とおく．
  $\pi(P)$の法線ベクトル$n$はACと平行で
  
$$
\begin{align*}
n \parallel\vec{\text{C'A}}\parallel\begin{pmatrix}\sqrt{2}\\ 1 \\ 1 \end{pmatrix}
\end{align*}
$$

  を満たす．

  線分$AP$の長さを$t\, (0\le t\le 2)$と置くと，
  Pの座標は$P(\frac{\sqrt{2}t}{2},\frac{t}{2},\frac{t}{2})$である．

  以上から，$\pi(P)$の方程式は
  
$$
\begin{align}
& \sqrt{2}\left(x - \frac{\sqrt{2}t}{2}\right) + \left(y - \frac{t}{2}\right) + \left(z - \frac{t}{2}\right) = 0 \\\therefore& \sqrt{2}x + y + z - 2t = 0 \label{2000-4:eq:1}
\end{align}
$$

  である．

  さて，題意のように点PがAC'の中点である時，APの長さは
  
$$
\begin{align*}
|AP|
     & = \frac{1}{2}|AC'| \\& = 1
\end{align*}
$$

  だから，$t=1$を$\eqref{2000-4:eq:1}$に代入すると
  
$$
\begin{align*}
\pi(t=1): \sqrt{2}x + y + z - 2 = 0
\end{align*}
$$

  となり，この方程式は
  B'$(\sqrt{2},0,0)$, D$(0,1,1)$を通る．
  以上から題意は示された．$\cdots$(答)

### (2)

### (1)
と同様に各頂点が$\pi$(P)を通る時以下の方になる．

  従って，切り口の形状は
  
$$
\begin{align*}
\begin{dcases}
      0 \le t \le \frac{1}{2} \\
      \frac{1}{2} \le t \le 1 \\
      1 \le t \le \frac{3}{2} \\
      \frac{3}{2} \le t \le 2 \\
    \end{dcases}
\end{align*}
$$

  の四つの場合わけで記述できる．
  対称性から，前者二つを考えれば後者二つは$t\to 2-t$の置換で求まる．

  
  \textbf{$1^{\circ} \ 0 \le t \le \frac{1}{2}$ の時}

  

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2000/4/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $\ 0 \le t \le \frac{1}{2}$の時の切断面は三角形になる．</figcaption>
</figure>

  $\pi$(P)は辺C'B'，C'D'，CC'，と交わるから，各々の交点をX, Y, Zとする．
  すると切断面の面積は$\triangle XYZ$の面積に等しい．
  
$$
\begin{align*}
S(t) = (\triangle\text{XYZ}\text{の面積})
\end{align*}
$$

  である．
  $\eqref{2000-4:eq:1}$から，
  
$$
\begin{align*}
& X(\sqrt{2}t,0,0) \\& Y(0,2t,0)        \\& Z(0,0,2t)
\end{align*}
$$

  だから，三角形の面積公式から
  
$$
\begin{align*}
S(t)
     & = \frac{1}{2}\sqrt{|\vec{XY}|^2|\vec{XZ}|^2-(\vec{XY}\cdot\vec{XZ})^2}\\& = \frac{1}{2}\sqrt{(2t^2+4t^2)(2t^2+4t^2)-(2t^2)^2}\\& = \frac{1}{2}\sqrt{32t^4}\\& = 2\sqrt{2}t^2
\end{align*}
$$

  である．
  
  \textbf{$2^\circ \ \frac{1}{2} \le t \le 1$ の時}

  

<figure id="2000-4:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2000/4/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $\ \frac{1}{2} \le t \le 1$の時の切断面は五角形になる．</figcaption>
</figure>

  切り口は[図3](#2000-4:fig:3)のような五角形になる．
  これは，四角形から三角形を切り抜いた形として計算できる．

  

<figure id="2000-4:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2000/4/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $\ \frac{1}{2} \le t \le 1$の時，切断面は四角形から三角形の部分を切り抜くことで計算できる．</figcaption>
</figure>

  四角形の面積は，[図4](#2000-4:fig:4)より$t$によらず$S(1/2)$の2倍である．
  一方切り取る三角形の面積は，$z$座標に注目すると$S(1/2)$の三角形と$1:2(1-t)$の比率だから
  
$$
\begin{align*}
(2-2t)^2S(1/2)
\end{align*}
$$

  となる．また$1^{\circ}$より$S(1/2)=\frac{\sqrt{2}}{2}$である．
  以上より
  
$$
\begin{align*}
S(t)
     & = 2S(1/2) - 4(1-t)^2S(1/2)                  \\& = \frac{\sqrt{2}}{2}\left(2-4(1-t)^2\right)\\& = \sqrt{2}\left(1-2(1-t)^2\right)
\end{align*}
$$

  である．

  
  \textbf{$3^\circ \ 1 \le t \le \frac{3}{2}$ の時}

  対称性から$3^\circ$の$t$を$2-t$でおきかえて
  
$$
\begin{align*}
S(t) = \sqrt{2}\left(1-2(t-1)^2\right)
\end{align*}
$$

  である．これは$3^\circ$の時と同じ表現である．

   
  \textbf{$4^\circ \ \frac{3}{2} \le t \le 2$ の時}

  対称性から1$^\circ$の$t$を$2-t$で置きかえて
  
$$
\begin{align*}
S(t) = 2\sqrt{2}(2-t)^2
\end{align*}
$$

  である．

   
  以上まとめて$t$を$x$でおきかえて
  
$$
\begin{align*}
S(x)
    = \begin{dcases}
        2\sqrt{2}x^2           & (0 \le x \le \frac{1}{2})                      \\
        \sqrt{2}\{1-2(x-1)^2\} & \left(\frac{1}{2} \le x \le \frac{3}{2}\right) \\
        2\sqrt{2}(2-x)^2       & (\frac{3}{2} \le x \le 2)
      \end{dcases}
\end{align*}
$$

  が求める答えである．$\cdots$(答)

  

  受験上の検算テクニックとして，この手の場合わけが生じた場合は境界での値が一致していることを確認したい．