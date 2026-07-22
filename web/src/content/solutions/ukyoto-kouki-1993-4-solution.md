---
university: "ukyoto"
category: "kouki"
year: "1993"
question: "4"
type: "solution"
title: "UKYOTO 1993 kouki Q4 (solution)"
---

## 【解】

  $f(x) = a^x - ax$ とおく．$x>0$ に対し $f(x)>0$ となるための条件を求めれば良い．
  ただし，題意より
  

$$
\begin{align*}
a > 0
\end{align*}
$$

  である．
  $0 < a \le 1$ とすると $f(x) \to -\infty$ ($x \to \infty$) から不適．
  従って
  

$$
\begin{align}
1 < a \label{1993-4:eq:3}
\end{align}
$$

  として考える．

  $f'(x)$の一階微分は
  

$$
\begin{align*}
f'(x) = a \left[ a^{x-1}\log a - 1 \right]
\end{align*}
$$

  だから，$f'(x)=0$の解は
  

$$
\begin{align*}
a^{\alpha-1} = \frac{1}{\log a}
\end{align*}
$$

  なる$\alpha$である．$a>1$よりこの両辺は正なので自然対数をとって，
  

$$
\begin{align}
(\alpha-1) \log a & = - \log(\log a)                                     \\\alpha& = 1 - \frac{\log(\log a)}{\log a}\label{1993-4:eq:1}
\end{align}
$$

  $f(x)$の増減表は[表1](#1993-4:table:1)となる．

  

<figure id="1993-4:table:1" class="table-wrapper">

| $x$  | $0$ |  $\cdots$  | $\alpha$ |              |
|:------:|:-----:|:------------:|:----------:|:------------:|
| $f'$ |       |    $-$     |   $0$    |    $+$     |
| $f$  |       | $\searrow$ |            | $\nearrow$ |

  <figcaption>表 1: $f(x)$の増減表</figcaption>
</figure>

  従って，題意の条件を満たすには $f(\alpha) \ge 0$ ならば良い．
  

$$
\begin{align*}
f(\alpha)
     & = a\left[a^{\alpha-1}-\alpha\right]\\& = \frac{1}{\log a} -\alpha
\end{align*}
$$

  だから，
  

$$
\begin{align*}
& f(\alpha) \ge 0              \\
    iff & \alpha\le\frac{1}{\log a }
\end{align*}
$$

  [(式1)](#1993-4:eq:1)を代入して
  

$$
\begin{align*}
& 1 - \frac{\log(\log a)}{\log a}\le\frac{1}{\log a }\\& \log\frac{a}{\log a }\le 1
\end{align*}
$$

  なる条件を得る．

  $\log x$ は $x$ について単調増加なので，$\log e = 1$に注意して$\log$を外して
  

$$
\begin{align*}
& \frac{a}{\log a}\le  e \\\therefore& e\log a -a \ge 0
\end{align*}
$$

  となる．以下この条件を満たすような$a$を求めるため，
  

$$
\begin{align*}
g(a) = e\log a -a
\end{align*}
$$

  とおくと，$g(a)\ge 0$となる$a$を求めれば良い．
  一階微分は
  

$$
\begin{align*}
g'(a) = \frac{e}{a} -1
\end{align*}
$$

  だから，$g(x)$の増減表は[表2](#1993-4:table:2)となる．

  

<figure id="1993-4:table:2" class="table-wrapper">

| $a$  | $1$ |              | $e$ |              |
|:------:|:-----:|:------------:|:-----:|:------------:|
| $g'$ |       |    $+$     |       |    $-$     |
| $g$  |       | $\nearrow$ | $0$ | $\searrow$ |

  <figcaption>表 2: $g(x)$の増減表</figcaption>
</figure>

  従って，$g(a) \ge 0$を満たす $a$ は $a=e$のみであり，これは[(式3)](#1993-4:eq:3)を満たすから，
  求める$a$は
  

$$
\begin{align*}
a = e
\end{align*}
$$

  である． $\cdots$(答)

  

## 【解説】

  解答ではかなり素直に関数を微分して条件を満たす$a$を求めに行ったが，よりショートカットも可能ある．
  題意の条件
  

$$
\begin{align*}
a^x \ge ax
\end{align*}
$$

  が任意の$x\ge 0$で満たすような$a$を探せば良い．$a>0$よりこの両辺は正なので$a$を底とする対数をとって
  

$$
\begin{align*}
x-1 \ge\log_a x
\end{align*}
$$

  となるから，
  

$$
\begin{align*}
h(x) = x-1 - \log_a x
\end{align*}
$$

  の増減表を書いて$h(x)\ge 0$となる条件を求めにいけば良い．