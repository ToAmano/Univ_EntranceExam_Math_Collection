---
university: "titech"
category: "kouki"
year: "1991"
question: "2"
type: "solution"
title: "TITECH 1991 kouki Q2 (solution)"
---

## 【解】

  座標平面上で考える．円Kを原点中心半径$2$の円$x^2+y^2=4$とし，正方形ABCDを$A(1,1), B(1,-1), C(-1,-1), D(-1,1)$とする．
  K上の点Pを$P(c=2\cos\alpha,s=2\sin\alpha)$とする．対称性から $0 \le \alpha \le \pi/4 \dots$ で調べれば良い．

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1991/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 座標平面上の円Kと正方形ABCD</figcaption>
</figure>

  点Pが直線DA上にくる時，$\alpha = \pi/6$であることに注意する．線分PO と角 $\theta$ をなす半直線 $l, m$ とする．$\theta$を大きくしていったとき，$l, m$ が正方形ABCDを通る条件は，$\alpha$ によって異なるため，
  \begin{numcases}{}
    0     &\le \alpha \le \pi/6 \label{1991-2:eq:1}\\
    \pi/6 &\le \alpha \le \pi/4 \label{1991-2:eq:2}
  \end{numcases}
  の2つの場合分けで考える．$\eqref{1991-2:eq:1}$ の場合は，$\theta$ が最大となるとき $l, m$ は A または B を通る．したがって，$\min \angle \mathrm{OP}(\alpha)\mathrm{B}$, $\min \angle \mathrm{OP}(\alpha)\mathrm{A}$ のうち，小さい方が最大の $\theta$ を与える．一方で$\eqref{1991-2:eq:2}$ の場合は，$\theta$ が最大となるとき $l, m$ は B または D を通る．したがって，$\min \angle \mathrm{OP}(\alpha)\mathrm{B}$, $\min \angle \mathrm{OP}(\alpha)\mathrm{C}$ のうち，小さい方が最大の $\theta$ を与える．これらの場合をそれぞれ図に示す．

  これらの条件を数式に起こすと
  \begin{numcases}{\max\theta = \\}
    \min \left(\min \angle \mathrm{OPB}, \min \angle \mathrm{OPA}\right) & $\displaystyle 0 \le \alpha \le \frac{\pi}{6}$ \label{1991-2:eq:3}\\
    \min \left(\min \angle \mathrm{OPB}, \min \angle \mathrm{OPD}\right) & $\displaystyle \frac{\pi}{6} \le \alpha \le \frac{\pi}{4}$ \label{1991-2:eq:4}
  \end{numcases}
  となる．この区間では$0\le\theta<\pi/2$であるから，$\theta$の最大値は$\cos\theta$の最小値に対応する．以下では$\cos\theta$の最小値を求める．
  

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1991/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2</figcaption>
</figure>

  まず，$\angle \mathrm{OP}(\alpha)\mathrm{A}$, $\angle \mathrm{OP}(\alpha)\mathrm{B}$, $\angle \mathrm{OP}(\alpha)\mathrm{D}$の表現について考える．対称性から$\angle \mathrm{OP}(\alpha)\mathrm{A}$について考えれば十分である．$\triangle \mathrm{OPA}$に余弦定理を用いると，
  
$$
\begin{align*}
\cos\angle\mathrm{OPA}& = \frac{\mathrm{OP}^2 + \mathrm{PA}^2 - \mathrm{OA}^2}{2 \mathrm{OP} \cdot \mathrm{PA}}\\& = \frac{2 + \mathrm{PA}^2 }{4\mathrm{PA}}\\& = \frac{1}{4}\left(\mathrm{PA} + \frac{2}{\mathrm{PA}}\right)
\end{align*}
$$

  を得る．ここで，PがK上の点であるから$\mathrm{OP} = 2$であること，および$\mathrm{OA}=\sqrt{2}$を利用した．ここで新しく関数$f(x)$を
  
$$
\begin{align*}
f(x) = \frac{1}{4}\left(x + \frac{2}{x}\right)\quad(x > 0)
\end{align*}
$$

  で定義すると，残りの2つの角についても同様に，
  
$$
\begin{align*}
\cos\angle\mathrm{OPA}& = f(\mathrm{PA}) \\\cos\angle\mathrm{OPB}& = f(\mathrm{PB}) \\\cos\angle\mathrm{OPD}& = f(\mathrm{PD})
\end{align*}
$$

  と表せる．$f(x)$の増減と，$\alpha$を動かしたときの各線分の長さの取りうる値から，$\cos\theta$の最小値を求める．

  $f'(x)=(1-2/x^2)/4$から，$f(x)$の増減表およびグラフの概形は図のようになる．

  

<figure id="tab_1" class="table-wrapper">

| $x$  |    $(0)$    |  $\dots$   |  $\sqrt{2}$  |  $\dots$   | $(\infty)$  |
|:------:|:-------------:|:------------:|:--------------:|:------------:|:-------------:|
| $f'$ |               |    $-$     |     $0$      |    $+$     |               |
| $f$  | $(+\infty)$ | $\searrow$ | $\sqrt{2}/2$ | $\nearrow$ | $(+\infty)$ |

  <figcaption>表 1: $f(x)$の増減表</figcaption>
</figure>

  

<figure id="fig_3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1991/2/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $f(x)$の概形</figcaption>
</figure>

  
  (i) $0 \le \alpha \le \pi/6$の場合

  この場合，
  
