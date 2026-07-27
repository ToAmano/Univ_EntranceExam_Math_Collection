---
university: "titech"
category: "zenki"
year: "1984"
question: "5"
type: "solution"
title: "TITECH 1984 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$S=\sin x,\ C=\cos x$と書く．

$$
\begin{align*}
\tan x=\cos x \quad\therefore\ S=C^2=1-S^2 \quad\therefore\ S=\frac12(-1\pm\sqrt5)
\end{align*}
$$

$|S|\le1$から$S=\dfrac{-1+\sqrt5}{2}\equiv S_0$である． $\cdots$①

グラフは下図で，交点$A$の$x$座標を$\alpha$とおく．$(\tan\alpha)'=\dfrac{1}{C^2}$だから，①とあわせて，$\ell$の傾きは

$$
\begin{align*}
\frac{1}{1-S_0^2}=\frac{1}{S_0}=\frac{2}{\sqrt5-1}=\frac{\sqrt5+1}{2}
\end{align*}
$$

であって，$A$から$x$軸に下ろした垂足$B$，$\ell$と$x$軸の交点$C$とすると，もとめる面積$T$として

$$
\begin{align*}
T=\int_0^\alpha\tan x\,dx-\triangle ABC \quad\cdots\text{①}
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1984/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 曲線$y=\tan x$，$y=\cos x$と面積$T$</figcaption>
</figure>

まず，

$$
\begin{align*}
\triangle ABC=\frac12\left(\sqrt{\frac{\sqrt5-1}{2}}\right)^2\cdot\frac{1}{\frac{\sqrt5+1}{2}}=\frac12\cdot\frac{\sqrt5-1}{\sqrt5+1}=\frac12\cdot\frac{(\sqrt5-1)^2}{4}\quad\cdots\text{②}
\end{align*}
$$

さらに

$$
\begin{align*}
\int_0^\alpha\tan x\,dx=\left[-\log(\cos x)\right]_0^\alpha=-\log(\cos\alpha)=-\frac12\log\frac{\sqrt5-1}{2}\quad\cdots\text{③}
\end{align*}
$$

①，②，③から

$$
\begin{align*}
T=-\frac12\log\frac{\sqrt5-1}{2}-\frac18(\sqrt5-1)^2
\end{align*}
$$