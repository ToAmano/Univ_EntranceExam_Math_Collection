---
university: "todai"
category: "kouki"
year: "1991"
question: "1"
type: "solution"
title: "TODAI 1991 kouki Q1 (solution)"
---

## 【解】

### (1)
 題意の関数を
    
$$
\begin{align*}
f(x) = \frac{\log x}{x}
\end{align*}
$$

    とおくと，一階微分は
    
$$
\begin{align*}
f'(x) = \frac{1 - \log x}{x^2}
\end{align*}
$$

    だから，増減表は[表1](#1991-1:table:1)となる．

    

<figure id="1991-1:table:1" class="table-wrapper">

| $x$  |     $0$     |  $\dots$   |      $e$      |  $\dots$   |     | $\infty$ |
|:------:|:-------------:|:------------:|:---------------:|:------------:|:---:|:----------:|
| $f'$ |               |    $+$     |      $0$      |    $-$     |     |            |
| $f$  | $(-\infty)$ | $\nearrow$ | $\frac{1}{e}$ | $\searrow$ |     |  $(0)$   |

  <figcaption>表 1: $f(x)$の増減表</figcaption>
</figure>

    従って，グラフの概形は以下．$\cdots$(答)

    

<figure id="1991-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1991/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $y=f(x)$のグラフ</figcaption>
</figure>

### (2)

    $a, b > 0$ より，$a^b = b^a$ の両辺の自然対数をとって，
    
$$
\begin{align}
& \frac{\log a}{a} = \frac{\log b}{b}\\& f(a) = f(b) \label{1991-1:eq:1}
\end{align}
$$

    である．

### (1)
のグラフと $2 < e < 3$ より，対称性からまず $a < b$ として考えると
    
$$
\begin{align*}
a = 2
\end{align*}
$$

    が必要である．
    $\eqref{1991-1:eq:1}$に代入して
    
$$
\begin{align*}
\frac{\log 2}{2} = \frac{\log b}{b}
\end{align*}
$$

    である．
    $b=4$ はこの解であり，グラフより解は唯一存在するから，$b=4$のみが解である．
    従って$b>a$の時も考えて求める解は
    
$$
\begin{align}
(a,b) = (2,4), (4,2)\label{1991-1:eq:2}
\end{align}
$$

    である．$\cdots$(答)

### (3)

    背理法で示す．
    $x>0$を有理数として$x \neq 3$ とする．
    $3^x = x^3$ をみたす $x = \frac{a}{b}$ ($a,b \in \mathbb{N}, a,b$ は互いに素) があると仮定する．
    両辺自然対数をとると
    
$$
\begin{align*}
\frac{\log 3}{3} = \frac{\log x}{x}
\end{align*}
$$

    だから，(1)のグラフから，
    
$$
\begin{align}
1 < x < 3 \label{1991-1:eq:3}
\end{align}
$$

    が必要である．

    一方で
    $3^x = x^3$ に$x=b/a$を代入すると
    
$$
\begin{align*}
& 3^{b/a} = \left(\frac{b}{a}\right)^3 \\& 3^b = \left(\frac{b}{a}\right)^{3a}
\end{align*}
$$

    ここで$a$と$b$は互いに素だから $b \neq 1$ と仮定するとこの式は
    
$$
\begin{align*}
\text{(整数)} = \text{(非整数)}
\end{align*}
$$

    となり矛盾する．
    従って $b=1$ であり，$x=a \in \mathbb{N}$ となる．
    この時$\eqref{1991-1:eq:3}$より，$x=2$ が必要である．
    しかしこれは(2)の結果$\eqref{1991-1:eq:2}$ に矛盾する．

    以上より背理法によって，$3^x = x^3$ をみたす正の有理数は $x=3$ のみであることが示された．
    $\cdots$(答)
    
    

## 【解説】

    解答中で$2<e<3$であることを用いた．自然対数の値は
    
$$
\begin{align*}
e \sim 2.718281828
\end{align*}
$$

    である．これは「船人、ヤツは一発梯子（ふなびと、やつはいっぱつはしご）」という語呂合わせで値を覚えておくと良い．

    

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1991/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $y=1/x$の面積近似の様子．$S_3<S_1<S_2$が成立する．</figcaption>
</figure>

    流石に不要だと思うが念の為$2<e<3$の評価をその場で導出できるよう簡単な証明も紹介しよう．
    かなり緩い評価なので，$y=1/x$に対する台形近似を利用する．
    $1\le x \le e$の領域の面積$S_1$は
    
$$
\begin{align*}
S_1
         & = \int_{1}^{e}\frac{1}{x} dx   \\& = \left[\log x \right]_{1}^{e}\\& = 1
\end{align*}
$$

    である．
    $S_1$を上側から評価すると，$y=1/x$が下に凸だから図のような台形$S_2$で上側を抑えられて
    
$$
\begin{align*}
S_2
         & = \frac{1}{2}\left(\frac{1}{e}+1\right)\left(e-1\right)\\& = \frac{(1+e)(e-1)}{2e}
\end{align*}
$$

    である．

    同様に下側からの評価は$((1+e)/2,2/(1+e))$での接線で形作られる台形$S_3$で抑えられて
    
$$
\begin{align*}
S_3
         & = \frac{1}{2}\left(\frac{4}{1+e}\right)\left(e-1\right)\\& = \frac{2(e-1)}{1+e}
\end{align*}
$$

    である．

    以上より
    
$$
\begin{align*}
& S_3 < S_1 < S_2                                \\& \frac{2(e-1)}{1+e} < 1 < \frac{(1+e)(e-1)}{2e}
\end{align*}
$$

    で，それぞれとくと
    
$$
\begin{align*}
& \begin{dcases}
               2(e-1) < e+1 \\
               2e < (1+e)(e-1)
           \end{dcases}\\\therefore
        1+\sqrt{2} < e < 3
\end{align*}
$$

    となり，$e$の簡単な評価が得られる．