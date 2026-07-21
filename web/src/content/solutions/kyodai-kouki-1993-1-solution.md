---
university: "kyodai"
category: "kouki"
year: "1993"
question: "1"
type: "solution"
title: "KYODAI 1993 kouki Q1 (solution)"
---

## 【解】

  条件(1)から考える．分母が$x \to 1$で$0$だから，全体として極限が収束するためには
  
$$
\begin{align*}
\lim_{x\to 1} f(x) = 0
\end{align*}
$$

  が必要である．$f(x)$は三次の多項式だから，これを満たすためには$f(x)$が$(x-1)$を因数にもち，
  
$$
\begin{align}
f(x) = (x-1)g(x) \label{1993-1:eq:1}
\end{align}
$$

  と表せる．ただし，$g(x)$は最高次の係数が$1$の二次関数であり
  
$$
\begin{align}
g(x) = x^2+\alpha x + \beta\label{1993-1:eq:2}
\end{align}
$$

  と書ける．

  条件(1)に代入して
  
$$
\begin{align*}
& \lim_{x \to 1}\frac{g(x)}{x(x+1)}=1 \\\therefore
    g(1) = 2
\end{align*}
$$

  だから$\eqref{1993-1:eq:2}$より
  
$$
\begin{align*}
& 1+\alpha+\beta =2   \\\therefore& \beta = -\alpha + 1
\end{align*}
$$

  であり，
  
$$
\begin{align}
g(x) & = x^2 + \alpha x -\alpha +1                            \\
    f(x) & = (x-1)(x^2 + \alpha x -\alpha +1) \label{1993-1:eq:4}
\end{align}
$$

  となる．

  次に条件(2)を考える．$f(x)$の一階微分は
  
$$
\begin{align*}
f'(x)
     & =x^2+\alpha x-\alpha+1+(x-1)(2x+\alpha) \\& =3x^2+2(\alpha-1)x-2\alpha+1
\end{align*}
$$

  であるから，$f'(0)<0$となる条件は
  
$$
\begin{align}
& -2\alpha + 1 < 0                      \\\therefore& \alpha>\frac{1}{2}\label{1993-1:eq:3}
\end{align}
$$

  である．

  最後に条件(3)を考える．
  まず，$f(0)=\alpha-1$,$f(1)=0$より，直線$l$は
  $(0,\alpha+1),(1,0)$を通る直線で，
  
$$
\begin{align*}
l: y = h(x) = -(\alpha-1)(x-1)
\end{align*}
$$

  と表せる．この時，$f(x)-h(x)$は$x=0,1$を共通の引数にもち，
  
$$
\begin{align*}
f(x)-h(x)
     & =(x-1)(x^2 + \alpha x -\alpha +1) + (\alpha-1)(x-1) \\& =(x-1)\left(x^2+\alpha x \right)\\& =(x-1)x(x+\alpha)                                   \\& = x^3 + (\alpha-1)x^2 -\alpha x
\end{align*}
$$

  と分解できる．
  $\eqref{1993-1:eq:3}$からこれは$0\le x\le 1$の範囲では常に$0$以下であり，
  題意の条件(3)は
  
$$
\begin{align*}
\frac{3}{4}& =\int_0^1 |f(x)-h(x)|dx                                                        \\& =-\int_0^1 (x-1)x(x+\alpha) dx                                                 \\& =-\left[\frac{1}{4}x^4+\frac{\alpha-1}{3} x^3-\frac{\alpha}{2}x^2 \right]_0^1 \\& = \frac{\alpha}{6} + \frac{1}{12}
\end{align*}
$$

  と書けるから，
  
$$
\begin{align*}
\alpha = 4
\end{align*}
$$

  を得る．これは$\eqref{1993-1:eq:3}$を満たしている．

  従って，\label{1993-1:eq:4}に代入して，求める$f(x)$は
  
$$
\begin{align*}
f(x)
     & =(x-1)(x^2 + 4 x -3) \\& =x^3 + 3x^2 -7x +3
\end{align*}
$$

  である．  $\cdots$(答)

  
  

## 【解説】

  この問題も求めた答えがちゃんと条件を満たしているか検算しやすい．
  例えば条件(1)は
  
$$
\begin{align*}
\lim_{x\to 1}\frac{x^3 + 3x^2 -7x +3}{x^3-x}& =\lim_{x\to 1}\frac{x^2+4x-3}{x^2+x}\\& = \frac{2}{2}\\& = 1
\end{align*}
$$

  となり，求めた$f(x)$がちゃんと条件を満たしていることが確認できる．