---
university: "utokyo"
category: "zenki"
year: "2013"
question: "3"
type: "problem"
title: "UTOKYO 2013 zenki Q3 (problem)"
---

$A$，$B$の2人がいる。
投げたとき表裏の出る確率がそれぞれ$\displaystyle\frac{1}{2}$のコインが1枚あり，
最初は$A$がそのコインを持っている。次の操作を繰り返す。

\begin{enumerate}
\item$A$がコインを持っているときは，コインを投げ，表が出れば$A$に1点を与え，コインは$A$がそのまま持つ。
裏が出れば，両者に点を与えず，$A$はコインを$B$に渡す。
  \item$B$がコインを持っているときは，コインを投げ，表が出れば$B$に1点を与え，コインは$B$がそのまま持つ。
裏が出れば，両者に点を与えず，$B$はコインを$A$に渡す。
\end{enumerate}

　そして$A$，$B$のいずれかが2点を獲得した時点で，2点を獲得した方の勝利とする。
たとえば，コインが表，裏，表，表と出た場合，この時点で$A$は1点，$B$は2点を獲得しているので$B$の勝利となる。

\begin{enumerate}
\item$A$，$B$あわせてちょうど$n$回コインを投げ終えたときに$A$の勝利となる確率$p(n)$を求めよ。
  \item$\displaystyle\sum_{n=1}^\infty p(n)$を求めよ。
\end{enumerate}