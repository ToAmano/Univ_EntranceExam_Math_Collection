---
university: "titech"
category: "zenki"
year: "1987"
question: "4"
type: "solution"
title: "TITECH 1987 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$x(t)=t+e^{at},\ y(t)=-t+e^{at}$とおく．又，$p=e^t$とする．

$$
\begin{align*}
x'(t)=1+ap^a, \qquad y'(t)=-1+ap^a \quad\cdots\text{①}
\end{align*}
$$

$a>0$から，$x'(t)>0$だから

$$
\begin{align*}
\frac{dy}{dx}=\frac{y'(t)}{x'(t)}=\frac{-1+ap^a}{1+ap^a}\quad\cdots\text{②}
\end{align*}
$$

題意から，$y(t)=0$の時，$dy/dx=0$なる$t$がある．$dy/dx=0\iff a\cdot p^a=1$（$\because②$）で，これをといて，（$a>0$）

$$
\begin{align*}
t=-\frac1a\log a
\end{align*}
$$

この時$y(t)=0$となるから，

$$
\begin{align*}
\frac1a\log a+\frac1a=0 \quad\therefore\ a=\frac1e\ (>0)
\end{align*}
$$

**(2)** ②及び(1)の結果から下表をうる．

|   $t$   |              |       |   $e$    |       |              |
|:---------:|:------------:|:-----:|:----------:|:-----:|:------------:|
|  $x'$   |    $+$     | $+$ |   $+$    |       |              |
|  $y'$   |              | $-$ |   $0$    | $+$ |              |
| $(x,y)$ | $\searrow$ |       | $(2e,0)$ |       | $\nearrow$ |

$t\to+\infty$の時，$x(t),y(t)\to+\infty$．$t\to-\infty$の時，$x(t)\to-\infty,\ y(t)\to+\infty$．

$$
\begin{align*}
x(t)\le y(t)\iff t+e^{t/e}\le-t+e^{t/e}\iff t\le0 \quad(x(0)=1,\ y(0)=1)
\end{align*}
$$

とあわせて，グラフの概形は下図でもとめる面積$S$は下図斜線部．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1987/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 曲線$C$の概形と面積$S$</figcaption>
</figure>

$$
\begin{align*}
S=\triangle+\int_1^{2e}y(t)dx=\frac12+\int_1^{2e}y(t)dx=\frac12+\int_0^ey(t)\frac{dx}{dt}dt \quad\cdots\text{③}
\end{align*}
$$

ここで，

$$
\begin{align*}
y(t)\frac{dx}{dt}=\left(-t+e^{\frac{t}{e}}\right)\left(1+\frac1ee^{\frac{t}{e}}\right)=\frac1ee^{\frac2et}+\left(1-\frac{t}{e}\right)e^{\frac{t}{e}}-t \quad\cdots\text{④}
\end{align*}
$$

であり，各項計算して，

$$
\begin{align*}
\int_0^e\frac1ee^{\frac2et}dt=\frac12\left[e^{\frac2et}\right]_0^e=\frac12(e^2-1)
\end{align*}
$$

$$
\begin{align*}
\int_0^e\left(1-\frac{t}{e}\right)e^{\frac{t}{e}}dt=e\int_0^1(1-x)e^xdx=e^2-2e
\end{align*}
$$

$$
\begin{align*}
\int_0^et\,dt=\frac12e^2
\end{align*}
$$

だから④に代入して，

$$
\begin{align*}
④=\frac12(e^2-1)+e^2-2e-\frac12e^2=e^2-2e-\frac12
\end{align*}
$$

だから，③から

$$
\begin{align*}
S=e(e-2)
\end{align*}
$$