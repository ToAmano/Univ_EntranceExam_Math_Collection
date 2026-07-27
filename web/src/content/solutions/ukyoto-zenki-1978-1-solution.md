---
university: "ukyoto"
category: "zenki"
year: "1978"
question: "1"
type: "solution"
title: "UKYOTO 1978 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $\alpha = a+b, \beta = ab$ とする.

(与式) $\Leftrightarrow (\alpha+c) - 3\sqrt[3]{|\beta|} \cdot c^{\frac{1}{3}} - (\alpha - 2\sqrt{|\beta|}) \ge 0 \quad \cdots$ ①

この左辺を $f(c)$ とおくと $\therefore f'(c) = 1 - \sqrt[3]{|\beta|} \cdot c^{-\frac{2}{3}}$ より下表をえる

| $c$  | $0$ |  $\cdots$  | $\sqrt{|\beta|}$ |  $\cdots$  |
|:------:|:-----:|:------------:|:------------------:|:------------:|
| $f'$ |       |    $-$     |       $0$        |    $+$     |
| $f$  |       | $\searrow$ |                    | $\nearrow$ |

よって,

$$
\begin{align*}
f(c) \ge f(\sqrt{|\beta|}) = \alpha + \sqrt{|\beta|} - 3\sqrt{|\beta|} - \alpha + 2\sqrt{|\beta|} = 0
\end{align*}
$$

だから①は示された \qed