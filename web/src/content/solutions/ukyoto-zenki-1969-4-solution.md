---
university: "ukyoto"
category: "zenki"
year: "1969"
question: "4"
type: "solution"
title: "UKYOTO 1969 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $A$からの流出速度を $v$，水の単位体積あたりの重さを $w$ とすると，

1.  時刻 $k$ における総水溶液は $vk$

2.  その重さは
    

$$
\begin{align*}
\begin{aligned}
    w \int_0^k (1+ae^{-bt}) v \, dt &= \left[ t - \frac{a}{b} e^{-bt} \right]_0^k v w \\
    &= vw \left[ \left( k - \frac{a}{b} e^{-bk} \right) - \left( -\frac{a}{b} \right) \right] \\
    &= vw \left( k + \frac{a}{b} - \frac{a}{b} e^{-bk} \right)
    \end{aligned}
\end{align*}
$$

だから，求める比重は

$$
\begin{align*}
\frac{vw \left( k + \frac{a}{b}(1 - e^{-bk}) \right)}{vk} \cdot \frac{1}{w} = 1 + \frac{a}{bk} (1 - e^{-bk})
\end{align*}
$$

\small

|  |
|:---|
| **補足メモ**: |
| 「比重…水に対する相対重さ」という解釈で良いのかな |
| $\Rightarrow \frac{(\text{重さ})}{(\text{総量})}$ が単位あたり重さ，これと水の重さでくらべる |