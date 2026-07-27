---
university: "titech"
category: "zenki"
year: "1993"
question: "2"
type: "solution"
title: "TITECH 1993 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

**(1)**

$$
\begin{align*}
\frac{\sin(2n+1)x}{\sin x}=\frac{x}{\sin x}\cdot\frac{\sin(2n+1)x}{(2n+1)x}\cdot(2n+1)\xrightarrow{x\to0}2n+1
\end{align*}
$$

**(2)** $\displaystyle\int_0^{\frac{\pi}{2}}\frac{\sin(2n+1)x}{\sin x}dx=\frac{\pi}{2}\ \cdots$①を帰納法で示す．$n=1$の時，

$$
\begin{align*}
\int_0^{\frac{\pi}{2}}\frac{\sin3x}{\sin x}dx=\int_0^{\frac{\pi}{2}}(3-4\sin^2x)dx=\left[3x\right]_0^{\frac{\pi}{2}}-4\cdot\frac12\left[x-\frac12\sin2x\right]_0^{\frac{\pi}{2}}
\end{align*}
$$

$$
\begin{align*}
=\frac32\pi-2\left(\frac{\pi}{2}\right)=\frac12\pi
\end{align*}
$$

で成立．以下$n=k\in\mathbb{N}$での成立を仮定し，$n=k+1$での成立を示す．

$$
\begin{align*}
\int_0^{\frac{\pi}{2}}\frac{\sin(2k+3)x}{\sin x}dx=\int_0^{\frac{\pi}{2}}\frac{\sin(2k+1)x\cos2x+\sin2x\cos(2k+1)x}{\sin x}dx
\end{align*}
$$

$$
\begin{align*}
=\int_0^{\frac{\pi}{2}}\frac{\sin(2k+1)x}{\sin x}(1-2\sin^2x)dx+\int_0^{\frac{\pi}{2}}2\cos x\cos(2k+1)x\,dx \quad\cdots\text{②}
\end{align*}
$$

であり，

$$
\begin{align*}
\int_0^{\frac{\pi}{2}}\frac{\sin(2k+1)x}{\sin x}dx=\frac{\pi}{2}\quad(\because\text{仮定})
\end{align*}
$$

$$
\begin{align*}
\int_0^{\frac{\pi}{2}}\sin x\sin(2k+1)x\,dx=0 \quad(\because k\ge1)
\end{align*}
$$

$$
\begin{align*}
\int_0^{\frac{\pi}{2}}\cos x\cos(2k+1)x\,dx=0 \quad(\because k\ge1)
\end{align*}
$$

だから，②に代入して

$$
\begin{align*}
\int_0^{\frac{\pi}{2}}\frac{\sin(2k+3)x}{\sin x}dx=\frac{\pi}{2}-0+0=\frac{\pi}{2}
\end{align*}
$$

より，$n=k+1$でも①は成立し，よって示された．