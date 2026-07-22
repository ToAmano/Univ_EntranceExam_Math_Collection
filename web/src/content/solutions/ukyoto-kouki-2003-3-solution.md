---
university: "ukyoto"
category: "kouki"
year: "2003"
question: "3"
type: "solution"
title: "UKYOTO 2003 kouki Q3 (solution)"
---

## 【解】

  解と係数の関係から
  

$$
\begin{align}
& \alpha_1 \alpha_2 \alpha_3                                 = -1 \label{2003-3:eq:1}\\& \alpha_2 \alpha_3 + \alpha_3 \alpha_1 + \alpha_1 \alpha_2  = b  \label{2003-3:eq:2}\\& \alpha_1 + \alpha_2 + \alpha_3                             = -a \label{2003-3:eq:3}
\end{align}
$$

  である.[(式1)](#2003-3:eq:1)より，どの$\alpha$も$0$ではない．
  [(式3)](#2003-3:eq:3)において$a \in \mathbb{R}$ だから, $\alpha_1 \sim \alpha_3$ のうち,1つ又は3つが実数の場合を調べれば良い.
  （二つのみ実数の時は，$a$が虚数となり不適）

  \begin{itemize}
    \item[$1$] $ \alpha_1, \alpha_2, \alpha_3 \in \mathbb{R} $の時
          題意の条件より
          

$$
\begin{align*}
\alpha_1 & = \alpha_2 \pm\sqrt{3}\\\alpha_2 & = \alpha_3 \pm\sqrt{3}\\\alpha_3 & = \alpha_1 \pm\sqrt{3}
\end{align*}
$$

          だが, 一つ目と二つ目の式から
          

$$
\begin{align*}
\alpha_1 = \alpha_3 \pm\sqrt{3}\pm\sqrt{3}\\
            =
            \begin{dcases}
              \alpha_3 + 2\sqrt{3} \\
              \alpha_3
              \alpha_3 - 2\sqrt{3}
            \end{dcases}
\end{align*}
$$

          を得るが，これは三つ目の式に反して矛盾．
          よって$ \alpha_1, \alpha_2, \alpha_3 \in \mathbb{R} $の時は条件を満たさず不適．

    \item[$2$] $\alpha_1,\alpha_2,\alpha_3$のうち，一つが実数，二つが虚数の時
          $\alpha_1,\alpha_2,\alpha_3$について対称だから，
          $\alpha_1 \in \mathbb{R}$, $\alpha_2, \alpha_3 \notin \mathbb{R}$
          の時を考えれば十分．
          [(式3)](#2003-3:eq:1,2003-3:eq:3)より，
          

$$
\begin{align*}
\alpha_2\alpha_3  & = -\frac{1}{\alpha_1}\in\mathbb{R}\alpha_2+\alpha_3 & = -a -\alpha_1 \in\mathbb{R}
\end{align*}
$$

          である．二つ目の式より$\alpha_2$と$\alpha_3$の虚部は符号が逆である．
          このもとで一つ目の式より，$\alpha_2$と$\alpha_3$の実部は等しくないといけない．
          すなわち
          

$$
\begin{align*}
\alpha_3 = \bar{\alpha_2}
\end{align*}
$$

          となる．
          $\alpha_2,\alpha_3$の対称性から $\alpha_2$ の虚部が$0$より大きくなるようにおく.
          以上の条件を満たす時，
          複素数平面上で, $\alpha_1 \sim \alpha_3$ は下図のようになる.

          従って，題意の条件$|\alpha_i-\alpha_j|=\sqrt{3}$は
          

$$
\begin{align*}
\begin{dcases}
              \alpha_2 & = \alpha_1 \pm \frac{3}{2} + \frac{\sqrt{3}}{2}i \quad \text{(複号同順)} \quad \cdots \text{\textcircled{2}} \\
              \alpha_3 & = \alpha_1 \pm \frac{3}{2} - \frac{\sqrt{3}}{2}i
            \end{dcases}
\end{align*}
$$

          とおける.

          $\alpha_1$を求めるため，[(式1)](#2003-3:eq:1)に代入して整理すると
          

$$
\begin{align*}
& \alpha_1^3 \pm 3 \alpha_1^2 + 3 \alpha_1 + 1  = 0 \\\therefore& \begin{dcases}
                 (\alpha_1+1)^3 = 0 \quad (\text{複号 正}) \\
                 (\alpha_1-1)^3 = -2 \quad (\text{複号 負})
               \end{dcases}\\\therefore& \alpha_1 = -1, 1-\sqrt[3]{2}
\end{align*}
$$

          を得る．従って，
          

$$
\begin{align*}
(\alpha_1, \alpha_2, \alpha_3)
            = & (-1, \frac{1}{2}+\frac{\sqrt{3}}{2}i, \frac{1}{2}-\frac{\sqrt{3}}{2}i),                                     \\& (1-\sqrt[3]{2}, -\frac{1}{2}-\sqrt[3]{2}+\frac{\sqrt{3}}{2}i, -\frac{1}{2}-\sqrt[3]{2}-\frac{\sqrt{3}}{2}i)
\end{align*}
$$

          となり，[(式3)](#2003-3:eq:2,2003-3:eq:3)に代入すると
          

$$
\begin{align*}
(a,b) = (0,0), (3\sqrt[3]{2}, 3\sqrt[3]{4})
\end{align*}
$$

          を得る．
  \end{itemize}

  

<figure id="2003-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/2003/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $\alpha_1,\alpha_2,\alpha_3$の様子</figcaption>
</figure>

  以上により全ての場合が尽くされた．従って求める$(a,b)$は
  

$$
\begin{align*}
(a,b) = (0,0), (3\sqrt[3]{2}, 3\sqrt[3]{4})
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】