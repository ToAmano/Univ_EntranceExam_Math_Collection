---
university: "kyodai"
category: "kouki"
year: "1994"
question: "6"
type: "solution"
title: "KYODAI 1994 kouki Q6 (solution)"
---

## 【解】

### (1)

  部分積分法より
  
$$
\begin{align*}
I_{n+1}& = \int_{1}^{e}(\log x)^{n+1} dx                                             \\& = \left[ x(\log x)^{n+1}\right]_{1}^{e} - \int_{1}^{e}(n+1)(\log x)^{n} dx \\& = e - (n+1)I_n
\end{align*}
$$

  だから，求める漸化式は
  
$$
\begin{align*}
I_{n+1} =  e - (n+1)I_n
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  まずは下側の不等式から評価する．
  $[1,e]$ で $0 \le \log x \le 1$ だから,
  
$$
\begin{align*}
(\log x)^n \ge(\log x)^{n+1}
\end{align*}
$$

  より，同じ区間で積分して $I_n \ge I_{n+1}$である．
  これに (1) を代入して
  
$$
\begin{align*}
I_n \ge e - (n+1)I_n \\\therefore I_n \ge\frac{e}{n+2}\quad(\because n \in\mathbb{N})
\end{align*}
$$

  であり，ここで
  
$$
\begin{align*}
& \frac{e}{n+2}\ge\frac{e-1}{n+1}\\\iff& e(n+1) \ge(e-1)(n+2)             \\\iff& n+2     \ge e
\end{align*}
$$

  で，$n\ge 1$よりこれは成立するから，
  
$$
\begin{align*}
I_n \ge\frac{e}{n+2}\ge\frac{e-1}{n+1}\\\therefore
    I_n \ge\frac{e-1}{n+1}
\end{align*}
$$

  となり，下側の不等式の成立が示された．

  次に上側の評価を考える．漸化式を二回利用して
  
$$
\begin{align*}
I_{n+1}& =  e - (n+2)I_{n+1}\\& =  e - (n+2)\left[e-(n+1)I_n\right]\\& =  -e(n+1) + (n+1)(n+2)I_n
\end{align*}
$$

  であり，ここで$I_{n+1}\le I_{1} =1$だから
  
$$
\begin{align*}
& -e(n+1) + (n+1)(n+2)I_n \le 1       \\\therefore& I_n \le\frac{e(n+1)+1}{(n+1)(n+2)}
\end{align*}
$$

  である．よって上側の不等式は示された．

  以上より，上下の不等式が成立することが示された．$\cdots$(答)

  

## 【解説】