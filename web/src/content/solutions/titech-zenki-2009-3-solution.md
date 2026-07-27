---
university: "titech"
category: "zenki"
year: "2009"
question: "3"
type: "solution"
title: "TITECH 2009 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$m,n\in\mathbb N$，$1\le m,n\le2N$（①）とする．$f(x)=x^2-nx+m$とおく．$f(x)=0$が$N$以上の実数解を持つ条件を考える．$f$の軸は$x=\dfrac n2$であり，①より$\dfrac n2\le N$．放物線$y=f(x)$は下に凸で軸が$N$以下にあるから，「$N$以上の実数解を持つ」ことと「$f(N)\le0$」は同値である（軸が$N$以下にある以上，2解がともに$N$以上になることはなく，$f(N)\le0$なら大きい方の解が$N$以上，$f(N)>0$なら実数解があっても両方$N$未満）．よって条件は

$$
\begin{align*}
f(N)=N^2-nN+m\le0\quad\therefore\ m\le Nn-N^2.\tag{②}
\end{align*}
$$

①，②をみたす領域を$nm$平面上に図示すると，直線$m=Nn-N^2$は$n=N$で$m=0$，$n=N+2$で$m=2N$を通る（境界は$m\ge1$の制約により$m=0$は含まれない）．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/2009/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 条件①，②をみたす領域（斜線部，$N\ge3$の場合の概形）</figcaption>
</figure>

$N\ge2$のとき，$n=N+1,\dots,2N$の各列について，

1.  $n=N+1$：$Nn-N^2=N$より，$m=1,\dots,N$の$N$通り．

2.  $n=N+2,\dots,2N$（$N-1$列）：$Nn-N^2\ge2N$となり$m$の上限$2N$が効くので，各列$m=1,\dots,2N$の$2N$通り．

（$n=1,\dots,N$では$Nn-N^2\le0$となり該当する$m\ge1$は存在しない．）よって，もとめる組の総数を$F(N)$とすると

$$
\begin{align*}
F(N)=N+(N-1)\cdot2N=N+2N^2-2N=N(2N-1).
\end{align*}
$$

$N=1$の場合はこの一般論の前提（$N+2\le2N$すなわち$N\ge2$）が成り立たないので直接確認する．$N=1$のとき$2N=2$で，$n=1$では該当する$m$はなく，$n=2$では$Nn-N^2=1$より$m=1$の$1$通り．よって$F(1)=1=1\cdot(2\cdot1-1)$となり，上と同じ式が成り立つ．

以上より，すべての正の整数$N$に対して，求める組$(m,n)$の個数は

$$
\begin{align*}
N(2N-1).
\end{align*}
$$