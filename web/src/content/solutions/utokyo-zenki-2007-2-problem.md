---
university: "utokyo"
category: "zenki"
year: "2007"
question: "2"
type: "problem"
title: "UTOKYO 2007 zenki Q2 (problem)"
---

$r$ は $0<r<1$ をみたす実数，$n$ は2以上の整数とする．
平面上に与えられた1つの円を，
次の条件 (i)，(ii) をみたす2つの円で置き換える操作 (P) を考える．

1.  新しい2つの円の半径の比は $r:1-r$ で，半径の和はもとの円の半径に等しい．

2.  新しい2つの円は互いに外接し，もとの円に内接する．

以下のようにして，平面上に $2^n$ 個の円を作る．

1.  最初に，平面上に半径1の円を描く．

2.  次に，この円に対して操作 (P) を行い，2つの円を得る(これを1回目の操作という)．

3.  $k$ 回目の操作で得られた $2^k$ 個の円のそれぞれについて，
  操作 (P) を行い，$2^{k+1}$ 個の円を得る $(1 \leqq k \leqq n-1)$．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/zenki/2007/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>

1.  $n$ 回目の操作で得られる $2^n$ 個の円の周の長さの和を求めよ．

2.  2回目の操作で得られる4つの円の面積の和を求めよ．

3.  $n$ 回目の操作で得られる $2^n$ 個の円の面積の和を求めよ．