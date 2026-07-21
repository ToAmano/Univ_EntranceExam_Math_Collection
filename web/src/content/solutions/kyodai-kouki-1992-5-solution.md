---
university: "kyodai"
category: "kouki"
year: "1992"
question: "5"
type: "solution"
title: "KYODAI 1992 kouki Q5 (solution)"
---

## 【解】

### (1)

  操作の途中で$m$より大きい玉を一度でも引けば$Y>m$となる．
  一方途中で引いた玉が全て$m$以下ならば$Y \le m$だから，
  $Y \le m$となる確率は，
  $n$回の試行全てで$m$以下の玉だけを引く確率に等しい．
  常に$m$以下の玉を引いている場合，
  各回の試行で箱の中の$m$以下の玉の数は$m-2$個で一定だから，
  求める確率は
  
$$
\begin{align*}
P(Y \le m) = \left(\frac{m-2}{N}\right)^n
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  $m\ge 3$の時と，$ m = 2$の時で分けて考える．
  まず$m \ge 3$の時から検討する．

### (1)
と同様に考えると，$X\le m$となるのは，
  \begin{itemize}
    \item[A] $n$回の試行全てで$m$以下の玉だけを引く \\
    \item[B] $n$回の試行中に一回だけ$m+1$以上の玉を引く
  \end{itemize}
  のどちらかである．
  (A)は(1)で求めた確率と同じだから，(B)について考える．
  $k(k \le N)$回目に$m+1\, (m \ge 3)$以上の玉を引く確率$q_k$を考えよう．
  この時箱の中の$m$以下の玉の数は$k-1$回目までは$m-2$個，
  $k+1$回目以降は$m-1$個であり，
  $k$回目に引く時の$m+1$以上の玉の数は$N-(m-2)$個だから，
  
$$
\begin{align*}
q_k
     & = \left(\frac{m-2}{N}\right)^{k-1}\left(\frac{N-(m-2)}{N}\right)\left(\frac{m-1}{N}\right)^{n-k}\\& = \frac{(m-1)^{n}}{N^n}\frac{N-m+2}{m-2}\left(\frac{m-2}{m-1}\right)^{k}
\end{align*}
$$

  である．
  従って，これを$k=1,2,\cdots,n$について和をとれば，
  操作中に一回だけ$m+1$以上のカードを引く確率$P(B)$が求まる．
  
$$
\begin{align*}
P(B)
     & = \sum_{k=1}^{n}q_k                                                                                                         \\& = \frac{(m-1)^{n}}{N^n}\frac{N-m+2}{m-2}\sum_{k=1}^{n}\left(\frac{m-2}{m-1}\right)^{k}\\& = \frac{(m-1)^n}{N^n}\frac{N-m+2}{m-2}\cdot\frac{m-2}{m-1}\frac{1 - \left(\frac{m-2}{m-1}\right)^n}{1-\frac{m-2}{m-1}}\\& = (N-m+2) \left(\frac{m-1}{N}\right)^n \left[1- \left(\frac{m-2}{m-1}\right)^n\right]\\& = (N-m+2) \left[\left(\frac{m-1}{N}\right)^n - \left(\frac{m-2}{N}\right)^n \right]
\end{align*}
$$

  したがって(1)とあわせて，求める確率は
  
$$
\begin{align}
P(X \le m)
     & = P(A)+P(B)
     & = P(Y \le m) P(B)                                                                                      \\& = (-N+m-1) \left(\frac{m-2}{N}\right)^n + (N-m+2) \left(\frac{m-1}{N}\right)^n \label{1992-5:eq:1}
\end{align}
$$

  である．

  次に$m=2$の時，求める確率は初回に任意の玉を引いた後，$2$回目以降全て$1$を引く確率であるから，
  
$$
\begin{align*}
P(X\le 2) = \left(\frac{1}{N}\right)^{n-1}
\end{align*}
$$

  となる．
  これは$\eqref{1992-5:eq:1}$で$m=2$としたものに一致するから，
  $m\ge 2$の全ての場合で$\eqref{1992-5:eq:1}$の表現でよく，
  求める確率は
  
$$
\begin{align*}
P(X \le m) = (-N+m-1) \left(\frac{m-2}{N}\right)^n + (N-m+2) \left(\frac{m-1}{N}\right)^n
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】