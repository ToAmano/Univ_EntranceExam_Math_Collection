---
university: "ukyoto"
category: "zenki"
year: "1998"
question: "5"
type: "solution"
title: "UKYOTO 1998 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 青、赤、白を $\text{B}, \text{R}, \text{W}$ とし、たとえば青球の1番を $\text{B-}1$ と表す。

(1) 3点となるのは、色も番号も異なる3つの玉をとりだしたときで、

$$
\begin{align*}
A(3) = 3 \times 2 \times 1 = 6
\end{align*}
$$

2点となることはありえず、$A(2) = 0$

1点となるのは、2つの玉のみ、色又は番号が被る時で、全く被らない1つのキメ方から

$$
\begin{align*}
A(1) = 9 \times (_4\text{C}_2 - 2) = 36
\end{align*}
$$

余事象から

$$
\begin{align*}
A(0) = _9\text{C}_3 - (6 + 0 + 36) = 42
\end{align*}
$$

(2)

$$
\begin{align*}
E &= 3 \times\frac{6}{_9\text{C}_3} + 2 \times 0 + 1 \times\frac{36}{_9\text{C}_3}\\&= \frac{18 + 36}{84} = \frac{9}{14}
\end{align*}
$$