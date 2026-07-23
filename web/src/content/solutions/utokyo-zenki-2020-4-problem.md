---
university: "utokyo"
category: "zenki"
year: "2020"
question: "4"
type: "problem"
title: "UTOKYO 2020 zenki Q4 (problem)"
---

$n$，$k$を，$1 \leqq k \leqq n$を満たす整数とする。$n$個の整数
\[ 2^m  (m=0, \, 1, \, 2, \, \cdots\cdots, \, n-1) \]
から異なる$k$個を選んでそれらの積をとる。
$k$個の整数の選び方すべてに対しこのように積をとることにより得られる
$_nC_k$個の整数の和を$a_{n,k}$とおく。例えば，
\[ a_{4,3}=2^0 \cdot 2^1 \cdot 2^2+2^0 \cdot 2^1 \cdot 2^3+
2^0 \cdot 2^2 \cdot 2^3+2^1 \cdot 2^2 \cdot 2^3=120 \]
である。

1.  2以上の整数$n$に対し，$a_{n,2}$を求めよ。

2.  1以上の整数$n$に対し，$x$についての整式
\[ f_n(x)=1+a_{n,1}x+a_{n,2}x^2+\cdots\cdots+a_{n,n}x^n \]
を考える。
$\displaystyle\frac{f_{n+1}(x)}{f_n(x)}$と
$\displaystyle\frac{f_{n+1}(x)}{f_n(2x)}$を
$x$についての整式として表せ。

3.  $\displaystyle\frac{a_{n+1,k+1}}{a_{n,k}}$を$n$，$k$で表せ。