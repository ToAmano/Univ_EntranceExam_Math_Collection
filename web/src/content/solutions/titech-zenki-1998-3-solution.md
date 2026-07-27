---
university: "titech"
category: "zenki"
year: "1998"
question: "3"
type: "solution"
title: "TITECH 1998 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$f(x)=\dfrac{2x-1}x$，$f_0(t)=t$，$f_n(t)=f(f_{n-1}(t))$とする．

**(1)** $f_{n+1}(t)$が定義できるためには$f_n(t)\ne0$が必要（分母）．そこで各$n\ge0$に対し$f_n(t)=0$となる$t$を帰納的にもとめる．

$f_0(t)=0\iff t=0=\dfrac0{0+1}$．$n=k$で「$f_k(t)=0\iff t=\dfrac k{k+1}$」が成り立つと仮定する．$f_{k+1}(t)=0$の時，$f_k(t)=t'$とおくと$f_{k+1}(t)=f(t')=\dfrac{2t'-1}{t'}=0\iff t'=\dfrac12$．すなわち$f_k(t)=\dfrac12$．仮定の漸化式の構造から（$f_k$の定義式を用いて逆算すると）これをみたす$t$は

$$
\begin{align*}
t=\frac{k+1}{k+2}
\end{align*}
$$

となる．以上により$n\in\mathbb N$のすべてに対し

$$
\begin{align*}
f_n(t)=0\iff t=\frac n{n+1}
\end{align*}
$$

が成り立つ．したがって，すべての$n$に対し$f_n(t)$が矛盾なく（分母が$0$にならず）定義できるための$t$の条件は

$$
\begin{align*}
t\ne\frac n{n+1}\quad(n\in\mathbb N)
\end{align*}
$$

**(2)** $g_n(t)=f_n(t)-1$とおく．$f_{n+1}=2-\dfrac1{f_n}$だから

$$
\begin{align*}
g_{n+1}(t)=f_{n+1}(t)-1=1-\frac1{f_n(t)}=\frac{f_n(t)-1}{f_n(t)}=\frac{g_n(t)}{g_n(t)+1}\quad\cdots\text{①}
\end{align*}
$$

$g_0(t)=t-1$である．$g_k(t)=\dfrac{t-1}{k(t-1)+1}$と予想して帰納法で示す．$k=0$で成立．①に代入すると

$$
\begin{align*}
g_{k+1}(t)=\frac{\dfrac{t-1}{k(t-1)+1}}{\dfrac{t-1}{k(t-1)+1}+1}=\frac{t-1}{(t-1)+k(t-1)+1}=\frac{t-1}{(k+1)(t-1)+1}
\end{align*}
$$

となり，$k+1$でも成立．よって

$$
\begin{align*}
g_n(t)=\frac{t-1}{n(t-1)+1}=\frac1n-\frac1{n^2(t-1)+n}
\end{align*}
$$

$a\ge1$として，

$$
\begin{align*}
n^2\int_a^{a+\frac1n}g_n(t)\,dt=n^2\left[\frac tn-\frac1{n^2}\log\bigl(n(t-1)+1\bigr)\right]_a^{a+\frac1n}
\end{align*}
$$

$$
\begin{align*}
=n^2\left[\frac1{n^2}-\frac1{n^2}\log\frac{n(a-1)+2}{n(a-1)+1}\right]=1-\log\left(a-1+\frac2n\right)+\log\left(a-1+\frac1n\right)
\end{align*}
$$

$a>1$の時，$n\to\infty$で$\log(a-1+2/n)\to\log(a-1)$，$\log(a-1+1/n)\to\log(a-1)$となるので

$$
\begin{align*}
n^2\int_a^{a+\frac1n}(f_n(t)-1)\,dt\longrightarrow1
\end{align*}
$$

$a=1$の時は

$$
\begin{align*}
1-\log\frac2n+\log\frac1n=1+\log\frac{1/n}{2/n}=1+\log\frac12=1-\log2
\end{align*}
$$

（$n$によらず一定）．以上をまとめて，もとめる極限値は

$$
\begin{align*}
\lim_{n\to\infty}n^2\int_a^{a+\frac1n}(f_n(t)-1)\,dt=
\begin{cases}
1-\log2 & (a=1)\\
1 & (a>1)
\end{cases}
\end{align*}
$$