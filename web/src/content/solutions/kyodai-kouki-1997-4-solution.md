---
university: "kyodai"
category: "kouki"
year: "1997"
question: "4"
type: "solution"
title: "KYODAI 1997 kouki Q4 (solution)"
---

## 【解】

### (1)

  $(a,b,c)$が与えられた連立方程式の解だから
  
$$
\begin{align}
\begin{dcases}
      b = 2a^2 - 1 \\
      c = 2b^2 - 1 \\
      a = 2c^2 - 1
    \end{dcases}\label{1997-4:eq:1}
\end{align}
$$

  が満たされる．

  背理法により題意を示す．
  $|a|>1$と仮定すると，$\eqref{1997-4:eq:1}$より$b>1,c>1,a>1$となる．
  従ってこの時，$a^2>a$などの不等式が成り立つ．
  $\eqref{1997-4:eq:1}$の全ての式を足し上げると
  
$$
\begin{align*}
a+b+c = 2(a^2+b^2+c^2)-3 > 2\left(a+b+c\right)-3 \\\therefore
    a+b+c <3
\end{align*}
$$

  を得るが，これは$a,b,c>1$に反して矛盾．よって背理法により$|a|\le 1$であり，
  この時$\eqref{1997-4:eq:1}$から$|b|\le 1, |c|\le 1$が従う．
  よって題意は示された．
  $\cdots$(答)

### (2)

### (1)
から
  
$$
\begin{align*}
& a = \cos\alpha& (0 \leqq\alpha < 2\pi)
\end{align*}
$$

  とおける．$\eqref{1997-4:eq:1}$および半角公式から
  
$$
\begin{align*}
b & = \cos 2\alpha\\
    c & = \cos 4\alpha\\
    a & =  \cos\alpha = \cos 8\alpha
\end{align*}
$$

  なる関係を得る．従って，最後の式を解く．和積公式から
  
$$
\begin{align*}
& \cos 8\alpha - \cos\alpha = 0                      \\& -2\sin\frac{9\alpha}{2}\sin\frac{7\alpha}{2} = 0
\end{align*}
$$

  であるから
  
$$
\begin{align*}
\sin\frac{9\alpha}{2} = 0 \lor\sin\frac{7\alpha}{2}
\end{align*}
$$

  である．$0 \leqq \alpha < 2\pi$ より$\alpha$は
  
$$
\begin{align*}
\alpha =
    \begin{dcases}
      \frac{4}{9} n \pi & (n=0,1,2,3,4) \\
      \frac{4}{7} k \pi & (k=0,1,2,3)
    \end{dcases}
\end{align*}
$$

  と書ける．$n=k=0$の時は$\alpha=0$で等しくなるが，そのほかの$n,k$では$\alpha$は相異なる値をとる．
  従って，求める解の個数は$n=0,1,2,3,4$, $k=1,2,3$の合計$8$個である．$\cdots$(答)

  
  

## 【解説】

  面白い問題で，色々と解法が考えられるところだ．
  まず(1)からいくつか別解を紹介しよう．いずれも$a,b,c$の対称性を用いることになる．
  まず，$|a|>1$を仮定すると$\eqref{1997-4:eq:1}$から$a,b,c>1$が従うことに気を付ける．
  これと背理法を組み合わせるのが全ての別解に共通するロジックである．

  **[（1）別解-1]**
  $b-a$を評価すると
  
$$
\begin{align*}
b-a
     & = 2a^2-a-1      \\& = (a-1)(2a+1)>0 \\\therefore& b>a
\end{align*}
$$

  だが，同様の評価を繰り返すと $a>c>b>a$ となり矛盾．

  
  **[（1）別解-2]**
  $a-1$を評価すると
  
$$
\begin{align*}
a-1
     & = 2c^2-2                   \\& = 2(c+1)(c-1)              \\& = 2(c+1) \cdot 2(b+1)(b-1) \\& = 8(c+1)(b+1)(a+1)(a-1)
\end{align*}
$$

  となり，$a-1 \ne 0$ で両辺を割れば
  
$$
\begin{align*}
1 = 8(c+1)(b+1)(a+1)
\end{align*}
$$

  となり矛盾する．

### (2)
の方も別解が考えられるので紹介しよう．
  対称性を使わないのであまり綺麗な方法ではないのだが，
  与えられた方程式は$3$変数なので，$1$変数消してしまおうという方針である．
  $\eqref{1997-4:eq:1}$からbを消去すると
  
$$
\begin{align*}
c = 2(2a^2-1)^2-1
\end{align*}
$$

  この右辺を$f(a)$とすると$f(a)$は$a$の4次関数で、$ac$平面上で
  $(0,1)$, $(\pm 1,1)$, $(\pm \frac{1}{\sqrt{2}}, -1)$を通り，
  
$$
\begin{align*}
a = 2c^2-1
\end{align*}
$$

  と合わせてグラフは[図1](#1997-4:fig:1)のようになる．

  

<figure id="1997-4:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1997/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $ac$平面に描いた連立方程式の様子</figcaption>
</figure>

  与えられた連立方程式の解の個数は，まさにグラフ上の二本の曲線の交点の数に他ならないから，
  求める解の個数は$8$個である．
  $\cdots$(答)