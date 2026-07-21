---
university: "titech"
category: "kouki"
year: "2006"
question: "2"
type: "solution"
title: "TITECH 2006 kouki Q2 (solution)"
---

## 【解】

  自然数$a,b,c$に対して
  
$$
\begin{align}
\begin{dcases}
      3a & =b^3 \\
      5a & =c^2
    \end{dcases}\label{2006-2:eq:1}
\end{align}
$$

  とおく．

### (1)

  $\eqref{2006-2:eq:1}$および$3,5$は素数であることから，$b,c$は各々$3,5$でわり切れる．
  したがって，$b'=\frac{1}{3}b$, $c'=\frac{1}{5}c ( \in \mathbb{N} )$として
  $\eqref{2006-2:eq:1}$に代入して
  
$$
\begin{align}
\begin{dcases}
      a & =9b'^3 \\
      a & =5c'^2
    \end{dcases}\label{2006-2:eq:2}
\end{align}
$$

  と書ける．従って$a$は$3^25^1$でわり切れる． $\cdots$(答)

### (2)

  背理法を用いて示す．
  $a$の素因数として,$3,5$以外の素数 $p \in \mathbb{N}_{\ne 1}$ があると仮定する．
  すると(1)と同様に，$\eqref{2006-2:eq:1}$から
  
$$
\begin{align*}
a & =p a'   \\
    b & =3p b'' \\
    c & =5p c''
\end{align*}
$$

  なる $a',b'',c'' \in \mathbb{N}$が存在する．
  $\eqref{2006-2:eq:1}$に代入すると
  
$$
\begin{align}
a'=9p^2b''^3 = 5pc''^2 \label{2006-2:eq:3}
\end{align}
$$

  である．

  したがって，$a'$が$p^2$でわり切れるので，$a'=p^{2}a''$ なる$a'' \in \mathbb{N}$が存在する．
  これを$\eqref{2006-2:eq:3}$に代入して
  
$$
\begin{align*}
a''=9b''^3 = \frac{5 c''^2}{p}
\end{align*}
$$

  を得る．$5c''^2/p$が整数であるためには，$p$が$5$と互いに素であることから，
  $c''$が$p$を因数に持って，
  
$$
\begin{align*}
c'' = p c'''
\end{align*}
$$

  なる$c'''\in\mathbb{N}$がある．$\eqref{2006-2:eq:3}$に代入すると，
  
$$
\begin{align*}
a''=9b''^3 = 5pc'''^2
\end{align*}
$$

  $p$は$9$と互いに素だから，$b''$は$p$を因数に持つ．
  従って$a''$が$p^3$を因数に持つ．
  $a=p^{3}a''$だったから，結局$a$が$p^6$を因数に持つ．

  一方，題意から$\alpha^t$ ($t \in \mathbb{N}_{\ge 6}$)の形の素因数$a$はもたない．
  これは矛盾．従って背理法より，$p=1,3,5$となり，題意は示された． $\cdots$(答)

### (3)

### (1)
, (2)から，$a=3^k \cdot 5^l$ ($k,l \in \mathbb{N}$) とおける．
  ただし(1)の結果および題意の条件より
  
$$
\begin{align}
\begin{dcases}
      2 \le k \le 5 \\
      1 \le l \le 5
    \end{dcases}\label{2006-2:eq:4}
\end{align}
$$

  である．
  $\eqref{2006-2:eq:2}$に代入して
  
$$
\begin{align}
a = 3^k \cdot 5^l = 9 \cdot b'^3 = 5 \cdot c'^2\label{2006-2:eq:6}
\end{align}
$$

  だから，$b'$および$c'$も同じく$3,5$のみ素因数にもち，
  
$$
\begin{align*}
b'=3^n \cdot 5^m, \\
    c'=3^x \cdot 5^y, \\
    n,m,x,y \in\mathbb{Z}_{\ge 0}
\end{align*}
$$

  と書ける．
  $\eqref{2006-2:eq:6}$に代入して
  
$$
\begin{align*}
3^k \cdot 5^l = 3^{3n+2}\cdot 5^{3m} = 3^{2x}\cdot 5^{2y+1}\\\therefore\begin{cases}
      k=3n+2=2x \\
      l=3m=2y+1
    \end{cases}
\end{align*}
$$

  である．
  これをみたす$(k,l)$は$\eqref{2006-2:eq:4}$の条件では
  $(k,l)=(2,3)$のみであり，この時
  
$$
\begin{align*}
a=3^2 \cdot 5^3 = 1125
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】

  東工大後期では珍しい純粋な整数問題．

### (1)
も(2)も肝となるのは，$a$がある数$p$を因数に持った場合，
  $b$や$c$も$p$を因数としてもち，結果として$b^3$や$c^2$と紐づく$a$は$p^3$や$p^2$を因数に持たないといけない，という事実である．

  この点を少し具体的に書くと，$a$を素因数分解して
  
$$
\begin{align*}
a = 2^{p_2}3^{p_3}5^{p_5}7^{p_7}\cdots n^{a_n}\cdots
\end{align*}
$$

  と書けたとする．$3a$が$b^3$で書けないといけないので，
  
$$
\begin{align*}
3a = 2^{p_2}3^{p_3+1}5^{p_5}7^{p_7}\cdots n^{a_n}\cdots
\end{align*}
$$

  において，
  
$$
\begin{align}
& p_2, p_3+1, p_5,\cdots, p_n \cdots\equiv 0 & (\mod 3) \label{2006-2:eq:7}
\end{align}
$$

  でないといけない．

  同様に$5a$が$c^2$で書けないといけないので，
  
$$
\begin{align*}
5a = 2^{p_2}3^{p_3}5^{p_5+1}7^{p_7}\cdots n^{a_n}\cdots
\end{align*}
$$

  において
  
$$
\begin{align}
& p_2, p_3, p_5+1,\cdots, p_n \cdots\equiv 0 & (\mod 2) \label{2006-2:eq:8}
\end{align}
$$

  でないといけない．

  以上$\eqref{2006-2:eq:7,2006-2:eq:8}$および$2$と$3$が互いに素なので$p_3,p_5$以外について
  
$$
\begin{align*}
& p_2,p_7,\cdots, p_n,\cdots\equiv 0 & (\mod 6)
\end{align*}
$$

  でないといけない．
  題意の条件より$p_n < 6$だから，これを満たすのはこれらが全て$0$の場合である．
  これが(2)である．

  残りの$p_3,p_5$は
  
$$
\begin{align*}
\begin{dcases}
      p_3+1 \equiv 0 & (\mod 3) \\
      p_5   \equiv 0 & (\mod 3) \\
      p_3   \equiv 0 & (\mod 2) \\
      p_5+1 \equiv 0 & (\mod 2)
    \end{dcases}
\end{align*}
$$

  を満たす．このうち$p_3,p_5 < 6$を満たすのは$p_3=2,p_5=3$のみであり，これが(1)(3)である．