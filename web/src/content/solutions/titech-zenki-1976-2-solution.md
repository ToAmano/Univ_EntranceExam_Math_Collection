---
university: "titech"
category: "zenki"
year: "1976"
question: "2"
type: "solution"
title: "TITECH 1976 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

与式の両辺0以上かつ，$1+4x^2>0$，$c>0$ から，平方根をとって，

$$
\begin{align*}
|b+x^2|>c\sqrt{1+4x^2}
\end{align*}
$$

$t=x^2$（$t\ge0$）として，

$$
\begin{align*}
|b+t|>c\sqrt{1+4t}\quad\cdots\text{①}
\end{align*}
$$

である．$b\le0$ の時，$t=-b$（$\ge0$）を①に代入すると

$$
\begin{align*}
0>c\sqrt{1-4b}
\end{align*}
$$

となり不適．したがって，$0<b$ が必要である．この時，①から

$$
\begin{align*}
b>c\sqrt{4t+1}-t\equiv f(t) \quad\cdots\text{②}
\end{align*}
$$

とすると，

$$
\begin{align*}
f'(t)=\frac{4c}{2\sqrt{4t+1}}-1=\frac{2c-\sqrt{4t+1}}{\sqrt{4t+1}}
\end{align*}
$$

から，$c$によって以下のようになる．

\textbf{$1^\circ\ c\le\dfrac{1}{2}$ の時}

$f'(t)\le0$ となり，$f(t)$ は単調減少である．したがって②が全ての $t$ で成立する条件は

$$
\begin{align*}
b>f(0)=c \quad\cdots\text{③}
\end{align*}
$$

\textbf{$2^\circ\ \dfrac{1}{2}\le c$ の時}

下表をうる．

| $t$  |    $0$     | $c^2-\dfrac14$ |              |
|:------:|:------------:|:----------------:|:------------:|
| $f'$ |    $+$     |      $0$       |    $-$     |
| $f$  | $\nearrow$ |                  | $\searrow$ |

したがって，$1^\circ$ と同様に，条件は

$$
\begin{align*}
b>f\left(c^2-\frac14\right)=c^2+\frac14 \quad\cdots\text{④}
\end{align*}
$$

以上③④は $b>0$ をみたすから，

$$
\begin{align*}
0<c\le\frac12\ \text{の時}\quad b>c
\end{align*}
$$

$$
\begin{align*}
\frac12\le c\ \text{の時}\quad b>c^2+\frac14
\end{align*}
$$