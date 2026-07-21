---
university: "sample_todai"
category: "zenki"
year: "1993"
question: "3"
type: "solution"
title: "SAMPLE_TODAI 1993 zenki Q3 (solution)"
---

**【解】**
  $xy$平面で切断してかんがえる．
  対称性から球の中心は$y$軸上にある．
  そこで、円の中心をP$(0, t)$として，この円Cを
  
$$
\begin{align}
    x^2 + (y-t)^2 = r^2 \label{1993-3:eq:1}
  \end{align}
$$

  とかける．元の水面の高さは$4$だから求める値$s$は
  
$$
\begin{align}
    s = 4 - t
  \end{align}
$$

  である．

  円の半径に応じて，以下の3パターンの場合がありうる．
  一つ目は円が大きくて$(\pm 2,4)$で放物線の容器と交わる場合である．
  二つ目は円と放物線が$-2 \le x \le 2$で二つの接点を持つ場合である．
  最後に三つ目は円と放物線が$x=0$でのみ接点を持つ場合である．

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \def\myr{2.5}
      \def\myt{4 + sqrt(\myr^2 - 4)}
      \def\startangle{200} 
      \def\endangle{340}   

      \begin{axis}[
          axis lines=middle,
          xlabel=$x$,
          ylabel=$y$,
          xlabel style={anchor=north east},
          ylabel style={anchor=north east},
          xmin=-3, xmax=3,
          ymin=-1, ymax=6,
          xtick={-2, 2},
          ytick={\empty},
          axis equal image, 
          clip=false, 
        ]

        \addplot[
          thick,
          domain=\startangle:\endangle,
          samples=100,
          name path=arc
        ] ({ \myr * cos(x) }, { \myt + \myr * sin(x) });

        \addplot[
          thick,
          domain=-2:2,
          samples=100,
          name path=parabola
        ] {x^2};

        \addplot[pattern=north east lines]
        fill between[of=parabola and arc];

        \draw (axis cs:-2, 0) -- (axis cs:-2, 4) -- (axis cs:2, 4) -- (axis cs:2, 0);
        \node at (axis cs:-2.5, 5.5) {$1^{\circ}$};
      \end{axis}
    \end{tikzpicture}
    \caption{$1^{\circ}$の場合．}
    \label{1993-3:fig:1}
  \end{figure}

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \def\myr{1.5}
      \def\myt{\myr^2 + 1/4}
      \def\myu{sqrt(\myt-1/2)}
      \def\myuu{\myt-1/2}

      \begin{axis}[
          axis lines=middle,
          xlabel=$x$,
          ylabel=$y$,
          xlabel style={anchor=north east},
          ylabel style={anchor=north east},
          xmin=-3, xmax=3,
          ymin=-1, ymax=6,
          xtick={-2, 2},
          ytick={\empty},
          axis equal image, 
          clip=false, 
        ]

        \addplot[
          thick,
          domain=0:360,
          samples=100,
        ] ({ \myr * cos(x) }, { \myt + \myr * sin(x) });

        \addplot[
          thick,
          domain=-2:2,
          samples=100,
        ] {x^2};

        \addplot[
          draw=none,
          domain=-\myu:\myu,
          name path=parabola
        ] {x^2};

        \addplot[
          draw=none,
          domain=180:360,
          name path=arc
        ] ({ \myr * cos(x) }, { \myt + \myr * sin(x) });

        \addplot[pattern=north east lines]
        fill between[of=parabola and arc];

        \draw (axis cs:-2, 0) -- (axis cs:-2, 4) -- (axis cs:2, 4) -- (axis cs:2, 0);
        \draw[dashed] (axis cs:{\myu}, 0) -- (axis cs:{\myu}, {\myuu}) -- (axis cs:{-\myu}, {\myuu}) -- (axis cs:{-\myu}, 0);
        \draw[dashed] (axis cs:{\myu}, {\myuu}) -- (axis cs:{0}, {\myt}) --  (axis cs:{-\myu}, {\myuu});
        \fill[] (axis cs:{\myu}, {\myuu}) circle (1.5pt);
        \fill[] (axis cs:{-\myu}, {\myuu}) circle (1.5pt);
        \fill[] (axis cs:{0}, {\myt}) circle (1.5pt);

        \node[below] at (axis cs:{\myu}, 0) {$u$};
        \node[above left] at (axis cs:0, {\myt}) {$t$};

        \node at (axis cs:-2.5, 5.5) {$2^{\circ}$};
      \end{axis}
    \end{tikzpicture}
    \caption{$2^{\circ}$の場合．}
    \label{1993-3:fig:2}
  \end{figure}

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \def\myr{0.4}
      \def\myt{\myr}
      \def\myu{0}
      \def\myuu{0}

      \begin{axis}[
          axis lines=middle,
          xlabel=$x$,
          ylabel=$y$,
          xlabel style={anchor=north east},
          ylabel style={anchor=north east},
          xmin=-3, xmax=3,
          ymin=-1, ymax=6,
          xtick={-2, 2},
          ytick={\empty},
          axis equal image, 
          clip=false, 
        ]

        \addplot[
          thick,
          domain=0:360,
          samples=100,
        ] ({ \myr * cos(x) }, { \myt + \myr * sin(x) });

        \addplot[
          thick,
          domain=-2:2,
          samples=100,
        ] {x^2};

        \draw (axis cs:-2, 0) -- (axis cs:-2, 4) -- (axis cs:2, 4) -- (axis cs:2, 0);
        \fill[] (axis cs:{\myu}, {\myuu}) circle (1.5pt);
        \fill[] (axis cs:{0}, {\myt}) circle (1.5pt);

        \node[above left] at (axis cs:0, {\myt}) {$r$};

        \node at (axis cs:-2.5, 5.5) {$2^{\circ}$};
      \end{axis}
    \end{tikzpicture}
    \caption{$3^{\circ}$の場合．}
    \label{1993-3:fig:3}
  \end{figure}

  まず$2^{\circ}, 3^{\circ}$について考える．
  $0\le x \le 2$での$C$と$y=x^2$の接点Qの座標を$(u,u^2)$とすると，これら二曲線の$u$での接線が一致するので、$(x^2)'=2x$から
  
