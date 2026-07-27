---
university: "titech"
category: "zenki"
year: "1998"
question: "2"
type: "solution"
title: "TITECH 1998 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

長方形$R$の4頂点を，$X(0,a)$，$Y(b,a)$，$Z(b,0)$，$W(0,0)$とする（$XY=b$，$XW=a$，$0<a<b<2a$）．円$A$は性質(P)から2辺$XY,XW$に接するとしてよく，半径を$x$とすると中心は$(x,a-x)$であり，

$$
\begin{align*}
0<x<\frac a2 \quad\cdots\text{(＊)}
\end{align*}
$$

が必要である．

**(1)** 円$A$に外接する性質(P)の円は，対称性から次の4つで尽くされる：頂点$W$で2辺$XW,WZ$に接する円$C_1$（半径$r_1$，中心$(r_1,r_1)$），頂点$Z$で2辺$WZ,ZY$に接する円$C_2$（半径$r_2$，中心$(b-r_2,r_2)$），頂点$Y$で2辺$ZY,YX$に接する円$C_3$（半径$r_3$，中心$(b-r_3,a-r_3)$），そして頂点$X$で円$A$と同じ2辺$XY,XW$に接し，$A$より角$X$寄りにある円$C_4$（半径$r_4$，中心$(r_4,a-r_4)$）．

**$C_1$について：** $A,C_1$が外接する条件から

$$
\begin{align*}
(x-r_1)^2+(a-x-r_1)^2=(x+r_1)^2
\end{align*}
$$

整理すると（$a-x-r_1>0$に注意して）

$$
\begin{align*}
(a-x-r_1)^2=4xr_1 \quad\therefore\ a-x-r_1=2\sqrt{xr_1}
\end{align*}
$$

$$
\begin{align*}
a=x+r_1+2\sqrt{xr_1}=(\sqrt x+\sqrt{r_1})^2 \quad\therefore\ r_1=(\sqrt a-\sqrt x)^2
\end{align*}
$$

**$C_3$について：** 同様に

$$
\begin{align*}
(b-x-r_3)^2+(x-r_3)^2=(x+r_3)^2 \ \Longrightarrow\ b=x+r_3+2\sqrt{xr_3}=(\sqrt x+\sqrt{r_3})^2
\end{align*}
$$

$$
\begin{align*}
\therefore\ r_3=(\sqrt b-\sqrt x)^2
\end{align*}
$$

**$C_2$について：** $A,C_2$が外接する条件から

$$
\begin{align*}
(b-x-r_2)^2+(a-x-r_2)^2=(x+r_2)^2
\end{align*}
$$

展開して整理すると

$$
\begin{align*}
(x+r_2)^2-2(a+b)(x+r_2)+a^2+b^2=0
\end{align*}
$$

$u=x+r_2$とおくと$u^2-2(a+b)u+(a^2+b^2)=0$より

$$
\begin{align*}
u=(a+b)\pm\sqrt{2ab}
\end{align*}
$$

複号のうち$+$は$r_2$が大きくなりすぎ図形的制約に反するので不適，

$$
\begin{align*}
r_2=(a+b)-\sqrt{2ab}-x
\end{align*}
$$

**$C_4$について：** $A,C_4$は同じ角$X$の二等分線上に中心があり，外接条件から中心間距離$\sqrt2(x-r_4)=x+r_4$（$r_4<x$）．よって

$$
\begin{align*}
\sqrt2\,x-\sqrt2\,r_4=x+r_4 \quad\therefore\ r_4=\frac{(\sqrt2-1)x}{\sqrt2+1}=(3-2\sqrt2)x
\end{align*}
$$

$r_1=(\sqrt a-\sqrt x)^2$が意味を持ち，かつ$0<r_1<a/2$をみたすことなどから，$0<r_k<a/2$（$k=1,2,3$）の存在条件を調べればよい．$r_1<a/2$の条件は$\sqrt a-\sqrt x<\sqrt{a/2}$，$r_3<a/2$の条件は$\sqrt b-\sqrt x<\sqrt{a/2}$であり，$b>a$からこちらがより強い条件を与える：

