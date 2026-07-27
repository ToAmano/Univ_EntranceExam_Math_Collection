---
university: "titech"
category: "zenki"
year: "1981"
question: "4"
type: "solution"
title: "TITECH 1981 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

1.  $t\to0$の時を考えるので，$|\cos2x|=\cos2x$として考えて良い．この時，平均値の定理から，
  

$$
\begin{align*}
F(t)=\frac{\int_0^{\frac{\pi}{2}t}\cos2x\,dx}{t}=\frac{\pi}{2}\cos2p \quad\left(0<p<\frac{\pi}{2}t\right)
\end{align*}
$$

  をみたす$p$がある．はさみうちから$t\to0$の時$p\to0$で，$\cos2x$は連続だから，
  

$$
\begin{align*}
F(t)\longrightarrow\frac{\pi}{2}\cos(2\cdot0)=\frac{\pi}{2}\quad(t\to0)
\end{align*}
$$

2.  
$$
\begin{align*}
F(t)=
  \begin{cases}
  \dfrac1t\displaystyle\int_0^{\frac{\pi}{2}t}\cos2x\,dx & \left(0<t\le\dfrac12\right) \\[2mm]
  \dfrac1t\left\{\displaystyle\int_0^{\frac{\pi}{4}}\cos2x\,dx-\int_{\frac{\pi}{4}}^{\frac{\pi}{2}t}\cos2x\,dx\right\} & \left(\dfrac12\le t\le1\right)
  \end{cases}
\end{align*}
$$

  

$$
\begin{align*}
=
  \begin{cases}
  \dfrac{1}{2t}\sin\pi t & \left(0<t\le\dfrac12\right) \\[2mm]
  \dfrac{1}{2t}(2-\sin\pi t) & \left(\dfrac12\le t\le1\right)
  \end{cases}
\end{align*}
$$

  したがって，前者は$(0,0)$と$\left(t,\dfrac12\sin\pi t\right)$を結ぶ直線の傾き，後者は$(0,0)$と$\left(t,1-\dfrac12\sin\pi t\right)$を結ぶ直線の傾きを表すことから，右図とあわせて，$y=F(t)$のグラフの概形は下図．

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1981/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=F(t)$のグラフの概形</figcaption>
</figure>

  したがって，$F(t)\ge1$となる$t$の範囲は，
  

$$
\begin{align*}
0<t\le\frac12,\quad t=1
\end{align*}
$$

\bigskip
**[解2]**

## 【解】

$(2)$\quad $g(t)=\displaystyle\int_0^{\frac{\pi}{2}t}|\cos2x|dx$ のグラフは，$\left(\dfrac12,g\left(\dfrac12\right)\right)$を軸に対称である．$0<t\le\dfrac12$の時，

$$
\begin{align*}
g(t)=\frac12\sin\pi t
\end{align*}
$$

であって，$y=g(t)$のグラフは右下のようになる．$F(t)$は$(0,0)$と$(t,g(t))$の傾きだから，

$$
\begin{align*}
0<t\le\frac12 \ \text{または}\ t=1
\end{align*}
$$