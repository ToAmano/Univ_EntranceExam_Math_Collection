---
university: "titech"
category: "kouki"
year: "2009"
question: "2"
type: "solution"
title: "TITECH 2009 kouki Q2 (solution)"
---

## 【解】

  双曲線と点$P$は[図1](#2009-2:fig:1)のような関係になる．

  

<figure id="2009-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2009/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形$PAB$の様子</figcaption>
</figure>

  従って，接点$A,B$の$x$成分を$m,s$として，
  
$$
\begin{align*}
m < 0 < s
\end{align*}
$$

  と置いて良い．

  この時，点$A,B$での接線$l_A,l_B$の方程式は
  
$$
\begin{align*}
l_A & : y = \frac{1}{m^2}x - \frac{2}{m}\\
    l_B & : y = \frac{1}{s^2}x - \frac{2}{s}
\end{align*}
$$

  である．この2本の直線の交点が$P(p,q)$だから，$l_A, l_B$を連立して
  
$$
\begin{align*}
& \frac{1}{m^2}p - \frac{2}{m}                                               = \frac{1}{s^2}p - \frac{2}{s}\\\therefore& \left(\frac{1}{m^2}-\frac{1}{s^2}\right) p                                 = -\frac{2}{s} +  \frac{2}{m}\\\therefore& \left(\frac{1}{m}-\frac{1}{s}\right)\left(\frac{1}{m}+\frac{1}{s}\right) p  = -\frac{2}{s} +  \frac{2}{m}\\\therefore& \left(\frac{1}{m}+\frac{1}{s}\right) p                                      = 2
\end{align*}
$$

  だから
  
$$
\begin{align}
p & = \frac{2}{\left(\frac{1}{m}+\frac{1}{s}\right)} = \frac{2ms}{m+s}\label{2009-2:eq:1}
\end{align}
$$

  である．この時$q$は$l_A$の式に代入して
  
$$
\begin{align}
q
     & = \frac{1}{m^2} p - \frac{2}{m}\nonumber\\& = \frac{1}{m^2}\cdot\frac{2ms}{m+s} - \frac{2}{m}\nonumber\\& = \frac{2s}{m(m+s)} - \frac{2}{m}\nonumber\\& = \frac{2s - 2(m+s)}{m(m+s)}\nonumber\\& = \frac{-2m}{m(m+s)}\nonumber\\& = \frac{-2}{m+s}\label{2009-2:eq:2}
\end{align}
$$

  となる．

  以下$\eqref{2009-2:eq:1,2009-2:eq:2}$を用いて三角形PABの面積を求める．
  まず，
  
$$
\begin{align*}
\vec{PA} = \begin{pmatrix} m - p \\ -\frac{1}{m} - q \end{pmatrix}\\\vec{PB} = \begin{pmatrix} s - p \\ -\frac{1}{s} - q \end{pmatrix}
\end{align*}
$$

  であることに注意する．これら二つのベクトルの作る三角形の面積公式から，
  $\triangle PAB$の面積$f$として
  
$$
\begin{align}
f
     & = \frac{1}{2}\left|(m-p)\left(-\frac{1}{s}-q\right) - (s-p)\left(-\frac{1}{m}-q\right)\right|\nonumber\\& = \frac{1}{2}\left|\left(m-\frac{2ms}{m+s}\right)\left(-\frac{1}{s}+\frac{2}{m+s}\right)\right.\nonumber\\& \quad\left. - \left(s-\frac{2ms}{m+s}\right)\left(-\frac{1}{m}+\frac{2}{m+s}\right)\right|\nonumber\\& = \frac{1}{2}\left|\frac{m^2-ms}{m+s}\cdot\frac{-m+s}{s(m+s)} - \frac{s^2-ms}{m+s}\cdot\frac{-s+m}{m(m+s)}\right|\nonumber\\& = \frac{1}{2(m+s)^2}\left|\frac{m(m-s)(-m+s)}{s} - \frac{s(s-m)(-s+m)}{m}\right|\nonumber\\& = \frac{1}{2(m+s)^2}\left|\frac{-m(s-m)^2}{s} + \frac{s(s-m)^2}{m}\right|\nonumber\\& = \frac{1}{2(m+s)^2}\left| -(s-m)^2 \left(\frac{m}{s} - \frac{s}{m}\right)\right|\nonumber\\& = \frac{1}{2(m+s)^2}\left| -(s-m)^2 \frac{m^2-s^2}{ms}\right|\nonumber\\& = \frac{1}{2(m+s)^2}\left|\frac{(s-m)^3 (m+s)}{ms}\right|\nonumber\\& = \frac{1}{2}\left|\frac{(s-m)^3}{ms(m+s)}\right|\label{2009-2:eq:3}
\end{align}
$$

  となる．

  次に，これを$t=pq$を用いて書き直すため，
  
$$
\begin{align*}
\alpha& =m+s        \\\beta& =s-m\,(>0)
\end{align*}
$$

  とおくと，
  
$$
\begin{align*}
sm
     & =\frac{1}{4}\left[(m+s)^2-(s-m)^2\right]\\& =\frac{1}{4}(\alpha^2-\beta^2)
\end{align*}
$$

  だから，$\eqref{2009-2:eq:3}$に代入して
  
$$
\begin{align}
f
     & =\frac{1}{2}\left|\frac{\beta^3}{\frac{1}{4}(\alpha^2-\beta^2)\alpha}\right|\nonumber\\& =2\left|\frac{\beta^3}{\alpha(\alpha^2-\beta^2)}\right|\label{2009-2:eq:4}
\end{align}
$$

  を得る．一方で，$t$を$\alpha,\beta$で表すと$\eqref{2009-2:eq:1,2009-2:eq:2}$より
  
$$
\begin{align}
t
     & = pq                                     \nonumber\\& = -4\frac{ms}{(m+s)^2}\nonumber\\& = -4\frac{\frac{1}{4}(\alpha^2-\beta^2)}{\alpha^2}\nonumber\\& =-\frac{\alpha^2-\beta^2}{\alpha^2}\nonumber\\& =-1+\left(\frac{\beta}{\alpha}\right)^2 \label{2009-2:eq:5}
\end{align}
$$

  $a = \alpha/\beta$と置いて$\eqref{2009-2:eq:4,2009-2:eq:5}$に代入して$f$と$t$を表すと
  
$$
\begin{align*}
f & =2\left|\frac{1}{a(a^2-1)}\right|\\
    t & =-1+\frac{1}{a^2}
\end{align*}
$$

  である．第二式から$|a|=\sqrt{\frac{1}{t+1}}$ だから，第一式に代入して
  
$$
\begin{align}
f
     & =2\left|\frac{1}{\sqrt{\frac{1}{t+1}}\left(\frac{1}{t+1}-1\right)}\right|\nonumber\\\\& =2\frac{\sqrt{t+1}(t+1)}{t}\quad(\because t>0) \label{2009-2:eq:6}
\end{align}
$$

  を得る．これが三角形PABの面積を$t=pq$で表したものである．$\cdots$(答)

  
  次に，この三角形の面積の最小値を求める．
  点Pが第一章限にあることから$t>0$での$\eqref{2009-2:eq:6}$の最小値を求めれば良い．
  新しく
  
$$
\begin{align*}
x = t^{1/3}\quad(x>0)
\end{align*}
$$

  と置いて式を整理すると
  
$$
\begin{align*}
f
     & = 2\sqrt{\frac{(t+1)^3}{t^2}}\\& = 2\sqrt{\frac{(x^3+1)^3}{x^6}}\\& = 2\sqrt{\left(x + \frac{1}{x^2}\right)^3}\\& = 2\left(\frac{x}{2}+\frac{x}{2} + \frac{1}{x^2}\right)^{3/2}\\& \ge 2 \left(3\sqrt[3]{\frac{1}{2}\frac{1}{2}}\right)^{3/2}\\& = 3\sqrt{3}
\end{align*}
$$

  である．ただし下から2行目の不等式は相加相乗平均の不等式による．
  等号成立は
  
$$
\begin{align*}
& \frac{x}{2} =  \frac{1}{x^2}\\& x =\sqrt[3]{2}
\end{align*}
$$

  の時，すなわち
  
$$
\begin{align*}
t = 2
\end{align*}
$$

  の時である．これは$t>0$を満たしているから，求める面積の最小値は
  
$$
\begin{align*}
\min f = 3\sqrt{3}
\end{align*}
$$

  である．$\cdots$(答)

  

## 【解】

  平面図形の問題．計算量が多いので正確な処理能力を求められる一題だ．
  接点を文字でおいて，最後に$t$を用いておいた接点のパラメータを消しにいく方針が一番わかりやすいだろう．
  今回のように，対称な文字をいくつか設定した場合は基本的には対称式を用いて文字消去をしていく方針になる．

  三角形の面積公式としてサラスの公式を利用しているので復習しよう．
  三角形OABにおいて，Oを原点とし，AとBの位置ベクトルを
  
$$
\begin{align*}
\vec{a} = \mqty(a_x,a_y) \\\vec{b} = \mqty(b_x,b_y)
\end{align*}
$$

  とすると，三角形OABの面積$S$は
  
$$
\begin{align*}
S = \frac{1}{2}\left|a_xb_y-a_yb_x\right|
\end{align*}
$$

  で与えられる．
  行列を知っている人であれば，これは$\vec{a},\vec{b}$から作った二次元正方行列
  
$$
\begin{align*}
\mqty(a_x & b_x \\ a_y & b_y)
\end{align*}
$$

  の行列式であることがわかるだろう．

  ちなみに，同様に三次元への拡張として，四面体OABCの体積$V$を求めることができる．
  原点を$O$とし，$A(a_x,a_y,a_z), B(b_x,b_y,b_z), C(c_x,c_y,c_z)$とすると，
  
$$
\begin{align*}
V
     & = \frac{1}{6}\left|\det\mqty(a_x                                                               & b_x & c_x \\ a_y & b_y & c_y \\ a_z & b_z & c_z) \right|\\& = \frac{1}{6}\left|a_xb_yc_z + a_yb_zc_x + a_zb_xc_y - a_zb_yc_x - a_xb_zc_y - a_yb_xc_z\right|
\end{align*}
$$

  が成り立つことが知られている．

  次に，最後三角形の面積の最小値を求めるところは，
  通常微分して増減表を書くところだが計算量低減のため相加相乗平均を利用している．
  微分して求める場合でも，$x$である程度書き換えてからルートの中身だけ微分することで計算量を減らせる．