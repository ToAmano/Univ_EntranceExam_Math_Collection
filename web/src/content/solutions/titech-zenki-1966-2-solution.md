---
university: "titech"
category: "zenki"
year: "1966"
question: "2"
type: "solution"
title: "TITECH 1966 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] 判別式として $D > 0 \iff p^2 - 2q > 0 \quad \dots \text{①}$ である．又, 収束する条件から

$$
\begin{align*}
-1 < \frac{\alpha}{2\beta}\le 1, \quad -1 < \frac{4\beta^2}{\alpha}\le 1 \quad\dots\text{②}
\end{align*}
$$

ここで, ①の $p > 1 \land 1-2p+2q \ge 0$ を図示すると右図斜線部 (境界は実線のみ含む) だから, $p, q > 0$ となり

$$
\begin{align*}
\alpha + \beta = p > 0, \quad\alpha\beta = \frac{q}{2} > 0 \quad\dots\text{③}
\end{align*}
$$

から $\alpha > 0, \, \beta > 0$ である．したがって, ②から

$$
\begin{align*}
-2\beta < \alpha\le 2\beta, \quad -\alpha < 4\beta^2 \le\alpha
\end{align*}
$$

$$
\begin{align*}
\therefore 0 < \alpha\le 2\beta, \quad 0 < 4\beta^2 \le\alpha
\end{align*}
$$

$$
\begin{align*}
\therefore 4\beta^2 \le\alpha\le 2\beta\quad\dots\text{④}
\end{align*}
$$

まず, $\alpha$の存在条件から $4\beta^2 \le 2\beta \quad \therefore 2\beta \le 1 \dots \text{⑤}$ が必要．
$\alpha \le \beta$ の時 ④の左側が不成立だから $\beta \le \alpha$ が必要である．③を $p > 1, \, 1-2p+2q \ge 0$ に代入して

$$
\begin{align*}
1 < \alpha + \beta, \quad 1 - 2(\alpha+\beta) + 4\alpha\beta\ge 0 \quad\dots\text{⑤}
\end{align*}
$$

④, ⑤を図示して, 右図黒丸の $(\alpha, \beta) = \left(1, \dfrac{1}{2}\right)$ を得る．
この時, ③から $(p, q) = \left(\dfrac{3}{2}, 1\right)$ である．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1966/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: ④，⑤を満たす$(p,q)$，$(\alpha,\beta)$の図示</figcaption>
</figure>