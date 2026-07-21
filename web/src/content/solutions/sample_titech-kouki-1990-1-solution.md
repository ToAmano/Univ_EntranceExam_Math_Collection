---
university: "sample_titech"
category: "kouki"
year: "1990"
question: "1"
type: "solution"
title: "SAMPLE_TITECH 1990 kouki Q1 (solution)"
---

**【解】**

実数 $x$ に対して $f(x) = (x+1)(x-2)$, $g(x) = 1+5x$ とおく．題意から，

$$
\begin{aligned}
g(x) \in \mathbb{Z}, \quad g(x) - \frac{1}{2} \le f(x) < g(x) + \frac{1}{2}
\end{aligned}
$$
 をみたす $x \in \mathbb{R}$ をもとめればよい．
$g(x) \in \mathbb{Z}$ から
$5x \in \mathbb{Z}$．つまり，$x = \frac{t}{5}$ ($t \in \mathbb{Z}$)
とかける．(1990-1:eq:1\)に代入して$t$の条件式を求めると，

$$
\begin{aligned}
t + \frac{1}{2} & \le \left(\frac{t}{5}+1\right)\left(\frac{t}{5}-2\right) < t+\frac{3}{2}  \\
        t + \frac{1}{2} & \le \frac{1}{25}t^2  - \frac{1}{5}t - 2 < t+\frac{3}{2}                   \\
        \therefore 125  & \le 2t^2 - 60t < 175
\end{aligned}
$$
 を得る．

ここで，二次関数$y = p(t) = 2t^2 - 60t$
のグラフの概形は1のようになっており， 
$$
\begin{aligned}
& p(-3) = 198 & p(-1) = 62  \\
         & p(31) = 62  & p(33) = 198
\end{aligned}
$$

だから，(1990-1:eq:2\)を満たすような$t \in \mathbb{Z}$は $t=-2, 32$
である．したがって求めるべき$x=t/5$は$x = \frac{32}{5}, -\frac{2}{5}$
である． $\cdots$(答)

<figure id="1990-1:fig:1" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_titech/kouki/1990/1/fig_1.svg" />
<figcaption>二次関数 <span class="math inline">\(y = 2t^2 - 60t\)</span>
のグラフ</figcaption>
</figure>

**【解説】**
二次関数の問題．条件を素直に式に落としていけば解ける比較的容易な問題である．
二次関数 $(x+1)(x-2)$ と一次関数 $1+5x$
がほぼ等しくなるような条件なので，解はこれらの交点に近くなるだろうというのが予想できる．
実際にこれを解いてみると 
$$
\begin{aligned}
(x+1)(x-2)   & = 1 + 5x \\
        x^2 - 6x - 3 & = 0      \\
        x = 3 \pm 2\sqrt{3}
\end{aligned}
$$
 であり，$x \approx 6.46$ と $x \approx -0.46$
が得られる． 本問題の解答である$x = \frac{32}{5}, -\frac{2}{5}$
はこれらの値にほぼ等しく，検算として利用できるだろう．
