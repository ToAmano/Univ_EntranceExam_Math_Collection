---
university: "ukyoto"
category: "zenki"
year: "2000"
question: "5"
type: "solution"
title: "UKYOTO 2000 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $C_n = (n+1) \int_0^1 x^n \cos\pi x \, dx$ $\cdots$ ①

(1) 

$$
\begin{align*}
C_{n+2}&= (n+3) \int_0^1 x^{n+2}\cos\pi x \, dx \\&= (n+3) \left[\left[\frac{1}{\pi}\sin\pi x \cdot x^{n+2}\right]_0^1 - \int_0^1 \frac{n+2}{\pi} x^{n+1}\sin\pi x \, dx \right]\\&= - \frac{1}{\pi}(n+3)(n+2) \int_0^1 x^{n+1}\sin\pi x \, dx \\&= - \frac{1}{\pi}(n+3)(n+2) \left[\left[\frac{-1}{\pi}\cos\pi x \cdot x^{n+1}\right]_0^1 + \frac{1}{\pi} C_n \right]\\&= - \frac{(n+3)(n+2)}{\pi}\left\{\frac{1}{\pi} + \frac{1}{\pi} C_n \right\}
\end{align*}
$$

(2) ①から

$$
\begin{align*}
\frac{C_n}{n+1}&= \int_0^1 x^n \cos\pi x \, dx \\&= \left[\frac{1}{n+1} x^{n+1}\cos\pi x \right]_0^1 - \int_0^1 \frac{1}{n+1} x^{n+1}(-\pi\sin\pi x) \, dx \\&= - \frac{1}{n+1} + \frac{\pi}{n+1}\int_0^1 x^{n+1}\sin\pi x \, dx
\end{align*}
$$

$$
\begin{align*}
C_n = -1 + \pi \int_0^1 x^{n+1} \sin\pi x \, dx \quad \cdots \text{②}
\end{align*}
$$

又、

$$
\begin{align*}
\int_0^1 x^{n+1}\sin\pi x \, dx &= \frac{1}{n+2}\left[ x^{n+2}\sin\pi x \right]_0^1 - \frac{\pi}{n+2}\int_0^1 x^{n+2}\cos\pi x \, dx \\&= - \frac{\pi}{n+2}\int_0^1 x^{n+2}\cos\pi x \, dx \\&= \left( - \frac{\pi}{(n+2)(n+3)} C_{n+2}\right)\quad\cdots\text{③}
\end{align*}
$$

$[0,1]$ で $x^n \ge 0$, $-1 \le \cos\pi x \le 1$ だから

$$
\begin{align*}
-x^{n+2} \le x^{n+2} \cos\pi x \le x^{n+2}
\end{align*}
$$

同区間で積分して

$$
\begin{align*}
- \frac{1}{n+3} \le \int_0^1 x^{n+2} \cos\pi x \, dx \le \frac{1}{n+3}
\end{align*}
$$

したがって③から

$$
\begin{align*}
- \frac{\pi}{(n+2)(n+3)} \le \int_0^1 x^{n+1} \sin\pi x \, dx \le \frac{\pi}{(n+2)(n+3)}
\end{align*}
$$

$n \to \infty$ として、はさみうちから $A \to 0 \ (n \to \infty)$ なので、②から

$$
\begin{align*}
C_n \to -1 \ (n \to \infty) \equiv C
\end{align*}
$$

(3) ②及び $C=-1$ から

$$
\begin{align*}
C_n - C = C_n + 1 = \pi \int_0^1 x^{n+1} \sin\pi x \, dx
\end{align*}
$$

だから、$a_n = \frac{C_{n+1}+1}{C_n+1}$ とおくと、

$$
\begin{align*}
a_n = \frac{\int_0^1 x^{n+2} \sin\pi x \, dx}{\int_0^1 x^{n+1} \sin\pi x \, dx} \quad \cdots \text{④}
\end{align*}
$$

である。③を④に代入して

$$
\begin{align*}
a_n &= \frac{\frac{C_{n+3}}{(n+3)(n+4)}}{\frac{C_{n+2}}{(n+2)(n+3)}}\\&= \frac{n+2}{n+4}\cdot\frac{C_{n+3}}{C_{n+2}}\\&= \frac{1+2/n}{1+4/n}\cdot\frac{C_{n+3}}{C_{n+2}}\to 1 \ (n \to\infty) \ (\because C_n \to -1)
\end{align*}
$$