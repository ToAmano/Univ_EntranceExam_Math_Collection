---
university: "todai"
category: "kouki"
year: "2000"
question: "1"
type: "solution"
title: "TODAI 2000 kouki Q1 (solution)"
---

## 【解】

    （1）
    **$k=1$の時** \\

    題意より$P_1(x)$は一次式であって，全ての$x$に対して
    

$$
\begin{align*}
& P_1(x) - P_1(x-1) = 1 \\& P_1(0) = 0
\end{align*}
$$

    が成立する．
    $n \in \mathbb{N}$として$x=n+1$を代入すると
    

$$
\begin{align*}
P_1(n+1) = P_1(n) + 1 \\
        P_1(0) = 0
\end{align*}
$$

    だから，漸化式を繰り返し用いて任意の自然数$n$に対して
    

$$
\begin{align*}
P_1(n) = n
\end{align*}
$$

    である．$P_1(x)$は一次式だから$n$を$x$で置き換えて
    

$$
\begin{align*}
P_1(x) = x
\end{align*}
$$

    である．$\cdots$(答)

    
    **$k=2$の時** \\

    題意より$P_2(x)$は二次式であって，全ての$x$に対して
    

$$
\begin{align*}
& P_2(x) - P_2(x-1) = x \\& P_2(0) = 0
\end{align*}
$$

    が成り立つ．$k=1$の時と同様，自然数$n$に対して$x=n+1$を代入して
    

$$
\begin{align*}
& P_2(n+1) = P_2(n) + (n+1) \\& P_2(0) = 0
\end{align*}
$$

    だから，漸化式を繰り返し用いて任意の自然数$n$に対して
    

$$
\begin{align*}
P_2(n)
         & = P_2(0) + \sum_{i=1}^{n} i \\
        = \frac{1}{2}n(n+1)
\end{align*}
$$

    である．$P_2(x)$は二次式だから$n$を$x$で置き換えて
    

$$
\begin{align*}
P_2(x) = \frac{1}{2}x(x+1)
\end{align*}
$$

    である．$\cdots$(答)

    
    （2）
    (1)と同様に一般の$k$，および自然数$n$に対して
    

$$
\begin{align*}
& P_k(n+1) = P_k(n) + (n+1)^{k-1}\\& P_k(0) = 0
\end{align*}
$$

    だから，漸化式を繰り返し用いて任意の自然数$n$に対して
    

$$
\begin{align}
P_k(n)
         & = P_k(0) + \sum_{i=1}^n i^{k-1}\\& = \sum_{i=1}^n i^{k-1}\label{2000-1:eq:1}
