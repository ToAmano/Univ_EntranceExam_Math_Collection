---
university: "titech"
category: "zenki"
year: "1970"
question: "2"
type: "solution"
title: "TITECH 1970 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

1.  準線のうち $x > 0$ のものを $l$ とする. $F(ae, 0)$ とおく時, この楕円の離心率は $e$ であり, 右図のように $P, H$ を定めると,
    

$$
\begin{align*}
\overline{PF} = e \overline{PH}
\end{align*}
$$

    だから, $\overline{PF} = r$ として,
    

$$
\begin{align*}
\frac{a}{e} - ae = r \cos\theta + \frac{r}{e}
\end{align*}
$$

    

$$
\begin{align*}
r = \frac{a(1-e^2)}{1+e\cos\theta}
\end{align*}
$$

    

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1970/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 楕円と焦点$F$，準線$l$の関係</figcaption>
</figure>

2.  $P, Q$ に対応する $\theta$ を $\alpha, \alpha+\pi \, (0 \leqq \alpha \leqq \pi)$, $R, S$ に対応する $\theta$ を $\alpha-\frac{\pi}{2}, \alpha+\frac{\pi}{2}$ とする. $A = a(1-e^2)$ とすると,
    

$$
\begin{align*}
\overline{PF}\cdot\overline{QF}&= r(\alpha) \cdot r(\alpha+\pi) \\&= \frac{A}{1+e\cos\alpha}\cdot\frac{A}{1-e\cos\alpha} = \frac{A^2}{1-e^2\cos^2\alpha}
\end{align*}
$$

    

$$
\begin{align*}
\overline{FR}\cdot\overline{FS} = r\left(\alpha+\frac{\pi}{2}\right) r\left(\alpha-\frac{\pi}{2}\right) = \frac{A^2}{1-e^2\sin^2\alpha}
\end{align*}
$$

    だから
    

$$
\begin{align*}
\frac{1}{\overline{PF}\cdot\overline{QF}} + \frac{1}{\overline{FR}\cdot\overline{FS}} = \frac{2-e^2}{A^2} = \frac{2-e^2}{a^2(1-e^2)^2}.
\end{align*}
$$