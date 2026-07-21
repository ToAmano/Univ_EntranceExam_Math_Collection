---
university: "kyodai"
category: "kouki"
year: "2004"
question: "5"
type: "solution"
title: "KYODAI 2004 kouki Q5 (solution)"
---

## 【解】

  まず，$n=1$の時は(1)を満たすことができず$0$通りである．
  従って以下$n\ge 2$で考える．

### (1)
をみたす条件で，$a,d$を固定すると，$b,c$共に$d-a$ずつ値を取りうる．したがって，求める場合の数は
  \[ S = \sum_{1 \le a < d \le n} (d-a)^2 \]
  である．$d-a = k$と固定すると，$k$の取りうる領域は
  
$$
\begin{align*}
1 \le k \le n-1
\end{align*}
$$

  である．
  この時，$(a,d)$の組は$a$を決めれば$d$も勝手に定まるから，
  
$$
\begin{align*}
a=1,2,\dots,n-k
\end{align*}
$$

  の$n-k$通りである．
  したがって，$k$を固定した時の$(a,b,c,d)$の組は$k^2(n-k)$であるから，
  求める場合の数$S(n)$は
  
$$
\begin{align*}
S(n)
     & = \sum_{k=1}^{n-1} k^2(n-k)                        \\& = \sum_{k=1}^{n-1}(-k^3+nk^2)                     \\& = -\frac{1}{4}n^2(n-1)^2 + \frac{n}{6}(n-1)n(2n-1) \\& = \frac{1}{12}n^2(n-1)[2(2n-1)-3(n-1)]\\& = \frac{1}{12}n^2(n-1)(n+1) \quad\text{通り}
\end{align*}
$$

  である．
  これは$n=1$の時の0通りにも対応している．よって求める答えは
  
$$
\begin{align*}
S(n) = \frac{1}{12}n^2(n-1)(n+1) \quad\text{通り}
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】