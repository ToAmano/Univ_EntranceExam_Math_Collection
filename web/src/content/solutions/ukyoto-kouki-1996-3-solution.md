---
university: "ukyoto"
category: "kouki"
year: "1996"
question: "3"
type: "solution"
title: "UKYOTO 1996 kouki Q3 (solution)"
---

## 【解】

  (1)
  対称性から $P_1$ が $l$, $m$ の交点 $O$ を 原点とする半径 $1$ の円上にあるとして良い．
  $OP_1$の長さが異なる場合は，全体の拡大縮小によって同一視できる．
  また，唯一の例外として$P_1$が$m$と$l$の交点である場合があるが，この場合の題意の成立は明らかである．

  

<figure id="1996-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1996/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 複素平面上の直線$l,m$と点$P_k,Q_k$の様子．</figcaption>
</figure>

  そこで以下複素平面で考え $l$ が実軸と一致し $m$ が $l$ を $\frac{\pi}{3}$ 回転したものになるとする．
  $P_k$, $Q_k$ を表す複素数 $p_k$, $q_k$ とする($k=1,2,3,4$)．
  題意より$Q_k$は$P_k$と$l$すなわち実軸について対称な点なので
  

$$
\begin{align}
\overline{q_k} = p_k \label{1996-3:eq:1}
\end{align}
$$

  を満たす．
  同じく題意より，$P_{k+1}$は$Q_k$を$m$すなわち$\theta=\pi/3$について対称な点なので，
  これは偏角を考えると$\overline{q_k}$を$2\pi/3$回転させたもので，大きさを考えると$Q_k$と同一なので
  

$$
\begin{align}
p_{k+1} = e\left(\frac{\pi}{3}\right)\overline{q_k}\label{1996-3:eq:2}
\end{align}
$$

  である．ただし
  

$$
\begin{align*}
e(\theta) = \cos\theta + i \sin\theta
\end{align*}
$$

  とする．

  [(式2)](#1996-3:eq:1,1996-3:eq:2)から
  

$$
\begin{align*}
p_{k+1} = e\left(\frac{2\pi}{3}\right)\cdot p_k
\end{align*}
$$

  だから，繰り返し用いて，
  

$$
\begin{align*}
p_4
     & = \{e(\frac{2\pi}{3})\}^3 \cdot p_1 \\& = e(2\pi) p_1                       \\& = p_1
\end{align*}
$$

  となり，題意は示された．$\cdots$(答)

  
  (2)
  $P_k, Q_k$ の偏角を $\alpha_k, \beta_k$ ($0 \le \alpha_k, \beta_k < 2\pi$) とおく．
  $P_k, Q_k$は半径$1$の円上にあるから
  

$$
\begin{align*}
p_k & = e(\alpha_k) \\
    q_k & = e(\beta_k)
\end{align*}
$$

  である．
  [(式2)](#1996-3:eq:2)の両辺$\arg$をとって，
  

$$
\begin{align}
\alpha_{k+1} = \alpha_k + \frac{2\pi}{3}\label{1996-3:eq:3}
\end{align}
$$

  である．

  さて，題意の長さ$L$を求めるには，$|P_{k}Q_{k}|$および$|P_{k+1}Q_{k}|$があれば良い．
  まず，前者は$\triangle OP_{k}Q_{k}$を考えることで，
  

$$
\begin{align*}
|P_{k}Q_{k}|
     & = 2\left|\sin\alpha_{k}\right|
\end{align*}
$$

  と計算できる．

  後者も$\triangle OP_{k+1}Q_{k}$を考えることで，
  

$$
\begin{align*}
|P_{k+1}Q_{k}|
     & = 2\left|\sin\left(\alpha_{k+1}-\frac{\pi}{3}\right)\right|\\& = 2\left|\sin\left(\alpha_{k}+\frac{\pi}{3}\right)\right|\quad(\because\text{[(式3)](#1996-3:eq:3)})
\end{align*}
$$

  と計算できる．

  従って，$L$は
  

$$
\begin{align*}
L
     & = \sum_{k=1}^3 \{ |P_k Q_k| + |Q_k P_{k+1}| \}\\& = 2 \sum_{k=1}^3 |\sin\alpha_k| + 2 \sum_{k=1}^3 \left|\sin(\alpha_k + \frac{\pi}{3})\right|\\& = 2 \sum_{k=0}^{5}\left|\sin(\alpha_1 + \frac{k\pi}{3})\right|\quad(\because\text{[(式3)](#1996-3:eq:3)})
\end{align*}
$$

  と $\alpha_1$ を用いて表せる．

  ここで $A_k = |\sin(\alpha_1 + \frac{k\pi}{3})|$ とおく．
  $0 \le \alpha_1 \le \frac{\pi}{3}$ の場合を調べれば，$\frac{i \pi}{3} \le \alpha_1 \le \frac{(i+1)\pi}{3}$ ($i=2,3,4,5$) の時には，
  $\alpha_1' = \alpha_1 - \frac{i\pi}{3}$ とおけば元の
  $0 \le \alpha_1' \le \frac{\pi}{3}$ の場合に帰着するので，
  この場合を調べれば十分である．この時
  

$$
\begin{align}
A_0, A_1, A_2 \ge 0 \label{1996-3:eq:4}
\end{align}
$$

  が成り立つ．

  この条件のもとで引き続き式変形する．
  合計$6$個の項を二つづつ整理して
  

$$
\begin{align*}
L
    = & 2\left[\left|\sin(\alpha_1)\right| + \left|\sin(\alpha_1 + \pi)\right|\right]\\& + 2\left[\left|\sin\left(\alpha_1+\frac{\pi}{3}\right)\right| + \left|\sin\left(\alpha_1 + \frac{\pi}{3} + \pi\right)\right|\right]\\& + 2\left[\left|\sin\left(\alpha_1+\frac{2\pi}{3}\right)\right| + \left|\sin\left(\alpha_1 + \frac{2\pi}{3} + \pi\right)\right|\right]\\
    = & 4\left|\sin(\alpha_1)\right| + 4\left|\sin\left(\alpha_1+\frac{\pi}{3}\right)\right| + 4\left|\sin\left(\alpha_1+\frac{2\pi}{3}\right)\right|\\
    = & 4\left[\sin(\alpha_1) + \sin\left(\alpha_1+\frac{\pi}{3}\right) + \sin\left(\alpha_1+\frac{2\pi}{3}\right)\right]\quad(\because\text{[(式4)](#1996-3:eq:4)})
\end{align*}
$$

  となる．和積の公式を用いて
  

$$
\begin{align*}
L
     & = 4\left\{ 2\sin(\alpha_1 + \frac{\pi}{3}) \cos\frac{\pi}{3} + \sin(\alpha_1 + \frac{\pi}{3}) \right\}\\& = 8\sin(\alpha_1 + \frac{\pi}{3})                                                                       \\& \le 8
\end{align*}
$$

  と評価できる．等号が成立するのは$\alpha_1=\pi/6$の時である．
  従って，求める最大値は
  

$$
\begin{align*}
\max L = 8
\end{align*}
$$

  である．$\cdots$(答)

  

## 【解説】

  (2)の最大値のとき，P，Qの作る図形は正六角形となり，この一周の長さは確かに$8$である．