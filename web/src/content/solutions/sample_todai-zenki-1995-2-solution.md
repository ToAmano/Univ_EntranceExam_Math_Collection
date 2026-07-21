---
university: "sample_todai"
category: "zenki"
year: "1995"
question: "2"
type: "solution"
title: "SAMPLE_TODAI 1995 zenki Q2 (solution)"
---

**【解】**

### (1)

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \begin{axis}[
          axis equal,
          xmin=-1.5, xmax=2.5,
          ymin=-1.5, ymax=1.5,
          xlabel=x, ylabel=y,
          axis lines=middle,
          xtick={2},
          samples=100,
          clip=false,
        ]
        \addplot [name path=circle1, domain=-1:1,draw=black] {sqrt(1-x^2)};
        \addplot [name path=circle1neg, domain=-1:1,draw=black] {-sqrt(1-x^2)};
        \addplot [name path=circle2, domain=0:2,draw=black] {sqrt(1-(x-1)^2)};
        \addplot [name path=circle2neg, domain=0:2,draw=black] {-sqrt(1-(x-1)^2)};

        \fill [pattern=north east lines] (axis cs:0,0) circle (1);
        \fill [pattern=north east lines] (axis cs:1,0) circle (1);

        \node[fill=white] at (axis cs:0,0) [below left] {P};
        \node[fill=white] at (axis cs:1,0) [below right] {Q};
        \node at (axis cs:0.3,1.2) [above left] {E};
        \node at (axis cs:2.1,0.3) [above right] {F};

        \coordinate (A) at (axis cs:-0.5,0.7);
        \coordinate (B) at (axis cs:-0.6,-0.75);
        \coordinate (C) at (axis cs:1.7,0.2);
        \draw[red, thick] (A) -- (B) -- (C) -- cycle;
        \fill[red] (A) circle (2pt) node[fill=white,above] {A};
        \fill[red] (B) circle (2pt) node[fill=white,below left] {B};
        \fill[red] (C) circle (2pt) node[fill=white,above right] {C};

      \end{axis}
    \end{tikzpicture}
    \caption{点ABCの様子}
    \label{1995-2:fig:1}
  \end{figure}

  $\mathrm{PQ}=1$ だから， $\mathrm{P}(0,0)$, $\mathrm{Q}(1,0)$ とし,
  $\triangle \mathrm{ABC}$ が $xy$ 平面にあるとする.
  (条件)をみたす時,$A,B,C$ は\cref{1995-2:fig:1}の斜線部分内にある.

  もし $A,B,C$ が\cref{1995-2:fig:1}で斜線部で, 境界を含まない部分にあるとすると $C$ から $AB$ に下ろした垂線と $E,F$ との交点のうち, 垂足 $H$ との距離が $\overline{CH}$ よりも大きいもの $C'$ が存在し
  $\triangle \mathrm{ABC} < \triangle \mathrm{ABC'}$ となる.
  したがって, $\triangle \mathrm{ABC}$ が最大の時, $C$ は $E$ 又は $F$ にある.
  他の頂点についても同様のことがいえるから題意は示された.

  $\cdots$(答)

### (2)

  Pを固定した時, ABにPから下した垂足をHとする.
  Hは $x^2+y^2=p^2$ 上を動く.
  この時三角形PAHを考えると
  
$$
\begin{align*}
    \overline{AB}
     & = 2\overline{AH} \\
     & = 2\sqrt{1-p^2}
  \end{align*}
$$

  で一定である．

  従って，この時E，F上でABからの距離が最大の点がCの時, $\triangle \mathrm{ABC}$ は最大である.
  そこで$0\le \theta < 2\pi$に対して
  
$$
\begin{align*}
    \vec{\mathrm{PH}} = p \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}
  \end{align*}
