---
university: "utokyo"
category: "zenki"
year: "2022"
question: "6"
type: "problem"
title: "UTOKYO 2022 zenki Q6 (problem)"
---

$O$を原点とする座標平面上で考える。
0以上の整数$k$に対して，ベクトル$\overrightarrow{v_k}$を
\[ \overrightarrow{v_k}=
\left( \cos\frac{2k\pi}{3}, \, \sin\frac{2k\pi}{3} \right) \]
と定める。投げたとき表と裏がどちらも$\displaystyle\frac{1}{2}$の確率で出るコインを$N$回投げて，
座標平面上に点$X_0, \, X_1, \, X_2, \, \cdots\cdots, \, X_N$を以下の規則(i)，(ii)に従って定める。

1.  $X_0$は$O$にある。

2.  $n$を1以上$N$以下の整数とする。
$X_{n-1}$が定まったとし，$X_n$を次のように定める。

1.  $n$回目のコイン投げで表が出た場合，
\[ \overrightarrow{OX_n}=\overrightarrow{OX_{n-1}}+\overrightarrow{v_k} \]
により$X_n$を定める。ただし，$k$は1回目から$n$回目までのコイン投げで裏が出た回数とする。
[●]$n$回目のコイン投げで裏が出た場合，$X_n$を$X_{n-1}$と定める。

3.  [●]$n$回目のコイン投げで表が出た場合，
\[ \overrightarrow{OX_n}=\overrightarrow{OX_{n-1}}+\overrightarrow{v_k} \]
により$X_n$を定める。ただし，$k$は1回目から$n$回目までのコイン投げで裏が出た回数とする。

4.  [●]$n$回目のコイン投げで裏が出た場合，$X_n$を$X_{n-1}$と定める。

1.  $N=8$とする。$X_8$が$O$にある確率を求めよ。

2.  $N=200$とする。$X_{200}$が$O$にあり，かつ，
合計200回のコイン投げで表がちょうど$r$回出る確率を$p_r$とおく。
ただし$0 \leqq r \leqq 200$である。
$p_r$を求めよ。
また$p_r$が最大となる$r$の値を求めよ。