---
university: "titech"
category: "zenki"
year: "1961"
question: "3"
type: "solution"
title: "TITECH 1961 zenki Q3 (solution)"
---

## 【解】

簡単のため$c = \cos\theta, s = \sin\theta$ とおく ($0 \le \theta < 2\pi$)と，
題意から$(x,y)$は半径$1$の円周上にあるから $(x,y) = (c,s)$ とおける．

$f(\theta) = c^2 - s^2 + 2\sqrt{3}cs$ とすると倍角公式および三角関数の合成より

$$
\begin{align}
f(\theta) 
 & = \cos 2\theta + \sqrt{3}\sin 2\theta\\&= 2\sin\left(2\theta + \frac{\pi}{6}\right)
\end{align}
$$

と書ける．$0 \le \theta < 2\pi$にも注意すると，
$f(\theta)$ が最大の時，$\theta = \dfrac{\pi}{6}, \dfrac{7}{6}\pi$ で $(x,y) = \left(\dfrac{\sqrt{3}}{2}, \dfrac{1}{2}\right), \left(-\dfrac{\sqrt{3}}{2}, -\dfrac{1}{2}\right)$である．

$f(\theta)$ が最小の時，$\theta = \dfrac{2}{3}\pi, \dfrac{5}{3}\pi$ で $(x,y) = \left(-\dfrac{1}{2}, \dfrac{\sqrt{3}}{2}\right), \left(\dfrac{1}{2}, -\dfrac{\sqrt{3}}{2}\right)$．
である．以上まとめると

$$
\begin{align}
(x,y) = 
 \begin{cases}
  \left(\dfrac{\sqrt{3}}{2}, \dfrac{1}{2}\right), \left(-\dfrac{\sqrt{3}}{2}, -\dfrac{1}{2}\right) & (\text{最大}) \\
  \left(-\dfrac{1}{2}, \dfrac{\sqrt{3}}{2}\right), \left(\dfrac{1}{2}, -\dfrac{\sqrt{3}}{2}\right) & (\text{最小})  
 \end{cases}
\end{align}
$$

が求める$(x,y)$の値である．

## 【解説】

単なる三角関数の最大最小問題に落とし込める．今回の$f(\theta)$の概形は以下のようになる．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1961/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $f(\theta)$の概形とその最大最小値．</figcaption>
</figure>