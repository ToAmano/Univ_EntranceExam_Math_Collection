---
university: "ukyoto"
category: "kouki"
year: "2005"
question: "5"
type: "solution"
title: "UKYOTO 2005 kouki Q5 (solution)"
---

## 【解】

  与式の右辺を積分して
  

$$
\begin{align*}
n < \frac{1}{\log_{e} 10}\left[ x (\log_{e} x - 1) \right]_{10}^{100}
\end{align*}
$$

  をみたす $\max n \in \mathbb{N}$をもとめれば良い.
  表記の簡潔さのため
  

$$
\begin{align*}
t = \log_{10}e
\end{align*}
$$

  ，不等式の右辺を$A$とおく．
  対数関数の基底の取り替え公式から
  

$$
\begin{align*}
\log_{e} x = \frac{\log_{10} x}{\log_{10} e}
\end{align*}
$$

  であることに注意して，全ての基底を$10$に直すと，
  

$$
\begin{align*}
A
     & = \frac{1}{\log_{e} 10}\left[ 100 (\log_{e} 100 - 1) - 10 (\log_{e} 10 - 1)\right]\\& = \log_{10} e\left[ 100 \left(\frac{\log_{10} 100}{\log_{10}e} - 1\right) - 10 \left(\frac{\log_{10} 10}{\log_{10}e} - 1\right)\right]\\& = t\left[ 100 \left(\frac{2}{t} - 1 \right) - 10 \left(\frac{1}{t} - 1 \right)\right]\\& = 190 - 90t
\end{align*}
$$

  である．題意より$0.434 < t < 0.435$ で，同区間で $A$ は$t$に関して単調減少だから，
  

$$
\begin{align*}
190 - 90 \cdot 0.435 & < A < 190 - 90 \cdot 0.434 \\
    150.85               & < A < 150.94
\end{align*}
$$

  より，求める自然数は
  

$$
\begin{align*}
n=150
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】