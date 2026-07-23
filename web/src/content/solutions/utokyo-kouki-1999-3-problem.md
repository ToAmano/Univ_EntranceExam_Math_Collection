---
university: "utokyo"
category: "kouki"
year: "1999"
question: "3"
type: "problem"
title: "UTOKYO 1999 kouki Q3 (problem)"
---

座標平面上にある3つの四角形 $ABCD$ と $A'B'C'D'$ が相似であるとは，対応する4つの頂点における内角がそれぞれ等しく，かつ対応する辺の長さの比がすべて等しいこととする．このとき，

$$
\begin{align}
\square ABCD \sim\square A'B'C'D'
\end{align}
$$

と書く．ただし，四角形 $ABCD$ と書くときには，4つの頂点 $A, B, C, D$ は図のように反時計回りに並んでいるものとし，また四角形は周および内部を込めて考えるものとする．

四角形$\text{A}_0 \text{B}_0 \text{C}_0 \text{D}_0$が与えられたとき，この四角形から出発して，任意の整数$n$に対して四角形$\text{A}_n \text{B}_n \text{C}_n \text{D}_n$を以下のように帰納的に定める．

1.  $n = 0$のときは，与えられた四角形$\text{A}_0 \text{B}_0 \text{C}_0 \text{D}_0$とする．

2.  $n > 0$のときは，四角形$\text{A}_{n-1} \text{B}_{n-1} \text{C}_{n-1} \text{D}_{n-1}$まで定まったとして，四角形$\text{A}_n \text{B}_n \text{C}_n \text{D}_n$を
        

$$
\begin{align}
\text{A}_n = \text{D}_{n-1}, \quad\text{B}_n = \text{C}_{n-1}\text{ かつ }\square\text{A}_n \text{B}_n \text{C}_n \text{D}_n \sim\square\text{B}_{n-1}\text{C}_{n-1}\text{D}_{n-1}\text{A}_{n-1}
\end{align}
$$

        となる四角形として定める．

3.  $n < 0$のときは， $0, -1, \dots, n+1$と負の向きに進んで，四角形$\text{A}_{n+1} \text{B}_{n+1} \text{C}_{n+1} \text{D}_{n+1}$まで定まったとして，四角形$\text{A}_n \text{B}_n \text{C}_n \text{D}_n$を
        

$$
\begin{align}
\text{D}_n = \text{A}_{n+1}, \quad\text{C}_n = \text{B}_{n+1}\text{ かつ }\square\text{A}_n \text{B}_n \text{C}_n \text{D}_n \sim\square\text{B}_{n+1}\text{C}_{n+1}\text{D}_{n+1}\text{A}_{n+1}
\end{align}
$$

        となる四角形として定める．

こうして定まった四角形$\text{A}_n \text{B}_n \text{C}_n \text{D}_n$を$K_n$と書くことにする．

さて，座標平面上の$3$点

$$
\begin{align}
\text{A}_0(2, 1), \quad\text{B}_0(8, 4), \quad\text{P}(4, 12)
\end{align}
$$

を与える．原点を$\text{O}$とし，線分$\text{OP}$上に原点以外の1点$\text{C}_0$をとる．点$\text{A}_0$から線分$\text{B}_0 \text{C}_0$に平行に引いた直線と，線分$\text{OP}$との交点を$\text{D}_0$とする．このようにして定まる四角形$\text{A}_0 \text{B}_0 \text{C}_0 \text{D}_0$から出発して，上記のようにして得られる四角形の系列

$$
\begin{align}
\dots, K_{-2}, K_{-1}, K_0, K_1, K_2, \dots
\end{align}
$$

について考える．

1.  $\angle \text{B}_0\text{O}\text{P}$を求めよ．

2.  線分$\text{OP}$上のある点$\text{C}_0$を与え，それにより定まる四角形$\text{A}_0 \text{B}_0 \text{C}_0 \text{D}_0$から出発して，四角形の系列$\dots, K_{-2}, K_{-1}, K_0, K_1, K_2, \dots$を作ったところ，ある0でない整数$n$が存在して，$K_n = K_0$となったという．このとき，点$\text{C}_0$の座標を求めよ．また，$K_n = K_0$となる整数$n$の値をすべて求めよ．

3.  線分$\text{OP}$上のある点$\text{C}_0$を与え，それにより定まる四角形$\text{A}_0 \text{B}_0 \text{C}_0 \text{D}_0$から出発して，四角形の系列$\dots, K_{-2}, K_{-1}, K_0, K_1, K_2, \dots$を作ったところ，これらの四角形が座標平面において原点を除いた部分を，辺と頂点以外には互いに重なることなく，すき間なくおおったという．このような性質をもつ点$\text{C}_0$をすべて求め，それらの座標を記せ．またそれらの場合のおのおのについて，点$(100, 50)$が$K_n$に含まれるような整数$n$の値をすべて求めよ．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1999/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>