$$
\begin{align}
     & \begin{pmatrix} 1 \\ 2u \end{pmatrix} \cdot \vec{QP} = 0                                   \\
    \Leftrightarrow
     & \begin{pmatrix} 1 \\ 2u \end{pmatrix} \cdot \begin{pmatrix} 0-u \\ t-u^2 \end{pmatrix} = 0 \\
     & \Leftrightarrow
    u(2u^2+1-2t) = 0 \label{1993-3:eq:2}
  \end{align}
$$

  が成立する．

  また，CがQを通る条件から
  
$$
\begin{align}
     & u^2+(u^2-t)^2=r^2                            \\
    \therefore
     & u^4+(1-2t)u^2+t^2-r^2=0  \label{1993-3:eq:3}
  \end{align}
$$

  である．対称性から円は放物線と$(u,u^2), (-u,u^2)$のみで共通点を持たないといけないから，
  \cref{1993-3:eq:3}が実数解として重解のみを持てば良い．

  
  \textbf{$1^{\circ}$ $0<t \le \frac{1}{2}$ の時}

  \cref{1993-3:eq:2}を満たす$u$は$u=0$のみである．
  \cref{1993-3:eq:3}に代入して
  
$$
\begin{align*}
    t^2-r^2 = 0
  \end{align*}
$$

  で，$r,t>0$から$r=t$である．
  この時$3^{\circ}$のようになる．
  求める$s=4-t$は
  
$$
\begin{align}
     & s = 4 -r & \left(0 < r \le \frac{1}{2}\right)\label{1993-3:eq:4}
  \end{align}
$$

  である．

  
  \textbf{$2^{\circ}$ $t>\frac{1}{2}$の時}

  \cref{1993-3:eq:2}から
  
