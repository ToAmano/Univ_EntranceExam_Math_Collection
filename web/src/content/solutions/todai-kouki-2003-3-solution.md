---
university: "todai"
category: "kouki"
year: "2003"
question: "3"
type: "solution"
title: "TODAI 2003 kouki Q3 (solution)"
---

## 【解】

### (1)

  $x_0 = 0$ より，漸化式を用いると$n=2,3$のとき
  
$$
\begin{align*}
& x_2 = a_1 x_1           \\& x_3 = (a_2 a_1 - 1) x_1
\end{align*}
$$

  となり，以下帰納的に$x_n$は$x_1$と比例係数$k_n$を用いて
  
$$
\begin{align}
\begin{dcases}
      x_n = k_n x_1 \\
      k_1 = 1       \\
      k_2 = a_1
    \end{dcases}\label{2003-3:eq:1}
\end{align}
$$

  と表せる．

  $x_1$の時は従って全ての$n$に対して$x_n=0$となり題意の$x_m=1$を満たさず矛盾するから，
  以下
  
$$
\begin{align*}
x_1 \neq 1
\end{align*}
$$

  として考える．

  漸化式の両辺を$x_1$で割って
  
$$
\begin{align}
k_{n+2} = a_{n+1} k_{n+1} - k_n \label{2003-3:eq:2}
\end{align}
$$

  だから，$\eqref{2003-3:eq:1}$の初期条件のもとで$k_3,k_4,\cdots$が一意に定まる．
  従って題意の条件を数列$\{x_n\}$が満たすには
  
$$
\begin{align*}
& x_m = 1             \\\therefore& x_1 = \frac{1}{k_m}
\end{align*}
$$

  とすればよく，従ってこのような数列はただ一つ存在する．  $\cdots$(答)
  

  次にこの数列について$0<x_n<1\, (n=1,2,\cdots, m-1)$であることを示す．
  そのため，まず$k_{n}<k_{n+1}$であることを数学的帰納法により示す．

  $n=1$の時は$k_1=1,k_2=a_1\ge 2$より$k_2>k_1$が成立する．
  そこで$n=t$での成立を仮定して$n=t+1$の時を考えると，漸化式$\eqref{2003-3:eq:2}$より
  
$$
\begin{align*}
k_{t+2} - k_{t+1}& = a_{t+1} k_{t+1} - k_t - k_{t+1}\\& = \left(a_{t+1}-1\right) k_{t+1} - k_t          \\& \ge k_{t+1} - k_t \quad(\because a_{t+1}\ge 2) \\
    > 0
\end{align*}
$$

  である．ただし最後の行で仮定を用いた．

  従って$n=t+1$の時も$k_{n}<k_{n+1}$が成立するから，数学的帰納法により任意の自然数$n$に対して
  
$$
\begin{align*}
k_{n} < k_{n+1}
\end{align*}
$$

  である．これと$k_1=1$から
  
$$
\begin{align}
0< k_1 < k_2 < \cdots < k_{m-1} < k_m \label{2003-3:eq:5}
\end{align}
$$

  である．両辺を$k_m>0$で割って，$x_1=1/k_m$および$\eqref{2003-3:eq:1}$より
  
$$
\begin{align*}
& 0< \frac{k_1}{k_m} < \frac{k_2}{k_m} < \cdots <.  \frac{k_{m-1}}{k_m} < 1 \\& 0< k_1x_1 < k_2x_1 < \cdots < k_{m-1}x_1 <  1                             \\& 0 < x_1 < x_2 < \cdots < x_{m-1} < 1
\end{align*}
$$

  である．よって題意は示された．$\cdots$(答)

### (2)

### (1)
との違いは，漸化式の$x_n$の係数が異なる部分のみである．
  従って，ほぼ全て(1)の議論が流用できる．

  $y_0 = 0$ より，漸化式を用いると$n=2,3$のとき
  
$$
\begin{align*}
& y_2 = a_1 y_1           \\& y_3 = (a_2 a_1 - b) y_1
\end{align*}
$$

  となり，以下帰納的に$y_n$は$y_1$と比例係数$k_n$を用いて
  
$$
\begin{align}
\begin{dcases}
      y_n = k_n y_1 \\
      k_1 = 1       \\
      k_2 = a_1
    \end{dcases}\label{2003-3:eq:3}
