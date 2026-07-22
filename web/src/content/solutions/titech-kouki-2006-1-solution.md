---
university: "titech"
category: "kouki"
year: "2006"
question: "1"
type: "solution"
title: "TITECH 2006 kouki Q1 (solution)"
---

## 【解】

### (1)

  題意より，
  
$$
\begin{align*}
& C: ax^2 + by^2 = 1 \quad(x \ge 0, y \le 0) \\& l_t: y = tx \quad(t \ge 0, x \ge 0)
\end{align*}
$$

  である．$l_t$,$C$上の点$P,P'$は
  $P(X,tX), P'(X,Y)$とおける．ただし
  
$$
\begin{align*}
& 0 \le X \le\frac{1}{\sqrt{a}}\\& Y = -\sqrt{\frac{1 - aX^2}{b}}
\end{align*}
$$

  である．この様子を[図1](#2006-1:fig:1)に示す．

  

<figure id="2006-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2006/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $C$および$l_t$の概形</figcaption>
</figure>

  $PP' = g(X)$とおくと，
  
$$
\begin{align*}
g(X)
     & = tX + |Y|                       \\& = tX + \sqrt{\frac{1 - aX^2}{b}}
\end{align*}
$$

  より，一階微分は
  
$$
\begin{align*}
g'(x)
     & = t + \frac{1}{\sqrt{b}}\frac{-2ax}{2\sqrt{1-ax^2}}\\& = \frac{t\sqrt{b(1-ax^2)}-ax}{\sqrt{b(1-ax^2)}}\\& = \frac{t^2b(1-ax^2)-a^2x^2}{\sqrt{b(1-ax^2)}\left(t\sqrt{b(1-ax^2)}+ax\right)}\\& = \frac{bt^2 - (abt^2+a^2)x^2}{\sqrt{b(1-ax^2)}\left(t\sqrt{b(1-ax^2)}+ax\right)}
\end{align*}
$$

  と書ける．
  分母は常に正であり，$g'=0$となるのは
  
$$
\begin{align*}
\alpha = \sqrt{\frac{bt^2}{abt^2 + a^2}}
\end{align*}
$$

  の時である．
  増減表は[表1](#2006-1:table:1)となる．
  

<figure id="2006-1:table:1" class="table-wrapper">

| $X$ | $0$ |  | $\alpha$ |  | $\frac{1}{\sqrt{a}}$ |
|:--:|:--:|:--:|:--:|:--:|:--:|
| $g'$ |  | $+$ | $0$ | $-$ |  |
| $g$ | $1/\sqrt{b}$ | $\nearrow$ | 最大 | $\searrow$ | $t/\sqrt{a}$ |

  <figcaption>表 1: $g(x)$の増減表</figcaption>
</figure>

  よって $X = \alpha$ で $g(X)$は最大だから，$P_t$の座標は
  
$$
\begin{align*}
X & = \alpha\\
    Y & = t\alpha
\end{align*}
$$

  で与えられる.

  ここから$t$を消去すれば，題意の曲線$C'$の表示を得る．
  まず，$t=0$の時, $P_0(0,0)$である．
  次に $t \ne 0$の時$X \ne 0$から
  
$$
\begin{align*}
t = \frac{Y}{X}
\end{align*}
$$

  であり，$X=\alpha$ に代入して
  
$$
\begin{align*}
& X  = \sqrt{\frac{bt^2}{abt^2 + a^2}}\\& X  = \sqrt{\frac{b(Y/X)^2}{ab(Y/X)^2 + a^2 }}\\\iff& X^2 \{ ab Y^2  + a^2 X^2 \} = b Y^2 \quad(\because X \ge 0) \\\iff& Y^2 (b-abX^2) = a^2 X^4                                      \\\iff& Y = \frac{aX^2}{\sqrt{b(1-aX^2)}}
\end{align*}
$$

  ただし，$X=1/\sqrt{a}$の時はこの式は成り立たないから，$0 < X < \frac{1}{\sqrt{a}}$である．
  この式は$t=0$でも成立するから，求めるべき曲線$C'$の表示は
  
$$
\begin{align*}
f(X) = \frac{aX^2}{\sqrt{b(1-aX^2)}}\quad\left(0 \le X < \frac{1}{\sqrt{a}}\right)
\end{align*}
$$

  である．$\cdots$(答)

  

<figure id="2006-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2006/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $C$および$C'$の概形</figcaption>
</figure>

### (2)
 $C$と$C'$の方程式の連立解を求める．
  楕円$C$の式に$y=f(x)$を代入して$y$を除去すると，
  
$$
\begin{align*}
& ax^2 + b\frac{(ax^2)^2}{b(1-ax^2)} = 1 \\\therefore& ax^2(1-ax^2) + a^2x^4 = 1-ax^2         \\\therefore& 2ax^2 = 1                              \\\therefore& x = \sqrt{\frac{1}{2a}}
\end{align*}
$$

  であり，この時，
  
$$
\begin{align*}
y & = f(x)                         \\& =\frac{a/2a}{\sqrt{b(1-a/2a)}}\\& = \sqrt{\frac{1}{2b}}
\end{align*}
$$

  である．以上から
  
$$
\begin{align*}
& \alpha = \sqrt{\frac{1}{2a}}& \beta  = \sqrt{\frac{1}{2b}}
\end{align*}
$$

  である．$\cdots$(答)

### (3)

  $f(x)$は区間内で単調増加で， グラフ概形および領域$D$は[図3](#2006-1:fig:3)である．

  

<figure id="2006-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2006/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $D$の概形</figcaption>
</figure>

  以下，バームクーヘン積分法によって$D$を$y$軸周りに回転した回転体の体積$V$を求める．
  $x \sim x+dx \quad (dx \ll 1)$の部分を軸まわりに回した
  立体の体積は幅$dx$, 高さ$\frac{1}{\sqrt{2b}}-f(x)$, 長さ$2\pi x$の直方体で近似できるので,
  求める立体の体積$V$として，
  
$$
\begin{align}
V = 2\pi\int_{0}^{\sqrt{\frac{1}{2a}}}\left(\frac{1}{\sqrt{2b}} - f(x)\right)x dx \label{2006-1:eq:1}
\end{align}
$$

  である．一項目は
  
$$
\begin{align}
\int_{0}^{\sqrt{\frac{1}{2a}}}\frac{1}{\sqrt{2b}} x dx
     & = \frac{1}{2}\frac{1}{\sqrt{2b}} x^2 \Big|_{0}^{\sqrt{\frac{1}{2a}}}\nonumber\\& = \frac{1}{4\sqrt{2}}\frac{1}{a\sqrt{b}}\label{2006-1:eq:2}
\end{align}
$$

  であり，二項目は$s=1-ax^2$と置換すると
  
$$
\begin{align}
\int_{0}^{\sqrt{\frac{1}{2a}}} f(x)x dx
     & = \int_{1}^{1/2}\frac{1-s}{\sqrt{bs}}\frac{1}{-2a} ds                        \nonumber\\& = \frac{1}{2a\sqrt{b}}\int_{1/2}^{1}\left(\frac{1}{\sqrt{s}} - \sqrt{s}\right) ds  \nonumber\\& = \frac{1}{2a\sqrt{b}}\left[2\sqrt{s} - \frac{2}{3} s^{3/2}\right]_{1/2}^{1}\nonumber\\& = \frac{1}{2a\sqrt{b}}\left[2\left(1-\frac{1}{\sqrt{2}}\right) -
    \frac{2}{3}\left(1-\frac{1}{2\sqrt{2}}\right)\right]\nonumber\\& = \frac{1}{2a\sqrt{b}}\left(\frac{4}{3} - \frac{5\sqrt{2}}{6}\right)\label{2006-1:eq:3}
\end{align}
$$

  だから，$\eqref{2006-1:eq:2,2006-1:eq:2}$を$\eqref{2006-1:eq:1}$に代入して
  
$$
\begin{align*}
V & = 2\pi\left[\frac{1}{4\sqrt{2}a\sqrt{b}}  - \frac{1}{2a\sqrt{b}}\left(\frac{4}{3} - \frac{5\sqrt{2}}{6}\right)\right]\\& = \frac{2\pi}{a\sqrt{b}}\left[\frac{13\sqrt{2}}{24} - \frac{2}{3}\right]
\end{align*}
$$

  が求める体積である．  $\cdots$(答)

  
  

## 【解説】

  平面図形と回転体という東工大の定番問題．問題設定が比較的単純なため，東工大のこの手の問題にしては容易な方である．

### (1)
ができれば(2)(3)はただ計算するだけなので，(1)を突破できるかがポイントとなる．

### (1)
の線分$PP'$の長さは，$P(X,Y)$の$x$座標を与えれば決定できる一変数関数（$g(x)$）なので，まずは$t$を固定した時の$g$の最大値を与える$X(t)$を求める．
  その上で軌跡を求めるには$X(t),Y(t)$から$t$を消去して$X,Y$の関係式を得れば良い．
  $PP'$が一変数関数なことと文字消去が$t=Y/X$だけなことから直線的に答えにたどり着ける．
  答えが妥当なことは$t$が極端なときを考えると，$t=0$のとき$P(0,0)$，$t\to\infty$のとき$P(1/\sqrt{2a},\infty)$であることからそれらしいとわかる．

  答案上工夫できる点があるとすれば，以下のような楕円が出てくるときに使える手法は検討の余地がある．

  一つ目の方法として，この手の楕円が登場するときのテクニックである
  
$$
\begin{align*}
\begin{dcases}
      x' = \frac{x}{\sqrt{a}} \\
      y' = \frac{y}{\sqrt{b}}
    \end{dcases}
\end{align*}
$$

  なる変数変換が考えられる．
  これを使うと楕円を円
  
$$
\begin{align*}
(x')^2+(y')^2=1
\end{align*}
$$

  に変換できる．
  すると，$P(X,tX)$は$P(X/\sqrt{a},tX/\sqrt{b})$に変換され，
  この座標系での$PP'$の長さ
  
$$
\begin{align*}
PP' = \frac{t\sqrt{a}x'}{\sqrt{b}} + \sqrt{1-(x')^2}
\end{align*}
$$

  が最大の時，元の座標系での$PP'$の最大である．
  残念ながらこの方法は今回問題を簡単にはしてくれない．

  二つ目の方法として，楕円上の点をパラメータ表示することも考えられる．
  すなわちパラメータ$\theta\, -\pi/2 \ge \theta \ge 0$を用いて
  $P'(\cos\theta/\sqrt{a},\sin\theta/\sqrt{b})$とおくと
  $P(\cos\theta/\sqrt{a},t\cos\theta/\sqrt{a})$であって
  
$$
\begin{align*}
|PP'| = g(\theta) = \frac{t\cos\theta}{\sqrt{a}} - \frac{\sin\theta}{\sqrt{b}}
\end{align*}
$$

  と計算できるから，あとはこれを最大化する$\theta$を求める．
  これは三角関数の合成を使えば容易に求まる．簡単のため$\theta \to -\theta$の変換をかけると
  
$$
\begin{align*}
g(\theta)
     & = \frac{t}{\sqrt{a}}\cos\theta + \frac{1}{\sqrt{b}}\sin\theta\\& = \sqrt{\frac{t^2}{a}+\frac{1}{b}}\sin\left(\theta + \beta\right)
\end{align*}
$$

  なる$\beta$が存在する．ただし$0 \ge \beta \ge \pi/2$および
  
$$
\begin{align*}
\begin{dcases}
      \cos\beta = \frac{\frac{1}{\sqrt{b}}}{\sqrt{\frac{t^2}{a}+\frac{1}{b}}} = \frac{a}{bt^2+a} \\
      \sin\beta = \frac{\frac{t}{\sqrt{a}}}{\sqrt{\frac{t^2}{a}+\frac{1}{b}}} = \frac{bt^2}{bt^2+a}
    \end{dcases}
\end{align*}
$$

  である．

  したがって$0 \ge \theta \ge \pi/2$の範囲でのこの最大値は$\theta + \beta = \pi/2$の時で
  
$$
\begin{align*}
\max g(\theta) =  \sqrt{\frac{bt^2+a}{ab}}
\end{align*}
$$

  であり，したがってこの時の$P(X,Y)$の座標は
  
$$
\begin{align*}
X
     & = \cos\theta/\sqrt{a}\\& = \cos(\pi/2-\beta)/\sqrt{a}\\& = \sin\beta/\sqrt{a}\\& = \frac{bt^2}{abt^2+a^2}
\end{align*}
$$

  および
  
$$
\begin{align*}
Y
     & =  \sin\theta/\sqrt{b}\\& =  \sin(\pi/2-\beta)/\sqrt{b}\\& =  \cos\beta/\sqrt{b}\\& =  \frac{a}{b^2t^2+ab}
\end{align*}
$$

  であり，解答に合流する．
  このパラメータの置き方だと$g$の微分が不要なので多少楽である．