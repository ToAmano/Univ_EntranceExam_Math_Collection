---
university: "utokyo"
category: "zenki"
year: "2010"
question: "2"
type: "solution"
title: "UTOKYO 2010 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (1) $a_k = \int_{0}^{\frac{1}{k}} \frac{1-x}{x+k} dx$ とおく。

$$
\begin{align*}
a_k &= \int_{0}^{\frac{1}{k}}\left\{ -1 + \frac{k+1}{x+k}\right\} dx = \left[ -x + (k+1)\log(x+k) \right]_{0}^{\frac{1}{k}}\\&= -\frac{1}{k} + (k+1)\log\frac{k+1}{k}
\end{align*}
$$

だから、$k \in \mathbb{N}$ より

$$
\begin{align*}
\text{(与式)} \Leftrightarrow \frac{2k+3}{2(k+1)^2} < \log\frac{k+1}{k} < \frac{2k+1}{2k(k+1)} \cdots \text{①}
\end{align*}
$$

である。ここで、右図の面積を比較して、

$$
\begin{align*}
\frac{1}{k+1/2} < \int_{k}^{k+1} \frac{1}{x} dx < \frac{1}{2}\left(\frac{1}{k} + \frac{1}{k+1}\right) \cdots *
\end{align*}
$$

$$
\begin{align*}
\frac{2}{2k+1} < \log\frac{k+1}{k} < \frac{2k+1}{2k(k+1)}
\end{align*}
$$

であり、

$$
\begin{align*}
\frac{2}{2k+1} - \frac{2k+3}{2(k+1)^2} = \frac{1}{2(k+1)^2(2k+1)} > 0 \quad \left( y = \frac{1}{x}, y'' = \frac{2}{x^3} \text{ より } y = \frac{1}{x} \text{ は下に凸} \right)
\end{align*}
$$

とあわせて、

$$
\begin{align*}
\frac{2k+3}{2(k+1)^2} < \log\frac{k+1}{k} < \frac{2k+1}{2k(k+1)}
\end{align*}
$$

だから①は示された。よって不等式は成立。

(2) ①で $k=n, n+1, \dots, m-1$ として足して、

$$
\begin{align*}
\sum_{k=n}^{m-1} \frac{1}{k+1} + \sum_{k=n}^{m-1} \frac{1}{(k+1)^2} < \log\frac{m}{n} < \frac{1}{2}\sum_{k=n}^{m-1}\left(\frac{1}{k} + \frac{1}{k+1}\right)
\end{align*}
$$

$$
\begin{align*}
\sum_{k=n+1}^{m} \frac{1}{k} < \log\frac{m}{n} - \sum_{k=n+1}^{m} \frac{1}{k} < \frac{m-n}{2mn} \cdots \text{②}
\end{align*}
$$

ここで、$\sum_{k=n+1}^{m} \frac{1}{k^2}$ は右図斜線部だから、面積比較して、

$$
\begin{align*}
\sum_{k=n+1}^{m}\frac{1}{k^2}&> \int_{n+1}^{m+1}\frac{1}{x^2} dx = \left[ -\frac{1}{x}\right]_{n+1}^{m+1}\\&= \frac{1}{n+1} - \frac{1}{m+1}\\&= \frac{m-n}{(m+1)(n+1)}
\end{align*}
$$

だから、②に代入して

$$
\begin{align*}
\frac{m-n}{(m+1)(n+1)} < \log\frac{m}{n} - \sum_{k=n+1}^{m} \frac{1}{k} < \frac{m-n}{2mn} \quad \text{終}
\end{align*}
$$

[別]
① 最後の評価は、

$$
\begin{align*}
\sum_{k=n+1}^{m} \frac{1}{k^2} > \sum_{k=n+1}^{m} \frac{1}{k(k+1)} = \frac{1}{n+1} - \frac{1}{m+1}
\end{align*}
$$

でも良い。

② $a_k$ の表式から

$$
\begin{align*}
\frac{1}{2(k+1)} < -1 + (k+1)\log\frac{k+1}{k} < \frac{1}{2k}
\end{align*}
$$

$$
\begin{align*}
\frac{1}{2(k+1)^2} < \log\frac{k+1}{k} - \frac{1}{k+1} < \frac{1}{2k(k+1)}
\end{align*}
$$

として $k$ について和をとっても良い。