\end{align}
$$

    である．
    題意を示すには，[(式1)](#2000-1:eq:1)をみたす$k$次多項式$P_k(x)$が唯一存在することを示せば良い．
    証明は数学的帰納法による．

    (1)から、$k=1,2$の時は成立するため，以下$k \leqq l \ (l \in \mathbb{N} \geqq 2)$の成立を仮定する．
    二項定理より
    

$$
\begin{align*}
(i+1)^{l+1} - i^{l+1}& = \sum_{t=0}^{l+1}{}_{l+1}C_{t} i^t - i^{l+1}\\& = \sum_{t=0}^{l}{}_{l+1}C_{t} i^t                       \\& = {}_{l+1}C_l i^{l} + \sum_{t=0}^{l-1}{}_{l+1}C_{t} i^t \\& = (l+1)i^{l} + \sum_{t=0}^{l-1}{}_{l+1}C_{t} i^t
\end{align*}
$$

    だから，$i=1,2,\cdots, n$として足し合わせて
    

$$
\begin{align*}
(n+1)^{l} - 1
         & = \sum_{i=1}^{n}(l+1)i^{l}  + \sum_{i=1}^{n}\sum_{t=0}^{l-1}{}_{l+1}C_{t} i^t               \\& = (l+1) \sum_{i=1}^{n} i^{l} + \sum_{t=0}^{l-1}{}_{l+1}C_{t}\left[\sum_{i=1}^{n} i^t \right]\\& = (l+1) \sum_{i=1}^{n} i^{l} + \sum_{t=0}^{l-1}{}_{l+1}C_{t} P_{t+1}(n)
\end{align*}
$$

    である．ただし最後の行の二項目で仮定を用いた．
    整理して
    

$$
\begin{align*}
\sum_{i=1}^{n} i^{l} = \frac{1}{l+1}\left[(n+1)^{l} - 1 - \sum_{t=0}^{l-1}{}_{l+1}C_{t} P_{t+1}(n)\right]
\end{align*}
$$

    だから，
    

$$
\begin{align*}
P_{l+1}(n) = \frac{1}{l+1}\left[(n+1)^{l} - 1 - \sum_{t=0}^{l-1}{}_{l+1}C_{t} P_{t+1}(n)\right]
\end{align*}
$$

    は[(式1)](#2000-1:eq:1)を満たす．
    これが任意の$n \in \mathbb{N}$で成立し，かつ$P_{l+1}(x)$は題意より$l+1$次式だから，$P_{l+1}(x)$は
    $n$を$x$で置き換えて
    

$$
\begin{align}
P_{l+1}(x) = \frac{1}{l+1}\left[(x+1)^{l+1} - 1 - \sum_{t=0}^{l-1}{}_{l+1}C_{t} P_{t+1}(x) \right]\label{2000-1:eq:2}
\end{align}
$$

    とかけることが必要である．

    この$P_{l+1}(x)$が実際ただ一つであって，$l+1$次多公式であり，かつ条件(C)を満たすことを示そう．
    仮定より$k \le l$については成立しているから，第三項は$l$次以下である．第一項が一番次数が高く，よって$P_{l+1}(x)$は$l+1$次多項式である．
    同様に第三項はただ一つ存在するから，$P_{l+1}(x)$もただ一つ存在する．

    最後に条件(C)について考える．一つ目の条件は
    

$$
\begin{align*}
& P_{l+1}(x) - P_{l+1}(x-1)                                                                                                  \\& = \frac{1}{l+1}\left[(x+1)^{l+1} - x^{l+1} - \sum_{t=0}^{l-1}{}_{l+1}C_{t}\left(P_{t+1}(x)-P_{t+1}(x-1)\right)\right]\\& = \frac{1}{l+1}\left[(x+1)^{l+1} - x^{l+1} - \sum_{t=0}^{l-1}{}_{l+1}C_{t} x^{t}\right]\\& = \frac{1}{l+1}\left[\sum_{t=0}^{l+1}{}_{l+1}C_{t} x^{t} - x^{l+1} - \sum_{t=0}^{l-1}{}_{l+1}C_{t} x^{t}\right]\\& = \frac{1}{l+1}\left[{}_{l+1}C_{l} x^{t}\right]\\& = \frac{1}{l+1}\left[(l+1) x^{t}\right]\\& = x^l
\end{align*}
$$

    より満たされる．ただし3行目で二項定理により$(x+1)^{l+1}$を展開した．

    次に，二つ目の条件は[(式2)](#2000-1:eq:2)に$x=0$を代入して，仮定より
    

$$
\begin{align*}
P_{l+1}(0)
         & = \frac{-1}{l+1}\sum_{t=0}^{l-1}{}_{l+1} C_{t} P_{t+1}(0) \\& = \frac{-1}{l+1}\sum_{t=0}^{l-1}{}_{l+1} C_{t} 0          \\& = 0 \quad(\because\text{仮定})
\end{align*}
$$

    より満たされる．

    以上より[(式2)](#2000-1:eq:2)の$P_{l+1}(x)$は条件(C)をみたす．
    以上から$k=l+1$でも題意は成立する．

    よって，数学的帰納法より，任意の$k\in\mathbb{N}\geqq 2$に対して題意が示された．$\cdots$(答)

    
    (3)
    題意の条件から$k$次多項式$Q_k(x)$は$x=0, 1, \dots, k-1$を零点に持つので，因数定理より$a \in \mathbb{R}$として
    

$$
\begin{align}
Q_k(x) = a \prod_{t=0}^{k-1}(x-t) \label{2000-1:eq:3}
\end{align}
$$

    とかける．$Q_{k}(k)=1$だから，$x=k$を代入して
    

$$
\begin{align*}
& 1 = Q_{k}(k) =  a (k!) \\\therefore& a = \frac{1}{k!}
\end{align*}
$$

    だから，[(式3)](#2000-1:eq:3)に代入して
    

$$
\begin{align}
Q_k(x) = \frac{1}{k!}\prod_{t=0}^{k-1}(x-t) \label{2000-1:eq:4}
\end{align}
$$

    である．

    さて，$P_k(x), Q_k(x)$は共に$k$次多項式だから、
    $P_k(x)$を$Q_k(x)$でわった商は定数$d_k$とおけ, あまりは$k-1$次以下の多項式$R_k(x)$になる．
    すなわち
    

$$
\begin{align*}
P_{k}(x) = d_k Q_k(x) + R_{k}(x)
\end{align*}
$$

    と書ける．
    さらに$R_{k}(x)$を$Q_{k-1}(x)$でわった商は定数$d_{k-1}$, あまりは$k-2$次以下の多項式$R_{k-1}(x)$になる．
    すなわち
    

$$
\begin{align*}
R_{k}(x) = d_{k-1} Q_{k-1}(x) + R_{k-1}(x)
\end{align*}
$$

    と書ける．以下$i$次以下の多項式$R_{i+1}(x)$を$i$次多項式$Q_{i}(x)$で割った商を定数$d_{i}$，あまりを$i-1$次以下の多項式$R_{i}(x)$とおく．
    最後$R_{0}(x)$は定数だから，分かりやすいようにこれを$R_{0}$と書く．
    この式を繰り返し用いて，
    

$$
\begin{align}
P_{k}(x)
         & = d_{k}Q_{k}(x) + d_{k-1}Q_{k-1}(x) + \cdots d_{1}Q_{1}(x) + R_{0}\\& = \sum_{i=1}^k d_i Q_i(x) + R_{0}\label{2000-1:eq:5}
\end{align}
$$

    を得る．

    従って，題意を示すには，
    

$$
\begin{align}
& d_{i}\in\mathbb{Z}& (i=1,2,\cdots, k) \label{2000-1:eq:6}\\& R_{0} = 0  \label{2000-1:eq:7}
\end{align}
$$

    の二つの条件を示せば良い．
    まず[(式7)](#2000-1:eq:7)について，
    条件(C)より$P_{k}(0)=0$であり，また[(式4)](#2000-1:eq:4)より$Q_{k}(0)=0$も従う．
    これらを[(式5)](#2000-1:eq:5)に代入して$R_{0}=0$であるから示された．

    よって[(式5)](#2000-1:eq:5)は
    

$$
\begin{align*}
P_{k}(x) = \sum_{i=1}^k d_i Q_i(x)
\end{align*}
$$

    と書き直せる．このもとで[(式6)](#2000-1:eq:6)を示す．
    自然数$n$に対して$x=n$を代入すると
    

$$
\begin{align}
P_{k}(n) = \sum_{i=1}^k d_i Q_i(n)
\end{align}
$$

    であり，左辺は[(式1)](#2000-1:eq:1)を代入して
    

$$
\begin{align*}
\sum_{i=1}^n i^{k-1} = \sum_{i=1}^k d_i Q_i(n)
\end{align*}
$$

    である．
    右辺は[(式4)](#2000-1:eq:4)より，
    

$$
\begin{align*}
& Q_{i}(n) = 0           & (i \ge n+1) \\& Q_{i}(n) = {}_{n}C_{i}& (i \le n)
\end{align*}
$$

    であることに注意すると，$n \le k$に対して
    

$$
\begin{align*}
\sum_{i=1}^n i^{k-1}& = \sum_{i=1}^{n} d_i {}_{n}C_{i}
\end{align*}
$$

    である．以下数学的帰納法により$d_i$が整数であることを示す．
    $n=1$の時は
    

$$
\begin{align*}
1
         & = d_{1}\cdot{}_{1}C_{1}\\& = d_{1}
\end{align*}
$$

    より，$d_{1}$は整数である．
    次に$n\ge 2$の時は
    

$$
\begin{align*}
\sum_{i=1}^n i^{k-1}& = d_n {}_{n}C_{n} + \sum_{i=1}^{n-1} d_i {}_{n}C_{i}\\& = d_n + \sum_{i=1}^{n-1} d_i {}_{n}C_{i}
\end{align*}
$$

    であり，$d_1,\cdots,d_{n-1}$が整数ならば，$d_n$も整数である．
    以上より帰納的に$d_1,d_2,\cdots,d_{k}$は整数である．

    従って題意は示された．$\cdots$(答)

    
    

## 【解説】