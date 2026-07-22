---
university: "ukyoto"
category: "kouki"
year: "1991"
question: "3"
type: "solution"
title: "UKYOTO 1991 kouki Q3 (solution)"
---

## 【解】

  

<figure id="1991-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1991/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $\vec{a},\vec{b},\vec{c}$の様子</figcaption>
</figure>

  対称性から，$\vec{a}$を
  

$$
\begin{align*}
\vec{a} = \begin{pmatrix}1 \\ 0 \\ 0\end{pmatrix}
\end{align*}
$$

  と固定して考えて良い．
  次に$\vec{b}$を$xy$平面においてもよく，
  題意の条件$\vec{a}\cdot\vec{b}=\cos\gamma$より，
  

$$
\begin{align*}
\vec{b} = \begin{pmatrix} \cos\gamma\\\sin\gamma\\ 0\end{pmatrix}
\end{align*}
$$

  とおける．残りの$\vec{c}$を一般性を保って
  

$$
\begin{align}
& \vec{c} = \begin{pmatrix} p                    \\ q \\ r\end{pmatrix} \\& p^2 q^2 + r^2 = 1 \label{1991-3:eq:1}
\end{align}
$$

  とおく．

  題意の残りの条件，$\vec{b}\cdot\vec{c}=\cos\alpha$, $\vec{a}\cdot\vec{c}=\cos\beta$に
  これらの座標を代入して
  

$$
\begin{align*}
\cos\alpha = \vec{b}\cdot\vec{c} = pc + q \sin r \quad\cdots\textcircled{2}\\\cos\beta = \vec{a}\cdot\vec{c} = p \quad\cdots\textcircled{3}
\end{align*}
$$

  となる．従って，
  

$$
\begin{align*}
A = \cos^2 \alpha+ \cos^2 \beta + \cos^2 \gamma - 2\cos\alpha\cos\beta\cos\gamma
\end{align*}
$$

  とおくと，
  

$$
\begin{align*}
A & = (p\cos\gamma + q \sin\gamma)^2 + p^2 + \cos^2 \gamma - 2(p\cos\gamma + q \sin\gamma) p \cos\gamma\\& = (p\cos\gamma + q \sin\gamma)(q \sin\gamma - p\cos\gamma) + p^2 + \cos^2\gamma\\& = q^2 \sin^2 \gamma - p^2 \cos^2\gamma + p^2 + \cos^2 \gamma& = (p^2 + q^2) \sin^2 r + c^2 r^2
\end{align*}
$$

  と計算できる．[(式1)](#1991-3:eq:1)より
  

$$
\begin{align*}
0 \le A \le(p^2 + q^2 + r^2) \sin^2 \gamma + \cos^2 \gamma = \sin^2 \gamma + \cos^2 \gamma = 1 \\\therefore
    0 \le A \le 1
\end{align*}
$$

  となり，題意の不等式は示された．$\cdots$(答)

  
  次に等号成立条件について考える．
  まず左側の等号が成立するのは，$A$の形から
  

$$
\begin{align*}
(p^2+q^2) \sin^2 r = 0 \land\cos^2 \gamma = 0
\end{align*}
$$

  の時だが，$\sin^2 \gamma = \cos^2 \gamma = 0$ となることはないから，
  $\cos\gamma, q, p$が全て$0$の時に等号が成立する．
  この時，$\vec{a} \perp \vec{b} \perp \vec{c}$ である．$\cdots$(答)

  
  最後に右側の等号が成立するのは，
  

$$
\begin{align*}
r^2 = 0 \iff r=0
\end{align*}
$$

  の時で，この時$\vec{a}, \vec{b}, \vec{c}$ は同平面上にある．$\cdots$(答)

  
  

## 【解説】