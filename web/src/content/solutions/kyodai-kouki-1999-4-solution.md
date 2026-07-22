---
university: "kyodai"
category: "kouki"
year: "1999"
question: "4"
type: "solution"
title: "KYODAI 1999 kouki Q4 (solution)"
---

## 【解】

    $\triangle ABC$の$3$辺の長さを$a,b,c$とする ($a,b,c > 0$)．
    $\triangle ABC$が鋭角三角形だから，余弦定理より
    

$$
\begin{align*}
c^2 = a^2+b^2 - 2ab\cos\angle\mathrm{ABC} < a^2+b^2
\end{align*}
$$

    のような式が成り立つから，
    

$$
\begin{align*}
\begin{cases}
            x^2 = \frac{a^2+b^2-c^2}{2} > 0 \\
            y^2 = \frac{a^2-b^2+c^2}{2} > 0 \\
            z^2 = \frac{-a^2+b^2+c^2}{2} > 0
        \end{cases}
\end{align*}
$$

    となる$x,y,z \in \mathbb{R}^+$が存在する．
    従って，これら$x,y,z$を$3$辺の長さとする直方体が存在する．
    この時図のように四面体$ABCD$をとると各面が相似になっているから題意は示された．$\cdots$(答)

    

<figure id="1999-4:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1999/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 題意を満たす直方体と四面体</figcaption>
</figure>

    
    

## 【解説】