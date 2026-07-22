---
university: "todai"
category: "zenki"
year: "1973"
question: "4"
type: "solution"
title: "TODAI 1973 zenki Q4 (solution)"
---

\input{macros}
     \begin{oframed}
     平面上に$1$辺の長さが$1$の正方形$S$がある．この平面上で$S$を平行移動して得られる正方形で，
     点Pを中心に持つものを$T(\mathrm{P})$とする．このとき，共通部分$S\cap P(\mathrm{P})$の
     面積が$1/2$となるような点Pの存在範囲を図示せよ．またこの範囲の面積を求めよ．
     \end{oframed}

## 【解】

 $S$を，$xy$平面上の
     

$$
\begin{align*}
&|x|\le\frac{1}{2}&|y|\le\frac{1}{2}
\end{align*}
$$

とする．P$(a,b)$とすれば，$T(\mathrm{P})$は
     

$$
\begin{align*}
&|x-a|\le\frac{1}{2}&|y-b|\le\frac{1}{2}
\end{align*}
$$

 
で表される．対称性から，
     

$$
\begin{align}
a,b\ge0\label{0}
\end{align}
$$

で考える．

     \begin{zahyou}[ul=10mm](-1,2)(-1,2)
     \tenretu*{P(0.75,0.75)}
     \YGurafu{0.5}{-0.5}{0.5}
     \YGurafu{-0.5}{-0.5}{0.5}
     \XGurafu{0.5}{-0.5}{0.5}
     \XGurafu{-0.5}{-0.5}{0.5}
     \YGurafu{0.25}{0.25}{1.25}
     \YGurafu{1.25}{0.25}{1.25}
     \XGurafu{0.25}{0.25}{1.25}
     \XGurafu{1.25}{0.25}{1.25}
     \Put\P[s]{P}
     \kuromaru{\P}
     \end{zahyou}

これらが共通部分を持つとき，
     

$$
\begin{align}
&\begin{cases}
          a-1/2\le1/2 \\
          b-1/2\le1/2
          \end{cases}\nonumber\\\Longleftrightarrow&\begin{cases}
          a\le 1 \\
          b\le 1
          \end{cases}\label{1}
\end{align}
$$

が条件で，このもとで長方形領域
     

$$
\begin{align*}
\begin{cases}
          a-1/2\le x\le1/2 \\
          b-1/2\le y\le1/2
          \end{cases}
\end{align*}
$$

が共通部分である．この面積は
     

$$
\begin{align*}
&\left(\frac{1}{2}-\left(a-\frac{1}{2}\right)\right)\left(\frac{1}{2}-\left(b-\frac{1}{2}\right)\right)\\
     =&(1-a)(1-b)
\end{align*}
$$

 である．従って，求める条件は
      

$$
\begin{align}
\frac{1}{2}\le(1-a)(1-b)\label{2}
\end{align}
$$

 である．以上[0](#0)，[1](#1)，[2](#2)からPの存在範囲は下図斜線部(境界含む)．

     \begin{zahyou}[ul=30mm](-0.75,0.75)(-0.75,0.75)
     \def\Fx{1-1/(2-2*X)}
     \def\Gx{-1+1/(2-2*X)}
     \def\Hx{1-1/(2+2*X)}
     \def\Mx{-1+1/(2+2*X)}
     \YGurafu\Fx{0}{0.5}
     \YGurafu\Gx{0}{0.5}
     \YGurafu\Hx{-0.5}{0}
     \YGurafu\Mx{-0.5}{0}
     \YNurii*\Fx\Gx{0}{0.5}
     \YNurii*\Hx\Mx{-0.5}{0}
     \end{zahyou}

 
 従って求める面積$U$は，対称性から
      

$$
\begin{align*}
U&=4\int_0^{1/2}\left(1-\frac{1}{2(1-a)}\right)\,da \\&=4\teisekibun{a+\frac{1}{2}\log |1-a|}{0}{1/2}\\&=2(1-\log 2)
\end{align*}
$$

  
 である．$\cdots$(答)