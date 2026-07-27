---
university: "ukyoto"
category: "zenki"
year: "1977"
question: "3"
type: "solution"
title: "UKYOTO 1977 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $S = \sin x, C = \cos x$ と略記する。漸化式から $k \in \mathbb{Z}_{\ge 0}$ として

$$
\begin{align*}
f^{4k}(x) = -S, \quad f^{4k+1}(x) = C, \quad f^{4k+2}(x) = -S, \quad f^{4k+3}(x) = -C
\end{align*}
$$

である。以下 $P$ の $x$ 座標を $P$ とする。

1.  $C_1 : y = xS, C_2 : y = C$ の時\\
    $P \sin P = \cos P$ であり、$t_1, t_2$ の接線ベクトルは $\begin{pmatrix} 1 \\ P \cos P + \sin P \end{pmatrix}$, $\begin{pmatrix} 1 \\ -\sin P \end{pmatrix}$ だから
    

$$
\begin{align*}
\begin{pmatrix} 1 \\ P \cos P + \sin P \end{pmatrix} \cdot \begin{pmatrix} 1 \\ -\sin P \end{pmatrix} = \cos P (\cos P - P \sin P) = 0
\end{align*}
$$

    となり、$t_1$ と $t_2$ は直交する。

2.  $C_1 : y = xC, C_2 : y = -S$ の時\\
    $P \cos P = -\sin P$ であり、接線ベクトルは $\begin{pmatrix} 1 \\ \cos P - P \sin P \end{pmatrix}$, $\begin{pmatrix} 1 \\ -\cos P \end{pmatrix}$ となり、$1^\circ$ と同じく $t_1, t_2$ は直交する。

3.  $C_1 : y = -xS, C_2 : y = -C$ の時\\
    $-P \sin P = -\cos P$ であり、接線ベクトルは $\begin{pmatrix} 1 \\ -P \cos P - \sin P \end{pmatrix}$, $\begin{pmatrix} 1 \\ \sin P \end{pmatrix}$ だから、$1^\circ$ と同じく $t_1, t_2$ は直交する。

4.  $C_1 : y = -xC, C_2 : y = S$ の時\\
    $-P \cos P = \sin P$ であり、接線ベクトルは $\begin{pmatrix} 1 \\ -\cos P + P \sin P \end{pmatrix}$, $\begin{pmatrix} 1 \\ \cos P \end{pmatrix}$ だから、$1^\circ$ と同じく $t_1, t_2$ は直交する。

以上から示された。