---
university: "utokyo"
category: "zenki"
year: "2014"
question: "2"
type: "problem"
title: "UTOKYO 2014 zenki Q2 (problem)"
---

$a$を自然数（すなわち1以上の整数）の定数とする。\\
　白球と赤球があわせて1個以上入っている袋$U$に対して，
次の操作（＊）を考える。\\
（＊）袋$U$から球を1個取り出し，

\begin{enumerate}
\item取り出した球が白球のときは，袋$U$の中身が白球$a$個，赤球1個となるようにする。
  \item取り出した球が赤球のときは，その球を袋$U$へ戻すことなく，袋$U$の中身はそのままにする。
\end{enumerate}

　はじめに袋$U$の中に，白球が$a+2$個，赤球が1個入っているとする。
この袋$U$に対して操作（＊）を繰り返し行う。\\
　たとえば，1回目の操作で白球が出たとすると，袋$U$の中身は白球$a$個，赤球1個となり，
さらに2回目の操作で赤球が出たとすると，袋$U$の中身は白球$a$個のみとなる。\\
　$n$回目に取り出した球が赤球である確率を$p_n$とする。
ただし，袋$U$の中の個々の球の取り出される確率は等しいものとする。

\begin{enumerate}
\item$p_1$，$p_2$を求めよ。
  \item$n\geqq3$に対して$p_n$を求めよ。
  \item$\displaystyle\lim_{m\to\infty}\frac{1}{m}\sum_{n=1}^mp_n$を求めよ。
\end{enumerate}