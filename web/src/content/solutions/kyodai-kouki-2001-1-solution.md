---
university: "kyodai"
category: "kouki"
year: "2001"
question: "1"
type: "solution"
title: "KYODAI 2001 kouki Q1 (solution)"
---

## 【解】

    与えられた関数を
    

$$
\begin{align*}
f(x,y,z) = x^2+2y^2+2z^2+2yz-2x(y+z)-5
\end{align*}
$$

    とおき，$f(x,y,z)=0$の正の整数解を求める．

    まず，$f(x,y,z)$は$y,z$について対称だから，そこから考える．
    $\alpha=y+z$, $\beta=yz$ とおく．$y$,$z$が正の整数である時，$\alpha,\beta$もまた正の整数である．
    従って，$\alpha,\beta$が正の整数であることが必要条件である．

    $y,z$ は $t$ の二次方程式
    

$$
\begin{align*}
g(t) = t^2-\alpha t+\beta=0
\end{align*}
$$

    の$2$ 正実解（重解含む）だから，$g(t)=0$の判別式$D$として
    

$$
\begin{align*}
\begin{dcases}
             & D \ge 0              \\
             & g(0) > 0             \\
             & \frac{\alpha}{2} > 0
        \end{dcases}
\end{align*}
$$

    を満たす必要がある．すなわち
    

$$
\begin{align}
\begin{dcases}
            \alpha^2-4\beta \ge 0 \\
            \alpha \ge 0          \\
            \beta \ge 0
        \end{dcases}\label{2001-1:eq:1}
\end{align}
$$

    が必要条件である．

    $\alpha,\beta$を利用して$f(x,y,z)$を書き直すと
    

$$
\begin{align*}
x^2-2\alpha x+2\alpha^2-2\beta-5=0
\end{align*}
$$

    であり，これがまた$x$について正の実数解を持つから，同様に判別式が$0$以上で
    

$$
\begin{align}
& \alpha^2-(2\alpha^2-2\beta-5) \ge 0                           \\\therefore& -\alpha^2+2\beta+5 \ge 0                                      \\& \beta\ge\frac{1}{2}\alpha^2-\frac{5}{2}\label{2001-1:eq:2}
\end{align}
$$

    であることが必要．

    [(式2)](#2001-1:eq:1,2001-1:eq:2)を$\alpha,\beta$平面に図示すると[図1](#2001-1:fig:1)の斜線部となる．

    

<figure id="2001-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2001/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $(\alpha,\beta)$の必要条件は斜線部境界含む．この中で唯一の格子点は$(3,2)$である．</figcaption>
</figure>

    この斜線部の中に含まれる格子点は $(3,2)$ だけだから，
    $(\alpha,\beta)=(3,2)$であることが必要であり，この時
    

$$
\begin{align*}
(y,z)=(2,1),(1,2)
\end{align*}
$$

    となる．この時，[(式2)](#2001-1:eq:2)に代入すると
    

$$
\begin{align*}
& x^2-6x+9=0 \\& (x-3)^2=0  \\\therefore& x=3
\end{align*}
$$

    となり，これは正の整数だから十分である．以上から，求める正整数解は
    

$$
\begin{align*}
(x,y,z)=(3,2,1), (3,1,2)
\end{align*}
$$

    である．$\cdots$(答)

    
    

## 【解説】