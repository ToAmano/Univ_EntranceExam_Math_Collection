---
university: "kyodai"
category: "kouki"
year: "2006"
question: "4"
type: "solution"
title: "KYODAI 2006 kouki Q4 (solution)"
---

## 【解】

  表記の簡潔さのため，
  $\angle A = \alpha$, $\angle B = \beta$, $\angle C = \gamma$ とおく．
  ただし
  
$$
\begin{align}
\begin{dcases}
      \alpha, \beta, \gamma > 0 \\
      \alpha + \beta + \gamma = \pi
    \end{dcases}\label{2006-4:eq:0}
\end{align}
$$

  である．

  

<figure id="2006-4:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2006/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $\triangle ABC$の様子．</figcaption>
</figure>

  $\triangle ABC$に正弦定理を用いて，外接円の半径$R=1$として
  
$$
\begin{align}
\frac{a}{\sin \alpha} = \frac{b}{\sin \beta} = \frac{c}{\sin \gamma} = 2R = 2 \label{2006-4:eq:1}
\end{align}
$$

  となる．

  以下$\triangle ABC$ の面積$S$を2通りで表す．
  まず$\eqref{006-4:eq:1}$より
  
$$
\begin{align}
S
     & = \frac{1}{2}|AB||AC|\sin\alpha\\& = \frac{1}{2} bc \sin\alpha\\& = \frac{1}{2}(2\sin\beta)(2\sin\gamma) \sin\alpha\\& = 2 \sin\alpha\sin\beta\sin\gamma\label{2006-4:eq:2}
\end{align}
$$

  である．

  次に，内接円の半径 $r$ ，中心Oとおくと
  
$$
\begin{align}
S
     & = \triangle OAB + \triangle OBC + \triangle OCA                             \\& =\frac{1}{2} r \left(2R \sin\alpha + 2R \sin\beta + 2R \sin\gamma\right)\\& =r \left(\sin\alpha + \sin\beta + \sin\gamma\right)\label{2006-4:eq:3}
\end{align}
$$

  である．

  以上$\eqref{2006-4:eq:2,2006-4:eq:3}$から
  
$$
\begin{align}
r = \frac{2 \sin\alpha\sin\beta\sin\gamma}{\sin \alpha + \sin \beta + \sin \gamma}\label{2006-4:eq:4}
\end{align}
$$

  だから，この右辺の最大値が$1/2$以下であることを示せば良い．
  $\eqref{2006-4:eq:0}$を用いて$\gamma$を削除して，
  
$$
\begin{align*}
f(x, y) = \frac{2\sin x \sin y \sin(x+y)}{\sin x + \sin y + \sin(x+y)}
\end{align*}
$$

  とおく．値域は
  
$$
\begin{align}
0 < x, y, x+y < \pi\label{2006-4:eq:5}
\end{align}
$$

  である．倍角公式，および和積公式から
  
$$
\begin{align*}
f(x, y)
     & = 2\frac{2 \sin \frac{x+y}{2} \cos \frac{x+y}{2} \cdot \sin x \sin y}{2 \sin \frac{x+y}{2} \cos \frac{x-y}{2} + 2 \sin \frac{x+y}{2} \cos \frac{x+y}{2}}\\& = 2\frac{\cos \frac{x+y}{2} \cdot \sin x \sin y}{\cos \frac{x-y}{2} + \cos \frac{x+y}{2}}
\end{align*}
$$

  となる．さらに倍角公式，和積公式を用いて
  
$$
\begin{align*}
f(x,y)
     & = 2\frac{\cos \frac{x+y}{2} \cdot 2\sin \frac{x}{2}\cos\frac{x}{2} \cdot 2\sin \frac{y}{2}\cos\frac{y}{2}}{2 \cos \frac{x}{2} \cos \frac{y}{2}}\\& = 4\cos\frac{x+y}{2}\sin\frac{x}{2}\sin\frac{y}{2}
\end{align*}
$$

  さらに積和公式を用いると
  
$$
\begin{align*}
f(x,y)
     & = 2 \sin\frac{x}{2}\left[\sin\left(y+\frac{x}{2}\right)-\sin\frac{x}{2}\right]
