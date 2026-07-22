---
university: "utokyo"
category: "kouki"
year: "2007"
question: "3"
type: "solution"
title: "UTOKYO 2007 kouki Q3 (solution)"
---

## 【解】

  (1)
  $t \in \mathbb{N}$ とおく．題意より数列$k_n,p_n,q_n$は以下の初期条件，漸化式を満たす．
  

$$
\begin{align}
k_0=1, p_0=p_1=x_1, q_0=q_1=x_N \label{2007-1:eq:1}
\end{align}
$$

  

$$
\begin{align}
& \begin{dcases}
         k_{2t-1} = \left( x_i \le \frac{p_{2t-2}+q_{2t-2}}{2} \text{をみたす} x_i \text{の個数} \right) \\
         k_{2t} = k_{2t-1}
       \end{dcases}\label{2007-1:eq:2}\\& \begin{dcases}
         p_{2t+1} = p_{2t} \\
         p_{2t} = \frac{1}{k_{2t}} \sum_{i=1}^{k_{2t}} x_i
       \end{dcases}\label{2007-1:eq:3}\\& \begin{dcases}
         q_{2t+1} = q_{2t} \\
         q_{2t} = \frac{1}{N-k_{2t}} \sum_{i=k_{2t}+1}^{N} x_i
       \end{dcases}\label{2007-1:eq:4}
\end{align}
$$

  これは与えられた数列$\{x_i\}$を$k_n$番目で二分して，数字の若い方の平均を$p_n$，数字の大きい方の平均を$q_n$とする処理である．

  さて，題意
  

$$
\begin{align}
\begin{dcases}
      1\le k_n\le N-1 \\
      x_1\le p_n<q_n\le x_N
    \end{dcases}\label{2007-1:eq:5}
