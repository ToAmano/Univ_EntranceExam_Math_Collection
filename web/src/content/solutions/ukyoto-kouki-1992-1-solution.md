---
university: "ukyoto"
category: "kouki"
year: "1992"
question: "1"
type: "solution"
title: "UKYOTO 1992 kouki Q1 (solution)"
---

## 【解】

  (1)
  まずは$f(x)$の次数$n\in\mathbb{Z}\ge 0$を求める．
  題意の条件より
  

$$
\begin{align}
\begin{dcases}
      F(x) & =f(x)  \\
      G(x) & =-f(x)
    \end{dcases}\label{1992-1:eq:1}
\end{align}
$$

  だから，$F(x),G(x)$の次数は$n+1$である．

  与えられた条件
  

$$
\begin{align}
F(G(x)) =  -F(x)^2 + pG(x) + q \label{1992-1:eq:7}
\end{align}
$$

  の両辺をxで微分して
  

$$
\begin{align*}
F'(G(x)) \cdot G'(x) = -2F(x) \cdot F'(x) + pG'(x)
\end{align*}
$$

  だから，[(式1)](#1992-1:eq:1)を代入して
  

$$
\begin{align*}
& -f(G(x)) f(x) = -2F(x)f(x) -pf(x)         \\& f(x) \left[f(G(x)) - 2F(x) - p\right] = 0
\end{align*}
$$

  となる．$f(x)$は恒等的に$0$ではないから，
  

$$
\begin{align}
f(G(x)) - 2F(x) - p = 0  \label{1992-1:eq:2}
\end{align}
$$

  を満たす．$f(G(x))$は$n(n+1)$次式，$F(x)$は$n+1$次式であるから，この恒等式が成立するには，
  

$$
\begin{align}
& n(n+1) = n+1 \\\therefore& n=1
\end{align}
$$

  が必要．つまり，$f(x)$は一次式で
  

$$
\begin{align}
& f(x) = \alpha x + \beta& (\alpha\ne 0) \label{1992-1:eq:3}
\end{align}
$$

  とおけて，積分することで
  

$$
\begin{align*}
F(x) = \frac{\alpha}{2}x^2 + \beta x
\end{align*}
$$

  を得る．

  一方題意より
  

$$
\begin{align}
G(x) = a - F(x) \label{1992-1:eq:4}
\end{align}
$$

  だから，[(式2)](#1992-1:eq:2)に[(式4)](#1992-1:eq:3,1992-1:eq:4)を代入して
  

$$
\begin{align*}
& \alpha(a-F(x)) + \beta - 2F(x) - p = 0    \\& (-\alpha-2)F(x) + a\alpha + \beta  - p = 0
\end{align*}
$$

  となる．$F(x)$は定数項がないから，この式が恒等的に成立するには係数比較して
  

$$
\begin{align}
& \begin{dcases}
         -\alpha-2 = 0 \\
         a\alpha + \beta  - p = 0
       \end{dcases}& \begin{dcases}
         \alpha = -2 \\
         p = a\alpha + \beta
       \end{dcases}\label{1992-1:eq:5}
\end{align}
$$

  である．

  次に$a$と$\alpha,\beta$の関係は
  

$$
\begin{align}
a
     & = \left[\frac{1}{2}\alpha t^2 + \beta t \right]_0^1 \\& = \frac{1}{2}\alpha + \beta\label{1992-1:eq:6}
\end{align}
$$

  である．

  [(式6)](#1992-1:eq:5,1992-1:eq:6)から$\alpha,\beta$を消去して
  

$$
\begin{align*}
\alpha& = -2     \\\beta& = a +1   \\
    p      & = -a + 1
\end{align*}
$$

  となるから，[(式3)](#1992-1:eq:3)より
  

$$
\begin{align}
\begin{dcases}
      f(x) & = -2x + a+1     \\
      F(x) & =-x^2 + (-a+1)x
    \end{dcases}\label{1992-1:eq:8}
\end{align}
$$

  である．

  逆にこの時，[(式7)](#1992-1:eq:7)に代入して
  

$$
\begin{align*}
& -(a-F(x))^2 + (a+1)(a-F(x)) = -\{F(x)\}^2 + p(a-F(x)) + q \\& (a-1)F(x) + a = (a-1)F(x) + pa + q
\end{align*}
$$

  となり，
  

$$
\begin{align*}
q
     & = a-pa
\end{align*}
$$

  とすれば良いから十分である．
  以上から，求める$F(x)$は
  

$$
\begin{align*}
F(x) = -x^2 + (a+1)x
\end{align*}
$$

  である．  $\cdots$(答)

  
  (2)
  $F(x)$を平方完成すると
  

$$
\begin{align*}
F(x) = -\left(x-\frac{a+1}{2}\right)^2 + \frac{(a+1)^2}{4}
\end{align*}
$$

  だから，$F(x)$の最大値は
  

$$
\begin{align*}
& \begin{dcases}
         (a+1)/2 \le 0 \text{の時，}       & \max F(x) = F(0) = 0                                        \\
         0 \le (a+1)/2 \le 1 \text{の時，} & \max F(x) = F\left(\frac{a+1}{2}\right) = \frac{(a+1)^2}{4} \\
         1 \le (a+1)/2 \text{の時，}       & \max F(x) = F(1) = a
       \end{dcases}\\& \begin{dcases}
         a \le -1  \text{の時，}      & \max F(x) =  0                \\
         -1 \le a \le 1 \text{の時，} & \max F(x) = \frac{(a+1)^2}{4} \\
         1 \le a \text{の時，}        & \max F(x) =  a
       \end{dcases}
\end{align*}
$$

  だから．これらが$\frac{1}{2}$に一致するのは，$a=\sqrt{2}-1$の時のみで，
  この時[(式8)](#1992-1:eq:8)に代入して求める$f(x)$は
  

$$
\begin{align*}
f(x) = -2x+\sqrt{2}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】

  (1)については，最初から$F(x)+G(x)=a$を用いて式変形をして行っても求まる．
  

$$
\begin{align*}
F(x) = a-G(x)
\end{align*}
$$

  だから，[(式7)](#1992-1:eq:7)に代入すると
  

$$
\begin{align*}
F(G(x))
     & = -\left(a-G(x)\right)^2 + p\left(a-G(x)\right) + q \\& = -G^2(x)+\left(p+2a\right)G(x)-a^2+q
\end{align*}
$$

  であり，$G(x)$を$x$と置き換えて
  

$$
\begin{align*}
F(x) = -x^2+(p+2a)x-a^2+q
\end{align*}
$$

  となる．よって$f(x)=F'(x)$より
  

$$
\begin{align*}
f(x) = -2x + p + 2a
\end{align*}
$$

  となり，
  

$$
\begin{align*}
a
      & = \int_0^1 (-2x+(p+2a)) dx \\& = -1+p+2a                  \\\therefore
    p & = 1-a
\end{align*}
$$

  だから
  

$$
\begin{align*}
F(x) = -x^2+(a+1)x
\end{align*}
$$

  である．