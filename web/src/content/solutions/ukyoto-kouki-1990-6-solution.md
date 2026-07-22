---
university: "ukyoto"
category: "kouki"
year: "1990"
question: "6"
type: "solution"
title: "UKYOTO 1990 kouki Q6 (solution)"
---

## 【解】

  (1)
  $X$は$X_i$の和だから
  

$$
\begin{align*}
X = \sum_{i=1}^{l} X_i
\end{align*}
$$

  である．  $\cdots$(答)

  
  (2)
  まず(1)の結果から
  

$$
\begin{align*}
X^2 & = \sum_{i=1}^{l} X_i^2 + 2\sum_{i \ne j} X_i X_j
\end{align*}
$$

  より，期待値は分解できること，および$i\neq j$で$X_i$と$X_j$が独立であることから
  

$$
\begin{align*}
E(X^2)
     & = \sum_{i=1}^{l} E(X_i^2) + 2\sum_{i \ne j} E(X_i X_j)   \\& = \sum_{i=1}^{l} E(X_i^2) + 2\sum_{i \ne j} E(X_i)E(X_j)
\end{align*}
$$

  を計算すれば良い．

  ここで，
  

$$
\begin{align*}
E(X_i)   & = \frac{1}{n}\\
    E(X_i^2) & = \frac{1}{n}
\end{align*}
$$

  を代入すれば
  

$$
\begin{align*}
E(X^2) & = \frac{\ell}{n} + \frac{\ell(\ell-1)}{n^2}
\end{align*}
$$

  である．  $\cdots$(答)

  
  (3)
  (2)の結果より，
  

$$
\begin{align*}
& E(X^2) > 2                         \\\iff& \frac{\ell^2 + (n-1)\ell}{n^2} > 2 \\\iff& \ell^2 + (n-1)\ell -2n^2 > 0
\end{align*}
$$

  を満たす最小の$l$を求めれば良い．
  

$$
\begin{align*}
f(x) = x^2 + (n-1)x -2n^2
\end{align*}
$$

  とおくと，$f(x)=0$の判別式は
  

$$
\begin{align*}
D
     & = (n-1)^2+8n^2 \\& = 9n^2-2n+1
     & > 0
\end{align*}
$$

  であり，$y=f(x)$のグラフの概形は下図．

  よって，求める$l$は
  

$$
\begin{align*}
\frac{-(n-1)+\sqrt{D}}{2}\le x
\end{align*}
$$

  を満たす最小の整数である．ここで$n$は自然数だから
  

$$
\begin{align*}
0<9n^2-6n+1 < 9n^2-2n+11 < 9n^2
\end{align*}
$$

  の各辺のルートをとって，
  

$$
\begin{align*}
3n-1 < \sqrt{D} < 3n
\end{align*}
$$

  なので
  

$$
\begin{align*}
n < \frac{-(n-1)+\sqrt{D}}{2} < n+\frac{1}{2}
\end{align*}
$$

  となり，求める最小の$l$は
  

$$
\begin{align*}
\min l = n+1
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】