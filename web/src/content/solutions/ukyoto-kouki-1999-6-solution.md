---
university: "ukyoto"
category: "kouki"
year: "1999"
question: "6"
type: "solution"
title: "UKYOTO 1999 kouki Q6 (solution)"
---

## 【解】

    (1)
    $f(x)$の原始関数$F(x)$とすると，与えられた方程式は
    

$$
\begin{align*}
\frac{F(b)-F(a)}{b-a} = F'(c)
\end{align*}
$$

    であるが，これは平均値の定理そのものである．よって示された．$\cdots$(答)

    
    (2)
    

$$
\begin{align}
& f(x) = \sin x & 0 \le x \le\frac{\pi}{2}\label{1999-6:eq:1}
\end{align}
$$

    とおき，$f(x)$ の逆関数 $g(x)$ とおく．
    

$$
\begin{align*}
x=g(y) \iff y=f(x) \quad\dots\text{①}
\end{align*}
$$

    

<figure id="1999-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1999/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 回転させる図形の様子</figcaption>
</figure>

    題意の立体の体積 $V$ は
    

$$
\begin{align}
V = \pi\int_{0}^{1}\{g(y)\}^2 dy \label{1999-6:eq:2}
\end{align}
$$

    と書ける．$x=g(y)$とおくと
    

$$
\begin{align}
\int_{0}^{1}\{g(y)\}^2 dy
         & = \int_{0}^{\pi/2} x^2 \frac{dy}{dx} dx                              \\& = \int_{0}^{\pi/2} x^2 f'(x) dx \quad(\because x=f(y))              \\& = \int_{0}^{\pi/2} x^2 \cos x dx \quad(\because[(式2)](#1999-6:eq:2)) \\& = \left[ x^2 \sin x + 2x \cos x - 2\sin x \right]_{0}^{\pi/2}\\& = \frac{\pi^2}{4} - 2
\end{align}
$$

    となるから，[(式2)](#1999-6:eq:2)に代入して
    

$$
\begin{align}
V = \pi\left(\frac{\pi^2}{4} - 2\right)\label{1999-6:eq:3}
\end{align}
$$

    である．

    次に体積$V$を$n$等分する点$y_n$について
    

$$
\begin{align}
\frac{V}{n} = \pi\int_{y_n}^{1}\{g(x)\}^2 dx \label{1999-6:eq:4}
\end{align}
$$

    が成立する．
    ここで(1)から
    

$$
\begin{align*}
(1-y_n) \cdot\{g(c)\}^2 = \int_{y_n}^{1}\{g(x)\}^2 dx \quad(y_n < c < 1)
\end{align*}
$$

    をみたす $c$ が存在する．
    [(式4)](#1999-6:eq:4)に代入して
    

$$
\begin{align}
\frac{V}{n} = \pi(1-y_n) \{g(c)\}^2 \label{1999-6:eq:5}
\end{align}
$$

    である．
    ここで，$n \to \infty$ の時 $y_n \to 1$．だから，はさみうちから $c \to 1$，つまり
    

$$
\begin{align*}
\lim_{n\to\infty}\{g(c)\}^2
         & = \left\{g(1) \right\}^2       \\& = \left(\frac{\pi}{2}\right)^2
\end{align*}
$$

    である．したがって，[(式5)](#1999-6:eq:3,1999-6:eq:5)より
    

$$
\begin{align*}
n(1-y_n)
         & = \frac{V}{\pi\{g(c)\}^2}\\& = \frac{\frac{\pi^2}{4} - 2}{\{g(c)\}^2}\\& \xrightarrow{n\to\infty}\frac{\frac{\pi^2}{4} - 2}{\left(\frac{\pi}{2}\right)^2}\\& = 1 -  \frac{8}{\pi^2}
\end{align*}
$$

    を得る．従って求める極限値は
    

$$
\begin{align*}
\lim_{n\to\infty} n(1-y_n) = 1 -  \frac{8}{\pi^2}
\end{align*}
$$

    である．$\cdots$(答)

    
    

## 【解説】

    (1)は，平均値の定理自体は認めてしまって良いと思われる．
    ただ，せっかくの良い機会なので，平均値の定理の証明をここで復習しよう．