---
university: "utokyo"
category: "zenki"
year: "1990"
question: "9"
type: "problem"
title: "UTOKYO 1990 zenki Q9 (problem)"
---

長さ1の線分をつなげてできる右のような平面上の図形 $Q_1,Q_2,Q_3,\cdots$ を考える．
$n=1,2,3,\cdots$ に対し，図形 $Q_n$ の左端の点を $A_n$，右端の点を $B_n$，上端の点を $C_n$ とする．

$Q_1$ は一辺の長さが1の正三角形の周である．
$Q_2$ は図のように，$Q_1$ を3つつなげてできる図形である．

$Q_n$ と同じ図形を3つ用意し，それらを $Q_n(1)$，$Q_n(2)$，$Q_n(3)$ とする．
$i=1,2,3$ に対し，$Q_n(i)$ の左端の点を $A_n(i)$，右端の点を $B_n(i)$，上端の点を $C_n(i)$ としたとき，
$Q_{n+1}$ は，$B_n(1)$ と $A_n(2)$，$C_n(2)$ と $B_n(3)$，$A_n(3)$ と $C_n(1)$ が
それぞれ同一の点になるようにおいできる図形である．

$Q_n$ において，
$A_n$ から線分の上を通り，
一度通った点は二度通らずに $B_n$ まで行く行き方を考える．
この行き方のうち，
途中 $C_n$ を通らない場合の個数を $x_n$ とし，
途中 $C_n$ を通る場合の個数を $y_n$ とする．
容易にわかるように，$x_1=y_1=1$ である．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/zenki/1990/9/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>

1.  $x_2$，$y_2$ を求めよ．

2.  $x_{n+1}$ を $x_n$，$y_n$ を用いて表せ．また，$y_{n+1}$ を $x_n$，$y_n$ を用いて表わせ．

3.  $x_3$，$y_3$ を求めよ．