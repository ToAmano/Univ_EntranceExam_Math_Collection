---
university: "ukyoto"
category: "kouki"
year: "1995"
question: "3"
type: "solution"
title: "UKYOTO 1995 kouki Q3 (solution)"
---

## 【解】

  $c=0$か否かで場合わけして考える．

  まず，$c=0$の時，
  $g(x)$ は高々1次関数で，その最大値・最小値は端点で取るので$|x| \leqq 1$ の時，
  

$$
\begin{align}
& \min\{g(1), g(-1)\}\leqq g(x) \leqq\max\{g(-1), g(1)\}\\\iff& a-b \leqq x \leqq a+b \label{1995-3:eq:1}
\end{align}
$$

  である．ただし，$a,b \ge 0$であることを用いた．

  一方で，$|p(\pm 1)| \leqq 1$ だから
  

$$
\begin{align}
-1 \leqq a \pm b \leqq 1  \label{1995-3:eq:2}
\end{align}
$$

  である．

  [(式2)](#1995-3:eq:1,1995-3:eq:2)から
  

$$
\begin{align*}
-1 \le g(x) \le 1
\end{align*}
$$

  となって$|g(x)\le 2$は成立する．

  次に $c \neq 0$ とする．
  $g(x)$ は2次関数で，その最大値・最小値は軸ないし端点でとる．
  軸は$x=-b/2c$だから，これらの点での$q(x)$の値は
  

$$
\begin{align*}
\begin{dcases}
      g(1) = a+b+c  \\
      g(-1) = a-b+c \\
      g\left(-\frac{b}{2c}\right) = a-\frac{b^2}{4c}
    \end{dcases}
\end{align*}
$$

  で，これらの絶対値が2以下ならば題意の条件を満たす．

  ここで，$|p(x)| \le 1$より
  

$$
\begin{align*}
|p(\pm 1)| = |a \pm b + c| \leqq 1
\end{align*}
$$

  であるから，
  

$$
\begin{align}
|g(\pm 1)| = |p(\pm 1)| \le 1 \label{1995-3:eq:5}
\end{align}
$$

  となる．

  次に軸での値について，軸が最大または最小となりうるのは軸が$-1\le x\le 1$の範囲にあるときで
  

$$
\begin{align}
& -1 \le\frac{-b}{2c}\le 1                        \\\iff& -1 \leqq\frac{b}{2c}\leqq 1 \label{1995-3:eq:3}
\end{align}
$$

  の場合を考えれば良い．この時三角不等式より
  

$$
\begin{align}
\left|g\left(-\frac{b}{2c}\right)\right|& = \left|a-\frac{b^2}{4c}\right|\\& \leqq |a| + |\frac{b^2}{4c}|                                                    \\& \leqq |a| + \left|\frac{b}{2}\right|\left|\frac{b}{2c}\right|\\& \leqq |a| + \left|\frac{b}{2}\right|\quad(\because\text{[(式3)](#1995-3:eq:3)}) \\& \leqq |a+b| \quad(\because b \ge 0) \label{1995-3:eq:4}
\end{align}
$$

  となる．

  一方で，$p(x)$の条件と三角不等式より
  

$$
\begin{align*}
& |p(1)-p(0)| \le |p(1)| + |p(0)| \le 2 \\\therefore& |a+b| \le 2
\end{align*}
$$

  だから，[(式3)](#1995-3:eq:3)より
  

$$
\begin{align}
\left|g\left(-\frac{b}{2c}\right)\right|\le 2 \label{1995-3:eq:6}
\end{align}
$$

  である．

  以上[(式6)](#1995-3:eq:5,1995-3:eq:6)より，全ての$x, |x|\leqq 1$に対して
  $|g(x)| \leqq 2$ である．
  よって $c \neq 0$ の場合も示された．

  以上で全ての場合が尽くされ，題意は示された．$\cdots$(答)

  
  

## 【解説】

  解答では丁寧に場合分けして解いたが，もっとエレガントに条件を駆使して解けるので紹介する．
  ポイントはうまいこと$q(x)$を$p(x)$を利用して表すことである．
  三角不等式から
  

$$
\begin{align*}
|q(x)|
     & = |cx^2+bx+a|               \\& = |c(x^2-1) + a+bx+c|       \\& \leqq |c||x^2-1| + |bx+a+c|
\end{align*}
$$

  であるが，$-1\le x \le 1$の範囲で
  

$$
\begin{align*}
& |c||x^2-1| \le |c| = |p(0)| \le 1           \\& |bx+a+c| \le |\pm b+a+c| = |p(\pm 1)| \le 1
\end{align*}
$$

  だから，
  

$$
\begin{align*}
|q(x)|
     & \leqq |c||x^2-1| + |bx+a+c| \\& \leqq 1 + 1                 \\& = 2
\end{align*}
$$

  となり題意は示された．