---
university: "sample_titech"
category: "kouki"
year: "1993"
question: "1"
type: "solution"
title: "SAMPLE_TITECH 1993 kouki Q1 (solution)"
---

## 【解】

  [図1](#1993-1:fig:1)のように、一辺の長さが1の立方体の8頂点を定める。回転軸をOEとし、その方向ベクトルを
  
$$
\begin{align*}
\va*{l} =
    \begin{pmatrix}
      1 \\
      1 \\
      1
    \end{pmatrix}
\end{align*}
$$

  とする．
  OE上の点$P_{t} = t\va*{l}$ ($0 \le t \le 1$)を通り，$\va*{l}$に垂直な平面$x+y+z=3t$で立体を切断したときの断面積を考える．
  これをOEを軸に回転させたときの面積を$S(t)$とする．
  最終的に、この$S(t)$を線分OEに沿って積分することで、回転体の体積$V$を求める．
  対称性から，$0\le t\le 1/2$についてのみ考えれば十分である．

  

<figure id="1993-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1993/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 立方体と頂点の定義</figcaption>
</figure>

  まず，断面積$S(t)$の計算を行う．$t$の大きさで場合分けして考える．

  
  \underline{\textbf{$0 \le t \le \frac{1}{3}$ の場合}}

  断面は[図2](#1993-1:fig:2)のように，3点$(3t,0,0), (0,3t,0), (0,0,3t)$を頂点とする正三角形となる．
  回転の軸となる点$P_t(t,t,t)$から最も遠い点はこの三角形の頂点である．
  例えば、点Q$(3t,0,0)$を考えると、回転体の半径の2乗は$\overline{P_t Q}^2$で与えられる．
  
$$
\begin{align*}
\overline{P_t Q}^2
     & = (3t-t)^2 + (0-t)^2 + (0-t)^2 \\& = 6t^2
\end{align*}
$$

  より，この場合の回転断面積$S(t)$は
  
$$
\begin{align}
S(t)
     & = \pi\overline{P_t Q}^2 \nonumber\\& = 6\pi t^2 \label{1993-1:eq:1}
\end{align}
$$

  となる．

  

<figure id="1993-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1993/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 三角形の断面 ($t=1/4$の例)</figcaption>
</figure>

  
  \underline{\textbf{$\frac{1}{3} \le t \le \frac{2}{3}$ の場合}}

  断面は[図3](#1993-1:fig:3)のような六角形となる．
  この六角形の頂点の一つは，例えば辺AB上の点Q$(1, 3t-1, 0)$である．
  

<figure id="1993-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/1993/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 六角形の断面 ($t=1/2$の例)</figcaption>
</figure>

  対称性から点$P_t$と各頂点の距離はいずれも等しく，回転半径は点$P_t(t,t,t)$とこの六角形の頂点との距離で決まる．
  
$$
\begin{align*}
\overline{P_t Q}^2
     & = (1-t)^2 + (3t-1-t)^2 + (0-t)^2 \\& = (1-t)^2 + (2t-1)^2 + t^2       \\& = (1-2t+t^2) + (4t^2-4t+1) + t^2 \\& = 6t^2 - 6t + 2
\end{align*}
$$

  よって，この場合の回転断面積$S(t)$は
  
$$
\begin{align}
S(t)
     & = \pi\overline{P_t Q}^2 \nonumber\\& = \pi(6t^2 - 6t + 2) \label{1993-1:eq:2}
\end{align}
$$

  となる．

  
  続いて，体積$V$の計算を行う．
  この立体は$t=\frac{1}{2}$（立方体の中心）に関して対称であるため，
  体積の半分$\frac{V}{2}$を$t=0$から$t=\frac{1}{2}$まで積分して求める．
  積分要素$dl$は$P_t = t\va*{l}$の移動距離であるため$dl = \sqrt{1^2+1^2+1^2}dt = \sqrt{3}dt$となる．
  
$$
\begin{align*}
\frac{V}{2}& = \int_{0}^{1/2} S(t) \sqrt{3}\dd t
\end{align*}
$$

  ここに$\eqref{1993-1:eq:1,1993-1:eq:2}$を代入して
  
$$
\begin{align*}
\frac{V}{2}& = \sqrt{3}\pi\left(\int_{0}^{1/3} 6t^2 \dd t + \int_{1/3}^{1/2}(6t^2 - 6t + 2) \dd t \right)\\& = \sqrt{3}\pi\left(\left[ 2t^3 \right]_{0}^{1/3} + \left[ 2t^3 - 3t^2 + 2t \right]_{1/3}^{1/2}\right)\\& = \sqrt{3}\pi\left(\frac{2}{27} + \left\{\frac{1}{4} - \frac{3}{4} + 1 \right\} - \left\{\frac{2}{27} - \frac{1}{3} + \frac{2}{3}\right\}\right)\\& = \sqrt{3}\pi\left(\frac{2}{27} + \frac{1}{2} - \frac{11}{27}\right)\\& = \sqrt{3}\pi\left(\frac{1}{2} - \frac{9}{27}\right) = \sqrt{3}\pi\left(\frac{1}{2} - \frac{1}{3}\right) = \sqrt{3}\pi\left(\frac{1}{6}\right)\\& = \frac{\sqrt{3}}{6}\pi
\end{align*}
$$

  したがって、求める体積$V$は、
  
$$
\begin{align*}
V = 2 \times\frac{\sqrt{3}}{6}\pi = \frac{\sqrt{3}}{3}\pi
\end{align*}
$$

  である．$\cdots$(答)

  

  

## 【解説】

  立方体を回転させるシンプルな問題だが，断面図には二つの場合わけが必要である．
  うまいこと座標を設定して断面を求められれば良い．

  いくつか基本的な事項を確認しておこう．まず，空間上である法線ベクトル$\vec{n}=(n_x,n_y,n_z)$をもち，点$\vec{a}=(a_x,a_y,a_z)$を通る平面の方程式は，
  ベクトル表示で
  
$$
\begin{align*}
\left(\vec{x}-\vec{a}\right)\cdot\vec{n} = 0
\end{align*}
$$

  と与えられる．パラメータ表示すると
  
$$
\begin{align*}
n_x(x-a_x)+n_y(y-a_y)+n_z(z-a_z)=0
\end{align*}
$$

  となる．今回の場合，点$(t,t,t)$を通り，法線ベクトルが$(1,1,1)$なので，切断平面の方程式は
  
$$
\begin{align*}
x+y+z=3t
\end{align*}
$$

  というわかりやすい形になる．
  従って，解答中では利用しなかったがこの方程式と立方体の交点を求めることでも断面の面積を求められる．

  次に，空間中で方向ベクトル$\vec{p}=(p_x,p_y,p_z)$として点$\vec{a}=(a_x,a_y,a_z)$を通る直線は，
  パラメータ$t$を用いて
  
$$
\begin{align*}
\vec{x}-\vec{a} = t\vec{p}
\end{align*}
$$

  と表せる．

  このパラメータ直線上の点$A$から$B$まで直線に沿って，あるスカラー量$f(\vec{l})$を積分することを考える．
  微小線素を$d\vec{l}$と置くと積分は
  
$$
\begin{align*}
\vec{V} = \int_{A}^{B} f(\vec{l}) d\vec{l}
\end{align*}
$$

  と表せる．今回の問題のように位置ベクトル$\vec{l}$が
  
$$
\begin{align*}
\vec{l}& = t \vec{AB}\\& = t \mqty(1  \\ 1 \\ 1)
\end{align*}
$$

  と単純にパラメータで表せる場合，微小線素は
  
$$
\begin{align*}
d\vec{l}& = dt \mqty(1 \\ 1 \\ 1)
\end{align*}
$$

  と表せる．$A,B$がそれぞれ$t=t_A,t_B$に対応するとすると，積分は$t$によって
  
$$
\begin{align*}
\vec{V} = \int_{t_A}^{t_B} f(t) \mqty(1 \\1\\1) dt
\end{align*}
$$

  と表せる．

  今回の問題では，積分は線素の絶対値に関するものだから
  
$$
\begin{align*}
V = \int_{A}^{B} f(l) dl
\end{align*}
$$

  となり，この時，線素$l$とパラメータ$t$の変換は
  
$$
\begin{align*}
dl
     & =dt \left|\mqty(1 \\ 1 \\ 1)\right|\\& = \sqrt{3} dt
\end{align*}
$$

  のように，方向ベクトルの大きさ分の余分な係数がかかることに注意が必要である．