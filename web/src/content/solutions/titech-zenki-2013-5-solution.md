---
university: "titech"
category: "zenki"
year: "2013"
question: "5"
type: "solution"
title: "TITECH 2013 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$C=\cos\chi$，$S=\sin\chi$とし，$C_2$上の点$P(C,bS)$（$0\le C\le1$）とおく．また$A(a,0)$（$C_1$の中心）とする．

**(1)** $C_1$が$C_2$に内接する条件は

$$
\begin{align*}
\min_P\overline{AP}=(C_1\text{の半径})=a\tag{①}
\end{align*}
$$

である．

$$
\begin{align*}
\overline{AP}^2=(C-a)^2+b^2S^2=(C-a)^2+b^2(1-C^2)=(1-b^2)C^2-2aC+(a^2+b^2)\equiv f(C)
\end{align*}
$$

とおく（$0\le C\le1$で考えればよい：$a>0$より対称性から接点は$x\ge0$側）．$f'(C)=2(1-b^2)C-2a$であり，$f'(0)=-2a<0$．$f'(1)=2(1-a-b^2)$の正負で場合分けする．

$1^\circ$ $f'(1)\le0\iff1\le a+b^2$のとき：$f'(C)$は$C$の1次式で両端が非正だから区間内で$f'(C)\le0$，すなわち$f$は単調減少で

$$
\begin{align*}
\min f(C)=f(1)=(1-b^2)-2a+(a^2+b^2)=(1-a)^2.
\end{align*}
$$

$2^\circ$ $f'(1)\ge0\iff1\ge a+b^2$のとき：このとき$1-b^2\ge a>0$だから，$f(C)$は下に凸な$C$の2次関数で，$C=\dfrac a{1-b^2}\in(0,1]$で最小となり

$$
\begin{align*}
\min f(C)=f\Bigl(\frac a{1-b^2}\Bigr)=\frac{a^2}{1-b^2}-\frac{2a^2}{1-b^2}+(a^2+b^2)=(a^2+b^2)-\frac{a^2}{1-b^2}.
\end{align*}
$$

①（$\min f(C)=a^2$）より，$1^\circ$では$(1-a)^2=a^2$，すなわち$a=\dfrac12$，$2^\circ$では$(a^2+b^2)-\dfrac{a^2}{1-b^2}=a^2$，整理して$b^2(1-b^2)=a^2$．これらはいずれも$C_1$が$C_2$の内側にあり接することに対応し，まとめると条件は

$$
\begin{align*}
a=\frac12\ \text{かつ}\ \frac12\le b^2\quad(\text{接点}(1,0))\qquad\text{または}\qquad b^2\le\frac12\ \text{かつ}\ a^2=b^2(1-b^2)\quad\Bigl(\text{接点は}C=\frac a{1-b^2}\text{となる点}\Bigr).
\end{align*}
$$

**(2)** $b=\dfrac1{\sqrt3}$のとき$b^2=\dfrac13\le\dfrac12$だから後者の場合に該当し，

$$
\begin{align*}
a^2=b^2(1-b^2)=\frac13\cdot\frac23=\frac29\quad\therefore\ a=\frac{\sqrt2}3.
\end{align*}
$$

接点の$x$座標は

$$
\begin{align*}
p=\frac a{1-b^2}=\frac{\sqrt2/3}{2/3}=\frac{\sqrt2}2
\end{align*}
$$

であり，$q=b\sqrt{1-p^2}=\dfrac1{\sqrt3}\sqrt{1-\dfrac12}=\dfrac1{\sqrt3}\cdot\dfrac1{\sqrt2}=\dfrac1{\sqrt6}=\dfrac{\sqrt6}6$（第1象限より$q>0$）．よって

$$
\begin{align*}
(p,q)=\Bigl(\frac{\sqrt2}2,\ \frac{\sqrt6}6\Bigr).
\end{align*}
$$

**(3)** $x\ge p$の範囲で$C_1$と$C_2$に囲まれた部分の面積を$T$とする．$y$軸に関する対称性（$x\ge p>0$の範囲は上下対称）から，上半分（$y\ge0$）の面積を$T'$として$T=2T'$．

$C_2$の上半分は$y=b\sqrt{1-x^2}$（$p\le x\le1$），$C_1$の上半分は$y=\sqrt{a^2-(x-a)^2}$（$p\le x\le2a$，$C_1$は$x\le2a$までしか存在しない）．よって

