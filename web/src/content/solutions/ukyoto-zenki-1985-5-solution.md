---
university: "ukyoto"
category: "zenki"
year: "1985"
question: "5"
type: "solution"
title: "UKYOTO 1985 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 2枚の硬貨A, Bとし、表の出る確率が各々 $a, b$ だとする。\\
確率変数 $X_1, X_2$ を以下のように定める。

$$
\begin{align*}
X_1 = \begin{cases} 0 & (A\text{がウラ}) \\ 1 & (A\text{が表}) \end{cases} \quad X_2 = \begin{cases} 0 & (B\text{がウラ}) \\ 1 & (B\text{が表}) \end{cases}
\end{align*}
$$

すると、$X = X_1 + X_2$ で、$X_1, X_2$ は独立だから、

$$
\begin{align*}
\begin{cases}
P(X=0) = P(X_1=0) \cdot P(X_2=0) \\
P(X=1) = P(X_1=0) \cdot P(X_2=1) + P(X_1=1) \cdot P(X_2=0) \\
P(X=2) = P(X_1=1) \cdot P(X_2=1)
\end{cases} \quad \cdots \text{①}
\end{align*}
$$

である。$P(X_1=0) = 1-a, P(X_1=1) = a$ などを①に代入して

$$
\begin{align*}
\begin{cases}
P(X=0) = (1-a)(1-b) \\
P(X=1) = (1-a)b + (1-b)a \\
P(X=2) = ab
\end{cases} \quad \cdots \text{②}
\end{align*}
$$

(1) $P(X=k) = {}_2\mathrm{C}_k \cdot p^k (1-p)^{2-k}$ の時、②に代入して、

$$
\begin{align*}
\begin{cases}
(1-p)^2 = (1-a)(1-b) = 1 + ab - (a+b) \\
2p(1-p) = a + b - 2ab \\
p^2 = ab
\end{cases}
\end{align*}
$$

$\alpha = a+b, \beta = ab$ として、

$$
\begin{align*}
\begin{cases}
\beta - \alpha = (1-p)^2 - 1 = p(p-2) \\
-2\beta + \alpha = 2p(1-p) \\
\beta = p^2
\end{cases}
\end{align*}
$$

第3式を1, 2式に代入して\\
$\alpha = p^2 - p(p-2) = 2p$\\
$\alpha = 2p(1-p) + 2\beta = 2p$\\
から、$a, b$ は $x$ の2次式 $x^2 - 2px + p^2 = 0$ の2解で、$(a, b) = (p, p) \quad \text{//} $

(2) $P(X=k) = \frac{1}{3}$ の時、②に代入して

$$
\begin{align*}
\frac{1}{3} = 1 + \beta - \alpha = \alpha - 2\beta = \beta
\end{align*}
$$

よって、$(\alpha, \beta) = \left(1, \frac{1}{3}\right)$ だから、$a, b$ は $t$ の2次式 $t^2 - t + \frac{1}{3} = 0$ の2解だが、この判別式を $D$ として

$$
\begin{align*}
D = 1 - \frac{4}{3} = -\frac{1}{3} < 0
\end{align*}
$$

から、$a, b \in \mathbb{R}$ に反し矛盾。よって $(a, b)$ は存在しない。$\text{//} $