\end{align}
$$

  と表せる．

  $y_1$の時は従って全ての$n$に対して$y_n=0$となり題意の$y_m=1$を満たさず矛盾するから，
  以下
  
$$
\begin{align*}
y_1 \neq 1
\end{align*}
$$

  として考える．

  漸化式の両辺を$y_1$で割って
  
$$
\begin{align}
k_{n+2} = a_{n+1} k_{n+1} - b k_n \label{2003-3:eq:4}
\end{align}
$$

  だから，$\eqref{2003-3:eq:3}$の初期条件のもとで$k_3,k_4,\cdots$が一意に定まる．
  従って題意の条件を数列$\{y_n\}$が満たすには
  
$$
\begin{align*}
& y_m = 1             \\\therefore& y_1 = \frac{1}{k_m}
\end{align*}
$$

  とすればよく，従ってこのような数列はただ一つ存在する．  $\cdots$(答)
  

  次にこの数列について$0<y_n<1\, (n=1,2,\cdots, m-1)$であることを示す．
  そのため，まず$k_{n}<k_{n+1}$であることを数学的帰納法により示す．

  $n=1$の時は$k_1=1,k_2=a_1\ge 2$より$k_2>k_1$が成立する．
  そこで$n=t$での成立を仮定して$n=t+1$の時を考えると，漸化式$\eqref{2003-3:eq:4}$より
  
$$
\begin{align*}
k_{t+2} - k_{t+1}& = a_{t+1} k_{t+1} - bk_t - k_{t+1}\\& = \left(a_{t+1}-1\right) k_{t+1} - bk_t                      \\& >  \left(a_{t+1}-1 - b\right) k_t \quad(\because\text{仮定}) \\& \ge 0
\end{align*}
$$

  である．ただし最後の行で$a_n\ge b+1$を用いた．

  従って$n=t+1$の時も$k_{n}<k_{n+1}$が成立するから，数学的帰納法により任意の自然数$n$に対して
  
$$
\begin{align*}
k_{n} < k_{n+1}
\end{align*}
$$

  である．これと$k_1=1$から
  
$$
\begin{align*}
0< k_1 < k_2 < \cdots < k_{m-1} < k_m
\end{align*}
$$

  である．両辺を$k_m>0$で割って，$y_1=1/k_m$および$\eqref{2003-3:eq:3}$より
  
$$
\begin{align*}
& 0< \frac{k_1}{k_m} < \frac{k_2}{k_m} < \cdots <.  \frac{k_{m-1}}{k_m} < 1 \\& 0< k_1y_1 < k_2y_1 < \cdots < k_{m-1}y_1 <  1                             \\& 0 < y_1 < y_2 < \cdots < y_{m-1} < 1
\end{align*}
$$

  である．よって題意は示された．$\cdots$(答)

### (3)

  $a_n \ge c > 2$ から，$\{x_n\}$は(1)の条件を満たす．
  従って，$\eqref{2003-3:eq:5}$が使える．
  漸化式$\eqref{2003-3:eq:2}$から，
  
$$
\begin{align}
k_{n+2}& = a_{n+1} k_{n+1} - k_n                                          \\& > (a_{n+1}-1) k_{n+1}\quad(\because\text{$\eqref{2003-3:eq:5}$}) \\& > (c-1) k_{n+1}\quad(\because a_n \ge c) \label{2003-3:eq:6}
\end{align}
$$

  である．ここで
  
$$
\begin{align*}
r' = \frac{1}{c-1}
\end{align*}
$$

  とおくと，$2 > c$から$0 < r' < 1$ である．
  不等式$\eqref{2003-3:eq:6}$を繰り返し用いて，$n=1,2,\cdots,m-1$に対して
  
$$
\begin{align*}
& k_m > \left(\frac{1}{r'}\right)^{m-n} k_n \\\therefore
    k_n < \left(r'\right)^{m-n} k_m
\end{align*}
$$

  である．両辺に$x_1 = 1/k_m>0$をかけて，$x_n=k_nx_1$より
  
$$
\begin{align*}
k_n x_1 < \left(r'\right)^{m-n}\\\therefore
    x_n < \left(r'\right)^{m-n}
\end{align*}
$$

  である．よって題意は示された．$\cdots$(答)

  
  

## 【解説】