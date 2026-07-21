---
university: "sample_titech"
category: "kouki"
year: "2002"
question: "2"
type: "solution"
title: "SAMPLE_TITECH 2002 kouki Q2 (solution)"
---

## 【解】

  $xyz$空間の原点$O(0,0,0)$, 円錐の頂点を$R(0,0,\sqrt{3})$とする．
  円錐の概形は[図1](#2002-2:fig:1)となる．

  

<figure id="2002-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/2002/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円錐の様子</figcaption>
</figure>

### (1)

  $xy$平面で考える．
  線分 $MQ$ が $M$ 以外に $C$ と交わらないということは，
  $\theta$の境界の値では，$MQ$と$C$が接するので，まずはこの場合を考える．
  この様子を[図2](#2002-2:fig:2)に示す．

  

<figure id="2002-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/2002/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $xy$平面での$P,Q,M$の様子</figcaption>
</figure>

  $M$での$C$の接線の方程式は
  
$$
\begin{align*}
\cos\theta x + \sin\theta y = 1
\end{align*}
$$

  であり，これが$Q(-2,0)$を通るので，
  
$$
\begin{align*}
-2\cos\theta = 1 \\\therefore\theta = \pm\frac{4\pi}{3}
\end{align*}
$$

  である．
  従って$\theta$の取り得る範囲はこれらの$\theta$の時より点$M$が$Q$側になる場合で，
  
$$
\begin{align*}
\frac{2\pi}{3}\le\theta\le\frac{4\pi}{3}
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  Sの展開図上で線分PMとなる曲線を$D$とする．
  PからMまでの最短経路は, PからMまで$D$上通り,
  MからQまで直線MQを通る経路である．$\cdots$(*)

  最短経路の長さ$f(\theta)$とすると
  
$$
\begin{align}
f(\theta) = |PM| + |QM|\label{2002-2:eq:1}
\end{align}
$$

  である．

  まず線分PMの長さを求める．
  Sの側面の展開図は[図3](#2002-2:fig:3)である．

  

<figure id="2002-2:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/2002/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 円錐側面の展開図</figcaption>
</figure>

  対称性から
  
$$
\begin{align}
0 \le\theta\le\pi\label{2002-2:eq:4}
\end{align}
$$

  として考える．

  まず，PMの劣弧の長さは，$\angle POQ=\theta$より
  
$$
\begin{align*}
\text{劣弧PM}& = \theta
\end{align*}
$$

  だから，円錐の側面の長さが$PR=2$であることにも留意すると
  
$$
\begin{align*}
\angle\text{MRP}& = \frac{\theta}{2}
\end{align*}
$$

  となるので，展開図上のPMの長さ$l(\theta)$は
  
$$
\begin{align}
l(\theta) & = 4 \sin\frac{\theta}{2}\label{2002-2:eq:2}
\end{align}
$$

  となる．

  次に，線分QMの長さを求める．これは各点の座標から，
  
$$
\begin{align}
|\text{QM}|
     & = \sqrt{(\cos\theta+2)^2 + \sin^2\theta}\\& = \sqrt{5+4\cos\theta}\label{2002-2:eq:3}
\end{align}
$$

  となる．

  以上$\eqref{2002-2:eq:2,2002-2:eq:3}$を$\eqref{2002-2:eq:1}$に代入すると，$\theta$を与えた時の最短経路の長さ$f(\theta)$は
  
$$
\begin{align}
f(\theta)
     & = l(\theta) + |\text{QM}|                                          \\& = 4\sin\frac{\theta}{2} + \sqrt{5+4\cos\theta}\label{2002-2:eq:5}
\end{align}
$$

  となる．

### (1)
および$\eqref{2002-2:eq:4}$から，この関数の
  
$$
\begin{align}
\frac{2\pi}{3}\le\theta\le\pi\label{2002-2:eq:6}
\end{align}
$$

  での最小値をもとめにば良い．新しく
  
$$
\begin{align*}
t=\cos\frac{\theta}{2}
\end{align*}
$$

  とおくと，半角および倍角の公式から
  
$$
\begin{align*}
\sin\frac{\theta}{4}& = \sqrt{\frac{1-\cos\frac{\theta}{2}}{2}}& \left(\sin\frac{\theta}{4}\ge 0\right)\\& = \sqrt{\frac{1-t}{2}}
\end{align*}
$$

  および
  
$$
\begin{align*}
\cos\theta& = 2\cos^2\frac{\theta}{2} - 1 \\& = 2t^2-1
\end{align*}
$$

  から，$f$の変数を$\theta$から$t$に移して
  
$$
\begin{align}
f(t)
     & = 4\sqrt{\frac{1-t}{2}} + \sqrt{5+4(2t^2-1)}\nonumber\\& = 2\sqrt{2(1-t)} + \sqrt{8t^2+1}\label{2002-2:eq:9}
\end{align}
$$

  となる．
  $\eqref{2002-2:eq:6}$から
  
$$
\begin{align}
0\le t \le\frac{1}{2}\label{2002-2:eq:7}
\end{align}
$$

  である．$f$の一階微分は
  
$$
\begin{align*}
f'(t)
     & = \frac{-2}{\sqrt{2(1-t)}} + \frac{16t}{2\sqrt{8t^2+1}}\\\\& = \frac{-2\sqrt{8t^2+1} + 8t\sqrt{2(1-t)}}{\sqrt{2(1-t)}\sqrt{8t^2+1}}\\& = \frac{-4(8t^2+1) + 2\cdot 8^2t^2(1-t)}{2\sqrt{2(1-t)}\sqrt{8t^2+1}\left(2\sqrt{8t^2+1} + 8t\sqrt{2(1-t)}\right)}\\& = \frac{4(-32t^3 + 24t^2-1)}{\sqrt{2(1-t)}\sqrt{8t^2+1}\left(\sqrt{8t^2+1} + 8t\sqrt{2(1-t)}\right)}
\end{align*}
$$

  である．この分母は常に正だから，$f'(t)$の正負は分子の正負と等しい．
  そこで分子を因数分解すると
  
$$
\begin{align*}
& -32t^3 + 24t^2-1                                                                                                            \\& = -32\left(t^3-\frac{3}{4}t^2+\frac{1}{32}\right)\\& = -32\left(t-\frac{1}{4}\right)\left(t^2-\frac{1}{2}t-\frac{1}{8}\right)\\& = -32\left(t-\frac{1}{4}\right)\left(t-\frac{1}{4}+\sqrt{\frac{3}{16}}\right)\left(t-\frac{1}{4}-\sqrt{\frac{3}{16}}\right)
\end{align*}
$$

  である．$\eqref{2002-2:eq:7}$の$t$の区間に注意して，
  
$$
\begin{align*}
\frac{1}{4}-\sqrt{\frac{3}{16}} < 0 < \frac{1}{4} < \frac{1}{2} < \frac{1}{4}+\sqrt{\frac{3}{16}}
\end{align*}
$$

  だから，$f(t)$の増減表は$\eqref{2002-2:table:1}$となる．

  \begin{table}[H]
    \centering
    \caption{$f(t)$の増減表}
    \label{2002-2:table:1}
    

| $t$ | $0$ | | $1/4$ | | $1/2$ |
|:----:|:-------------:|:----------:|:-----:|:----------:|:------------:|
| $f'$ | | $-$ | $0$ | $+$ | |
| $f$ | $1+2\sqrt{2}$ | $\searrow$ | 最小 | $\nearrow$ | $2+\sqrt{3}$ |

  \end{table}

  従って，求める最小値は$t=1/4$の時で
  
$$
\begin{align*}
\min f(t)
     & = f\left(\frac{1}{4}\right)\\& = 2\sqrt{2\left(1-\frac{1}{4}\right)} + \sqrt{8\left(\frac{1}{4}\right)^2+1}\\& = \sqrt{6} + \sqrt{\frac{3}{2}}\\& = \frac{3\sqrt{6}}{2}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】

  最後の$f(\theta)$の最小値を求める部分はいくつかやり方がある．
  いずれもこの形のまま計算するのは厳しく，なんらか新しい変数を置いてやることになるだろう．
  今回の解答のように，$\theta/2$を利用する方が$\theta/4$と$\theta$を対称に扱っていて計算は早い．

  それを見るために，$t=\sin\frac{\theta}{4}$として求めてみよう．
  $\theta$の動く範囲が$\eqref{2002-2:eq:4}$だから，
  
$$
\begin{align}
\frac{1}{2}\le t \le\frac{\sqrt{2}}{2}\label{2002-2:eq:10}
\end{align}
$$

  である．$\eqref{2002-2:eq:9}$に倍角公式を利用して$t$で表すと
  
$$
\begin{align*}
f(t) & = 4t + \sqrt{9-32t^2(1-t^2)}
\end{align*}
$$

  だから，一階微分は
  
$$
\begin{align*}
f'(t)
     & = 4 + \frac{128t^3 - 64t}{2\sqrt{9-32t^2(1-t^2)}}\\& = 4 \frac{\sqrt{32t^4-32t^2+9}+16t^3-8t}{\sqrt{32t^4-32t^2+9}}
\end{align*}
$$

  となり，分母は常に正だから$f'$の符号は分子の符号に等しい．
  
$$
\begin{align*}
& f'(t) \ge 0                                                                                   \\\Leftrightarrow& \sqrt{32t^4-32t^2+9}\ge 8t(1-2t^2) \quad(\ge 0) \quad(\because\text{$\eqref{2002-2:eq:10}$}) \\\Leftrightarrow& 32t^4-32t^2+9 \ge 64t^2(1-2t^2)^2                                                             \\\Leftrightarrow& 256s^3-288s^2+96s-9 \le 0 \quad(s=t^2, \frac{1}{4}\le s \le\frac{1}{2})                    \\\Leftrightarrow& (s-\frac{3}{8})(256s^2-192s+24) \le 0                                                         \\\Leftrightarrow& (s-\frac{3}{8})(s-\frac{3+\sqrt{3}}{16})(s-\frac{3-\sqrt{3}}{16}) \le 0
\end{align*}
$$

  だから. $f$の増減表は$\eqref{2002-2:table:2}$となる．
  \begin{table}[H]
    \centering
    \caption{$f$の増減表}
    \label{2002-2:table:2}
    

| $t$ | $\frac{1}{2}$ | | $\frac{\sqrt{6}}{4}$ | | $\frac{\sqrt{2}}{2}$ |
|:--:|:--:|:--:|:--:|:--:|:--:|
| $s=t^2$ | $\frac{1}{4}$ | | $\frac{3}{8}$ | | $\frac{1}{2}$ |
| $f'$ | | $-$ | $0$ | $+$ | |
| $f$ | | $\searrow$ | | $\nearrow$ | |

  \end{table}
  したがって，$f(t)$は
  
$$
\begin{align*}
t=\frac{\sqrt{6}}{4}
\end{align*}
$$

  で最小値
  
$$
\begin{align*}
\min f(\theta)
     & = \sqrt{6}+\frac{\sqrt{6}}{2}\\& = \frac{3\sqrt{6}}{2}
\end{align*}
$$

  をとる.