$$
\begin{align*}
T'=\int_p^1b\sqrt{1-x^2}\,dx-\int_p^{2a}\sqrt{a^2-(x-a)^2}\,dx.
\end{align*}
$$

第1項：$\displaystyle\int\sqrt{1-x^2}dx=\frac12\bigl[x\sqrt{1-x^2}+\arcsin x\bigr]$を用いて，$x=1$で$\dfrac12\cdot\dfrac\pi2=\dfrac\pi4$，$x=p=\frac{\sqrt2}2$で$\sqrt{1-p^2}=\frac{\sqrt2}2$だから$\dfrac12\bigl[\dfrac{\sqrt2}2\cdot\dfrac{\sqrt2}2+\dfrac\pi4\bigr]=\dfrac12\bigl[\dfrac12+\dfrac\pi4\bigr]=\dfrac14+\dfrac\pi8$．よって

$$
\begin{align*}
\int_p^1\sqrt{1-x^2}dx=\frac\pi4-\Bigl(\frac14+\frac\pi8\Bigr)=\frac\pi8-\frac14,\qquad
b\int_p^1\sqrt{1-x^2}dx=\frac1{\sqrt3}\Bigl(\frac\pi8-\frac14\Bigr)=\frac{\sqrt3}{24}\pi-\frac{\sqrt3}{12}.
\end{align*}
$$

第2項：$u=x-a$と置換すると，$x=p$で$u=p-a=\frac{\sqrt2}2-\frac{\sqrt2}3=\frac{\sqrt2}6$，$x=2a$で$u=a$．$\displaystyle\int\sqrt{a^2-u^2}du=\frac12\bigl[u\sqrt{a^2-u^2}+a^2\arcsin\frac ua\bigr]$を用いる．$u=a$で$\dfrac12\cdot a^2\cdot\dfrac\pi2=\dfrac{a^2\pi}4$．$u=\frac{\sqrt2}6$のとき，$\sqrt{a^2-u^2}=q=\frac{\sqrt6}6$（接点の$y$座標）であり，$\dfrac ua=\dfrac{\sqrt2/6}{\sqrt2/3}=\dfrac12$より$\arcsin\dfrac12=\dfrac\pi6$だから

$$
\begin{align*}
\frac12\Bigl[\frac{\sqrt2}6\cdot\frac{\sqrt6}6+a^2\cdot\frac\pi6\Bigr]=\frac12\Bigl[\frac{\sqrt{12}}{36}+\frac29\cdot\frac\pi6\Bigr]=\frac12\Bigl[\frac{\sqrt3}{18}+\frac\pi{27}\Bigr]=\frac{\sqrt3}{36}+\frac\pi{54}.
\end{align*}
$$

よって

$$
\begin{align*}
\int_p^{2a}\sqrt{a^2-(x-a)^2}dx=\frac{a^2\pi}4-\Bigl(\frac{\sqrt3}{36}+\frac\pi{54}\Bigr)=\frac29\cdot\frac\pi4-\frac{\sqrt3}{36}-\frac\pi{54}=\frac\pi{18}-\frac{\sqrt3}{36}-\frac\pi{54}=\frac\pi{27}-\frac{\sqrt3}{36}
\end{align*}
$$

（$\pi/18-\pi/54=3\pi/54-\pi/54=2\pi/54=\pi/27$を用いた）．以上より

$$
\begin{align*}
T'=\Bigl(\frac{\sqrt3}{24}\pi-\frac{\sqrt3}{12}\Bigr)-\Bigl(\frac\pi{27}-\frac{\sqrt3}{36}\Bigr)=\frac{\sqrt3}{24}\pi-\frac{\sqrt3}{12}+\frac{\sqrt3}{36}-\frac\pi{27}=\Bigl(\frac\pi{24}-\frac1{18}\Bigr)\sqrt3-\frac\pi{27}
\end{align*}
$$

（$-\sqrt3/12+\sqrt3/36=-3\sqrt3/36+\sqrt3/36=-2\sqrt3/36=-\sqrt3/18$を用いた）．よって

$$
\begin{align*}
T=2T'=\Bigl(\frac\pi{12}-\frac19\Bigr)\sqrt3-\frac{2\pi}{27}.
\end{align*}
$$