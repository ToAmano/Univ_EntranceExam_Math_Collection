---
university: "utokyo"
category: "zenki"
year: "2009"
question: "3"
type: "solution"
title: "UTOKYO 2009 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (1) 1に4色すべてが入っている確率を $\alpha$ とすると、対称性から、求める確率 $P_1$ は

$$
\begin{align*}
P_1 = \alpha^2 \cdots (1)
\end{align*}
$$

である。$\alpha$ について、5回の操作で、4つの色のうち、3つの色が1回ずつ、の残りの1色が2回出るので、

$$
\begin{align*}
\alpha = 4 \cdot{}_5C_2 \cdot{}_3C_1 \cdot{}_2C_1 \cdot \left(\frac{1}{4}\right)^5 = \frac{15}{4^3}
\end{align*}
$$

だから、(1)より

$$
\begin{align*}
P_1 = \frac{3^2 \cdot 5^2}{4^6} \quad \text{\#\!}
\end{align*}
$$

(2) 5回の操作で、4色全てが少なくとも1回出れば良く、

$$
\begin{align*}
P_2 = \alpha = \frac{3 \cdot 5}{4^3} \quad \text{\#\!}
\end{align*}
$$

(3) 10回の操作で、4色全てが少なくとも2回出れば良い。この時、残りの2つの玉について、

1.  2つとも同じ色

2.  2つとも違う色

がありうる。$1^\circ$ の時の確率は

$$
\begin{align*}
4 \times{}_{10}C_{4} \cdot{}_{6}C_{2} \cdot{}_{4}C_{2} \cdot \left(\frac{1}{4}\right)^{10} = 3^3 \cdot 5^2 \cdot 7 \left(\frac{1}{4}\right)^8
\end{align*}
$$

$2^\circ$ の時の確率は

$$
\begin{align*}
_{4}C_{2} \cdot{}_{10}C_{3} \cdot{}_{7}C_{3} \cdot{}_{4}C_{2} \cdot \left(\frac{1}{4}\right)^{10} = 3^3 \cdot 5^2 \cdot 7 \cdot 2 \left(\frac{1}{4}\right)^8
\end{align*}
$$

だから、

$$
\begin{align*}
P_3 = 3^3 \cdot 5^2 \cdot 7 \cdot \left(\frac{1}{4}\right)^8 (1+2) = 3^4 \cdot 5^2 \cdot 7 \left(\frac{1}{4}\right)^8
\end{align*}
$$

(1)とあわせて、

$$
\begin{align*}
\frac{P_3}{P_1} = \frac{4^6 \cdot 3^4 \cdot 5^2 \cdot 7}{3^2 \cdot 5^2 \cdot 4^8} = \frac{3^2 \cdot 7}{4^2} = \frac{63}{16} \quad \text{\#\!}
\end{align*}
$$