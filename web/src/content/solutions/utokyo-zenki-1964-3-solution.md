---
university: "utokyo"
category: "zenki"
year: "1964"
question: "3"
type: "solution"
title: "UTOKYO 1964 zenki Q3 (solution)"
---

\input{macros}
     \begin{oframed}
     点$V$を頂点とし，正方形$ABCD$を底面とする四角錐$V\cdot ABCD$があって，その$4$側面
     はいずれも底辺$20 \,\mathrm{cm}$，高さ$40\,\mathrm{cm}$の二等辺三角形である．
     
     辺$VA$上に$VP:PA=3:1$なる点$P$をとり，$3$点$P$，$B$，$C$を通る平面でこの四角錐を切る
     とき，切り口の面積を求めよ．
     \end{oframed}

## 【解】

辺$VD$上に$VQ:QD=3:1$なる点$Q$をとると，切り口は台形$PBCQ$となる．相似から
$PQ=\dfrac{3}{4}AB=15 \,\mathrm{cm}$である．また$AD$，$BC$の中点を$M$，$N$として
$\triangle VMN$で立体を切断すると右のようになる．ただし$R$は$PQ$の中点である．
ここで$\triangle VMN$に余弦定理を用いて
     \[\cos \angle RMN=\frac{1}{4}\]
だから，$\triangle MNR$に余弦定理を用いて
     \[RN=\sqrt{(10)^2+(20)^2-100}=20 \,\mathrm{cm}\]
である．対称性から$RN$は台形の高さであるから，求める面積は
     

$$
\begin{align*}
\frac{1}{2}|RN|(|PQ|+|BC|)&=\frac{1}{2}20(15+20) \\&=350 \,\mathrm{cm^2}
\end{align*}
$$

である．$\cdots$(答)

図が欲しい