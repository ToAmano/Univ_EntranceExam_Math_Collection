---
university: "kyodai"
category: "kouki"
year: "1989"
question: "6"
type: "solution"
title: "KYODAI 1989 kouki Q6 (solution)"
---

## 【解】

    帰納的に$f(x)\equiv 0$ とはならないから
    
$$
\begin{align*}
g_n(x) = \frac{1}{f_n(x)}
\end{align*}
$$

    とすると
    
$$
\begin{align*}
f_{n+1}(x) & = \frac{af_n(x)}{f_n(x)+1}
\end{align*}
$$

    の両辺逆数とって
    
$$
\begin{align*}
g_{n+1}(x) & = \frac{1}{a}(1+g_n(x))
\end{align*}
$$

    なる漸化式を得る．
    初期条件は $g_1(x) = \frac{1}{f_1(x)} = \frac{x+1}{ax}$ だから
    $a=1$か否かで場合わけして，
    

1.  [$1^\circ$] $a=1$ の時
              \begin{align*}
                  g_n(x) & = g_1(x) + (n-1) = \frac{x+1}{ax} + (n-1)
              \end{align*}

2.  [$2^\circ$] $0<a<1$ の時
              等比数列の公式から
              \begin{align*}
                  g_n(x)
                   & = \left(\frac{1}{a}\right)^{n-1} \left(\frac{x+1}{ax} - \frac{1}{a-1}\right) + \frac{1}{a-1}
              \end{align*}

    より
    

1.  [$1^\circ$] $a=1$ の時
              \begin{align*}
                  f_n(x) & = \frac{ax}{(x+1)+a(n-1)x} = \frac{x}{nx+1}
              \end{align*}

2.  [$2^\circ$] $0<a<1$ の時
              \begin{align*}
                  f_n(x) & = \frac{ax(a-1)}{\left(\frac{1}{a}\right)^{n-1} (-x+a-1) + ax}
              \end{align*}

    が求める一般項である．$\cdots$(答)

### (2)

    $a=1$か否かで場合わけして考える．

    

1.  [$1^\circ$] $a=1$ の時
              \begin{align*}
                  b_n        & = n \text{ とおけば}                                                                    \\
                  b_n f_n(c) & = \frac{nc}{nc+1} = \frac{1}{1+\frac{1}{nc}} \longrightarrow 1 \quad (n \to \infty)
              \end{align*}
              となって条件をみたす．

2.  [$2^\circ$] $a \neq 1$ の時
              \begin{align*}
                  b_n        & = \left(\frac{1}{a}\right)^{n-1} \text{ とおけば } |a|<1 \text{ から} \\
                  b_n f_n(c) & = \frac{a(a-1)c}{(a-1-c)+ac \cdot a^{n-1}}                      \\
                             & \longrightarrow \frac{ac(a-1)}{a-1-c} \quad (n \to \infty)
              \end{align*}
              となり，条件をみたす． ($\because c>0, 0<a<1$)

    以上から
    
$$
\begin{align*}
b_n = \begin{dcases}
                  n                              & (a=1)   \\
                  \left(\frac{1}{a}\right)^{n-1} & (0<a<1)
              \end{dcases}
\end{align*}
$$

    は条件をみたす．$\cdots$(答)

    

## 【解説】