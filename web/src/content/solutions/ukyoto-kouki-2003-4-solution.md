---
university: "ukyoto"
category: "kouki"
year: "2003"
question: "4"
type: "solution"
title: "UKYOTO 2003 kouki Q4 (solution)"
---

## 【解】

  背理法で題意を示す．
  $a_{n+1} > \frac{1}{2} a_n - p$ をみたす $n \in \mathbb{N}$ がないと仮定すると
  

$$
\begin{align*}
a_{n+1}\le\frac{1}{2} a_n - p
\end{align*}
$$

  が任意の $n \in \mathbb{N}$ で成り立つ。変形して
  

$$
\begin{align*}
a_{n+1} + p \le\frac{1}{2}(a_n + p)
\end{align*}
$$

  だから，この漸化式をくり返し用いて
  

$$
\begin{align*}
a_n \le\left(\frac{1}{2}\right)^{n-1}(a_1 + p) - p
\end{align*}
$$

  となる．
  $a_1, p > 0$ だから十分大きい $n$ に対し $a_n < 0$ となり矛盾．
  よって示された．
  $\cdots$(答)

  
  

## 【解説】