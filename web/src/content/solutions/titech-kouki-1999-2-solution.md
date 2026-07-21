---
university: "titech"
category: "kouki"
year: "1999"
question: "2"
type: "solution"
title: "TITECH 1999 kouki Q2 (solution)"
---

## 【解】

  はじめから(2)のような一般的な状況を考える．すなわち，自然数 $n\ge 2$ に対して $3n$ 個の円を用いて操作を行っていく．そこで最初に(2)から考えよう．
  $k$回目の操作で描かれる円の半径を$r_{n}(k)$とおく．

  

<figure id="1999-2:fig:0">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1999/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $k=1$の様子</figcaption>
</figure>

  

<figure id="1999-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1999/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $k=1$のときの半径の導出</figcaption>
</figure>

  まず初期条件$k=1$を考える．ひとつの円の中心を$A$，隣接する円との接点$B$とする．[図2](#1999-2:fig:1)で $\angle \text{AOB}= \dfrac{\pi}{3n}$ だから
  
$$
\begin{align}
\sin\dfrac{\pi}{3n}& = \frac{AB}{OA}\nonumber\\& =\frac{r_n(1)}{1-r_n(1)}\nonumber\\\therefore
    r_n(1) & = \frac{\sin \frac{\pi}{3n}}{1+\sin \frac{\pi}{3n}}\label{1999-2:eq:1}
\end{align}
$$

  と求まる．

  

<figure id="1999-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1999/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $r_n(k+1)$と$r_{n}(k)$の関係</figcaption>
</figure>

  円の半径の一般項$r_n(k)$と$r_n(k+1)$を考える．[図3](#1999-2:fig:3)で$k$回目の円の中心$O_k$とおく．半径$1$の最初の円の中心$A$とし，$A$から各円に接する直線を$AC$とする．$O_k$から$AC$におろした垂線の足を$T_k$とおく．$O_k$から$O_kT_k$におろした垂線の足を$R_k$とおく．

  線分$O_kT_k$の長さは半径$r_n(k)$に等しい．別の表現で$O_kT_k$を計算すると
  
$$
\begin{align*}
O_kT_k
     & = O_kR_k + R_kT_k                                           \\& = O_kO_{k+1}\sin\frac{\pi}{3n} + r_n(k+1)                   \\& = \left(r_n(k)+r_n(k+1)\right)\sin\frac{\pi}{3n} + r_n(k+1)
\end{align*}
$$

  となる．したがって
  
$$
\begin{align*}
r_n(k)   & = \left(r_n(k)+r_n(k+1)\right)\sin\frac{\pi}{3n} + r_n(k+1) \\
    r_n(k+1) & = \frac{1-a_n}{1+a_n}r_n(k) \label{1999-2:eq:2}
\end{align*}
$$

  なる漸化式を得る．
  $\eqref{1999-2:eq:1,1999-2:eq:2}$から等比数列の公式より，一般項は
  
$$
\begin{align}
r_n(k)
     & = \left(\frac{1-a_n}{1+a_n}\right)^{k-1} r_n(1)           \\& = \left(\frac{1-a_n}{1+a_n}\right)^{k-1}\frac{a_n}{1+a_n}
\end{align}
$$

  となる．$A = \left(\frac{1-a_n}{1+a_n}\right)$ として $|A|<1$ だから，円の面積の総和は
  
$$
\begin{align}
S_n
     & = \lim_{k \to \infty}\sum_{p=1}^{k} r^2_n(p) \cdot\pi\cdot 3n \\& = \pi\left(\frac{a_n}{1+a_n}\right)^2 \frac{1}{1-A^2}\cdot 3n  \\& = \frac{3\pi}{4} n a_n  \label{1999-2:eq:3}
\end{align}
$$

  である．円周の総和は
  
$$
\begin{align}
C_n
     & = \lim_{p=1}^{k}\sum_{p=1}^{k} 2\pi r_n(p) \cdot 3n \\& = 6n\pi\frac{a_n}{1+a_n}\frac{1}{1-A}\\& = 3n\pi\label{1999-2:eq:4}
\end{align}
$$

  と求まる．

### (1)

  $\eqref{1999-2:eq:3,1999-2:eq:4}$に$n=2$を代入して
  
$$
\begin{align*}
& S_2 = \dfrac{3}{4}\pi& C_2 = 6\pi
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  $\eqref{1999-2:eq:3,1999-2:eq:4}$が答えである．
  
$$
\begin{align*}
S_n & = \frac{3\pi}{4} n \sin\dfrac{\pi}{3n}\\
    C_n & = 3n\pi
\end{align*}
$$
$\cdots$(答)

### (3)

  $\eqref{1999-2:eq:3}$の$n\to\infty$の極限をとって
  
$$
\begin{align*}
\lim_{n\to\infty} S_n
     & = \lim_{n\to\infty}\dfrac{\pi^2}{4}\dfrac{3n}{\pi}\sin\dfrac{\pi}{3n}\\& = \frac{\pi^2}{4}
\end{align*}
$$

  である．ただし，$n\to\infty$で$3n/\pi\to 0$であることを用いた．$\cdots$(答)

  
  

## 【解説】

  平面図形の問題．1995年の1番とほぼ同様の円を敷き詰めていく問題である．特に漸化式の導出はほぼ全く同じなため，過去問演習をやっていた人にとってはボーナス問題だった可能性が高い．

  問題としては漸化式が立てば極限値の計算は非常に容易であるから，漸化式が立つかどうかがポイント．
  $r_n(k)$と$r_n(k+1)$の関係を丁寧に図に落として立式しよう．

### (1)
は本来誘導の意図だろうが，漸化式が立つという見通しがあれば先に(2)に手を出して，(1)はあとから値を代入すればだいぶ時間の短縮になる．