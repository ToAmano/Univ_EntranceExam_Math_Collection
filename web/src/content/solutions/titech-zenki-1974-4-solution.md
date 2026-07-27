---
university: "titech"
category: "zenki"
year: "1974"
question: "4"
type: "solution"
title: "TITECH 1974 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

対称性から，立体のうち $y\ge0$ の部分の体積 $V_1$，もとめる体積 $V_2$ として，

$$
\begin{align*}
V_2=2V_1 \quad\cdots\text{①}
\end{align*}
$$

である．接線は $y$ 軸平行でないので，$m$ を傾きとして

$$
\begin{align*}
\ell: y=m(x-2a)
\end{align*}
$$

とおける．これが楕円と接するので，$X=x/a,\ Y=y/b$ とおき直した座標で，

$$
\begin{align*}
bY=m(aX-2a)
\end{align*}
$$

と $X^2+Y^2=1$ が接する．したがって

$$
\begin{align*}
\frac{|2am|}{\sqrt{(am)^2+b^2}}=1
\end{align*}
$$

各辺0以上から2乗して，

$$
\begin{align*}
4a^2m^2=a^2m^2+b^2 \quad\therefore\ m=\pm\frac{\sqrt3}{3}\frac{b}{a}
\end{align*}
$$

図の接線の傾きは負だから，$a,b>0$ より複号負をとって，

$$
\begin{align*}
\ell: y=-\frac{\sqrt3}{3}\frac{b}{a}(x-2a)
\end{align*}
$$

である．この時接点 $P\left(\dfrac{a}{2},\dfrac{\sqrt3}{2}b\right)$ となる．したがって，

$$
\begin{align*}
V_1 = (\text{円錐部分}) - (\text{楕円部分}) \quad\cdots\text{②}
\end{align*}
$$

において，

$$
\begin{align*}
(\text{円錐部分}) = \frac{1}{3}\pi(2a)^2\frac{2\sqrt3}{3}b-\frac{1}{3}\pi\left(\frac{1}{2}a\right)^2\left(\frac{2\sqrt3}{3}b-\frac{\sqrt3}{2}b\right)
= \frac{1}{3}\pi\left[\frac{8\sqrt3}{3}a^2b-\frac{\sqrt3}{24}a^2b\right] = \frac{7\sqrt3}{8}\pi a^2b
\end{align*}
$$

$$
\begin{align*}
(\text{楕円部分}) = \pi\int_0^{\frac{\sqrt3}{2}b}a^2\left(1-\frac{y^2}{b^2}\right)dy=a^2\pi\left[y-\frac{1}{3b^2}y^3\right]_0^{\frac{\sqrt3}{2}b}=\frac{3\sqrt3}{8}\pi a^2b
\end{align*}
$$

を②に代入して

$$
\begin{align*}
V_1=\frac{7-3}{8}\sqrt3\pi a^2b=\frac{\sqrt3}{2}\pi a^2b
\end{align*}
$$

①から

$$
\begin{align*}
V_2=\sqrt3\pi a^2b
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1974/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 回転体の体積$V_1$，$V_2$を求めるための図</figcaption>
</figure>