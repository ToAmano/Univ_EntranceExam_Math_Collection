---
university: "titech"
category: "kouki"
year: "2005"
question: "2"
type: "solution"
title: "TITECH 2005 kouki Q2 (solution)"
---

## 【解】

  座標平面で考える．
  円$C$を原点中心とし，$x^2+y^2=1$とおく．
  $P(1,0)$, $Q(\cos\theta, \sin \theta)$とおく．
  対称性より
  
$$
\begin{align*}
0 \le\theta\le\pi
\end{align*}
$$

  で考える．

### (1)

  円 $A,B$ の半径 $r_A, r_B$，中心 $O_A, O_B$ とする．
  まず，点$P$で$A$と$C$が接するから，$O_A$は線分OP上にある．
  同様に点$Q$で$B$と$C$が接するから，$O_B$は線分OQ上にある．
  従って，これらの円の概要は図のようになる．

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2005/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円$A,B,C$の概形</figcaption>
</figure>

  以下，円$A$と$B$が接することから，$r_A$および$r_B$に関する条件を導く．
  まず，
  
$$
\begin{align*}
0 < r_A, r_B < 1
\end{align*}
$$

  のもとで，題意の条件より
  
$$
\begin{align}
\begin{dcases}
      \overline{OO_A}    = 1-r_A \\
      \overline{OO_B}    = 1-r_B \\
      \overline{O_AO_B} = r_A+r_B
    \end{dcases}\label{2005-2:eq:1}
\end{align}
$$

  である．
  $\theta\neq\pi$ の時 $\triangle O_A O O_B$ に余弦定理を用いて，$\eqref{2005-2:eq:1}$から
  
$$
\begin{align}
& \overline{O_A O_B}^2 = \overline{OO_A}^2 + \overline{OO_B}^2 -2 \overline{OO_A}\overline{OO_B}\cos\theta\nonumber\\\therefore& (r_A+r_B)^2 = (1-r_A)^2 + (1-r_B)^2 - 2(1-r_A)(1-r_B)\cos\theta\nonumber\\\therefore& 2r_A r_B = -2(r_A+r_B) + 2 - 2(1-r_A)(1-r_B)\cos\theta\nonumber\\\therefore& r_A r_B = -(r_A+r_B) + 1 - (1-r_A)(1-r_B)\cos\theta\label{2005-2:eq:2}
\end{align}
$$

  を得る．
  一方$\theta=\pi$のとき，$O,O_A,O_B$は$x$軸上にあり，
  
$$
\begin{align*}
r_A+r_B = 1
\end{align*}
$$

  となるが，これは$\eqref{2005-2:eq:2}$に内包される．そこで以下，$0<\theta\le\pi$で$\eqref{2005-2:eq:2}$を考える．

  新しい変数$\alpha,\beta$を
  
$$
\begin{align*}
\alpha& =r_A+r_B \\\beta& =r_A r_B
\end{align*}
$$

  とおくと，$\eqref{2005-2:eq:2}$は
  
$$
\begin{align}
& \beta               = -\alpha+1 - (1+\beta-\alpha)\cos\theta\nonumber\\\therefore& (1+\cos\theta)\beta = (1-\cos\theta)(1-\alpha) \label{2005-2:eq:3}
\end{align}
$$

  となる．

  また，$r_A, r_B$ は $x$ の2次方程式 $f(x)=x^2-\alpha x+\beta=0$ の $0<x<1$ をみたす2実解(重解含む)だから，
  このような$r_A,r_B$が存在するような$\alpha,\beta$の条件として
  
$$
\begin{align}
& \begin{dcases}
         \text{端点:}  & f(0)>0, f(1)>0           \\
         \text{判別式:} & D\ge 0                   \\
         \text{軸:}   & 0 < \frac{\alpha}{2} < 1
       \end{dcases}\nonumber\\\therefore& \begin{dcases}
         \text{端点:}  & \beta \ge 0, 1-\alpha+\beta \ge 0 \\
         \text{判別式:} & \alpha^2-4\beta \ge 0             \\
         \text{軸:}   & 0 < \frac{\alpha}{2} < 1
       \end{dcases}\nonumber\\\therefore& \begin{dcases}
          & 0 < \beta, \alpha-1 < \beta   \\
          & \beta \le \frac{1}{4}\alpha^2 \\
          & 0 < \alpha < 2
       \end{dcases}\label{2005-2:eq:4}
