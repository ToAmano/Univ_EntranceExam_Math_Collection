---
university: "titech"
category: "kouki"
year: "2000"
question: "1"
type: "solution"
title: "TITECH 2000 kouki Q1 (solution)"
---

## 【解】

  (1)
  $f(-a)=0$より，$f(x)$は$(x+a)$を因数に持ち，
  

$$
\begin{align*}
f(x)=(x+a)(x^2+(1-a)x+b)
\end{align*}
$$

  と書ける．これ以上の分解はできないため，これが答えである．  $\cdots$(答)

  
  (2)
  新しく
  

$$
\begin{align*}
g(x) = x^2+(1-a)x+b
\end{align*}
$$

  とおく．$f(x)$の三次の係数が正だから，$g(x)$の解の数によって関数$f(x)$の概形が[図1](#2000-1:fig:1)の4パターンに変化する．

  

<figure id="2000-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2000/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三次関数の解の個数とグラフの概形</figcaption>
</figure>

  $g(x)$の判別式$D$は
  

$$
\begin{align*}
D=(a-1)^2-4b
\end{align*}
$$

  である．$D\ge0$の時 $f(x)=0$は2実解 $\alpha, \beta$ (重解を含む)をもつ．これらの解が$-a$と等しい場合があるかを調べる．
  この時の解は
  

$$
\begin{align}
x = \frac{a-1 \pm \sqrt{(a-1)^2-4b}}{2}\label{2000-1:eq:2}
\end{align}
$$

  である．これが$-a$と等しいとき，
  

$$
\begin{align*}
-a      & = \frac{a-1 \pm \sqrt{(a-1)^2-4b}}{2}\\
    -3a + 1 & = \pm\sqrt{(a-1)^2-4b}
\end{align*}
$$

  両辺二乗して
  

$$
\begin{align}
& (-3a+1)^2 = (a-1)^2-4b   \nonumber\\& 9a^2-6a+1 = a^2-2a+1 -4b \nonumber\\& b = - 2a^2+a \label{2000-1:eq:3}
\end{align}
$$

  である．$D=0$との関係では，常に
  

$$
\begin{align*}
\frac{1}{4}(a-1)^2 \ge -2a^2+a
\end{align*}
$$

  が成り立つ．等号成立は$a=1/3$のときであり，
  この時，$b=1/9$であり，
  

$$
\begin{align*}
g(x)
     & = x^2+\frac{2}{3}x+\frac{1}{9}\\& = \left(x+\frac{1}{3}\right)^2
\end{align*}
$$

  と$x=-a$を重解を持つ．
  それ以外の時は，$g(x)$は$-a$およびそれと異なる解を持つ．
  以上の事実を念頭に以下場合わけを行う．

  

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2000/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $g(x)$の解の個数分布</figcaption>
</figure>

  以下場合わけをして考える．全体像は[表1](#2000-1:table:1)である．
  

<figure id="2000-1:table:1" class="table-wrapper">

| $f(x)$の解の数 | $g(x)$の条件                  |
|:----------------:|:--------------------------------|
|       3つ        | $x=-a$以外に異なる2実解を持つ |
|       2つ        | $x=-a$以外の重解を持つ        |
|       2つ        | $x=-a$とそれ以外に解を持つ    |
|       1つ        | 実数解なし                      |
|       1つ        | $x=-a$に重解を持つ            |

  <figcaption>表 1: 場合分けの全体像</figcaption>
</figure>

  

1.  $f(x)$が異なる三つの実数解を持つとき．\\
          この時は，$g(x)$が異なる二つの実数解を持つ，つまり$D>0$である．
          この時は$g(x)$の解が$-a$ではあり得ない．
          従って
          

$$
\begin{align*}
(a-1)^2-4b > 0 \\
\end{align*}
$$

          の時である．
          このもとで題意の条件を満たすには，$f(x)$の最も大きい解が$0$以下であれば良い．
          

$$
\begin{align*}
& \max(-a, \alpha, \beta) \le 0
\end{align*}
$$

          [(式2)](#2000-1:eq:2)より，求める条件は
          

$$
\begin{align*}
& \begin{dcases}
                 -a \le 0 \\
                 \frac{a-1 + \sqrt{(a-1)^2-4b}}{2} \le 0
               \end{dcases}\\\therefore& \begin{dcases}
                 -a \le 0 \\
                 \sqrt{(a-1)^2-4b} \le 1-a
               \end{dcases}\\\therefore& \begin{dcases}
                 -a \le 0  \\
                 1-a \le 0 \\
                 (a-1)^2-4b \le (1-a)^2
               \end{dcases}\\\therefore& \begin{dcases}
                 0 \le a \le 1 \\
                 0 \le b
               \end{dcases}
\end{align*}
$$

2.  $f(x)$が異なる二つの実数解を持つとき．\\
          この時は，$D=0$で$g(x)$の解が$-a$でないときか，$D>0$で$g(x)$の一つの解が$-a$となる($-a$が$f$の重解となる)ときである．
          前者の時は$D=0$より
          

$$
\begin{align*}
D = (a-1)^2 -4b = 0
\end{align*}
$$

          であり，この時の重解は $x = \frac{a-1}{2}$である．これが$-a$と一致しないことにより$a\neq 1/3$が必要．
          題意の条件は
          

$$
\begin{align*}
& -a \le 0 \\\therefore& a \ge 0
\end{align*}
$$

          である．

          後者の条件は，[(式3)](#2000-1:eq:3)より
          

$$
\begin{align*}
b & = - 2a^2+a        \\
            D & = (a-1)^2 -4b > 0
\end{align*}
$$

          であり，この時$g(x)$のもう一つの解は解と係数の関係から
          

$$
\begin{align*}
x = 2a - 1
\end{align*}
$$

          である．題意の条件はこれが$0$以下であることで
          

$$
\begin{align*}
& 2a-1 \le 0        \\& a \le\frac{1}{2}
\end{align*}
$$

          である．

3.  $f(x)$がただ一つの実数解を持つとき．\\
          これは$f(x)$が三重解を持つか，または$D<0$の時のときである．
          前者の時は$a=1/3$であり，この元で題意の条件は$-a \le 0$であるから，
          

$$
\begin{align*}
\begin{dcases}
              (a-1)^2 -4b = 0 \\
              a = \frac{1}{3}
            \end{dcases}
\end{align*}
$$

          となる．

          後者の時は$D<0$かつ$-a \le 0$であればよく，
          

$$
\begin{align*}
\begin{dcases}
              (a-1)^2 -4b < 0 \\
              a \ge 0
            \end{dcases}
\end{align*}
$$

  以上をまとめると，以下の4つの条件となる．
  

$$
\begin{align*}
\begin{dcases}
      (a-1)^2-4b > 0, 0 \le a \le 1, 0 \le b          \\
      (a-1)^2 -4b > 0, b = - 2a^2+a, a\le \frac{1}{2} \\
      (a-1)^2 -4b = 0, a \ge 0                        \\
      (a-1)^2 -4b < 0 ,      a \ge 0                  \\
    \end{dcases}
\end{align*}
$$

  これを整理して
  

$$
\begin{align*}
\begin{dcases}
      b = - 2a^2+a            & a < 0         \\
      0 \le b                 & 0 \le a \le 1 \\
      b \ge \frac{(a-1)^2}{4} & 1 < a
    \end{dcases}
\end{align*}
$$

  である．
  $ab$平面にこの条件を図示すれば，[図3](#2000-1:fig:3)の斜線部が求める答えである．
  ただし，実線部および境界を含む．

  

<figure id="2000-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2000/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 求める$(a,b)$の領域は斜線部（境界含む）と，実線部分である．</figcaption>
</figure>

  $\cdots$(答)

  
  

## 【解説】

  方程式および多変数関数の問題．(1)は色々試せば$-a$を因数として持つことがわかるのですぐに答えを導ける．
  本題は(2)の方で，三次関数$f(x)$の形の違いによって求める題意の条件が異なるので，場合わけによる正確な処理が求められる．
  特に注意しないといけないのは$g(x)$の解が$-a$となるかどうかという点である．
  この場合は$x=-a$の方で重解を持つことになるので，$g(x)$が重解を持つのとは別のパターンとして処理が必要である．
  結果的に[表1](#2000-1:table:1)のように5パターンの場合わけを処理すれば解答に辿り着ける．

  簡単な検算としては，$f(0)=ab$で，これが条件より$0$以上なので$ab\ge 0$であり，
  最後の[図3](#2000-1:fig:3)はこの条件を満たしているのでぱっと見大丈夫そうなのが確認できる．