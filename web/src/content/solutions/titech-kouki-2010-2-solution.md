---
university: "titech"
category: "kouki"
year: "2010"
question: "2"
type: "solution"
title: "TITECH 2010 kouki Q2 (solution)"
---

## 【解】

  関数を
  
$$
\begin{align*}
f(x) = \left(\log x\right)^2 & (x>0)
\end{align*}
$$

  とおく．

### (1)

  一階，二階微分は
  
$$
\begin{align}
f'(x)  & = 2 \frac{\log x}{x}\label{2010-2:eq:1}\\
    f''(x) & = 2 \frac{1-\log x}{x^2}
\end{align}
$$

  であるから，増減表は[表1](#2010-2:table:1)となる．
  

<figure id="2010-2:table:1" class="table-wrapper">

| $x$ | $0$ | $\cdots$ | $1$ | $\cdots$ | $e$ | $\cdots$ |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $f'$ |  | $-$ | $0$ | $+$ | $+$ | $+$ |  |
| $f''$ |  | $+$ | $+$ | $+$ | $0$ | $-$ |  |
| $f$ | $(\infty)$ | $\roundedArrowDR$ | $0$ | $\roundedArrowRU$ | $1$ | $\roundedArrowUR$ | () |

  <figcaption>表 1: $f(x)$の増減表</figcaption>
</figure>

  従って，グラフの概形は[図1](#2010-2:fig:1)となる．
  

<figure id="2010-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2010/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $C$の概形．$x=e$が変曲点となる．</figcaption>
</figure>

  $\cdots$(答)

### (2)

  $P(\alpha, f(\alpha))$ での接線 $L(\alpha)$ は,$\eqref{2010-2:eq:1}$から
  
$$
\begin{align*}
y
     & = l(x)                                               \\& = f'(x) (x - \alpha) + f(\alpha)                     \\& = 2\frac{\log \alpha}{\alpha}(x-\alpha) + f(\alpha)
\end{align*}
$$

  であるから，$L(\alpha)$ と $C$ の共有点の個数は
  
$$
\begin{align}
& l(x) = f(x)                                                                                   \\\therefore& (\log x)^2 - (\log\alpha)^2 - 2\frac{\log \alpha}{\alpha}(x-\alpha) = 0 \label{2010-2:eq:5}
\end{align}
$$

  の $x>0$ の解の個数にひとしい.
  $\eqref{2010-2:eq:5}$の左辺を $g(x)$ とおき，$g(x)$の挙動から解の個数を求める．
  
$$
\begin{align*}
g(x) = (\log x)^2 - (\log\alpha)^2 - 2\frac{\log \alpha}{\alpha}(x-\alpha)
\end{align*}
$$

  $g(x)$の一階微分は
  
$$
\begin{align*}
g'(x) = 2 \left(\frac{\log x}{x} - \frac{\log \alpha}{\alpha}\right)
\end{align*}
$$

  であるから，新しく
  
$$
\begin{align*}
h(x) = \frac{\log x}{x}
\end{align*}
$$

  とおくと
  
$$
\begin{align*}
g'(x) = 2 \left(h(x)-h(\alpha)\right)
\end{align*}
$$

  となる．よって$h(x)$の挙動から$g'(x)$の符号がわかる．
  $\eqref{2010-2:eq:1}$より$h(x) = f'(x)/2$だから，
  
$$
\begin{align*}
h'(x) = \frac{f''(x)}{2}
\end{align*}
$$

  であり，$h(x)$の増減表は[表2](#2010-2:table:2)となる．
  

<figure id="2010-2:table:2" class="table-wrapper">

| $x$  |     $0$     |  $\cdots$  | $e$ |  $\cdots$  | $\infty$ |
|:------:|:-------------:|:------------:|:-----:|:------------:|:----------:|
| $h'$ |               |    $+$     | $0$ |    $-$     |            |
| $f$  | $(-\infty)$ | $\nearrow$ | $1$ | $\searrow$ |   \(0\)    |

  <figcaption>表 2: $h(x)$の増減表</figcaption>
</figure>

  従って$y=h(x)$のグラフの概形は[図2](#2010-2:fig:2)となる．
  

<figure id="2010-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2010/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $h(x)$の概形.$x=e$で最大値をとり，$\alpha$の値によって$g'(x)$の零点の数が変化する．</figcaption>
</figure>

  以下$\alpha$の値によって場合わけする．

  
  \underline{**$0<\alpha\le 1$の時**}

  $g'(x) = 0$となる$x$は$x=\alpha$ただ一つである．
  $x<\alpha$では$g'(x)<0$, $\alpha<x$では$g'(x)>0$である．
  また，$g(x)$の極限値は
  
$$
\begin{align*}
\lim_{x\to 0} g(x)      & = \infty\\\lim_{x\to \infty} g(x) & = \infty
\end{align*}
$$

  である．
  従って$g(x)$の増減表は[表3](#2010-2:table:3)のようになる．
  

<figure id="2010-2:table:3" class="table-wrapper">

| $x$  |    $0$     |  $\cdots$  | $\alpha$ |  $\cdots$  |  $\infty$  |
|:------:|:------------:|:------------:|:----------:|:------------:|:------------:|
| $g'$ |              |    $-$     |   $0$    |    $+$     |              |
| $g$  | $(\infty)$ | $\searrow$ |   $0$    | $\nearrow$ | $(\infty)$ |

  <figcaption>表 3: $g(x)$の増減表</figcaption>
</figure>

  従って，$g(x)=0$の解の数は$x=\alpha$ただ一つ．

  
  \underline{**$\alpha= e$の時**}

  $g'(x) = 0$となる$x$は$x=\alpha$ただ一つである．
  それ以外のとき，$g'(x)<0$である．
  また，$g(x)$の極限値は
  
$$
\begin{align*}
\lim_{x\to 0} g(x)      & = \infty\\\lim_{x\to \infty} g(x) & = -\infty
\end{align*}
$$

  である．
  従って$g(x)$の増減表は[表4](#2010-2:table:4)のようになる．
  

<figure id="2010-2:table:4" class="table-wrapper">

| $x$  |    $0$     |  $\cdots$  | $\alpha$ |  $\cdots$  |  $\infty$   |
|:------:|:------------:|:------------:|:----------:|:------------:|:-------------:|
| $g'$ |              |    $-$     |   $0$    |    $-$     |               |
| $g$  | $(\infty)$ | $\searrow$ |   $0$    | $\nearrow$ | $(-\infty)$ |

  <figcaption>表 4: $g(x)$の増減表</figcaption>
</figure>

  よって，$g(x)=0$の解の数は$x=\alpha$ただ一つ．

  
  \underline{**$1 < \alpha, \, \alpha\neq e$の時**}

  この時は$x=\alpha$以外にもう一つ$g'(x)=0$となる$x$がある．
  これを$x=\beta$とする．
  また，$g(x)$の極限値は
  
$$
\begin{align*}
\lim_{x\to 0} g(x)      & = \infty\\\lim_{x\to \infty} g(x) & = -\infty
\end{align*}
$$

  である．
  よって$g(x)$の増減表は[表5](#2010-2:table:5)となる．
  

<figure id="2010-2:table:5" class="table-wrapper">

| $x$ | $0$ | $\cdots$ | $\alpha$ | $\cdots$ | $\beta$ | $\cdots$ | $\infty$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $g'$ |  | $-$ | $0$ | $+$ | $0$ | $-$ |  |
| $g$ | $(\infty)$ | $\searrow$ | $0$ | $\nearrow$ |  | $\searrow$ | $(-\infty)$ |

  <figcaption>表 5: $h(x)$の増減表</figcaption>
</figure>

  従って，$g(x)=0$の解の数は二つである．

  以上三つの場合わけにより全ての場合は尽くされた．
  従って求める共有点の個数は
  
$$
\begin{align*}
n(\alpha) =
    \begin{dcases}
      0 < \alpha \le 1, \alpha = e & \cdots \text{1つ} \\
      1 < \alpha (\alpha \ne e)    & \cdots \text{2つ}
    \end{dcases}
\end{align*}
$$

  である．  $\cdots$(答)

### (3)

  $P$から$x$軸に下ろした垂足$Q(\alpha,0)$, $L(a)$と$x$軸の交点$R$, また$T(1,0)$とおく.
  すると$R$の$x$座標は
  
$$
\begin{align*}
& 2\frac{\log \alpha}{\alpha}(x-\alpha) + \left(\log\alpha\right)^2 = 0 \\\therefore& x = \alpha - \frac{\alpha}{2}\log\alpha
\end{align*}
$$

  となる．
  題意の領域の概形は[図3](#2010-2:fig:3)のようになる．
  

<figure id="2010-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2010/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 求める面積の概形</figcaption>
</figure>

  求める面積$S(\alpha)$は，図形$PQT$の面積$A(\alpha)$から，三角形$PQR$の面積$B(\alpha)$を減じたものに等しい．
  すなわち
  
$$
\begin{align}
S(\alpha) = A(\alpha) - B(\alpha) \label{2010-2:eq:2}
\end{align}
$$

  まず，$\triangle PQR$について，
  
$$
\begin{align*}
|QR|
     & = \alpha - \frac{1}{2}\alpha\log\alpha - \alpha\\& = - \frac{1}{2}\alpha\log\alpha
\end{align*}
$$

  および
  
$$
\begin{align*}
|PQ| = \left(\log\alpha\right)^2
\end{align*}
$$

  だから，
  
$$
\begin{align}
B(\alpha)
     & = \frac{1}{2}|QR||PQ|  \nonumber\\& = \frac{-1}{4}\alpha\left(\log\alpha\right)^3 \label{2010-2:eq:3}
\end{align}
$$

  である．
  次に$A(\alpha)$は部分積分法を繰り返し用いて
  
$$
\begin{align}
A(\alpha)
     & = \int_{\alpha}^{1}(\log x)^2 dx     \nonumber\\& = \left[ x(\log x)^2 - 2x\log x + 2x \right]_{\alpha}^{1}\nonumber\\& = (0 - 0 + 2)-(\alpha(\log\alpha)^2 - 2\alpha\log\alpha + 2\alpha)           \nonumber\\& = 2 - \alpha(\log\alpha)^2 + 2\alpha\log\alpha -2\alpha\label{2010-2:eq:4}
\end{align}
$$

  だから，$\eqref{2010-2:eq:3,2010-2:eq:4}$を$\eqref{2010-2:eq:2}$に代入して
  
$$
\begin{align*}
S(\alpha)
     & = 2 -\alpha(\log\alpha)^2 + 2\alpha\log\alpha - 2\alpha + \frac{1}{4}\alpha(\log\alpha)^3
\end{align*}
$$

  が求める面積である．  $\cdots$(答)

  
  

## 【解説】

  典型的な平面図形の問題で，あまり捻ったところもないのでとっつきやすい．

### (1)
でグラフの概形と言われれた時は，二階微分を計算して変曲点まで求めるのが受験業界での暗黙の了解である．

### (2)
では$y=\frac{\log x}{x}$の形の関数が出てくるが，これは2004年度の2番でも題材になっている．
  東工大の後期は比較的以前扱った題材が再度出てくることがあり，過去問演習の大切さを教えてくれる．

  今回の解答ではちゃんと厳密に方程式の解の個数から$n(\alpha)$を求めているが，

### (1)
のグラフの概形で変曲点まで求めているので，$\alpha \le 1$では一つ，$\alpha=e$でも一つ，それ以外では二つというのはすぐにわかる．
  なので答えがわかっている状態で答案を作りにいっているという表現が適切だろう．

### (3)
は図形の面積を求める問題で，$(\log x)^2$の形の積分を処理できれば問題ない．
  この形は$\log x$の微分を繰り返す形で部分積分を実行すれば良い．
  ちなみに一般の$(\log x)^{n}$の場合
  
$$
\begin{align*}
\int\left(\log x\right)^n dx
     & = x\left(\log x\right)^n - nx\left(\log x\right)^{n-1}\\& + n(n-1)x\left(\log x\right)^{n-2}-\cdots +(-1)^n n!x
\end{align*}
$$

  となるので頭の片隅に入れておくと良い．ここで各項の符号は正負の順番で入れ替わり，あとは$x$をかけた状態で$(\log x)^{n}$の次数を下ろして係数を足していけば良いので覚えやすい．
  一例として$n=1,2,3$の場合を示しておこう．
  
$$
\begin{align*}
\int\left(\log x\right)^1 dx & = x\log x - x + C                                \\\int\left(\log x\right)^2 dx & = x(\log x)^2 - 2x\log x + 2x + C                \\\int\left(\log x\right)^3 dx & = x(\log x)^3 - 3x(\log x)^2 + 6x\log x - 6x + C
\end{align*}
$$

  答えの簡単な検算として，$\alpha\to 1$の極限で$S(\alpha)$が$0$になることを確かめられる．
  また，もう一方の極限$\alpha\to 0$ではしっかりと$S(\alpha)$は無限大に発散する．
  よって，両方の極限での挙動は合っているので一安心できる．