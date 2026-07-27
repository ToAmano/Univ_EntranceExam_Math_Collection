---
university: "titech"
category: "zenki"
year: "1975"
question: "6"
type: "solution"
title: "TITECH 1975 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$F(x)=\dfrac{1}{x}\displaystyle\int_0^x f(t)dt$ の両辺 $x$ で微分して

$$
\begin{align*}
F'(x)=-\frac{1}{x^2}\int_0^x f(t)dt+\frac{f(x)}{x}=\frac{1}{x}(f(x)-F(x)) \quad\cdots\text{①}
\end{align*}
$$

である．ここで，題意から，$0\le t\le x$ の時 $f(x)\ge f(t)$ だから，同区間で積分して

$$
\begin{align*}
xf(x)\ge\int_0^x f(t)dt \quad\cdots\text{②}
\end{align*}
$$

したがって，$0<x$ の時，②の両辺 $x$ で割って，

$$
\begin{align*}
f(x)\ge F(x) \quad\cdots\text{③}
\end{align*}
$$

したがって，①の右辺は0以上だから，$F'(x)\ge0$．つまり $F(x)$ は単調増加．

次に，$y=G(x)=xF(x)$ とおく．

$$
\begin{align*}
G'(x)=f(x)
\end{align*}
$$

だから，$x>0$ の時

$$
\begin{align*}
3F(x)=f(x) \iff 3xF(x)=xf(x) \iff 3G(x)=xG'(x) \quad\cdots\text{④}
\end{align*}
$$

である．

$$
\begin{align*}
3y=x\frac{dy}{dx}\iff\frac{3}{x}dx=\frac{1}{y}dy
\end{align*}
$$

両辺積分して，$C_0,C$ を定数として，

$$
\begin{align*}
3\log x+C_0=\log y \quad\therefore\ y=C\cdot x^3
\end{align*}
$$

とかける．両辺微分して，$y'=f(x)$ より，

$$
\begin{align*}
f(x)=3Cx^2
\end{align*}
$$

$f(1)=1$ から，$C=\dfrac{1}{3}$ となり，$f(x)=x^2$ である．逆にこの時，$F(x)=\dfrac{1}{3}x^2$ となり，

1.  $f(x)$ は連続かつ単調増加

2.  $3F(x)=f(x)$

3.  $f(1)=1$

をみたす．以上から $f(x)=x^2$

\medskip
**[解2]（後半）**

①から $f(x)=xF'(x)+F(x)$ だから，$y=F(x)$ として

$$
\begin{align*}
3F(x)=f(x) \iff 3y=x\frac{dy}{dx}+y \iff\frac{1}{x}dx=\frac{1}{2y}dy
\end{align*}
$$

積分して，

$$
\begin{align*}
y=C\cdot x^2
\end{align*}
$$

とおけるから，$F(1)=1$ から $C=1$ となって，$F(x)=x^2$ である．（以下略）