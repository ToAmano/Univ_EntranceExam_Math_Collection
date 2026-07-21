---
university: "kyodai"
category: "kouki"
year: "2004"
question: "2"
type: "solution"
title: "KYODAI 2004 kouki Q2 (solution)"
---

## 【解】

  与式の両辺$0$以上なのでを二乗して，
  
$$
\begin{align}
& |\alpha+(it+t+1)|^2 \leq 1                                                                                            \\& |\alpha|^2 + (it+t+1)\overline{\alpha} + (-it+t+1)\alpha + |it+t+1|^2                      \leq 1                     \\& |\alpha|^2 + (\overline{\alpha}-\alpha)it + (\alpha+\overline{\alpha})(t+1) + (t+1)^2+t^2  \leq 1                     \\& 2t^2 + 2t + (\overline{\alpha}-\alpha)it + (\alpha+\overline{\alpha})(t+1)  + |\alpha|^2   \leq 0 \label{2004-2:eq:1}
\end{align}
$$

  である．この不等式を満たすような実数$t$が存在する条件を考える．

  まず，
  
$$
\begin{align*}
\Re(\alpha) & =X \in\mathbb{R}\\\Im(\alpha) & =Y \in\mathbb{R}
\end{align*}
$$

  とおくと
  
$$
\begin{align*}
& \alpha+\overline{\alpha}=2X    \\& i(\overline{\alpha}-\alpha)=2Y \\& |\alpha|^2=X^2+Y^2
\end{align*}
$$

  だから,$\eqref{2004-2:eq:1}$に代入して
  
$$
\begin{align}
2t^2+2(X+Y+1)t + X^2+2X+Y^2 \le 0 \label{2004-2:eq:2}
\end{align}
$$

  なる実数係数の$t$の二次式を得る．
  左辺を $f(t)$ とすると，\label{2004-2:eq:2}を満たす$t \in \mathbb{R}$ の存在条件は
  $f(t)=0$ の判別式 $D$ が0以上であることで，
  
$$
\begin{align*}
& D/4 = (X+Y+1)^2 - 2(X^2+2X+Y^2) \geq 0  \\\therefore& (X-Y+1-\sqrt{2})(X-Y+1+\sqrt{2}) \leq 0
\end{align*}
$$

  である．
  $\alpha=X+Yi$ だから, このような$\alpha$の条件を複素数平面上に図示すると[図1](#2004-2:fig:1)の斜線部 (境界含む)になる．$\cdots$(答)

  

<figure id="2004-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2004/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $\alpha$の領域</figcaption>
</figure>

  
  

## 【解説】

  検算の例として，境界線上の点$\alpha=\sqrt{2}-1$で実際に$t$が存在するかをチェックしてみよう．
  
$$
\begin{align*}
|(1+i)t+\sqrt{2}|^2             & \leq 1 \\
    |it+t+\sqrt{2}|^2               & \leq 1 \\
    t^2 + \left(t+\sqrt{2}\right)^2 & \leq 1 \\
    2t^2 + 2\sqrt{2}t + 1           & \leq 0
\end{align*}
$$

  これはしっかりと実数解が存在するので大丈夫そうである．
  このように，実際に何点か取って検算してみると，答えがもっともらしいかどうかがわかるので
  受験で点を落とさないためには大事な作業である．