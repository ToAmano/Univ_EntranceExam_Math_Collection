---
university: "titech"
category: "zenki"
year: "1980"
question: "3"
type: "solution"
title: "TITECH 1980 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$(t,e^t)$ における接線 $\ell_t$ は，$(e^x)'=e^x$ より，

$$
\begin{align*}
\ell_t: y=e^t(x-t)+e^t \quad\cdots\text{①}
\end{align*}
$$

である．これが $(a,b)$ を通る時，

$$
\begin{align*}
b=e^t(a-t)+e^t\equiv f(t) \quad\cdots\text{②}
\end{align*}
$$

$y=e^x$ では，接点が異なれば接線が異なるので，②をみたす $t$ の数が $(a,b)$ から引きうる接線の数に等しい．

$$
\begin{align*}
f'(t)=e^t(a+1-t-1)=e^t(a-t)
\end{align*}
$$

から，下表をうる．

| $t$  |              |  $a$  |              |
|:------:|:------------:|:-------:|:------------:|
| $f'$ |    $+$     |  $0$  |    $-$     |
| $f$  | $\nearrow$ | $e^a$ | $\searrow$ |

したがって，$f(t)\to-\infty\ (t\to+\infty)$，$f(t)\to0\ (t\to-\infty)$ から，$y=f(t)$ のグラフは右上図のようになる．したがって，$a$ を固定した時，②は $y=b$，$y=f(t)$ のグラフの交点で与えられるので

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1980/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=f(t)$のグラフの概形</figcaption>
</figure>

$$
\begin{align*}
\begin{cases}
b\le0\ \text{の時，解は}1\text{つ} \\
0<b<e^a\ \text{の時，}2\text{つ} \\
b=e^a\ \text{の時，}1\text{つ} \\
b>e^a\ \text{の時，}0\text{個}
\end{cases}
\end{align*}
$$

となる．$a$ の固定を解除して，

$$
\begin{align*}
\begin{cases}
b\le0\ \text{または}\ b=e^a\ \text{の時}\quad 1\text{個} \\
0<b<e^a\ \text{の時}\quad 2\text{個} \\
b>e^a\ \text{の時}\quad 0\text{個}
\end{cases}
\end{align*}
$$