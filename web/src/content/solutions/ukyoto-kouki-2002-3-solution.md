---
university: "ukyoto"
category: "kouki"
year: "2002"
question: "3"
type: "solution"
title: "UKYOTO 2002 kouki Q3 (solution)"
---

## 【解】

    

<figure id="2002-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/2002/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 四面体ABCDの様子</figcaption>
</figure>

    平面$\alpha$が平面ABCに一致する時，C'はCと一致するが，
    各角が鋭角三角形だから，D'は平面ABC上でAを通り
    辺ABに垂直な直線$l_1$と，Bを通り辺ABに垂直な直線$l_2$の
    間の領域にある．

    同様のことを辺BC，CAに対しても考えると，
    D'は下図のように3組の平行直線 $(l_1, l_2)$, $(m_1, m_2)$, $(n_1, n_2)$
    で囲まれた領域内にある．
    $m_1$と$n_2$， $n_2$と$l_2$， $l_1$と$m_2$ の交点を各々P, Q, Rとすると，
    $D'$は六角形APBQCRの内部に存在する．

    

<figure id="2002-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/2002/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 六角形APBQCRの様子</figcaption>
</figure>

    $l,m,n$の直線の定義から
    

$$
\begin{align*}
& \angle\text{CAP} = \angle\text{CBP} = \frac{\pi}{2}\\& \angle\text{ABQ} = \angle\text{ACQ} = \frac{\pi}{2}\\& \angle\text{BCR} = \angle\text{BAR} = \frac{\pi}{2}
\end{align*}
$$

    だから，六角形APBQCRは同一円周上にある．
    この円は三角形ABCの外接円である．

    従って，点D'は三角形ABCの外接円の内側にある．
    よって円周角の定理から
    

$$
\begin{align}
\angle\text{ACB} = \angle\text{ACB} < \angle\text{AD'B}\label{2002-3:eq:1}
\end{align}
$$

    である．

    次に平面$\alpha$が平面ABDに一致するまで回転させることを考える．
    この時$\angle \text{AC'B}$と$\angle \text{AD'B}$は連続的に変化する．
    条件から辺ABと辺CDが垂直でないので，C'とD'は一致しないことに注意する．
    最終的に平面$\alpha$が平面ABDに一致するとき，[(式1)](#2002-3:eq:1)と同じく
    

$$
\begin{align}
\angle\text{AC'B} > \angle\text{ADB} = \angle\text{AD'B}\label{2002-3:eq:2}
\end{align}
$$

    である．

    従って，[(式2)](#2002-3:eq:1,2002-3:eq:2)から，
    平面$\alpha$を動かす間に$\angle \text{AC'B}$と$\angle \text{AD'B}$の大小関係が逆転する．
    これらの角度は連続的に変化するので，$\angle \text{AC'B}=\angle \text{AD'B}$となるような$\alpha$が絶対に存在する．
    この時円周角の定理より，異なる4点A, B, C', D'が同一円周上に存在する．
    よって題意は示された．$\cdots$(答)

    
    

## 【解説】