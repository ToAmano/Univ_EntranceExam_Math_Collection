---
university: "sample_titech"
category: "kouki"
year: "1990"
question: "1"
type: "solution"
title: "SAMPLE_TITECH 1990 kouki Q1 (solution)"
---

**【解】**

    実数 $x$ に対して $f(x) = (x+1)(x-2)$, $g(x) = 1+5x$ とおく．題意から，
    
$$
\begin{align}\label{1990-1:eq:1}
        g(x) \in \mathbb{Z}, \quad g(x) - \frac{1}{2} \le f(x) < g(x) + \frac{1}{2}
    \end{align}
$$

    をみたす $x \in \mathbb{R}$ をもとめればよい．
    $g(x) \in \mathbb{Z}$ から $5x \in \mathbb{Z}$．つまり，$x = \frac{t}{5}$ ($t \in \mathbb{Z}$)
    とかける．\cref{1990-1:eq:1}に代入して$t$の条件式を求めると，
    
$$
\begin{align}
        t + \frac{1}{2} & \le \left(\frac{t}{5}+1\right)\left(\frac{t}{5}-2\right) < t+\frac{3}{2} \nonumber \\
        t + \frac{1}{2} & \le \frac{1}{25}t^2  - \frac{1}{5}t - 2 < t+\frac{3}{2} \nonumber                  \\
        \therefore 125  & \le 2t^2 - 60t < 175 \label{1990-1:eq:2}
    \end{align}
$$

    を得る．

    ここで，二次関数$y = p(t) = 2t^2 - 60t$ のグラフの概形は\cref{1990-1:fig:1}のようになっており，
    
$$
\begin{align*}
         & p(-3) = 198 & p(-1) = 62  \\
         & p(31) = 62  & p(33) = 198
    \end{align*}
$$

    だから，\cref{1990-1:eq:2}を満たすような$t \in \mathbb{Z}$は $t=-2, 32$ である．したがって求めるべき$x=t/5$は$x = \frac{32}{5}, -\frac{2}{5}$ である． $\cdots$(答)

    \begin{figure}[H]
        \centering
        \def\yBoundaryLower{125}
        \def\yBoundaryUpper{175}
        \def\yAtIntPoints{128} 

        \pgfmathsetmacro{\tLowerSmallMinus}{15 - 0.5 * sqrt(1150)} 
        \pgfmathsetmacro{\tUpperSmallPlus}{15 + 0.5 * sqrt(1150)} 

        \pgfmathsetmacro{\tLowerLargeMinus}{15 - 0.5 * sqrt(1250)} 
        \pgfmathsetmacro{\tUpperLargePlus}{15 + 0.5 * sqrt(1250)} 

        \begin{tikzpicture}[
                xscale=0.1, 
                yscale=0.01,
            ]
            \def\tmin{-3}
            \def\tmax{33}
            \def\ymin{-10}
            \def\ymax{250}

            \draw[->] (\tmin, 0) -- (\tmax, 0) node[right] {$t$};
            \draw[->] (0, \ymin) -- (0, \ymax) node[above] {$y$};

            \node at (0,0) [below right] {$0$};

            \draw[blue, thick, domain=\tmin:\tmax, samples=100] plot (\x, {2*\x*\x - 60*\x});

            \fill[red] (-2, 128) circle (5pt);
            \fill[red] (32, 128) circle (5pt);

            \draw[dashed, gray] (-2, 0) -- (-2, \yAtIntPoints);
            \node at (-2, 0) [below] {$-2$};
            \draw[dashed, gray] (32, 0) -- (32, \yAtIntPoints);
            \node at (32, 0) [below] {$32$};
            \draw[dashed, gray] (0, \yAtIntPoints) -- (32, \yAtIntPoints);
            \node at (0, \yAtIntPoints) [right] {$128$};

            \draw[dashed, gray] (\tmin, \yBoundaryLower) -- (\tmax, \yBoundaryLower);
            \draw[dashed, gray] (\tmin, \yBoundaryUpper) -- (\tmax, \yBoundaryUpper);

            \draw[red, ultra thick, domain=\tLowerLargeMinus:\tLowerSmallMinus, samples=50] plot (\x, {2*\x*\x - 60*\x});
            \draw[red, ultra thick, domain=\tUpperSmallPlus:\tUpperLargePlus, samples=50] plot (\x, {2*\x*\x - 60*\x});
        \end{tikzpicture}
        \caption{二次関数 $y = 2t^2 - 60t$ のグラフ}
        \label{1990-1:fig:1}
    \end{figure}

    **【解説】**
    二次関数の問題．条件を素直に式に落としていけば解ける比較的容易な問題である．
    二次関数 $(x+1)(x-2)$ と一次関数 $1+5x$ がほぼ等しくなるような条件なので，解はこれらの交点に近くなるだろうというのが予想できる．
    実際にこれを解いてみると
    
$$
\begin{align*}
        (x+1)(x-2)   & = 1 + 5x \\
        x^2 - 6x - 3 & = 0      \\
        x = 3 \pm 2\sqrt{3}
    \end{align*}
$$

    であり，$x \approx 6.46$ と $x \approx -0.46$ が得られる．
    本問題の解答である$x = \frac{32}{5}, -\frac{2}{5}$ はこれらの値にほぼ等しく，検算として利用できるだろう．