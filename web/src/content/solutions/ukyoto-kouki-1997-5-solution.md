---
university: "ukyoto"
category: "kouki"
year: "1997"
question: "5"
type: "solution"
title: "UKYOTO 1997 kouki Q5 (solution)"
---

## 【解】

  初期状態で青のカード$a$枚，赤のカード$b$枚，黄のカードが$c$枚であるとする．
  この時，$k$回目に青のカードをとり出す確率を$Q_k$とする．
  $Q_{k+1}$について，$k+1$回目にとり出すカードが$k$回目に加えたものか否かで場合分けする．
  $k$回目が終わった時点で，カードは全部で$a+b+c+k$枚存在する．
  $k+1$回目に引くカードが$k$回目に加えたものであるとき，それが青である確率は$Q_k$である．
  $k+1$回目に引くカードが$k$回目に加えたものでないとき，それら$a+b+c+k-1$枚から青を引く確率は$Q_k$である．
  従って，漸化式は
  

$$
\begin{align*}
Q_{k+1}& = \frac{1}{a+b+c+k} Q_k + \frac{a+b+k-1}{a+b+c+k} Q_k \\& = Q_k                                                 \\
\end{align*}
$$

  である．
  この漸化式をくり返し用いて，任意の自然数$n$に対して
  

$$
\begin{align*}
Q_n = Q_1 = \frac{a}{a+b+c}
\end{align*}
$$

  を得る．従って，ここに$(a,b,c)=(3,2,1)$を代入して
  

$$
\begin{align}
Q_n=\frac{1}{2}\label{1997-5:eq:1}
\end{align}
$$

  を得る．

  以下，題意の期待値を求める．
  $n$回目の試行が完了した時の青の個数は，最初の$3$個と，途中で引いた青の数の和に等しい．
  まず，以下のように確率変数$X_k$を定める．
  

$$
\begin{align*}
X_k =
    \begin{dcases}
      1 & (k\text{回目に青を引く})  \\
      0 & (\text{otherwise})
    \end{dcases}
\end{align*}
$$

  [(式1)](#1997-5:eq:1)より，$X_k$の期待値$E(X_k)$は
  

$$
\begin{align*}
E(X_k) = Q_k = \frac{1}{2}
\end{align*}
$$

  である．
  求める期待値$E_n$は
  

$$
\begin{align*}
E_n = 3 + E(X_1+X_2+\cdots+X_n)
\end{align*}
$$

  である．期待値の加法定理から
  

$$
\begin{align*}
E(n)
     & = 3+E(X_1+\dots+X_n)         \\& = 3+\sum_{k=1}^n E(X_k)      \\& = 3+\sum_{k=1}^n \frac{1}{2}\\& = \frac{n}{2}+3
\end{align*}
$$

  が求める答えである．$\cdots$(答)
  
  

## 【解説】