---
university: "kyodai"
category: "kouki"
year: "2002"
question: "1"
type: "solution"
title: "KYODAI 2002 kouki Q1 (solution)"
---

## 【解】

    Bに1枚だけ入っているのは，$k$枚目に取り出した札だけBに入っている時 ($k=2,3,\dots,n$) である．
    取り出した札の順番を，左から$n$枚の札をならべた列と1対1に対応させて考える。

    Bに入っている札の番号が$l$ ($l=1,2,\dots,n$) の時，他の$n-1$枚のならべ方は
    「$1,2,\dots,l-1,l+1,\dots,n$」の$1$通りだけである．
    $l$はそれより左に並んでいるどれかの数字よりは小さい必要があるから，
    $k$としてありうるのは$k=l+1,l+2,\dots,n$の$n-l$通りである．
    従って，Bに入っている札の番号が$l$である確率$Q(l)$は
    

$$
\begin{align*}
Q(l) = \frac{n-l}{n!}
\end{align*}
$$

    である．

    したがって，求める確率$P(n)$は$Q(l)$を$l$について和を取ったものだから，$n \ge 2$の時，
    

$$
\begin{align*}
P(n)
         & = \sum_{l=1}^{n}\frac{n-l}{n!}\\& = \frac{1}{n!}\sum_{l=0}^{n-1} l \\& = \frac{1}{n!}\frac{(n-1)n}{2}\\& = \frac{1}{2}\frac{1}{(n-2)!}
\end{align*}
$$

    $\cdots$(答)
    

## 【解説】