---
university: "titech"
category: "zenki"
year: "1997"
question: "2"
type: "solution"
title: "TITECH 1997 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$y=f(x)=\dfrac{1}{a+x}\ (a\ge0)$のグラフは下図で，斜線部は

$$
\begin{align*}
S_n=\sum_{k=n}^{2n}\frac{1}{a+k}
\end{align*}
$$

の面積である．面積比較して

$$
\begin{align*}
\int_n^{2n}f(x)dx+\frac{1}{a+2n}<S_n<\int_n^{2n}f(x)dx+\frac{1}{a+n}\quad\cdots\text{①}
\end{align*}
$$

$$
\begin{align*}
\int_n^{2n}f(x)dx=\left[\log(x+a)\right]_n^{2n}=\log\frac{2n+a}{n+a}=\log2+\log\frac{1+a/2n}{1+a/n}
\end{align*}
$$

だから，①の最左右辺は共に$\log2$に収束するので，はさみうちの定理から

$$
\begin{align*}
S_n\longrightarrow\log2 \quad\cdots(1)
\end{align*}
$$

これは$a$によらない．$\cdots(2)$