---
university: "ukyoto"
category: "zenki"
year: "2001"
question: "4"
type: "solution"
title: "UKYOTO 2001 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 題意の正八面体の一辺を $2$ とし、$P_1$ を始点とするベクトル $\overrightarrow{P_1 P_m}$ の終点を $\nabla$ とする。
任意の $m \ (m=2,\cdots,6)$ に対し

$$
\begin{align*}
\overrightarrow{P_1 P_m} \cdot \vec{v} \le 0
\end{align*}
$$

を満たす $\nabla$ の存在範囲は、右図で $\overrightarrow{P_1 P_m}$ を法線ベクトルとする $(m=2,3,4,5)$ 4平面で囲まれた部分（$\alpha$ とおく）である。ところでこの4平面は、右下図のように空間を対称に $4$ 等分割するので、
（立方体の各面を底面、$P_1$ を頂点とする $6$ つの四角錐は合同）
対称性から $\nabla$ が $\alpha$ にある場合のみを考えれば良い。
又、題意から

$$
\begin{align*}
\overrightarrow{P_1 P_m} \cdot \vec{v} \neq 0
\end{align*}
$$

である。以上から

$$
\begin{align*}
\overrightarrow{P_1 P_m} \cdot \vec{v} < 0
\end{align*}
$$

となり、題意は示された。

\begin{tikzpicture}[scale=1.5]
\coordinate (A) at (1,0,0);
\coordinate (B) at (0,1,0);
\coordinate (C) at (-1,0,0);
\coordinate (D) at (0,-1,0);
\coordinate (E) at (0,0,1);
\coordinate (F) at (0,0,-1);
\draw (A) -- (B) -- (C) -- (D) -- cycle;
\draw (E) -- (A) (E) -- (B) (E) -- (C) (E) -- (D);
\draw[dashed] (F) -- (A) (F) -- (B) (F) -- (C) (F) -- (D);
\node[above] at (B) {$P_1$};
\node[below] at (D) {$P_6$};
\end{tikzpicture}

[解2] 正八面体の中心を $O$ とし、$\overrightarrow{OX} = \vec{v}$ となる点 $X$ をとる。$P_1, \cdots, P_6$ の中で点 $X$ から最も近い点を $P_k$ とする。$\overline{P_k X} \le \overline{P_m X}$ より

$$
\begin{align*}
|\overrightarrow{OX} - \overrightarrow{OP_k}| \le |\overrightarrow{OX} - \overrightarrow{OP_m}|
\end{align*}
$$

各辺 $0$ 以上だから $2$ 乗して

$$
\begin{eqnarray*}
2 (\overrightarrow{OP_m} - \overrightarrow{OP_k}) \cdot\overrightarrow{OX}&\le& |\overrightarrow{OP_m}|^2 - |\overrightarrow{OP_k}|^2 = 0 \\\therefore\overrightarrow{P_k P_m}\cdot\vec{v}&\le& 0
\end{eqnarray*}
$$

$\overrightarrow{P_k P_m} \cdot \vec{v} \neq 0$ から

$$
\begin{align*}
\overrightarrow{P_k P_m} \cdot \vec{v} < 0
\end{align*}
$$