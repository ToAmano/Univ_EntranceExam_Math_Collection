---
university: "ukyoto"
category: "kouki"
year: "1990"
question: "1"
type: "solution"
title: "UKYOTO 1990 kouki Q1 (solution)"
---

## 【解】

  $f(x) = x^4 - 6x^2$ とおくと，$f(x)$は偶関数で，曲線
  

$$
\begin{align*}
C: y = f(x)
\end{align*}
$$

  の様子は[図1](#1990-1:fig:1)である．

  

<figure id="1990-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1990/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=f(x)$の様子</figcaption>
</figure>

  $f'(x) = 4x^3 - 12x$ だから，$x=t$ における接線は
  

$$
\begin{align*}
l: y
     & = (4t^3 - 12t) (x-t) + t^4 - 6t^2           \\& = (4t^3 - 12t)x - 4t^4 + 12t^2 + t^4 - 6t^2 \\& = (4t^3 - 12t)x - 3t^4 + 6t^2
\end{align*}
$$

  である．これが $(a,b)$ を通る時
  

$$
\begin{align*}
& b = (4t^3 - 12t)a - 3t^4 + 6t^2                \\\therefore& 0 = 3t^4 - 4at^3 - 6t^2 + 12at + b \equiv g(t)
\end{align*}
$$

  である．グラフより，$y=f(x)$は$t=\pm\sqrt{3}$でのみ二重接線を持つから，
  題意の条件は，四次方程式$g(t)=0$が
  

$$
\begin{align}
t\neq\pm\sqrt{3}\label{1990-1:eq:1}
\end{align}
$$

  に四つの異なる実数解を持つことと同値である．
  そこで以下この条件を調べる．
  まず，[(式1)](#1990-1:eq:1)より
  

$$
\begin{align}
& b \neq f(\pm\sqrt{3})       \\\therefore& b \neq -9\label{1990-1:eq:2}
\end{align}
$$

  である．

  次に，$g(x)$の増減表を書くことで，$g(t)=0$の解の個数を考察する．
  まず$g(x)$の一階微分は
  

$$
\begin{align*}
g'(t)
     & = 12t^3 - 12at^2 - 12t + 12a \\& = 12 (t^3 - at^2 - t + a)    \\& = 12 (t^2(t-a) - (t-a))      \\& = 12 (t-a) (t^2 - 1)         \\& = 12 (t-a) (t+1) (t-1)
\end{align*}
$$

  だから，$a$によって以下のような増減表を得る．

  

1.  $a < -1$
          \[
            \begin{array}{|c||c|c|c|c|c|c|c|}
              \hline
              t  &          & a &          & -1 &          & 1 &          \\
              \hline
              g' & -        & 0 & +        & 0  & -        & 0 & +        \\
              \hline
              g  & \searrow &   & \nearrow &    & \searrow &   & \nearrow \\
              \hline
            \end{array}
          \]

2.  $-1 < a < 1$
          \[
            \begin{array}{|c||c|c|c|c|c|c|c|}
              \hline
              t  &          & -1 &          & a &          & 1 &          \\
              \hline
              g' & -        & 0  & +        & 0 & -        & 0 & +        \\
              \hline
              g  & \searrow &    & \nearrow &   & \searrow &   & \nearrow \\
              \hline
            \end{array}
          \]

3.  $1 < a$
          \[
            \begin{array}{|c||c|c|c|c|c|c|c|}
              \hline
              t  &          & -1 &          & 1 &          & a &          \\
              \hline
              g' & -        & 0  & +        & 0 & -        & 0 & +        \\
              \hline
              g  & \searrow &    & \nearrow &   & \searrow &   & \nearrow \\
              \hline
            \end{array}
          \]

4.  $a=\pm 1$ の時
          \text{$g$は単調増加関数となり不適}

  よって，$g(t)=0$が四つの異なる実解を持つ条件は
  

$$
\begin{align*}
\begin{dcases}
      a < -1     & g(a)<0, g(-1)>0, g(1)<0 \\
      -1 < a < 1 & g(-1)<0, g(a)>0, g(1)<0 \\
      1 < a      & (-1)>0, g(a)<0, g(1)>0
    \end{dcases}
\end{align*}
$$

  である．$g$の値は
  

$$
\begin{align*}
g(a)  & = -a^4 + 6a^2 + b \\
    g(1)  & = 8a-3+b          \\
    g(-1) & = -8a-3+b
\end{align*}
$$

  だから，[(式2)](#1990-1:eq:2)と合わせて図示すると[図2](#1990-1:fig:2)斜線部（$b=-9$, 境界は除く）が求める条件である．$\cdots$(答)

  

<figure id="1990-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1990/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 求めた$(a,b)$の領域（斜線部，ただし境界および$b=-9$は除く．</figcaption>
</figure>

  
  

## 【解説】