\end{align*}
$$

  と変形できる．
  $\eqref{2006-4:eq:5}$から$\sin \frac{x}{2} > 0$だから，
  $x$を固定して$y$を動かした時，
  $f(x, y)$ は
  
$$
\begin{align*}
& \sin\left(y+\frac{x}{2}\right) = 1   \\\therefore& y = \frac{1}{2}\left(\pi - x \right)
\end{align*}
$$

  で最大値を取る．（$\eqref{2006-4:eq:5}$を満たしていることに注意．）
  その最大値$f(x)$とおくと，
  
$$
\begin{align*}
& f(x) \equiv\max f(x, y) = 2\sin\frac{x}{2}\left[1-\sin\frac{x}{2}\right]& 0 < x < \pi\\
\end{align*}
$$

  である．
  次に$x$を動かすと，
  
$$
\begin{align*}
& \sin\frac{x}{2} = \frac{1}{2}\\\therefore& x = \frac{\pi}{3}
\end{align*}
$$

  で最大値
  
$$
\begin{align*}
\max f(x) = f\left(\frac{\pi}{3}\right) = \frac{1}{2}
\end{align*}
$$

  をとる．
  従って$\eqref{2006-4:eq:4}$から
  
$$
\begin{align*}
r \le\frac{1}{2}
\end{align*}
$$

  である．等号成立条件は
  
$$
\begin{align*}
\alpha = \beta = \gamma = \frac{\pi}{3}
\end{align*}
$$

  である．以上から題意は示された．$\cdots$(答)

  
  

## 【解説】

  解答は，もっとも技巧がいらない代わりに計算量が多い方法で解いた．
  この問題はさまざまな解き方があるのでここでいくつか解説して行く．

  おそらく一番簡潔（だが実際の答案では使えない）なのは，初等幾何におけるオイラーの定理（またはオイラーの不等式）を用いると一発で求まる．
  オイラーの定理とは，三角形の内接円の半径を $r$，外接円の半径を $R$ とおくとき，
  外心 $O$ と内心 $I$ との距離 $d$ は以下の式で表される．
  
$$
\begin{align*}
d^2 = R(R-2r)
\end{align*}
$$

  従って，左辺が$0$以上なので$R-2r\ge 0 \iff r \le R/2=1/2$である．

  ここでこのオイラーの定理の証明を与えておこう．

  $(R-d)(R+d) = PI \cdot IQ = AI \cdot IM = AI \cdot BM = DM \cdot NI \cdot 2Rr$
  より示された日
  \textcircled{1} ではなく
  \textcircled{2} は
  $$ \angle BIM = \angle BAI + \angle ABI $$
  $$ = \angle MAC + \angle IBC $$
  $$ = \angle IBM $$
  だから二等辺三角形
  \textcircled{3} は $\triangle ANI \sim \triangle DBM$ (2角相等)
  $\Rightarrow$ これから $R \ge 2r$ は明らか!!

  次に，イェンゼンの不等式を用いた方法を紹介する．
  $\eqref{2006-4:eq:4}$以降，回答では文字消去をして解いていったが，
  当然対称なまま変形していった方が綺麗に変形していける．
  まず，倍角公式より分子は
  
$$
\begin{align*}
\text{分子}& =\sin\alpha\sin\beta\sin\gamma\\& = 8\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}\sin\frac{\beta}{2}\cos\frac{\beta}{2}\sin\frac{\gamma}{2}\cos\frac{\gamma}{2}
\end{align*}
$$

  と変形できる．
  次に分母は和積公式を繰り返し用いて変形する．
  途中で$\alpha+\beta+\gamma=\pi$を利用する．
  
