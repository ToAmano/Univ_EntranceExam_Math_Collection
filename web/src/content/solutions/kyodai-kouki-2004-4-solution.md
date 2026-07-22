---
university: "kyodai"
category: "kouki"
year: "2004"
question: "4"
type: "solution"
title: "KYODAI 2004 kouki Q4 (solution)"
---

## 【解】

  $OX = OA = t$とおく ($0 < t $)．$t$の整数部分を求めれば良い．
  題意の条件から，角点の関係は[図1](#2004-4:fig:1)のようにとなる．

  

<figure id="2004-4:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2004/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $A,B,C,X$の関係</figcaption>
</figure>

  題意の条件より
  

$$
\begin{align*}
\tan 44^\circ& = \frac{t}{t+1}\\\tan 45^\circ& = 1
\end{align*}
$$

  だから，加法定理により$\tan 1^{\circ}$を評価すると
  

$$
\begin{align*}
\tan 1^\circ& = \tan(45^\circ-44^\circ)                                               \\& = \frac{\tan 45^\circ - \tan 44^\circ}{1 + \tan 45^\circ \tan 44^\circ}\\& = \frac{1 - \frac{t}{t+1}}{1 + 1 \cdot \frac{t}{t+1}}\\& = \frac{1}{2t+1}
\end{align*}
$$

  となる．題意の不等式に代入して
  

$$
\begin{align*}
0.01745 < \frac{1}{2t+1} < 0.01746 \\
    57.2 < 2t+1 < 57.3                 \\
    28.1 < t < 28.15
\end{align*}
$$

  となり，求める答えは
  

$$
\begin{align*}
t = 28 [m]
\end{align*}
$$

  である．  $\cdots$(答)

  
  

## 【解説】