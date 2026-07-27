---
university: "ukyoto"
category: "zenki"
year: "1976"
question: "1"
type: "solution"
title: "UKYOTO 1976 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{proof}[解]
(1) $f'(x) = n x^{n-1}$ と、$f(x)$ が偶関数あるいは奇関数なことより、$|f(x)| < \frac{1}{1000} \quad \left(-\frac{1}{2} \le x \le \frac{1}{2}\right)$ を満たすには

$$
\begin{align*}
\left| f\left(\frac{1}{2}\right) \right| < \frac{1}{1000}
\end{align*}
$$

であれば良い. 代入して

$$
\begin{align*}
\left(\frac{1}{2}\right)^n < \frac{1}{1000} \quad \cdots \text{①}
\end{align*}
$$

ここで、$2^{10} = 1024 > 1000$ から $\left(\frac{1}{2}\right)^{10} < \frac{1}{1000}$. 同様に $\left(\frac{1}{2}\right)^9 > \frac{1}{1000}$ だから ①をみたす $n$ は $n \ge 10$ である ($y = \left(\frac{1}{2}\right)^x$ は $x>0$ で単調減少).

\medskip
(2) (1)で $x = \frac{X}{2}$ とおきかえると、$f(x) = \left(\frac{1}{2}\right)^n X^n \ (n \ge 10)$ は $-1 \le X \le 1$ で $|f(x)| < \frac{1}{1000}$ をみたす. そこで $g(x) = \left(\frac{1}{2}\right)^n x^n$ とおき、$10 \le n \in \mathbb{N}$ のうちで

$$
\begin{align*}
10^4 < g(3) < 10^5 \quad \cdots \text{②}
\end{align*}
$$

であるような $n$ をさがす.

ところで、

$$
\begin{align*}
\left(\frac{3}{2}\right)^{11} \le 10^2 \quad (\because 3^5 = 243, \, 2^5 \cdot 10 = 320)
\end{align*}
$$

$$
\begin{align*}
\left(\frac{3}{2}\right)^6 \ge 10 \quad (\because 3^6 - 2^6 \cdot 10 = 829 - 640 > 0)
\end{align*}
$$

の両辺 $\log_{10}$ をとって

$$
\begin{align*}
6 > \frac{1}{\log_{10} \frac{3}{2}} \ge \frac{11}{2} \quad \cdots \text{③}
\end{align*}
$$

さらに、②の両辺 $\log_{10}$ をとって

$$
\begin{align*}
4 < n \log_{10} \frac{3}{2} < 5 \quad \cdots \text{④}
\end{align*}
$$

$\log_{10} \frac{3}{2} > 0$ から、

$$
\begin{align*}
\frac{4}{\log_{10} \frac{3}{2}} < n < \frac{5}{\log_{10} \frac{3}{2}} \quad \cdots \text{⑤}
\end{align*}
$$

④をみたすような $n$ は②を満たし、④から⑤を満たす $n$ は

$$
\begin{align*}
24 > \frac{4}{1/6} < n < \frac{5}{1/5.5} = \frac{55}{2} = 27.5
\end{align*}
$$

もみたす. したがって、たとえば $n = 25$ とした $g(x) = \left(\frac{x}{2}\right)^{25}$ は解の1つ ($\because 25 \ge 10$).
\end{proof}

\begin{proof}[別解]
(1)から $g(x) = f(x - 1/2) = (x - 1/2)^n \ (n \ge 10)$ とすると前半の条件を満たす.
\end{proof}