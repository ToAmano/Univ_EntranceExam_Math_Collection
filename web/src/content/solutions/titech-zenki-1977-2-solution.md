---
university: "titech"
category: "zenki"
year: "1977"
question: "2"
type: "solution"
title: "TITECH 1977 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$A=\{20,21,22,23,24\}$，$B=\{25,26,27,28,29\}$，$C=\{80,81,82,83,84\}$，
$D=\{85,86,87,88,89\}$ とする．題意の試行では，$A,B$ のうちから1つ，$C,D$ のうちから1つ数をとり出す．その組は以下で全てである．

|       | $A$ | $B$ |
|:-----:|:-----:|:-----:|
| $C$ |  ア   |  イ   |
| $D$ |  ウ   |  エ   |

このうち，アでは必ず $S\ge S'$，エでは必ず $S<S'$ となる． $\cdots$①

そこで，以下イ，ウについて考える．

**$1^\circ$ イの時**

$B,C$ の数は，四捨五入すると各々30,80になるから，$S'=2400$ である．一方，$S$ は以下のようになる．（$\bigcirc$ は $S<S'$ を，$\times$ は $S\ge S'$ を表す）

| $C\backslash B$ | 25 | 26 | 27 | 28 | 29 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 80 | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ |
| 81 | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ |
| 82 | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ |
| 83 | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\times$ |
| 84 | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\bigcirc$ | $\times$ |

**$2^\circ$ ウの時**

$A,D$ の数は，四捨五入すると各々20,90になるから，$S'=1800$ である．$S$ の表は以下

| $D\backslash A$ |      20      |      21      |     22     |     23     |     24     |
|:-----------------:|:------------:|:------------:|:----------:|:----------:|:----------:|
|        85         | $\bigcirc$ | $\bigcirc$ | $\times$ | $\times$ | $\times$ |
|        86         | $\bigcirc$ |  $\times$  | $\times$ | $\times$ | $\times$ |
|        87         | $\bigcirc$ |  $\times$  | $\times$ | $\times$ | $\times$ |
|        88         | $\bigcirc$ |  $\times$  | $\times$ | $\times$ | $\times$ |
|        89         | $\bigcirc$ |  $\times$  | $\times$ | $\times$ | $\times$ |

①，$1^\circ$，$2^\circ$ から，全てのえらび方 $10^2=100$ 通りのうち，$S<S'$ となるのは，

$$
\begin{align*}
25+23+6=54 \text{（通り）}
\end{align*}
$$

（① ，$1^\circ$ ，$2^\circ$ の順に対応）

だから，もとめるカクリツは $\dfrac{54}{100}=\dfrac{27}{50}$