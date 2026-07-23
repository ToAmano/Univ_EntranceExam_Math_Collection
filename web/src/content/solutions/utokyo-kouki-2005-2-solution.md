---
university: "utokyo"
category: "kouki"
year: "2005"
question: "2"
type: "solution"
title: "UTOKYO 2005 kouki Q2 (solution)"
---

## 【解】

  (1)
  まず$r \ge 2$とする．
  $2 \le n \le r-1$ をみたす自然数 $n$ に対し，
  第 $n$ ラウンドまでゲームが続く確率 $P(n)$ は，
  $n-1$ 回目まで $1 \le x \le k$ をみたす $x$ のみがでる確率で，
  

$$
\begin{align*}
P(n) = \left(\frac{k}{10}\right)^{n-1}
\end{align*}
$$

  である．
  $n=1$の時は$P(1)=1$でこの表現で良いので，以下$1 \le n \le r-1$で考える．

  したがって，第 $n$ ラウンドでゲームが終了する時の得点の期待値 $E(n)$ は
  

$$
\begin{align}
E(n)
     & = P(n) \cdot\left(\frac{k+1}{10} + \dots + \frac{10}{10}\right)\\& = \frac{(k+11)(10-k)}{20} P(n) \label{2005-2:eq:2}
\end{align}
$$

  である．

  また，第 $r$ ラウンドでゲームが終了する時の期待値は，
  

$$
\begin{align*}
E(r)
     & = P(r)\frac{1+2+\cdots+10}{10}\\& = \frac{11}{2}P(r)
\end{align*}
$$

  である．

  ゲーム全体の期待値$E$は，
  期待値の和の公式より各ラウンドでゲームが終了した時の期待値$E(n)$の和であり，
  

$$
\begin{align}
E
     & = \sum_{n=1}^{r} E(n)                                                                                                               \\& = \sum_{n=1}^{r-1} E(n) + E(r)                                                                                                      \\& = \frac{1}{20}(k+11)(10-k) \frac{1-\left(\frac{k}{10}\right)^{r-1}}{1-\frac{k}{10}} + \frac{11}{2}\left(\frac{k}{10}\right)^{r-1}\\& = \frac{k+11}{2}\left\{ 1-\left(\frac{k}{10}\right)^{r-1}\right\} + \frac{11}{2}\left(\frac{k}{10}\right)^{r-1}\\& = \frac{k+11}{2} - \frac{k}{2}\left(\frac{k}{10}\right)^{r-1}\label{2005-2:eq:1}
\end{align}
$$

  である．

  最後に$r=1$のときの期待値は
  

$$
\begin{align*}
E(r=1)
     & = \frac{1+2+\cdots + 10}{10}\\& =\frac{11}{2}
\end{align*}
$$

  であり，[(式1)](#2005-2:eq:1)の表現で良い．

  以上から，自然数$r$に対して，戦略$f_k(x)$を取った時の得点の期待値は
  

$$
\begin{align*}
E = \frac{k+11}{2} - \frac{k}{2}\left(\frac{k}{10}\right)^{r-1}
\end{align*}
$$

  である．$\cdots$(答)
  

  （2）
  まず最初に，以下の補題を示す．

  \begin{lemma}
    得点の期待値を最大にする戦略は(1)の形の関数 $f_{k}(x)$ で与えられる．
  \end{lemma}

  \begin{proof}
    $1 \le n \le 9$ とし，
    

$$
\begin{align*}
f(x)=
      \begin{dcases}
        1 & (x=n)   \\
        0 & (x=n+1)
      \end{dcases}
\end{align*}
$$

    だと仮定する．
    この戦略をとるラウンドを $p\, (1 \le p \le r-1)$ とする．
    このラウンドでの得点の期待値$E_p$は, $n$ に無関係な定数
    

1.  $p$ラウンドが実施される確率

2.  $n$以外を引いてゲームが終了する時の1ターンの期待値

    を用いて
    

$$
\begin{align*}
E_n = A\left(B+\frac{n}{10}\right)
\end{align*}
$$

    と表される．一方で
    

$$
\begin{align*}
f(x)=
      \begin{dcases}
        0 & (x=n)   \\
        1 & (x=n+1)
      \end{dcases}
\end{align*}
$$

    だとすると同様に
    

$$
\begin{align*}
E'_n = A\left(B+\frac{n+1}{10}\right)
\end{align*}
$$

    であり，$E'_n>E_n$が成り立つ．また，この変更によって$p$ラウンド以外への影響はない．
    したがって, $f(1), f(2), \dots, f(10)$ を書き下した時， "1,0" という配列があればそれを入れかえることにより期待値を大きくできる．
    これをくり返すことによって, 「補題」は示された．
  \end{proof}

  「補題」と（1）から，$r=2$の時の期待値の最大値は
  

$$
\begin{align*}
E(2)
     & = \frac{k+11}{2} - \frac{k}{2}\cdot\frac{k}{10}\\& = \frac{10(k+11)}{20} - \frac{k^2}{20}\\& = \frac{-k^2+10k+110}{20}\\& = \frac{1}{20}\left[-\left(k-5\right)^2+135\right]
\end{align*}
$$

  の形で与えられる．
  従ってこの最大値は$k=5$の時の$27/4$である．
  

$$
\begin{align*}
\begin{dcases}
      \text{戦略:} f_{5}(x) \\
      \text{期待値:} \frac{27}{4}
    \end{dcases}
\end{align*}
$$

  $\cdots$(答)
  

  (3)
  第一ラウンドで$f_{k_1}(x)$，第二ラウンドで$f_{k_2}(x)$を採用するとする．
  （2）より，第二ラウンドでは最適解$k_2=5$を採用する．
  この時のゲーム全体の期待値は第一ラウンドでゲームが終了する時の期待値$E(1)$と，
  (2)での期待値$27/4$を用いて
  

$$
\begin{align*}
E
     & = E(1) + \frac{k_1}{10}\frac{27}{4}\\& = \frac{(k_1+11)(10-k_1)}{20} + \frac{27k_1}{40}
\end{align*}
$$

  である．ただし$E(1)$は[(式2)](#2005-2:eq:2)で与えられていることを用いた．

  $k_1$について整理して，
  

$$
\begin{align*}
E
     & =  \frac{1}{40}\left[-2k_1^2-2k_1 + 110 + 27k_1 \right]\\& =  \frac{1}{40}\left[-2k_1^2+25k_1 + 110  \right]\\& =  \frac{1}{20}\left[-\left(k_1-\frac{25}{4}\right)^2 + \frac{625}{16} + 110  \right]\\
\end{align*}
$$

  である．
  これを最大にする $k_1$ は $k_1=6$ で,
  この時 $E = \frac{149}{20}$である．
  よって
  

1.  第一ラウンドで $f_6(x)$, 第二ラウンドで $f_5(x)$ \\

2.  $E = \frac{149}{20}$

  である．$\cdots$(答)

  
  

## 【解説】