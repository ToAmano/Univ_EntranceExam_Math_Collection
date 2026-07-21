---
university: "todai"
category: "zenki"
year: "1961"
question: "4"
type: "solution"
title: "TODAI 1961 zenki Q4 (solution)"
---

\input{macros}
     \begin{oframed}
     $\triangle ABC$の$3$辺$BC$，$CA$，$AB$の上にそれぞれ点$L$，$M$，$N$をとり
          \[\frac{BL}{LC}=\frac{CM}{MA}=\frac{AN}{NB}=\frac{1}{2}\]
     となるようにする.
     $AL$と$CN$の交点を$P$，$AL$と$BM$の交点を$Q$，$BM$と$CN$の交点を$R$とするとき，$\triangle PQR$の面積と
     $\triangle ABC$の面積との比を求めよ．
     \end{oframed}

## 【解】

 $\triangle ABL$と$CN$にメラネウスを用いて
     
$$
\begin{align}
&\frac{NB}{AN}\frac{CL}{BC}\frac{BA}{LP}=1\nonumber\\&\frac{PA}{LP}=\frac{3}{4}\label{1}
\end{align}
$$

対称性から(詳しくはメラネウスを各三角形に用いることで)
     
$$
\begin{align}
LQ:QP:PA=NP:PR:RC\nonumber\\
     =MR:RQ:QB=a:b:c\label{2}
\end{align}
$$

とおけることに注意して，$\triangle CPL$と$BR$にメラネウスを用いて
     
$$
\begin{align}
\frac{RP}{CR}\frac{QL}{PQ}\frac{BC}{LB}=1 \nonumber\\\frac{a}{c}=\frac{1}{3}\label{3}
\end{align}
$$
   
一方\eqref{1}，\eqref{2}から，
     
$$
\begin{align}
a+b:c=4:3 \label{4}
\end{align}
$$
  
\eqref{3}，\eqref{4}から
     \[a:b:c=1:3:3\]
であるから，
     \[\triangle PQR=\frac{2}{3}\frac{3}{7}\frac{1}{2}\triangle ABC=\frac{1}{7}\triangle ABC\]     
であるy．$\cdots$(答)