$$

  と置く．

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \def\p{0.7}
      \def\thetaVal{140}
      \pgfmathsetmacro{\tval}{sqrt(1-\p*\p)}
      \begin{axis}[
          axis equal,
          xmin=-1.5, xmax=2.5,
          ymin=-1.5, ymax=1.5,
          xlabel=x, ylabel=y,
          axis lines=middle,
          xtick={\empty},
          ytick={\empty},
          samples=100,
          clip=false,
        ]
        \addplot [name path=circle1, domain=-1:1,draw=black] {sqrt(1-x^2)};
        \addplot [name path=circle1neg, domain=-1:1,draw=black] {-sqrt(1-x^2)};
        \addplot [name path=circle2, domain=0:2,draw=black] {sqrt(1-(x-1)^2)};
        \addplot [name path=circle2neg, domain=0:2,draw=black] {-sqrt(1-(x-1)^2)};
        \addplot [dashed,domain=-\p:\p,draw=black] {sqrt(\p^2-x^2)};
        \addplot [dashed,domain=-\p:\p,draw=black] {-sqrt(\p^2-x^2)};

        \node[fill=white] at (axis cs:0,0) [below left] {P};
        \node[fill=white] at (axis cs:1,0) [below right] {Q};
        \node at (axis cs:0.3,1.2) [above left] {E};
        \node at (axis cs:2.1,0.3) [above right] {F};

        \coordinate (H)  at (axis cs:{\p*cos(\thetaVal)}, {\p*sin(\thetaVal)});
        \coordinate (X1) at (axis cs:{-cos(\thetaVal)}, {-sin(\thetaVal)});
        \coordinate (X2) at (axis cs:{cos(\thetaVal)}, {sin(\thetaVal)});
        \coordinate (X3) at (axis cs:{1+cos(\thetaVal)}, {sin(\thetaVal)});
        \coordinate (X4) at (axis cs:{1-cos(\thetaVal)}, {-sin(\thetaVal)});

        \fill[blue] (H)  circle (2pt) node[above] {$H$};
        \fill[red]  (X1) circle (2pt) node[below] {$X_1$};
        \fill[red]  (X2) circle (2pt) node[above] {$X_2$};
        \fill[red]  (X3) circle (2pt) node[above] {$X_3$};
        \fill[red]  (X4) circle (2pt) node[below] {$X_4$};

        \draw[dashed] (X1) -- (X2);
        \draw[dashed] (X3) -- (X4);
        \draw[blue, thick] (axis cs:0,0) -- (H);

        \coordinate (P) at (axis cs:0,0);
        \coordinate (Q) at (axis cs:1,0);
        \pic [draw, "$\theta$", angle eccentricity=1.2] {angle = Q--P--H};

        \coordinate (A) at (axis cs:{\p*cos(\thetaVal) - \tval*sin(\thetaVal)}, {\p*sin(\thetaVal) + \tval*cos(\thetaVal)});
        \coordinate (B) at (axis cs:{\p*cos(\thetaVal) + \tval*sin(\thetaVal)}, {\p*sin(\thetaVal) - \tval*cos(\thetaVal)});

        \draw[thick, green!50!black] (A) -- (B);

        \fill[green!50!black] (A) circle (2pt) node[above left] {A};
        \fill[green!50!black] (B) circle (2pt) node[above] {B};
        \pic [draw, red, angle eccentricity=1.3, angle radius=0.2cm] {right angle = A--H--P};

      \end{axis}
    \end{tikzpicture}
    \caption{点A，B，Cの様子}
    \label{1995-2:fig:2}
  \end{figure}

  点CがE，F上でABからの距離が最大のとき，点Cでの円の接線の法線ベクトルも
  
$$
\begin{align}
    \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix} \label{1995-2:eq:1}
  \end{align}
$$

  である．
  このような点はE上に2点, F上に2点あるので，E上のものを$X_1, X_2$，F上のものを$X_3, X_4$とすると
  $X_1,X_2$について
  
$$
\begin{align}
    \begin{dcases}
      \overline{HX_1} = 1 + p \\
      \overline{HX_2} = 1 - p
    \end{dcases} \label{1995-2:eq:2}
  \end{align}
$$

  であり，$X_3, X_4$については\cref{1995-2:eq:1}より
  
$$
\begin{align*}
     & X_3(1+\cos\theta, \sin\theta) \\
     & X_4(1-\cos\theta, \sin\theta)
  \end{align*}
$$

  として良い．
  $X_3,X_4$と線分ABの距離を$L_3,L_4$とすると
  
$$
\begin{align}
    \begin{dcases}
      L_3 = |\cos\theta(1+\cos\theta)+\sin^2\theta-p| = |1-p+\cos\theta| \\
      L_4 = |\cos\theta(1-\cos\theta)-\sin^2\theta-p| = |-1-p+\cos\theta|
    \end{dcases}\label{1995-2:eq:3}
  \end{align}
$$

  である．$0 \le p \le 1$および$-1 \le \cos\theta \le 1$から，\cref{1995-2:eq:2,1995-2:eq:3}のうちで最大のものは
  $L_4$において$\cos\theta = -1$として時で
  
$$
\begin{align*}
    \max L_4 = (p+2)
  \end{align*}
$$

  である．

  この時，$\cos\theta=-1$より$\theta=\pi$となって，確かに$\mathrm{PQ} \perp \mathrm{AB}$ である．
  よって題意は示された．
  $\cdots$(答)

### (3)

