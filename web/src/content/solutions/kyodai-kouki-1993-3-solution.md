---
university: "kyodai"
category: "kouki"
year: "1993"
question: "3"
type: "solution"
title: "KYODAI 1993 kouki Q3 (solution)"
---

## 【解】

  (1)
  点 $X_i$ に対しその位置ベクトルを $\vec{x}_i$ で定める．
  ただし，添え字$0$の点については例外的に$\vec{a}_0 = \vec{a}$ などとする．
  題意の条件から，$A_1,B_1,C_1,D_1$のベクトルは
  

$$
\begin{align*}
\vec{a}_1 & = \frac{1}{3}(\vec{b}' + \vec{c}' + \vec{d}') \\\vec{b}_1 & = \frac{1}{3}(\vec{a}' + \vec{c}' + \vec{d}') \\\vec{c}_1 & = \frac{1}{3}(\vec{a}' + \vec{b}' + \vec{d}') \\\vec{d}_1 & = \frac{1}{3}(\vec{a}' + \vec{b}' + \vec{c}')
\end{align*}
$$

  と表せる．
  新しく点$T$を
  

$$
\begin{align}
\vec{t} = \frac{1}{3}\left(\vec{a} + \vec{b} + \vec{c} + \vec{d}\right)\label{1993-3:eq:3}
\end{align}
$$

  で定めると，
  

$$
\begin{align*}
\vec{TA_1}& = -\frac{1}{3}\vec{a}\\\vec{TB_1}& = -\frac{1}{3}\vec{b}\\\vec{TC_1}& = -\frac{1}{3}\vec{c}\\\vec{TD_1}& = -\frac{1}{3}\vec{d}
\end{align*}
$$

  となり，題意の条件から$|\vec{a}| = |\vec{b}| = |\vec{c}| = |\vec{d}|$ であることより，
  

$$
\begin{align*}
|\vec{TA_1}| = |\vec{TB_1}| = |\vec{TC_1}| = |\vec{TD_1}|
\end{align*}
$$

  となる.

  つまり，$T$が求めるべき円の中心であり，
  

$$
\begin{align*}
\vec{P}_1 = \frac{1}{3}\left(\vec{a} + \vec{b} + \vec{c} + \vec{d}\right)
\end{align*}
$$

  となる．この時円の半径は$|\vec{a}/3$である． $\cdots$(答)

  
  (2)
  (1) と同様に考える．点$T_n$を
  

$$
\begin{align*}
\vec{t}_n = \frac{1}{3}(\vec{a}_n + \vec{b}_n + \vec{c}_n + \vec{d}_n)
\end{align*}
$$

  とすると，題意の条件より
  

$$
\begin{align}
\begin{dcases}
      \vec{a}_{n+1} & = \vec{t}_n - \frac{1}{3}\vec{a}_n \\
      \vec{b}_{n+1} & = \vec{t}_n - \frac{1}{3}\vec{b}_n \\
      \vec{c}_{n+1} & = \vec{t}_n - \frac{1}{3}\vec{c}_n \\
      \vec{d}_{n+1} & = \vec{t}_n - \frac{1}{3}\vec{d}_n
    \end{dcases}\label{1993-3:eq:1}
\end{align}
$$

  である．両辺足し合わせて
  

$$
\begin{align*}
3\vec{t}_{n+1} = 4\vec{t}_n-\vec{t}_n \\\therefore\vec{t}_{n+1} = \vec{t}_n
\end{align*}
$$

  であるから，この漸化式を繰り返し用いて，[(式3)](#1993-3:eq:3)より
  

$$
\begin{align*}
\vec{t}_n
     & = \vec{t}_1 = \vec{t}\\& = \frac{1}{3}\left(\vec{a} + \vec{b} + \vec{c} + \vec{d}\right)
\end{align*}
$$

  である．

  以下，$k=a,b,c,d$に対して$\vec{k}_n$の漸化式を考える．
  [(式1)](#1993-3:eq:1)より
  

$$
\begin{align*}
& \vec{k}_{n+1}                        = -\frac{1}{3}\vec{k}_n + \vec{t}\\\therefore& \vec{k}_{n+1} - \frac{3}{4}\vec{t} = -\frac{1}{3}(\vec{k}_n - \frac{3}{4}\vec{t})
\end{align*}
$$

  だから，等比数列の公式から
  

$$
\begin{align*}
\vec{k}_n = \left(-\frac{1}{3}\right)^n \left(\vec{k}_0 - \frac{3}{4}\vec{t}\right) + \frac{1}{4}\vec{t}
\end{align*}
$$

  となる．従って，
  

$$
\begin{align}
\vec{p}_n = \frac{3}{4}\vec{t} - \frac{3}{4}\vec{t}\left(-\frac{1}{3}\right)^n \label{1993-3:eq:2}
\end{align}
$$

  とおけば，
  

$$
\begin{align*}
|\vec{PK}_n| = \left|\left(-\frac{1}{3}\right)^n\right| |\vec{k}_0|
\end{align*}
$$

  となるが，題意の条件より$|a|=|b|=|c|=|d|$だから，これは$k$によらない一定値となる．
  従って，$A_n$, $B_n$, $C_n$, $D_n$ は $P_n$ を中心とする円周上にある．

  求めるベクトル$\vec{P_nP_{n+1}}$は[(式3)](#1993-3:eq:2,1993-3:eq:3)より
  

$$
\begin{align*}
\vec{P_n P_{n+1}}& = \frac{3}{4}\vec{t}\left[1 - \left(-\frac{1}{3}\right)^{n+1} - \left(1 - \left(-\frac{1}{3}\right)^n\right)\right]\\& = 3\frac{1}{3}\left(-\frac{1}{3}\right)^n \vec{t}\\& = -\left(-\frac{1}{3}\right)^{n+1}(\vec{a} + \vec{b}+ \vec{c} + \vec{d})
\end{align*}
$$

  である．$\cdots$(答)

  
  (3)
  $P_n$ の$n\to\infty$での極限の位置ベクトルを求めれば良い．
  [(式2)](#1993-3:eq:2)から，
  

$$
\begin{align*}
\vec{q}& = \lim_{n\to\infty}P_{n}\\& =\frac{3}{4}\vec{t}\\& = \frac{1}{4}\left(\vec{a} + \vec{b} + \vec{c} + \vec{d}\right)
\end{align*}
$$

  が求める位置ベクトルである．$\cdots$(答)

  

  

## 【解説】