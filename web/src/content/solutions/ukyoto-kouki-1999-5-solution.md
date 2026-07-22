---
university: "ukyoto"
category: "kouki"
year: "1999"
question: "5"
type: "solution"
title: "UKYOTO 1999 kouki Q5 (solution)"
---

## 【解】

    $x^2+ax+b=0$の解を$\alpha,\beta$とおく．
    題意より，
    

$$
\begin{align}
\alpha = u+\sqrt{3}v \label{1999-5:eq:1}
\end{align}
$$

    とおける．解と係数の関係から，
    

$$
\begin{align}
a & = -\alpha-\beta\label{1999-5:eq:2}\\
        b & = \alpha\beta\label{1999-5:eq:3}
\end{align}
$$

    である．

    [(式2)](#1999-5:eq:2)より
    

$$
\begin{align}
\beta = -u-a-\sqrt{3}v \label{1999-5:eq:4}
\end{align}
$$

    となる．[(式3)](#1999-5:eq:3)に代入して
    

$$
\begin{align*}
b
         & = (u+\sqrt{3}v)(-u-a-\sqrt{3}v) \\& = -u(u+a)-3v^2 -(a+2u)v\sqrt{3}
\end{align*}
$$

    となる．
    ここで$a,b,u,v$が有理数だから，この式が成立するには
    

$$
\begin{align*}
& (a+2u)v = 0         \\\therefore& a+2u = 0 \lor v = 0
\end{align*}
$$

    のどちらかが成立しないといけない．

    **$v \neq 0$の時**

    まず，$v\neq 0$の場合を考える．
    この場合
    

$$
\begin{align}
u = -\frac{a}{2}\label{1999-5:eq:6}
\end{align}
$$

    だから，$\alpha,\beta$は[(式4)](#1999-5:eq:1,1999-5:eq:4)より
    

$$
\begin{align*}
\alpha& = -\frac{a}{2} + \sqrt{3}v \\\beta& = -\frac{a}{2} - \sqrt{3}v \\
\end{align*}
$$

    となり，[(式3)](#1999-5:eq:3)は
    

$$
\begin{align}
12v^2 = a^2-4b \label{1999-5:eq:5}
\end{align}
$$

    となる．
    題意の条件$a,b\in\mathbb{Z}$より右辺は整数だから左辺も整数であり，
    有理数$v$を互いに素な整数$n,m$を用いて
    

$$
\begin{align*}
v = \frac{m}{n}
\end{align*}
$$

    と書くと，
    

$$
\begin{align*}
12\frac{m^2}{n^2}\in\mathbb{Z}
\end{align*}
$$

    が必要であり，12が$n^2$で割り切れることが条件である．
    従って$n=1 \lor 2$である．

    \begin{itemize}
        \item[$1^\circ$] $n=2$の時

              [(式5)](#1999-5:eq:5)に代入して
              

$$
\begin{align*}
3m^2 = a^2 - 4b
\end{align*}
$$

              である．ところが，両辺法$4$とする合同式をとると，$A \in \mathbb{Z}$とすれば$A^2 \equiv 0, 1 \pmod{4}$であるから，
              

$$
\begin{align*}
\text{左辺}\equiv 3m^2 \equiv 0, 3 \pmod{4}\\\text{右辺}\equiv a^2  \equiv 0, 1 \pmod{4}
\end{align*}
$$

              となり，両辺が等しいためには$3m^2\equiv a^2 \equiv 0$とならねばならない．
              $3$と$4$は互いに素だから，この時$m^2$が$4$で割り切れる，すなわち$m$が$2$で割り切れる．
              しかし，仮定より$n$と$m$は互いに素だからこれは矛盾．

        \item[$2^\circ$] $n=1$の時

              この時，$v$は整数である．
              [(式5)](#1999-5:eq:5)に代入して
              

$$
\begin{align*}
a^2 = 4(3m^2 + b)
\end{align*}
$$

              となる．$3m^2 + b \in\mathbb{Z}$だから$a^2$が$4$で割り切れる，すなわち$a$が$2$で割り切れる．
              従って，[(式6)](#1999-5:eq:6)から$u$も整数となる．
              以上から，$u,v \in\mathbb{Z}$となる．
    \end{itemize}

    以上から，$v\neq 0$の場合は$u,v\in\mathbb{Z}$であることが示された．

    **$v =  0$の時**

    この時，$\alpha = u$だから，
    

$$
\begin{align*}
u^2+au+b=0
\end{align*}
$$

    が成立する．有理数$u$を互いに素な整数$n,m$を用いて
    

$$
\begin{align*}
u = \frac{m}{n}
\end{align*}
$$

    と書くと，
    

$$
\begin{align*}
& \frac{m^2}{n^2}+a\frac{m}{n}+b=0 \\\therefore& \frac{m^2}{n} = -(am+bn)
\end{align*}
$$

    である．右辺が整数だから左辺も整数でないといけないが，
    これは$n\neq 1$の時$m,n$が互いに素である仮定に反して矛盾するから，
    $n=1$である．従って$u$も整数となる．
    以上から，$v = 0$の場合も$u,v\mathbb{Z}$であることが示された．

    
    以上二つの場合わけでいずれの場合も$u,v\mathbb{Z}$であることが示された．
    従って題意は示された．$\cdots$(答)

    
    

## 【解説】