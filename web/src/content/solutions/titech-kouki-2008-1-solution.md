---
university: "titech"
category: "kouki"
year: "2008"
question: "1"
type: "solution"
title: "TITECH 2008 kouki Q1 (solution)"
---

## 【解】

  問題の構成として，(1)は(2)の$n=2$の時を証明する問題になっている．
  そこで，(2)を数学的帰納法により証明すれば(1)が含まれていることになるため，いきなり(2)を考える．

  各不等式に式番号を与える．
  

$$
\begin{align}
& 0 < a_1 \le a_2 \le\dots\le a_n                                          \label{2008-1:eq:1}\\& A_j: \sum_{i=1}^j a_i x_i \le\sum_{i=1}^j a_i y_i \quad(j=1, 2, \dots, n) \label{2008-1:eq:2}\\& \sum_{i=1}^n x_i \le\sum_{i=1}^n y_i \label{2008-1:eq:3}
\end{align}
$$

  
  \underline**$n=2$のとき**

  まず，$A_1$は
  

$$
\begin{align*}
a_1x_1 \le a_1y_1
\end{align*}
$$

  であり，[(式1)](#2008-1:eq:1)より$a_1>0$だから両辺$a_1$で割って
  

$$
\begin{align}
x_1 \le y_1 \label{2008-1:eq:4}
\end{align}
$$

  である．

  $A_2$は
  

$$
\begin{align*}
a_1x_1+a_2x_2 \le a_1y_1+a_2y_2
\end{align*}
$$

  であり，まず$a_1$と$a_2$についてこの不等式を整理すると
  

$$
\begin{align}
a_2\left(x_2-y_2\right)\le a_1\left(y_1-x_1\right)\label{2008-1:eq:5}
\end{align}
$$

  である．さらに，[(式1)](#2008-1:eq:1)より$0<a_1\le a_2$だから，右側の不等式はさらに上から評価すると
  

$$
\begin{align}
a_1\left(y_1-x_1\right)\le a_2 \left(y_1-x_1\right)\label{2008-1:eq:6}
\end{align}
$$

  ただし，[(式4)](#2008-1:eq:4)より$y_1-x_1\ge 0$であることを用いた．以上[(式6)](#2008-1:eq:5,2008-1:eq:6)から
  

$$
\begin{align*}
a_2\left(x_2-y_2\right)\le a_2 \left(y_1-x_1\right)
\end{align*}
$$

  である．両辺$a_2>0$で割って
  

$$
\begin{align*}
& x_2-y_2 \le y_1-x_1 \\\therefore& x_1+x_2 \le y_1+y_2
\end{align*}
$$

  であり，これは[(式3)](#2008-1:eq:3)であるから$n=2$のとき[(式3)](#2008-1:eq:3)は成り立つ．
  ((1)の証明)  $\cdots$(答)

  
  \underline{\textbf{$n\le k (k \in \mathbb{N} \ge 2)$での成立を仮定}}

  [(式2)](#2008-1:eq:1,2008-1:eq:2)を仮定する．
  $A_j (j=3,4,\cdots,k+1)$について．$n=2$の時と同じく
  

$$
\begin{align*}
\begin{dcases}
      a_2 (x_2 - y_2) + \sum_{i=3}^{j} a_i x_i \le a_1 (y_1 - x_1) + \sum_{i=3}^{j} a_i y_i \\
      a_1 (y_1 - x_1) + \sum_{i=3}^{j} a_i y_i \le a_2 (y_1 - x_1) + \sum_{i=3}^{j} a_i y_i
    \end{dcases}
\end{align*}
$$

  が成り立つ．従ってこれら二つの不等式より
  

$$
\begin{align}
a_2 (x_2 - y_2) + \sum_{i=3}^{j} a_i x_i \le a_2 (y_1 - x_1) + \sum_{i=3}^{j} a_i y_i \label{2008-1:eq:7}
\end{align}
$$

  である．

  ここで新しい数列$\{a'_i\}, \{X_i\}, \{Y_i\}$を
  

$$
\begin{align}
\begin{cases}
      a'_i = a_{i+1}                 & (i=1,2,\cdots,k) \\
      X_1 = x_2 - y_2, X_i = x_{i+1} & (i=2,3,\cdots,k) \\
      Y_1 = y_1 - x_1, Y_i = y_{i+1} & (i=2,3,\cdots,k)
    \end{cases}\label{2008-1:eq:10}
\end{align}
$$

  と定めると，$a_i$が[(式1)](#2008-1:eq:1)を満たすから$a'_{i}$は
  

$$
\begin{align}
0 < a'_1 \le a'_2 \le\cdots\le a'_{k}\label{2008-1:eq:8}
\end{align}
$$

  を満たす．さらに，[(式7)](#2008-1:eq:7)より
  

$$
\begin{align}
& a'_1 X_1 + \sum_{i=2}^{j-1} a'_i X_i \le  a'_1 Y_1 + \sum_{i=2}^{j-1} a'_i Y_i \nonumber\\\therefore& \sum_{i=1}^{j-1} a'_{i}X_{i}\le\sum_{i=1}^{j-1} a'_{i}Y_{i}\label{2008-1:eq:9}
\end{align}
$$

  である．以上[(式9)](#2008-1:eq:8,2008-1:eq:9)から，数列$\{a'_i\}, \{X_i\}, \{Y_i\}$は[(式2)](#2008-1:eq:1,2008-1:eq:2)を満たしている．
  これと帰納法の仮定より，$\{X_i\}, \{Y_i\}$に対して[(式3)](#2008-1:eq:3)が成り立つ．
  

$$
\begin{align*}
\sum_{i=1}^{k} X_i \le\sum_{i=1}^{k} Y_i
\end{align*}
$$

  ここに[(式10)](#2008-1:eq:10)を代入して元の$x_i,y_i$の式に戻すと
  

$$
\begin{align*}
& \left(x_2 - y_2\right) + \sum_{i=2}^{k+1} x_i
    \le\left(y_1 - x_1\right) + \sum_{i=2}^{k+1} y_i    \\\iff&
    \sum_{i=1}^{k+1} x_i \le\sum_{i=1}^{k+1} y_i
\end{align*}
$$

  となり，数列$\{x_i\}, \{x_i\}$は$n=k+1$に対して[(式3)](#2008-1:eq:3)を満たす．
  よって，$n=k+1$でも題意は成立する．

  
  以上から，数学的帰納法により任意の$n \in \mathbb{N} \ge 2$に対し$\diamond$は成立する．
  よって題意は示された．$\cdots$(答)

  
  

## 【解説】

  不等式の証明問題で数学的帰納法により証明できるのだが，式変形は多少この手の不等式証明に慣れてないと難しいかもしれない．

  とはいえ主張自体は直感的にはそれっぽいように思えるので，それをうまく数式化していければ良い．
  すごく大雑把にいうと単調増加の重み$\{a_n\}$が与えられた時，重み付けされた二つの数列$\{a_nx_n\}$と$\{a_ny_n\}$が大小を保つならば
  元の数列$\{x_n\}$，$\{y_n\}$も大小を保つ，ということである．

  ちなみに問題では数列$\{x_n\}$，$\{y_n\}$の二つが与えられているが，
  

$$
\begin{align*}
z_n = y_n - x_n
\end{align*}
$$

  で差分を導入すれば
  

$$
\begin{align*}
& \sum_{i=1}^j a_i z_i \ge 0 \quad(j=1, 2, \dots, n) \\\implies& \sum_{i=1}^n z_i \ge 0
\end{align*}
$$

  を示す問題になる．
  こちらの方が数列が一つ消える分扱いが簡単になるだろう．
  $n=2$の時は
  

$$
\begin{align*}
\begin{dcases}
      0 < a_1 \le a_2 \\
      a_1 z_1 \ge 0   \\
      a_1 z_1 + a_2z_2 \ge 0
    \end{dcases}\implies
    z_1 + z_2 \ge 0
\end{align*}
$$

  を示せば良い．まず$a_1 >0$より$z_1 \ge 0$が従い，$a_1 \le a_2$より
  

$$
\begin{align*}
& 0 \le a_1 z_1 + a_2z_2 \le a_2(z_1 + z_2) \\\therefore& 0 \le z_1+z_2
\end{align*}
$$

  となり示される．

  (2)の数学的帰納法の証明も
  

$$
\begin{align*}
\sum_{i=1}^j a_i z_i \ge 0 \quad(j=1, 2, \dots, n,n+1)
\end{align*}
$$

  を仮定したとき，$a_1 \le a_2$および$z_1 \ge 0$から
  

$$
\begin{align*}
& 0 \le\sum_{i=1}^j a_i z_i \le a_2z_1 + a_2z_2 + \sum_{i=3}^{j} a_iz_i \\\therefore& 0 \le a_2(z_1+z_2) + \sum_{i=3}^{j} a_iz_i
\end{align*}
$$

  とすれば，$\{a_2,a_3,\cdots,a_j\}$および$\{z_1+z_2,z_3,\cdots,z_j\}$に対して仮定が使える．

  この形になっていると，仮定である
  

$$
\begin{align*}
\sum_{i=1}^j a_i z_i \ge 0 \quad(j=1, 2, \dots, n,n+1)
\end{align*}
$$

  について少しイメージしやすい．$j=1$から順に書き出してみると
  

$$
\begin{align*}
& a_1 z_1 \ge 0                     \\& a_1 z_1 + a_2 z_2 \ge 0           \\& a_1 z_1 + a_2 z_2 + a_3 z_3 \ge 0
     & \cdots
\end{align*}
$$

  となる．一つ目の式から$z_1 \ge 0$が従い，二つ目の式から
  

$$
\begin{align*}
z_2 \ge\frac{-a_1}{a_2} z_1
\end{align*}
$$

  が従う．これは$(z_1,z_2)$平面に図示すると[図1](#2008-1:fig:1)の斜線部の領域である．
  $a_1 \le a_2$から境界の直線の傾きは$-1$よりも大きく，よって$z_1+z_2=k$とおくと
  

$$
\begin{align*}
k = z_1 + z_2 \ge z_1 + \frac{-a_1}{a_2} z_1 = \left(1+\frac{-a_1}{a_2}\right) z_1 \ge 0
\end{align*}
$$

  となる．(1)はこのように図形的にも解釈できる．

  

<figure id="2008-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2008/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $z_1z_2$平面における，$z_1+z_2$のとりうる領域．</figcaption>
</figure>

  三つ目の式は
  

$$
\begin{align*}
z_3
     & \ge\frac{-1}{a_3}\left[a_1 z_1 + a_2 z_2 \right]
\end{align*}
$$

  となる．以下同様に$z_4,\cdots, z_{n}$の下限が，それ以下の$z_i$たちによって規定される．
  したがって，これを$z_n$から順に下側へと伝搬していくと，結局$z_n$が$z_1$で評価できるだろうという推測がつく．
  実際やってみよう．

  まず，与えられている条件式を以下のように書き換える．
  

$$
\begin{align*}
& a_1 z_1 \ge 0                                                 \\& a_2(z_1+z_2) + (a_1-a_2) z_1 \ge 0                            \\& a_3 (z_1+z_2+z_3) + (a_2-a_3) (z_1+z_2) + (a_1-a_2) z_1 \ge 0 \\& \cdots\\& a_n (z_1+z_2+\cdots z_n) + (a_{n-1}-a_n) (z_1+\cdots+z_{n-1}) \\& \quad\quad\quad + \cdots + (a_1-a_2) z_1 \ge 0
\end{align*}
$$

  簡単のため大文字$Z_i$を$\{z_1,\cdots,z_i\}$の総和として定義する
  

$$
\begin{align*}
Z_i = \sum_{k=1}^{i} z_i
\end{align*}
$$

  とこの条件式は$j \ge 2$に対して
  

$$
\begin{align}
& a_j Z_j + \sum_{i=1}^{j-1}(a_{i}-a_{i+1})Z_i \ge 0   & (j=2,\cdots,n) \label{2008-1:eq:11}\\\therefore& Z_j \ge\sum_{i=1}^{j-1}\frac{a_{i+1}-a_{i}}{a_j}Z_i
\end{align}
$$

  となる．したがって，$j=n\, (n \ge 3)$から条件式を使うと
  

$$
\begin{align*}
Z_n
     & \ge\sum_{i=1}^{n-1}\frac{a_{i+1}-a_{i}}{a_n}Z_i                                                                              \\& = \frac{a_{n}-a_{n-1}}{a_n}Z_{n-1} + \sum_{i=1}^{n-2}\frac{a_{i+1}-a_{i}}{a_n}Z_i                                             \\& \ge\frac{a_{n}-a_{n-1}}{a_n}\sum_{i=1}^{n-2}\frac{a_{i+1}-a_{i}}{a_{n-1}}Z_i + \sum_{i=1}^{n-2}\frac{a_{i+1}-a_{i}}{a_n}Z_i \\& =  \frac{1}{a_{n-1}}\sum_{i=1}^{n-2}\left(a_{i+1}-a_{i}\right) Z_i                                                            \\
\end{align*}
$$

  と，$Z_{n-1}$を除去できる．したがって，この評価を繰り返すと$n\ge 3$に対して
  

$$
\begin{align*}
Z_n
     & \ge\frac{1}{a_{n-1}a_{n-2}\cdots a_2}\sum_{i=1}^{1}\left(a_{i+1}-a_{i}\right) Z_i \\& =\frac{(a_2-a_1)z_1}{a_{n-1}a_{n-2}\cdots a_2}
\end{align*}
$$

  となり，$a_1 \le a_2$および$z_1 \ge 0$よりこれは$0$以上であって，題意は示された．
  このように本問は帰納法を使わずとも証明できる．

  証明において核心となる[(式11)](#2008-1:eq:11)はアーベルの部分和分法（級数変形法）と呼ばれ，しばしば現れる古くから知られた手法である．
  これは色々な変形が知られているのだが，数列$\{a_n\}$と$\{b_n\}$が与えられた時
  

$$
\begin{align*}
& B_n = \sum_{k=0}^{n}b_k                                              \\& \sum_{n=0}^{N} a_nb_n = a_N B_N - \sum_{n=0}^{N-1}B_n(a_{n+1}-a_{n})
\end{align*}
$$

  のように数列の積の和を，「数列の和」と「数列の差」の積の和に変形する公式である．
  式の形を見ればわかるように，これは部分積分法の離散列版とみなすことができる．