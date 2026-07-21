---
university: "kyodai"
category: "kouki"
year: "1999"
question: "3"
type: "solution"
title: "KYODAI 1999 kouki Q3 (solution)"
---

## 【解】

    
$$
\begin{align*}
2a_{n+1}& = \alpha(3a_n^2 + 2a_n b_n - b_n^2 - a_n + b_n) \\
        2b_{n+1}& = \alpha(-a_n^2 - 2a_n b_n - b_n^2 - a_n + b_n) \\
        a_1      & = b_1 = 1
\end{align*}
$$

### (1)

    初期条件$a_1=b_1=1$を用いて，
    与えられた漸化式に$n=1,2,3$を順に代入すると
    
$$
\begin{align*}
a_2 & = \frac{\alpha}{2}\cdot 4 = 2\alpha\\
        b_2 & = \frac{\alpha}{2}(-4) = -2\alpha\\
        a_3 & = \frac{\alpha}{2}(12\alpha^2 - 8\alpha^2 - 4\alpha^2 - 2\alpha - 2\alpha) = -2\alpha^2 \\
        b_3 & = \frac{\alpha}{2}(-4\alpha^2 + 8\alpha^2 - 4\alpha^2 - 2\alpha - 2\alpha) = -2\alpha^2 \\
        a_4 & = \frac{\alpha}{2}(12\alpha^4 + 8\alpha^4 - 4\alpha^4) = 8\alpha^5                      \\
        b_4 & = \frac{\alpha}{2}(-4\alpha^4 - 8\alpha^4 - 4\alpha^4) = -8\alpha^5
\end{align*}
$$

    となる．$\cdots$(答)
    

    （2）
    $X_n = a_n + b_n, Y_n = a_n - b_n$とおく．
    与えられた漸化式の辺々を足し引きして
    
$$
\begin{align*}
X_{n+1}& = \frac{\alpha}{2}\left[2a_n^2-2b_n^2-2a_n+2b_n\right]\\& = \alpha\left[(a_n+b_n)(a_n-b_n)-(a_n-b_n)\right]\\& = \alpha(X_n - 1) \cdot Y_n                            \\
        Y_{n+1}& = \frac{\alpha}{2}\left[4a_n^2+4a_nb_n\right]\\& = 2\alpha a_n(a_n+b_n)                                  \\& = \alpha(X_n+Y_n) \cdot X_n
\end{align*}
$$

    なる漸化式を得る．
    また，初期条件は(1)より
    
$$
\begin{align*}
& X_1  = 2, Y_1 = 0      \\& X_2 = 0, Y_2 = 4\alpha
\end{align*}
$$

    である．漸化式を繰り返し用いて
    
$$
\begin{align}
X_{n+2}& =  \alpha(X_{n+1} - 1) \cdot Y_{n+1}\\& = \alpha(X_{n+1} - 1) \cdot\alpha(X_n+Y_n)X_n           \\& = \alpha^2 (X_{n+1} - 1)(X_n+Y_n)X_n   \label{1999-3:eq:2}\\
        Y_{n+2}& = \alpha(X_{n+1}+Y_{n+1}) \cdot X_{n+1}\\& = \alpha(X_{n+1}+Y_{n+1}) \cdot\alpha(X_n - 1)Y_n        \\& = \alpha^2 (X_{n+1}+Y_{n+1})(X_n - 1)Y_n\label{1999-3:eq:3}
\end{align}
$$

    だから，$X_2=0$より漸化式から$X_4=X_6=\cdots = 0$，
    および，$Y_1=0$より漸化式から$Y_3=Y_5=\cdots = 0$となる．
    つまり$k\mathbb{N}$とおいて
    
$$
\begin{align}
\begin{dcases}
            X_{2k}   & = 0 \\
            Y_{2k-1} & = 0
        \end{dcases}\label{1999-3:eq:4}
\end{align}
$$

    となる．

    そこで次に$X_{2k+1}$および$Y_{2k}$について考えると，
    $\eqref{1999-3:eq:2}$で$n=2k-1$, $\eqref{1999-3:eq:3}$で$n=2k$とおいて
    $\eqref{1999-3:eq:4}$を用いて
    
$$
\begin{align}
X_{2k+1}& = \alpha^2 (X_{2k} - 1)(X_{2k-1}+Y_{2k-1})X_{2k-1}\\& = -\alpha^2 X^2_{2k-1}\label{1999-3:eq:5}\\
        Y_{2(k+1)}& =\alpha^2 (X_{2k+1}+Y_{2k+1})(X_{2k} - 1)Y_{2k}\\& = - \alpha^2 X_{2k+1}Y_{2k}\label{1999-3:eq:6}\\
\end{align}
$$

    となる．

    新しく
    
$$
\begin{align*}
Z_{k} = \frac{a_{2k+1}}{a_{2k}}
\end{align*}
$$

    とおくと，これを$X_n,Y_n$で書き換えて
    
$$
\begin{align*}
Z_{k} = \frac{X_{2k+1}+Y_{2k+1}}{X_{2k}+Y_{2k}}
\end{align*}
$$

    となる．$\eqref{1999-3:eq:4}$を代入して
    
$$
\begin{align*}
Z_{k} = \frac{X_{2k+1}}{Y_{2k}}
\end{align*}
$$

    となる．初期条件は(1)より
    
$$
\begin{align*}
Z_{1}& = \frac{X_{3}}{Y_{2}}\\& = \frac{a_{3}+b_{3}}{a_{2}-b_{2}}\\& = \frac{-2\alpha^2-2\alpha^2}{2\alpha+2\alpha}\\& = -\alpha
\end{align*}
$$

    である．
    $Z_{k}$の漸化式は$\eqref{1999-3:eq:5,1999-3:eq:6}$より
    
$$
\begin{align*}
Z_{k+1}& = \frac{X_{2(k+1)+1}}{Y_{2(k+1)}}\\& = \frac{-\alpha^2 X^2_{2k+1}}{- \alpha^2 X_{2k+1}Y_{2k}}\\& = \frac{X_{2k+1}}{Y_{2k}}\\& = Z_{k}
\end{align*}
$$

    となり，繰り返し用いて$Z_{1}=-\alpha$から
    
$$
\begin{align*}
Z_{k} = -\alpha
\end{align*}
$$

    となる．従って求める値は
    
$$
\begin{align*}
\frac{a_{2k+1}}{a_{2k}} = -\alpha
\end{align*}
$$

    である．$\cdots$(答)

    
    

## 【解説】

    $X_n$と$Y_n$の一般項を与えておこう．

    まず$X_{2k+1}$については漸化式を繰り返し用いて，初期条件$X_1=2$と合わせて，一般項は
    
$$
\begin{align*}
X_{2k-1}& = (-1)^{k-1}\alpha^{2^k-2}X_1^{2^{k-1}}\\& = (-1)^{k-1}\alpha^{2^k-2}2^{2^{k-1}}
\end{align*}
$$