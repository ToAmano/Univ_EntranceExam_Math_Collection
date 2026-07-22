---
university: "ukyoto"
category: "kouki"
year: "1998"
question: "2"
type: "solution"
title: "UKYOTO 1998 kouki Q2 (solution)"
---

## 【解】

  まず，以下の補題を示す．

  **[補題1]** $f_n(x)$は$2$次関数かつ偶関数である．

  証明は帰納法で示す．
  $n=1$の時は初期条件により成立．
  そこで$n = k \in \mathbb{N}$での成立を仮定すると
  

$$
\begin{align}
& f_k(x) = a_k x^2 + b_k & (a_k \neq 0) \label{1998-2:eq:0}
\end{align}
$$

  とおける．
  題意の漸化式から
  

$$
\begin{align}
f_{k+1}(x)
     & = 3x^2 \int_0^1 a_k t^2 dt + 3 \int_0^1 (a_k t^2 + b_k) dt \\& = 2 a_k x^2 + a_k + 3 b_k \label{1998-2:eq:1}
\end{align}
$$

  となる．
  $a_i \neq 0$ だから，たしかに$n=k+1$でも$f_{n}(x)$は二次式である．
  以上から数学的帰納法により補題1は示された．

  
  以下具体的に$f_n(x)$を求める．補題1より[(式0)](#1998-2:eq:0)の表示および[(式1)](#1998-2:eq:1)の漸化式が全ての$n$について成り立つ，
  すなわち
  

$$
\begin{align}
& f_n(x) = a_n x^2 + b_n               & (n \ge 1) \label{1998-2:eq:6}\\& f_{n+1}(x) = 2 a_n x^2 + a_n + 3 b_n & (n \ge 1)
\end{align}
$$

  である．$f_{n+1}(x)$も同様に表示して係数比較すると
  

$$
\begin{align}
a_{n+1}& = 2 a_n                           \\
    b_{n+1}& = a_n + 3 b_n \label{1998-2:eq:2}
\end{align}
$$

  とおける．
  初期条件は問題文で与えられた$f_1(x) = 4 x^2 + 1$から
  

$$
\begin{align}
\begin{dcases}
      a_1 & = 4 \\
      b_1 & = 1
    \end{dcases}\label{1998-2:eq:3}
\end{align}
$$

  である．
  まず$a_n$は等比数列の公式から
  

$$
\begin{align}
a_n = 2^{n+1}\label{1998-2:eq:4}
\end{align}
$$

  と求まる．
  これを[(式2)](#1998-2:eq:2)に代入して$c_n = \frac{b_n}{2^n}$ とおくと，
  

$$
\begin{align*}
& c_{n+1}      = \frac{3}{2} c_n + 1   \\\therefore& c_{n+1} + 2  = \frac{3}{2}(c_n + 2)
\end{align*}
$$

  と書ける．初期条件は[(式3)](#1998-2:eq:3)より
  

$$
\begin{align*}
c_1 = \frac{1}{2}
\end{align*}
$$

  である．
  よって等比数列の公式より
  

$$
\begin{align*}
c_n
     & = \left(\frac{3}{2}\right)^{n-1}\left(\frac{1}{2}+2\right) - 2 \\& = \frac{5}{2}\left(\frac{3}{2}\right)^{n-1} - 2
\end{align*}
$$

  だから，$b_n=2^n c_n$は
  

$$
\begin{align}
b_n = 5 \cdot 3^{n-1} - 2^{n+1}\label{1998-2:eq:5}
\end{align}
$$

  と求まる．

  以上[(式5)](#1998-2:eq:4,1998-2:eq:5)を[(式6)](#1998-2:eq:6)に代入して，
  求める$f_n(x)$は
  

$$
\begin{align*}
f_n(x) = 2^{n+1} x^2 + 5 \cdot 3^{n-1} - 2^{n+1}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】