$$
\begin{align*}
    u =
    \begin{dcases}
      0 \\
      \sqrt{t-\frac{1}{2}}
    \end{dcases}
  \end{align*}
$$

  である．

  $u=0$の時は\cref{1993-3:eq:3}が成立するためには$r=t$が必要だが，
  この時\cref{1993-3:eq:3}は
  
$$
\begin{align*}
    u^2(u^2+(1-2t))=0
  \end{align*}
$$

  となり，$u=0$に加えて重解でない$u=\pm\sqrt{2t-1}$を解にもち不適である．

  そこで，$u=\sqrt{t-\frac{1}{2}}$である．まず，$u \le 2$であることから
  
$$
\begin{align}
     & \sqrt{t-\frac{1}{2}} \le 2          \\
    \therefore
     & t - \frac{1}{2} \le 4               \\
    \therefore
     & t \le \frac{9}{2} \label{1993-3:eq:5}
  \end{align}
$$

  である．

  \cref{1993-3:eq:3}に代入して
  
$$
\begin{align*}
     & \left(t-\frac{1}{2}\right)^2 + (1-2t)\left(t-\frac{1}{2}\right) + t^2 - r^2 = 0 \\
    \therefore
     & -\left(t^2-t+\frac{1}{4}\right) + t^2 - r^2 = 0                                 \\
    \therefore
     & t = r^2 + \frac{1}{4}
  \end{align*}
$$

  であることが必要である．この時\cref{1993-3:eq:5}より
  
$$
\begin{align*}
     & \frac{1}{2} \le t \le \frac{9}{2}                  \\
     & \frac{1}{2} \le  r^2 + \frac{1}{4} \le \frac{9}{2} \\
     & \frac{1}{4} \le  r^2  \le \frac{17}{4}             \\
     & \frac{1}{2} \le  r  \le \frac{\sqrt{17}}{2}
  \end{align*}
$$

  である．

  逆にこの時，\cref{1993-3:eq:3}は
  
$$
\begin{align*}
     & u^4 + (1-2t)u^2 + \left(t^2-t + \frac{1}{4}\right) = 0 \\
    \therefore
     & \left[u^2-\left(t-\frac{1}{2}\right)\right]^2 = 0
  \end{align*}
$$

  となって$u$について重解のみを持ち十分である．
  従って求める値$s$は
  
$$
\begin{align}
    s
     & = 4 - t                                                                                                           \\
     & = 4 - \left(r^2 + \frac{1}{4}\right)                                                                              \\
     & = \frac{15}{4} - r^2                 & \left(\frac{1}{2} \le  r  \le \frac{\sqrt{17}}{2}\right) \label{1993-3:eq:6}
  \end{align}
$$

  である．

  
  最後に，$1^{\circ}$の場合について考える．
  この時\cref{1993-3:eq:5}より，円の中心の$y$座標が
  
$$
\begin{align}
    t \ge \frac{9}{2} \label{1993-3:eq:7}
  \end{align}
$$

  であって，また円$C$が$(\pm2, 4)$を通るから
  
$$
\begin{align*}
    2^2 + (4-t)^2 = r^2 \\
    \therefore
    (4-t)^2 = r^2 -4
  \end{align*}
$$

  である．$t$の条件\cref{1993-3:eq:7}から$r$の条件は
  
$$
\begin{align*}
    r^2 -4 \ge \frac{1}{4} \\
    r \ge \frac{\sqrt{17}}{2}
  \end{align*}
$$

  である．

  この時円と放物線を連立した\cref{1993-3:eq:3}は
  
$$
\begin{align*}
     & u^4 + (1-2t)u^2 + t^2 -4 - (4-t)^2 = 0 \\
    \therefore
     & u^4 + (1-2t)u^2 + 8t -20 = 0           \\
    \therefore
     & (u^2-4)\left(u^2 - (2t-5)\right) = 0
  \end{align*}
$$

  だから，交点は$u=\pm 2, \pm\sqrt{2t-5}$である．
  $t \ge \frac{9}{2}$の時$\sqrt{2t-5}\ge 2$であるから，$0\le x <2$に他の交点は存在せず十分である．
  以上から$s$は
  
