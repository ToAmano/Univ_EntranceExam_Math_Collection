---
university: "ukyoto"
category: "kouki"
year: "1995"
question: "6"
type: "solution"
title: "UKYOTO 1995 kouki Q6 (solution)"
---

## 【解】

    (1)

    

<figure id="1995-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1995/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 題意の状況</figcaption>
</figure>

    $x=t\,(t>0)$の$C$の接線は
    

$$
\begin{align}
y=-\frac{1}{t^2}x+\frac{2}{t}\label{1995-6:eq:1}
\end{align}
$$

    である．
    これが$A$を通る時，
    

$$
\begin{align*}
& 0 = -\frac{1}{t^2}a+\frac{2}{t}\\\therefore& t = \frac{a}{2}\quad(\because t>0)
\end{align*}
$$

    を満たすから，
    [(式1)](#1995-6:eq:1)に代入して
    

$$
\begin{align*}
L_a : y
         & = f_{a}\\& = -\frac{4}{a^2}x+\frac{4}{a}
\end{align*}
$$

    である．

    次に，直線RQの方程式は
    

$$
\begin{align}
& RQ:y=-\frac{1}{2}x+2  \label{1995-6:eq:2}
\end{align}
$$

    と表せるから，RQと$L_a$の交点の$x$座標$x_0$は
    

$$
\begin{align*}
& -\frac{4}{a^2}x_0+\frac{4}{a} = -\frac{1}{2}x_0+2 \\& (\frac{1}{2}-\frac{4}{a^2})x = 2-\frac{4}{a}
\end{align*}
$$

    の解である．$a \neq 2\sqrt{2}$のもとでこれを解いて
    

$$
\begin{align}
x_0 & = \frac{2-4/a}{1/2-4/a^2}\\& = \frac{4a(a-2)}{a^2-8}\label{1995-6:eq:3}
\end{align}
$$

    を得る．この時$y$座標は
    

$$
\begin{align}
y_0  =  \frac{4(a-4)}{a^2-8}\label{1995-6:eq:4}
\end{align}
$$

    である．

    従って，$0<a<4$および$a \neq 2\sqrt{2}$のもとで，
    題意の条件は
    

$$
\begin{align*}
\begin{dcases}
            x_0 > 0 \\
            y_0 > 0
        \end{dcases}\\\therefore\begin{dcases}
            \frac{4a(a-2)}{a^2-8} > 0 \\
            \frac{4(a-4)}{a^2-8} > 0
        \end{dcases}\\\therefore
        0 < a < 2
\end{align*}
$$

    である．$\cdots$(答)

    

    (2)
    (1)で求めた条件$0<a<2$のもとでとかんがえる．
    $T,S_1,S_2$は
    

$$
\begin{align*}
T+S_1 & = \triangle ORQ = \frac{1}{2}\cdot 2 \cdot 4 = 4           \\
        T+S_2 & = \triangle OAB = \frac{1}{2}\cdot a \cdot\frac{4}{a} = 2
\end{align*}
$$

    と書けるから，
    $S_1 = 4-T$, $S_2 = 2-T$なので，$r$および$m$は$T$を用いて
    

$$
\begin{align}
r
         & = S_1+S_2                     \\& = (4-T)+(2-T)                 \\& = 6-2T    \label{1995-6:eq:5}\\
        m
         & = S_1S_2                      \\& = (4-T)(2-T)                  \\
\end{align}
$$

    となる．
    ここから$T$を除去して
    

$$
\begin{align}
m
         & = \frac{1}{4}(r+2)(r-2)                  \\& = \frac{1}{4}(r^2-4) \label{1995-6:eq:6}
\end{align}
$$

    である．

    以下$T$の値域を求めることで$r$の値域を求める．
    図および [(式4)](#1995-6:eq:3,1995-6:eq:4)から
    

$$
\begin{align*}
T
         & = \triangle OAM + \triangle OQM              \\& = \frac{1}{2}a y_0 + \frac{1}{2}\cdot 2 x_0 \\& = \frac{2 x_0 + ay_0 }{2}\\& = \frac{4a(3a-8)}{2(a^2-8)}\\& = 2\left[3 + \frac{8(-3+a)}{8-a^2}\right]
\end{align*}
$$

    である．
    分母は$a$について単調減少，分子は$a$について単調増加だから，
    全体として$T$は$a$について単調増加であり，$0<a<2$のもとで
    

$$
\begin{align*}
& \lim_{a\to 0}T <T <\lim_{a\to 2} T \\& 0<T<2
\end{align*}
$$

    であり，この時[(式5)](#1995-6:eq:5)より
    

$$
\begin{align}
2<r<6 \label{1995-6:eq:7}
\end{align}
$$

    である．

    従って求めるべき条件は[(式7)](#1995-6:eq:6,1995-6:eq:7)であり，
    図示して[図2](#1995-6:fig:2)となる．$\cdots$(答)

    

<figure id="1995-6:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1995/6/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $(r,m)$の存在領域．白丸点は含まず．</figcaption>
</figure>

    
    

## 【解説】