$$
\begin{align*}
\text{分母}& = \sin\alpha + \sin\beta + \sin\gamma\\& = 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2} + 2\sin\frac{\gamma}{2}\cos\frac{\gamma}{2}\\& = 2\sin\frac{\pi-\gamma}{2}\cos\frac{\alpha-\beta}{2} + 2\sin\frac{\gamma}{2}\cos\frac{\gamma}{2}\\& = 2\cos\frac{\gamma}{2}\cos\frac{\alpha-\beta}{2} + 2\sin\frac{\gamma}{2}\cos\frac{\gamma}{2}\\& = 2\cos\frac{\gamma}{2}\left[\cos\frac{\alpha-\beta}{2} + \sin\frac{\gamma}{2}\right]\\& = 2\cos\frac{\gamma}{2}\left[\cos\frac{\alpha-\beta}{2} + \sin\frac{\pi-\alpha-\beta}{2}\right]\\& = 2\cos\frac{\gamma}{2}\left[\cos\frac{\alpha-\beta}{2} + \cos\frac{\alpha+\beta}{2}\right]\\& = 2\cos\frac{\gamma}{2}\cdot 2\cos\frac{\alpha}{2}\cos\frac{\beta}{2}\\& = 4\cos\frac{\alpha}{2}\cos\frac{\beta}{2}\cos\frac{\gamma}{2}
\end{align*}
$$

  となる．従って，
  
$$
\begin{align*}
r = 4R\sin\frac{\alpha}{2}\sin\frac{\beta}{2}\sin\frac{\gamma}{2}
\end{align*}
$$

  となる．各項は正だから，相加相乗平均より
  
$$
\begin{align*}
r \le 4R \left(\frac{\sin\frac{\alpha}{2}+\sin\frac{\beta}{2}+\sin\frac{\gamma}{2}}{3}\right)^3
\end{align*}
$$

  さらに$\sin x$は$0<x<\pi$で上に凸だから，イェンゼンの不等式より
  
$$
\begin{align*}
r
     & \le 4R \left[\sin\left(\frac{\frac{\alpha}{2}+\frac{\beta}{2}+\frac{\gamma}{2}}{3}\right)\right]^3 \\& = 4R\left[\sin\frac{\pi}{6}\right]^3                                                              \\& = \frac{R}{2}\\& = \frac{1}{2}
\end{align*}
$$

  となる．よって示された．
  等号成立は$\alpha=\beta=\gamma=\pi/3$のときである．

  以上の例は，角度を用いて変形していく方法だったが，
  辺の長さ$a,b,c$を用いて変形して行く方法もある．
  $\eqref{2006-4:eq:2,2006-4:eq:3}$を長さを用いて書くと
  
$$
\begin{align*}
S = \frac{abc}{4R} = \frac{1}{2}r(a+b+c)
\end{align*}
$$

  である．さらに，ヘロンの公式から
  
$$
\begin{align*}
S = \frac{1}{4}\sqrt{(a+b+c)(-a+b+c)(a-b+c)(a+b-c)}
\end{align*}
$$

  とも書けることに留意する．
  従って，
  
$$
\begin{align*}
R-2r
     & = \frac{abc}{4S} - \frac{4S}{a+b+c}\\& = \frac{abc(a+b+c) - 16S^2}{4S(a+b+c)}
\end{align*}
$$

  この分子$P$が0以上であることを示す．ヘロンの公式を代入して
  
$$
\begin{align*}
P
     & = abc(a+b+c) - 16S^2                             \\& = abc(a+b+c) - (a+b+c)(a+b-c)(b+c-a)(c+a-b)      \\& = (a+b+c)\left[abc-(a+b-c)(b+c-a)(c+a-b) \right]
\end{align*}
$$

  である．ここで，Ravi変換と呼ばれる変換
  
$$
\begin{align*}
x & = \frac{a+b-c}{2}\\
    y & = \frac{b+c-a}{2}\\
    z & = \frac{c+a-b}{2}
\end{align*}
$$

  を代入する．$a,b,c$が三角形の辺だから$x,y,z>0$である．
  
$$
\begin{align*}
P
     & = (a+b+c)\left[(x+y)(y+z)(z+x) - 8xyz\right]\\& = (a+b+c)\left[(xyz+xyz+x^2y+x^2z+y^2x+y^2z+z^2x+z^2y) - 8xyz\right]
\end{align*}
$$

  ここで，大括弧の中は相加相乗平均より
  
$$
\begin{align*}
& \frac{xyz+xyz+x^2y+x^2z+y^2x+y^2z+z^2x+z^2y}{8}\ge\sqrt[8]{(xyz)^8} = xyz \\\therefore& (xyz+xyz+x^2y+x^2z+y^2x+y^2z+z^2x+z^2y) - 8xyz \ge 0
\end{align*}
$$

  だから，$P\ge 0 \iff R \ge 2r$である．よって題意は示された．