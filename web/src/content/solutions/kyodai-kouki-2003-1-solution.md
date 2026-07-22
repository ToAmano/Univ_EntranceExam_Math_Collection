---
university: "kyodai"
category: "kouki"
year: "2003"
question: "1"
type: "solution"
title: "KYODAI 2003 kouki Q1 (solution)"
---

## 【解】

    

<figure id="2003-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2003/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形ABCの様子</figcaption>
</figure>

    点 $X$ に対応し, $\vec{AX} = \vec{x}$ と書くことにする．
    すなわち，点Aを原点とする位置ベクトルで考える．
    $\vec{b}, \vec{c}$ は三角形をなすから平行ではなく，一次独立である．
    また，三角形ABCが正三角形であるから
    

$$
\begin{align}
|\vec{b}| = |\vec{c}| = |\vec{c}-\vec{b}| \label{2003-1:eq:1}
\end{align}
$$

    題意より，$k=1,2$ として
    

$$
\begin{align*}
\vec{P_k}& = t_k \vec{b}\\\vec{Q_k}& = s_k \vec{b} + (1-s_k) \vec{c}\\\vec{R_k}& = r_k \vec{c}
\end{align*}
$$

    とおける．ただし
    

$$
\begin{align*}
& 0 < t_k < 1 \\& 0 < s_k < 1 \\& 0 < r_k < 1
\end{align*}
$$

    である．

    $\triangle P_k Q_k R_k$ の重心 $G_k$ と して
    

$$
\begin{align*}
\vec{G_k}& = \frac{1}{3}\left[\vec{P_k}+\vec{Q_k}+\vec{R_k}\right]\\& = \frac{1}{3}\left[(t_k+s_k) \vec{b} + (1+r_k-s_k) \vec{c}\right]
\end{align*}
$$

    だから， $G_1 = G_2$ の時
    

$$
\begin{align}
& \begin{dcases}
               t_1+s_1   & = t_2+s_2   \\
               1+r_1-s_1 & = 1+r_2-s_2
           \end{dcases}\\\therefore& s_1-s_2  = t_1-t_2 = r_1-r_2 \label{2003-1:eq:2}
\end{align}
$$

    が成り立つ．

    [(式2)](#2003-1:eq:1,2003-1:eq:2)から
    

$$
\begin{align*}
\vec{P_1 P_2}& = |(t_2-t_1) \vec{b}| = |(r_1-r_2) \vec{c}| = \vec{R_1 R_2}\\\vec{Q_1 Q_2}& = |(s_1-s_2)(\vec{b}-\vec{c})| = |(r_1-r_2)\vec{C}| = \vec{R_1 R_2}
\end{align*}
$$

    だから，
    

$$
\begin{align*}
\vec{P_1 P_2} = \vec{Q_1 Q_2} = \vec{R_1 R_2}
\end{align*}
$$

    が成り立つ．$\cdots$(答)

    
    

## 【解説】