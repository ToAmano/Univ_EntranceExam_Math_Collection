---
university: "ukyoto"
category: "zenki"
year: "1989"
question: "1"
type: "solution"
title: "UKYOTO 1989 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $\angle A_n O B_n = \theta_n$ とおくと、題意から
帰納的に

$$
\begin{align*}
\theta_n = \left(\frac{1}{2}\right)^{n-1} \theta \cdots \text{①}
\end{align*}
$$

右下図で、

$$
\begin{align*}
OA_n = a_n
\end{align*}
$$

$$
\begin{align*}
OB_{n+1} = a_{n+1}
\end{align*}
$$

だから

$$
\begin{align*}
\begin{cases} a_n \cos\left(\left(\frac{1}{2}\right)^n \theta\right) = a_{n+1} \\ a_1 = 1 \end{cases}
\end{align*}
$$

となり、

$$
\begin{align*}
a_n = \cos\left\{ \left(\frac{1}{2}\right)^{n-1} \theta \right\} \cdots \cos\frac{\theta}{8} \cos\frac{\theta}{4} \cos\frac{\theta}{2}
\end{align*}
$$

である

(1)

$$
\begin{align*}
a_3 \cdot \sin\frac{\theta}{4} = \sin\frac{\theta}{4} \cdot \cos\frac{\theta}{4} \cdot \cos\frac{\theta}{2} = \frac{1}{2} \sin\frac{\theta}{2} \cdot \cos\frac{\theta}{2} = \frac{1}{4} \sin\theta \quad \text{//}
\end{align*}
$$

(2) $a_n \sin\frac{\theta}{2^{n-1}} = A_n$ も、(1)と同じように計算して

$$
\begin{align*}
A_n = \left(\frac{1}{2}\right)^{n-1} \sin\theta
\end{align*}
$$

だから

$$
\begin{align*}
a_n = \frac{ \left(\frac{1}{2}\right)^{n-1} \theta }{ \sin\left\{ \left(\frac{1}{2}\right)^{n-1} \theta \right\} } \cdot \frac{\sin\theta}{\theta} \to \frac{\sin\theta}{\theta} \quad (n \to \infty) \quad \text{//}
\end{align*}
$$

\begin{tikzpicture}
\draw (0,4) node[above]{O} -- (-2,0) node[below]{$A_1$} -- (2,0) node[below]{$B_1$} -- cycle;
\draw (-1.5, 1) node[left]{$A_2$} -- (1.5, 1) node[right]{$B_2$};
\draw (-1, 2) node[left]{$A_3$} -- (1, 2) node[right]{$B_3$};
\draw (0,4) -- (0,0);
\end{tikzpicture}