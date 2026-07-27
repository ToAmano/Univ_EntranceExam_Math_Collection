---
university: "ukyoto"
category: "zenki"
year: "1996"
question: "5"
type: "solution"
title: "UKYOTO 1996 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] (1) 選んだ頂点 $X_1$ とする。

\begin{tikzpicture}
\draw (0,0) -- (2,0) -- (1,1.732) -- cycle;
\node[below left] at (0,0) {$B$};
\node[below right] at (2,0) {$C$};
\node[above] at (1,1.732) {$A$};
\fill (1,0.577) circle (1.5pt) node[right] {$P_n$};
\end{tikzpicture}

$\overrightarrow{OP_1} = \frac{1}{2}(\overrightarrow{OP_0} + \overrightarrow{OX_1})$ \\
$|\overrightarrow{OP_1}|^2 = \frac{1}{4}\{|\overrightarrow{OP_0}|^2 + |\overrightarrow{OX_1}|^2 + 2\overrightarrow{OP_0} \cdot \overrightarrow{OX_1}\}$ \\
$= \frac{1}{4}|\overrightarrow{OP_0}|^2 + 1 + 2\overrightarrow{OP_0} \cdot \overrightarrow{OX_1} \quad (\because |\overrightarrow{OX_1}| = 1)$ \\
より、

$$
\begin{align*}
E_1 = \sum_{X_1=A,B,C} |\overrightarrow{OP_1}|^2 \cdot \frac{1}{3}
\end{align*}
$$

$$
\begin{align*}
= \frac{1+|\overrightarrow{OP_0}|^2}{4} + \frac{2}{3} \cdot \frac{1}{4} \overrightarrow{OP_0} \cdot (\overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC}) = \frac{1+|\overrightarrow{OP_0}|^2}{4} \quad (\because \overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC} = \vec{0})
\end{align*}
$$

 \hfill(終)

(2) 点$X$に対し、$\overrightarrow{OX} = \vec{x}$ とする。題意から、

$$
\begin{align*}
\overrightarrow{P_{n+1}} = \frac{1}{2}(\overrightarrow{P_n} + \overrightarrow{x_{n+1}})
\end{align*}
$$

だから、くり返し用いて、

$$
\begin{align*}
\overrightarrow{P_n} = \frac{1}{2}\overrightarrow{x_n} + \frac{1}{4}\overrightarrow{x_{n-1}} + \cdots + \frac{1}{2^n}\overrightarrow{x_1} + \frac{1}{2^n}\overrightarrow{OP_0}
\end{align*}
$$

$$
\begin{align*}
= \frac{1}{2^n}\overrightarrow{OP_0} + \sum_{i=1}^n \frac{1}{2^{n+1-i}}\overrightarrow{OX_i}
\end{align*}
$$

 \hfill(終)

[解2] \\
(3) $E_1 = \frac{1}{4} \ (\because (1)) \cdots \text{③}$ である。ここで、$n \ge 2$ の時、

$$
\begin{align*}
\overrightarrow{P_n} = \frac{1}{2} \{ \overrightarrow{P_{n-1}} + \overrightarrow{x_n} \}
\end{align*}
$$

$$
\begin{align*}
|\overrightarrow{P_n}|^2 = \frac{1}{4}\{ |\overrightarrow{P_{n-1}}|^2 + |\overrightarrow{x_n}|^2 \} + \frac{1}{2}\overrightarrow{P_{n-1}} \cdot \overrightarrow{x_n} \cdots \text{④}
\end{align*}
$$

であり、

$$
\begin{align*}
E(|\overrightarrow{P_{n-1}}|) = E_{n-1}
\end{align*}
$$

$$
\begin{align*}
E(|\overrightarrow{x_n}|^2) = 1
\end{align*}
$$

$$
\begin{align*}
E(\overrightarrow{P_{n-1}} \cdot \overrightarrow{x_n}) = \frac{1}{3}\overrightarrow{P_{n-1}} \cdot (\vec{a} + \vec{b} + \vec{c}) = 0
\end{align*}
$$

を④に代入して

$$
\begin{align*}
E_n = \frac{1}{4} (E_{n-1} + 1)
\end{align*}
$$

③とあわせて

$$
\begin{align*}
E_n = \frac{1}{3}\{1 - \left(\frac{1}{4}\right)^n\}
\end{align*}
$$

 \hfill(終)

(3) $P_0 = O$ の時、

$$
\begin{align*}
\overrightarrow{OP_n} = \sum_{i=1}^n \frac{1}{2^{n+1-i}} \overrightarrow{OX_i}
\end{align*}
$$

だから、$Y_i$ を、$\overrightarrow{y_i} = \frac{1}{2^{n+1-i}} \overrightarrow{x_i}$ となるよう定めると、

$$
\begin{align*}
|\overrightarrow{P_n}|^2 = |\overrightarrow{y_1} + \overrightarrow{y_2} + \cdots + \overrightarrow{y_n}|^2
\end{align*}
$$

$$
\begin{align*}
= \sum_{i=1}^n |\overrightarrow{y_i}|^2 + 2 \sum_{i < j} \overrightarrow{y_i} \cdot \overrightarrow{y_j}
\end{align*}
$$

$$
\begin{align*}
= \sum_{i=1}^n \frac{1}{4^{n+1-i}} + 2 \sum_{i < j} \overrightarrow{y_i} \cdot \overrightarrow{y_j} \quad (\because |\overrightarrow{x_i}| = 1)
\end{align*}
$$

$$
\begin{align*}
= \frac{1}{3}\{1 - (1/4)^n\} + 2 \sum_{i < j} \overrightarrow{y_i} \cdot \overrightarrow{y_j} \cdots \text{①}
\end{align*}
$$

である。ここで、$i \ne j$ に対して、

$$
\begin{align*}
\overrightarrow{x_i} \cdot \overrightarrow{x_j} = \begin{cases} 1 & (X_i = X_j) \\ -1/2 & (X_i \ne X_j) \end{cases} \cdots \text{②}
\end{align*}
$$

だから $\overrightarrow{x_i} \cdot \overrightarrow{x_j}$ の期待値 $P_{i,j}$ は

$$
\begin{align*}
P = \frac{1}{3} \cdot 1 + \frac{2}{3} \left(-\frac{1}{2}\right) = 0
\end{align*}
$$

なので、$\sum_{i < j} \overrightarrow{y_i} \cdot \overrightarrow{y_j}$ の期待値 $Q$ は、

$$
\begin{align*}
Q = \sum_{i < j} \frac{1}{2^{n+1-i} \cdot 2^{n+1-j}} \cdot P_{i,j} = 0
\end{align*}
$$

だから ①より

$$
\begin{align*}
E_n = \frac{1}{3}(1 - (1/4)^n) + Q = \frac{1}{3} \{ 1 - \left(\frac{1}{4}\right)^n \}
\end{align*}
$$

 \hfill(終)