---
university: "titech"
category: "zenki"
year: "1968"
question: "3"
type: "solution"
title: "TITECH 1968 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$e(\theta) = \cos\theta + i\sin\theta$ とする．$z = e(\alpha)$, $w = e(\beta)$ であり，

$$
\begin{align*}
e(\alpha) + e(\beta) &= (\cos\alpha + \cos\beta) + i(\sin\alpha + \sin\beta) \\&= 2 \cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2} + 2 i \sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}\\&= 2 \cos\frac{\alpha-\beta}{2} e\left(\frac{\alpha+\beta}{2}\right)
\end{align*}
$$

だから，$t = z+w$ として，

$$
\begin{align*}
|1 + z + w| \le 1 \iff |1 + t|^2 \le 1 \iff |t|^2 + t + \bar{t}\le 0 \quad\cdots\text{①}
\end{align*}
$$

に代入して，$|e(\theta)| = 1$ より，

$$
\begin{align*}
4 \cos^2\frac{\alpha-\beta}{2} + 2 \cos\frac{\alpha-\beta}{2}\cdot 2 \cos\frac{\alpha+\beta}{2}\le 0
\end{align*}
$$

$$
\begin{align*}
\iff\cos\frac{\alpha-\beta}{2}\left(\cos\frac{\alpha-\beta}{2} + \cos\frac{\alpha+\beta}{2}\right)\le 0
\end{align*}
$$

$$
\begin{align*}
\iff\cos\frac{\alpha-\beta}{2}\cos\frac{\alpha}{2}\cos\frac{\beta}{2}\le 0 \quad\cdots\text{②}
\end{align*}
$$

以上から，求める $(\alpha, \beta)$ は ②を満たし，かつ $0 \le \alpha, \beta \le 2\pi$ なる $(\alpha, \beta)$ であり，図示して下図斜線部（境界含む）．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1968/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: ②を満たす$(\alpha,\beta)$の範囲（斜線部）</figcaption>
</figure>

$$
\begin{align*}
\begin{cases}
0 \le \alpha \le \pi \land 0 \le \beta \le \pi \text{ の時} & ② \iff \cos\frac{\alpha-\beta}{2} \le 0 \\
0 \le \alpha \le \pi \land \pi \le \beta \le 2\pi \text{ 〃} & ② \iff \cos\frac{\alpha-\beta}{2} \ge 0 \\
\pi \le \alpha \le 2\pi \land 0 \le \beta \le \pi \text{ 〃} & ② \iff \cos\frac{\alpha-\beta}{2} \ge 0 \\
\pi \le \alpha \le 2\pi \land \pi \le \beta \le 2\pi \text{ 〃} & ② \iff \cos\frac{\alpha-\beta}{2} \le 0
\end{cases}
\end{align*}
$$