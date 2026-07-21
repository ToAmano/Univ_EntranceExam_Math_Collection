---
university: "todai"
category: "kouki"
year: "1997"
question: "3"
type: "solution"
title: "TODAI 1997 kouki Q3 (solution)"
---

## 【解】

### (1)

  $a \in \mathbb{N}$および 4桁以下の非負整数$m$ を用いて
  
$$
\begin{align*}
N = a \times 10^4 + m
\end{align*}
$$

  とおく.

  $N=10000$の時，$a=1$および$m=0$である．
  この時，二回の試行で同じ数が出る時を考える．
  $N=10000$の時は発生した数と表示される数は全て一対一対応しているから，
  一回目の試行で出た数字を$x$とすると，二回目の試行でも$x$が出ないとならない．
  従って求める確率は
  
$$
\begin{align}
p_{10000}& = \frac{1}{N}\label{1997-3:eq:1}\\& = \frac{1}{10^4}
\end{align}
$$

  である．  $\cdots$(答)

### (2)

  $a=1$および$m\neq 0$の時を考える．
  この時，ある数字が表示される確率は
  
$$
\begin{align*}
\begin{dcases}
      0001 \sim m \text{の時は} \frac{2}{N}         & (\text{パターンは}m\text{通り})    \\
      0000，\text{および} m+1 \text{以上は} \frac{1}{N} & (\text{パターンは}N-2m\text{通り})
    \end{dcases}
\end{align*}
$$

  であるから，確率$P_{N}$は
  
$$
\begin{align}
P_{N}& = m \left(\frac{2}{N}\right)^2 + (N-2m) \left(\frac{1}{N}\right)^2 \\& = \frac{N+2m}{N^2}\label{1997-3:eq:2}
\end{align}
$$

  となる．$\eqref{1997-3:eq:1}$から，$m=0$の時もこの表現で良い．

  従って，$P_{10001}$と$P_{10000}$について，$l=10000$とすると
  
$$
\begin{align}
P_{10001} - P_{10000}& = \frac{(l+1)+2}{(l+1)^2} - \frac{1}{l}\\& = \frac{\ell-1}{(\ell+1)^2 \ell} > 0 \label{1997-3:eq:3}
\end{align}
$$

  だから，
  
$$
\begin{align*}
P_{10001} > P_{10000}
\end{align*}
$$

  である．
  また，差$\eqref{1997-3:eq:3}$を有効数字$1$桁で計算すると
  
$$
\begin{align*}
P_{10001} - P_{10000}& = \frac{9999}{(10000+1)^2 \cdot 10^4}\\& = \frac{9999}{(10^4+1)^2 \cdot 10^4}\\& \approx 9.997 \times 10^{-9}\\& \approx 1.0 \times 10^{-8}
\end{align*}
$$

  である．$\cdots$(答)

### (3)

  $a=2$の場合，$N=20000$の場合については，(1)と同様に考えると
  
$$
\begin{align}
P_{20000}& = \frac{2}{20000}\\& = \frac{1}{10^4}\quad(=P_{10000}) \label{1997-3:eq:4}
\end{align}
$$

  である．

  一方$a=1$の場合，$N=10000,10001,\cdots,19999$について考える．
  この時
  
$$
\begin{align*}
N = 10^4 + m
\end{align*}
$$

  だから，$\eqref{1997-3:eq:2}$は
  
$$
\begin{align*}
P_{N} = \frac{10^4+3m}{(10^4+m)^2}
\end{align*}
$$

  と書ける．そこで$m$を$x$で置き換えた関数
  
$$
\begin{align*}
f(x) = \frac{10^4+3x}{(10^4+x)^2}
\end{align*}
$$

  を考える．
  一階微分は
  
$$
\begin{align*}
f'(x) & = \frac{3(10^4+x)^2 - (10^4+3x) \cdot 2(10^4+x)}{(10^4+x)^4}\\& = \frac{-3x+10^4}{(10^4+x)^3}
\end{align*}
$$

  だから，$f(x)$の増減表は$\eqref{1997-3:table:1}$となる．
  \begin{table}[H]
    \centering
    \caption{$f(x)$の増減表．}
    \label{1997-3:table:1}
    

