---
university: "utokyo"
category: "kouki"
year: "1990"
question: "3"
type: "problem"
title: "UTOKYO 1990 kouki Q3 (problem)"
---

\newcommand{\drawTriangle}[3]{
  \draw (#1) -- (#2) -- (#3) -- cycle;
}

\newcommand{\recursiveTriangleQTwo}[4]{
  \ifnum#4=0
    \drawTriangle{#1}{#2}{#3};
  \else
    \path let
    \p1 = (#1), \p2 = (#2), \p3 = (#3)
    in
    coordinate (MAB2) at ($ (\p1)!0.5!(\p2) $)
    coordinate (MBC2) at ($ (\p2)!0.5!(\p3) $)
    coordinate (MCA2) at ($ (\p3)!0.5!(\p1) $);
    \drawTriangle{#1}{#2}{#3};
    \drawTriangle{MAB2}{MBC2}{MCA2};
  \fi
}

\newcommand{\recursiveTriangleQThree}[3]{
  \path let
  \p1 = (#1), \p2 = (#2), \p3 = (#3)
  in
  coordinate (MAB3) at ($ (\p1)!0.5!(\p2) $)
  coordinate (MBC3) at ($ (\p2)!0.5!(\p3) $)
  coordinate (MCA3) at ($ (\p3)!0.5!(\p1) $);
  \drawTriangle{#1}{#2}{#3};
  \drawTriangle{MAB3}{MBC3}{MCA3};
  \recursiveTriangleQTwo{#1}{MAB3}{MCA3}{1}
  \recursiveTriangleQTwo{MAB3}{#2}{MBC3}{1}
  \recursiveTriangleQTwo{MCA3}{MBC3}{#3}{1}
}

\newcommand{\recursiveTriangleQFour}[3]{
  \path let
  \p1 = (#1), \p2 = (#2), \p3 = (#3)
  in
  coordinate (MAB4) at ($ (\p1)!0.5!(\p2) $)
  coordinate (MBC4) at ($ (\p2)!0.5!(\p3) $)
  coordinate (MCA4) at ($ (\p3)!0.5!(\p1) $);
  \drawTriangle{#1}{#2}{#3};
  \drawTriangle{MAB4}{MBC4}{MCA4};
  \recursiveTriangleQThree{#1}{MAB4}{MCA4}
  \recursiveTriangleQThree{MAB4}{#2}{MBC4}
  \recursiveTriangleQThree{MCA4}{MBC4}{#3}
}

長さ1の線分をつなげてできる右のような平面上の図形 $Q_1, Q_2, Q_3, \ldots$ を考える．\\
$n = 1, 2, 3, \ldots$ に対し，図形 $Q_n$ の左端の点を $A_n$, 右端の点を $B_n$, 上端の点を $C_n$ とする．

$Q_1$ は一辺の長さが1の正三角形の周である．$Q_2$ は図のように，$Q_1$ を3つつなげてできる図形である．

$Q_n$ と同じ図形を3つ用意し，それらを $Q_n(1), Q_n(2), Q_n(3)$ とする．
$i = 1, 2, 3$ に対し，$Q_n(i)$ の左端の点を $A_n(i)$, 右端の点を $B_n(i)$, 上端の点を $C_n(i)$ としたとき，
$Q_{n+1}$ は，$B_n(1) = A_n(2),\; C_n(2) = B_n(3),\; A_n(3) = C_n(1)$ がそれぞれ同一の点になるようにおいてできる図形である．

$Q_n$ において，$A_n$ から線分の上を通り，一度通った点は二度通らずに $B_n$ まで行く行き方を考える．
この行き方のうち，途中 $C_n$ を通らない場合の個数を $x_n$ とし，途中 $C_n$ を通る場合の個数を $y_n$ とする．
容易にわかるように，$x_n - y_n = 1$ である．

1.  $x_2,\; y_2$ を求めよ．

2.  $x_{n+1}$ を $x_n,\; y_n$ を用いて表せ．また，$y_{n+1}$ を $x_n,\; y_n$ を用いて表せ．

3.  $x_3,\; y_3$ を求めよ．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1990/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 図形 \( Q_1 \)</figcaption>
</figure>