### (2)
の結果から $p$を固定した時に $S$を最大にするのは
  \cref{1995-2:fig:3}のようにHが$x$軸上に存在する時である．

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \def\p{0.7}
      \def\thetaVal{180}
      \pgfmathsetmacro{\tval}{sqrt(1-\p*\p)}
      \begin{axis}[
          axis equal,
          xmin=-1.5, xmax=2.5,
          ymin=-1.5, ymax=1.5,
          xlabel=x, ylabel=y,
          axis lines=middle,
          xtick={\empty},
          ytick={\empty},
          samples=100,
          clip=false,
        ]
        \addplot [name path=circle1, domain=-1:1,draw=black] {sqrt(1-x^2)};
        \addplot [name path=circle1neg, domain=-1:1,draw=black] {-sqrt(1-x^2)};
        \addplot [name path=circle2, domain=0:2,draw=black] {sqrt(1-(x-1)^2)};
        \addplot [name path=circle2neg, domain=0:2,draw=black] {-sqrt(1-(x-1)^2)};
        \addplot [dashed,domain=-\p:\p,draw=black] {sqrt(\p^2-x^2)};
        \addplot [dashed,domain=-\p:\p,draw=black] {-sqrt(\p^2-x^2)};

        \node[fill=white] at (axis cs:0,0) [below left] {P};
        \node[fill=white] at (axis cs:1,0) [below right] {Q};
        \node at (axis cs:0.3,1.2) [above left] {E};
        \node at (axis cs:2.1,0.3) [above right] {F};

        \coordinate (H)  at (axis cs:{\p*cos(\thetaVal)}, {\p*sin(\thetaVal)});
        \coordinate (C) at (axis cs:{1-cos(\thetaVal)}, {-sin(\thetaVal)});

        \fill[blue] (H)  circle (2pt) node[above left] {$H$};

        \draw[blue, thick] (axis cs:0,0) -- (H);

        \coordinate (P) at (axis cs:0,0);
        \coordinate (Q) at (axis cs:1,0);

        \coordinate (A) at (axis cs:{\p*cos(\thetaVal) - \tval*sin(\thetaVal)}, {\p*sin(\thetaVal) + \tval*cos(\thetaVal)});
        \coordinate (B) at (axis cs:{\p*cos(\thetaVal) + \tval*sin(\thetaVal)}, {\p*sin(\thetaVal) - \tval*cos(\thetaVal)});

        \draw[thick, green!50!black] (A) -- (B) -- (C) -- cycle;

        \fill[green!50!black]  (C) circle (2pt) node[above right] {$C$};
        \fill[green!50!black] (A) circle (2pt) node[above left] {A};
        \fill[green!50!black] (B) circle (2pt) node[above] {B};
        \pic [draw, red, angle eccentricity=1.3, angle radius=0.2cm] {right angle = A--H--P};

      \end{axis}
    \end{tikzpicture}
    \caption{$p$を固定した時，三角形ABCの面積が最大になるような場合．}
    \label{1995-2:fig:3}
  \end{figure}

  この時の面積$S(p)$として，
  
$$
\begin{align*}
    S(p)
     & = \frac{1}{2} \overline{AB}\cdot \overline{HC} \\
     & = \frac{1}{2} \cdot 2 \sqrt{1-p^2} \cdot (p+2) \\
     & = \sqrt{(1-p^2)(p+2)^2}                        \\
     & \equiv \sqrt{f(p)}
  \end{align*}
$$

  である．
  以下この最大値を求める．
  $f(p)$が最大の時$S(p)$も最大だから，$f(p)$の増減表を書く．
  一階微分は
  
$$
\begin{align*}
    f'(p)
     & = 2(p+2)(1-p^2) - 2p(p+2)^2 \\
     & = 2(p+2)(1-2p-2p^2)
  \end{align*}
$$

  より，\cref{1995-2:table:1}を得る．
  \begin{table}[H]
    \centering
    \caption{$f(p)$の増減表．}
    \label{1995-2:table:1}
    

| $p$ | $0$ | $\cdots$ | $\frac{-1+\sqrt{3}}{2}$ | $\cdots$ | $1$ |
|:----:|:---:|:----------:|:-----------------------:|:----------:|:---:|
| $f'$ | | $+$ | $0$ | $-$ | |
| $f$ | | $\nearrow$ | | $\searrow$ | |

  \end{table}

  したがって，$f$および$S$は$p=\frac{-1+\sqrt{3}}{2}$で最大値
  
$$
\begin{align*}
    \max S
     & = \sqrt{\max f(p)}                               \\
     & = \sqrt{f\left(\frac{-1+\sqrt{3}}{2}\right)}     \\
     & = \sqrt{\frac{1+2p}{2}} \frac{3+\sqrt{3}}{2}     \\
     & = \sqrt{\frac{\sqrt{3}}{2}} \frac{3+\sqrt{3}}{2}
  \end{align*}
$$

  をとる．

  **【解説】**

### (2)
の別解を紹介する．
  ABとPQのなす角を$\theta$とする. ABと平行に, Fの接線を引き, 接点をCとする.
  右図から, ABとCのキョリ$h$は
  $$ h = p + \sin\theta + 1 $$
  $\overline{AB}=\text{const}, p=\text{const}$から,
  $\triangle \mathrm{ABC}$が最大になるとき
  $h$が最大で $\theta = \pi/2$. (了)