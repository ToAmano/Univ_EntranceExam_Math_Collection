---
university: "utokyo"
category: "zenki"
year: "1965"
question: "6"
type: "solution"
title: "UTOKYO 1965 zenki Q6 (solution)"
---

\input{macros}
     \begin{oframed}
     下の図は半径の長さ$1$の半円で，弦$AP$，$AQ$と直径$AB$のつくる角はそれぞれ$30^\circ$，$60^\circ$である．
     
     このとき，弦$AP$，$AQ$と円弧$PQ$とで囲まれる部分を直径$AB$のまわりに一回転して得られる立体の体積を求めよ． 
          
          \scalebox{1}{\input{ut-65-6p1}}
          
     \end{oframed}

## 【解】

 $A(-1,0)$，$B(1,0)$となるように$xy$座標をおく．すると原点$O$がこの半円の中心である．故に$\angle AOQ=\pi/3$，
$\angle AOP=2\pi/3$である．$P$，$Q$から$x$軸に下ろした垂足を，$L$，$H$とする．
     
     \scalebox{1}{\input{ut-65-6p2}}
     
このとき，求める体積$V$として
     

$$
\begin{align*}
V_1&=(\triangle AQH\text{の回転体}) \\
     V_2&=(PQHL\text{の回転体}) \\
     V_3&=(\triangle APL\text{の回転体})
\end{align*}
$$

とおけば，
     

$$
\begin{align}
V=V_1+V_2-V_3\label{1}
\end{align}
$$

である．各項計算して，
     

$$
\begin{align*}
V_1&=\frac{1}{3}\frac{1}{2}\frac{3}{4}\pi=\frac{1}{8}\pi\\
     V_2&=\int_{-1/2}^{1/2}\pi(1-x^2)dx=\frac{11}{12}\pi\\
     V_3&=\frac{1}{3}\frac{2}{3}\frac{3}{4}\pi=\frac{3}{8}\pi
\end{align*}
$$

これらを[1](#1)に代入して
     

$$
\begin{align*}
V=\left(\frac{1}{8}+\frac{11}{12}-\frac{3}{8}\right)\pi=\frac{2}{3}\pi
\end{align*}
$$

である．$\cdots$(答)