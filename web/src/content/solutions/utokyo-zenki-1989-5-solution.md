---
university: "utokyo"
category: "zenki"
year: "1989"
question: "5"
type: "solution"
title: "UTOKYO 1989 zenki Q5 (solution)"
---

\input{macros}
     \begin{oframed}
     $f(x)=\pi x^2\sin\pi x^2$とする．$y=f(x)$のグラフの$0\le x\le1$の部分と$x$軸とで囲まれた
     図形を$y$軸のまわりに回転させてできる立体の体積$V$は$V=2\pi\dint{0}{1}xf(x)dx$で与えられる
     ことを示し，この値を求めよ．
     \end{oframed}

## 【解】

 区間内で$f(x)\ge0$に注意する．区間内に$X$，$X+\Delta x$をとり，($\Delta x>0$)
$0\le x\le X$の範囲での回転体の体積を$V(X)$と書く．また，同区間での$f(x)$の最大小
値をそれぞれ$M(X)$，$m(X)$とおくと，
     

$$
\begin{align*}
0\le m(X)\le f(x)\le M(X)
\end{align*}
$$

ゆえ，これを$y$軸の周りに回転させれば，
     

$$
\begin{align*}
P&=\left\{(X+\Delta x)^2-X^2\right\}\\&=2X\Delta x+(\Delta x)^2 \\&=\Delta x(2X+\Delta x) \\
     Q&=2X+\Delta x
\end{align*}
$$

として
     

$$
\begin{align}
\pi Pm(X)\le V(X+\Delta x)-V(X)\le\pi PM(X) \nonumber\\\pi Qm(X)\le\frac{V(X+\Delta x)-V(X)}{\Delta x}\le\pi QM(X) \label{1}
\end{align}
$$

である．ここで$\Delta x\to0$とすれば
     

$$
\begin{align*}
M(X),m(x)\to f(X) \\\frac{V(X+\Delta x)-V(X)}{\Delta x}\to V'(X)
\end{align*}
$$

だから，[1](#1)の両辺は$2\pi Xf(X)$に，真ん中は$V'(X)$に，それぞれ収束する．
挟み撃ちの定理から
     

$$
\begin{align*}
V'(X)=2\pi Xf(X)
\end{align*}
$$

となるので，両辺積分して$V(0)=0$より
     

$$
\begin{align*}
V=2\pi\int_0^1xf(x)dx
\end{align*}
$$

である．$\Box$　　     

次に値を計算する．$t=\pi x^2$とすれば$\dfrac{dt}{dx}=2\pi x$，$t:0\to\pi$だから
     

$$
\begin{align*}
V&=\int_0^\pi t\sin tdt \\&=\left[-t\cos t+\sin t\right]_0^\pi\\&=\pi
\end{align*}
$$

である．$\cdots$(答)