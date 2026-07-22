---
university: "todai"
category: "kouki"
year: "1999"
question: "3"
type: "solution"
title: "TODAI 1999 kouki Q3 (solution)"
---

## 【解】

  (1)

  

<figure id="1999-3:fig:0">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1999/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 四角形$A_nB_nC_nD_n$と$A_{n+1}B_{n+1}C_{n+1}D_{n+1}$の様子</figcaption>
</figure>

  

<figure id="1999-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1999/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 四角形$A_0B_0C_0D_0$の様子</figcaption>
</figure>

  与えられた座標の情報を用いて，$\triangle B_0OP$に余弦定理を適用すると
  

$$
\begin{align*}
\cos\angle B_0OP
     & = \frac{\overrightarrow{OB_0} \cdot \overrightarrow{OP}}{|\overrightarrow{OB_0}| |\overrightarrow{OP}|}\\& = \frac{160}{\sqrt{80} \cdot \sqrt{160}}\\& = \frac{\sqrt{2}}{2}
\end{align*}
$$

  である．
  点$B_0,P$はいずれも第一章限にあって $0 < \angle B_0OP < \pi/2$ だから，
  

$$
\begin{align*}
\angle B_0OP = \frac{\pi}{4}
\end{align*}
$$

  である．$\cdots$(答)

  
  (2)
  点$C_0$が線分$OP$上にあるから，$C_0(4t, 12t) \ (t \in \mathbb{R}, 0< t < 1)$ とおける．

  この時$\triangle OA_0D_0$と$\triangle OB_0C_0$ が$1:4$の相似であることから，
  $D_0(t, 3t)$ とおける．

  すると，四角形$A_0B_0C_0D_0$の辺の長さについて
  

$$
\begin{align*}
\overline{A_0B_0}& = 3\sqrt{5}\\\overline{C_0D_0}& = 3\sqrt{10}|t|
\end{align*}
$$

  となる．

  $K_n$の定義から，$K_n$と$K_{n+1}$の相似比は$\overline{A_0B_0}:\overline{C_0D_0}$に等しく
  

$$
\begin{align}
K_n: K_{n+1}& =1:\frac{3\sqrt{10}t}{3\sqrt{5}}\\& = 1:\sqrt{2}t \label{1999-3:eq:1}
\end{align}
$$

  である．

  題意のように$K_n=K_0$なる$n$があるとき，まずはこれらの大きさが等しいことが必要であって，
  相似比が$1:1$であることが必要だから
  

$$
\begin{align*}
& \sqrt{2}t = 1          \\\therefore& t = \frac{\sqrt{2}}{2}
\end{align*}
$$

  である．よってこの時
  

$$
\begin{align*}
C_0(2\sqrt{2},6\sqrt{2})
\end{align*}
$$

  となる．

  逆にこの時任意の$K_n$が合同だから
  

$$
\begin{align*}
\angle A_0OD_n = \angle B_0OP = \pi/4 \quad\cdots\cdots②
\end{align*}
$$

  が成り立ち，$x$軸と線分$OB_0$のなす角度$\alpha$として
  

$$
\begin{align*}
A_n(\sqrt{3}\cos(\alpha + \pi n/4), \sqrt{3}\sin(\alpha + \pi n/4))
\end{align*}
$$

  と書ける．
  $A_n=A_0$の時が$K_n=K_0$となる時だから，求める$n$の条件は
  

$$
\begin{align*}
& n\frac{\pi}{4} = 2k\pi& (k \in\mathbb{Z}) \\& n \equiv 0             & (\pmod{8})
\end{align*}
$$

  である．$\cdots$(答)

  

  (3)
  題意の条件より，任意の$n$に対して$\triangle OC_k B_k$ が相似である．
  従って，任意の$n$に対して$\angle A_nOD_n$が等しく，(2)と同様
  

$$
\begin{align*}
\angle A_0OD_n = \angle B_0OP = \pi/4
\end{align*}
$$

  が成り立つ．

  従って，$A_n$の座標は，実数列$a_n$を用いて
  

