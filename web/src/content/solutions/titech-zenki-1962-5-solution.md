---
university: "titech"
category: "zenki"
year: "1962"
question: "5"
type: "solution"
title: "TITECH 1962 zenki Q5 (solution)"
---

{\bf ［解］}

 漸化式からまず$f_1(x)$を求めると

$$
\begin{align*}
f_1(x) 
  &= \frac{1}{2h}\int_{x-h}^{x+h}\cos x \, dx \\&= \frac{1}{2h}[\sin(x+h) - \sin(x-h)]\\&= \frac{1}{2h}\cdot 2\sin h \cos x \\&= \frac{\sin h}{h}\cos x \\&= \frac{\sin h}{h} f_0(x)
\end{align*}
$$

である．
従ってこれをくり返し用いて，$p = \dfrac{\sin h}{h}$ とおくと

$$
\begin{align}
f_n(x) = p^n \cos x
\end{align}
$$

と書ける．
これは公比$p$の等比数列だから求めるべき和は

$$
\begin{align*}
\sum_{k=0}^n f_k(x) 
  &= \cos x \frac{1 - p^{n+1}}{1 - p}\\&\xrightarrow{n \to \infty}\frac{1}{1 - p}\cos x \quad(\because |p| < 1) \\&= \frac{h}{h - \sin h}\cos x
\end{align*}
$$

である．