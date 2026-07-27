---
university: "titech"
category: "zenki"
year: "2005"
question: "4"
type: "solution"
title: "TITECH 2005 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

実数$x,y$が$x^2+y^2\le1$をみたすとする．

**(1)** $s=x+y,\ t=xy$とおく．$x,y$は$z^2-sz+t=0$の2実解だから，判別式条件

$$
\begin{align*}
s^2-4t\ge0
\end{align*}
$$

また$x^2+y^2=s^2-2t\le1$だから

$$
\begin{align*}
s^2-2t\le1 \iff t\ge\frac{s^2-1}2
\end{align*}
$$

2式をまとめて，$(s,t)$の動く範囲は

$$
\begin{align*}
\frac{s^2-1}2\le t\le\frac{s^2}4
\end{align*}
$$

（境界は$t=\frac14s^2$と$t=\frac12(s^2-1)$，交点は$\frac14s^2=\frac12s^2-\frac12\iff s^2=2\iff s=\pm\sqrt2$）．これは$-\sqrt2\le s\le\sqrt2$の範囲の，2つの放物線に挟まれた領域（境界を含む）である．

**(2)** $f(s,t)=t+ms$とおく．(1)から$\dfrac{s^2-1}2\le t\le\dfrac{s^2}4$（$-\sqrt2\le s\le\sqrt2$）．$s$を固定すると，$f$は$t$の増加関数だから

$$
\begin{align*}
\frac{s^2-1}2+ms\le f(s,t)\le\frac{s^2}4+ms
\end{align*}
$$

左辺を$g(s)$，右辺を$h(s)$とおく（$-\sqrt2\le s\le\sqrt2$）．

$$
\begin{align*}
g(s)=\frac12(s^2-1)+ms=\frac12(s+m)^2-\frac12m^2-\frac12
\end{align*}
$$

$$
\begin{align*}
h(s)=\frac14s^2+ms=\frac14(s+2m)^2-m^2
\end{align*}
$$

$m\ge0$に注意する．

**最小値について：** $g$は$s=-m$で最小の下に凸な放物線．

1.  $-\sqrt2\le-m$（$m\le\sqrt2$）の時：頂点が区間内にあり，$\min g=g(-m)=-\dfrac12m^2-\dfrac12$

2.  $-m<-\sqrt2$（$m>\sqrt2$）の時：$g$は区間内で単調増加，$\min g=g(-\sqrt2)=\dfrac12(m-\sqrt2)^2-\dfrac12m^2-\dfrac12=-\sqrt2m+\dfrac12$

**最大値について：** $h$は$s=-2m\le0$で最小をとる下に凸な放物線だから，区間$[-\sqrt2,\sqrt2]$上の最大値は端点でとる．$m\ge0$では頂点$-2m$から遠いのは常に$s=\sqrt2$の側（$|\sqrt2-(-2m)|=\sqrt2+2m\ge|-\sqrt2-(-2m)|=|2m-\sqrt2|$，$m\ge0$で常に成立）だから

$$
\begin{align*}
\max h=h(\sqrt2)=\frac14(\sqrt2+2m)^2-m^2=\sqrt2m+\frac12
\end{align*}
$$

以上をまとめて，もとめる最大値・最小値は

$$
\begin{align*}
\text{最大値}=\sqrt2\,m+\frac12,\qquad\text{最小値}=
\begin{cases}
-\dfrac12m^2-\dfrac12 & (0\le m\le\sqrt2)\\[2mm]
-\sqrt2\,m+\dfrac12 & (m\ge\sqrt2)
\end{cases}
\end{align*}
$$