---
university: "todai"
category: "kouki"
year: "2005"
question: "3"
type: "solution"
title: "TODAI 2005 kouki Q3 (solution)"
---

## 【解】

  (1)

  

<figure id="2005-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2005/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $D$と$E$の領域．</figcaption>
</figure>

  $x^2+y^2=1$と$x^2+y^2=4$の円の$x$の値域に注意して場合分けすると
  

$$
\begin{align*}
& S_a =                                                                                              \\& \begin{dcases}
         2 \int_0^{a+1} \sqrt{4-x^2} \, dx - 2 \int_0^{a+1} \sqrt{1-x^2} \, dx & (-\frac{1}{2} \le a \le 0) \\
         2 \int_0^{a+1} \sqrt{4-x^2} \, dx - 2 \int_0^{1} \sqrt{1-x^2} \, dx   & (0 \le a \le 1)            \\
         2 \int_0^{2} \sqrt{4-x^2} \, dx                                       & (1 \le a \le 2)
       \end{dcases}
\end{align*}
$$

  である．  $\cdots$(答)

  
  (2)
  $S(a)$は連続的に変化するので，場合分けの各区間内で$S(a)$は微分可能であり
  

$$
\begin{align*}
& S'(a) =                                                                                                                                      \\& \begin{dcases}
         2\left[\sqrt{4-(a+1)^2} - \sqrt{4-a^2} - \sqrt{1-(a+1)^2} + \sqrt{1-a^2}\right] & (-\frac{1}{2} \le a \le 0) \\
         2\left[\sqrt{4-(a+1)^2} - \sqrt{4-a^2} + \sqrt{1-a^2}\right]                    & (0 \le a \le 1)            \\
         -2\sqrt{4-a^2}                                                                  & (1 \le a \le 2)
       \end{dcases}
\end{align*}
$$

  である．$\cdots$(答)

  
  (3)
  (2)の結果より，$1\le a \le 2$では$S'(a)\le 0$だから，$S(a)$の最大値は
  

$$
\begin{align*}
-\frac{1}{2}\le a \le 1
\end{align*}
$$

  で取る．

  次に$-\frac{1}{2}\le a \le 0$の時を考える．
  

$$
\begin{align*}
f(x) = \sqrt{4-x^2} - \sqrt{1-x^2}
\end{align*}
$$

  とおくと，(2)の結果より
  

$$
\begin{align*}
S'(a) = 2\left[f(a+1)-f(a)\right]
\end{align*}
$$

  である．
  一方で$f(x)$は変形して
  

$$
\begin{align*}
f(x) = \frac{3}{\sqrt{4-x^2}\sqrt{1-x^2}}
\end{align*}
$$

  と書けるから，$f(x)$は偶関数でありかつ$0 \le x$で単調増加である．

  

<figure id="2005-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2005/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $y=f(x)$のグラフ</figcaption>
</figure>

  従って，$-\frac{1}{2} \le a \le 0$で
  

$$
\begin{align*}
& f(a+1) \ge f(a) \\\therefore& S'(a) \ge 0
\end{align*}
$$

  である．すなわちこの区間で$S'(a)$は単調増加である．

  よって$S(a)$の最大値は
  

$$
\begin{align*}
0 \le a \le 1
\end{align*}
$$

  でとる．この時(2)から
  

$$
\begin{align*}
S'(a) = 2 \left[\sqrt{4-(a+1)^2}-f(a)\right]
\end{align*}
$$

  である．この区間で$\sqrt{4-(a+1)^2}$は単調減少，$f(a)$は単調増加だから，
  全体として$S'(a)$は単調減少である．
  これと端点で
  

$$
\begin{align*}
S(1) & = -2\sqrt{3} < 0    \\
    S(0) & = 2(\sqrt{3}-1) > 0
