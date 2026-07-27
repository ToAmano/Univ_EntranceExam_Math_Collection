---
university: "titech"
category: "zenki"
year: "1988"
question: "3"
type: "solution"
title: "TITECH 1988 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$A: x^2+y^2=r^2$，$B: y=\cos\left(\sqrt{\dfrac{\pi}{2}}x\right)$とおく．$A$と$B$の共有点の数は$y$を消した

$$
\begin{align*}
x^2+\cos^2\left(\sqrt{\frac{\pi}{2}}x\right)=r^2 \quad\cdots\text{①}
\end{align*}
$$

の解の数に等しい．この左辺を$f(x)$とおく．$f(x)$は偶関数だから，$x\ge0$でかんがえる．

$$
\begin{align*}
f'(x)=2x+2\cos\left(\sqrt{\frac{\pi}{2}}x\right)\left(-\sqrt{\frac{\pi}{2}}\sin\left(\sqrt{\frac{\pi}{2}}x\right)\right)=2x-\sqrt{\frac{\pi}{2}}\sin\left(\sqrt{2\pi}x\right)
\end{align*}
$$

より，

$$
\begin{align*}
f'(x)\ge0 \iff 2x\ge\sqrt{\frac{\pi}{2}}\sin\left(\sqrt{2\pi}x\right)
\end{align*}
$$

だから左図から下表をうる．

| $x$ | $0$ |  | $\frac12\sqrt{\frac{\pi}{2}}$ |  | $+\infty$ |
|:--:|:--:|:--:|:--:|:--:|:--:|
| $f'$ |  | $-$ | $0$ | $+$ |  |
| $f$ | $1$ | $\searrow$ |  | $\nearrow$ | $+\infty$ |

したがって，グラフは右上図よって解は

$$
\begin{align*}
\begin{cases}
0<r^2<\dfrac{\pi}{8}+\dfrac12\ \text{の時} & 0\text{個} \\
r^2=\dfrac{\pi}{8}+\dfrac12 & 2\text{個} \\
\dfrac{\pi}{8}+\dfrac12<r^2<1 & 4\text{個} \\
r^2=1 & 3\text{個} \\
1<r^2 & 2\text{個}
\end{cases}
\end{align*}
$$

だから

$$
\begin{align*}
N(r)=
\begin{cases}
0 & \left(0<r<\sqrt{\dfrac{\pi}{8}+\dfrac12}\right) \\
2 & \left(r=\sqrt{\dfrac{\pi}{8}+\dfrac12},\ 1<r\right) \\
3 & (r=1) \\
4 & \left(\sqrt{\dfrac{\pi}{8}+\dfrac12}<r<1\right)
\end{cases}
\end{align*}
$$