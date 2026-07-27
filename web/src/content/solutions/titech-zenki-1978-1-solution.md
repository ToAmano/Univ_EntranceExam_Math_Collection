---
university: "titech"
category: "zenki"
year: "1978"
question: "1"
type: "solution"
title: "TITECH 1978 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$$
\begin{align*}
(x^3+ax^2+bx+c)^2=(x^2-1)(x^2+px+q)^2+D
\end{align*}
$$

が $x$ についての恒等式である．左辺，右辺を各々 $f(x),g(x)$ とする．

$$
\begin{align*}
f(x)=x^6+2ax^5+(2b+a^2)x^4+(2c+2ab)x^3+(2ac+b^2)x^2+2bcx+c^2
\end{align*}
$$

$$
\begin{align*}
g(x)=x^6+2px^5+(p^2+2q-1)x^4+(2pq-2p)x^3+(q^2-p^2-2q)x^2-2pqx-q^2+D
\end{align*}
$$

係数比較して，

$$
\begin{align*}
a=p, \quad 2b=2q-1, \quad ab+c=pq-p, \quad 2ac+b^2=q^2-p^2-2q, \quad bc=-pq, \quad c^2=-q^2+D
\end{align*}
$$

を得る．したがって，第1，2式から

$$
\begin{align*}
a=p, \qquad b=q-\frac12 \quad\cdots\text{①}
\end{align*}
$$

第3式に代入して

$$
\begin{align*}
c=-\frac12 p \quad\cdots\text{②}
\end{align*}
$$

第4式から $q=-\dfrac14$ となり①より $b=-\dfrac34$ となる．第5式から，

$$
\begin{align*}
bc=-pq \quad\Longrightarrow\quad\frac38p=\frac14p \quad\therefore\ p=0
\end{align*}
$$

だから，①②より $a=c=0$ で，最後の式から，

$$
\begin{align*}
D=c^2+q^2=0+\frac{1}{16}=\frac{1}{16}
\end{align*}
$$