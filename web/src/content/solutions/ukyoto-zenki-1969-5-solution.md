---
university: "ukyoto"
category: "zenki"
year: "1969"
question: "5"
type: "solution"
title: "UKYOTO 1969 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

$$
\begin{align*}
\begin{aligned}
|\vec{X}|^2 &= |\vec{A}|^2 + |\vec{B_k}|^2 + 2\vec{A} \cdot \vec{B_k} \\
&= a^2 + 1 + 2\vec{A} \cdot \vec{B_k} \quad \dots \text{①'}
\end{aligned}
\end{align*}
$$

である。題意から，$\vec{A} = a \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}$ とおける。($0 \leqq \theta < 2\pi$)

$|\vec{X}|^2$ の大きさの期待値を $E$ とおくと①'から，

$$
\begin{align*}
\begin{aligned}
E &= \frac{1}{6} \sum_{k=1}^6 \left\{ a^2+1 + 2 \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix} \cdot \begin{pmatrix} \cos\frac{k\pi}{3} \\ \sin\frac{k\pi}{3} \end{pmatrix} \right\} \\
&= (a^2+1) + \frac{1}{3} \sum_{k=1}^6 \cos\left(\frac{k\pi}{3} - \theta\right) \quad \dots \text{②}
\end{aligned}
\end{align*}
$$

ここで，単位円に内接する正六角形を考えると，中心から各頂点へのベクトルの $x$ 成分は $\cos\left(\frac{k\pi}{3} - \theta\right)$ ($k=1, 2, \dots, 6$) で表わされ，又，この和は零だから，

$$
\begin{align*}
\sum_{k=1}^6 \cos\left(\frac{k\pi}{3} - \theta\right) = 0
\end{align*}
$$

②に代入して

$$
\begin{align*}
E = a^2 + 1
\end{align*}
$$