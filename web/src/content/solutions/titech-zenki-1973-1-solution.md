---
university: "titech"
category: "zenki"
year: "1973"
question: "1"
type: "solution"
title: "TITECH 1973 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

まず, $\frac{p}{q} + \frac{2}{3} \dots$ ①である. このもとで考える. 与式から

$$
\begin{align*}
-\frac{1}{q^2} < \frac{p}{q} - \frac{2}{3} < \frac{1}{q^2}\quad\dots\text{②}
\end{align*}
$$

まず $q > 0$ の時, ②の両辺 $q^2$ をかけて, セイリする.

$$
\begin{align*}
\frac{2}{3}q - \frac{1}{q} < p < \frac{2}{3}q + \frac{1}{q}\quad\dots\text{③}
\end{align*}
$$

$q = 3m \ (m \in \mathbb{N})$ の時, $|\frac{1}{q}| < 1$ から③をみたす $(p,q)$ は $(2m, 3m)$ となるが, ①からこれは不適.

次に $q = 3m+1 \ (m \in \mathbb{Z}_{\ge 0})$ の時, $\frac{2}{3}q = 2m + \frac{2}{3}$ だから右図及び $\frac{1}{q} = \frac{1}{3m+1}$ が単調減少であることから,

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1973/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $q=3m+1$の場合の$p$の範囲</figcaption>
</figure>

1.  $\frac{2}{3} \le \frac{1}{q} \iff m=0$ の時, $p = 2m, 2m+1$

2.  $\frac{1}{3} \le \frac{1}{q} < \frac{2}{3} \iff \frac{1}{2} < m \le \frac{4}{3}$ の時, $m$ がなく不適.

3.  $\frac{1}{q} < \frac{1}{3}$ の時, ③をみたす $p$ はない.

最後に $q = 3m-1 \ (m \in \mathbb{N})$ の時, $\frac{2}{3}q = 2m - \frac{2}{3}$ だから右図より

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1973/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $q=3m-1$の場合の$p$の範囲</figcaption>
</figure>

1.  $\frac{2}{3} \le \frac{1}{q} \iff m \le \frac{5}{6}$ の時, これをみたす $m$ はない.

2.  $\frac{1}{3} \le \frac{1}{q} < \frac{2}{3} \iff \frac{5}{6} < m \le \frac{4}{3}$ の時, $m=1$ で $p = 2m-1$.

3.  $\frac{1}{q} < \frac{1}{3}$ の時, ③をみたす $p$ はない.

以上から, $q > 0$ の時, $(p,q) = (0,1), (1,1), (1,2) \dots$ ④である.

さらに, $q < 0$ の時, ②の両辺に $q^2$ をかけて,

$$
\begin{align*}
\frac{2}{3}q + \frac{1}{q} < p < \frac{2}{3}q - \frac{1}{q}
\end{align*}
$$

$q = 3m \ (m \in \mathbb{Z})$ は $q > 0$ の時と同様不適である.

$q = -(3m+1) \ (m \in \mathbb{Z}_{\ge 0})$ の時, $\frac{2}{3}q = -(2m + \frac{2}{3})$ だから, 同様に絞ると,

<figure id="fig_3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1973/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $q=-(3m+1)$の場合の$p$の範囲</figcaption>
</figure>

$m=0$ の時 $p = -(2m+1), -2m$ である.

$q = -(3m-1) \ (m \in \mathbb{N})$ の時 $\frac{2}{3}q = -(2m - \frac{2}{3})$ で同様に $m=1$ の時 $p = -2m+1$.

以上から, $q < 0$ の時, $(p,q) = (0,-1), (-1,-1), (-1,-2) \dots$ ⑤である.

④, ⑤から

$$
\begin{align*}
(p,q) = (0, \pm 1), (\pm 1, \pm 1), (\pm 1, \pm 2) \quad(\text{複号同順})
\end{align*}
$$