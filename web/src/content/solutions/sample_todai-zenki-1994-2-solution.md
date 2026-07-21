---
university: "sample_todai"
category: "zenki"
year: "1994"
question: "2"
type: "solution"
title: "SAMPLE_TODAI 1994 zenki Q2 (solution)"
---

<div class="oframed">

</div>

<div class="multicols">
**【解】** $1$

<figure id="1994-2:fig:1" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai/zenki/1994/2/fig_1.svg" />
<figcaption>一辺の長さ<span
class="math inline">$l$</span>の正方形と点Pの様子</figcaption>
</figure>

Pは円が1周する間$`4$l-2$`$だけ転がる．円の半径が$`1`$だから，
この時のPの回転角は$`4$l-2$`$に等しい．
また，各頂点でPの見た目の位相は$`\pi/2`$ずつ追加されるので，これは角が$`4`$つで合計$`2\pi`$となる．
したがってPが一周まわった時の総回転角は
``` math

$$
\begin{aligned}
L = 4$l-2$ + 2\pi
\end{aligned}
$$

```
となる．
Pが一周回って元の位置と等しくなるのは，$`L`$が$`2\pi`$の整数倍であることである．
よって$`n \in \mathbb{Z}`$として
``` math

$$
\begin{aligned}
& 4$l-2$ = 2n\pi         \\
    \therefore
     & l = \frac{n}{2}\pi + 2
\end{aligned}
$$

```
と書ける．$`\cdots`$$答$

$2$ 題意の条件$`l>2`$から，$1$をみたす$`l`$の最小値は$`n=1`$の時の
``` math

$$
\begin{aligned}
l=\frac{1}{2}\pi+2
\end{aligned}
$$

```
である． $`xy`$座標において，正方形の4頂点A Dを
``` math

$$
\begin{aligned}
& A$-1, -1$                           \\
     & B$\frac{\pi}{2}+1, -1$              \\
     & C$\frac{\pi}{2}+1, \frac{\pi}{2}+1$ \\
     & D$-1, \frac{\pi}{2}+1$
\end{aligned}
$$

```
とおき，$`P`$が$`A \to B \to C \to D`$の順に動くとする．

<figure id="1994-2:fig:2" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai/zenki/1994/2/fig_2.svg" />
<figcaption>一辺の長さ<span
class="math inline">$l$</span>の正方形ABCDと点Pの様子</figcaption>
</figure>

まず辺$`AB`$上を動く時を考える．
はじめ$`P$\cos\alpha, \sin\alpha$`$だとする． ただし
``` math

$$
\begin{aligned}
0 \le \alpha < 2\pi
\end{aligned}
$$

```
とする． 円が長さ$`\theta`$だけ転がった時のPの位置ベクトル
``` math

$$
\begin{aligned}
\vec{OP}
     & = \begin{pmatrix} \theta \\ 0 \end{pmatrix} + \begin{pmatrix} \cos$\alpha-\theta$ \\ \sin$\alpha-\theta$ \end{pmatrix} \quad $0 \le \theta \le \frac{\pi}{2}$
\end{aligned}
$$

```
だから，この時のPの軌跡の長さ$`l_1`$は
``` math

$$
\begin{aligned}
l_1
     & = \int_{0}^{\frac{\pi}{2}} |\overline{OP}| d\theta                                                                                    \\
     & = \int_{0}^{\frac{\pi}{2}} \sqrt{\{1+\sin$\alpha-\theta$\}^2 + \{\cos$\alpha-\theta$\}^2} d\theta                                     \\
     & = \int_{0}^{\frac{\pi}{2}} \sqrt{2\{1+\cos$\frac{\pi}{2}-\alpha+\theta$\}} d\theta                                                    \\
     & = 2 \int_{0}^{\frac{\pi}{2}} |\cos$\frac{\pi}{4}-\frac{\alpha}{2}+\frac{\theta}{2}$| d\theta                                          \\
     & = 4 \int_{\frac{\pi}{4}}^{\frac{\pi}{2}} |\cos$t-\frac{\alpha}{2}$| dt \quad $t = \frac{\pi}{4}+\frac{\theta}{2}$
\end{aligned}
$$

```
である．

