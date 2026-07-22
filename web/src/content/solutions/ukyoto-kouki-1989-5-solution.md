---
university: "ukyoto"
category: "kouki"
year: "1989"
question: "5"
type: "solution"
title: "UKYOTO 1989 kouki Q5 (solution)"
---

## 【解】

    以下，
    

$$
\begin{align*}
n \ge 3 \cdots\textcircled{1}
\end{align*}
$$

    のもので考える．
    A君の得点を$X_A$，B君の得点を$X_B$とする．
    A君の得点が$k$となる確率$P_A(X_A=k)$は，全体の場合の数${}_nC_2$通りのうち，
    一枚が$k$，もう一枚が$k-1$以下になる場合の数からもとまり，
    

$$
\begin{align*}
P_A(X_A=k)
         & = \frac{k-1}{{}_nC_2} = \frac{k-1}{\frac{n(n-1)}{2}}\\& = \frac{2(k-1)}{n(n-1)}
\end{align*}
$$

    である．

    一方，B君の得点が$k$点となる確率$P_B(X_B=k)$は，全体の場合の数$n^2$通りのうち，
    二枚とも$k$以下のカードを引く場合の数から2枚とも$k-1$以下のカードを引く場合の数を差し引いたもので，
    

$$
\begin{align*}
P_B(X_B=k)
         & = \frac{k^2 - (k-1)^2}{n^2}\\& = \frac{2k-1}{n^2}
\end{align*}
$$

    である．この導出からわかるように，B君が$k$点以下をとる確率は
    

$$
\begin{align*}
P_B(X_B\le k) & = \frac{k^2}{n^2}
\end{align*}
$$

    である．

    これらは互いに独立であることから，A君が勝つ確率$p$は，A君の得点がB君よりも高いことで，
    

$$
\begin{align}
p
         & = \sum_{k=2}^n P_A(X_A=k) \cdot P_B(X_B\le k-1)                \\& = \sum_{k=2}^n \frac{2(k-1)}{n(n-1)}\cdot\frac{(k-1)^2}{n^2}\\& = \sum_{k=1}^{n-1}\frac{2k}{n(n-1)}\cdot\frac{k^2}{n^2}\\& = \frac{2}{n^3(n-1)}\sum_{k=1}^{n-1} k^3  \label{1989-5:eq:1}
\end{align}
$$

    と計算できる．

    ここで和の公式から
    

