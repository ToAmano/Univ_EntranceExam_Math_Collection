---
university: "sample_titech"
category: "kouki"
year: "2000"
question: "1"
type: "solution"
title: "SAMPLE_TITECH 2000 kouki Q1 (solution)"
---

<div class="oframed">

</div>

<div class="multicols">
**【解】**

$1$ $`f$-a$=0`$より，$`f$x$`$は$`$x+a$`$を因数に持ち，
``` math

$$
\begin{aligned}
f$x$=$x+a$$x^2+(1-a$x+b)
\end{aligned}
$$

```
と書ける．これ以上の分解はできないため，これが答えである．
$`\cdots`$$答$

$2$ 新しく
``` math

$$
\begin{aligned}
g$x$ = x^2+$1-a$x+b
\end{aligned}
$$

```
とおく．$`f$x$`$の三次の係数が正だから，$`g$x$`$の解の数によって関数$`f$x$`$の概形が<a href="#2000-1:fig:1" data-reference-type="ref+label"
data-reference="2000-1:fig:1">1</a>の4パターンに変化する．

<figure id="2000-1:fig:1" data-latex-placement="H">
<div class="subcaptionblock">
<p><span>0.5</span> <img
src="/Math-Solutions/images/tikz/sample_titech/kouki/2000/1/fig_1.svg"
alt="image" /></p>
</div>
<div class="subcaptionblock">
<p><span>0.5</span> <img
src="/Math-Solutions/images/tikz/sample_titech/kouki/2000/1/fig_2.svg"
alt="image" /></p>
</div>
<div class="subcaptionblock">
<p><span>0.5</span> <img
src="/Math-Solutions/images/tikz/sample_titech/kouki/2000/1/fig_3.svg"
alt="image" /></p>
</div>
<div class="subcaptionblock">
<p><span>0.5</span> <img
src="/Math-Solutions/images/tikz/sample_titech/kouki/2000/1/fig_4.svg"
alt="image" /></p>
</div>
<figcaption>三次関数の解の個数とグラフの概形</figcaption>
</figure>

$`g$x$`$の判別式$`D`$は
``` math

$$
\begin{aligned}
D=$a-1$^2-4b
\end{aligned}
$$

```
である．$`D\ge0`$の時 $`f$x$=0`$は2実解 $`\alpha, \beta`$
$重解を含む$をもつ．これらの解が$`-a`$と等しい場合があるかを調べる．
この時の解は
``` math

$$
\begin{aligned}
x = \frac{a-1 \pm \sqrt{$a-1$^2-4b}}{2}
\end{aligned}
$$

```
である．これが$`-a`$と等しいとき，
``` math

$$
\begin{aligned}
-a      & = \frac{a-1 \pm \sqrt{$a-1$^2-4b}}{2} \\
    -3a + 1 & = \pm \sqrt{$a-1$^2-4b}
\end{aligned}
$$

```
両辺二乗して
``` math

$$
\begin{aligned}
& $-3a+1$^2 = $a-1$^2-4b    \\
     & 9a^2-6a+1 = a^2-2a+1 -4b  \\
     & b = - 2a^2+a
\end{aligned}
$$

```
である．$`D=0`$との関係では，常に
``` math

$$
\begin{aligned}
\frac{1}{4}$a-1$^2 \ge -2a^2+a
\end{aligned}
$$

```
が成り立つ．等号成立は$`a=1/3`$のときであり， この時，$`b=1/9`$であり，
``` math

$$
\begin{aligned}
g$x$
     & = x^2+\frac{2}{3}x+\frac{1}{9} \\
     & = \left$x+\frac{1}{3}\right$^2
\end{aligned}
$$

```
と$`x=-a`$を重解を持つ．
それ以外の時は，$`g$x$`$は$`-a`$およびそれと異なる解を持つ．
以上の事実を念頭に以下場合わけを行う．

<figure data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_titech/kouki/2000/1/fig_5.svg" />
<figcaption><span
class="math inline">$g(x$\)</span>の解の個数分布</figcaption>
</figure>

以下場合わけをして考える．全体像は<a href="#2000-1:table:1" data-reference-type="ref+label"
data-reference="2000-1:table:1">1</a>である．

| $`f$x$`$の解の数 | $`g$x$`$の条件                  |
|:----------------:|:--------------------------------|
|       3つ        | $`x=-a`$以外に異なる2実解を持つ |
|       2つ        | $`x=-a`$以外の重解を持つ        |
|       2つ        | $`x=-a`$とそれ以外に解を持つ    |
|       1つ        | 実数解なし                      |
|       1つ        | $`x=-a`$に重解を持つ            |

