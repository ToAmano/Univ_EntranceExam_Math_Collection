---
university: "titech"
category: "zenki"
year: "1992"
question: "4"
type: "solution"
title: "TITECH 1992 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$$
\begin{align*}
f(x)=
\begin{cases}
2x & (0\le x<1/2) \\
2x-1 & (1/2\le x\le1)
\end{cases}
\end{align*}
$$

**(1)** 漸化式から，

$$
\begin{align*}
f_{n+1}(x)=
\begin{cases}
2f_n(x) & (0\le f_n(x)<1/2) \\
2f_n(x)-1 & (1/2\le f_n(x)\le1)
\end{cases}\quad\cdots\text{①}
\end{align*}
$$

となる．$y=f_2(x)$，$y=f_3(x)$のグラフを順に書いて，

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1992/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=f_2(x)$，$y=f_3(x)$のグラフ</figcaption>
</figure>

（$y=f_2(x)$，$y=f_3(x)$）

又，式にして，$k=0,1,\cdots,7$に対し

$$
\begin{align*}
f_3(x)=8x-k \quad\left(\frac{k}{8}\le x<\frac{k+1}{8}\right), \qquad f_3(1)=1
\end{align*}
$$

**(2)** (1)以下同様に，$f_n(x)=2^nx-t\ \left(\dfrac{t}{2^n}\le x<\dfrac{t+1}{2^n}\right)$，$f_n(1)=1$（$t=0,1,\cdots,2^n-1$）であること$\cdots\diamondsuit$を帰納的に示す．$n=\ell\ (\ell\in\mathbb{N})$での$\diamondsuit$の成立を仮定すると，①から，

$$
\begin{align*}
f_{\ell+1}(x)=
\begin{cases}
2(2^\ell x-t) & \left(\dfrac{t}{2^\ell}\le x<\dfrac{t+1/2}{2^\ell}\right) \\
2(2^\ell x-t)-1 & \left(\dfrac{t+1/2}{2^\ell}\le x<\dfrac{t+1}{2^\ell}\right)
\end{cases}
\end{align*}
$$

つまり

$$
\begin{align*}
f_{\ell+1}(x)=
\begin{cases}
2^{\ell+1}x-2t & \left(\dfrac{2t}{2^{\ell+1}}\le x<\dfrac{2t+1}{2^{\ell+1}}\right) \\
2^{\ell+1}x-(2t+1) & \left(\dfrac{2t+1}{2^{\ell+1}}\le x<\dfrac{2t+2}{2^{\ell+1}}\right)
\end{cases}
\end{align*}
$$

だから，$f_{\ell+1}(1)=1$とあわせて，$f_{\ell+1}(x)=2^{\ell+1}x-t'\ \left(\dfrac{t'}{2^{\ell+1}}\le x<\dfrac{t'+1}{2^{\ell+1}}\right)$となり，$n=\ell+1$でも$\diamondsuit$は成立．よって任意の$n\in\mathbb{N}$で$\diamondsuit$は成立．

従って，$1\le\ell\le n$なる自然数$\ell$に対し

$$
\begin{align*}
f_\ell(p)=2^\ell p-t_p \quad(\text{ただし}\ t_p\text{は}\ t_p/2^\ell\le p<(t_p+1)/2^\ell\text{をみたす0以上の整数}) \quad\cdots\text{②}
\end{align*}
$$

と書ける．ところで，$n\to\infty$を考えるので$n$は$m$より大きいとして良く，$m\le n$で考えれば良い．$\cdots$③

$$
\begin{align*}
\frac{t_p}{2^\ell}\le\frac{k}{2^m}<\frac{t_p+1}{2^\ell}\iff k\cdot2^{\ell-m}-1<t_p\le k\cdot2^{\ell-m}\quad\cdots\text{③}
\end{align*}
$$

である．$\ell\ge m$の時，③の両辺は整数（1つ差）で$t_p\in\mathbb{Z}$だから右側の等号が成立し，この時$f_\ell(p)=0$である．したがって，$\ell=1,2,\cdots,m$で和をとれば良い（$\because$③）．

$$
\begin{align*}
\sum_{\ell=1}^nf_\ell(p)=\sum_{\ell=1}^mf_\ell(p)=A \quad(n\text{に関係ない定数})
\end{align*}
$$

だから，

$$
\begin{align*}
(\text{与式})=\frac{A}{n}\xrightarrow{n\to\infty}0
\end{align*}
$$

となる．