PがBからCへ移動する時は$`\alpha`$ を $`\alpha - \frac{\pi}{2}`$
でおきかえて，この時のPの軌跡の長さ$`l_2`$は
``` math

$$
\begin{aligned}
l_2
     & = 2 \int_{0}^{\frac{\pi}{2}} |\cos$\frac{3}{4}\pi - \frac{\alpha}{2} + \frac{\theta}{2}$| d\theta \\
     & = 4 \int_{\frac{\pi}{4}}^{\frac{\pi}{2}} |\sin$t-\frac{\alpha}{2}$| dt
\end{aligned}
$$

```
である． 同様にPがCからDまで移動する時の軌跡の長さ$`l_3`$は$`\alpha`$ を
$`\alpha - 2\pi`$で，DからAまで移動する時の軌跡の長さ$`l_4`$は$`\alpha`$を$`\alpha - 3\pi`$
でおきかえたものだから
``` math

$$
\begin{aligned}
l_3
     & =  4 \int_{\frac{\pi}{4}}^{\frac{\pi}{2}} |\cos$t-\frac{\alpha-2\pi}{2}$| dt         \\
     & = l_1                                                                                \\
    l_4
     & = 4 \int_{\frac{\pi}{4}}^{\frac{\pi}{2}} |\cos$t-\frac{\alpha-3\pi}{2}$| dt          \\
     & = 4 \int_{\frac{\pi}{4}}^{\frac{\pi}{2}} |\cos$\frac{\pi}{2}+t-\frac{\alpha}{2}$| dt \\
     & = 4 \int_{\frac{\pi}{4}}^{\frac{\pi}{2}} |\sin$t-\frac{\alpha}{2}$| dt               \\
     & = l_2
\end{aligned}
$$

```
である．よって，合計の軌跡の長さ$`L`$は
``` math

$$
\begin{aligned}
L = 2$l_1+l_2$
\end{aligned}
$$

```
である．
<a href="#$式3, 式4, 式3, 式4, 式3, 式4$| + |\sin$t-\frac{\alpha}{2}$|\} dt \\
     & = 8\int_{\frac{\pi}{4}-\frac{\alpha}{2}}^{\frac{\pi}{2}-\frac{\alpha}{2}} \{|\cos t| + |\sin t |\} dt
\end{aligned}
$$

```
を得る．

$`t \to \frac{\pi}{2}-t`$と変数変換して
``` math

$$
\begin{aligned}
L
     & = -8\int_{\frac{\pi}{4}+\frac{\alpha}{2}}^{\frac{\alpha}{2}} \{|\cos $\pi/2-x$| + |\sin $\pi/2-x$ |\} dx \\
     & = 8\int_{p}^{\frac{\pi}{4}+p} \{|\sin x| + |\cos x|\} dx
\end{aligned}
$$

```
また，ここで簡単のため
``` math

$$
\begin{aligned}
& p = \frac{\alpha}{2} & 0 \le p < \pi
\end{aligned}
$$

```
とおいた．

$`y=|\cos t| + |\sin t|`$は周期$`\frac{\pi}{2}`$の周期関数だから，$`0 \le \alpha \le \frac{\pi}{2}`$で考えれば良い．
この時$`p \le t \le p + \frac{\pi}{4}`$では$`|\sin t| = \sin t`$であって，
$`|cos t|`$の値は$`\alpha`$の値によって変化する．
三角関数の合成を用いて$`L`$を変形すると
``` math

$$
\begin{aligned}
& L                                                                                                                                                                                                                                         \\
     & = \begin{dcases}
           8\int_{p}^{\frac{\pi}{4}+p} $\cos t + \sin t$ dt                                                               & \left$0 \le p \le \frac{\pi}{4}\right$             \\
           8\int_{p}^{\frac{\pi}{2}} $\cos t + \sin t$ dt + 8\int_{\frac{\pi}{2}}^{\frac{\pi}{4}+p} $-\cos t + \sin t$ dt & \left$\frac{\pi}{4} \le p \le \frac{\pi}{2}\right$
         \end{dcases}                                                 \\
     & = \begin{dcases}
           8\sqrt{2}\int_{p}^{\frac{\pi}{4}+p} \sin\left$t + \frac{\pi}{4}\right$ dt                                                                                      & \left$0 \le p \le \frac{\pi}{4}\right$             \\
           8\sqrt{2}\int_{p}^{\frac{\pi}{2}}\sin\left$t + \frac{\pi}{4}\right$ dt + 8\sqrt{2}\int_{\frac{\pi}{2}}^{\frac{\pi}{4}+p} \sin\left$t - \frac{\pi}{4}\right$ dt & \left$\frac{\pi}{4} \le p \le \frac{\pi}{2}\right$
         \end{dcases}
\end{aligned}
$$

```
を得る．

以下，$`p`$が変化した時の$`L`$の最大・最小を求めればよい．
$`L`$の$`p`$による一階微分は和積公式を用いて
``` math

