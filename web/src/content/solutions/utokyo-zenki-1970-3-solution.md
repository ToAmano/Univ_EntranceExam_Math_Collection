---
university: "utokyo"
category: "zenki"
year: "1970"
question: "3"
type: "solution"
title: "UTOKYO 1970 zenki Q3 (solution)"
---

\input{macros}
     \begin{oframed}
     $25\,\ \mathrm{m}$隔てて二地点$P$，$Q$がある．いま$A$，$B$二人がそれぞれ$P$$Q$に立ち，同時に向かい合って走り出す．
     走り出してから$t$秒後の$A$，$B$の速度を，$P$から$Q$に向かう方向を正の向きとしてそれぞれ$u \,\ \mathrm{(m/s)}$，
     $v\,\ \mathrm{(m/s)}$とすれば，$u$は一定で，$v=3t^2/4-3t$である．
     
     このとき，$B$が$Q$に帰るまでに$A$が$B$に出会うかまたは追いつくためには，$u$が少なくともどれほどの大きさでなければ
     ならないか．
     \end{oframed}

## 【解】

$A$$B$の$P$からの距離をそれぞれ$A(t)$，$B(t)$とすると，
     

$$
\begin{align*}
A(t)=\int_0^tudt+A(0)=ut \\
     B(t)=\int_0^tvdt+B(0)=\frac{1}{4}t^3-\frac{3}{2}t^2+25
\end{align*}
$$

である.$B(t)\le25\Longleftrightarrow0\le t\le6$であるから，$A$が$B$に追いつくには，$y=A(t)$と$y=B(t)$が$0<t<6$で少なくとも一回
交わればよい．$y$を消去して
     

$$
\begin{align}
&A(t)=B(t) \nonumber\\\Longleftrightarrow&u=\frac{1}{4}t^2-\frac{3}{2}t+\frac{25}{t}\equiv f(t)\label{1}
\end{align}
$$

である．
      

$$
\begin{align*}
f'(t)=\frac{1}{2}t-\frac{3}{2}-\frac{25}{t^2}=\frac{(t-5)(t^2+2t+10)}{2t^2}
\end{align*}
$$

 
から，下表を得る．
     

$$
\begin{align*}
\begin{array}{|c|c|c|c|c|c|}\hline
          t  & 0 &     & 5     &     &6  \\ \hline
          f' &    & -   & 0     &+    &    \\  \hline
          f  &    &\se&15/4 &\ne &25/6  \\ \hline  
          \end{array}
\end{align*}
$$

よって，$f(t)\to\infty(t\to0)$と合わせて，グラフは下図．
     
     \scalebox{1}{a}
     
従って[1](#1)が$0<t<6$に解を持つ条件は
     

$$
\begin{align*}
\frac{15}{4}\le u
\end{align*}
$$

     
であるから，求める最小値は$15/4 \,\ \mathrm{(m/s)}$である．$\cdots$(答)