\end{align}
$$

  が課せられる．

  $\eqref{2005-2:eq:3,2005-2:eq:4}$を$\alpha\beta$平面に図示すると，
  [図1](#2005-2:fig:2,2005-2:fig:3)の太線部となる．

  

<figure id="2005-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2005/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $\theta\neq \pi$の時に$r_A,r_B$が存在するための$\alpha,\beta$の条件</figcaption>
</figure>

  

<figure id="2005-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2005/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $\theta=\pi$の時に$r_A,r_B$が存在するための$\alpha,\beta$の条件</figcaption>
</figure>

  これは数式に起こすと$t = \tan\frac{\theta}{2}$,$c=\cos\frac{\theta}{2}$, $s=\sin\frac{\theta}{2}$ として， として
  
$$
\begin{align}
\begin{dcases}
      0 < \theta < \pi \text{の時．} & \beta = t^2(1-\alpha) \quad \left(2\frac{(1-s)t}{c} \le \alpha < 1\right) \\
      \theta = \pi \text{の時．}     & \alpha=1, 0 < \beta \le \frac{1}{4}
    \end{dcases}\label{2005-2:eq:6}
\end{align}
$$

  である．

  さて，$A$ と $B$ の面積和を $T$ として，
  
$$
\begin{align}
T = \pi(r_A^2+r_B^2) = \pi(\alpha^2-2\beta) \label{2005-2:eq:5}
\end{align}
$$

  だから，$\eqref{2005-2:eq:6}$の条件のもとで，$\eqref{2005-2:eq:5}$を最小化する．

  
  \underline{**$0 < \theta < \pi$ の時**}

  $\eqref{2005-2:eq:5}$に$\eqref{2005-2:eq:6}$を代入して$\beta$を除去すると
  
$$
\begin{align*}
\frac{T}{\pi}& = \alpha^2-2\beta\\& = \alpha^2-2t^2(1-\alpha)  \\& = \alpha^2+2t^2\alpha-2t^2 \\& = (\alpha+t^2)^2-t^4-2t^2
\end{align*}
$$

  で $t>0$ と$\eqref{2005-2:eq:6}$から
  
$$
\begin{align*}
\alpha = \frac{2(1-s)t}{c}
\end{align*}
$$

  で $T$ は最小で，この時の最小値は
  
$$
\begin{align}
\frac{\min T}{\pi}& = \left[ 4\frac{(1-s)^2}{c^2} + 4\frac{s(1-s)}{c^2} - 2 \right] t^2 \nonumber\\& = \frac{2(s-1)^2 s^2}{c^4}\nonumber\\& = \frac{2(1-s)^2 s^2}{(1-s^2)^2}\nonumber\\& = \frac{2s^2}{(1+s)^2}\label{2005-2:eq:7}
\end{align}
$$

  を得る．

  
  \underline{**$\theta=\pi$ の時**}

  $\eqref{2005-2:eq:6}$から$\min T$ は
  $(\alpha,\beta)=(1,\frac{1}{4})$ の時の $\frac{1}{2}$ で，この時も$\eqref{2005-2:eq:7}$で良い．

  
  又，$\pi \le \theta \le 2\pi$ の時も対称性よりこれで良いので，($0 \to 2\pi-\theta$ ととりかえて同じになる)
  求める最小値は$0<\theta<2\pi$に対して
  
$$
\begin{align*}
S_\theta& = 2\pi\left(\frac{\sin\frac{\theta}{2}}{1+\sin\frac{\theta}{2}}\right)^2
\end{align*}
$$

  である．$\cdots$(答)

### (2)
 $x=1+\sin\frac{\theta}{2}$ とすると，$0\le x < 2\pi$で$0 \le x \le 2$ であり，
  
$$
\begin{align*}
S_\theta& = 2\pi\left(\frac{x-1}{x}\right)^2 \\& = 2\pi\left(1-\frac{1}{x}\right)^2
\end{align*}
$$

  で．これば $x=2$ すなわち $\theta=\pi$ の時最大値
  
$$
\begin{align*}
S_\theta = \frac{\pi}{2}
\end{align*}
$$

  をとる．$\cdots$(答)

  
  

## 【解説】

  平面図形の問題．立式できればあとは多変数関数の最小を求める問題に帰着する．

### (1)
がこの問題のポイントで，$\theta$を固定した時の二つの円の半径をどのように設定すれば面積の和が最小化するか？を考えれば良い．
  最大となるのは片方の円の半径が$0$（従ってもう片方の半径が$C$と同じ$1$）の時なので，その逆パターンとして両方の円の半径が等しい時だろうと想像がつく．
  それを数式で示していけばよい．
  答案では二つの円の半径を変数で設定して，$S_{\theta}$を計算して最小化した．
  二つの半径は対称なので，このような場合は対称式を導入して解いていくのが王道のやり方だ．

  実際，二つの円を同じ半径にするのが最も大きい$S$を与えることは
  $\eqref{2005-2:eq:6}$を見ればわかる．なぜならば$(\alpha,\beta)$が重解を持つ曲線(判別式$D=0$)
  
$$
\begin{align*}
\beta = \frac{\alpha^2}{4}
\end{align*}
$$

  上で$S_{\theta}$が最大になることを$\eqref{2005-2:eq:7}$の導出過程で示しているからである．

  さて，以上のような議論を考えると，$r_{A}=r_{B}$の時に$S_{\theta}$が最小になることがもっとわかりやすいように答案を作ることも考えられる．
  今回の答案では対称式を$\alpha=r_{A}+r_{B},\beta=r_{A}r_{B}$で定義したのでこの事実が分かりにくくなっている．

  そこで，$\beta$の代わりに$\gamma=r_{A}-r_{B}$を用いると，$\gamma=0$が明確に$S_{\theta}$の最小値を与えるはずである．
  $\beta$との関係は
  
$$
\begin{align*}
\beta = \frac{\alpha^2 -\gamma^2}{4}
\end{align*}
$$

  だから，条件$\eqref{2005-2:eq:3,2005-2:eq:4,2005-2:eq:5}$は（簡単のため$\theta\neq\pi$の時のみ考えると）
  
$$
\begin{align*}
& \begin{dcases}
         S_{\theta} = \frac{\pi}{2}\left(\alpha^2+\gamma^2\right)              \\
         (1+\cos\theta)\frac{\alpha^2 -\gamma^2}{4} = (1-\cos\theta)(1-\alpha) \\
         0 < \frac{\alpha^2 -\gamma^2}{4}                                      \\
         \alpha-1 < \frac{\alpha^2 -\gamma^2}{4}                               \\
         \frac{\alpha^2 -\gamma^2}{4} \le \frac{1}{4}\alpha^2                  \\
         0 < \alpha < 2
       \end{dcases}\\\therefore& \begin{dcases}
         \frac{2S_{\theta}}{\pi} = \left(\alpha^2+\gamma^2\right)           \\
         \gamma^2 = \alpha^2 + 4\frac{1-\cos\theta}{1+\cos\theta}(\alpha-1) \\
         \gamma^2 < \alpha^2                                                \\
         \gamma^2 < (2-\alpha)^2                                            \\
         0 < \alpha < 2
       \end{dcases}
\end{align*}
$$

  となる．ここで，$\alpha\gamma$平面にこの条件を図示すると[図4](#2005-2:fig:4)の赤線部（端点含む）となる．
  $\sqrt{\frac{2S_{\theta}}{\pi}}$は平面上の円の半径と解釈できる．
  よって，とりうる$S_{\theta}$の範囲は，赤線部の双曲線と円が交点を持つ範囲で規定される．
  図から$S_{\theta}$が最小になるのは
  円が双曲線と$\alpha$軸の交点$(\sqrt{\frac{4(1-\cos\theta)}{1+\cos\theta}},0)$を通る時である．
  よって明確に$\gamma=0$であることが示された．

  

<figure id="2005-2:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2005/2/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $\theta\neq \pi$の時に$r_A,r_B$が存在するための$\alpha,\gamma$の条件は赤字太線部．$S_{\theta}$は図形的に$\alpha\gamma$平面の円である．</figcaption>
</figure>

  従って，求めるべき$S_{\theta}$は
  
$$
\begin{align*}
S_{\theta}& = \frac{\pi}{2}\left[\left(\sqrt{\frac{4(1-\cos\theta)}{1+\cos\theta}}\right)^2+0^2\right]\\& = \frac{2\pi(1-\cos\theta)}{(1+\cos\theta)}\\& = \frac{2\pi\sin\frac{\pi}{2}}{1+\sin\frac{\pi}{2}}
\end{align*}
$$

  となり，答案と一致する．こちらの解法の方が図形的に分かり易く，問題の構造も明確になるため優れている．
  問題の裏側がわかると答案に工夫ができる良い例である．

### (2)
は正真正銘のボーナス問題で，$S_{\theta}$が出ていれば一撃でその最大値が求まる．
  この手の形は解答中で実演しているように，分母が綺麗になるように変数変換すると見通しが良くなることが多い．

  答えも$\theta=\pi$の時で，これは直感的にも一番円の半径を大きくできそうである．
  この時$\eqref{2005-2:eq:2}$から$r_A+r_B=1$を保ちながら，
  
$$
\begin{align*}
S_{\theta} = \pi\left(r_A^2+r_B^2\right)
\end{align*}
$$

  を最大化すれば良いが，$y=x^2$が下に凸なことからイェンゼンの不等式を利用すると
  
$$
\begin{align*}
S_{\theta} = \pi\left(r_A^2+r_B^2\right)\le 2\pi\left(\frac{r_A+r_B}{2}\right)^2 = \frac{\pi}{2}
\end{align*}
$$

  を得る．等号成立条件は$r_A=r_B$の時で，二つの円の半径が$1/2$の時である．