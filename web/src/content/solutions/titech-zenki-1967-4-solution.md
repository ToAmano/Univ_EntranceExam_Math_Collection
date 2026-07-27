---
university: "titech"
category: "zenki"
year: "1967"
question: "4"
type: "solution"
title: "TITECH 1967 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $C = \cos x, S = \sin x$ とおく. 又, $p = S+C$ とすると $SC = \frac{p^2-1}{2}, -\sqrt{2} \leqq p \leqq \sqrt{2} \dots \text{①}$ である.

$$
\begin{align*}
f(x) &= 3(S-C) - \cos 2x = (S-C)(S+C+3) \\
f'(x) &= 3(C+S) + 2\sin 2x \\&= 3(C+S) + 4SC \\&= 3p + 2p^2 - 2 = (2p-1)(p+2)
\end{align*}
$$

から, ①とあわせて下表をうる.

$$
\begin{align*}
\begin{array}{c|c|c|c|c|c|c|c}
x & 0 & \dots & \alpha & \dots & \beta & \dots & 2\pi \\ \hline
p & 1 & + & 1/2 & - & 1/2 & + & 1 \\ \hline
f' & & + & 0 & - & 0 & + & \\ \hline
f & -4 & \nearrow & & \searrow & & \nearrow & -4
\end{array}\qquad\left(\alpha, \beta\text{ は } p = \frac{1}{2}\text{ となるもの.}\right)
\end{align*}
$$

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1967/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $S-C$の符号と$\alpha$，$\beta$の関係</figcaption>
</figure>

ここで,

$$
\begin{align*}
S-C &= \pm\sqrt{(S-C)^2} = \pm\sqrt{(S+C)^2 - 4SC}\\&= \pm\sqrt{2-p^2}
\end{align*}
$$

及び右図から $x=\alpha$ の時 $S-C > 0$, $x=\beta$ の時 $S-C < 0$ だから

$$
\begin{align*}
\begin{cases}
f(\alpha) = \sqrt{2-\frac{1}{4}} \left( \frac{1}{2} + 3 \right) = \sqrt{2-\frac{1}{4}} \cdot \frac{7}{2} = \frac{7}{4}\sqrt{7} \\
f(\beta) = -\sqrt{2-\frac{1}{4}} \left( \frac{1}{2} + 3 \right) = -\sqrt{2-\frac{1}{4}} \cdot \frac{7}{2} = -\frac{7}{4}\sqrt{7}
\end{cases}
\end{align*}
$$

となり, $-4 > -\frac{7}{4}\sqrt{7}$ とあわせて

$$
\begin{align*}
\text{max}\;\;\frac{7}{4}\sqrt{7}, \quad\text{min}\;\; -\frac{7}{4}\sqrt{7}
\end{align*}
$$