---
university: "utokyo"
category: "kouki"
year: "2007"
question: "1"
type: "solution"
title: "UTOKYO 2007 kouki Q1 (solution)"
---

## 【解】

    (1)

    曲線$C: xy^2=4$ を $yx$ 平面に図示すると[図1](#2007-1:fig:1)のようになる．
    

<figure id="2007-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2007/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 曲線$C$と点$P_0,P_1,P_2$の様子</figcaption>
</figure>

    両辺$y^2$で割ってから$x$で微分すると，微分の連鎖律より
    

$$
\begin{align*}
& \frac{d}{dx}\left(x\right) = \frac{d}{dx}\left(\frac{4}{y^2}\right)\\\therefore& 1 = \frac{dy}{dx}\cdot\frac{d}{dy}\left(\frac{4}{y^2}\right)\\\therefore& 1 = \frac{dy}{dx}\cdot\left(\frac{-8}{y^3}\right)\\\therefore& \frac{dy}{dx} =  \left(\frac{-y^3}{8}\right)
\end{align*}
$$

    だから，$P_0(x_0, y_0)$ における$C$の接線 $l_0$ は
    

$$
\begin{align*}
y = \frac{-y^3_0}{8}\left(x-x_0\right) + y_0
\end{align*}
$$

    である．
    従って，これと$C$の交点の$x$座標は$C$の方程式と連立した方程式の解である．
    $(x_0,y_0)$が$x_0y^2_0=4$を満たすこと，
    および接線の性質からこの方程式が$x-x_0$を重根として持つことに留意して式変形を進める．
    

$$
\begin{align*}
& x\left(\frac{-y^3_0}{8}\left(x-x_0\right) + y_0\right)^2 = 4           \\\therefore& xy^2_{0}\left(-\frac{y^2_0}{8}\left(x-x_0\right) + 1\right)^2 = 4      \\\therefore& \frac{4x}{x_0}\left(-\frac{1}{2x_0}\left(x-x_0\right) + 1\right)^2 = 4 \\\therefore& \frac{x}{x_0}\left(-\frac{x}{x_0}+ 3\right)^2 = 4                      \\
\end{align*}
$$

    ここで，$t=x/x_0$とおくと
    

$$
\begin{align}
& t(t^2-6t+9) = 4                      \\\therefore& t^3-6t^2+9t-4 = 0                    \\\therefore& (t-1)^2(t-4) = 0 \label{2007-1:eq:1}
\end{align}
$$

    となり，$P_1(x_1,y_1)$の$x$座標は
    

$$
\begin{align}
x_1 = 4x_0 = \frac{16}{y^2_0}\label{2007-1:eq:2}
\end{align}
$$

    である．この時の$y$座標は$y<0$より
    

$$
\begin{align}
y_1 = -\sqrt{\frac{4}{x_1}} = -\frac{1}{2}y_0 \label{2007-1:eq:3}
\end{align}
$$

    である．

    次に，$P_1$での$C$の接線は$(x_0,y_0)$を$(x_1,y_1)$で置き換えればよく，
    [(式1)](#2007-1:eq:1)と同様の議論によって$P_2(x_2,y_2)$の$x$座標は
    

$$
\begin{align}
x_2 = 4x_1 = 16 x_0 = \frac{64}{y^2_0}\label{2007-1:eq:4}
\end{align}
$$

    である．この時の$y$座標は$y>0$より
    

$$
\begin{align}
y_2 = \sqrt{\frac{4}{x_2}} = \frac{1}{4}y_0 \label{2007-1:eq:5}
\end{align}
$$

    以上[(式5)](#2007-1:eq:2,2007-1:eq:3,2007-1:eq:4,2007-1:eq:5)より求める座標は
    

$$
\begin{align*}
\begin{dcases}
            P_1 = (x_1,y_1) = \left(\frac{16}{y^2_0},-\frac{1}{2}y_0\right) \\
            P_2 = (x_2,y_2) = \left(\frac{64}{y^2_0},\frac{1}{4}y_0\right)
        \end{dcases}
\end{align*}
$$

    である．$\cdots$(答)
    

    (2)

    

<figure id="2007-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2007/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 三角形$P_0P_1P_2$の様子</figcaption>
</figure>

    まず三角形$P_0P_1P_2$の面積$T$を求める．(1)の結果から
    

$$
\begin{align*}
\vec{P_0 P_1}& = \begin{pmatrix} 16/y^2_0 - 4/y_0^2 \\ -\frac{1}{2}y_0 - y_0 \end{pmatrix} = \begin{pmatrix} 12/y_0 \\ -\frac{3}{2}y_0 \end{pmatrix} \\\vec{P_0 P_2}& = \begin{pmatrix} 64/y^2_0 - 4/y^2_0 \\\frac{1}{4}y_0 - y_0 \end{pmatrix} = \begin{pmatrix} 60/y^2_0 \\ -\frac{3}{4}y_0 \end{pmatrix}
\end{align*}
$$

    だから，サラスの公式から$T$は
    

$$
\begin{align}
T
         & = \frac{1}{2}\left| -\frac{3}{2}y_0 \cdot\frac{60}{y_0} + \frac{3}{4}y_0 \cdot\frac{12}{y_0}\right|\\& = \frac{1}{2}\left| -90 + 9 \right|\\& = \frac{81}{2}\frac{1}{y_0}\label{2007-1:eq:6}
\end{align}
$$

    である．

    次に$S$を求めるために，曲線$C$と線分$P_0P_2$で囲まれる面積を$T'$とすると
    

$$
\begin{align}
S = T -T' \label{2007-1:eq:7}
\end{align}
$$

    である．

    

<figure id="2007-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2007/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 面積$S$と$T'$の様子．$P_0, P_2$から$y$軸におろした垂線を$A, B$とおく．</figcaption>
</figure>

    [図3](#2007-1:fig:3)のように$P_0, P_2$から$y$軸におろした垂線を$A, B$とおくと
    

$$
\begin{align}
T'
         & = \text{台形}P_0ABP_2 - \int_{y_2}^{y_0} x \, dy                                                                               \\& = \frac{1}{2}\left(\frac{4}{y_0} + \frac{64}{y_0}\right)\frac{3}{4}y_0 - \int_{\frac{1}{4}y_0}^{y_0}\frac{4}{y^2}\, dy \\& = \frac{51}{2y_0} + \left[\frac{4}{y}\right]_{\frac{1}{4}y_0}^{y_0}\\& = \frac{27}{2y_0}\label{2007-1:eq:8}
\end{align}
$$

    であるから，
    [(式8)](#2007-1:eq:6,2007-1:eq:8)を[(式7)](#2007-1:eq:7)に代入して
    

$$
\begin{align*}
S
         & =\frac{81}{2}\frac{1}{y_0} - \frac{27}{2y_0}\\& =\frac{27}{y_0}
\end{align*}
$$

    である．従って求める比は
    

$$
\begin{align*}
\frac{T}{S}& = \frac{81/2}{27}\\& = \frac{3}{2}
\end{align*}
$$

    である．$\cdots$(答)
    

    (3)
    (1)より$l_0$ の傾きは $-\frac{y^3_0}{8}$, $l_1$ の傾きは $-\frac{y^3_{1}}{8}$ だから，
    $\angle P_0 P_1 P_2 = \frac{\pi}{2}$ となる条件は
    

$$
\begin{align*}
& -\frac{y^3_0}{8}\cdot\left(-\frac{y^3_{1}}{8}\right) = -1 \\\therefore& y^3_0y^3_1 = -64
\end{align*}
$$

    ここに[(式3)](#2007-1:eq:3)を代入して題意より$y_0>0$に注意すると
    

$$
\begin{align*}
& y^3_0 \left(\frac{-y_0}{2}\right)^3 = -64 \\& y^6_0 = 2^9                               \\& y_0 = 2^{3/2}
\end{align*}
$$

    である．$\cdots$(答)
    

    (4)
    (3)の条件が満たされるとき，つまり$\angle P_0 P_1 P_2 = \frac{\pi}{2}$ の時，
    円周角の定理より$\triangle P_0 P_1 P_2$ の外接円の直径$R$は線分$P_0P_2$の長さと等しく，
    (1)で求めた$P_2$の座標を利用して
    

$$
\begin{align*}
R
         & =  \overline{P_0 P_2}\\& =  \left|\begin{pmatrix}64/y_0^2-4/y_0^2                                          \\ y_0/4 - y_0\end{pmatrix}\right|\\& =  \left|\begin{pmatrix}60/y_0^2                                                  \\ -3y_0/4 \end{pmatrix}\right|\\& = \sqrt{\left(\frac{60}{y_0}\right)^2 + \left(-\frac{3}{4}y_0\right)^2 }\\& = \sqrt{\frac{9}{16}y_0^2 + \frac{3600}{y_0^2}}\\
\end{align*}
$$

    を得る．
    ここに(3)の結果$y_0=2^{3/2}$に代入すると
    

$$
\begin{align*}
R
         & = \sqrt{\frac{9}{2}+\frac{225}{4}}\\& = \frac{9\sqrt{3}}{2}
\end{align*}
$$

    である．
    従って外接円の面積$S'$は
    

$$
\begin{align*}
S'
         & = \pi\left(\frac{R}{2}\right)^2         \\& = \pi\left(\frac{9\sqrt{3}}{4}\right)^2 \\& = \pi\frac{81 \cdot 3}{16}\\& = \frac{243}{16}\pi
\end{align*}
$$

    である．$\cdots$(答)
    

    

## 【解説】

    (1)
    時間短縮になるか微妙なところだが，問題が$y_0$を基軸として答えを出すように要求しているので最初から$x=f(y)$の形で変形していくことも考えられる．

    $\left(\frac{4}{y}\right)' = -\frac{4}{y^2}$ より，$P_0(x_0, y_0)$ における接線 $l_0$ は
    \[
        l_0: x = -\frac{4}{y_0^2}(y-y_0) + \frac{4}{y_0}
    \]
    \[
        = -\frac{4}{y_0^2}y + \frac{8}{y_0}
    \]
    である．したがって，これと $C$ の交点の $y$ 座標は
    \[
        \left(-\frac{4}{y_0^2}y + \frac{8}{y_0}\right) y = 4
    \]
    \[
        -4y^2 + 8y_0 y = 4y_0^2
    \]
    \[
        4y^2 - 8y_0 y + 4y_0^2 = 0
    \]
    \[
        y^2 - 2y_0 y + y_0^2 = 0
    \]
    \[
        (y-y_0)^2 = 0
    \]
    の解だから，$P_0$ の $y$ 座標は $y_0$ である．

    さらに，この点で $C$ の接線 $l_1$ についても同様にして，$y_1 = -\frac{1}{2}y_0$ のとき，$x_1 = -\frac{4}{y_1^2}y_1 + \frac{8}{y_1} = -\frac{4}{(-\frac{1}{2}y_0)} + \frac{8}{(-\frac{1}{2}y_0)} = \frac{8}{y_0} - \frac{16}{y_0} = -\frac{8}{y_0}$.

    $P_1$ の $y$ 座標は $y_1 = -\frac{1}{2}y_0$ である．
    $P_2$ の $y$ 座標は $y_2 = \frac{1}{4}y_0$ である．

    $P_1\left(\frac{16}{y_0}, -\frac{1}{2}y_0\right)$ $P_2\left(\frac{64}{y_0}, \frac{1}{4}y_0\right)$