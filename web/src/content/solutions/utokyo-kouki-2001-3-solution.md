---
university: "utokyo"
category: "kouki"
year: "2001"
question: "3"
type: "solution"
title: "UTOKYO 2001 kouki Q3 (solution)"
---

## 【解】

  

<figure id="2001-3:fig:0">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円周とその上の長さ$L$の円弧</figcaption>
</figure>

  $[k, k+1]$ の部分集合 $D_k$ を
  

$$
\begin{align}
D_k = \left\{x | k \le x \le k+1, P(x) \in I\right\}\label{2001-3:eq:1}
\end{align}
$$

  によって定める．

  以下，
  

$$
\begin{align}
f(x) = Ax^2+Bx+C \label{2001-3:eq:2}
\end{align}
$$

  とおく．題意より
  

$$
\begin{align}
A \in\mathbb{N}, B, C \in\mathbb{Z}\label{2001-3:eq:3}
\end{align}
$$

  とおいて良い．
  $f''(x) = 2A > 0$ だから $f$ は下に凸である．

  $f(x)$は二次の係数が正の二次関数だから，$f(x)$ の $k \le x \le k+1$ の部分は$k \to \infty$ とすれば区間内で単調増加として良い．

  ここで一般に連続，微分可能，単調増加かつ下に凸な関数$g(x)$の
  $a \le x \le b$ の部分の$y$軸への正射影の長さを $a_y$, $x$軸への正射影
  の長さを $a_x=b-a$として，区間内での平均変化率 $\Delta$ を
  

$$
\begin{align}
\Delta = \frac{a_y}{a_x}\label{2001-3:eq:4}
\end{align}
$$

  とおく．

  

<figure id="2001-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 関数$y=f(x)$の平均変化率の定義</figcaption>
</figure>

  さて[(式3)](#2001-3:eq:3)より$f(k), f(k+1) \in \mathbb{Z}$ だから，$f(k) \le y \le f(k+1)$ の間には $f(k+1)-f(k)$ 個の
  整数で区切られた区間
  

$$
\begin{align*}
f(k),f(k)+1, [f(k)+1,f(k)+2], \cdots, [f(k+1)-1,f(k+1)]
\end{align*}
$$

  が存在する．対応して各区間において，$P(x)$の角度の範囲は
  

$$
\begin{align*}
& 2\pi f(k)     \le 2\pi f(x) \le 2\pi(f(k)+1) \\& 2\pi(f(k)+1) \le 2\pi f(x) \le 2\pi(f(k)+2) \\& 2\pi(f(k)+2) \le 2\pi f(x) \le 2\pi(f(k)+3) \\& \cdots\\& 2\pi(f(k+1)-1) \le 2\pi f(x) \le 2\pi f(k+1)
\end{align*}
$$

  のように$2\pi$ずつ回転するから，各区間に$I$に含まれる部分の割合は
  

$$
\begin{align}
\frac{L}{2\pi}\label{2001-3:eq:5}
\end{align}
$$

  である．

  

<figure id="2001-3:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2001/3/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $y$軸方向に長さ$1$の区間があれば，そのうち$L/2\pi$の部分が$I$に含まれる．</figcaption>
</figure>

  以上の考察から$f(k) \le y \le f(k+1)$の範囲に含まれる$I$の範囲は
  

$$
\begin{align}
P_{k} = \frac{L}{2\pi}\left(f(k+1)-f(k)\right)\label{2001-3:eq:6}
\end{align}
$$

  である．これが$y=f(x)$のグラフにおいて，$T_k$の部分の$y$軸への正射影の長さに他ならない．
  従って，この$T_k$の区間における$f(x)$の平均変化率$\Delta_{k}$を
  

$$
\begin{align}
\Delta_{k} = \frac{P_{k}}{T_{k}}\label{2001-3:eq:7}
\end{align}
$$

  と定義しよう．

  $f$は下に凸だから，$k \le x \le k+1$においては$f'$は単調増加なので
  

$$
\begin{align}
f'(k) \le\Delta_{k}\le f'(k+1) \label{2001-3:eq:8}
\end{align}
$$

  が成り立つ．[(式7)](#2001-3:eq:7)を代入して$k$が十分大きい時$f'>0$に注意して
  

$$
\begin{align*}
& f'(k) \le\frac{P_{k}}{T_{k}}\le f'(k+1)        \\\therefore& \frac{P_k}{f'(k+1)}\le T_k \le\frac{P_k}{f'(k)}
\end{align*}
$$

  となる．

  ここに$f'(x) = 2Ax+B$および[(式6)](#2001-3:eq:6)を代入して
  

$$
\begin{align*}
\frac{2Ak+A+B}{2Ak+2A+B}\frac{L}{2\pi}\le T_k \le\frac{2Ak+A+B}{2Ak+B}\frac{L}{2\pi}
\end{align*}
$$

  を得る．$k\to\infty$の極限を取ると
  

$$
\begin{align*}
& \lim_{k\to\infty}\frac{2Ak+A+B}{2Ak+2A+B}\frac{L}{2\pi} = \frac{L}{2\pi}\\& \lim_{k\to\infty}\frac{2Ak+A+B}{2Ak+B}\frac{L}{2\pi}   = \frac{L}{2\pi}
\end{align*}
$$

  だから，挟み撃ちの定理より
  

$$
\begin{align*}
\lim_{k\to\infty} T_{k} = \frac{L}{2\pi}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】