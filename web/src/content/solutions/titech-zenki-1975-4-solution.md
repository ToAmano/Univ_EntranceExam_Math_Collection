---
university: "titech"
category: "zenki"
year: "1975"
question: "4"
type: "solution"
title: "TITECH 1975 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

2接点を $P\left(t,\dfrac{1}{t}\right)$，$Q\left(-s,\dfrac{1}{s}\right)$ $(t,s>0)$ とすると，$P,Q$ での接線は $\left(\dfrac{1}{x}\right)'=-\dfrac{1}{x^2}$ から，

$$
\begin{align*}
\ell_P: y=-\frac{1}{t^2}x+\frac{2}{t}, \qquad\ell_Q: y=\frac{1}{s^2}x+\frac{2}{s}
\end{align*}
$$

となり，交点 $R$，$\ell_P$ の $x$ 切片 $T$，$\ell_Q$ の $x$ 切片 $U$ とすると

$$
\begin{align*}
R\left(2\frac{ts(s-t)}{t^2+s^2},2\frac{t+s}{t^2+s^2}\right), \qquad T(2t,0), \qquad U(-2s,0)
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1975/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点$P$，$Q$，$R$，$T$，$U$の位置関係</figcaption>
</figure>

だから，題意の△の面積 $f$ は，$R$ から $x$ 軸への垂足 $H$ として

$$
\begin{align*}
f=\overline{TU}\times\overline{RH}\cdot\frac{1}{2} = \frac{1}{2}(2t+2s)\cdot2\frac{t+s}{t^2+s^2} = 2\frac{(t+s)^2}{t^2+s^2}=2\left(1+\frac{2ts}{t^2+s^2}\right)\quad\cdots\text{①}
\end{align*}
$$

AM-GM から，$t^2+s^2\ge2ts$ $\therefore 1\ge\dfrac{2st}{t^2+s^2}$（$\because t,s>0$）で等号成立は $s=t$ の時．

よって①から，

$$
\begin{align*}
f\le2(1+1)=4
\end{align*}
$$

となる．