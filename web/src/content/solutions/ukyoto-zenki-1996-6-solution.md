---
university: "ukyoto"
category: "zenki"
year: "1996"
question: "6"
type: "solution"
title: "UKYOTO 1996 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $v = const$ とする。$100 \text{ km}$ 走るのに要する時間は $\frac{100}{v} \ [h]$ である。 $\cdots \text{①}$ \\
はじめにガソリンが $x_0 \ [l]$ あったとして、題意から

$$
\begin{align*}
\frac{dx}{dt} = - \frac{100 + x}{100} \cdot e^{kv}
\end{align*}
$$

$$
\begin{align*}
\frac{1}{100 + x} dx = - \frac{e^{kv}}{100} dt
\end{align*}
$$

積分して、初期条件から、

$$
\begin{align*}
x + 100 = (x_0 + 100)e^{-\frac{e^{kv}}{100}t} \cdots \text{②}
\end{align*}
$$

したがって、①から、総ガソリン消費量 $Y$ は、②より

$$
\begin{align*}
Y = x_0 - x|_{t=\frac{100}{v}}
\end{align*}
$$

$$
\begin{align*}
= x_0 - \left\{ (x_0+100) e^{-\frac{e^{kv}}{v}} - 100 \right\} \quad \left( A = \frac{e^{kv}}{v} \text{ とおく} \right)
\end{align*}
$$

$$
\begin{align*}
= (1 - e^{-A})x_0 - 100(-1 + e^{-A})
\end{align*}
$$

$-\frac{e^{kv}}{v} < 0$ から $Y(x_0)$ は 1次係数正の $x_0$ の1次式 $\cdots \text{④}$ \\
又、$t = \frac{100}{v}$ で $x \ge 0$ だから、②より

$$
\begin{align*}
(x_0 + 100) e^{-\frac{e^{kv}}{v}} \ge 100
\end{align*}
$$

$$
\begin{align*}
x_0 \ge 100(e^{\frac{e^{kv}}{v}} - 1) \equiv P \cdots \text{⑤}
\end{align*}
$$

④、⑤より、$Y(v)$ を $\min$ にする $x_0$ は $P$ である。

$$
\begin{align*}
\min Y(v) = (1 - e^{-A})100(e^A - 1) - 100(-1 + e^{-A})
\end{align*}
$$

$$
\begin{align*}
= 100[e^A - 1] \cdots \text{⑥}
\end{align*}
$$

$e^x$ は単調増加だから $A$ が $\min$ の時 $Y$ も $\min$ である

$$
\begin{align*}
\frac{dA}{dv} = \frac{k e^{kv} v - e^{kv}}{v^2} = \frac{kv - 1}{v^2} e^{kv}
\end{align*}
$$

から、$v = \frac{1}{k} \ (>0)$ で $A$ は $\min$ である。⑤からこの時

$$
\begin{align*}
P = 100(e^{ek} - 1)
\end{align*}
$$

 \hfill(終)