$$
\begin{align}
& A_n(a_n \cos(\alpha + \pi n/4), a_n \sin(\alpha + \pi n/4)) \label{1999-3:eq:3}\\& a_0 = \sqrt{5}
\end{align}
$$

  と書ける．
  (2)で求めた相似比[(式1)](#1999-3:eq:1)より
  

$$
\begin{align*}
& \overrightarrow{OA_{n+1}}|: |\overrightarrow{OA_n}| = \sqrt{2}t : 1 \\\therefore& a_{n+1} = \sqrt{2}t a_{n}
\end{align*}
$$

  と書けるから，$a_0=\sqrt{5}$のもとでこの漸化式を解いて
  

$$
\begin{align}
a_n = \sqrt{5}\left(\sqrt{2}t\right)^{n}\label{1999-3:eq:2}
\end{align}
$$

  と求まる．
  以上より，$A_n$は$\mod 8$で同じ$n$のものをグループとして点Oから始まる異なる半直線上にならぶ．

  題意のように四角形が平面を敷き詰める時，
  半直線$OB_0$, $OP$にはさまれた領域に[図3](#1999-3:fig:3)のように
  $K_n$が詰まることが従って必要となる．

  

<figure id="1999-3:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1999/3/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 半直線$OB_0$, $OP$にはさまれた領域に$K_n$がしき詰まっている様子．</figcaption>
</figure>

  図でとなりあう$K_n$の相似比は
  

$$
\begin{align*}
\overline{A_0P_0} : \overline{B_0C_0} = 1:4
\end{align*}
$$

  である．
  $a_{n+8}:a_{n}$の相似比がこれに等しいことが必要である．
  [(式2)](#1999-3:eq:2)より，この条件は
  

$$
\begin{align*}
& \left(\sqrt{2}t\right)^{8} = 4, \frac{1}{4}\\\therefore& \sqrt{2}t=4^{1/8}, \left(\frac{1}{4}\right)^{1/8}\\\therefore& t=2^{-1/4}, 2^{-3/4}
\end{align*}
$$

  となる．
  この時対応する$C_0$の座標は
  

$$
\begin{align*}
C_0(2^{7/4}, 3 \cdot 2^{7/4}) \\
    C_0(2^{5/4}, 3 \cdot 2^{5/4})
\end{align*}
$$

  である．
  逆にこの時，$K_n$は図のように平面を敷き詰めるから十分である．
  $\cdots$(答)
  

  

<figure id="1999-3:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1999/3/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $t=2^{-\frac{1}{4}}$ の時，$K_n$が$xy$平面にしき詰まっている様子．</figcaption>
</figure>

  次に，点$Q(100,50)$について考える．
  この点は直線$OB_0$上にあって，また$|\overrightarrow{OQ}| = 50\sqrt{5}$ である．
  二つの$t$の値についてそれぞれ調べる．
  いずれの場合も，$A_n$が直線$OB_n$上に存在するのは[(式2)](#1999-3:eq:2)より
  $n$が$8$の倍数の時である．従って，$A_{8n}$と$Q$の位置関係を調べればQを含む$K_n$がわかる．

  
  \textbf{1° $t=2^{-\frac{1}{4}}$ の時}

  [(式2)](#1999-3:eq:2)より
  

$$
\begin{align*}
a_{8n} = \sqrt{5}\cdot 4^n
\end{align*}
$$

  は単調増加で，
  

$$
\begin{align*}
|\overrightarrow{OA_{16}}| < 50\sqrt{5} < |\overrightarrow{OA_{24}}|
\end{align*}
$$

  である．
  従って求める$n$は図より$n=15,16$である．

  
  \textbf{2° $t=2^{-\frac{3}{4}}$ の時}

  [(式2)](#1999-3:eq:2)より
  

$$
\begin{align*}
a_{8n} = \frac{\sqrt{5}}{4^n}
\end{align*}
$$

  は単調減少で，
  

$$
\begin{align*}
|\overrightarrow{OA_{-16}}| < 50\sqrt{5} < |\overrightarrow{OA_{-24}}|
\end{align*}
$$

  である．
  従って求める$n$は図より$n=-16,-17$である．

  
  以上まとめて，求める$C_0$および$Q$を含む$K_n$は
  

$$
\begin{align*}
\begin{dcases}
      C_0(2^{\frac{7}{4}}, 3 \cdot 2^{\frac{7}{4}}) \text{ の時、} n=15, 16 \\
      C_0(-2^{\frac{7}{4}}, -3 \cdot 2^{\frac{7}{4}}) \text{ の時、} n=-16, -17
    \end{dcases}
\end{align*}
$$

  である．$\cdots$(答)
  
  

## 【解説】