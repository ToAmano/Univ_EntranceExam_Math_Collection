---
university: "ukyoto"
category: "zenki"
year: "2001"
question: "6"
type: "solution"
title: "UKYOTO 2001 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $k \in \mathbb{N}$ に対し、$a_k = \int_{\frac{k-1}{n}\pi}^{\frac{k}{n}\pi} e^{-x} |\sin nx| dx$ とおく。$A_n = \int_0^\pi e^{-x} |\sin nx| dx$
おくと、

$$
\begin{align*}
A_n = \sum_{k=1}^n a_k \cdots \text{\textcircled{1}}
\end{align*}
$$

である。

$$
\begin{eqnarray*}
a_{k+1}&=& \int_{\frac{k}{n}\pi}^{\frac{k+1}{n}\pi} e^{-x} |\sin nx| dx \\&=& \int_{\frac{k-1}{n}\pi}^{\frac{k}{n}\pi} e^{-(t+\frac{\pi}{n})} |\sin n(t+\frac{\pi}{n})| dt\ (t = x - \frac{\pi}{n}) \\&=& e^{-\frac{\pi}{n}} a_k \cdots\text{\textcircled{2}}
\end{eqnarray*}
$$

又、

$$
\begin{eqnarray*}
a_1 &=& \int_0^{\frac{\pi}{n}} e^{-x}\sin nx dx \\&=& \left[\frac{e^{-x}}{1+n^2}(-\sin nx - n \cos nx) \right]_0^{\frac{\pi}{n}}\\&=& \frac{1}{1+n^2}\{ e^{-\frac{\pi}{n}}(n) - 1(-n) \}\\&=& \frac{n}{1+n^2}(e^{-\frac{\pi}{n}} + 1) \cdots\text{\textcircled{3}}
\end{eqnarray*}
$$

だから \textcircled{2} をくり返し用いて、

$$
\begin{align*}
a_k = e^{-\frac{(k-1)}{n}\pi} a_1
\end{align*}
$$

\textcircled{1} に代入して

$$
\begin{eqnarray*}
A_n &=& \sum_{k=0}^{n-1} a_1 e^{-\frac{k}{n}\pi}\\&=& a_1 \frac{1-e^{-n \frac{\pi}{n}}}{1-e^{-\frac{\pi}{n}}} = \frac{n}{1+n^2}(1+e^{-\frac{\pi}{n}}) \frac{1-e^{-\pi}}{1-e^{-\frac{\pi}{n}}}\\&=& \frac{n}{1+n^2}\frac{\frac{\pi}{n}}{1-e^{-\frac{\pi}{n}}}\left(\frac{1}{\frac{\pi}{n}}\right)(1+e^{-\frac{\pi}{n}})(1-e^{-\pi}) \\&=& \frac{1}{1+\frac{1}{n^2}}\frac{\frac{\pi}{n}}{1-e^{-\frac{\pi}{n}}}(1-e^{-\pi}) \left(\frac{1}{\pi}\right)(1+e^{-\frac{\pi}{n}}) \\&\xrightarrow{n\to\infty}& 1 \cdot 1 \cdot(1-e^{-\pi}) \cdot\left(\frac{1}{\pi}\right)\cdot 2 = \frac{2}{\pi}(1-e^{-\pi})
\end{eqnarray*}
$$

[解2] (\textcircled{1} まで同じ)
$[\frac{k-1}{n}\pi, \frac{k}{n}\pi]$ において、$e^{-\frac{k}{n}\pi} \le e^{-x} \le e^{-\frac{k-1}{n}\pi}$ だから、$|\sin nx| \ge 0$ とあわせて、

$$
\begin{align*}
e^{-\frac{k}{n}\pi} \int_{\frac{k-1}{n}\pi}^{\frac{k}{n}\pi} |\sin nx| dx \le a_k \le e^{-\frac{k-1}{n}\pi} \int_{\frac{k-1}{n}\pi}^{\frac{k}{n}\pi} |\sin nx| dx
\end{align*}
$$

$$
\begin{align*}
\frac{2}{n} e^{-\frac{k}{n}\pi} \le a_k \le \frac{2}{n} e^{-\frac{k-1}{n}\pi} = e^{\frac{\pi}{n}} \left( \frac{2}{n} e^{-\frac{k}{n}\pi} \right) \cdots \text{\textcircled{2}}
\end{align*}
$$

ここで、$B_n = \sum_{k=1}^n \frac{2}{n} e^{-\frac{k}{n}\pi}$ とすると、

$$
\begin{align*}
B_n = \frac{2}{n} e^{-\frac{\pi}{n}} \frac{1-e^{-\pi}}{1-e^{-\frac{\pi}{n}}}
\end{align*}
$$

だから \textcircled{1}、\textcircled{2} より、

$$
\begin{align*}
B_n \le A_n \le e^{\frac{\pi}{n}} B_n
\end{align*}
$$

はさみうちから

$$
\begin{align*}
A_n \to B_n
\end{align*}
$$

で、

$$
\begin{align*}
B_n = \frac{\frac{\pi}{n}}{1-e^{-\frac{\pi}{n}}} \frac{2}{\pi} e^{-\frac{\pi}{n}} (1-e^{-\pi}) \to \frac{2}{\pi}(1-e^{-\pi})
\end{align*}
$$

から

$$
\begin{align*}
A_n \to \frac{2}{\pi}(1-e^{-\pi})
\end{align*}
$$