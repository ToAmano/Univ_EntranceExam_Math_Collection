---
university: "titech"
category: "kouki"
year: "2001"
question: "2"
type: "solution"
title: "TITECH 2001 kouki Q2 (solution)"
---

## 【解】

  $A(a\cos\alpha, a\sin\alpha)$, $B(b\cos\beta, b\sin\beta)$とおく ($0 \le \alpha, \beta < 2\pi$)と
  

$$
\begin{align}
\begin{dcases}
      \vec{CA} = \begin{pmatrix} a\cos\alpha-1 \\ a\sin\alpha \end{pmatrix} \\
      \vec{CB} = \begin{pmatrix} b\cos\beta-1 \\ b\sin\beta \end{pmatrix}
    \end{dcases}\label{2001-2:eq:8}
\end{align}
$$

  である．$\triangle ABC$の様子を[図1](#2001-2:fig:1)に示す．

  

<figure id="2001-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2001/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形$ABC$の様子</figcaption>
</figure>

  $\triangle ABC$ の面積が最大の時を考える．
  まず $A$ を固定して $B$ を動かすと，$T$が最大になるのは
  直線$AC$と直線$OB$が直交する時である．従って，
  

$$
\begin{align*}
\begin{pmatrix}a\cos\alpha-1 \\ a\sin\alpha\end{pmatrix} \cdot\begin{pmatrix} \cos\beta\\\sin\beta\end{pmatrix} = 0
\end{align*}
$$

  題意より，これが$\alpha=3\pi/4, \beta=4\pi/3$で成り立つから
  

$$
\begin{align*}
& \begin{pmatrix}-a\frac{\sqrt{2}}{2}-1                     \\ a\frac{\sqrt{2}}{2}\end{pmatrix} \cdot\begin{pmatrix} 1              \\\sqrt{3}\end{pmatrix} = 0 \\\therefore& -a\frac{\sqrt{2}}{2}-1 + \frac{\sqrt{6}}{2}a = 0 \\\therefore& (\sqrt{6}-\sqrt{2})a = 2                         \\\therefore& a = \frac{\sqrt{2}}{\sqrt{3}-1}\\& = \frac{\sqrt{2}(\sqrt{3}+1)}{2}
\end{align*}
$$

  が必要である．

  全く同様に，$B$ を固定して $A$ を動かすと，$T$が最大になるのは
  直線$BC$と直線$OA$が直交する時である．従って，
  

$$
\begin{align*}
\begin{pmatrix}b\cos\beta-1 \\ b\sin\beta\end{pmatrix} \cdot\begin{pmatrix} \cos\alpha\\\sin\alpha\end{pmatrix} = 0
\end{align*}
$$

  題意より，これが$\alpha=3\pi/4, \beta=4\pi/3$で成り立つから
  

$$
\begin{align*}
& \begin{pmatrix}-b\frac{1}{2}-1                     \\ a\frac{\sqrt{3}}{2}\end{pmatrix} \cdot\begin{pmatrix} 1 \\ 1\end{pmatrix} = 0 \\\therefore& -b\frac{1}{2}-1 + \frac{\sqrt{3}}{2}b = 0 \\\therefore& (\sqrt{3}-1)b = 2                         \\\therefore& b = \frac{2}{\sqrt{3}-1}\\& = \sqrt{3}+1
\end{align*}
$$

  が必要である．

  以上より
  

$$
\begin{align*}
\begin{dcases}
      a =  \frac{\sqrt{2}(\sqrt{3}+1)}{2} \\
      b = \sqrt{3}+1
    \end{dcases}
\end{align*}
$$

  が必要である．

  逆にこの時，$(\alpha,\beta)=(\frac{\pi}{4},\frac{3\pi}{4})$ が $\triangle ABC$ の面積の最大値を与えることを示す．
  まず $\triangle ABC$ の面積には必ず最大値が存在することに留意する．
  最大値を与える $\alpha,\beta$ は必要条件の導出に利用したのと同様の条件
  

$$
\begin{align*}
\begin{dcases}
      \vec{BC}\cdot\vec{OA}=0 \\
      \vec{AC}\cdot\vec{OB}=0
    \end{dcases}
\end{align*}
$$

  を満たすから，具体的な座標[(式8)](#2001-2:eq:8)を代入して
  

$$
\begin{align}
& \begin{dcases}
                   \begin{pmatrix}b\cos\beta-1  \\ b\sin\beta\end{pmatrix} \cdot \begin{pmatrix}\cos\alpha \\ \sin\alpha\end{pmatrix} = 0 \\
                   \begin{pmatrix}a\cos\alpha-1 \\ a\sin\alpha\end{pmatrix} \cdot \begin{pmatrix} \cos\beta \\ \sin\beta \end{pmatrix} = 0
                 \end{dcases}\\\therefore& \begin{dcases}
                   b\cos(\beta-\alpha) = \cos\alpha \\
                   a\cos(\beta-\alpha) = \cos\beta
                 \end{dcases}\\\therefore& \begin{dcases}
                   b\cos(\beta-\alpha) = \cos\alpha \\
                   \frac{\sqrt{2}}{2}b\cos(\beta-\alpha) = \cos\beta
                 \end{dcases}\label{2001-2:eq:2}
\end{align}
$$

  が成り立つ．ただし，最後の行で$a=\sqrt{2}b/2$を利用した．
  以下
  

$$
\begin{align*}
t = \cos\alpha
\end{align*}
$$

  とおくと，[(式2)](#2001-2:eq:2)から
  

$$
\begin{align}
\begin{dcases}
      \cos(\beta-\alpha) = \frac{1}{b} t \\
      \cos\beta = \frac{\sqrt{2}}{2} t
    \end{dcases}\label{2001-2:eq:5}
\end{align}
$$

  だから，一つ目の式を加法定理で展開して
  

$$
\begin{align}
& \cos\beta\cos\alpha + \sin\alpha\sin\beta = \frac{t}{b}\nonumber\\\therefore& \frac{\sqrt{2}}{2} t^2 \pm\sqrt{1-t^2}\sqrt{1-\frac{t^2}{2}} = \frac{t}{b}\nonumber\\\therefore& \pm\sqrt{1-t^2}\sqrt{1-\frac{t^2}{2}} = t\left(\frac{1}{b}-\frac{\sqrt{2}}{2}t\right)\label{2001-2:eq:4}
\end{align}
$$

  両辺二乗して整理すると
  

$$
\begin{align}
& \left(1-t^2\right)\left(1-\frac{t^2}{2}\right) = t^2\left(\frac{1}{b}-\frac{\sqrt{2}}{2}t\right)^2 \\\therefore& 1-\frac{3}{2}t^2 = \frac{1}{b^2}t^2-\frac{\sqrt{2}}{b}t^3                                          \\\therefore& \frac{\sqrt{2}}{b}t^3  - \left(\frac{1}{b^2}+\frac{3}{2}\right)t^2 +1 = 0
\end{align}
$$

  ここで$1/b=(b-2)/2$に注意すると
  

$$
\begin{align*}
\frac{1}{b^2} = \frac{2-\sqrt{3}}{2} = \frac{3-b}{2} = -\frac{1}{b} + \frac{1}{2}
\end{align*}
$$

  より変形を続けて
  

$$
\begin{align}
& \frac{\sqrt{2}}{b}t^3 + \left(\frac{1}{b}-2\right)t^2 +1 = 0       \nonumber\\& \left(t+\frac{\sqrt{2}}{2}\right)\left[\frac{\sqrt{2}}{b}t^2-2t+\sqrt{2}\right] = 0 \nonumber\\& \left(t+\frac{\sqrt{2}}{2}\right)\left[\frac{\sqrt{2}}{2}(\sqrt{3}-1)t^2-2t+\sqrt{2}\right] = 0 \label{2001-2:eq:3}
\end{align}
$$

  ここで，大括弧の中の$t$の二次式の判別式$D$は
  

$$
\begin{align*}
D/4 = 1 - \frac{\sqrt{2}}{2}\sqrt{2}(\sqrt{3}-1) = -\sqrt{3} < 0
\end{align*}
$$

  より負だから，この二次式は常に正であり，[(式3)](#2001-2:eq:3)の実数解は
  

$$
\begin{align*}
& t=-\frac{1}{\sqrt{2}}\\\therefore& \alpha = \frac{3\pi}{4}, \frac{5\pi}{4}
\end{align*}
$$

  のみである．この時[(式5)](#2001-2:eq:5)より
  

$$
\begin{align*}
& \cos\beta = \frac{1}{2}\\\therefore& \beta = \frac{\pi}{3},\frac{5\pi}{3}
\end{align*}
$$

  である．
  また，$t<0$より[(式4)](#2001-2:eq:4)で複号負が採用される．
  すなわち
  

$$
\begin{align*}
\sin\alpha\sin\beta < 0
\end{align*}
$$

  である．
  以上の条件を満たす$(\alpha,\beta)$の組は
  

$$
\begin{align*}
(\alpha,\beta) = (\frac{3}{4}\pi, \frac{3}{4}\pi), (\frac{5}{4}\pi, \frac{7}{4}\pi)
\end{align*}
$$

  の二つである．
  対称性からいずれの場合も$\triangle ABC$の面積は等しくなるから，
  たしかに $(\alpha,\beta) = (\frac{\pi}{4}, \frac{3}{4}\pi)$ で $\triangle ABC$ の面積は最大となる．
  以上から十分である．

  よって，求める $(a,b)$ は
  

$$
\begin{align}
\begin{dcases}
      a = \frac{\sqrt{2}(\sqrt{3}+1)}{2} \\
      b = \sqrt{3}+1
    \end{dcases}\label{2001-2:eq:6}
\end{align}
$$

  である．$\cdots$(答)

  
  (2)

  

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2001/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 三角形$A_0B_0C$の様子</figcaption>
</figure>

  [(式6)](#2001-2:eq:6)より$A,B$ の座標は
  

$$
\begin{align*}
& A\left(-\frac{\sqrt{2}a}{2},\frac{\sqrt{2}a}{2}\right) = \left(-\frac{b}{2},\frac{\sqrt{2}a}{2}\right)\\& B\left(-\frac{b}{2},\frac{-\sqrt{3}b}{2}\right)
\end{align*}
$$

  であり，$x$座標が等しいことに注意する．
  そこで$A,B$から$x$軸に下ろした垂足を$H$とおく．

  従って，線分ABの長さは$y$座標の差分に等しく，
  

$$
\begin{align*}
|AB|
     & = |AH| + |BH|                               \\& = \frac{\sqrt{2}}{2}a + \frac{\sqrt{3}}{2}b \\& = \frac{1+\sqrt{3}b}{2}\\& = \frac{1}{2}b^2
\end{align*}
$$

  である．

  $\triangle ABC$に正弦定理を用いると，外接円の半径$R$は
  

$$
\begin{align*}
\frac{|AB|}{\sin\angle ACB} = 2R
\end{align*}
$$

  である．
  ここで，
  $OA\perp BC$より$\angle OCB = \angle OAB=\frac{\pi}{4}$であり，
  $OB\perp AC$より$\angle OCA = \angle OBA=\frac{\pi}{6}$である．
  従って
  

$$
\begin{align*}
\angle ACB= \angle OCB + \angle OCA = \frac{\pi}{4} + \frac{\pi}{6}=\frac{5\pi}{12}
\end{align*}
$$

  となるから，
  

$$
\begin{align}
R
     & = \frac{|AB|}{2\sin\angle ACB}\\& = \frac{b^2}{4\sin\frac{5\pi}{12}}\label{2001-2:eq:7}
\end{align}
$$

  である．

  ここで，[(式5)](#2001-2:eq:5)より
  

$$
\begin{align*}
& \cos\left(\beta-\alpha\right) = \cos\frac{7\pi}{12} = \frac{\cos\alpha}{b} = -\frac{\sqrt{2}}{2b}\\\therefore& \cos\frac{5\pi}{12} = -\cos\frac{7\pi}{12} = \frac{\sqrt{2}}{2b}
\end{align*}
$$

  だから，
  

$$
\begin{align*}
\sin\frac{5\pi}{12}& = \sqrt{1-\sin^2\frac{5\pi}{12}}\\& = \sqrt{1-\frac{1}{2b^2}}\\& = \frac{\sqrt{3}+1}{2\sqrt{2}}\\& = \frac{b}{2\sqrt{2}}
\end{align*}
$$

  であり，[(式7)](#2001-2:eq:7)に代入して求める外接円の半径は
  

$$
\begin{align*}
R
     & = \frac{2\sqrt{2}b^2}{2 \cdot 2b}\\& = \frac{\sqrt{2}}{2}b             \\& = \frac{\sqrt{2}(\sqrt{3}+1)}{2}
\end{align*}
$$

  となる．$\cdots$(答)

  
  

## 【解説】

  平面図形の問題．
  三角形ABCがどういう時に最大になるかを式に起こして考えられるかがポイントである．
  二つの円が同心円上にあるので，このような三角形は$OA \perp BC$, $OB \perp AC$を満たすことに気づくと比較的少ない数式変形で条件を導ける．

  $\triangle ABC$の面積$T$は
  

$$
\begin{align*}
T
     & = \frac{1}{2}\left|(a\cos\alpha-1)b\sin\beta - a\sin\alpha(b\cos\beta-1) \right|\\& = \frac{1}{2}\left| ab\sin(\beta-\alpha) - b\sin\beta + a\sin\alpha\right|
\end{align*}
$$

  と計算できるものの，これ自体を使っていくのは少し大変だろう．

  さて，三角形ABCが最大となる条件の部分だが，
  点と直線の距離の公式から同様の結果を導くこともできるので紹介する．

  $A$ を固定して $B$ を動かすと，$T$が最大になるのは直線$AC$と点$B$の距離が最大になる時である．
  題意の条件よりこの時$\alpha=3\pi/4$だから，直線$AC$の方程式は
  

$$
\begin{align*}
y = \frac{-a}{a+\sqrt{2}}(x-1)
\end{align*}
$$

  だから，$AC$と$B$の距離は，点と直線の距離公式より
  

$$
\begin{align*}
\frac{\left| -ab\cos\theta - (a+\sqrt{2})b\sin\theta +a)\right|}{(1-\sqrt{2})^2+1}
\end{align*}
$$

  である．$a,b>0$より，これが最大になるのは
  

$$
\begin{align*}
ab\cos\theta + (a+\sqrt{2})b\sin\theta = \begin{pmatrix}a \\ a+\sqrt{2}\end{pmatrix} \cdot\vec{OB}
\end{align*}
$$

  が最小のとき．これは$\vec{OB}$が$(a,a+\sqrt{2})$と成す角$\pi$の時である．
  ここで，ベクトル$(a,a+\sqrt{2})$は$\vec{CA}$と直交するベクトルであり，
  従ってこの条件は$\vec{OB}\cdot\vec{CA}=0$に他ならない．よって解答と合流する．
  以上で点と直線の距離公式による導出ができた．

  この時$\beta=4\pi/3$だから，
  

$$
\begin{align*}
\begin{pmatrix}a \\ a+\sqrt{2}\end{pmatrix} \parallel\begin{pmatrix}\cos\frac{\pi}{3}\\\sin\frac{\pi}{3}\end{pmatrix}
\end{align*}
$$

  より，
  

$$
\begin{align*}
& \frac{a}{a+\sqrt{2}} = \frac{1}{\sqrt{3}}\\\therefore
    a & = \frac{\sqrt{2}}{\sqrt{3}-1}\\& = \frac{\sqrt{2}(\sqrt{3}+1)}{2}
\end{align*}
$$

  であることが必要である．これは解答と同じ値である．