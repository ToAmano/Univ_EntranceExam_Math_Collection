---
university: "sample_todai"
category: "zenki"
year: "1994"
question: "2"
type: "problem"
title: "SAMPLE_TODAI 1994 zenki Q2 (problem)"
---

一辺の長さが $l$ の正方形の内部に半径 $1$ の円が入っている．ここで $l > 2$ とする．

この円が図のように正方形の角から出発して正方形の辺にそってすべらずに正方形の内部
をころがる．ただし円が正方形の他の辺に接すればすぐにはその辺にそってすべらずにころ
がるとする．この円の中心が最初にもとの位置にもどってくるまでの円周上の点 $P$ の軌
跡を考える．

\begin{enumerate}
  \item[(1)] $P$ の軌跡の始点と終点が一致するための $l$ の条件を求めよ．
  \item[(2)] $l$ は (1) の条件を満たす最小の長さとする．このとき $P$ の軌跡の長さのとりうる値
        の範囲を求めよ．
\end{enumerate}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}[scale=1.2]
    \draw (0,0) rectangle (4,4);

    \draw (1,1) circle (1);

    \draw[<->] (0,-0.5) -- (4,-0.5) node[midway, below] {$l$};

    \draw (1,1) -- (1.707,1.707);
    \fill (1.707,1.707) circle (0.07) node[above right] {$P$};
    \draw[-{Stealth[length=2mm]}] (1.5,1.8) arc (45:135:0.4);
  \end{tikzpicture}
\end{figure}