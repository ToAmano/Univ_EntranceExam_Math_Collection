---
university: "titech"
category: "zenki"
year: "1966"
question: "6"
type: "solution"
title: "TITECH 1966 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $C = \cos x, \, S = \sin x$ とおく．$I = \int_0^\pi x S e^x dx$ とおく．

$$
\begin{align*}
\begin{aligned}
I &= [x S e^x]_0^\pi - \int_0^\pi (S + x C) e^x dx = -\int_0^\pi S e^x dx - \int_0^\pi C x e^x dx \quad \dots \text{①} \\[5pt]
\int_0^\pi C x e^x dx &= [C x e^x]_0^\pi - \int_0^\pi (C - S x) e^x dx \\[5pt]
&= -\pi e^\pi - \int_0^\pi C e^x dx + I \quad \dots \text{②}
\end{aligned}
\end{align*}
$$

$A = \int_0^\pi S e^x dx, \, B = \int_0^\pi C e^x dx$ とおく．①, ②に代入して

$$
\begin{align*}
\begin{aligned}
I &= -A + \pi e^\pi + B - I \\[5pt]
\therefore I &= \frac{\pi e^\pi + B - A}{2} \quad \dots \text{③}
\end{aligned}
\end{align*}
$$

ここで,

$$
\begin{align*}
\begin{aligned}
A &= \frac{1}{1+1} [e^x(S-C)]_0^\pi = \frac{1}{2}(e^\pi + 1) \\[5pt]
B &= \frac{1}{1+1} [e^x(C+S)]_0^\pi = \frac{1}{2}(-e^\pi - 1)
\end{aligned}
\end{align*}
$$

だから③に代入して

$$
\begin{align*}
I = \frac{\pi e^\pi - e^\pi - 1}{2} = \frac{(\pi-1)e^\pi - 1}{2}
\end{align*}
$$

[解2]

$$
\begin{align*}
\begin{aligned}
I &= [-C x e^x]_0^\pi + \int_0^\pi C e^x(x+1) dx = \pi e^\pi + B + \int_0^\pi C e^x x dx \\[5pt]
\int_0^\pi C e^x x dx &= [S e^x x]_0^\pi - \int_0^\pi S e^x (x+1) dx = -A - I
\end{aligned}
\end{align*}
$$

だから

$$
\begin{align*}
\begin{aligned}
I &= \pi e^\pi + B - A - I \\[5pt]
\therefore I &= \frac{\pi e^\pi + B - A}{2}
\end{aligned}
\end{align*}
$$

(以下略)