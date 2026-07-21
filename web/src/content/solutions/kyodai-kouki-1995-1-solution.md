---
university: "kyodai"
category: "kouki"
year: "1995"
question: "1"
type: "solution"
title: "KYODAI 1995 kouki Q1 (solution)"
---

## 【解】

### (1)

    $x^n$ を $x^2+ax+b$ でわった商を $P_n(x)$ とおく．すなわち
    
$$
\begin{align*}
x^n = Pn(x)(x^2+ax+b) + r_n x + s_n
\end{align*}
$$

    である．$s_n$と$r_n$の漸化式を得るため，両辺に$x$をかけると
    
$$
\begin{align*}
x^{n+1}& = x P_n(x) (x^2+ax+b) + r_n x^2 + s_n x                \\& = (x P_n(x) + r_n) (x^2+ax+b) + (s_n - ar_n) x - b r_n
\end{align*}
$$

    これが$P_{n+1}(x)(x^2+ax+b) + r_{n+1} x + s_{n+1}$に等しいから
    係数比較して
    
$$
\begin{align*}
r_{n+1}& = s_n - ar_n \\
        s_{n+1}& = -b r_n
\end{align*}
$$

    を得る．二つ目の式を一つ目の式に代入して$s_n$を消去すると
    
$$
\begin{align}
r_{n+2} = -a r_{n+1} - b r_n \label{1995-1:eq:1}
\end{align}
$$

    である．初期条件は
    
$$
\begin{align}
& r_1 = 1                      & s_1 = 0 \label{1995-1:eq:2}\\& r_2 = -a \label{1995-1:eq:3}
\end{align}
$$

    である．
    題意の条件(イ)から，
    $\eqref{1995-1:eq:1}$の特性方程式$x^2+ax+b=0$の解は
    $x=\alpha,\beta$だから，漸化式を書き直して
    
$$
\begin{align*}
& r_{n+2} - \alpha r_{n+1} = \beta(r_{n+1}-\alpha r_{n}) \\& r_{n+2} - \beta  r_{n+1} = \alpha(r_{n+1}-\beta r_{n})
\end{align*}
$$

    より，これを初期条件$\eqref{1995-1:eq:2,1995-1:eq:3}$のもとで解いて，
    
$$
\begin{align*}
& r_{n+1} - \alpha r_{n} = \beta^{n-1}(-a-\alpha) \\& r_{n+1} - \beta r_{n} = \alpha^{n-1}(-a-\beta)
\end{align*}
$$

    解と係数の関係より$a=-\alpha-\beta$だから，
    
$$
\begin{align*}
& r_{n+1} - \alpha r_{n} = \beta^{n}\\& r_{n+1} - \beta r_{n} = \alpha^{n}
\end{align*}
$$

    となり，両辺引き算して
    
$$
\begin{align*}
& (\alpha - \beta) r_{n} = \alpha^n - \beta^n       \\\therefore& r_{n} = \frac{\alpha^n - \beta^n}{\alpha - \beta}
\end{align*}
$$

    を得る．ただし，(イ)の条件$0 < \beta < \alpha$より$\alpha-\beta\neq 0$であることを用いた．

    題意の条件(ロ) に代入して
    
$$
\begin{align*}
\frac{\alpha^n - \beta^n}{\alpha - \beta} < \frac{\alpha^{n+1} - \beta^{n+1}}{\alpha - \beta}
\end{align*}
$$

    が任意の自然数 $n$ で成立する．
    (イ) から $0 < \beta < \alpha$だから，両辺 $\alpha-\beta (>0)$ をかけてから$\beta^n (>0)$ で割って整理すると
    
$$
\begin{align}
\beta - 1 < \left(\frac{\alpha}{\beta}\right)^n (\alpha - 1) \label{1995-1:eq:4}
\end{align}
$$

    となる．
    よって題意は示された．$\cdots$(答)

### (2)

    (イ)，（ロ）と同値になる条件を考える．まず，(イ)は
    二次方程式
    
$$
\begin{align*}
f(x) = x^2+ax+b =0
\end{align*}
$$

    が$0<x$に異なる二つの実数解を持つことと同値である．

    このもとで，（ロ）の条件は（1）で求めた$\eqref{1995-1:eq:4}$と同値だから，
    $\eqref{1995-1:eq:4}$および，$f(x)=0$が$0<x$に異なる二つの実数解を持つ条件を求めれば良い．

    そこで，まず$\eqref{1995-1:eq:4}$から考える．
    これがが任意の自然数で成立するのは$0<\beta<\alpha$のもとで$\eqref{1995-1:table:1}$の時である．
    \begin{table}[H]
        \centering
        \caption{$\eqref{1995-1:eq:4}$が成立する$\alpha,\beta$の条件}
        \label{1995-1:table:1}
        

| | $0 < \alpha < 1$ | $\alpha = 1$ | $1 < \alpha$ |
|:---------------:|:----------------:|:------------:|:------------------------:|
| $0 < \beta < 1$ | $\times$ | $\circ$ | $\circ$ |
| $\beta = 1$ | $\times$ | $\times$ | $\circ$ |
| $1 < \beta$ | $\times$ | $\times$ | $1<\beta<\alpha$の時のみ |

    \end{table}

    したがって，$\eqref{1995-1:eq:4}$が任意の自然数で成立する $\alpha, \beta$ の条件は，
    
$$
\begin{align*}
0 < \beta < \alpha\land 1 \le\alpha
\end{align*}
$$

    の時である．

    したがって，もとめる $(a, b)$ の必要十分条件は
    「$x$ の二次方程式 $x^2+ax+b=0$ が二つの正の実解をもち，かつ
    大きい方の解が $1$ 以上であること」
    である．判別式を $D$ とすると，以下の二つの場合わけで全ての場合を尽くせる．

    **1$^\circ$ 2解とも $1$ 以上の時**

    この時は，判別式が$0$より大きくて軸$x=-a/2$が$1$以上，かつ$f(1)\ge 0$ならば良い．
    従って求める条件は
    
$$
\begin{align*}
& \begin{dcases}
               D > 0               \\
               1 \leq -\frac{a}{2} \\
               f(1) \geq 0
           \end{dcases}\\\iff& \begin{dcases}
               a^2-4b > 0 \\
               a \leq -2  \\
               1+a+b \geq 0
           \end{dcases}
\end{align*}
$$

    である．

    **2$^\circ$ 1つが $0 < x < 1$，もう1つが $1 \leq x$ の時**

    この時は，判別式が$0$より大きく，$f(0)>0$および$f(1)\le 0$であれば良い．
    従って求める条件は
    
$$
\begin{align*}
& \begin{dcases}
               f(1) \leq 0 \\
               D > 0       \\
               f(0) > 0
           \end{dcases}\\\iff& \begin{dcases}
               1+a+b \leq 0 \\
               a^2-4b > 0   \\
               b > 0
           \end{dcases}
\end{align*}
$$

    である．

    以上二つの場合をまとめて，求める条件は
    
$$
\begin{align*}
& \begin{dcases}
               a^2-4b > 0 \\
               a \leq -2  \\
               1+a+b \geq 0
           \end{dcases}\\\lor& \begin{dcases}
               1+a+b \leq 0 \\
               a^2-4b > 0   \\
               b > 0
           \end{dcases}
\end{align*}
$$

    であり，この領域は
    [図1](#1995-1:fig:1)の斜線部である． (境界は $b=-a-1$ のみ含み，白丸は含まず．)$\cdots$(答)

    

<figure id="1995-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1995/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 求める$(a,b)$の領域</figcaption>
</figure>

    
    

## 【解説】