\end{align*}
$$

  より，$S(a_0)=0$ なる$a_0$が唯1つあって，$f(a)$の増減表は[表1](#2005-3:table:1)となる．

  

<figure id="2005-3:table:1" class="table-wrapper">

| $a$ | $-\frac{1}{2}$ |  | $0$ |  | $a_0$ |  | $1$ |  | $2$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $S'$ | $0$ | $+$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ | $0$ |
| $S$ |  | $\nearrow$ |  | $\nearrow$ | $\text{max}$ | $\searrow$ |  | $\searrow$ |  |

  <figcaption>表 1: $f(a)$の増減表．</figcaption>
</figure>

  よって$a=a_0$で最大であるから，これをみたす4次式をつくれば良い．
  $S'(a)=0$より
  

$$
\begin{align*}
\sqrt{4-(a+1)^2} = \sqrt{4-a^2} - \sqrt{1-a^2}
\end{align*}
$$

  両辺 $0$以上だから2乗してよく
  

$$
\begin{align*}
& 4-(a+1)^2 = 5-2a^2 - 2\sqrt{(1-a^2)(4-a^2)}\\\therefore& 2\sqrt{(1-a^2)(4-a^2)} = -a^2+2a+2
\end{align*}
$$

  である．
  $0\le a \le 1$の時$-a^2+2a+2>0$ だから両辺 $0$以上だから2乗して
  

$$
\begin{align*}
& 4(1-a^2)(4-a^2) = (-a^2+2a+2)^2    \\& 4(a^4-5a^2+4) = a^4-4a^3-4a^2+8a+4 \\& 3a^4+4a^3-20a^2-8a+12=0
\end{align*}
$$

  この方程式は四次係数が$3$でそれ以下の係数も全て整数であり，題意の条件を満たす．
  よって$a$を$x$で置き換えて求める四次方程式は
  

$$
\begin{align}
3x^4+4x^3-16x^2-8x+12=0 \label{2005-3:eq:1}
\end{align}
$$

  である．  $\cdots$(答)

  
  (4)
  $x = \sqrt{2}t$として[(式1)](#2005-3:eq:1)に代入して
  

$$
\begin{align*}
12t^4 + 8\sqrt{2}t^3 - 40t^2 - 8\sqrt{2}t + 12 = 0
\end{align*}
$$

  $t=0$は解でないので両辺$t^2$で割って
  

$$
\begin{align*}
& 12\left(t^2+\frac{1}{t^2}\right) + 8\sqrt{2}\left(t-\frac{1}{t}\right) - 40 = 0              \\\therefore& 12\left[\left(t-\frac{1}{t}\right)^2+2\right] + 8\sqrt{2}\left(t-\frac{1}{t}\right) - 40 = 0
\end{align*}
$$

  である．
  $ z = t-1/t$ とおいて代入すると，
  

$$
\begin{align}
& 12(z^2+2) + 8\sqrt{2}z - 40 = 0               \\& 3z^2 + 2\sqrt{2}z - 4 = 0 \label{2005-3:eq:2}
\end{align}
$$

  が求める二次方程式である． $\cdots$(答)

  
  (5)
  $t=\sqrt{2}a$及び$z=t-1/t$より，
  

$$
\begin{align*}
z = \frac{a}{\sqrt{2}} - \frac{\sqrt{2}}{a}
\end{align*}
$$

  である．
  (3)より求める$a$は$0 < a < 1$に存在するが，この領域では$z<0$である．

  

<figure id="2005-3:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2005/3/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $z$のグラフ</figcaption>
</figure>

  $z$は[(式2)](#2005-3:eq:2)の解で
  

$$
\begin{align*}
z = \frac{1}{3}\left(-\sqrt{2}\pm\sqrt{14}\right)
\end{align*}
$$

  だが，$z<0$より複号負を採用して
  

$$
\begin{align*}
z
     & = \frac{1}{3}\left(-\sqrt{2} - \sqrt{14}\right)\\& = \frac{a}{\sqrt{2}} - \frac{\sqrt{2}}{a}
\end{align*}
$$

  である．
  両辺に$a$をかけて整理すると
  

$$
\begin{align*}
& \frac{1}{2}a^2 + \frac{1}{3}\left(1+\sqrt{7}\right)a -1 = 0      \\\therefore& a = - \frac{1}{3}(1+\sqrt{7}) \pm\frac{1}{3}\sqrt{26+2\sqrt{7}}
\end{align*}
$$

  を得る．
  $a>0$より複号正を採用して，求める$a$は
  

$$
\begin{align*}
a_0
     & = -\frac{1}{3}(1+\sqrt{7}) + \frac{1}{3}\sqrt{26+2\sqrt{7}}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】