---
university: "todai"
category: "kouki"
year: "2000"
question: "2"
type: "solution"
title: "TODAI 2000 kouki Q2 (solution)"
---

## 【解】

  以下$f(x) = x^l \sin nx$ とおく．

  (1)
  $y=f(x)$を$x$軸まわりに回転した立体の体積$V_n$は
  

$$
\begin{align}
V_n
     & = \int_0^{2\pi}\pi f(x)^2 dx                                                 \\& = \pi\int_0^{2\pi} x^{2l}\sin^2 nx \, dx                                    \\& = \frac{\pi}{2}\int_0^{2\pi} x^{2l}(1 - \cos 2nx) \, dx \label{2000-2:eq:1}
\end{align}
$$

  である．各項計算すると，まず
  

$$
\begin{align}
\int_0^{2\pi} x^{2l}\, dx
     & = \left[\frac{x^{2l+1}}{2l+1}\right]_0^{2\pi}\\& = \frac{(2\pi)^{2l+1}}{2l+1}\label{2000-2:eq:2}
\end{align}
$$

  である．次に二項目は部分積分法により
  

$$
\begin{align*}
& \left|\int_0^{2\pi} x^{2l}\cos 2nx \, dx\right|\\& = \left|\frac{1}{2n}\left[ x^{2l}\sin 2nx \right]_0^{2\pi} - \frac{2l}{2n}\int_0^{2\pi} x^{2l-1}\sin 2nx \, dx\right|\\& = \left| - \frac{l}{n}\int_0^{2\pi} x^{2l-1}\sin 2nx \, dx  \right|\\& \le\frac{l}{n}\left|\int_0^{2\pi} x^{2l-1}\, dx \right|\\& =  \frac{l}{n}\frac{(2\pi)^{2l}}{2l}\\& \xrightarrow{n \to \infty} 0
\end{align*}
$$

  だから，挟み撃ちの定理より
  

$$
\begin{align}
\lim_{n\to\infty}\int_0^{2\pi} x^{2l}\cos 2nx \, dx = 0 \label{2000-2:eq:3}
\end{align}
$$

  である．
  [(式2)](#2000-2:eq:2,2000-2:eq:2)を[(式1)](#2000-2:eq:1)に代入して
  

$$
\begin{align*}
\lim_{n\to\infty}V_n
     & = \frac{\pi}{2}\frac{(2\pi)^{2l+1}}{2l+1}\\
\end{align*}
$$

  が求める極限値である．$\cdots$(答)
  

  (2)

  $C$の $x \sim x+\Delta x$ を $y$ 軸まわりに回転した体積は，$\Delta x$ が十分小さい時
  高さ $f(x)$，幅 $\Delta x$，長さ $2\pi x$ の直方体で近似できるので（バームクーヘン公式）
  

$$
\begin{align}
W_n
     & = \int_0^{2\pi} 2\pi x |f(x)| \, dx                               \\& = 2\pi\int_0^{2\pi} x^{2l+1} |\sin nx| \, dx \label{2000-2:eq:4}
\end{align}
$$

  と表せる．
  ここで
  

$$
\begin{align*}
A_k = \int_{\frac{k-1}{n}\pi}^{\frac{k}{n}\pi} x^{2l+1} |\sin nx| \, dx
\end{align*}
$$

  とおくと，
  [(式4)](#2000-2:eq:4)から
  

$$
\begin{align}
\bar{W}_n = 2\pi\sum_{k=1}^{2n} A_k \label{2000-2:eq:5}
\end{align}
$$

  である．
  $\left[ \frac{k-1}{n}\pi, \frac{k}{n}\pi \right]$ で $g(x) = x^{2l+1}$ の最大，最小を与える $x$ を各々 $M_k, m_k$
  とすると，$|\sin nx| \ge 0$ から
  

$$
\begin{align}
g(m_k) \int_{\frac{k-1}{n}\pi}^{\frac{k}{n}\pi} |\sin nx| \, dx \le A_k \le g(M_k) \int_{\frac{k-1}{n}\pi}^{\frac{k}{n}\pi} |\sin nx| \, dx \label{2000-2:eq:6}
\end{align}
$$

  である．
  両辺の積分は$t = x - \frac{k-1}{n}\pi$ と置換して
  

$$
\begin{align*}
\int_{\frac{k-1}{n}\pi}^{\frac{k}{n}\pi} |\sin nx| \, dx
     & = \int_0^{\frac{\pi}{n}} |\sin n(t + \frac{k-1}{n}\pi)| \, dt \\& = \int_0^{\frac{\pi}{n}} |\sin(nt + (k-1)\pi)| \, dt         \\& = \int_0^{\frac{\pi}{n}}\sin nt \, dt                        \\& = \left[ -\frac{1}{n}\cos nt \right]_0^{\frac{\pi}{n}}\\& =  \frac{2}{n}
\end{align*}
$$

  と評価できるから，[(式6)](#2000-2:eq:6) に代入して
  

$$
\begin{align*}
\frac{2}{n} g(m_k) \le A_k \le\frac{2}{n} g(M_k)
\end{align*}
$$

  となる．これを $k=1, 2, \dots, 2n$ について和を取って[(式5)](#2000-2:eq:5)より，
  

$$
\begin{align}
\frac{2}{n}\sum_{k=1}^{2n} g(m_k) \le\frac{W_n}{2\pi}\le\frac{2}{n}\sum_{k=1}^{2n} g(M_k)\label{2000-2:eq:7}
\end{align}
$$

  となる．両辺の$n\to\infty$での極限値は，区分求積法より
  

$$
\begin{align*}
\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{2n} g(M_k)
     & = \frac{1}{\pi}\int_0^{2\pi} g(x) \, dx   \\& = \frac{1}{\pi}\frac{(2\pi)^{l+2}}{l+2}\\\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{2n} g(m_k)
     & \to\frac{1}{\pi}\int_0^{2\pi} g(x) \, dx \\& = \frac{1}{\pi}\frac{(2\pi)^{l+2}}{l+2}
\end{align*}
$$

  と同じ値に収束するから，
  だから [(式7)](#2000-2:eq:7) 及びはさみうちの定理から
  

$$
\begin{align*}
\lim_{n\to\infty} W_n
     & = 2\pi\cdot\frac{2}{\pi}\frac{(2\pi)^{l+2}}{l+2}\\& = \frac{4}{l+2}(2\pi)^{l+2}
\end{align*}
$$

  が求める極限値である．$\cdots$(答)
  

  

## 【解説】