---
university: "kyodai"
category: "kouki"
year: "2003"
question: "5"
type: "solution"
title: "KYODAI 2003 kouki Q5 (solution)"
---

## 【解】

  $f(x) = x^{100}$ とおく。$k \in \mathbb{N}$ として平均値の定理から
  

$$
\begin{align*}
f\left(\frac{2k}{2n}\right) - f\left(\frac{2k-1}{2n}\right)
    = \frac{1}{2n} f'(c_k) \quad\left(\frac{2k-1}{2n} < c_k < \frac{2k}{2n}\right)
\end{align*}
$$

  なる $c_k$ がある。従って，
  

$$
\begin{align*}
\sum_{k=1}^{2n}(-1)^k \left(\frac{k}{2n}\right)^{100}& = \sum_{k=1}^{n}\left\{\left(\frac{2k}{2n}\right)^{100} - \left(\frac{2k-1}{2n}\right)^{100}\right\}\\& = \sum_{k=1}^{n}\frac{1}{2n} f'(c_k)
\end{align*}
$$

  と書き直せる．区分求積法より，
  $n \to \infty$ のとき
  

$$
\begin{align*}
\lim_{n\to\infty}\sum_{k=1}^{2n}(-1)^k \left(\frac{k}{2n}\right)^{100}& = \int_0^1 \frac{1}{2} f'(x) dx \\& = \frac{1}{2}(f(1) - f(0))     \\& = \frac{1}{2}
\end{align*}
$$

  となり，
  

$$
\begin{align*}
\frac{1}{2}
\end{align*}
$$

  が求める極限値である．$\cdots$(答)

  
  

## 【解説】