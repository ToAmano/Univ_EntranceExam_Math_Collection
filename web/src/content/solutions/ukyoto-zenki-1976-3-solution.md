---
university: "ukyoto"
category: "zenki"
year: "1976"
question: "3"
type: "solution"
title: "UKYOTO 1976 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{proof}[解]
$f(x)$ の最高次を $a_n x^n \ (a_n \ne 0, n \in \mathbb{Z}_{\ge 0})$ とおくと,
$f(x) \cdot f'(x)$ の最高次は $n a_n^2 x^{2n-1}$, $\int_0^x f(t) dt$ の最高次は $\frac{a_n}{n+1} x^{n+1}$ である.

\medskip
$1^\circ \ n \ge 3$ の時\\
$2n-1 > n+1$ から、与式左辺の最高次は $n a_n^2 x^{2n-1}$ だから 比較して

$$
\begin{align*}
n \cdot a_n^2 \cdot x^{2n-1} = \frac{4}{9} x
\end{align*}
$$

しかしこれをみたす $n \in \mathbb{N}_{\ge 3}$ は存在せず、不適.

\medskip
$2^\circ \ n \le 1$ の時\\
$2n-1 < n+1$ から、$1^\circ$ と同様にして

$$
\begin{align*}
\frac{a_n}{n+1} x^{n+1} = \frac{4}{9} x
\end{align*}
$$

より、$(a_n, n) = \left(\frac{4}{9}, 0\right)$, つまり $f(x) = \frac{4}{9}$ が必要. 与式に代入して

$$
\begin{align*}
(\text{左辺}) = \frac{4}{9} (x - 1)
\end{align*}
$$

となり、十分.

\medskip
$3^\circ \ n = 2$ の時\\
この時、$n a_n^2 + \frac{a_n}{n+1} \ne 0$ の時、与式左辺の最高次は $x^3$ となり矛盾. 従って $n a_n^2 + \frac{a_n}{n+1} = 0$ が必要で、$n=2, a_n \ne 0$ とあわせて $a_n = -\frac{1}{6}$ だから、$f(x) = -\frac{1}{6} x^2 + ax + b$ とおける. 代入して

$$
\begin{align*}
\left( -\frac{1}{6} x^2 + ax + b \right) \left( -\frac{1}{3} x + a \right) = \frac{1}{18} x^3 + \frac{a}{2} x^2 + bx + \frac{1}{18} - \frac{a}{2} - b = \frac{4}{9} (x - 1)
\end{align*}
$$

$$
\begin{align*}
\left( a^2 + \frac{2}{3} b \right) x + ab - \frac{1}{2} a - b + \frac{1}{18} = \frac{4}{9} (x - 1)
\end{align*}
$$

係数比較して

$$
\begin{align*}
a^2 + \frac{2}{3} b = \frac{4}{9} \quad \cdots \text{①}
\end{align*}
$$

$$
\begin{align*}
(a - 1) b - \frac{1}{2} a + \frac{1}{18} = -\frac{4}{9} \quad \cdots \text{②}
\end{align*}
$$

①を②に代入整理して $(a-1)\left(\frac{1}{2} - a^2\right) = 0$ だから、
$(a, b) = \left(1, -\frac{5}{6}\right), \left(\pm \frac{1}{\sqrt{2}}, \frac{1}{6}\right)$ だから、

$$
\begin{align*}
f(x) = -\frac{1}{6} x^2 + x - \frac{5}{6}, \quad -\frac{1}{6} x^2 \pm \frac{1}{\sqrt{2}} x + \frac{1}{6}
\end{align*}
$$

以上から

$$
\begin{align*}
f(x) = \frac{4}{9}, \quad -\frac{1}{6} x^2 + x - \frac{5}{6}, \quad -\frac{1}{6} x^2 \pm \frac{\sqrt{2}}{2} x + \frac{1}{6}
\end{align*}
$$

\end{proof}