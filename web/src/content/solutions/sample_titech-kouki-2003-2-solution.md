---
university: "sample_titech"
category: "kouki"
year: "2003"
question: "2"
type: "solution"
title: "SAMPLE_TITECH 2003 kouki Q2 (solution)"
---

## 【解】

  題意の直線$2x+3y=m$は図のようになる．

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/sample_titech/kouki/2003/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1</figcaption>
</figure>

  さて，$x$,$y$をパラメータ表示するため，
  
$$
\begin{align*}
\begin{dcases}
      2x+3y=m \\
      -2m+3m=m
    \end{dcases}
\end{align*}
$$

  を辺々引いて,
  
$$
\begin{align*}
2(x+m)+3(y-m)=0
\end{align*}
$$

  $2$ と $3$ は互いに素だから, $k \in \mathbb{Z}$ として,
  
$$
\begin{align*}
& \begin{dcases}
         x+m = 3k \\
         y-m = -2k
       \end{dcases}\\\therefore& (x,y) = (3k-m, -2k+m)
\end{align*}
$$

  と表すことができる．
  $x$,$y$が非負だから，$k$に対する条件は
  
$$
\begin{align*}
\frac{m}{3}\le k \frac{m}{2}
\end{align*}
$$

  であり，従って$N(m)$は
  
$$
\begin{align}
N(m) = \left(\frac{m}{3}\le k \le\frac{m}{2}\text{をみたす } k \in\mathbb{Z}\text{の数}\right)\label{2003-2:eq:1}
\end{align}
$$

  と言い換えることができる．

  ここで，ガウス記号$[a]$を導入する．
  これは $a$ 以下の最大の整数を表すものとする.
  すると$\eqref{2003-2:eq:1}$は
  
$$
\begin{align}
N(m) =
    \begin{dcases}
      \left[\frac{m}{2}\right] - \left[\frac{m}{3}\right]     & (m \not\equiv 0, \mod 3) \\
      \left[\frac{m}{2}\right] - \left[\frac{m}{3}\right] + 1 & (m \equiv 0, \mod 3)
    \end{dcases}\label{2003-2:eq:4}
\end{align}
$$

  と書ける．

### (1)

  $\eqref{2003-2:eq:4}$を用いて$N(m+6)$を計算すると
  
$$
\begin{align*}
N(m+6) =
      & \begin{dcases}
          \left[\frac{m+6}{2}\right] - \left[\frac{m+6}{3}\right]     & (m \not\equiv 0, \mod 3) \\
          \left[\frac{m+6}{2}\right] - \left[\frac{m+6}{3}\right] + 1 & (m \equiv 0, \mod 3)
        \end{dcases}\\
    = & \begin{dcases}
          \left[\frac{m}{2}+3\right] - \left[\frac{m}{3}+2\right]     & (m \not\equiv 0, \mod 3) \\
          \left[\frac{m}{2}+3\right] - \left[\frac{m}{3}+2\right] + 1 & (m \equiv 0, \mod 3)
        \end{dcases}\\
    = & \begin{dcases}
          \left[\frac{m}{2}\right]+3 - \left[\frac{m}{3}\right]-2      & (m \not\equiv 0, \mod 3) \\
          \left[\frac{m}{2}\right]+3 - \left[\frac{m}{3}\right] -2 + 1 & (m \equiv 0, \mod 3)
        \end{dcases}\\
    = & \begin{dcases}
          \left[\frac{m}{2}\right] - \left[\frac{m}{3}\right] + 1    & (m \not\equiv 0, \mod 3) \\
          \left[\frac{m}{2}\right] - \left[\frac{m}{3}\right] +1 + 1 & (m \equiv 0, \mod 3)
        \end{dcases}\\
    = & N(m) + 1
\end{align*}
$$

  となり，題意は示された．$\cdots$(答)

### (2)

  簡単のため，
  
$$
\begin{align*}
f(m) = 1-m+\left[\frac{m}{2}\right]+\left[\frac{2}{3}m\right]
\end{align*}
$$

  とおくと，$f(m)$が$\eqref{2003-2:eq:4}$に等しいことを証明すれば良い．

  以下，$m$を$\mod 3$で場合分けして考える．$k\in\mathbb{Z} \ge 0$とする．

  
  \underline{\textbf{$1^{\circ} m \equiv 0$の時}}

  この時，$m=3k$とおいて$f(m)$と$\eqref{2003-2:eq:4}$をそれぞれ計算すると
  
$$
\begin{align*}
f(m)
     & = 1-3k+\left[\frac{m}{2}\right]+\left[\frac{2}{3}3k\right]\\& = 1-3k+\left[\frac{m}{2}\right] + 2k                       \\& = \left[\frac{m}{2}\right] - k +1
\end{align*}
$$

  および
  
$$
\begin{align*}
N(m)
     & = \left[\frac{m}{2}\right] - \left[\frac{3k}{3}\right] + 1 \\& = \left[\frac{m}{2}\right] - k + 1
