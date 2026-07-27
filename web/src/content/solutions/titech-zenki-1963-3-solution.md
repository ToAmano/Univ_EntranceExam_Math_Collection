---
university: "titech"
category: "zenki"
year: "1963"
question: "3"
type: "solution"
title: "TITECH 1963 zenki Q3 (solution)"
---

## 【解】

 
$O(0,0), C(\sqrt{2},0), A(-\sqrt{2},0), B(0,-\sqrt{2}), D(0, \sqrt{2})$ となるよう $xy$ 平面をおく．
円 $O$ が $\square ABCD$ の内部だから

$$
\begin{align}
0 < r \le 1 \label{eq:1}
\end{align}
$$

である．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1963/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 座標平面上の正方形$ABCD$の様子．</figcaption>
</figure>

まず点$E$の座標を求めよう．
これは題意より点$\left(\dfrac{-\sqrt{2}r}{2},\dfrac{\sqrt{2}r}{2}\right)$と$\left(\dfrac{-\sqrt{2}r}{2},\dfrac{-\sqrt{2}r}{2}\right)$から引いた円の接線だから，
この時 $E(-\sqrt{2}r, 0)$ となる．二つの円の相似の中心がAだから，AOとAEの比を考えると

$$
\begin{align}
(AO) : (AE) = \sqrt{2} : \sqrt{2}(1-r) = 1 : 1-r
\end{align}
$$

だから，円 $E$ の半径は 

$$
\begin{align}
r\cdot(1-r) = r(1-r)
\end{align}
$$

である．よって円$E$の方程式は

$$
\begin{align}
(x + \sqrt{2}r)^2 + y^2 = r^2(1-r)^2 \label{eq:2}
\end{align}
$$

である．この様子を以下に示す．

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1963/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 二つの円$O$と$E$の様子．</figcaption>
</figure>

(1) 点$E$が必ず円$O$の外側に来ることを踏まえると，2円が交わる条件は二つの円の距離が半径の差と和の間におさまっていることで

$$
\begin{align}
r - r(1-r) < \sqrt{2}r < r + r(1-r) \\\iff 0 < r < 2 - \sqrt{2}\quad(\because\text{[(式1)](#eq:1)})
\end{align}
$$

が求める$r$の範囲である．

(2) 対称性から$K$ が第2象限にあるとして良い．すると $K(X, Y)$ は二つの円の方程式の共有解で

$$
\begin{align}
\begin{cases}
X = \frac{\sqrt{2}}{4}r (r^2 - 2r - 2) \\
Y = \sqrt{r^2 - X^2}
\end{cases}
\end{align}
$$

である．

<figure id="fig_3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1963/3/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 円$E$と円$O$の交点$K, L$および角$\theta$</figcaption>
</figure>

したがって$KL$と$x$軸の交点を$P$とすると

$$
\begin{align*}
\cos\frac{\theta}{2}&= \frac{|EP|}{|EK|}\\&= \frac{|EP|}{\text{円Eの半径}}\\&= \frac{X + \sqrt{2}r}{r(1-r)}\\&= \frac{\sqrt{2}r \left[ \frac{r^2-2r-2}{4} + 1 \right]}{r(1-r)}\\&= \frac{r^2-2r+2}{4(1-r)}\cdot\sqrt{2}\\&= \frac{\sqrt{2}}{4}\left\{(1-r) + \frac{1}{1-r}\right\}\label{eq:2}
\end{align*}
$$

である．

以下$r$が動いた時の[(式2)](#eq:2)の値域から$\theta$の値域を求める．
簡単のため$t = 1-r$ および 

$$
\begin{align}
f(t) = t + \frac{1}{t}
\end{align}
$$

とおくと，(1)の結果より

$$
\begin{align}
-1+\sqrt{2} < t < 1
\end{align}
$$

であり，従って$y=f(t)$のグラフは以下のようになる．

<figure id="fig_4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1963/3/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $y=f(t)$のとりうる範囲．</figcaption>
</figure>

よって$2 < f(t) < 2\sqrt{2}$ である．[(式2)](#eq:2)に代入して

$$
\begin{align}
\frac{\sqrt{2}}{2} < \cos\frac{\theta}{2} < 1 \label{eq:3}
\end{align}
$$

を得る．$0 \le \theta \le \pi$ 及び $\cos \frac{\theta}{2}$ が同区間で単調減少なことから

$$
\begin{align}
0 < \frac{\theta}{2} < \frac{\pi}{4}\\\therefore 0 < \theta < \frac{\pi}{2}
\end{align}
$$

が求める$\theta$の範囲である．