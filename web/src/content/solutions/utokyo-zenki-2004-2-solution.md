---
university: "utokyo"
category: "zenki"
year: "2004"
question: "2"
type: "solution"
title: "UTOKYO 2004 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{proof}[解]
(1) 合同の法を $100$ とする. 自然数 $n$ が, $n \equiv 10\alpha + \beta \quad (\alpha, \beta = 0, 1, \dots, 9)$ をみたしているとする. $n^2$ が 3 桁以上の時, $9^2 = 81$ から $\alpha \ge 1$ である. 題意から

$$
\begin{align*}
n^2 = 100\alpha^2 + 20\alpha\beta + \beta^2 \equiv 20\alpha\beta + \beta^2 \equiv 10a + b
\end{align*}
$$

$$
\begin{align*}
\therefore 10(2\alpha\beta - a) + (\beta^2 - b) \equiv 0
\end{align*}
$$

$\beta$ で場合分けする.

|  $\beta$   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
|:------------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|    $b$     |  0  |  1  |  4  |  9  |  6  |  5  |  6  |  9  |  4  |  1  |
| $a$ の偶奇 | 偶  | 偶  | 偶  | 偶  | 奇  | 偶  | 奇  | 偶  | 偶  | 偶  |

このうち $a+b$ が偶数になるのは, $b = 0$ or $4$ の時である.

\medskip
(2) 合同の法を $10000$ とする. (1)から, 題意の平方数は

$$
\begin{align*}
n^2 \equiv 0 \text{ or } 4444
\end{align*}
$$

である. $n^2 \equiv 0$ の時は, たしかに $n^2$ は 10000 で割り切れる. $n^2 \equiv 4444$ の時をかんがえる.

この時, $m \in \mathbb{N}$ として

$$
\begin{align*}
n^2 = 10000 m + 4444 = 4(2500 m + 1111)
\end{align*}
$$

となり, $2500m + 1111$ が平方数になるが, (1)に矛盾. よってこのような平方数はない.

以上から示された. \qed
\end{proof}