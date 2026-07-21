---
university: "kyodai"
category: "kouki"
year: "1992"
question: "2"
type: "solution"
title: "KYODAI 1992 kouki Q2 (solution)"
---

## 【解】

### (1)

  題意の立方体は[図1](#1992-2:fig:1)である．
  

<figure id="1992-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1992/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 立方体の様子</figcaption>
</figure>

  題意の場合の数は展開図ADRQ([図2](#1992-2:fig:2))において，AからRへ行く最短経路に等しい．

  

<figure id="1992-2:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1992/2/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 展開図ADRQの様子</figcaption>
</figure>

  全体の移動回数は$3n$回であり，そのうちどのタイミングでAD方向に動くかを決めれば良いので，
  求める場合の数は
  
$$
\begin{align*}
_{3n}C_n = \frac{3n!}{n!2n!}
\end{align*}
$$

  通りである．  $\cdots$(答)

### (2)

  どの辺を通って$R$へ辿り着くかで場合分けする．
  頂点を通る場合は重複があるため，最後にそのような場合の数を差し引くこととする．
  まず，辺に関する場合わけは，以下の六通りである．

  \begin{itemize}
    \item 辺PQを通ってRへ行く事象: $\alpha$ \\
    \item 辺QBを通ってRへ行く事象: $\beta$    \\
    \item 辺BCを通ってRへ行く事象: $\gamma$   \\
    \item 辺CDを通ってRへ行く事象: $\delta$   \\
    \item 辺DSを通ってRへ行く事象: $\epsilon$ \\
    \item 辺SPを通ってRへ行く事象: $\omega$
  \end{itemize}
  従って，求める場合の数は
  
$$
\begin{align}
N = n(\alpha\cup\beta\cup\delta\cup\epsilon\cup\omega) \label{1992-2:eq:1}
\end{align}
$$

  である．(1)と対称性から，
  
$$
\begin{align}
n(\alpha) = n(\beta) = \cdots = {}_{3n}C_n \label{1992-2:eq:2}
\end{align}
$$

  である．

  次に，二つの事象を同時に満たす（頂点を通る）ような場合の数を考える．
  対称性から，AからQを経由してRへ辿り着くルートを考えると，AからQへ行くのに${}_{2n}C_n$通り，QからRへは辺を通っていく一通りだから，
  結局場合の数は${}_{2n}C_n$通りである．従って
  
$$
\begin{align}
n(\alpha\cap\beta) = n(\beta\cap\gamma) = \cdots = {}_{2n}C_n \label{1992-2:eq:3}
\end{align}
$$

  である．このようなケースはAとR以外の頂点の数の分，六通りある．

  三つ以上の事象を同時に満たすような場合は存在しないので，
  以上$\eqref{1992-2:eq:1,1992-2:eq:2,1992-2:eq:2,1992-2:eq:3}$から
  求める場合の数は
  
$$
\begin{align*}
N
     & = 6 n(\alpha) -6 n(\alpha\cap\beta)    \\& =6 \cdot{}_{3n}C_n - 6 \cdot{}_{2n}C_n
\end{align*}
$$

  である． $\cdots$(答)

  
  

## 【解説】