| $x$ | $0$ | $\cdots$ | $\frac{10^4}{3}$ | $\cdots$ | $10^4-1$ |
|:----:|:---:|:----------:|:----------------:|:----------:|:--------:|
| $f'$ | | $+$ | $0$ | $-$ | |
| $f$ | | $\nearrow$ | | $\searrow$ | |

  \end{table}

  $\eqref{1997-3:eq:4}$も考慮すると，$f(x)$は$x=frac{10^4}{3} = 3333.3\cdots$で最大値をとる．
  従って$P_N$の最大値は$N=13333$か$N=13334$でとる．
  ここで
  
$$
\begin{align*}
P_{13333}& \fallingdotseq 1.125 \times 10^{-4}\\
    P_{13334}& \fallingdotseq 5.626 \times 10^{-5}
\end{align*}
$$

  より，$P_N$の最大値は$N=13333$の時で，
  
$$
\begin{align*}
r = \max P_N = P_{13333} = \frac{19999}{(13333)^2}
\end{align*}
$$

  となる．

  次に最小値については，$N=10000,19999,20000$のいずれかで取る．
  $\eqref{1997-3:eq:4}$より$N=10000$と$N=20000$の時は$P_N$は同じ値を取る．
  一方$N=19999$の時は，$l=10000$とおくと
  
$$
\begin{align*}
P_{19999}& = \frac{10^4+3*9999}{(10^4+9999)^2}\\& = \frac{l+3(l-1)}{(2l-1)^2}\\& = \frac{4l-3}{(2l-1)^2}\\
\end{align*}
$$

  で，これと$P_{10000}$の比較は
  
$$
\begin{align*}
P_{19999} - P_{10000}\\& =\frac{4l-3}{(2l-1)^2} - \frac{1}{l}\\& = \frac{(4l-3)l-(2l-1)^2}{l(2l-1)^2}\\& = \frac{l-1}{l(2l-1)^2}& >0
\end{align*}
$$

  より，$P_{10000}$の方が小さく，これが最小値である．
  
$$
\begin{align*}
q = P_{10000} = P_{20000} = \frac{1}{10000}
\end{align*}
$$

  以上まとめて
  
$$
\begin{align*}
r & = \frac{19999}{(13333)^2}\\
    q & = \frac{1}{10^4}
\end{align*}
$$

  である．  $\cdots$(答)

### (4)

  一般の$a$について考える．$m\neq 0$の時，ある数字が表示される確率は
  
$$
\begin{align*}
\begin{dcases}
      0001 \sim m \text{の時は} \frac{a+1}{N}       & (\text{パターンは}m\text{通り})                         \\
      0000，\text{および} m+1 \text{以上は} \frac{1}{N} & (\text{パターンは}10^4-m=\frac{N-(a+1)m}{a}\text{通り})
    \end{dcases}
\end{align*}
$$

  だから，
  
$$
\begin{align}
P_{N}& = m \left(\frac{a+1}{N}\right)^2 + \frac{N-(a+1)m}{a}\left(\frac{a}{N}\right)^2 \\& = \frac{m(a+1)^2+(N-(a+1)m)a}{N^2}\\& = \frac{ma + m + Na }{N^2}
\end{align}
$$

  となる．

  $m=0$の時は
  
$$
\begin{align*}
P_N = \frac{a}{N}
\end{align*}
$$

  だから，この場合もこの表現で良い．

  ここで$l=10^4$とおくと$N=la+m$より
  
$$
\begin{align*}
P_{N}& = \frac{ma + m + (al+m)a }{(al+m)^2}\\& = \frac{la^2 + 2ma + m }{(al+m)^2}\\& = \frac{(al+m)^2/l + m - m^2/l}{(al+m)^2}\\& = \frac{1}{l} + \frac{ m(1-m/l)}{(al+m)^2}\\
\end{align*}
$$

  を得る．

  ここで$m < l$より，第二項は非負だから，
  
$$
\begin{align}
P_{N}\ge\frac{1}{l} = q
\end{align}
$$

  と評価できる．

  同様に，この関数は$a$について単調減少だから$a=1$の場合が最大であり，

### (3)
からこの場合の最大値が$r$だから，
  
$$
\begin{align*}
P_{N}\le P_{l+m}\le r
\end{align*}
$$

  である．

  以上まとめて
  
$$
\begin{align*}
q \le P_{N}\le r
\end{align*}
$$

  である．よって題意は示された．$\cdots$(答)

  
  

## 【解説】