\end{align*}
$$

  より，$N(m)=f(m)$が成立する．

  
  \underline{\textbf{$2^{\circ} m \equiv 1$の時}}

  この時，$m=3k+1$とおいて$f(m)$と$\eqref{2003-2:eq:4}$をそれぞれ計算すると
  
$$
\begin{align*}
f(m)
     & = 1-(3k+1)+\left[\frac{m}{2}\right]+\left[\frac{2}{3}(3k+1)\right]\\& = -3k+\left[\frac{m}{2}\right] + 2k                                \\& = \left[\frac{m}{2}\right] - k
\end{align*}
$$

  および
  
$$
\begin{align*}
N(m)
     & = \left[\frac{m}{2}\right] - \left[\frac{3k+1}{3}\right]\\& = \left[\frac{m}{2}\right] - k
\end{align*}
$$

  より，$N(m)=f(m)$が成立する．

  
  \underline{\textbf{$3^{\circ} m \equiv 2$の時}}

  この時，$m=3k+2$とおいて$f(m)$と$\eqref{2003-2:eq:4}$をそれぞれ計算すると
  
$$
\begin{align*}
f(m)
     & = 1-(3k+2)+\left[\frac{m}{2}\right]+\left[\frac{2}{3}(3k+2)\right]\\& = -3k-1+\left[\frac{m}{2}\right] + 2k+1                            \\& = \left[\frac{m}{2}\right] - k
\end{align*}
$$

  および
  
$$
\begin{align*}
N(m)
     & = \left[\frac{m}{2}\right] - \left[\frac{3k+2}{3}\right]\\& = \left[\frac{m}{2}\right] - k
\end{align*}
$$

  より，$N(m)=f(m)$が成立する．

  
  以上で全ての場合が尽くされ，
  
$$
\begin{align*}
N(m) = f(m) = 1-m+\left[\frac{m}{2}\right]+\left[\frac{2}{3}m\right]
\end{align*}
$$

  がしめされた．$\cdots$(答)

  

  

## 【解説】

  答案中では，ガウス記号を用いて比較的綺麗に式変形を行った．
  ただ，この問題はそのような道具を導入せずとも，$\eqref{2003-2:eq:1}$さえ出ていれば
  $\mod 6$で場合分けすれば正解を導ける．
  場合わけの数は増えてしまうが，計算量はあまり増えないので有力だ．
  以下別解として示そう．

### (1)

  $\eqref{2003-2:eq:1}$に注意して $m$ を $6$ で割ったあまりで場合分けする.
  $t \in \mathbb{N}$ として，
  
$$
\begin{align}
\begin{cases}
      m=6t \text{ の時,}   & N(m) = 3t-2t+1 = t+1       \\
      m=6t-1 \text{ の時,} & N(m) = (3t-1)-(2t-1) = t   \\
      m=6t-2 \text{ の時,} & N(m) = (3t-1)-(2t-1) = t   \\
      m=6t-3 \text{ の時,} & N(m) = (3t-2)-(2t-2) = t   \\
      m=6t-4 \text{ の時,} & N(m) = (3t-2)-(2t-2) = t   \\
      m=6t-5 \text{ の時,} & N(m) = (3t-3)-(2t-2) = t+1
    \end{cases}\label{2003-2:eq:2}
\end{align}
$$

  を得る．$N(m+6)$は$t\to t+1$とした時に該当し，このときいずれも$N(m)$は$1$だけ増えるから，
  たしかに $N(m+6) = N(m)+1$ が成立する.
  よって題意は示された．

### (2)

  簡単のため
  
$$
\begin{align*}
f(m) = 1-m+\left[\frac{m}{2}\right]+\left[\frac{2}{3}m\right]
\end{align*}
$$

  とおく. (1)と同様に$m$を$6$で割った余りで場合わけすると，
  
$$
\begin{align}
\begin{dcases}
      m=6t \text{ の時,} f(m) = 1-6t+3t+4t = t+1             \\
      m=6t-1 \text{ の時,} f(m) = 1-(6t-1)+(3t-1)+(4t-1) = t \\
      m=6t-2 \text{ の時,} f(m) = 1-(6t-2)+(3t-1)+(4t-2) = t \\
      m=6t-3 \text{ の時,} f(m) = 1-(6t-3)+(3t-2)+(4t-2) = t \\
      m=6t-4\text{ の時,} f(m) = 1-(6t-4)+(3t-2)+(4t-3) = t  \\
      m=6t-5 \text{ の時,} f(m) = 1-(6t-5)+(3t-3)+(4t-4) = t-1
    \end{dcases}\label{2003-2:eq:3}
\end{align}
$$

  である．
  $\eqref{2003-2:eq:2,2003-2:eq:3}$を比較することで，
  たしかに $f(m)=N(m)$ であることがわかる．
  以上から題意は示された．