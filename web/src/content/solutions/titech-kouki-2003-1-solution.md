---
university: "titech"
category: "kouki"
year: "2003"
question: "1"
type: "solution"
title: "TITECH 2003 kouki Q1 (solution)"
---

## 【解】

  (1)
  $S_1, S_2, S_3$ は, $\triangle \text{OPQ}$ の $xy$ 平面, $yz$ 平面, $zx$ 平面への正射影の面積である.
  そこで, $\triangle \text{OPQ}$ を含む平面の単位法線ベクトルを $\vec{m} = \begin{pmatrix} X \\ X \\ Z \end{pmatrix}$ とする.
  $xy, yz, zx$ 平面の 単位法線ベクトル,
  

$$
\begin{align*}
\vec{a_1} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}, \vec{a_2} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \vec{a_3} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
\end{align*}
$$

  と $\vec{m}$ のなす角を各々 $\theta_1, \theta_2, \theta_3$ とすると,
  

$$
\begin{align*}
\cos\theta_1 & = \frac{\vec{a_1} \cdot \vec{m}}{|\vec{a_1}| |\vec{m}|} = Z, \\\cos\theta_2 & = \frac{\vec{a_2} \cdot \vec{m}}{|\vec{a_2}| |\vec{m}|} = X, \\\cos\theta_3 & = \frac{\vec{a_3} \cdot \vec{m}}{|\vec{a_3}| |\vec{m}|} = Y
\end{align*}
$$

  となる.
  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2003/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形OPQと，その$xy$平面への正射影OP'Q'</figcaption>
</figure>

  正射影の性質より, $S_k = S \cos \theta_k$ ($k=1,2,3$) だから,
  

$$
\begin{align*}
S_1^2 + S_2^2 + S_3^2
     & = S^2 (\cos^2 \theta_1 + \cos^2 \theta_2 + \cos^2 \theta_3) \\& = S^2(X^2+Y^2+Z^2)                                          \\& = S^2 \left|\vec{m}\right|\\& = S^2
\end{align*}
$$

  である.ただし3行目で$\vec{m}$が単位法線ベクトルだから$|\vec{m}|=1$であることを用いた．
  よって題意は示された．

  
  (2)
  $k=S_1+S_2+S_3$ とおき, $k$の最大最小値を考える.
  (1)及び $S_1, S_2, S_3 \ge 0$ から, $S_1, S_2, S_3$ 空間で, 点$(S_1, S_2, S_3)$ は
  

$$
\begin{align*}
S_1^2 + S_2^2 + S_3^2 = S^2 \\
    S_1, S_2, S_3 \ge 0
\end{align*}
$$

  をみたしながら動く.この曲面は[図2](#2003-1:fig:2)のようになる．

  

<figure id="2003-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2003/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $(S_1,S_2,S_3)$の動く範囲</figcaption>
</figure>

  この曲面と平面 $k=S_1+S_2+S_3$ が共有点を持つ条件から,
  

$$
\begin{align*}
S \le k \le\sqrt{3}S
\end{align*}
$$

  ただし，等号成立は$k=S$の時$(S_1, S_2, S_3)=(S,0,0), (0,S,0), (0,0,S)$であり，
  $k=\sqrt{3}S$の時$(S_1, S_2, S_3)=(S/\sqrt{3},S/\sqrt{3},S/\sqrt{3})$である．
  したがって, 求める最大最小値は
  

$$
\begin{align*}
\min k & = S         \\\max k & = \sqrt{3}S
\end{align*}
$$

  である. $\cdots$(答)

  
  

## 【解説】

  (2)はありがちな関数の最大最小問題で様々な解法が考えられるところだ．
  解答では図形的な解法を用いた．これは非常にシンプルで覚えておきたいテクニックである．
  そのほかいくつか考えられる解法を紹介しよう．

  まず，上側の評価は非常に簡単で，コーシーシュワルツの不等式から一発で出てくる．
  

$$
\begin{align*}
S_1+S_2+S_3 \le\sqrt{3}\sqrt{S_1^2+S_2^2+S_3^2} = \sqrt{3}S
\end{align*}
$$

  であり，等号成立は$S_1=S_2=S_3=1/\sqrt{3}$のときである．

  下側の評価は境界が等号成立になるため，不等式で一発で求めに行くのは難しい．
  というのもたいていの不等式の等号成立条件は全ての変数が等しいときだからである．
  下からの評価でもっとも簡単なのは解答のような図形的解法だろう．
  別案として対称式を利用する方法もある．
  

$$
\begin{align*}
(S_1+S_2+S_3)^2
     & = S_1^2+S_2^2+S_3^3 + 2(S_1S_2+S_2S_3+S_3S_1) \\& = S^2 + 2(S_1S_2+S_2S_3+S_3S_1)
\end{align*}
$$

  であり，これを下から評価する．$S_1,S_2,S_3\ge 0$だから
  

$$
\begin{align*}
(S_1+S_2+S_3)^2 \ge S^2
\end{align*}
$$

  であり，等号成立は$S_1S_2+S_2S_3+S_3S_1=0$すなわち$S_1S_2=0$,$S_2S_3=0$,$S_3S_1=0$である．
  これは$S_1$,$S_2$,$S_3$のうち二つが$0$であればよく，$(S_1,S_2,S_3)=(0,0,S),(S,0,0),(0,S,0)$であれば成り立つ．

  今回の問題では計算量が増えてあまり有効ではないが，球面をパラメータ表示する手も考えられる．
  すなわち
  

$$
\begin{align*}
S_1 & = S\cos\theta\cos\psi\\
    S_2 & = S\cos\theta\sin\psi\\
    S_3 & = S\sin\theta
\end{align*}
$$

  とおく．ただし$0\le\theta,\psi\le\pi/2$である．よって求めるべきは
  

$$
\begin{align*}
f(\theta,\psi)
     & = S\cos\theta\cos\psi+S\cos\theta\sin\psi+S\sin\theta\\& = S\cos\theta\left(\cos\psi+\sin\psi\right)+S\sin\theta\\& = \sqrt{2}S\cos\theta\sin\left(\psi+\frac{\pi}{4}\right) + S\sin\theta
\end{align*}
$$

  の最大最小値である．区間内で$\cos\theta\ge 0$だから，まず$\theta$を固定して$\psi$を動かして
  最大最小値を考えると，
  

$$
\begin{align*}
\frac{1}{\sqrt{2}}\le\sin\left(\psi+\frac{\pi}{4}\right)\le 1
\end{align*}
$$

  である．等号成立は，下側は$\psi=0,\pi/2$，上側は$\psi=\pi/4$である．従って
  

$$
\begin{align*}
S\cos\theta + S\sin\theta\le f(\theta,\psi) \le\sqrt{2}S\cos\theta + S\sin\theta\\\sqrt{2}S\sin\left(\theta+\frac{\pi}{4}\right)\le f(\theta,\psi) \le\sqrt{3}S\sin(\theta+\alpha)
\end{align*}
$$

  を得る．ただし$\alpha$は$\sin\alpha=\sqrt{2/3}$,$\cos\alpha=\sqrt{1/3}$を満たすパラメータである．
  下側の評価は$\theta=0,\pi/2$で最小値となり，上側は$\theta+\alpha=\pi/2$で最大値となる．よって
  

$$
\begin{align*}
S \le f(\theta,\psi) \le\sqrt{3} S
\end{align*}
$$

  を得る．