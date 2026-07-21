---
university: "titech"
category: "kouki"
year: "2011"
question: "2"
type: "solution"
title: "TITECH 2011 kouki Q2 (solution)"
---

## 【解】

  先に曲線$C$の概形を求める．
  $0 < \theta < \pi/2$ で $x=\tan\theta$ は非負だから両辺二乗しても同値であって，
  
$$
\begin{align*}
x^2
     & = \frac{1}{\tan^2 \theta}\\& = \frac{1-\cos\theta^2}{\cos\theta^2}\\& = \frac{1}{\cos\theta^2}-1            \\& = y^2-1
\end{align*}
$$

  となり，$C$は双曲線である．
  $0 < \theta < \pi/2$ から, $0 < x, 1 \leq y$ で,
  求める$C$の概形は[図1](#2011-2:fig:1)である．

  

<figure id="2011-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2011/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $C$の概形と点$P$, $Q$の関係</figcaption>
</figure>

### (1)

  $S_1$は$y=\sqrt{x^2+1}$を$0\le x\le t$で積分したものであり，
  
$$
\begin{align*}
S_1
     & = \int_{0}^{t}\sqrt{x^2+1}\, dx                                                \\& = \left[\frac{x}{2}\sqrt{x^2+1} + \frac{1}{2}\log(x+\sqrt{x^2+1})\right]_{0}^{t}\\& = \frac{1}{2}\left[t\sqrt{t^2+1} + \log(t+\sqrt{t^2+1})\right]\\
\end{align*}
$$

  である． $\cdots$(答)

  次に$S_2$は底辺$|OP|=t$，高さ$|PQ|=\sqrt{t^2+1}$の三角形の面積であり，
  
$$
\begin{align*}
S_2 = \frac{1}{2}t\sqrt{t^2+1}
\end{align*}
$$

  である． $\cdots$(答)

### (2)

### (1)
の結果から，与式は
  
$$
\begin{align*}
\frac{S_1 - S_2}{\log t}& = \frac{1}{2}\frac{\log(t+\sqrt{t^2+1})}{\log t}\\& = \frac{1}{2}\frac{\log t + \log(1+\sqrt{1+1/t^2})}{\log t}\\& = \frac{1}{2}\left(1+\frac{\log (1+\sqrt{1+1/t^2})}{\log t}\right)\\& =\to\frac{1}{2}\quad(t \to\infty)
\end{align*}
$$

  となり，求めるべき極限値は$1/2$である． $\cdots$(答)

  
  

## 【解説】

  平面図形の問題．素直に条件を置いていけば良く，計算負荷も軽いので
  かなり簡単な問題だろう．

### (2)
は要するに，$C$の漸近線である$y=x$と曲線$C$に囲まれた部分の面積が
  どのように振る舞うかというのを示す問題である．この様子を[図2](#2011-2:fig:2)に示す．
  この問題から，ここの部分の面積が対数で発散していくということがわかる．

  

<figure id="2011-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2011/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $S_1$と$S_2$の差は塗りつぶされた部分である．</figcaption>
</figure>