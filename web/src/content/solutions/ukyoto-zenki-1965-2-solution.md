---
university: "ukyoto"
category: "zenki"
year: "1965"
question: "2"
type: "solution"
title: "UKYOTO 1965 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $k > 0 \dots \text{①}$。根の1つを $\alpha$ とすると、$k$ についての恒等式

$$
\begin{align*}
(\alpha - a)k^2 + (\alpha^2 - 4\alpha + 4)k + b - 4\alpha = 0
\end{align*}
$$

が成り立つから

$$
\begin{align*}
a = \alpha, \quad (\alpha - 2)^2 = 0, \quad b = 4\alpha
\end{align*}
$$

$$
\begin{align*}
\Rightarrow \begin{cases} \alpha = 2 \\ a = 2 \\ b = 8 \end{cases} \quad \text{--- (H)}
\end{align*}
$$

である。代入して与方程式は

$$
\begin{align*}
k x^2 - (k+2)^2 x + (2k^2 + 4k + 8) = 0
\end{align*}
$$

$$
\begin{align*}
(x - 2)\left(k x - (k^2 + 2k + 4)\right) = 0
\end{align*}
$$

だから、もう片方の解は

$$
\begin{align*}
x = \frac{k^2 + 2k + 4}{k} = k + \frac{4}{k} + 2 \ge 8
\end{align*}
$$

($\text{∵ } k > 0$ から AM-GM, 等号成立は $k = \frac{4}{k} \ \therefore k = 2$)

だから、$k = 2$ の時 $\min 8$ をとる。