場合分けの全体像 {#2000-1:table:1}

<span id="2000-1:table:1" data-label="2000-1:table:1"></span>

1.  $`f$x$`$が異なる三つの実数解を持つとき．\
    この時は，$`g$x$`$が異なる二つの実数解を持つ，つまり$`D>0`$である．
    この時は$`g$x$`$の解が$`-a`$ではあり得ない． 従って
    ``` math
    
$$
\begin{aligned}
$a-1$^2-4b > 0 \\
\end{aligned}
$$

    ```
    の時である．
    このもとで題意の条件を満たすには，$`f$x$`$の最も大きい解が$`0`$以下であれば良い．
    ``` math
    
$$
\begin{aligned}
& \max$-a, \alpha, \beta$ \le 0
\end{aligned}
$$

    ```
    <a href="#$式2, 式2, 式2$^2-4b}}{2} \le 0
                   \end{dcases} \\
                \therefore
                 & \begin{dcases}
                     -a \le 0 \\
                     \sqrt{$a-1$^2-4b} \le 1-a
                   \end{dcases}                    \\
                \therefore
                 & \begin{dcases}
                     -a \le 0  \\
                     1-a \le 0 \\
                     $a-1$^2-4b \le $1-a$^2
                   \end{dcases}                       \\
                \therefore
                 & \begin{dcases}
                     0 \le a \le 1 \\
                     0 \le b
                   \end{dcases}
\end{aligned}
$$

    ```

2.  $`f$x$`$が異なる二つの実数解を持つとき．\
    この時は，$`D=0`$で$`g$x$`$の解が$`-a`$でないときか，$`D>0`$で$`g$x$`$の一つの解が$`-a`$となる$$`-a`$が$`f`$の重解となる$ときである．
    前者の時は$`D=0`$より
    ``` math
    
$$
\begin{aligned}
D = $a-1$^2 -4b = 0
\end{aligned}
$$

    ```
    であり，この時の重解は
    $`x = \frac{a-1}{2}`$である．これが$`-a`$と一致しないことにより$`a\neq 1/3`$が必要．
    題意の条件は
    ``` math
    
$$
\begin{aligned}
& -a \le 0 \\
                \therefore
                 & a \ge 0
\end{aligned}
$$

    ```
    である．

    後者の条件は，<a href="#$式3, 式3, 式3$^2 -4b > 0
\end{aligned}
$$

    ```
    であり，この時$`g$x$`$のもう一つの解は解と係数の関係から
    ``` math
    
$$
\begin{aligned}
x = 2a - 1
\end{aligned}
$$

    ```
    である．題意の条件はこれが$`0`$以下であることで
    ``` math
    
$$
\begin{aligned}
& 2a-1 \le 0        \\
                 & a \le \frac{1}{2}
\end{aligned}
$$

    ```
    である．

3.  $`f$x$`$がただ一つの実数解を持つとき．\
    これは$`f$x$`$が三重解を持つか，または$`D<0`$の時のときである．
    前者の時は$`a=1/3`$であり，この元で題意の条件は$`-a \le 0`$であるから，
    ``` math
    
$$
\begin{aligned}
\begin{dcases}
                  $a-1$^2 -4b = 0 \\
                  a = \frac{1}{3}
                \end{dcases}
\end{aligned}
$$

    ```
    となる．

    後者の時は$`D<0`$かつ$`-a \le 0`$であればよく，
    ``` math
    
$$
\begin{aligned}
\begin{dcases}
                  $a-1$^2 -4b < 0 \\
                  a \ge 0
                \end{dcases}
\end{aligned}
$$

    ```

以上をまとめると，以下の4つの条件となる．
``` math

$$
\begin{aligned}
\begin{dcases}
      $a-1$^2-4b > 0, 0 \le a \le 1, 0 \le b          \\
      $a-1$^2 -4b > 0, b = - 2a^2+a, a\le \frac{1}{2} \\
      $a-1$^2 -4b = 0, a \ge 0                        \\
      $a-1$^2 -4b < 0 ,      a \ge 0                  \\
    \end{dcases}
\end{aligned}
$$

```
これを整理して
``` math

$$
\begin{aligned}
\begin{dcases}
      b = - 2a^2+a            & a < 0         \\
      0 \le b                 & 0 \le a \le 1 \\
      b \ge \frac{$a-1$^2}{4} & 1 < a
    \end{dcases}
\end{aligned}
$$

```
である．
$`ab`$平面にこの条件を図示すれば，<a href="#2000-1:fig:3" data-reference-type="ref+label"
data-reference="2000-1:fig:3">2</a>の斜線部が求める答えである．
ただし，実線部および境界を含む．

<figure id="2000-1:fig:3" data-latex-placement="H">
<img
src="/Math-Solutions/images/tikz/sample_titech/kouki/2000/1/fig_6.svg" />
<figcaption>求める<span
class="math inline">$(a,b$\)</span>の領域は斜線部（境界含む）と，実線部分である．</figcaption>
</figure>

$`\cdots`$$答$

**【解説】**
方程式および多変数関数の問題．$1$は色々試せば$`-a`$を因数として持つことがわかるのですぐに答えを導ける．
本題は$2$の方で，三次関数$`f$x$`$の形の違いによって求める題意の条件が異なるので，場合わけによる正確な処理が求められる．
特に注意しないといけないのは$`g$x$`$の解が$`-a`$となるかどうかという点である．
この場合は$`x=-a`$の方で重解を持つことになるので，$`g$x$`$が重解を持つのとは別のパターンとして処理が必要である．
結果的に<a href="#2000-1:table:1" data-reference-type="ref+label"
data-reference="2000-1:table:1">1</a>のように5パターンの場合わけを処理すれば解答に辿り着ける．

簡単な検算としては，$`f$0$=ab`$で，これが条件より$`0`$以上なので$`ab\ge 0`$であり，
最後の<a href="#2000-1:fig:3" data-reference-type="ref+label"
data-reference="2000-1:fig:3">2</a>はこの条件を満たしているのでぱっと見大丈夫そうなのが確認できる．

</div>
