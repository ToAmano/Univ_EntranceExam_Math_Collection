---
university: "sample_todai"
category: "zenki"
year: "1992"
question: "1"
type: "solution"
title: "SAMPLE_TODAI 1992 zenki Q1 (solution)"
---

**【解】**

\(1\) 題意の関数 \begin{align*}
        f_a(x) = \sqrt{x^2-1} + \frac{a}{x}
\end{align*} とおく．

$y=f_a(x)$が$1\le x$で$y<x$を満たす，つまり \begin{align*}
         & f_a(x) < x                   \\
        \iff
         & \sqrt{x^2-1} < x-\frac{a}{x}
\end{align*} を満たすような最大の実数$a$を求める．
$x-a/x>0$のもとで両辺二乗して \begin{align*}
         & x^2-1 < x^2 - 2a + \frac{a^2}{x^2} \\
        \iff
         & 2a-1 < \frac{a^2}{x^2}
\end{align*} $a=0$の時はこの不等式は成立する．
そこで$a\neq 0$の時を考えて両辺$a^2$でわると \begin{align*}
        \frac{2a-1}{a^2} < \frac{1}{x^2}
\end{align*} これが $1 \le x$ なる任意の $x$ でなりたつ．
$1/x^2$は$1 \le x$での下限値が$0<1/x^2$だから， 求める条件は
\begin{align*}
        \frac{2a-1}{a^2} \le 0 \\
        \therefore
        a \le \frac{1}{2}
\end{align*} である．

従って求める$a$の最大値は \begin{align*}
        a_0 = \frac{1}{2}
\end{align*} である．$\cdots$(答)

\(2\)
(1)から，$y=f_{a_0}(x)$は常に$y=x$の下側にあって，グラフの概形は1のようになる．

<figure id="1992-1:fig:1" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai/zenki/1992/1/fig_1.svg" />
<figcaption><span
class="math inline">\(y=f_a(x)\)</span>のグラフの概形と，題意の領域．</figcaption>
</figure>

従って求める体積$V(\theta)$は， \begin{align}
        V(\theta)
         & = \pi \int_1^{1/\cos\theta} \left[x^2 - f_a(x)^2\right] dx                                                       \\
         & = \pi \int_1^{1/\cos\theta} \left[x^2 - \left(x^2-1 + \frac{1}{4x^2} + \frac{1}{x}\sqrt{x^2-1}\right)\right]  dx \\
         & = \pi \int_1^{1/\cos\theta} \left[1 - \frac{1}{x^2} - \frac{1}{x}\sqrt{x^2-1}\right]  dx 
\end{align} である． 各項計算すると，まず第一，二項は \begin{align}
        \int_1^{1/\cos\theta} \left(1-\frac{1}{x^2}\right)dx
         & = \left[x + \frac{1}{x}\right]_{1}^{1/\cos\theta}                              \\                                                                          \\
         & = \frac{1}{\cos\theta} + \frac{\cos\theta}{4} - \frac{5}{4} \\
\end{align} である．
次に最終項は$x=1/\cos\alpha$と置換して，$dx/d\alpha = \sin\alpha/\cos^2\alpha$だから
\begin{align}
        \int_1^{1/\cos\theta} \frac{1}{x}\sqrt{x^2-1} dx
         & = \int_0^{\theta} \cos\alpha\tan\alpha \frac{\sin\alpha}{\cos^2\alpha}d\alpha \\
         & = \int_0^{\theta} \tan^2\alpha d\alpha                                        \\
         & = \int_0^{\theta} \left(\frac{1}{\cos^2\alpha}-1\right) d\alpha               \\
         & = \left[\tan\alpha-\alpha\right]_0^{\theta}                                   \\
         & = \tan\theta - \theta 
\end{align} である．
(1992-1:eq:2,1992-1:eq:3\)を(1992-1:eq:1\)に代入して，求める体積は \begin{align*}
        V(\theta)
         & = \pi \left( \frac{1}{\cos\theta} + \frac{1}{4}\cos\theta - \tan\theta + \theta - \frac{5}{4} \right)
\end{align*} である．$\cdots$(答)

\(3\) $t=\frac{\pi}{2}-\theta$ とおくと，$\theta \to \pi/2-0$
の時，$t \to +0$ である． (2) から，$V(\theta)$を$t$を使って書き直すと，
\begin{align*}
        V
         & = \pi \left( \frac{1}{\cos\left(\frac{\pi}{2}-t\right)} + \frac{1}{4}\cos\left(\frac{\pi}{2}-t\right) - \tan\left(\frac{\pi}{2}-t\right) + \frac{\pi}{2}-t - \frac{5}{4} \right) \\
         & = \pi \left( \frac{1}{\sin t} + \frac{1}{4}\sin t - \frac{1}{\tan t} + \frac{\pi}{2}-t - \frac{5}{4} \right)                                                                     \\
         & = \pi \left( \frac{1-\cos t}{\sin t} + \left(\frac{\pi}{2}-\frac{5}{4}\right) + \left(\frac{1}{4}\sin t - t\right) \right)                                                       \\
         & = \pi \left( \frac{t}{\sin t} \frac{1-\cos t}{t^2} t + \left(\frac{\pi}{2}-\frac{5}{4}\right) + \left(\frac{1}{4}\sin t - t\right) \right)
\end{align*} となる．$t \to +0$ の極限を取って， \begin{align*}
        \lim_{t \to +0} V
         & = \pi \left( 1 \cdot \frac{1}{2} \cdot 0 + 0 + \frac{\pi}{2}-\frac{5}{4} + 0 \right) \\
         & = \frac{\pi}{4}\left(2\pi-5\right)
\end{align*} である．$\cdots$(答)

**【解説】**
