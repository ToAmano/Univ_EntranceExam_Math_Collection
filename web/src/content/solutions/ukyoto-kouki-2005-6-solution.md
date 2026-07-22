---
university: "ukyoto"
category: "kouki"
year: "2005"
question: "6"
type: "solution"
title: "UKYOTO 2005 kouki Q6 (solution)"
---

## 【解】

  表の出た100円玉の枚数$X$, 500円玉の枚数$Y$とする.
  $X \le Y-1$ となる確率$P(X \le Y-1)$を求めれば良い.
  この時，裏の出た枚数は100円玉$n-X$枚，500円玉は$n+1-Y$である．
  「表の出た $100$ 円玉の枚数より表の出た $500$ 円玉の枚
  数の方が多い」とはすなわち「裏の出た $100$ 円玉の枚数より裏の出た $500$ 円玉の枚数が少ない」
  ということだから，
  

$$
\begin{align}
P(X \le Y-1)
     & = P(n-X+1 \ge n+1-Y)             \\& = P(Y \le X) \label{2005-6:eq:1}
\end{align}
$$

  である．
  ここで，これら二つのパターンは枚数に関して全てのパターンを尽くしており，
  

$$
\begin{align}
P(X \le Y-1) + P(Y \le X) = 1 \label{2005-6:eq:2}
\end{align}
$$

  である．この様子を[図1](#2005-6:fig:1)に示す．

  [(式2)](#2005-6:eq:1,2005-6:eq:2)より
  

$$
\begin{align*}
P(X+1 \le Y) = \frac{1}{2}
\end{align*}
$$

  が求める答えである．

  

<figure id="2005-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/2005/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $X$と$Y$のとりうるパターンを平面上に図示した様子．</figcaption>
</figure>

  **[解2]**
  1玉の500円玉に注目し, その表裏で場合分けする.
  残り$n$枚ずつの$100$円玉，$500$円玉の表の枚数をそれぞれ $X, Y$ とする.

  **$1^\circ$ 表の時**
  残り$n$枚ずつ投げて, $X \le Y$ となれば良く, 確率 $P(X \le Y)$

  **$2^\circ$ 裏の時**
  残り$n$枚ずつ投げて, $X < Y$ となれば良く, 確率 $P(X < Y)$

  コインが$n$枚ずつあるため対称性から $P(X < Y) = P(X > Y)$ だから
  \[ \frac{1}{2} \left( P(X \le Y) + P(X \not< Y) \right) = \frac{1}{2} \left( P(X \le Y) + P(X \ge Y) \right) = \frac{1}{2} \]

  **[解3]**
  500円が$k$枚表である確率を$P_k$とおくと,
  100円が$j$枚表である確率を$q_j$とおくと,
  

$$
\begin{align*}
P_k & = {}_{n+1}\mathrm{C}_k \left(\frac{1}{2}\right)^{n+1}\\
    q_j & = {}_{n}\mathrm{C}_j \left(\frac{1}{2}\right)^{n}
\end{align*}
$$

  で，
  

$$
\begin{align*}
P & = \sum_{k=1}^{n+1} P_k (q_0 + \dots + q_{k-1})                                                                                                 \\& = \left(\frac{1}{2}\right)^{2n+1}\sum_{k=1}^{n+1}{}_{n+1}\mathrm{C}_k ({}_n\mathrm{C}_0 + \dots + {}_n\mathrm{C}_{k-1}) \quad\dots\text{①}
\end{align*}
$$

  ここで, $A = \sum_{k=1}^{n+1} {}_{n+1}\mathrm{C}_k ({}_n\mathrm{C}_0 + \dots + {}_n\mathrm{C}_{k-1})$ とおくと, $A$ は $(1+x)^n (1+x)^{n+1}$ の展開項のうち, $x^{n+1}$ 次以上
  のもの和である.
  \[ (x+1)^{2n+1} = {}_{2n+1}\mathrm{C}_0 x^0 + \dots + {}_{2n+1}\mathrm{C}_n x^n + {}_{2n+1}\mathrm{C}_{n+1} x^{n+1} + \dots + {}_{2n+1}\mathrm{C}_{2n+1} x^{2n+1} \]
  として, ${}_{2n+1}\mathrm{C}_{2n+1-k} = {}_{2n+1}\mathrm{C}_k$ だから.
  \[ 2^{2n+1} = 2 \left({}_{2n+1}\mathrm{C}_0 + \dots + {}_{2n+1}\mathrm{C}_n \right) = 2A \]
  \[ \therefore A = 2^{2n} \quad \dots \text{②} \]
  ①②から,
  \[ P = \left(\frac{1}{2}\right)^{2n+1} 2^{2n} = \frac{1}{2} \]

  $\cdots$(答)

  
  

## 【解説】