$$
\begin{align}
    s
     & = 4 - t                                                                      \\
     & = - \sqrt{r^2-4} & \left(r \ge \frac{\sqrt{17}}{2} \right) \label{1993-3:eq:8}
  \end{align}
$$

  以上三つの場合わけ\cref{1993-3:eq:4,1993-3:eq:6,1993-3:eq:8}をまとめて，$s$を$r$の関数として表すと
  
$$
\begin{align*}
    s & =
    \begin{dcases}
      4 - r              & \left(0 < r \le \frac{1}{2}\right)                       \\
      \frac{15}{4} - r^2 & \left(\frac{1}{2} \le  r  \le \frac{\sqrt{17}}{2}\right) \\
      - \sqrt{r^2-4}     & \left(r \ge \frac{\sqrt{17}}{2} \right)
    \end{dcases}
  \end{align*}
$$

  である．$\cdots$(答)

### (2)

  あふれ出る水の体積$V(r)$は$xy$平面で$0 \le y \le 4$とCの共通部分Tとして，
  Tを$y$軸まわりに回転した立体の体積に等しい．
  円$C$の上端の$y$座標$y_0$は
  
$$
\begin{align*}
    y_0
     & =t+r     \\
     & =(4-s)+r \\
     & =4+r-s   \\
     & =
    \begin{dcases}
      2r                   & \left(0 < r \le \frac{1}{2}\right)                       \\
      r^2+r-\frac{1}{4}    & \left(\frac{1}{2} \le  r  \le \frac{\sqrt{17}}{2}\right) \\
      4 + r + \sqrt{r^2-4} & \left(r \ge \frac{\sqrt{17}}{2} \right)
    \end{dcases}
  \end{align*}
$$

  で，これが4より大きいかで場合分けする．
  
$$
\begin{align*}
    \begin{dcases}
      0 < r \le \frac{3}{2} \text{の時} & y \le 4 \\
      \frac{3}{2} < r \text{の時}       & y \ge 4
    \end{dcases}
  \end{align*}
$$

  だから，各場合わけは以下のようになる．

  
  \textbf{㋐ $0 < r \le \frac{3}{2}$ の時}

  $V(r)$は球の体積に等しく
  
$$
\begin{align*}
    V(r) = \frac{4}{3}\pi r^3
  \end{align*}
$$

  であり，これは$r$について単調増加である．

  
  \textbf{㋑ $\frac{3}{2} \le r$ の時}

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \def\myr{2}
      \def\myt{\myr^2 + 1/4}
      \def\myu{sqrt(\myt-1/2)}
      \def\myuu{\myt-1/2}

      \begin{axis}[
          axis lines=middle,
          xlabel=$x$,
          ylabel=$y$,
          xlabel style={anchor=north east},
          ylabel style={anchor=north east},
          xmin=-3, xmax=3,
          ymin=-1, ymax=6,
          xtick={-2, 2},
          ytick={\empty},
          axis equal image, 
          clip=false, 
        ]

        \addplot[
          thick,
          domain=0:360,
          samples=100,
        ] ({ \myr * cos(x) }, { \myt + \myr * sin(x) });

        \addplot[
          thick,
          domain=-2:2,
          samples=100,
        ] {x^2};

        \addplot[
          draw=none,
          domain=-2:2,
          name path=parabola
        ] {4};

        \addplot[
          draw=none,
          domain=180:360,
          name path=arc
        ] ({ \myr * cos(x) }, { \myt + \myr * sin(x) });

        \addplot[pattern=north east lines]
        fill between[of=parabola and arc];

        \draw (axis cs:-2, 0) -- (axis cs:-2, 4) -- (axis cs:2, 4) -- (axis cs:2, 0);
        \draw[dashed] (axis cs:{\myu}, {\myuu}) -- (axis cs:{0}, {\myt}) --  (axis cs:{-\myu}, {\myuu});
        \fill[] (axis cs:{\myu}, {\myuu}) circle (1.5pt);
        \fill[] (axis cs:{-\myu}, {\myuu}) circle (1.5pt);
        \fill[] (axis cs:{0}, {\myt}) circle (1.5pt);

        \node[above left] at (axis cs:0, {\myt}) {$t$};
        \node[below left] at (axis cs:0, {\myt-\myr}) {$t-r$};

        \node at (axis cs:-2.5, 5.5) {$2^{\circ}$};
      \end{axis}
    \end{tikzpicture}
    \caption{Tは斜線部．}
    \label{1993-3:fig:4}
  \end{figure}

  Tの概形は\cref{1993-3:fig:4}の斜線部である．
  従って
  
