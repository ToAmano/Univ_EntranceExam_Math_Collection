---
university: "titech"
category: "zenki"
year: "1976"
question: "3"
type: "solution"
title: "TITECH 1976 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

対称性から，右図の $\triangle OAB$ 内で $P$ がうごく時のみを考える．この時，$P$ と最近の辺は $AB$ である．$P$ から $AB$ に下ろした垂足を $H$ とし，$O$ を極，$x$軸正方向を始線とする極座標で $P(r,\theta)$ とおく．（$r,\theta\ge0$）題意から，

$$
\begin{align*}
\overline{OP}=\overline{PH}\iff r=\frac{a}{2}-r\cos\theta\iff r=\frac{\frac12 a}{1+\cos\theta}\quad(0\le\theta\le\pi/4) \quad\cdots\text{①}
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1976/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点$P$の軌跡と$\triangle OAB$の関係</figcaption>
</figure>

この時，たしかに $P$ は $\triangle OAB$ 内にある．対称性から，もとめる面積 $S$，$S$ のうち $\triangle OAB$ 内のものを $S'$ として，

$$
\begin{align*}
S=8S' \quad\cdots\text{②}
\end{align*}
$$

であり，

$$
\begin{align*}
S'=\int_0^{\pi/4}\frac{1}{2}r^2d\theta = \frac{1}{2}\cdot\frac{a^2}{4}\int_0^{\pi/4}\frac{1}{(1+\cos\theta)^2}d\theta = \frac{a^2}{8}\int_0^{\pi/4}\frac{1}{4\cos^4\frac\theta2}d\theta
\end{align*}
$$

（以下 $C=\cos\dfrac{\theta}{2},\ t=\tan\dfrac{\theta}{2}$ とする）

$$
\begin{align*}
=\frac{a^2}{32}\int_0^{\pi/4}(1+t^2)\frac{1}{C^2}d\theta = \frac{2a^2}{32}\left[t+\frac13t^3\right]_0^{\pi/4} = \frac{a^2}{16}\left(\tan\frac\pi8+\frac13\tan^3\frac\pi8\right)\quad\cdots\text{③}
\end{align*}
$$

ここで，$p=\tan\dfrac\pi8$ とすると $p>0$ より，

$$
\begin{align*}
\tan\frac\pi4=\frac{2p}{1-p^2}\quad\therefore\ p^2+2p-1=0 \quad\therefore\ p=-1+\sqrt2
\end{align*}
$$

だから，③より

$$
\begin{align*}
S'=\frac{a^2}{16}(-1+\sqrt2)\left(1+\frac13(-1+\sqrt2)^2\right) = \frac{a^2}{16}(-1+\sqrt2)\left(\frac{6-2\sqrt2}{3}\right)
\end{align*}
$$

となって，②に代入して

$$
\begin{align*}
S=\frac{a^2}{2}\cdot\frac23(-1+\sqrt2)(3-\sqrt2) = \frac{a^2}{3}(-5+4\sqrt2)
\end{align*}
$$

\medskip
**[解2]（$\triangle OAB$ 内で考える）**

$P$ の軌跡は，$O$ を焦点，$AB$ を準線とする放物線で，その方程式は $\alpha=\dfrac14 a$ として

$$
\begin{align*}
y^2=-4\alpha\left(x-\frac{a}{4}\right)=-a\left(x-\frac a4\right)
\end{align*}
$$

である．よって右図斜線部の面積 $S'$ は

$$
\begin{align*}
S'=\int_0^{\frac{\sqrt2-1}{2}a}\left(-\frac1ay^2+\frac a4\right)dy-\frac12\left(\frac{\sqrt2-1}{2}a\right)^2
\end{align*}
$$

$$
\begin{align*}
=-\frac1{3a}\left(\frac{\sqrt2-1}{2}a\right)^3+\frac a4\cdot\frac{\sqrt2-1}{2}a-\frac18(3-2\sqrt2)a^2
\end{align*}
$$

と計算され，[解1] と同じく $S=\dfrac{a^2}{3}(-5+4\sqrt2)$ を得る．（原稿はここで途切れている）