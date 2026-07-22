---
university: "ukyoto"
category: "kouki"
year: "1996"
question: "4"
type: "solution"
title: "UKYOTO 1996 kouki Q4 (solution)"
---

## 【解】

  

<figure id="1996-4:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1996/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 四面体ABCDの様子</figcaption>
</figure>

  四面体の$4$頂点をA，B，C，Dとして，
  

$$
\begin{align}
\begin{dcases}
      \text{AB} & = \sqrt{x+y} = \alpha \\
      \text{BC} & = \sqrt{x-y} = \beta
    \end{dcases}\label{1996-4:eq:1}
\end{align}
$$

  とおく．

  このような四面体の存在条件を考える.
  一辺の長さ$1$の正三角形$\text{ACD}$は$\alpha, \beta$によらず存在する.
  よって点Bの存在条件を考えれば良い.
  そこで, $\text{D}$を原点, $\text{DA}$を$X$軸方向とし$\mathrm{C}(\frac{1}{2}, \frac{\sqrt{3}}{2}, 0)$
  となるような$XYZ$座標で考える．

  

<figure id="1996-4:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1996/4/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $XY$平面の様子</figcaption>
</figure>

  $\text{B}(X,Y,Z)$の存在条件は
  

$$
\begin{align}
& \begin{dcases}
         |BD| = 1      \\
         |AB| = \alpha \\
         |BC| = \beta
       \end{dcases}\therefore\\& \begin{dcases}
         X^2+Y^2+Z^2                                                          & = 1        \\
         (X-1)^2+Y^2+Z^2                                                      & = \alpha^2 \\
         \left(X-\frac{1}{2}\right)^2+\left(Y-\frac{\sqrt{3}}{2}\right)^2+Z^2 & = \beta^2
       \end{dcases}\label{1996-4:eq:2}
\end{align}
$$

  をみたす$(X, Y, Z)$の存在条件に等しい.
  ただし，ABCDが四面体となる条件として
  

$$
\begin{align*}
Z \neq 0
\end{align*}
$$

  が必要である．

  [(式2)](#1996-4:eq:2)で第一式を第二，三式に代入すると
  

$$
\begin{align*}
& \begin{dcases}
         -2X+2          & = \alpha^2 \\
         -X-\sqrt{3}Y+2 & = \beta^2
       \end{dcases}\\& \begin{dcases}
         X & = \frac{1}{2}(2-\alpha^2)                                      \\
         Y & = \frac{\sqrt{3}}{3}\left(1+\frac{1}{2}\alpha^2-\beta^2\right)
       \end{dcases}
\end{align*}
$$

  だから，これを[(式2)](#1996-4:eq:2)の第一式に代入して$X,Y$を削除すると
  

$$
\begin{align}
Z^2 = 1 - \frac{1}{4}\left(2-\alpha^2\right)^2 - \frac{1}{3}\left(1+\frac{1}{2}\alpha^2-\beta^2\right)^2 \label{1996-4:eq:3}
\end{align}
$$

  である．

  このような実数$X, Y, Z$の存在条件は
  [(式3)](#1996-4:eq:3)の左辺が$0$より大となることで($\because z \neq 0$)
  

$$
\begin{align*}
& 1 - \frac{1}{4}(2-\alpha^2)^2 - \frac{1}{3}\left(1+\frac{1}{2}\alpha^2-\beta^2\right)^2 > 0 \\\Leftrightarrow& 1 - \frac{1}{4}(2-(x+y))^2 - \frac{1}{12}(2-x+3y)^2 > 0                                     \\\Leftrightarrow& x^2-4x+3y^2+1 < 0                                                                           \\\Leftrightarrow& \frac{(x-2)^2}{3} + y^2 < 1
\end{align*}
$$

  である．

  これと$x+y,x-y>0$が求める領域で，図示すると図車線部（境界は含まず）である．$\cdots$(答)

  

<figure id="1996-4:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1996/4/fig_3.svg" alt="図 3" />
  <figcaption>図 3: 求める$xy$の存在領域．境界は含まず．</figcaption>
</figure>

  
  

## 【解説】