---
university: "ukyoto"
category: "zenki"
year: "1964"
question: "4"
type: "solution"
title: "UKYOTO 1964 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $P(a, b)$ とし、2接点 $Q(\alpha, \alpha^2), R(\beta, \beta^2)$ とおく。ただし $\alpha < \beta \cdots$ ①とする。

$Q, R$ における接線は、各々

$$
\begin{align*}
\begin{cases}
y = 2\alpha x - \alpha^2 \\
y = 2\beta x - \beta^2
\end{cases}
\end{align*}
$$

だから、これらの交点が $P$ であり、

$$
\begin{align*}
a = \frac{\alpha+\beta}{2}, \quad b = \alpha\beta \quad \cdots \text{②}
\end{align*}
$$

となる。したがって、

$$
\begin{align*}
\begin{aligned}
\vec{PQ} &= \begin{pmatrix} \alpha-a \\ \alpha^2-b \end{pmatrix} = \begin{pmatrix} \frac{\alpha-\beta}{2} \\ \alpha(\alpha-\beta) \end{pmatrix} = (\beta-\alpha) \begin{pmatrix} -\frac{1}{2} \\ -\alpha \end{pmatrix} \quad \cdots (*) \\
\vec{PR} &= \begin{pmatrix} \beta-a \\ \beta^2-b \end{pmatrix} = \begin{pmatrix} \frac{-\alpha+\beta}{2} \\ \beta(\beta-\alpha) \end{pmatrix} = (\beta-\alpha) \begin{pmatrix} \frac{1}{2} \\ \beta \end{pmatrix}
\end{aligned}
\end{align*}
$$

である。2接線のなす角 $\theta$ として、$\theta = \pi/3$ or $2\pi/3$ だから、

$$
\begin{align*}
\tan\theta = \pm \tan\pi/3 = \pm \sqrt{3} \quad \cdots \text{③}
\end{align*}
$$

となる。一方、

$$
\begin{align*}
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{|\vec{PQ}||\vec{PR}|\sin\theta}{|\vec{PQ}||\vec{PR}|\cos\theta} = \frac{2 \Delta PQR}{\vec{PQ}\cdot\vec{PR}} \quad (\because |\vec{PQ}||\vec{PR}| \neq 0)
\end{align*}
$$

だから、(*)から

$$
\begin{align*}
\tan\theta = \frac{|\frac{1}{2}\alpha - \frac{1}{2}\beta|}{-\frac{1}{4} - \alpha\beta} = \frac{-\frac{1}{2}(\beta-\alpha)}{\frac{1}{4} + \alpha\beta} \quad (\because \text{①}) \quad \cdots \text{④}
\end{align*}
$$

となる。②から $\alpha, \beta$ が $x$ の2次方程式 $x^2 - 2ax + b = 0$ の2実解であることから、

$$
\begin{align*}
\beta-\alpha = 2\sqrt{a^2-b} \quad (a^2-b \geqq 0)
\end{align*}
$$

に注意して、②, ④から、

$$
\begin{align*}
\pm \sqrt{3} = \frac{-\sqrt{a^2-b}}{\frac{1}{4}+b}
\end{align*}
$$

2乗して良く、

$$
\begin{align*}
3\left(b + \frac{1}{4}\right)^2 = a^2 - b \iff a^2 - 3\left(b + \frac{5}{12}\right)^2 = \frac{1}{9} \quad \cdots \text{⑥}
\end{align*}
$$

以上から求める軌跡は $a^2 - b \geqq 0 \land \text{⑥}$ だが、①の時 $a^2 - b \geqq 0$ は満たされるので、求めるものは

$$
\begin{align*}
x^2 - 3\left(y + \frac{5}{12}\right)^2 = \frac{1}{9}
\end{align*}
$$

\medskip[解2] 2接線の傾き $\theta_\alpha, \theta_\beta$ とする。これら正負で以下のようになる。
([解1]を流用、$ -\frac{\pi}{2} < \theta_\alpha, \theta_\beta < \frac{\pi}{2} $)

いずれの場合にも、これらのなす角 $\theta$ ($0 \leqq \theta \leqq \pi$) は

$$
\begin{align*}
\theta = \pi - (\theta_\beta - \theta_\alpha), \quad \theta = \theta_\beta - \theta_\alpha
\end{align*}
$$

で与えられ、いずれの場合も

$$
\begin{align*}
\tan\theta = \pm \tan(\theta_\beta - \theta_\alpha)
\end{align*}
$$

となる。$\theta = \frac{\pi}{3}, \frac{2\pi}{3}$ だから、

$$
\begin{align*}
\pm \sqrt{3} = \pm \tan(\theta_\beta - \theta_\alpha) \quad \cdots \text{P}
\end{align*}
$$

ここで $\tan\theta_\alpha = 2\alpha$, $\tan\theta_\beta = 2\beta$ より

$$
\begin{align*}
\tan(\theta_\beta - \theta_\alpha) = \frac{2(\beta-\alpha)}{1+4\alpha\beta}
\end{align*}
$$

だから、①より

$$
\begin{align*}
\pm \sqrt{3} = \pm \frac{2(\beta-\alpha)}{1+4\alpha\beta} \iff 3 = \frac{4(\beta-\alpha)^2}{(1+4\alpha\beta)^2} \quad (\text{Pに合流})
\end{align*}
$$

(以下略)