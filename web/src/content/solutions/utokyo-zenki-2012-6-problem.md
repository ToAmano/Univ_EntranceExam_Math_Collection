---
university: "utokyo"
category: "zenki"
year: "2012"
question: "6"
type: "problem"
title: "UTOKYO 2012 zenki Q6 (problem)"
---

2×2行列$P=\begin{pmatrix} p & q \\ r & s \end{pmatrix}$に対して
\[ Tr(P)=p+s \]
と定める。\\
　$a$，$b$，$c$は$a \geqq b>0$，$0 \leqq c \leqq 1$を満たす実数とする。
行列$A$，$B$，$C$，$D$を次で定める。

\[ A=\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}, 
B=\begin{pmatrix} b & 0 \\ 0 & a \end{pmatrix}, 
C=\begin{pmatrix} a^c & 0 \\ 0 & b^c \end{pmatrix}, 
D=\begin{pmatrix} b^{1-c} & 0 \\ 0 & a^{1-c} \end{pmatrix} \]
また実数$x$に対し$U(x)=\begin{pmatrix} \cos x & -\sin x \\ \sin x & \cos x \end{pmatrix}$
とする。\\
　このとき以下の問いに答えよ。

1.  各実数$t$に対して，$x$の関数
\[ f(x)=Tr \left( (U(t)AU(-t)-B) U(x) \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} U(-x) \right) \]
の最大値$m(t)$を求めよ。
(ただし，最大値をとる$x$を求める必要はない。)

2.  すべての実数$t$に対し
\[ 2Tr(U(t)CU(-t)D) \geqq Tr(U(t)AU(-t)+B) - m(t) \]
が成り立つことを示せ。