$$
\begin{align*}
\sqrt x>\sqrt b-\sqrt{\frac a2}\quad\therefore\ x>\left(\sqrt b-\sqrt{\frac a2}\right)^2
\end{align*}
$$

（$r_2$を与える$u$の方程式は判別式$(a+b)^2-(a^2+b^2)=2ab>0$から常に解をもち，$r_2$は自動的に存在する．）以上と(＊)をあわせて，もとめる条件は

$$
\begin{align*}
\left(\sqrt b-\sqrt{\frac a2}\right)^2<x<\frac a2
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1998/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円$W$，$X$，$Y$，$Z$の配置</figcaption>
</figure>

**(2)** (1)の条件下で，まず$C_4$の半径$r_4=(3-2\sqrt2)x$は$3-2\sqrt2\approx0.17$と小さいため，常に$r_1$より小さい（実際$r_1=(\sqrt a-\sqrt x)^2$は$x<a/2$の範囲で$r_4$より大きいことが確かめられる）．また

$$
\begin{align*}
r_3-r_2=(b+x-2\sqrt{bx})-\bigl((a+b)-\sqrt{2ab}-x\bigr)=2x-2\sqrt{bx}+\sqrt{2ab}-a
\end{align*}
$$

$$
\begin{align*}
=2\left(\sqrt x-\frac{\sqrt{2a}}2\right)\left(\sqrt x-\frac{2\sqrt b-\sqrt{2a}}2\right)
\end{align*}
$$

(1)の範囲内でこれが負であることが確かめられるので，$r_3<r_2$．以上から4円の半径の大小は

$$
\begin{align*}
r_2>r_3>r_1>r_4
\end{align*}
$$

となり，$A$に外接する4円のうち「2番目に大きい円」$B$は半径$r_3$の$C_3$である．

したがって$A$と$B$の面積の和$S$は

$$
\begin{align*}
S=\pi\left(x^2+r_3^2\right)=\pi\left\{x^2+(\sqrt b-\sqrt x)^4\right\}
\end{align*}
$$

$X=\sqrt x$とおいて微分すると

$$
\begin{align*}
\frac{dS}{dx}=\pi\left\{2x+4(\sqrt x-\sqrt b)^3\cdot\frac1{2\sqrt x}\right\}=\pi\left\{2X^2+\frac{2(X-\sqrt b)^3}{X}\right\}
\end{align*}
$$

$$
\begin{align*}
=\frac{2\pi}{X}\left\{X^3+X^3-3\sqrt bX^2+3bX-b\sqrt b\right\}=\frac{4\pi}{X}\left(X-\frac{\sqrt b}2\right)\left(X^2-\sqrt bX+b\right)
\end{align*}
$$

$$
\begin{align*}
=\frac{4\pi}{X}\left(X-\frac{\sqrt b}2\right)\left\{\left(X-\frac{\sqrt b}2\right)^2+\frac{3b}4\right\}
\end{align*}
$$

$\{\ \cdots\ \}$の中は常に正だから，$dS/dx$の符号は$X-\sqrt b/2$の符号と一致し，(1)の範囲$\sqrt b-\sqrt{a/2}<X<\sqrt{a/2}$の中に$X=\sqrt b/2$が含まれる（$2a>b$より$\sqrt b/2<\sqrt{a/2}$）ので，下表を得る．

| $X$ | $\sqrt b-\sqrt{a/2}$ |  | $\sqrt b/2$ |  | $\sqrt{a/2}$ |
|:--:|:--:|:--:|:--:|:--:|:--:|
| $S'$ |  | $-$ | $0$ | $+$ |  |
| $S$ |  | $\searrow$ |  | $\nearrow$ |  |

よって$X=\sqrt b/2$，すなわち$x=b/4$で$S$は最小となり，この時$r_3=(\sqrt b-\sqrt{b/4})^2=(\sqrt b/2)^2=b/4$だから

$$
\begin{align*}
\min S=\pi\left\{\left(\frac b4\right)^2+\left(\frac b4\right)^2\right\}=\frac{b^2}{8}\pi
\end{align*}
$$