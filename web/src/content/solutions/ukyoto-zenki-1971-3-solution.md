---
university: "ukyoto"
category: "zenki"
year: "1971"
question: "3"
type: "solution"
title: "UKYOTO 1971 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**]

$m$ は $a, b$ によって以下のようになる. (軸の位置で場合分け)

1.  $-\frac{a}{2} \le 0 \iff a \ge 0$ の時, $m = f(0) = b$

2.  $0 \le -\frac{a}{2} \le 1 \iff -2 \le a \le 0$ の時, $m = f\left(-\frac{a}{2}\right) = -\frac{1}{4}a^2 + b$

3.  $1 \le -\frac{a}{2} \iff a \le -2$ の時, $m = f(1) = a + b + 1$

又, $(a, b)$ の存在領域は下図斜線部 (境界含む) である.

\begin{tikzpicture}[scale=1.2]
    \draw[->] (-3,0) -- (3,0) node[right]{$a$};
    \draw[->] (0,-1.5) -- (0,2) node[above]{$b$};
    \draw[thick,domain=-3:3] plot (\x, {-0.5*\x + 1}) node[right]{\small $b = -\frac{1}{2}a + 1$};
    
    \begin{scope}
        \clip (-3,-1.5) rectangle (3,2);
        \fill[gray!20] (-3, 2.5) -- (3, -0.5) -- (3,-1.5) -- (-3,-1.5) -- cycle;
        \draw[thick] (-3, 2.5) -- (3, -0.5);
    \end{scope}
    
    \node[below left] at (0,0) {$0$};
    \fill (0,1) circle (1.5pt) node[left]{\small $1$};
    \fill (2,0) circle (1.5pt) node[below]{\small $2$};
\end{tikzpicture}

1.  $\max f(0) = 1 \quad ((a, b) = (0, 1))$

2.  $m \le -\frac{1}{4}a^2 - \frac{1}{2}a + 1 = -\frac{1}{4}(a+1)^2 + \frac{5}{4} \le \frac{5}{4}$\\
    等号成立 $(a, b) = \left(-1, \frac{3}{2}\right)$

3.  $m \le a + 1 - \frac{1}{2}a + 1 = \frac{1}{2}a + 2 \le 1$\\
    等号成立 $(a, b) = (-2, 2)$

以上から $(a, b) = \left(-1, \frac{3}{2}\right)$ が $m$ を最大にする.