---
university: "titech"
category: "zenki"
year: "1972"
question: "3"
type: "solution"
title: "TITECH 1972 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

1.  $_{l+n}C_l = \dfrac{(l+n)!}{l!\cdot n!}$ だから
  

$$
\begin{align*}
_{l+n}C_l > {}_{m+n}C_m
\end{align*}
$$

  

$$
\begin{align*}
\frac{(l+n)!}{l!} > \frac{(m+n)!}{m!}
\end{align*}
$$

  

$$
\begin{align*}
(l+n)\cdots(l+1) > (m+n)\cdots(m+1)
\end{align*}
$$

  

$$
\begin{align*}
\therefore\ l>m
\end{align*}
$$

2.  $R(x)$ は高々2次式で，$R(x)=A(x-a)^2+B(x-a)+C$ とおける．又適当な多項式 $P(x)$ があって，
  

$$
\begin{align*}
F(x)=(x-a)^3P(x)+R(x)
\end{align*}
$$

  とかける．ここで，$G(x)=F(x)-R(x)$ とおくと，$G(x)$ は $(x-a)^3$ で割り切れるから
  

$$
\begin{align*}
G(a)=G'(a)=G''(a)=0
\end{align*}
$$

  

$$
\begin{align*}
\therefore\ R(a)=F(a),\ R'(a)=F'(a),\ R''(a)=F''(a) \quad\cdots\text{①}
\end{align*}
$$

  であり，$R(a)=C,\ R'(a)=B,\ R''(a)=2A$ だから，①より
  

$$
\begin{align*}
C=F(a),\ B=F'(a),\ A=\frac{1}{2}F''(a)
\end{align*}
$$

  だから
  

$$
\begin{align*}
R(x)=\frac{1}{2}F''(a)(x-a)^2+F'(a)(x-a)+F(a)
\end{align*}
$$