$$
\begin{align*}
\begin{dcases}
      \mathrm{PA} & \text{単調減少で}\sqrt{2} \ge \mathrm{PA} \ge \sqrt{3}-1 \text{まで動く．}         \\
      \mathrm{PB} & \text{単調増加で}\sqrt{2} \le \mathrm{PB} \le \sqrt{8-2\sqrt{3}} \text{まで動く．}
    \end{dcases}
\end{align*}
$$

  だから，$f(x)$のグラフの増減から，
  
$$
\begin{align*}
\begin{dcases}
      \max \left(\cos \angle \mathrm{APO}\right) = \frac{\sqrt{3}}{2} & \mathrm{PA} = \sqrt{3}-1         \\
      \max \left(\cos \angle \mathrm{BPO}\right) =  \beta             & \mathrm{PB} = \sqrt{8-2\sqrt{3}}
    \end{dcases}
\end{align*}
$$

  となる．ここで$\beta=f(\sqrt{8-2\sqrt{3}})$とおいた．$f(x)$のグラフの概形より$\sqrt{3}/2>\beta$だから，このときの$\max \theta$は$\eqref{1991-2:eq:3}$より$\cos \angle \mathrm{APO} = \frac{\sqrt{3}}{2}$すなわち$\max \theta=\pi/6$である．

  
  (ii) $\pi/6 \le \alpha \le \pi/4$の場合

  この場合，
  
$$
\begin{align*}
\begin{dcases}
      \mathrm{PD} & \text{単調減少で}\sqrt{3}+1 \ge \mathrm{PD} \ge \sqrt{6} \text{まで動く．}         \\
      \mathrm{PB} & \text{単調増加で}\sqrt{8-2\sqrt{3}} \le \mathrm{PB} \le \sqrt{6} \text{まで動く．}
    \end{dcases}
\end{align*}
$$

  だから，$f(x)$のグラフの増減から，
  
$$
\begin{align*}
\begin{dcases}
      \max \left(\cos \angle \mathrm{DPO}\right) = \frac{\sqrt{3}}{2} & \mathrm{PD} = \sqrt{3}+1 \\
      \max \left(\cos \angle \mathrm{BPO}\right) = \frac{\sqrt{6}}{3} & \mathrm{PB} = \sqrt{6}
    \end{dcases}
\end{align*}
$$

  となる．$\sqrt{3}/2>\sqrt{6}{3}$より，したがってこのときの$\max \theta$は$\eqref{1991-2:eq:4}$より$cos \angle \mathrm{DPO} = \frac{\sqrt{3}}{2}$すなわち$\max \theta=\pi/6$である．

  
  以上(i),(ii)から，どちらの場合も$\max \theta = \pi/6$である．したがって，求める最大値は$\displaystyle \max\theta = \frac{\pi}{6}$である．$\cdots$(答)

  
  

## 【解説】

  平面図形の問題．
  「2本の半直線が正方形ABCDを通る」というのをそのまま数式に起こすのは大変だが，最大値や最小値を求めるだけということで極端な場合だけを考えればすむことに気づけるかがポイント．
  また，図形的な図形的な感覚を使えばほとんど計算なしで答えも出せる良問だろう．

  今回の回答では，$\eqref{1991-2:eq:3,1991-2:eq:4}$から$\theta$の最大値を関数$f(x)$を導入してかなり丁寧に求めたが，$\angle \mathrm{APO}$,$\angle \mathrm{BPO}$,$\angle \mathrm{DPO}$が単調に変化することは図から自明としてしまっても良いかもしれない．この場合は後半の解答は細かい数値の比較は除いて以下のように簡略化できる．

  
  (i) $0 \le \alpha \le \pi/6$の場合

  図からこの区間で$\angle \mathrm{OPB}$は$P=(\sqrt{3},1)$で最小値を，$\angle \mathrm{OPA}$は$P=(\sqrt{3},1)$で最小値$\pi/6$を取る．このうち小さいのは後者であり，求める$\max\theta=\pi/6$である．

  
  (ii) $\pi/6 \le \alpha \le \pi/4$の場合

  図からこの区間で$\angle \mathrm{OPB}$は$P=(\sqrt{2},\sqrt{2})$で最小値$\arccos(\sqrt{6}/3)$を，$\angle \mathrm{OPD}$は$P=(\sqrt{3},1)$で最小値$\pi/6$を取る．このうち小さいのは後者であり，求める$\max\theta=\pi/6$である．

  以上(i), (ii)から，いずれの場合も求める最大値は$\max\theta=\pi/6$である．

  結局$\angle \mathrm{APO}$,$\angle \mathrm{BPO}$,$\angle \mathrm{DPO}$のうちで，$\angle \mathrm{BPO}$が最小になることはなく，$\angle \mathrm{APO}$と$\angle \mathrm{DPO}$のみ考えればよい．そして，いずれも許容角度が最小となるのは$P=(\sqrt{3},1)$であり，このときPADは一直線で$\angle \mathrm{APO}=\angle \mathrm{DPO}=\pi/6$だから答え自体はすぐにでるのだが，これはグラフからはそこまではっきりわかることでもないような気もするのである程度丁寧に記述していったほうがよいだろう．

  

<figure id="fig_4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1991/2/fig_4.svg" alt="図 4" />
  <figcaption>図 4: 許容される$\max\theta$が最も小さくなる，$\alpha=\pi/6$，すなわち$P=(\sqrt{3},1)$のときの図形</figcaption>
</figure>