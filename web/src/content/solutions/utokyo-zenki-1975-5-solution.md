---
university: "utokyo"
category: "zenki"
year: "1975"
question: "5"
type: "solution"
title: "UTOKYO 1975 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (1) $r(n) = \frac{a}{2^n}$ とおく。 $O_n$ を原点とし, $\vec{O_n O_{n+1}}$ を $x$ 軸とする下図のような平面をとる。この平面での $S_n, S_{n+1}$ の断面は

$$
\begin{align*}
C_n : x^2 + y^2 = r(n)^2
\end{align*}
$$

$$
\begin{align*}
C_{n+1} : (x - r(n))^2 + y^2 = r(n+1)^2
\end{align*}
$$

であり, これらの交点の $x$ 座標は,

$$
\begin{align*}
x = \frac{-r(n+1)^2 + 2r(n)^2}{2r(n)} = \frac{7a}{2^{n+3}}
\end{align*}
$$

である。ここで, $x, y$ 軸へ $\frac{2^n}{a}$ 倍した座標で考えれば, もとめる体積 $V_n$ は

$$
\begin{align*}
\begin{aligned}
\left( \frac{2^n}{a} \right)^3 V_n &= \pi \int_{\frac{7}{8}}^{\frac{1}{2}} \left\{ \frac{1}{4} - (x-1)^2 \right\} dx + \pi \int_{\frac{7}{8}}^1 (1 - x^2) dx \\
&= \pi \int_{\frac{1}{8}}^{\frac{1}{2}} \left( \frac{1}{4} - x^2 \right) dx + \pi \int_{\frac{7}{8}}^1 (1 - x^2) dx \quad \cdots \text{①}
\end{aligned}
\end{align*}
$$

各項計算して,

1.  $\displaystyle \int_{\frac{1}{8}}^{\frac{1}{2}} \left(\frac{1}{4} - x^2\right) dx = \left[ \frac{1}{4} x - \frac{1}{3} x^3 \right]_{\frac{1}{8}}^{\frac{1}{2}} = \frac{1}{4} \left( \frac{1}{2} - \frac{1}{8} \right) - \frac{1}{3} \left( \frac{1}{8} - \frac{1}{8^3} \right) = \frac{27}{8 \cdot 64}$

2.  $\displaystyle \int_{\frac{7}{8}}^1 (1 - x^2) dx = \left[ x - \frac{1}{3} x^3 \right]_{\frac{7}{8}}^1 = \frac{2}{3} - \left( \frac{7}{8} - \frac{1}{3} \left( \frac{7}{8} \right)^3 \right) = \frac{23}{3 \cdot 8^3}$

だから, ①より

$$
\begin{align*}
V_n = \pi \left(\frac{a}{2^n}\right)^3 \left\{ \frac{27}{8^3} + \frac{23}{3 \cdot 8^3} \right\} = \pi \left(\frac{a}{2^{n+3}}\right)^3 \cdot \frac{104}{3}
\end{align*}
$$

(2)

$$
\begin{align*}
V_m = \frac{104 a^3 \pi}{3} \sum_{n=1}^m \left(\frac{1}{2^{n+3}}\right)^3 = \frac{104 a^3 \pi}{3} \left(\frac{1}{2^4}\right)^3 \frac{1 - (1/2)^{3m}}{1 - (1/2)^3} \xrightarrow{m \to \infty} \frac{13}{1344} a^3 \pi
\end{align*}
$$

[注]
$V_n$ の求値に球帽公式を用いると,

1.  $\displaystyle \int_{\frac{1}{8}}^{\frac{1}{2}} \left(\frac{1}{4} - x^2\right) dx = \frac{3/8}{2 \cdot 1/2} \cdot \frac{4}{3} \pi \left(\frac{1}{2}\right)^3 - \frac{1}{3} \left(\frac{\sqrt{15}}{8}\right)^2 \cdot \pi \cdot \frac{1}{8} = \frac{27 \pi}{8^3}$

2.  $\displaystyle \int_{\frac{7}{8}}^1 (1 - x^2) dx = \frac{1/8}{2 \cdot 1} \cdot \frac{4}{3} \pi - \frac{1}{3} \left(\frac{\sqrt{15}}{8}\right)^2 \cdot \pi \cdot \frac{7}{8} = \frac{23 \pi}{3 \cdot 8^3}$

と計算出来る。

\begin{tikzpicture}[scale=2.0]
  \draw[->] (-0.3,0) -- (1.6,0) node[right] {$x$};
  \draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};
  \node[below left] at (0,0) {$O_n$};
  
  \draw (0,0) circle (1);
  \draw (1,0) circle (0.5);
  \node[below] at (1,0) {$O_{n+1}$};
  \node[below right] at (0.5,0) {$\frac{a}{2^n}$};
  
  \begin{scope}
    \clip (0,0) circle (1);
    \clip (1,0) circle (0.5);
    \fill[gray!30] (-1,-1) rectangle (2,1);
  \end{scope}
  \draw (0,0) circle (1);
  \draw (1,0) circle (0.5);
  
  \begin{scope}[shift={(0,-2.5)}]
    \draw[->] (-0.3,0) -- (1.4,0) node[right] {$x'$};
    \draw[->] (0,-0.3) -- (0,1.3) node[above] {$y'$};
    \node[below left] at (0,0) {$0$};
    
    \draw[domain=0:1,samples=100] plot (\x, {sqrt(1-\x*\x)});
    \draw[domain=0.5:1.5,samples=100] plot (\x, {sqrt(0.25-(\x-1)*(\x-1))});
    
    \node[above left] at (0.7,0.7) {$x'^2+y'^2=1$};
    \node[above right] at (1.1,0.4) {$(x'-1)^2+y'^2=\frac{1}{4}$};
    
    \draw[dashed] (7/8,0) -- (7/8, {sqrt(1-49/64)});
    \node[below] at (7/8,0) {$7/8$};
    \node[below] at (1/2,0) {$1/2$};
    \node[below] at (1,0) {$1$};
    \node[left] at (0, {sqrt(15)/8}) {$\frac{\sqrt{15}}{8}$};
  \end{scope}
\end{tikzpicture}