\end{align}
$$

  を帰納法で示す．

  $n=1$の時は[(式1)](#2007-1:eq:1)から成立するので，
  以下$n=m\in\mathbb{N}$での成立を仮定して，$n=m+1$での成立を示す．
  $m$の偶奇で場合分けする．

  
  \textbf{1° $m\in \text{even}$の時}

  まず，$p_n,q_n$については[(式4)](#2007-1:eq:3,2007-1:eq:4)から
  $p_{m+1} = p_m, q_{m+1} = q_m$だから仮定より
  

$$
\begin{align*}
x_1 \le p_{m+1} < q_{m+1}\le x_N
\end{align*}
$$

  が成立する．
  ついで$k_n$については[(式2)](#2007-1:eq:2)から
  

$$
\begin{align*}
k_{m+1}& = \left( x_i \le\frac{p_{2m}+q_{2tm}}{2}\text{をみたす} x_i \text{の個数}\right)
\end{align*}
$$

  だが，仮定より
  

$$
\begin{align*}
x_1 \le p_{2m} < \frac{p_{2m}+q_{2m}}{2} < q_{2m}\le x_N \\\therefore
    x_1 \le\frac{p_{2m}+q_{2m}}{2} < x_{N}
\end{align*}
$$

  だから
  が成り立つ．従って
  

$$
\begin{align*}
1 \le k_{m+1} < N-1
\end{align*}
$$

  となり，$n=m+1$でも[(式5)](#2007-1:eq:5)が成立する．

  
  \textbf{2° $m\in \text{odd}$の時}

  まず$k_n$について[(式2)](#2007-1:eq:2)より
  

$$
\begin{align*}
k_{m+1} = k_{m}
\end{align*}
$$

  だから仮定と合わせて
  

$$
\begin{align*}
1 \le k_{m+1}\le N-1
\end{align*}
$$

  である．

  ついで$p_n,q_n$について[(式4)](#2007-1:eq:3,2007-1:eq:4)より
  

$$
\begin{align*}
p_{m+1}& = \frac{1}{k_m}\sum_{i=1}^{k_m}x_i = \frac{x_1+\cdots+x_{k_m}}{k_m}\\
    q_{m+1}& = \frac{1}{N-k_m}\sum_{i=k_m+1}^{N}x_i = \frac{x_{k_m+1}+\cdots+x_N}{N-k_m}
\end{align*}
$$

  であって，題意より$x_n$は$x_1 \le \cdots \le x_N, x_1 < x_N$を満たすから
  

$$
\begin{align*}
& \frac{k_m x_1}{k_m}\le p_{m+1}\le\frac{k_m x_{k_m}}{k_m}\le\frac{N-k_m}{N-k_m}x_{k_{m+1}}\le q_{m+1}\le\frac{N-k_m}{N-k_m}x_N \\\therefore& x_1 \le p_{m+1}\le q_{m+1}\le x_N
\end{align*}
$$

  である．ここで$p_{m+1}$と$q_{m+1}$の等号成立条件は
  

$$
\begin{align*}
x_{1} = x_{2} = \cdots = x_{N}
\end{align*}
$$

  だが，これは$x_1 < x_N$より実現し得ないので等号は不成立で
  

$$
\begin{align*}
x_1 \le p_{m+1} < q_{m+1}\le x_N
\end{align*}
$$

  となる．よって$n=m+1$でも題意は成立する．

  
  以上二つの場合わけで全てが尽くされ，いずれの場合でも$n=m+1$での仮定の成立が示された．

  従って数学的帰納法により，[(式5)](#2007-1:eq:5)が任意の自然数で成立する．

  $\cdots$(答)
  

  (2)
  $n$の偶奇で場合分けして$J_n \le J_{n-1}$を示す．

  
  \textbf{1° $n \in \text{even}$の時}

  この時[(式2)](#2007-1:eq:2)より$k_n = k_{n-1}$だから
  

$$
\begin{align*}
\begin{dcases}
      J_n     = \sum_{i=1}^{k_{n-1}} (x_i-p_n)^2     + \sum_{i=k_{n-1}+1}^{N} (x_i-q_n)^2 \\
      J_{n-1} = \sum_{i=1}^{k_{n-1}} (x_i-p_{n-1})^2 + \sum_{i=k_{n-1}+1}^{N} (x_i-q_{n-1})^2
    \end{dcases}
\end{align*}
$$

  とかけて，差分を取ると
  

$$
\begin{align*}
J_{n-1}-J_n
     & = \left[\sum_{i=1}^{k_{n-1}}(x_i-p_{n-1})^2 - \sum_{i=1}^{k_n}(x_i-p_n)^2 \right]\\& + \left[\sum_{i=k_{n-1}+1}^{N}(x_i-q_{n-1})^2 - \sum_{i=k_n+1}^{N}(x_i-q_n)^2 \right]\label{2007-3:eq:6}
\end{align*}
$$

  を得る．

  ここで$x$の2次方程式
  

$$
\begin{align*}
f(x)
     & = \sum_{i=1}^{k_{n-1}}(x_i-x)^2                                                          \\& = k_{n-1}x^2 - 2 \left(\sum_{i=1}^{k_{n-1}} x_i \right) x + \sum_{i=1}^{k_{n-1}}(x_i)^2
\end{align*}
$$

  を考える．
  $p_n = \frac{1}{k_{n-1}} \sum_{i=1}^{k_{n-1}} x_i$ を代入して
  

$$
\begin{align*}
f(x)
     & = k_{n-1}\left[x^2-2p_nx+k_{n-1}(p_{n})^2\right]\\& = k_{n-1}\left[(x-p_n)^2+(k_{n-1}-1)(p_{n})^2 \right]
\end{align*}
$$

  だから，これは$x=p_{n}$で最小値をとり，[(式6)](#2007-3:eq:6)の第一項目は
  

$$
\begin{align*}
f(p_{n-1})-f(p_{n}) \ge 0
\end{align*}
$$

  より正となる．
  同様に
  

$$
\begin{align*}
g(x) = \sum_{i=k_{n-1}+1}^{N}(x_i-x)^2
\end{align*}
$$

  とおくと第二項目にも同じ議論が適用できて正だから，全体として[(式6)](#2007-3:eq:6)は正，すなわち
  

$$
\begin{align*}
J_{n-1}\ge J_{n}
\end{align*}
$$

  である．

  
  \textbf{1° $n \in \text{odd}$の時}

  漸化式[(式4)](#2007-1:eq:3,2007-1:eq:4)より$p_{n}=p_{n-1}, q_{n}=q_{n-1}$だから
  

$$
\begin{align*}
\begin{dcases}
      J_n      = \sum_{i=1}^{k_n}     (x_i-p_{n-1})^2 + \sum_{i=k_{n}+1}^{N}     (x_i-q_{n-1})^2 \\
      J_{n-1}  = \sum_{i=1}^{k_{n-1}} (x_i-p_{n-1})^2 + \sum_{i=k_{n-1}+1}^{N} (x_i-q_{n-1})^2
    \end{dcases}
\end{align*}
$$

  であり，両式の差分を取るとほとんどの項はキャンセルアウトする．
  $k_n$と$k_{n-1}$の大小に応じて以下のように書ける．
  

$$
\begin{align}
& J_{n-1} - J_{n}\\& =
    \begin{dcases}
      \sum_{i=k_{n}+1}^{k_{n-1}} \left[ (x_i-p_{n-1})^2 - (x_i-q_{n-1})^2 \right]  & (k_n < k_{n-1} ) \\
      0                                                                            & (k_n = k_{n-1})  \\
      \sum_{i=k_{n-1}+1}^{k_{n}} \left[ -(x_i-p_{n-1})^2 + (x_i-q_{n-1})^2 \right] & (k_n > k_{n-1})  \\
    \end{dcases}\\& =
    \begin{dcases}
      2 \sum_{i=k_{n}+1}^{k_{n-1}} \left( x_i - \frac{p_{n-1}+q_{n-1}}{2} \right) (q_{n-1}-p_{n-1})  & (k_n < k_{n-1}) \\
      0                                                                                              & (k_n = k_{n-1}) \\
      2 \sum_{i=k_{n-1}+1}^{k_{n}} \left( -x_i + \frac{p_{n-1}+q_{n-1}}{2} \right) (q_{n-1}-p_{n-1}) & (k_n > k_{n-1}) \\
    \end{dcases}\label{2007-1:eq:6}
\end{align}
$$

  さて，ここで$x_i$と$\frac{p_{n-1}+q_{n-1}}{2}$の大小について考える．
  $k_{n}$の定義により
  

$$
\begin{align*}
\begin{dcases}
      x_i \le \frac{p_{n-1}+q_{n-1}}{2} & (i \le k_{n}) \\
      x_i > \frac{p_{n-1}+q_{n-1}}{2}   & (i > k_{n})
    \end{dcases}
\end{align*}
$$

  又(2)から $p_{n-1}<q_{n-1}$ だから，[(式6)](#2007-1:eq:6)の右辺はいずれの場合も$0$以上である．
  従って
  

$$
\begin{align*}
J_{n-1}\ge J_{n}
\end{align*}
$$

  である．

  
  従って以上の場合わけで全ての場合が尽くされ，いずれの場合も$J_{n-1}\ge J_{n}$であることが示された．
  よって題意は示された．  $\cdots$(答)
  

  (3)
  (2)で得られた不等式$J_{n-1} \ge J_{n}$で$n=1,2,\cdots$として
  

$$
\begin{align}
J_0 \ge J_1 \ge J_2 \ge\cdots\label{2007-1:eq:7}
\end{align}
$$

  となる．

  一方で，$k_n, p_n, q_n$ はいずれも有限個の値をとるので、$J_n$も有限個の値をとる．
  従って，[(式7)](#2007-1:eq:7)を満たすにはある$m \in \mathbb{N}$があって，
  

$$
\begin{align*}
J_m = J_{m+1} = J_{m+2} = \cdots
\end{align*}
$$

  となる必要がある．
  $m$に制限をかけても題意の証明には影響がないので，
  $m$は4以上の偶数としても良い．

  この時$m$以上の整数$n$に対して題意が成立することを示す．
  $n$の偶奇によって場合わけする．

  
  \textbf{1° $n\in \text{even}$の時}

  漸化式[(式2)](#2007-1:eq:2)から$k_n=k_{n-1}$である．
  また，(2)の場合わけで$n$が偶数の場合の $J_{n-1}=J_n$ の等号成立条件より，
  $p_n=p_{n-1}, q_n=q_{n-1}$である．よってこの場合は題意が示された．

  
  \textbf{2° $n\in \text{odd}$の時}

  $m$が偶数であること，および$n \ge m$より，$n-1$は$m$以上の偶数である．
  従って$n-1$に対して1°を適用して
  

$$
\begin{align*}
p_{n-1}=p_{n-2}, q_{n-1}=q_{n-2}
\end{align*}
$$

  である．$n-2$は奇数だから，再び漸化式[(式4)](#2007-1:eq:3,2007-1:eq:4)から
  $p_{n-2}=p_{n-3}, q_{n-2}=q_{n-3}$である．以上から
  

$$
\begin{align*}
p_{n-1} = p_{n-2} = p_{n-3}\\
    q_{n-1} = q_{n-2} = q_{n-3}
\end{align*}
$$

  である．

  従って$k_n$の定義より，
  

$$
\begin{align*}
k_n & = \left( x_i \le\frac{p_{n-1}+q_{n-1}}{2}\text{をみたす} x_i \text{の個数}\right)\\& = \left( x_i \le\frac{p_{n-3}+q_{n-3}}{2}\text{をみたす} x_i \text{の個数}\right)\\& = k_{n-1}
\end{align*}
$$

  となる．よって$n$が奇数の場合も題意は成立する．

  従って以上の場合わけで全ての場合が尽くされ，いずれの場合も題意が成立することが示された．$\cdots$(答)
  

  

## 【解説】