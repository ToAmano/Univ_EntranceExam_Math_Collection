---
university: "titech"
category: "zenki"
year: "1964"
question: "6"
type: "solution"
title: "TITECH 1964 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

\begin{proof}[解]

1.  

$$
\begin{align*}
\int_0^1 f(x) \, dx = \frac{1}{4} + \frac{a}{3} + \frac{b}{2} + c \qquad \dots \text{\textcircled{1}}
\end{align*}
$$

    

$$
\begin{align*}
\sum_{k=1}^n f\left(\frac{k}{n}\right) = \sum_{k=1}^n \left[ \frac{1}{n^3} k^3 + \frac{a}{n^2} k^2 + \frac{b}{n} k + c \right]
\end{align*}
$$

    

$$
\begin{align*}
= \frac{1}{n^3} \left\{ \frac{n(n+1)}{2} \right\}^2 + \frac{a}{n^2} \frac{1}{6} n(n+1)(2n+1) + \frac{b}{n} \frac{1}{2} n(n+1) + cn
\end{align*}
$$

    

$$
\begin{align*}
= \frac{(n+1)^2}{4n} + \frac{a}{6} \frac{(n+1)(2n+1)}{n} + \frac{b}{2}(n+1) + cn
\end{align*}
$$

    

$$
\begin{align*}
= \frac{1}{4}\left(n + 2 + \frac{1}{n}\right) + \frac{a}{6}\left(2n + 3 + \frac{1}{n}\right) + \frac{b}{2}(n+1) + cn
\end{align*}
$$

    

$$
\begin{align*}
= \left(\frac{1}{4} + \frac{a}{3} + \frac{b}{2} + c\right) n + \left(\frac{1}{2} + \frac{a}{2} + \frac{b}{2}\right) + \left(\frac{1}{4} + \frac{a}{6}\right) \frac{1}{n} \qquad \dots \text{\textcircled{2}}
\end{align*}
$$

    \textcircled{1}\textcircled{2}から
    

$$
\begin{align*}
n \int_0^1 f(x) \, dx - \sum_{k=1}^n f\left(\frac{k}{n}\right) = -\left(\frac{1}{2} + \frac{a}{2} + \frac{b}{2}\right) - \left(\frac{1}{4} + \frac{a}{6}\right) \frac{1}{n} \xrightarrow{n \to \infty} -\frac{a+b+1}{2}
\end{align*}
$$

2.  

$$
\begin{align*}
f(1+h) - f(1) = \{(1+h)^3 - 1\} + a\{(1+h)^2 - 1\} + b\{(1+h) - 1\}
\end{align*}
$$

    

$$
\begin{align*}
= (h^3 + 3h^2 + 3h) + a(h^2 + 2h) + bh
\end{align*}
$$

    

$$
\begin{align*}
f'(x) = 3x^2 + 2ax + b
\end{align*}
$$

    から
    

$$
\begin{align*}
\frac{f(1+h) - f(1)}{h^2} - \frac{f'(1)}{h} = h + (3+a) + \frac{3+2a+b}{h} - \frac{3+2a+b}{h}
\end{align*}
$$

    

$$
\begin{align*}
= h + (3+a) \xrightarrow{h \to 0} 3+a
\end{align*}
$$

\end{proof}