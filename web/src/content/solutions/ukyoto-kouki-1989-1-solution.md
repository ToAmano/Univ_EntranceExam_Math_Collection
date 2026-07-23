---
university: "ukyoto"
category: "kouki"
year: "1989"
question: "1"
type: "solution"
title: "UKYOTO 1989 kouki Q1 (solution)"
---

## 【解】

    (1)
    題意より，互いに素な奇数$a',b'$を用いて
    

$$
\begin{align*}
a & = a'd \\
        b & = b'd
\end{align*}
$$

    とおける．与式に代入して
    

$$
\begin{align*}
m & = d(11a'+b') \\
        h & = d(3a'+b')
\end{align*}
$$

    以下，$A=11a'+b'$, $B=3a'+b'$ の最大公約数を求める．
    数$l,m$の最大公約数を$(l,m)$で表すと，ユークリッドの互除法から
    

$$
\begin{align*}
(A,B)
         & =  (A-B,B)      \\& = (8a', 3a'+b')
\end{align*}
$$

    である．
    $a', b'$ が互いに素だから，$(a', 3a'+b') = 1$ なので，
    

$$
\begin{align*}
(A,B) = (8,3a'+b')
\end{align*}
$$

    となり，$(A,B)$ は$8$の約数，つまり$1,2,4,8$のいずれかである．
    ここで，$a',b'$が奇数だから $3a'+b'$ は偶数である．
    従って，少なくとも$(A,B)$ は$2$を因数に持ち，偶数となる．
    よって$1$はありえず
    

$$
\begin{align*}
(A,B) = 2,4,8
\end{align*}
$$

    となる．従って
    

$$
\begin{align*}
(m,n) = 2d, 4d, 8d
\end{align*}
$$

    となり，題意は示された．$\cdots$(答)

    
    (2)
    $m,n$ が共に平方数だと仮定して，背理法により証明する．
    この時，自然数$\alpha,\beta$があって
    

$$
\begin{align}
\begin{dcases}
            m & = \alpha^2 \\
            n & = \beta^2
        \end{dcases}\label{1989-1:eq:1}
\end{align}
$$

    とおける．与式を逆に解いて
    

$$
\begin{align}
a & = \frac{m-n}{8}\\
        b & = \frac{11n-3m}{8}\label{1989-1:eq:2}
\end{align}
$$

    だから，[(式1)](#1989-1:eq:1)を代入して
    

$$
\begin{align*}
a =\frac{(A+B)(A-B)}{8}
\end{align*}
$$

    となる．
    $A+B, A-B$ の偶奇が一致すること，$a \in \text{odd}$ であることから $p,q \in \text{odd}$ として，
    $A+B,A-B$のとりうる値は
    

$$
\begin{align*}
(A+B, A-B) = (4p, 2q) \quad\text{or}\quad(2p, 4q)
\end{align*}
$$

    のふた通りである．
    

\begin{enumerate}
[]
        \item $(A+B, A-B) = (4p, 2q)$の時

              $A= 2p+q, B = 2p-q$ を[(式2)](#1989-1:eq:2)に代入して
              

$$
\begin{align*}
b & = \frac{1}{8}[11(2p-q)^2 - 3(2p+q)^2]\\& = \frac{1}{8}[32p^2-56pq + 8q^2]\\& = 4p^2-7pq+q^2
\end{align*}
$$

              となるが，$p,q$が奇数だから右辺は偶数であり，$b$が奇数であることに矛盾する．
        \item $(A+B, A-B) = (2p, 4q)$の時

              $A= p+2q, B = p-2q$ を[(式2)](#1989-1:eq:2)に代入して
              

$$
\begin{align*}
b & = \frac{1}{8}[11(p-2q)^2 - 3(p+2q)^2]\\& = \frac{1}{8}[8p^2 - 56pq + 32q^2]\\& = p^2-7pq+4q^2
\end{align*}
$$

              となるが，$p,q$が奇数だから右辺は偶数であり，$b$が奇数であることに矛盾する．
\end{enumerate}

    以上いずれの場合も矛盾するから，背理法により$m,n$がともに平方数であることはない．$\cdots$(答)

    
    

## 【解説】