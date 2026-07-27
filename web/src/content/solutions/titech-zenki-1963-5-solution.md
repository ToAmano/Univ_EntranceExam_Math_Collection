---
university: "titech"
category: "zenki"
year: "1963"
question: "5"
type: "solution"
title: "TITECH 1963 zenki Q5 (solution)"
---

## 【解】

題意より

$$
\begin{align}
a > 0 \label{eq:1}
\end{align}
$$

とする．題意の二つの放物線を

$$
\begin{align}
\begin{cases}
C_1 : y = x^2 \\
C_2 : x = \frac{1}{6}a^2 y^2 - \frac{7}{6}ay \equiv f(y)
\end{cases}
\end{align}
$$

とおく．$C_2$を平方完成すると

$$
\begin{align}
f(y) = \frac{1}{6}a^2 \left( y - \frac{7}{2a^2}\right)^2 - \frac{49}{24a^2}
\end{align}
$$

である．

まずは二つの放物線の交点の$x$座標を求める．$C_1, C_2$から$y$を消去して

$$
\begin{align}
& 6x = a^2 x^4 - 7ax^2 \\& x(a^2 x^3 - 7ax - 6) = 0 \\& x(ax + 1)((ax)^2 - (ax) - 6) = 0 \\& x(ax + 1)(ax - 3)(ax + 2) = 0 \\\therefore& x = 0, \, -\frac{1}{a}, \, -\frac{2}{a}, \,\frac{3}{a}
\end{align}
$$

となる．
よってグラフの概形は下図のようになる．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1963/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>

二つの放物線の囲む二つの部分の面積を図のように$S_1, S_2$とおく．
$S_2$は二辺の長さが$\dfrac{1}{a^2}, \dfrac{1}{a}$の長方形の面積から$C_1, C_2$の作る二つの部分の面積を減じたもので，

$$
\begin{align}
S_2 = 
\begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
  \draw (0,0) rectangle (1,0.7);
\end{tikzpicture}
-
\begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
  \draw (0,0) -- (1,0) -- (1,0.7);
  \draw (0,0) parabola (1,0.7);
\end{tikzpicture}
-
\begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
  \draw (0,0) -- (0,0.7) -- (1,0.7);
  \draw (0,0) parabola (1,0.7);
\end{tikzpicture}\label{eq:2}
\end{align}
$$

となる．各項を計算すると

$$
\begin{align*}
\begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
  \draw (0,0) rectangle (1,0.7);
\end{tikzpicture}&= \frac{1}{a}\cdot\frac{1}{a^2} = \frac{1}{a^3}\\\begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
  \draw (0,0) -- (1,0) -- (1,0.7);
  \draw (0,0) parabola (1,0.7);
\end{tikzpicture}&= \int_0^{\frac{1}{a}} x^2 \, dx = \frac{1}{3}\frac{1}{a^3}\\\begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
  \draw (0,0) -- (0,0.7) -- (1,0.7);
  \draw (0,0) parabola (1,0.7);
\end{tikzpicture}&= -\int_0^{\frac{1}{a^2}} f(y) \, dy = -\left[\frac{a^2}{18}y^3 - \frac{7}{12}ay^2 \right]_0^{\frac{1}{a^2}} = \frac{19}{36}\frac{1}{a^3}
\end{align*}
$$

だから、[(式2)](#eq:2)に代入して

$$
\begin{align}
S_2 = \frac{\left( 1 - \frac{1}{3} - \frac{19}{36} \right) / a^3 = \frac{5}{36}}{a^3}\label{eq:3}
\end{align}
$$

を得る．

一方 $S_1$ は$\dfrac{1}{a^2}\le y \le \dfrac{4}{a^2}$での$C_1, C_2$の作る領域の差分だから

$$
\begin{align}
S_1 =
 \begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
   \draw (1.4,0) -- (0.35,0) arc (-90:-270:0.35) -- (1.4,0.7) -- cycle;
 \end{tikzpicture}
 -
 \begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
   \draw (-0.2,0.7) -- (1.2,0.7) -- (1.2,0) -- (0,0) -- cycle;
 \end{tikzpicture}\label{eq:4}
\end{align}
$$

である．$y=x^2$の逆関数が$x=\sqrt{y}$であることに注意して各項計算すると

$$
\begin{align*}
\begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
   \draw (1.4,0) -- (0.35,0) arc (-90:-270:0.35) -- (1.4,0.7) -- cycle;
 \end{tikzpicture}&= -\int_{\frac{1}{a^2}}^{\frac{4}{a^2}} f(y) \, dy = -\left[\frac{a^2}{18}y^3 - \frac{7}{12}ay^2 \right]_{\frac{1}{a^2}}^{\frac{4}{a^2}} = \frac{21}{4a^3}\\\begin{tikzpicture}[scale=0.4, baseline=-0.5ex]
   \draw (-0.2,0.7) -- (1.2,0.7) -- (1.2,0) -- (0,0) -- cycle;
 \end{tikzpicture}&= -\int_{\frac{1}{a^2}}^{\frac{4}{a^2}}\sqrt{y}\, dy = \left[\frac{2}{3} y^{\dfrac{3}{2}}\right]_{\frac{1}{a^2}}^{\frac{4}{a^2}} = \frac{14}{3a^3}
\end{align*}
$$

だから，[(式4)](#eq:4)に代入して

$$
\begin{align}
S_1 = \frac{\left( \frac{21}{4} - \frac{14}{3} \right)}{a^3} = \frac{7}{12a^3}\label{eq:5}
\end{align}
$$

を得る．
[(式5)](#eq:3,eq:5)から求める面積比は

$$
\begin{align}
S_1 : S_2 = \frac{7}{12} : \frac{5}{36} = 21 : 5
\end{align}
$$

である．