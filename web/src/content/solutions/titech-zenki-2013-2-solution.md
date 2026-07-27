---
university: "titech"
category: "zenki"
year: "2013"
question: "2"
type: "solution"
title: "TITECH 2013 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

（原稿の解答は「[解]」のみで中断していたため，以下は独立に与える完全な解答である．）

**(1)** $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$，$B=\begin{pmatrix}e&f\\g&h\end{pmatrix}$とすると

$$
\begin{align*}
AB=\begin{pmatrix}ae+bg&af+bh\\ce+dg&cf+dh\end{pmatrix}
\end{align*}
$$

より

$$
\begin{align*}
\Delta(AB)&=(ae+bg)(cf+dh)-(af+bh)(ce+dg)\\&=acef+adeh+bcfg+bdgh-acef-adfg-bceh-bdgh\\&=ad(eh-fg)-bc(eh-fg)=(ad-bc)(eh-fg)=\Delta(A)\Delta(B).
\end{align*}
$$

**(2)** $x=\Delta(A)$，$y=t(A)$とする．ケイリー・ハミルトンの定理より

$$
\begin{align*}
A^2=yA-xE.\tag{①}
\end{align*}
$$

(1)より$\Delta(A^5)=\Delta(A)^5=x^5$．一方$A^5=E$より$\Delta(A^5)=\Delta(E)=1$だから$x^5=1$．$x$は実数だから

$$
\begin{align*}
x=1.
\end{align*}
$$

①は$A^2=yA-E$となる．この漸化式を用いて$A^3,A^4,A^5$を$A,E$で表すと

$$
\begin{align*}
A^3&=A\cdot A^2=y A^2-A=(y^2-1)A-yE,\\
A^4&=A\cdot A^3=(y^2-1)A^2-yA=(y^3-2y)A-(y^2-1)E,\\
A^5&=A\cdot A^4=(y^3-2y)A^2-(y^2-1)A=(y^4-3y^2+1)A-(y^3-2y)E.
\end{align*}
$$

$A^5=E$より

$$
\begin{align*}
(y^4-3y^2+1)A-(y^3-2y+1)E=O.\tag{②}
\end{align*}
$$

$A$がスカラー行列（$A=cE$，$c$は実数）の場合，$A^5=c^5E=E$より$c^5=1$，$c$は実数だから$c=1$，すなわち$A=E$．このとき$y=t(E)=2$（$x=\Delta(E)=1$と合わせて，これは1つの解である）．

$A$がスカラー行列でない場合，$A,E$は1次独立だから，②より

$$
\begin{align*}
y^4-3y^2+1=0,\qquad y^3-2y+1=0
\end{align*}
$$

が同時に成り立つ必要がある．$y^3-2y+1=(y-1)(y^2+y-1)$と因数分解でき，$y=1$または$y^2+y-1=0$．$y=1$を$y^4-3y^2+1$に代入すると$1-3+1=-1\neq0$となり不適．$y^2+y-1=0$（$y^2=1-y$）のとき，$y^4=(1-y)^2=1-2y+y^2=1-2y+(1-y)=2-3y$なので

$$
\begin{align*}
y^4-3y^2+1=(2-3y)-3(1-y)+1=2-3y-3+3y+1=0
\end{align*}
$$

となり成立する．よって$y^2+y-1=0$の2解

$$
\begin{align*}
y=\frac{-1\pm\sqrt5}2
\end{align*}
$$

が非スカラーの場合の解である（これらは$A$の固有値が$1$の原始$5$乗根の共役対$e^{\pm2\pi i/5}$，$e^{\pm4\pi i/5}$となる場合に対応し，$t(A)=2\cos\frac{2\pi}5=\frac{-1+\sqrt5}2$，$2\cos\frac{4\pi}5=\frac{-1-\sqrt5}2$として実際に実現される）．

以上より，$x=\Delta(A)=1$は常に成り立ち，

$$
\begin{align*}
y=t(A)=2,\ \frac{-1+\sqrt5}2,\ \frac{-1-\sqrt5}2
\end{align*}
$$

のいずれかである．