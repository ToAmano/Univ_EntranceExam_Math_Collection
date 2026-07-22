---
university: "ukyoto"
category: "kouki"
year: "2005"
question: "4"
type: "solution"
title: "UKYOTO 2005 kouki Q4 (solution)"
---

## 【解】

  

<figure id="2005-4:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/2005/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 四面体OABCとA'B'C'の様子</figcaption>
</figure>

  点Xに対し, $\vec{OX}=\vec{x}$ と表すことにすると
  $\vec{a}, \vec{b}, \vec{c}$ は四面体をなすから1次独立である．

  三角形ABCの重心Gの位置ベクトルは
  

$$
\begin{align*}
\vec{g} = \frac{\vec{a}+\vec{b}+\vec{c}}{3}
\end{align*}
$$

  だから，線分OGを$t:1-t$で内分する点Pの位置ベクトルは
  

$$
\begin{align*}
\vec{p}& = t \vec{g}\\& = t \frac{\vec{a}+\vec{b}+\vec{c}}{3}
\end{align*}
$$

  である．

  次にA'について考える．
  A'はAP上の点だから$k \in \mathbb{R}$として
  

$$
\begin{align*}
\vec{a'}& = \vec{a}+k(\vec{p}-\vec{a})
     & = \left(1-k+\frac{t}{3}\right)\vec{a}+\frac{kt}{3}\vec{b} +\frac{kt}{3}\vec{c}
\end{align*}
$$

  とおける．
  一方でA'は平面OBC上の点だから$\vec{b}$と$\vec{c}$の重ね合わせでかけ，$\vec{a}$の成分はあってはならない．
  従って，$\vec{a}$の係数比較すると，
  

$$
\begin{align*}
& 0 = 1-k+\frac{kt}{3}\\\therefore& k = \frac{3}{3-t}
\end{align*}
$$

  となり，
  

$$
\begin{align*}
\vec{a'} = \frac{t}{3-t}(\vec{b}+\vec{c})
\end{align*}
$$

  と書ける．

  同様にB'およびC'について
  

$$
\begin{align*}
\vec{b'}& = \frac{t}{3-t}(\vec{a}+\vec{c}) \\\vec{c'}& = \frac{t}{3-t}(\vec{a}+\vec{b})
\end{align*}
$$

  であるから，
  三角形A'B'C'の各辺の長さについて
  

$$
\begin{align*}
\vec{A'B'}& = \left|\frac{t}{3-t}\right||\vec{a}-\vec{b}| \\& = \frac{t}{3-t} AB                            \\\vec{B'C'}& = \frac{t}{3-t} BC                            \\\vec{C'A'}& = \frac{t}{3-t} CA
\end{align*}
$$

  となるから，
  たしかに $\triangle ABC \propto \triangle A'B'C'$ で，相似比は
  

$$
\begin{align*}
\triangle ABC : \triangle A'B'C' = 1 : \frac{t}{3-t}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】