---
university: "utokyo"
category: "zenki"
year: "1968"
question: "5"
type: "solution"
title: "UTOKYO 1968 zenki Q5 (solution)"
---

\input{macros}
     \begin{oframed}
     整数を係数とする次数$3$の多項式$P(x)$で，次の条件を満たすものを求めよ．
          

1.  

2.  $P(x)$のグラフは原点に関して対称である．

3.  $P(x)=0$は重根を持たない．

4.  $P(x)$は極大値も極小値も持たない．

5.  $P\left(\dfrac{1}{2}\right)$は整数である．

6.  $0<P(1)<6$である．

     \end{oframed}

## 【解】

条件(1)から，$P(x)$は奇関数であるから，$a,b\in\mathbb{R}$として
$P(x)=ax^3+bx$とおける．ただし$a\not=0$である．さらに条件(2)から，$b\not=0$が従う．
($b=0$なら重根$x=0$を持つ．)さらに条件(3)から$P'(x)=3ax^2+b$の符号が入れ替わらなければよい．言い換えれば常に非負か，常に非正であればよい．然るに$P'(0)=b$及び$x\to\infty$の極限を考えることで，$a,b$の符号が一致していなければならない($\because ab\not=0$)．つまり$ab>0$である．

次に(4)から
      

$$
\begin{align}
&P\left(\frac{1}{2}\right)=\frac{a+4b}{8}\in\mathbb{Z}\nonumber\\\Longleftrightarrow&a+4b=8k(k\in\mathbb{Z})\label{1}
\end{align}
$$

となる．以上に加えて条件(5)から$0<a+b<6$である．$a,b\in\mathbb{Z}$及び$ab>0$からあり得る
$(a,b)$の候補は
     

$$
\begin{align*}
(1,1),(1,2),(1,3),(1,4),(2,1)  \\(2,2),(2,3),(3,1),(3,2),(4,1)
\end{align*}
$$

のみであるが，このうち
[1](#1)を満たすのは$(a,b)=(4,1)$のみである．故に求めるのは$P(x)=4x^3+x\cdots$(答)である．