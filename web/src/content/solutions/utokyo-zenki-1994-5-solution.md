---
university: "utokyo"
category: "zenki"
year: "1994"
question: "5"
type: "solution"
title: "UTOKYO 1994 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

**[研究]**

$\triangleright$ 問題は(2). 換言すると

$$
\begin{align*}
p = \frac{1}{n}, \quad q = \frac{1}{m}, \quad p+4q < 1
\end{align*}
$$

をみたす $(p,q)$ のうち

$$
\begin{align*}
E = \left(p - \frac{1}{2}\right)^2 + 2(q-1)^2
\end{align*}
$$

を最大にする $(p,q)$ は？

\medskip

$\to (p,q)$ をメインにするか $(n,m)$ をメインにするか.

＊ ① $(p,q)$ メインなら, 図示してしまうのが良さそう.
$E$ は, $p,q$ についてそれぞれ単調減少だから, $(p,q)$ は大きい程良い.
$\to$ 定右面, どちらかで場合分けし、どれが良いかギンミする.
$\Rightarrow$ ただ $\frac{1}{\text{◯}}$ の形が使いにくいかも.

＊ ② $(m,n)$ メインの時, $p+4q < 1 \iff 4n+m < nm$ から.
不定方程式を考えて, $m,n$ を極力小さくとれば良い.
$\longrightarrow (n-1)(m-4) > 4$ から, $m-4 \ge 1 \iff m \ge 5$ が必要.
さらに $m-4 \ge 5$ となれば, $n$ は任意.
$\Rightarrow$ こちらの方がよさそう.

\bigskip

## 【解】

 題意より, 下表をえる. ($r = 1 - p - 4q \quad \dots \textcircled{1}$)

|   1   |   2   |   3   |   4   |   5   |   6   |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| $q$ | $q$ | $p$ | $r$ | $q$ | $q$ |

(1) $1^\circ \ a+b \le 4$

1枚目の $a$ の値で場合分けして ($a=1, a=2, a=3$)

$$
\begin{align*}
P(A) = q(q+q+p) + q(q+q) + pq = 4q^2 + 2pq \quad \dots \textcircled{2}
\end{align*}
$$

$2^\circ \ a < b$

1と同様に ($a=1, a=2, a=3, a=4, a=5$)

$$
\begin{align*}
P(B) = q(1-q) + q(1-2q) + p(1-2q-p) + r(q+q) + q \cdot q
\end{align*}
$$

$$
\begin{align*}
= -p^2 + p - 4pq - 10q^2 + 4q \quad (\because \text{\textcircled{1}}) \quad \dots \textcircled{3}
\end{align*}
$$

\textcircled{2}, \textcircled{3} から

$$
\begin{align*}
E = 2(4q^2 + 2pq) + (-p^2 + p - 4pq - 10q^2 + 4q)
\end{align*}
$$

$$
\begin{align*}
= -p^2 + p - 2q^2 + 4q \quad \hfill \qed
\end{align*}
$$

\bigskip

(2) $\frac{1}{p} = n, \frac{1}{q} = m \; (n,m \in \mathbb{N})$ とおく. $0 < p, q, r < 1$ から,

$$
\begin{align*}
0 < \frac{1}{n}, \frac{1}{m} < 1, \quad 0 < 1 - \frac{1}{n} - \frac{4}{m} < 1
\end{align*}
$$

前者から, $n, m \ge 2$ であり, 後者から

$$
\begin{align*}
0 < 4n + m < mn
\end{align*}
$$

左側の不等式の成立は母から明らかなので, 右についてかんがえると,

$$
\begin{align*}
(n-1)(m-4) > 4 \quad \dots \textcircled{5}
\end{align*}
$$

又,

$$
\begin{align*}
E = -\left(p - \frac{1}{2}\right)^2 + \frac{1}{4} - 2(q-1)^2 + 2
\end{align*}
$$

$$
\begin{align*}
= \frac{9}{4} - \left(\frac{2-n}{2n}\right)^2 - 2\left(\frac{1-m}{m}\right)^2 \quad \dots \textcircled{6}
\end{align*}
$$

ここで, $y = f(x) = \frac{2-x}{2x}$, $y = g(x) = \frac{1-x}{x}$ のグラフは下図.

\begin{tikzpicture}[scale=0.9, >=stealth]
  \begin{scope}[shift={(0,0)}]
    \draw[->] (-0.5,0) -- (3,0) node[right] {$x$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
    \draw[dashed] (0,-0.5) -- (3,-0.5) node[right] {$y=-\frac{1}{2}$};
    \draw[domain=0.5:2.8, smooth, variable=\x, blue, thick] plot ({\x}, {(2-\x)/(2*\x)});
    \node[below left] at (2,0) {$2$};
    \node at (1.5,1) {$y = f(x)$};
  \end{scope}

  \begin{scope}[shift={(5,0)}]
    \draw[->] (-0.5,0) -- (3,0) node[right] {$x$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
    \draw[dashed] (0,-1) -- (3,-1) node[right] {$y=-1$};
    \draw[domain=0.4:2.8, smooth, variable=\x, red, thick] plot ({\x}, {(1-\x)/\x});
    \node[below left] at (1,0) {$1$};
    \node at (1.5,1) {$y = g(x)$};
  \end{scope}
\end{tikzpicture}

又, \textcircled{5} をみたす $(m,n)$ は以下のようになる.

|    $n$    |    $m$    |
|:-----------:|:-----------:|
|      2      | $m \ge 9$ |
|      3      | $m \ge 7$ |
|      4      | $m \ge 6$ |
|      5      | $m \ge 6$ |
| $n \ge 6$ | $m \ge 5$ |

左をみたす定義域内では, $\{f(n)\}^2, \{g(m)\}^2$ は共に単調増加だから, $E$ を最大にする候補は左表の等号成立時の $(n,m)$ である.

又, $n = 4, 5$ の時については $m \ge 6$ だから, $(n,m) = (5,6)$ の場合より $(n,m) = (4,6)$ の時の方が $E$ は大きい.

| $(n,m)$ | $\{f(n)\}^2 + 2\{g(m)\}^2$ |
|:--:|:---|
| $(2,9)$ | $0 + 2\left(\frac{8}{9}\right)^2 = \frac{128}{81}$ |
| $(3,7)$ | $\left(\frac{1}{6}\right)^2 + 2\left(\frac{6}{7}\right)^2 = \frac{7^2 + 2 \cdot 6^4}{6^2 \cdot 7^2}$ |
| $(4,6)$ | $\left(\frac{1}{4}\right)^2 + 2\left(\frac{5}{6}\right)^2 = \frac{209}{9 \cdot 16}$ |
| $(6,5)$ | $\left(\frac{1}{3}\right)^2 + 2\left(\frac{4}{5}\right)^2 = \frac{313}{9 \cdot 25}$ |

1.  $\displaystyle \frac{313}{9 \cdot 25} < \frac{209}{9 \cdot 16}, \quad \frac{209}{9 \cdot 16} < \frac{128}{81}$

2.  $\displaystyle \frac{7^2 + 2 \cdot 6^4}{6^2 \cdot 7^2} > \frac{313}{9 \cdot 25}$

このうち $\{f(n)\}^2 + 2\{g(m)\}^2$ がもっとも小さいのは $(n,m) = (6,5)$ の時で, この時 $E$ が最大. よって求める $(p,q)$ は $(p,q) = \left(\frac{1}{6}, \frac{1}{5}\right)$ である. \hfill $\qed$