$$
\begin{align*}
    V(r)
     & = \pi \int_{t-r}^{4} \left[r^2-(y-t)^2\right] dy        \\
     & = \pi \int_{-r}^{s} \left[r^2-y^2\right] dy             \\
     & = \pi \left[ \frac{2}{3}r^3+r^2s-\frac{1}{3}s^3 \right]
  \end{align*}
$$

  である．

  ここで(1)から
  
$$
\begin{align*}
    \frac{ds}{dr} & =
    \begin{dcases}
      -2r         & \left(r \le \frac{\sqrt{17}}{2}\right)  \\
      \frac{r}{s} & \left(\frac{\sqrt{17}}{2} \le r \right)
    \end{dcases}
  \end{align*}
$$

  であるから，$V(r)$の一階微分は
  
$$
\begin{align*}
    V'(r)
     & = \pi \left[ 2r(r+s)+s'(r^2-s^2) \right]                                                                                                                                                                                                                                     \\
     & = \pi \left[ 2r(r+s)+s'(r+s)(r-s) \right]                                                                                                                                                                                                                                    \\
     & = \pi \left(r+s\right)\left[ 2r+s'(r-s) \right]                                                                                                                                                                                                                              \\
     & = \begin{dcases}
           \pi 2r \left(r+s\right)\left( 1 + s - r \right) & \left(r \le \frac{\sqrt{17}}{2}\right)  \\
           \pi \frac{r(r+s)^2}{s} < 0                      & \left(\frac{\sqrt{17}}{2} \le r \right)
         \end{dcases}                                                                                                                                                    \\
     & = \begin{dcases}
           \pi 2r\left(-r^2+r+\frac{15}{4}\right)\left(-r^2-r+\frac{19}{4}\right) & \left(r \le \frac{\sqrt{17}}{2}\right)  \\
           \pi \frac{r(r+s)^2}{s} < 0                                             & \left(\frac{\sqrt{17}}{2} \le r \right)
         \end{dcases}                                                                                                                             \\
     & = \begin{dcases}
           \pi 2r\left(r+\frac{3}{2}\right)\left(r-\frac{5}{2}\right)\left(r-\frac{-1+2\sqrt{5}}{2}\right)\left(r-\frac{-1-2\sqrt{5}}{2}\right) & \left(r \le \frac{\sqrt{17}}{2}\right)  \\
           \pi \frac{r(r+s)^2}{s} < 0                                                                                                           & \left(\frac{\sqrt{17}}{2} \le r \right)
         \end{dcases}
  \end{align*}
$$

  である．
  従って$V(r)$の増減表は\cref{1993-3:table:1}となる．

  \begin{table}[H]
    \centering
    \caption{$V(r)$の増減表}
    \label{1993-3:table:1}
    

| $r$ | $\frac{3}{2}$ | $\cdots$ | $\frac{-1+\sqrt{21}}{2}$ | $\cdots$ | $\frac{\sqrt{17}}{2}$ | |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $V'$ | | $+$ | $0$ | $-$ | | $-$ |
| $V$ | | $\nearrow$ | | $\searrow$ | | $\searrow$ |

  \end{table}

  したがって$V(r)$が最大になるのは
  
$$
\begin{align*}
    r=\frac{-1+2\sqrt{5}}{2}
  \end{align*}
$$

  の時である．$\cdots$(答)

  

  **【解説】**