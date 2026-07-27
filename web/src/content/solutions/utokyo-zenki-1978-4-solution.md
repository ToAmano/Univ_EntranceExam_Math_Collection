---
university: "utokyo"
category: "zenki"
year: "1978"
question: "4"
type: "solution"
title: "UTOKYO 1978 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

単位行列を $I$ とおく。ケーリー・ハミルトンの定理から、

$$
\begin{align*}
A^2 - \left(\frac{1}{3} + 3\right) A + \det(A) \cdot I = 0 \implies A^2 = \frac{10}{3}A - I \quad \cdots \text{①}
\end{align*}
$$

である。したがって、$n \in \mathbb{N}_{\ge 2}$ に対し、

$$
\begin{align*}
A^{n+1} = A^{n-1} \cdot A^2 = A^{n-1} \left( \frac{10}{3} A - I \right) = \frac{10}{3} A^n - A^{n-1} \quad \cdots \text{②}
\end{align*}
$$

となる。ここで、数列 $c_n$ が $c_{n+2} = \frac{10}{3} c_{n+1} - c_n$ を満たすとき、その一般項は $p, q$ を定数として

$$
\begin{align*}
c_n = 3^n p + \left(\frac{1}{3}\right)^n q
\end{align*}
$$

で与えられることに注意する。

\medskip

(1) $A = \begin{pmatrix} 1/3 & 5 \\ 0 & 3 \end{pmatrix}$, $A^2 = \begin{pmatrix} 1/9 & 50/9 \\ 0 & 9 \end{pmatrix}$ である。ここで

$$
\begin{align*}
A^n = 3^{n-1} \begin{pmatrix} 0 & 45/8 \\ 0 & 3 \end{pmatrix} + \left(\frac{1}{3}\right)^{n-1} \begin{pmatrix} 1/3 & -5/8 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} (1/3)^n & (3^n - (1/3)^n)\frac{15}{8} \\ 0 & 3^n \end{pmatrix} \quad \cdots \text{③}
\end{align*}
$$

であることを帰納的に示す。$n=1,2$ の時は成立する。そこで $n=k, k+1 \ (k \in \mathbb{N})$ での③の成立を仮定すると、②から

$$
\begin{align*}
A^{k+2}&= \frac{10}{3}\begin{pmatrix} (1/3)^{k+1} & (3^{k+1} - (1/3)^{k+1})\frac{15}{8} \\ 0 & 3^{k+1} \end{pmatrix} - \begin{pmatrix} (1/3)^k & (3^k - (1/3)^k)\frac{15}{8} \\ 0 & 3^k \end{pmatrix}\\&= \begin{pmatrix} (1/3)^{k+2} & (3^{k+2} - (1/3)^{k+2})\frac{15}{8} \\ 0 & 3^{k+2} \end{pmatrix}
\end{align*}
$$

となり、$n=k+2$ でも成立する。以上より示された。

したがって、

$$
\begin{align*}
A^n = \begin{pmatrix} (1/3)^n & (3^n - (1/3)^n)\frac{15}{8} \\ 0 & 3^n \end{pmatrix}
\end{align*}
$$

である。さらに

$$
\begin{align*}
\begin{pmatrix} a_n \\ b_n \end{pmatrix} = A^n \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} (1/3)^n a + \frac{15}{8}(3^n - (1/3)^n) b \\ 3^n b \end{pmatrix} \quad \cdots \text{④}
\end{align*}
$$

だから、$\alpha = 3^n$ とおくと、

$$
\begin{align*}
a_n^2 + b_n^2 = \left\{ \frac{15}{8} b \alpha + \left(a - \frac{15}{8}b\right) \frac{1}{\alpha} \right\}^2 + (b\alpha)^2
\end{align*}
$$

であり、$n \to \infty$ ($\alpha \to \infty$) において、

### $b \ne 0$ のとき

$$
\begin{align*}
u = \lim_{n \to \infty} \frac{a_n}{\sqrt{a_n^2 + b_n^2}} = \frac{\frac{15}{8}b}{\sqrt{\left(\frac{15}{8}b\right)^2 + b^2}} = \frac{15}{17}\frac{b}{|b|}
\end{align*}
$$

$$
\begin{align*}
v = \lim_{n \to \infty} \frac{b_n}{\sqrt{a_n^2 + b_n^2}} = \frac{b}{\sqrt{\left(\frac{15}{8}b\right)^2 + b^2}} = \frac{8}{17}\frac{b}{|b|}
\end{align*}
$$

### $b = 0$ のとき

④に代入して $\begin{pmatrix} a_n \\ b_n \end{pmatrix} = \begin{pmatrix} a/\alpha \\ 0 \end{pmatrix}$ だから、$v=0, u = \frac{a}{|a|}$ となる。

\medskip
以上をまとめて、

$$
\begin{align*}
\begin{cases}
b=0 \text{ のとき } & (u,v) = \left(\frac{a}{|a|}, 0\right) \\[1ex]
b \ne 0 \text{ のとき } & (u,v) = \left(\frac{15}{17}\frac{b}{|b|}, \frac{8}{17}\frac{b}{|b|}\right)
\end{cases}
\end{align*}
$$

となる。