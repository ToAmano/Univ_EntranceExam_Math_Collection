---
university: "ukyoto"
category: "zenki"
year: "1963"
question: "5"
type: "solution"
title: "UKYOTO 1963 zenki Q5 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[**解**] $\triangle O P_n P_{n+1}$ と $\triangle O P_{n+1} P_{n+2}$ の相似比は、

$$
\begin{align*}
\frac{|O P_{n+1}|}{|O P_n|} \text{ である。} \quad \dots \text{①}
\end{align*}
$$

ここで $\triangle O P_0 P_1$ に正弦定理を用いて、

$$
\begin{align*}
\frac{|O P_1|}{\sin \theta} = \frac{\alpha}{\sin(\alpha+\theta)} \implies |O P_1| = \frac{\sin \theta}{\sin(\alpha+\theta)} \cdot \alpha \quad \dots \text{②}
\end{align*}
$$

だから、$\alpha \neq 0$ より、①から

$$
\begin{align*}
\frac{|O P_1|}{|O P_0|} = 1 \cdot \frac{\sin \theta}{\sin(\alpha+\theta)}
\end{align*}
$$

したがって、$0 < \frac{\sin \theta}{\sin(\alpha+\theta)} < 1$ ならば $P_n$ は $O$ に収束する。 （以上 (イ)）

\begin{tikzpicture}[scale=1.2, >=stealth]
  \coordinate (O) at (0,0);
  \coordinate (P0) at (2.5,0);
  \coordinate (P1) at (1.5, 1.8);
  \draw (O) -- (P0) -- (P1) -- cycle;
  \node[below left] at (O) {$O$};
  \node[below right] at (P0) {$P_0$};
  \node[above] at (P1) {$P_1$};
  \node at (0.5, 0.2) {$\alpha$};
  \node at (2.0, 0.2) {$\theta$};
  \node at (1.4, 1.4) {$\theta$};
\end{tikzpicture}

さて、$\triangle O P_n P_{n+1}$ の面積 $S_n$ とする。まず、

$$
\begin{align*}
S_0 = \frac{1}{2} |O P_0| |O P_1| = \frac{1}{2} \cdot \frac{\sin \theta}{\sin(\alpha+\theta)} \alpha^2 \quad \dots \text{③}
\end{align*}
$$

であり、①から、$p = \frac{\sin \theta}{\sin(\alpha+\theta)}$ として

$$
\begin{align*}
S_{n+1} = p^2 S_n
\end{align*}
$$

くり返し用いて、③から

$$
\begin{align*}
S_n = (p^2)^{n-1} \cdot \frac{1}{2} p \alpha^2 = \frac{1}{2} p^{2n-1} \alpha^2
\end{align*}
$$

したがって、$0 < p < 1$ とあわせて、

$$
\begin{align*}
S = \lim_{n \to \infty} \sum_{k=0}^n S_k = \frac{1}{2} p \alpha^2 \frac{1}{1-p^2}
\end{align*}
$$

だから、$S$ は $\triangle O P_0 P_1$ の

$$
\begin{align*}
\frac{1}{1-p^2} = \frac{1}{1 - \left( \frac{\sin \theta}{\sin(\alpha+\theta)} \right)^2} \text{ (倍)}
\end{align*}
$$

である。(以上 (ロ))

ここで、$a_n = |P_n P_{n+1}|$ とおく。①から

$$
\begin{align*}
a_{n+1} = p a_n \quad \dots \text{④}
\end{align*}
$$

であり、$\triangle O P_0 P_1$ に正弦定理を用いて、

$$
\begin{align*}
\frac{|P_0 P_1|}{\sin \theta} = \frac{\alpha}{\sin(\alpha+\theta)} \implies a_0 = \frac{\sin \theta}{\sin(\alpha+\theta)} \alpha
\end{align*}
$$

だから、④をくり返し用いて、

$$
\begin{align*}
a_n = \frac{\sin \theta}{\sin(\alpha+\theta)} \alpha \cdot p^{n-1}
\end{align*}
$$

となるので、

$$
\begin{align*}
L &= \lim_{n \to \infty}\sum_{k=0}^n a_k = \frac{\sin \theta \cdot \alpha}{\sin(\alpha+\theta)}\cdot\frac{1}{1-p}\quad(\because |p| < 1) \\&= \frac{\sin \theta \cdot \alpha}{\sin(\alpha+\theta)}\cdot\frac{\sin(\alpha+\theta)}{\sin(\alpha+\theta) - \sin \theta} = \frac{\sin \theta}{\sin(\alpha+\theta) - \sin \theta}\cdot\alpha
\end{align*}
$$

である。$\theta \to +0$ として、

$$
\begin{align*}
L = \frac{\theta}{\sin(\alpha+\theta) - \sin \theta} \cdot \frac{\sin \theta}{\theta} \cdot \alpha \longrightarrow \frac{\alpha}{\cos \alpha}
\end{align*}
$$