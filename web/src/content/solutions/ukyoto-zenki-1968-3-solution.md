---
university: "ukyoto"
category: "zenki"
year: "1968"
question: "3"
type: "solution"
title: "UKYOTO 1968 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

1.  右のグラフから
    \begin{itemize}

2.  $l < 0$ の時, $x \leqq l$ をみたす $x$ に対して $x^2 > 0 > l$ となり, $S$ には属さない.

3.  $l > 1$ の時, $x = l$ での題意の成立が必要だが,
        

$$
\begin{align*}
l^2 - l = l(l-1) > 0
\end{align*}
$$

        となって $l^2 < l$ に矛盾.
    \end{itemize}
    よって, $0 \leqq l \leqq 1$ である.

    
    \begin{tikzpicture}[scale=1.5]
        \draw[->] (-0.5,0) -- (2.5,0) node[right]{$x$};
        \draw[->] (0,-0.5) -- (0,2.5) node[above]{$y$};
        \node[below left] at (0,0) {$O$};
        \draw[thick, domain=-0.2:1.5, smooth] plot (\x, {\x*\x}) node[right]{$y=x^2$};
        \draw[thick, domain=-0.2:1.8, smooth] plot (\x, {\x}) node[right]{$y=x$};
        \draw[dashed] (1,0) node[below]{$1$} -- (1,1) -- (0,1) node[left]{$1$};
        \draw[dashed] (1.3,0) node[below]{$l$} -- (1.3,1.69);
    \end{tikzpicture}

4.  \begin{itemize}

5.  $0 < m < 1$ とすると, $x = m$ での題意の成立が必要だが ($m \leqq l \leqq 1$ だから)
        

$$
\begin{align*}
m^2 - m = m(m-1) < 0 \implies m^2 < m
\end{align*}
$$

        となり矛盾.

6.  $1 < m$ とすると, $1 < m \leqq l$ となり, (1) から $0 \leqq l \leqq 1$ であることに反する.
    \end{itemize}
    以上から $m \leqq 0$ または $m = 1$ である.

7.  $m = 1$ の時, $0 \leqq l \leqq 1$ と $1 \leqq l$ から $l = 1$ であり,
    

$$
\begin{align*}
S = \{1\}
\end{align*}
$$

8.  $m < 0$ の時, $m \leqq x \leqq l$ の全ての $x$ で $m \leqq x^2 \leqq l$ となるような $m$ を求める.
    $x^2 = l \iff x = \pm \sqrt{l}$ から, グラフは右のようになり, 条件は
    

$$
\begin{align*}
-\sqrt{l} \leqq m \leqq 0
\end{align*}
$$

    である.

    
    \begin{tikzpicture}[scale=1.5]
        \draw[->] (-2.0,0) -- (2.0,0) node[right]{$x$};
        \draw[->] (0,-0.5) -- (0,2.5) node[above]{$y$};
        \node[below left] at (0,0) {$O$};
        \draw[thick, domain=-1.5:1.5, smooth] plot (\x, {\x*\x}) node[right]{$y=x^2$};
        \draw[thick, domain=-0.5:1.8, smooth] plot (\x, {\x}) node[right]{$y=x$};
        \draw[dashed] (-1.2,0) node[below]{$-\sqrt{l}$} -- (-1.2,1.44);
        \draw[dashed] (1.2,0) node[below]{$l$} -- (1.2,1.44);
        \draw[dashed] (-1.2,1.44) -- (1.2,1.44);
    \end{tikzpicture}