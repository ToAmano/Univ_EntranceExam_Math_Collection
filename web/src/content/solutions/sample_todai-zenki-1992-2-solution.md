---
university: "sample_todai"
category: "zenki"
year: "1992"
question: "2"
type: "solution"
title: "SAMPLE_TODAI 1992 zenki Q2 (solution)"
---

::: oframed
:::

::: multicols
2 **\[解\]**

\(1\)

<figure id="1992-2:fig:1" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai-zenki-1992-2_tikz_1.svg" />
<figcaption>平面<span
class="math inline">\(H_1,H_2\)</span>の様子．</figcaption>
</figure>

$L$を$x$軸, $H_1$を$xy$平面, Bを原点とし,
$H_2$が$z \geqq 0$になるように空間座標をおく．
$H_1$と$H_2$のなす角を$\theta$とおく．
$C$から$L$に下ろした垂足を$C'$とし，その座標をC'($p, 0, 0$)とする．

$CC' = q (q>0)$ とおくと， $$\begin{align*}
    C(p, q\cos\theta, q\sin\theta)
\end{align*}$$ とおける．

さらに A($a, b, 0$) ($b>0$) とおくと，$\overline{AC}$の長さは
$$\begin{align*}
    \overline{AC}^2
     & = (a-p)^2 + (b-q\cos\theta)^2 + q^2\sin^2\theta \\
     & = -2bq\cos\theta + q^2+b^2+(a-p)^2
\end{align*}$$ と書ける．

さて，$\angle ABC=\alpha\, (0 \le \alpha \le \pi)$とおいて$\triangle ABC$に余弦定理を用いると
$$\begin{align*}
    \cos\alpha
     & = \frac{\overline{AB}^2+\overline{BC}^2-\overline{AC}^2}{2\overline{AB} \cdot \overline{BC}}                                                              \\
     & = \frac{\overline{AB}^2+\overline{BC}^2}{2\overline{AB} \cdot \overline{BC}} + \frac{2bq\cos\theta - q^2-b^2-(a-p)^2}{2\overline{AB} \cdot \overline{BC}}
\end{align*}$$ と書ける．

$\theta$の変化によって$\overline{AB}, \overline{BC}$は変化しないから，
$$\begin{align*}
    \cos\alpha
     & = (\text{定数})  + \frac{bq}{\overline{AB} \cdot \overline{BC}} \cos\theta
\end{align*}$$ と書ける．

従って，$0 \leqq \theta \leqq \pi$で$\cos\theta$は単調減少で，$\frac{bq}{AB \cdot BC} > 0$から
$\cos\alpha$は$\theta$の単調減少関数である．
$0 \leqq \alpha \leqq \pi$とあわせて$\alpha$は$\theta$の単調増加関数である．
よって題意は示された．$\cdots$(答)

\(2\)

どの点が同一直線上にあるかで場合分けして考える．

**1° A,B,C,Dが同一直線上の時**

<figure id="1992-2:fig:2" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai-zenki-1992-2_tikz_2.svg" />
<figcaption>1° A,B,C,Dが同一直線上の時</figcaption>
</figure>

対称性から[2](#1992-2:fig:2){reference-type="ref+label"
reference="1992-2:fig:2"}の時だけ考える． $$\begin{align*}
    \angle ABC + \angle BCD + \angle CDA + \angle DAB = 2\pi
\end{align*}$$ だから与式は成立する．

**2° AからDのうち3つが同一直線上の時**

<figure id="1992-2:fig:3" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai-zenki-1992-2_tikz_3.svg" />
<figcaption>2° AからDのうち3つが同一直線上の時</figcaption>
</figure>

対称性から図の時だけ考える． $$\begin{align*}
    \angle ABC + \angle BCD + \angle CDA + \angle DAB = \pi + \pi = 2\pi
\end{align*}$$ だから与式は成立する．

**3° どの3点も同一直線上にない時**

<figure id="1992-2:fig:4" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai-zenki-1992-2_tikz_4.svg" />
<figcaption>3° どの3点も同一直線上にない時</figcaption>
</figure>

直線ACをLとしてLを共通の境界とし，角$\theta(0 \leqq \theta \leqq \pi)$で交わる
2半平面$H_1$, $H_2$上のLと異なる所に各々点B, Dをとることが出来る．

この時$3$点(B,C,D), (A,B,D)に(1)の議論を用いることが出来る．
まず平面$H_1,H_2$上でA,B,C,Dを固定して$\theta$を$0 \leqq \theta \leqq \pi$で動かす．
この時 $\angle ABC$, $\angle CDA$は一定で，(1)から $\angle DAB$,
$\angle BCD$は$\theta$の単調増加関数だから
$\angle ABC + \angle BCD + \angle CDA + \angle DAB$は$\theta=\pi$で最大値をとる．
この時4点A,B,C,Dはどの3点も同一直線上にないことから四角形ABCDを構成する．
この時直線ACに関してB,
Dが反対側にあることから各点の関係は[5](#1992-2:fig:5){reference-type="ref+label"
reference="1992-2:fig:5"}のようになる．

<figure id="1992-2:fig:5" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_todai-zenki-1992-2_tikz_5.svg" />
<figcaption>点ABCDの関係</figcaption>
</figure>

よって条件をみたすもとでA〜Dをうごかしても，四角形の内角の和は$2\pi$で一定だから
$$\begin{align*}
    \angle ABC + \angle BCD + \angle CDA + \angle DAB = 2\pi
\end{align*}$$ よって与式は成立する．

以上1°〜3°で全ての場合は尽くされ，題意は示された．$\cdots$(答)

**\[解説\]**
:::
