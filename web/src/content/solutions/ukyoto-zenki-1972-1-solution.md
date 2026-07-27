---
university: "ukyoto"
category: "zenki"
year: "1972"
question: "1"
type: "solution"
title: "UKYOTO 1972 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] ベクトルの2つの公理を①, ②とする. すなわち,

$$
\begin{align*}
\vec{A} + \vec{B} = \vec{B} + \vec{A} \quad \cdots \text{①}
\end{align*}
$$

$$
\begin{align*}
(\vec{A} + \vec{B}) + \vec{C} = \vec{A} + (\vec{B} + \vec{C}) \quad \cdots \text{②}
\end{align*}
$$

以下, $\vec{S_n} = \sum_{k=1}^n \vec{A_k}$, $\vec{T_n} = \sum_{k=1}^n \vec{B_k}$ とする. $\vec{S_n} = \vec{T_n} \quad \cdots$ ③ を帰納的に示す.

### [補題1]

任意のベクトル $\vec{a_1}, \dots, \vec{a_n}$ に対し ($n \ge 2$)

$$
\begin{align*}
\vec{a_1} + \dots + \vec{a_n} = \vec{a_2} + \vec{a_3} + \dots + \vec{a_n} + \vec{a_1} \quad \cdots \star
\end{align*}
$$

(証) 帰納法による. $n=2$ の時は $\star$ は ①に他ならない. $n=k$ での成立を仮定すると, $n=k+1$ の時

$$
\begin{align*}
\vec{a_1} + \dots + \vec{a_{k+1}}&= \vec{a_1} + \dots + \vec{a_{k-1}} + (\vec{a_k} + \vec{a_{k+1}}) \quad(\because\text{②}) \\&= \vec{a_2} + \dots + (\vec{a_k} + \vec{a_{k+1}}) + \vec{a_1}\quad(\because\text{仮定}) \\&= \vec{a_2} + \dots + \vec{a_k} + \vec{a_{k+1}} + \vec{a_1}\quad(\because\text{②})
\end{align*}
$$

ゆえに $n=k+1$ でも $\star$ は成立.
以上から $\star$ は示された. \hfill 終

\bigskip
まず, $n=1$ の時. ③ $\iff \vec{A_1} = \vec{B_1}$ でこれは定義から成立する. そこで $i \in \mathbb{N}$ に対し, $n \le i$ での③の成立を仮定する. $n=i+1$ の時, $k=0, 1, \dots, i$ に対して,

$$
\begin{align*}
\vec{A_{i+1}} = \vec{B_{k+1}}
\end{align*}
$$

なる $k$ があることに注意する.

1.  $k=i$ の時
    

$$
\begin{align*}
\vec{T_{i+1}}&= \vec{T_i} + \vec{B_{i+1}}\\&= \vec{S_i} + \vec{A_{i+1}}\quad(\because\text{仮定}, \vec{A_{i+1}} = \vec{B_{i+1}}) \\&= \vec{S_{i+1}}
\end{align*}
$$

    となり, $n=i+1$ でも ③は成立.

2.  $k \ne i$ の時
    

$$
\begin{align*}
\vec{T_{i+1}}&= \vec{B_1} + \dots + \vec{B_k} + \vec{B_{k+1}} + \vec{B_{k+2}} + \dots + \vec{B_{i+1}}\\&= \vec{B_{k+1}} + \vec{B_1} + \dots + \vec{B_k} + \vec{B_{k+2}} + \dots + \vec{B_{i+1}}\quad(\because\text{仮定}) \\&= \vec{B_1} + \dots + \vec{B_k} + \vec{B_{k+2}} + \dots + \vec{B_{i+1}} + \vec{B_{k+1}}\quad(\because\text{補題1}) \\&= \vec{S_{i+1}}\quad(\because 1^\circ\text{に帰着})
\end{align*}
$$

以上 $1^\circ, 2^\circ$ から, $n=i+1$ でも ③は成立する. ゆえに③は示された. \hfill 終