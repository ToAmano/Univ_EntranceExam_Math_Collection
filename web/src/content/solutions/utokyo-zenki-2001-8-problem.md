---
university: "utokyo"
category: "zenki"
year: "2001"
question: "8"
type: "problem"
title: "UTOKYO 2001 zenki Q8 (problem)"
---

1.  図1のように，等間隔 $h$ で格子状に互いに直交する2組の無数の平行線が引いてある平面が与えられている．
  その上に半径1の円 $C$ を無作為に落とすとき，この円がちょうど2本の線と交わる確率 $p$ を求めよ．

2.  図2のように，半径 $\sqrt2+1$ の円が重複なく，かつ隣り合う円と接して無数に敷き詰められた平面がある．
  この上に半径1の円 $C$ を無作為に落とすとき，その円 $C$ が平面上のちょうど3つの円と交わる確率 $q$ を求めよ．

ただし，解答にあたり次のことを用いてよい．

平面上に共に原点 $O$ を始点とする一次独立な2つのベクトル $\bm{a}$，$\bm{b}$ を考え，
点 $O$ と $\bm{a}$，$\bm{b}$，$\bm{a+b}$ の3つのベクトルの終点の4点を頂点とする平行四辺形を $E$ とする．
$E$ の領域 $F$ に対して，
$F$ を $\bm{a}$ と $\bm{b}$ の整数係数の一次結合 $m\bm{a}+n\bm{b}$ によって平行移動したもの全体の和集合を $D$ とする．
即ち記号で書くと

$$
\begin{align*}
D=\{\bm{x}+m\bm{a}+n\bm{b}\mid\bm{x}\in F, m\in\mathbf{Z}, n\in\mathbf{Z}\}
\end{align*}
$$

とおく．ここで $\mathbf{Z}$ は整数全体を表す．

このとき平面に1点 $P$ を無作為に落とすとき，
その点が $D$ 内に落ちる確率は，
$F$ の面積の平行四辺形 $E$ の面積に対する比になっている．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/zenki/2001/8/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>