$$
\begin{align*}
\sum_{k=1}^{n} k^3 & = \left\{\frac{n(n+1)}{2}\right\}^2
\end{align*}
$$

    だから，[(式1)](#1989-5:eq:1)に代入して
    

$$
\begin{align}
p
         & = \frac{2}{n^3(n-1)}\sum_{k=1}^{n-1}\left\{\frac{n(n-1)}{2}\right\}^2 \\& = \frac{n-1}{2n}\label{1989-5:eq:2}
\end{align}
$$

    である．

    次に，B君の勝つ確率Qを考える．勝ち負けはA君が勝つかB君が勝つか引き分けしかないから，
    引き分けとなる確率Rとして
    

$$
\begin{align}
& p+q+r=1                        \\\therefore& q = 1 -p-r \label{1989-5:eq:3}
\end{align}
$$

    だから，$r$を求めれば$q$が求まる．

    同点である確率Rは
    

$$
\begin{align*}
r
         & = \sum_{k=1}^n P_A(X_A=k) \cdot P_B(X_B=k)                                    \\& = \sum_{k=1}^n \frac{2(k-1)}{n(n-1)}\cdot\frac{2k-1}{n^2}\\& = \frac{1}{n^3(n-1)}\sum_{k=1}^n (2k-2)(2k-1)                                 \\& = \frac{1}{n^3(n-1)}\sum_{k=1}^n (4k^2-6k+2)                                  \\& = \frac{1}{n^3(n-1)}\left[\frac{4}{6}n(n+1)(2n+1)-6\frac{n(n+1)}{2}+2n\right]\\& = \frac{1}{3n^3(n-1)}\left[2n(n+1)(2n+1)-9n(n+1)+6n\right]\\& = \frac{1}{3n^3(n-1)} n(4n+1)(n-1)                                            \\& = \frac{4n+1}{3n^2}
\end{align*}
$$

    であるから，[(式2,3)](#1989-5:eq:2,3)より
    

$$
\begin{align*}
p-q
         & = p-(1-p-r)                            \\& = 2p+r-1                               \\& = \frac{n-1}{n} + \frac{4n+1}{3n^2} -1 \\& = \frac{3n(n-1)+4n+1-3n^2}{3n^2}\\& = \frac{n+1}{3n^2}\\& > 0                                    \\\therefore& p > q
\end{align*}
$$

    だから，A君が勝つ確率の方が大きい．$\cdots$(答)

    
    

## 【解説】

    B君の取り方だと，二回目に同じカードを引くことがある分，A君の方が得点が高そうというのが直感的な理解だが，
    実際に計算してみてもその通りになる，ということである．
    実際のところ$P_A(X_A=k)$と$P_B(X_B=k)$を比較してみると
    

$$
\begin{align*}
P_A(X_A=k)-P_B(X_B=k)
         & = \frac{2k-2}{n(n-1)} - \frac{2k-1}{n^2}\\& = \frac{(2k-2)n-(2k-1)(n-1)}{n^2(n-1)}\\& = \frac{2k-n-1}{n^2(n-1)}\\
\end{align*}
$$

    だから，これは$k$が大きいところで正，すなわちA君の方が大きい$k$をとる確率が高い，ということを表している．
    このことがわかっていれば，$p$や$q$の和の計算を見通しよく進めることができるだろう．

    ちなみに，解答中では$q$の代わりに引き分けとなる確率$r$の方を計算したが，
    もちろん直接$q$を計算することもできるので以下計算例を示しておこう．
    本解答と同様に，まずA君が$k$点以下をとる確率は，
    

$$
\begin{align*}
P_A(X_A \le k)
         & = \frac{{}_{k}C_2}{{}_nC_2}\\& = \frac{k(k-1)}{n(n-1)}
\end{align*}
$$

    だから，
    

$$
\begin{align*}
q
         & = \sum_{k=2}^n P_B(X_B=k) \cdot P_A(X_A \le k-1)          \\& = \sum_{k=2}^n \frac{2k-1}{n^2}\frac{(k-1)(k-2)}{n(n-1)}\\& = \frac{1}{n^3(n-1)}\sum_{k=1}^n (2k+1)k(k-1)
\end{align*}
$$

    となる．

    ここで和の公式から
    

$$
\begin{align*}
\sum_{k=1}^{n} k^3 & = \left\{\frac{n(n+1)}{2}\right\}^2 \\\sum_{k=1}^{n} k^2 & = \frac{1}{6}n(n+1)(2n+1)
\end{align*}
$$

    だから，これを代入して
    

$$
\begin{align*}
q
         & =  \frac{1}{n^3(n-1)}\left[2\left\{\frac{n(n-1)}{2}\right\}^2 - \frac{1}{6}n(n-1)(2n-1) - \frac{n(n-1)}{2}\right]\\& =  \frac{n(n-1)}{6n^3(n-1)}\left[3n(n-1) - (2n-1) - 3\right]\\& =  \frac{n(n-1)}{6n^3(n-1)}(3n+1)(n-2)                                                                             \\& =  \frac{(3n+1)(n-2)}{6n^2}\\& =  \frac{3n^2-5n-2}{6n^2}
\end{align*}
$$

    と求めることができる．
    導出を比較すると$r$の計算の方が簡単なため，気づけばこういう時間短縮のテクニックを使っていきたい．

    

$$
\begin{align*}
\sum_{k=2}^n k(k-1)(k-2)
                                & = \frac{1}{4}(n+1)n(n-1)(n-2) \\\sum_{k=2}^n (k-1)(k-2) & = \frac{1}{3} n(n-1)(n-2)
\end{align*}
$$