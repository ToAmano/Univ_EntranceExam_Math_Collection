---
university: "titech"
category: "zenki"
year: "1963"
question: "2"
type: "solution"
title: "TITECH 1963 zenki Q2 (solution)"
---

## 【解】

題意の条件文は以下の3つである．

$$
\begin{align}
& x > 0, y > 0, a > 0 \label{eq:1}\\& x + y \le 1 + a \label{eq:2}\\& \frac{1}{x} + \frac{1}{y}\le 4(1+a) \label{eq:3}
\end{align}
$$

ここから$y$を消去していくことによって題意を示す．
まず[(式2)](#eq:2)を$y$について整理して

$$
\begin{align}
y \le 1 + a - x \label{eq:4}
\end{align}
$$

である．
次に[(式3)](#eq:3)を$y$について整理すると[(式1)](#eq:1)に注意して

$$
\begin{align}
\frac{1}{y}\le 4(1+a) - \frac{1}{x}\\\therefore 
 0 < \frac{1}{4(1+a) - \frac{1}{x}}\le y  \label{eq:5}
\end{align}
$$

である．
[(式5)](#eq:4,eq:5)を[(式1)](#eq:1)に代入して $y$ の存在条件を考えると，$y$が存在するための条件は

$$
\begin{align}
& 0 < 1 + a - x \label{eq:6}\\& 0 < \frac{1}{4(1+a) - \frac{1}{x}}\\& \frac{1}{4(1+a) - \frac{1}{x}}\le 1 + a - x \label{eq:7}
\end{align}
$$

である．
[(式7)](#eq:7)を整理すると

$$
\begin{align}
1 \le(1+a-x) \left\{ 4(1+a) - \frac{1}{x}\right\} = -4(1+a)x - \frac{1+a}{x} + 1 + 4(1+a)^2
\end{align}
$$

だから両辺に $x (>0)$ をかけて

$$
\begin{align}
0 \le -4(1+a)x^2 + 4(1+a)^2 x - (1+a)
\end{align}
$$

を得る．[(式1)](#eq:1)より$1+a > 0$ だから両辺 $(1+a)$ でわって

$$
\begin{align}
&4x^2 - 4(1+a)x + 1 \le 0 \\&(2x - 1)^2 \le 4ax
\end{align}
$$

となる．右辺に[(式6)](#eq:6)を用いて

$$
\begin{align}
(2x - 1)^2 < 4a(1+a)
\end{align}
$$

だから題意は示された．

## 【解説】

解答では数式変換だけに頼って解いたが，図示した方がミスは起こりにくいだろう．
与えられた領域[(式3)](#eq:1,eq:2,eq:3)を$xy$平面に図示すると下図の斜線部のようになる．
緑の線が

$$
\begin{align}
y = (2x-1)^2 -4a(a+1)
\end{align}
$$

を表しており，斜線部の$x$の範囲では常に$y<0$をとっていることがわかるから，よってグラフより題意は示される．
（もちろん解答にするときはちゃんと負になることを示さないといけない．）
結局問題なのは二つの曲線

$$
\begin{align}
x+y = 1+a \\\frac{1}{x} + \frac{1}{y} = 4(1+a)
\end{align}
$$

の交点を求めるのが計算上面倒臭いという点で，そこさえクリアできれば解法自体は単純だ．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1963/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $x,y$の存在領域</figcaption>
</figure>