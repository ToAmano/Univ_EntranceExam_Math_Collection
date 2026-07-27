---
university: "ukyoto"
category: "zenki"
year: "1968"
question: "1"
type: "solution"
title: "UKYOTO 1968 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

1.  **正しい**

    対偶をとると「$a > b \implies a \neq b$」だからこれは明らか.

2.  **正しくない**

    座標平面で $A(0,0)$, $B(1,0)$, $C(1,1)$, $D(0,1)$ とすると, どの3点も一直線上にないが,
    

$$
\begin{align*}
\vec{AB} + \vec{CD} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \begin{pmatrix} -1 \\ 0 \end{pmatrix} = \vec{0}
\end{align*}
$$

    である.

3.  **正しい**

    まず, $A=B$を示す. $A \subset B \dots \text{①}$ である. 次に,
    

$$
\begin{align*}
B \subset C \subset A
\end{align*}
$$

    だから $B \subset A \dots \text{②}$. ①, ②から $A=B$ である. 同様にして $B=C$ も示されるので
    

$$
\begin{align*}
A=B=C
\end{align*}
$$

4.  **正しい**

    帰納法で示す. $n=5$の時, $25 < 32$となって成立. $n=k \, (k \in \mathbb{N}, k \geqq 5)$ での成立を仮定し, $n=k+1$の時
    

$$
\begin{align*}
2^{k+1} > 2 \cdot k^2 \quad \dots \text{① (仮定)}
\end{align*}
$$

    

$$
\begin{align*}
2k^2 > (k+1)^2 \quad \dots \text{②} \quad (\because (\text{左}) - (\text{右}) = k^2 - 2k - 1 > 0 \quad (k \geqq 5))
\end{align*}
$$

    ①, ②から
    

$$
\begin{align*}
2^{k+1} > (k+1)^2
\end{align*}
$$

    となって $n=k+1$ で成立. 以上から示された.

5.  **正しくない**

    正しいとすると $\frac{1}{N} = 0$ なる $N \in \mathbb{N}$ が存在する. 両辺に $N (\neq 0)$ をかけると
    

$$
\begin{align*}
1 = 0
\end{align*}
$$

    となって矛盾するから示された.