$$
\begin{aligned}
\frac{dL}{dp}=
      & \begin{dcases}
          8\sqrt{2}\left[\sin$p+\frac{\pi}{2}$ -\sin$p+\frac{\pi}{4}$\right] & $0 \le p \le \frac{\pi}{4}$             \\
          8\sqrt{2}\left[-\sin$p+\frac{\pi}{4}$ + \sin p\right]              & $\frac{\pi}{4} \le p \le \frac{\pi}{2}$
        \end{dcases}      \\
    = & \begin{dcases}
          16\sqrt{2}\cos\left$p + \frac{3\pi}{8}\right$\sin\left$\frac{\pi}{8}\right$ & $0 \le p \le \frac{\pi}{4}$             \\
          -16\sqrt{2}\cos\left$p + \frac{\pi}{8}\right$\sin\left$\frac{\pi}{8}\right$ & $\frac{\pi}{4} \le p \le \frac{\pi}{2}$
        \end{dcases} \\
\end{aligned}
$$

```
と計算できるから，$`L`$の増減表は<a href="#1994-2:table:1" data-reference-type="ref+label"
data-reference="1994-2:table:1">1</a>となる．

| $`p`$ | $`0`$ |  | $`\frac{\pi}{8}`$ |  | $`\frac{\pi}{4}`$ |  | $`\frac{3\pi}{8}`$ |  | $`\frac{\pi}{2}`$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $`L'`$ |  | $`+`$ | $`0`$ | $`-`$ |  | $`-`$ | $`0`$ | $`+`$ |  |
| $`L`$ |  | $`\nearrow`$ |  | $`\searrow`$ |  | $`\searrow`$ |  | $`\nearrow`$ |  |

$`L`$の増減表 {#1994-2:table:1}

したがって、最大値は $`p=\frac{1}{8}\pi`$ 又は $`p=\frac{1}{2}\pi`$
の時にとる． 最小値は $`p=0`$ 又は $`p=\frac{3}{8}\pi`$の時にとる．

<figure id="1994-2:fig:3" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai/zenki/1994/2/fig_3.svg" />
<figcaption><span class="math inline">\(y=8|\sin t|+8|\cos
t|\)</span>の概形と<span
class="math inline">$L$</span>を面積と見立てた際の領域（<span
class="math inline">$p=\pi/8$</span>の場合の例）．</figcaption>
</figure>

ここで$`L`$は、$`y=8|\sin t|+8|\cos t|, t=p, t=p+\frac{\pi}{4}`$
とx軸の囲む面積でグラフは<a href="#1994-2:fig:3" data-reference-type="ref+label"
data-reference="1994-2:fig:3">3</a>だから
$`p=\frac{1}{2}\pi`$の時より$`p=\frac{1}{8}\pi`$の時の方がLは大きく，
$`p=0`$の時より$`p=\frac{3}{8}\pi`$の時の方がLは小さい． したがって

- $`p=\frac{1}{8}\pi`$ でLは最大\

- $`p=\frac{3}{8}\pi`$ でLは最小

である．

**1° $`P=\frac{1}{8}\pi`$の時**

この時$`L`$は
``` math

$$
\begin{aligned}
L
     & = 8\int_{\frac{1}{8}\pi}^{\frac{3}{8}\pi} \sqrt{2}\sin$t+\pi/4$dt \\
     & = -8\sqrt{2}[\cos\frac{5}{8}\pi - \cos\frac{3}{8}\pi]             \\
     & = 16\sqrt{2}\cos\frac{3}{8}\pi
\end{aligned}
$$

```
であり，$`\cos\frac{3}{8}\pi`$は半角公式より
``` math

$$
\begin{aligned}
\cos\frac{3}{8}\pi = \sqrt{\frac{1+\cos\frac{3}{4}\pi}{2}} = \frac{\sqrt{2-\sqrt{2}}}{2} \left$>0\right$
\end{aligned}
$$

```
と計算できるから，代入して
``` math

$$
\begin{aligned}
L = 8\sqrt{4-2\sqrt{2}}
\end{aligned}
$$

```
を得る．

**2° $`P=\frac{3}{8}\pi`$の時**

この時$`L`$は
``` math

$$
\begin{aligned}
L
     & = 16\int_{\frac{3}{8}\pi}^{\frac{\pi}{2}} \sqrt{2}\sin$t+\pi/4$dt \\
     & = 16\sqrt{2}$\frac{\sqrt{2}}{2} - \cos\frac{3}{8}\pi$             \\
     & = 8\{2-\sqrt{4-2\sqrt{2}}\}
\end{aligned}
$$

```
である．

以上<a href="#$式6, 式7, 式6, 式7, 式6, 式7$

**【解説】**

</div>
