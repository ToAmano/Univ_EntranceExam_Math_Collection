---
university: "todai"
category: "kouki"
year: "2002"
question: "3"
type: "solution"
title: "TODAI 2002 kouki Q3 (solution)"
---

## 【解】

### (1)

  関数$y=f(x)$のグラフは[図1](#2002-3:fig:1)である．

  

<figure id="2002-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2002/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=f(x)$のグラフ</figcaption>
</figure>

  従って，$b=f(b)$を解くとグラフより
  
$$
\begin{align*}
b = 0, \frac{2}{3}
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  題意を満たす，すなわち$a_4=0,2/3$となる場合を考える．
  まず，前者の場合は
  
$$
\begin{align*}
& a_4=0                                          \\\iff& a_3=0, 1                                       \\\iff& a_2 = 0, \frac{1}{2}, 1                        \\\iff& a_1 = 0, \frac{1}{4}, \frac{2}{4}, \frac{3}{4}
\end{align*}
$$

  である．
  後者の場合は
  
$$
\begin{align*}
& a_4=\frac{2}{3}\\\iff& a_3= \frac{1}{3}, \frac{2}{3}\\\iff& a_2=0, \frac{1}{6}, \frac{2}{6},\frac{4}{6}, \frac{5}{6}\\\iff& a_1 = \frac{1}{12}, \frac{2}{12}, \frac{4}{12}, \frac{5}{12}, \frac{7}{12}, \frac{8}{12}, \frac{10}{12}, \frac{11}{12}
\end{align*}
$$

  である．
  以上まとめて，求める初期値は
  
$$
\begin{align*}
& a_1 = \frac{i}{12}& (i=0,1,2,\cdots,12)
\end{align*}
$$

  である．$\cdots$(答)

### (3)

  $n \ge 2$ において, $a_n=0,2/3$ となる $a_1$ は, $a_1 = \frac{i}{3 \cdot 2^{n-2}} \quad (i=0,1,\dots,3 \cdot 2^{n-2})$ で表現できること（$\diamondsuit$）を帰納的に示す.

### (2)
から $n=2$ では成立するので, 以下 $n=k (\ge 2)$ での成立を仮定し, $n=k+1$ でも成立することを示す.

  $i=0,1,\dots,3 \cdot 2^{k-2}$ として，数列$a_2,a_3,\cdots,a_{k+1}$を考えると，
  仮定より$a_{k+1}=0,2/3$となる$a_2$の条件は
  
$$
\begin{align*}
a_{k+1}=0 \iff a_{2} = \frac{i}{3 \cdot 2^{k-2}}
\end{align*}
$$

  であり，この時$a_1$は
  
$$
\begin{align*}
a_1
     & = \frac{1}{2}a_{2}, 1-\frac{1}{2}a_{2}\\& = \frac{i}{3 \cdot 2^{k-1}}
\end{align*}
$$

  となるから，$\diamondsuit$は$n=k+1$でも成立する．

  以上から数学的帰納法により，任意の$2$以上の自然数について$\diamondsuit$が成立する．
  $n=1$の時の$a_1=0,2/3$は，$n$を動かした時にこの表現に含まれるから別で考慮する必要はなく，
  求める条件は
  
$$
\begin{align*}
a_{1}  = \frac{i}{3 \cdot 2^{k-2}}\quad(k \in\mathbb{N}\geqq 2, i=0,1,\dots,3 \cdot 2^{k-2})
\end{align*}
$$

  である．$\cdots$(答)

### (4)

  背理法によって題意を示す．
  $a_1$ が (3) の条件をみたさない値で, かつ任意の $n \in \mathbb{N}$ に対して $a_n < \frac{3}{4}$ だと仮定する. \\
  $a_n < \frac{1}{2}$ の時，漸化式は $a_{n+1} = 2a_n$ だから, $a_1 < \frac{1}{2}$ ならばくり返し用いて $a_m \ge \frac{1}{2}$ となる自然数 $m$ が必ず存在する.
  一方で，$m \le n$なる自然数$n$に対しては，仮定より$a_n < 3/4$だから常に
  
$$
\begin{align*}
a_{n+1} > \frac{1}{2}
\end{align*}
$$

  であり，漸化式は
  
$$
\begin{align*}
a_{n+1} = -2 a_{n} + 2
\end{align*}
$$

  が用いられる．
  よって$m \le n$に対して漸化式を解くと
  
$$
\begin{align*}
& a_{n+1} = 2(1-a_n)                                            \\\therefore& a_{n+1} - \frac{2}{3} = -2\left(a_n - \frac{2}{3}\right)\\\therefore& a_n = (-2)^{n-m}\left(a_m - \frac{2}{3}\right) + \frac{2}{3}
\end{align*}
$$

  である．仮定から $a_m \ne \frac{2}{3}$ なので,
  
$$
\begin{align*}
\lim_{n\to\infty} |a_n| = \infty
\end{align*}
$$

  となり$0 \le a_n \le 1$に矛盾する．
  したがって背理法により必ず$a_n \ge 3/4$となる$n$が存在することが示された.$\cdots$(答)

### (5)

### (3)
より，$a_1$ が (3) の条件をみたすことと $a_n=0, 2/3$ なる $n$ が存在することは同値である．
  また, $b=0, \frac{2}{3}$ は $a_n$ の恒等写像だから，
  
$$
\begin{align}
\text{「$a_1$ が (3) の条件をみたす $\implies a_n$ は収束する」}\label{2002-3:eq:1}
\end{align}
$$

  が成り立つ.

  以下, $a_1$ が (3) の条件をみたさない時をかんがえる.
  この時. （4）から$a_m \ge \frac{3}{4}$ なる $m \in \mathbb{N}$ が存在し，
  漸化式から $a_{m+1} < \frac{1}{2}$ となる．
  この後 $a_{m+1}=a'_1$ とみなして $a'_{n+1} = f(a_n')$ で新しく数列 $\{a'_n\}$ を定めると，
  $a'_{1}$ は (3) の条件をみたさないので再び $a'_{l} \ge \frac{3}{4}$ なる $l$ がある．
  以下同様の操作が無限にくりかえされるから $a_n$ は収束しない．

  以上から，求める必要十分条件は，初項が
  
$$
\begin{align*}
a_1 = \frac{i}{3 \cdot 2^{k-2}}\quad(k \in\mathbb{N}, k \ge 2, i=0,1,\dots,3 \cdot 2^{k-2})
\end{align*}
$$

  と表されることである.$\cdots$(答)

  
  

## 【解説】