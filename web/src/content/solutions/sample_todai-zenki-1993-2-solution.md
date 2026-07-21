---
university: "sample_todai"
category: "zenki"
year: "1993"
question: "2"
type: "solution"
title: "SAMPLE_TODAI 1993 zenki Q2 (solution)"
---

<div class="oframed">

</div>

<div class="multicols">
**【解】**

$1$ 三角形ABCの重心の座標を
``` math

$$
\begin{aligned}
\begin{dcases}
      x_g = \frac{x_1+x_2+x_3}{3} \\
      y_g = \frac{y_1+y_2+y_3}{3}
    \end{dcases}
\end{aligned}
$$

```
とおく．

与えられた曲線と平行な曲線を
``` math

$$
\begin{aligned}
l: g$x,y$ = a$x-x_g$ + b$y-y_g$ + c = 0
\end{aligned}
$$

```
とおく．
ここで$`a,b`$は所与の固定値（ただし$`$a,b$ \neq $0,0$`$）であり，$`c`$が色々変わる時の$`f$l$`$の最小値を考えれば良い．
$`K=A,B,C`$ に対し$`k=1,2,3`$ とおくと，点と直線の距離公式から
``` math

$$
\begin{aligned}
d$l,k$ = \frac{|g$x_k, y_k$|}{\sqrt{a^2+b^2}}
\end{aligned}
$$

```
なので，
``` math

$$
\begin{aligned}
T_k = a$x_k-x_g$ + b$y_k-y_g$
\end{aligned}
$$

```
とおくと，
``` math

$$
\begin{aligned}
f$l$
     & = \frac{1}{a^2+b^2} \sum_{k=1}^{3} \{g$x_k, y_k$\}^2                                                              \\
     & = \frac{1}{a^2+b^2} \sum_{k=1}^{3} [c^2 + 2T_kc + T_k^2]                                                          \\
     & = \frac{1}{a^2+b^2} \left[3c^2 + 2$\sum_{k=1}^{3} T_k$c + \sum_{k=1}^{3} T_k^2\right]                             \\
     & = \frac{3}{a^2+b^2} \left[\left$c+\frac{1}{3}\sum_{k=1}^{3} T_k\right$^2 + \frac{8}{9}\sum_{k=1}^{3} T_k^2\right]
\end{aligned}
$$

```
である． $`c`$を動かすと
``` math

$$
\begin{aligned}
c = -\frac{1}{3}\sum_{k=1}^{3}T_k
\end{aligned}
$$

```
で $`f$l$`$ は最小値をとる． この時の$`c`$を具体的に計算すると
``` math

$$
\begin{aligned}
c
     & = -\frac{1}{3} [a$x_1+x_2+x_3 - 3x_g$ + b$y_1+y_2+y_3 - 3y_g$] \\
     & = 0
\end{aligned}
$$

```
だから，$`l`$の方程式は
``` math

$$
\begin{aligned}
l_0 : a$x-x_g$ + b$y-y_g$ = 0
\end{aligned}
$$

```
となる．従ってたしかに $`l_0`$ は $`\triangle ABC`$ の重心
$`$x_g, y_g$`$ を通る． よって題意は示された．$`\cdots`$$答$

$2$ 並進対称性より$`\triangle ABC`$ の重心が $`O$0,0$`$
となるようにして考えて良い． 回転対称性より$`A$1,0$`$
の時をかんがえれば良い．

この時，残りのB，Cの座標について重心の条件から
``` math

$$
\begin{aligned}
\begin{dcases}
      1+x_2+x_3=0 \\
      y_2+y_3=0
    \end{dcases}
\end{aligned}
$$

```
である．

以下，$`0\le \theta < 2\pi`$なる実数$`\theta`$を用いて
``` math

$$
\begin{aligned}
l: -\sin\theta x+\cos\theta y=0
\end{aligned}
$$

```
とおく．$`\theta`$ と $`l`$ は１対１に対応する．
従って，$`f$l$`$が最小になるような$`\theta`$が3つ存在する時を考えれば良い．

<figure id="1993-2:fig:1" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai/zenki/1993/2/fig_1.svg" />
<figcaption>三角形ABCの様子</figcaption>
</figure>

点と直線の距離公式から
``` math

$$
\begin{aligned}
d$l,k$^2
     & = $-\sin\theta x_k+\cos\theta y_k$^2                                  \\
     & = \sin^2\theta x_k^2+\cos^2\theta y_k^2-2\cos\theta \sin\theta x_ky_k
\end{aligned}
$$

```
だから，
``` math

$$
\begin{aligned}
f$l$
     & = \sum_{k=1}^3 d$l,k$^2
     & = \sin^2\theta$1+x_2^2+x_3^2$ + \cos^2\theta $y_2^2+y_3^2$ - 2\cos\theta\sin\theta $x_2y_2+x_3y_3$
\end{aligned}
$$

```
である． <a href="#$式1, 式1, 式1$
     & = \sin^2\theta $2x_2^2+2x_2+2$ + 2y_2^2\cos^2\theta - 2\cos\theta\sin\theta$2x_2y_2+y_2$ \\
     & = P$1-\cos2\theta$ + Q$1+\cos2\theta$ - R\sin2\theta                                     \\
     & = $-P+Q$\cos2\theta - R\sin2\theta + $P+Q$
\end{aligned}
$$

```
と書ける．ただし
``` math

$$
\begin{aligned}
\begin{dcases}
      P=x_2^2+x_2+1 \\
      Q=y_2^2       \\
      R=$2x_2+1$y_2
    \end{dcases}
\end{aligned}
$$

```
とした．

<a href="#$式2, 式2, 式2$^2+R^2 \neq 0
\end{aligned}
$$

```
の時，三角関数の合成を用いて適当な実数$`\alpha`$があって
``` math

$$
\begin{aligned}
f$l$ = \sqrt{$-P+Q$^2+R^2} \sin$2\theta+\alpha$ + $P+Q$
\end{aligned}
$$

```
が成り立つ．
$`0 \le \theta < 2\pi`$から$`\alpha \le 2\theta+\alpha < 2\pi+\alpha`$
だから， $`f$l$`$は３つの$`\theta`$で最小値をとりえず不適である．

したがって $`$-P+Q$^2+R^2=0`$
が必要である．この時$`P,Q,R \in \mathbb{R}`$ から
``` math

$$
\begin{aligned}
-P+Q=R=0
\end{aligned}
$$

```
であり，この時$`f$l$=P+Q`$で$`\theta`$によらず一定であり，$`3`$つの$`\theta`$で最小値をとる．

一定で十分である。<a href="#$式3, 式3, 式3$ = 0
    \end{dcases}
\end{aligned}
$$

```
第二式から $`y_2=0`$ または $`x_2=-\frac{1}{2}`$ である．
$`y_2=0`$の時<a href="#$式1, 式1, 式1, 式1, 式1, 式1$
     & B=$-\frac{1}{2}, \pm\frac{\sqrt{3}}{2}$ \\
     & C=$-\frac{1}{2}, \mp\frac{\sqrt{3}}{2}$
\end{aligned}
$$

```
であり$`\triangle ABC`$ は正三角形である．
よって題意は示された．$`\cdots`$$答$

**【解説】**

</div>
