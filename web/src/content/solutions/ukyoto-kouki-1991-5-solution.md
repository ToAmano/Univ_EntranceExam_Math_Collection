---
university: "ukyoto"
category: "kouki"
year: "1991"
question: "5"
type: "solution"
title: "UKYOTO 1991 kouki Q5 (solution)"
---

## 【解】

  

$$
\begin{align*}
\circ\quad\circ\quad\underline{X_1}\quad\circ\quad\underline{X_1}\quad\circ\quad\underline{Y_1}\quad\circ\quad\underline{Y_2}
\end{align*}
$$

  (1)
  $E(X_1+Y_1)$ は $n$個の自然数から二つを取り出す${}_n C_2$ 通り全てについての和である．
  この時各数字は $n-1$ 回出るので
  

$$
\begin{align*}
E(X_1+Y_1)
     & = \frac{1}{{}_n C_2}\sum_{k=1}^n k(n-1) \\& = n+1
\end{align*}
$$

  が求める期待値である．  $\cdots$(答)

  
  (2)
  $X_1=k\, (k=2,3,\cdots, n)$となる場合の数は，$k-1$以下の自然数から$Y_1$を選ぶ${}_{k-1}C_{1}$通りである．
  全体の場合の数は(1)より${}_n C_2$通りだから，$E(X_1)$は
  

$$
\begin{align*}
E(X_1) & = \sum_{k=2}^{n}\frac{k \cdot{}_{k-1} C_1}{{}_n C_2}\\& = \frac{1}{{}_n C_2}\sum_{k=2}^n k \cdot{}_k C_2 \quad(\because{}_n C_r = \frac{n}{r}{}_{n-1} C_{r-1}) \\& = \frac{4}{n(n-1)}{}_{n+1} C_3 \quad(\because\sum_{k=r}^{n} k{}_k C_r = {}_{n+1} C_{r+1})                \\& = \frac{4}{n(n-1)}\frac{(n+1)n(n-1)}{3 \cdot 2 \cdot 1}\\& = \frac{2(n+1)}{3}
\end{align*}
$$

  と求まる．$\cdots$(答)

  
  (3)
  先に $(X_1, Y_1)$ をえらんでも $(X_2, Y_2)$ えらんでも良いので，これらは対称である．
  従って，$Y_2$の期待値と$Y_1$の期待値は等しい．
  そこで$Y_1$について考える．
  期待値の和の公式より
  

$$
\begin{align*}
E(X_1+Y_1) = E(X_1) + E(Y_1) \quad\dots\text{①}
\end{align*}
$$

  であるから，(1)と(2)を代入して
  

$$
\begin{align*}
E(Y_2)
     & = E(X_1+Y_1)- E(Y_1) \\& = \frac{1}{3}(n+1)
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】

  (2)を先に出してもよい．その場合$E(Y_1)$は以下のように求まる．
  $Y_1=k$ なる確率と，$X_1=n+1-k$ なる確率は明らかに等しいから，
  

$$
\begin{align*}
E(Y_1)
     & = n+1 - E(X_1)     \\& = \frac{1}{3}(n+1)
\end{align*}
$$

  類題として，$1$から$n$の$n$個の自然数から，$m$個をえらぶことを考える．
  小さい方から $k$番目の期待値は
  

$$
\begin{align*}
E_k & = \frac{k(n+1)}{m+1}
\end{align*}
$$

  で与えられる．
  
    \begin{tikzpicture}
      \draw (0,0) -- (6,0) node[right] {$\dots$};
      \foreach \x in {0,1,2,3,4}
      \node at (\x,0) {$\circ$};
      \draw[->] (3.5, 0.5) -- (4.5, 0.5) node[right] {$(n-m+1) \cdot A$};
    \end{tikzpicture}
  

  $k=1, m$についての証明は容易である．$k=m$の方は，本解説と同様に
  

$$
\begin{align*}
E_k
     & = \sum_{k=m}^n \frac{k \cdot{}_{k-1}C_{m-1}}{{}_n C_m}\\& = \frac{1}{{}_n C_m}\sum_{k=m}^n m \cdot{}_{k}C_{m}\quad(\because{}_n C_r = \frac{n}{r}{}_{n-1} C_{r-1}) \\& = \frac{m}{{}_n C_m}{}_{n+1}C_{m+1}\quad(\because\sum_{k=r}^n k \cdot{}_k C_r = n {}_{n+1} C_{r+1})       \\& = \frac{m}{{}_n C_m}\frac{n!}{(m+1)!(n-m-1)!}\\&= \frac{m(n+1)}{m+1}\\& = \frac{m(n+1)}{m+1}
\end{align*}
$$

  となる．
  対称性から $E_{1} = n+1-E_{m}$ となることに注意して
  

$$
\begin{align*}
E(1) = \frac{n+1}{m+1}
\end{align*}
$$

  となる．以上から$k=1,m$では示された．

  \begin{itemize}
    \item ${}_n C_r = {}_{n} C_{n-r}$
    \item $\sum_{k=r}^n {}_k C_r = {}_{n+1} C_{r+1}$
  \end{itemize}