---
university: "titech"
category: "kouki"
year: "1994"
question: "1"
type: "solution"
title: "TITECH 1994 kouki Q1 (solution)"
---

## 【解】

  題意の2つ目の条件の絶対値を外すと$F(x)$ は以下のように定義される：
  
$$
\begin{align}
F(x) =
    \begin{dcases}
      (1+a)x^2 + (c-ab)x & (x \ge b) \\
      (1-a)x^2 + (c+ab)x & (x \le b)
    \end{dcases}\label{1994-1:eq:1}
\end{align}
$$

  $\eqref{1994-1:eq:1}$から $F(x)$ は $x\neq b$ で微分可能である．そこで，題意の一つ目の条件式を両辺$x$で微分することで
  
$$
\begin{align}
F'(x) = f(x) \quad(x \ne b)
\end{align}
$$

  がなりたつ．$\eqref{1994-1:eq:1}$の両辺を$x$で微分して，
  
$$
\begin{align}
f(x) =
    \begin{dcases}
      2(1+a)x + (c-ab) & (x > b) \\
      2(1-a)x + (c+ab) & (x < b)
    \end{dcases}\label{1994-1:eq:2}
\end{align}
$$

  を得る．したがって$f(x)$は$x\neq b$で連続である．

  さて，題意の条件(i)より，$f(x)$は$x=b$でも連続でなければならない．そのためには$\displaystyle \lim_{x\to b} f(x)$の両側極限が同じ値に収束すればよい．
  
$$
\begin{align*}
\lim_{x \to b+0} f(x) & = 2(a+1)b + (c-ab) \\\lim_{x \to b-0} f(x) & = 2(1-a)b + (c+ab)
\end{align*}
$$

  これらの左右極限がひとしいためには
  
$$
\begin{align*}
2(1+a)b + (c-ab) & = 2(1-a)b + (c+ab) \\\therefore 2ab   & = 0                \\\therefore ab    & = 0
\end{align*}
$$

  でありこの時$a=0$ または $b=0$である．また，
  
$$
\begin{align}
f(b) = 2b+c
\end{align}
$$

  となる．以下場合分けして残りの条件(ii),(iii)から定数$a$,$b$,$c$を決定することで$f(x)$を求める．

   
  (a) $a=0$ の時

  $\eqref{1994-1:eq:1}$から$F(x)=x^2 + cx$となる．(ii)から$F(1)=0$すなわち$c=-1$である．
  したがって$\eqref{1994-1:eq:2}$から$f(x)=2x-1$だが，これは(iii)の$f(0)=1$に反して矛盾．

   
  (b) $b=0$ の時

  $\eqref{1994-1:eq:1,1994-1:eq:2}$から，$F(x)$および$f(x)$は
  
$$
\begin{align*}
F(x) = \begin{cases}
             (1+a)x^2 + cx & (x \ge 0) \\
             (1-a)x^2 + cx & (x \le 0)
           \end{cases}\\
    f(x) = \begin{cases}
             2(1+a)x + c & (x \ge 0) \\
             2(1-a)x + c & (x \le 0)
           \end{cases}
\end{align*}
$$

  と表せる．(ii)(iii)を代入して，
  
$$
\begin{align*}
\begin{cases}
      a+1+c = 0 \\
      c=1
    \end{cases}\\\therefore a = -2, \ c=1
\end{align*}
$$

  を得る．以上からもとめる$f(x)$は
  
$$
\begin{align*}
f(x) = \begin{cases}
             -2x+1 & (x \ge 0) \\
             6x+1  & (x \le 0)
           \end{cases}
\end{align*}
$$

  である．この関数$f(x)$は題意のすべての条件を満たす．$\cdots$(答)

  
  

## 【解説】

  多変数関数の問題．5つの条件を条件をひとつずつ処理していけば良い．
  手順としては条件(ii)が$F(x)$に関するもので，その他が$f(x)$に関するものなので，先に(ii)を処理してから他の条件を処理するとすんなりいく．
  $f$の原始関数$F$が二次関数なので$f$は一次関数となり答えがもっともらしいことを確認できる．

  受験上のテクニックとしては，この手の問題は条件(i)から(iiiき)が簡単に検算できるためやる癖をつけたい．