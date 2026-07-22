---
university: "titech"
category: "kouki"
year: "1997"
question: "2"
type: "solution"
title: "TITECH 1997 kouki Q2 (solution)"
---

## 【解】

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1997/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 四角錐OABCD</figcaption>
</figure>

  対称性から、$X_n$がAに一致する確率を$q_n$とおくと、$X_n$がB,C,Dに一致する確率も$q_n$にひとしい．
  $X_n$がOに一致する確率を$p_n$とおく．$X_n$はO,A,B,C,Dのうちいずれかに一致するから，全体の確率が$1$となることより
  

$$
\begin{align}
p_n + 4q_n = 1 \label{1997-2:eq:1}
\end{align}
$$

  を満たす．

  次に$p_n$の漸化式を求める．$n+1$で$X_n$が$O$に等しい時，$n$では$X_n$はA,B,C,Dのいずれかに存在し，そこから確率$1/3$で$O$に移動する．したがって漸化式は
  

$$
\begin{align*}
p_{n+1} = \frac{4}{3}q_n
\end{align*}
$$

  である．[(式1)](#1997-2:eq:1)を代入して$q_n$を消去して
  

$$
\begin{align}
p_{n+1}& = \frac{1}{3}(1-p_n)
\end{align}
$$

  を得る．
  特性方程式$x = (1-x)/3$の解は$x = 1/4$だから，漸化式を変形すると
  

$$
\begin{align*}
p_{n+1}-\frac{1}{4}& = \frac{-1}{3}\left(p_n-\frac{1}{4}\right)
\end{align*}
$$

  だから，これと$p_1=0$から
  

$$
\begin{align}
p_n
     & = \left(-\frac{1}{3}\right)^{n-1}\left(0-\frac{1}{4}\right)+\frac{1}{4}\\& = \frac{1}{4}\left\{1-\left(-\frac{1}{3}\right)^{n-1}\right\}
\end{align}
$$

  となる．$\cdots$(答)

  
  

## 【解説】

  かなり容易な確率漸化式の問題である．
  問題のポイントとしては，特に確率をどのように指定するか明示がないので自分でうまいこと設定する必要があるところだろう．
  四角錐OABCDの中で点Oだけが特別であり，他のABCDは対称であることを使うと，解答のように二つの変数で漸化式を導ける．

  数列の一般項が出てくる問題では，$n\to\infty$での極限の振る舞いがそれらしいかを確かめたい．
  実際今回の場合は
  

$$
\begin{align*}
& \lim_{n\to\infty} p_n = \frac{1}{4}\\& \lim_{n\to\infty} q_n = \frac{3}{16}
\end{align*}
$$

  となる．この数値自体が正確かはすぐにはわからないが，
  

$$
\begin{align*}
\lim_{n\to\infty} p_n \neq\lim_{n\to\infty} q_n
\end{align*}
$$

  となっていることは，点Oの特殊性を考えるとそれらしいだろう．