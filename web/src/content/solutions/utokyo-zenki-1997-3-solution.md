---
university: "utokyo"
category: "zenki"
year: "1997"
question: "3"
type: "solution"
title: "UTOKYO 1997 zenki Q3 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

 $0 < r < 1 \quad \cdots \text{①}$

\bigskip

(1) $|\vec{PA}| = |\vec{PB}|$ から, $P$ は線分 $AB$ の垂直2等分面 $x=y$ 上にあるので, $P(p,p,q)$ と表せる. この時

$$
\begin{align*}
|\vec{PA}| = r |\vec{PO}| \iff |\vec{PA}|^2 = r^2 |\vec{PO}|^2
\end{align*}
$$

で,

$$
\begin{align*}
(p-1)^2 + p^2 + q^2 = r^2 (2p^2 + q^2)
\end{align*}
$$

を満たす $p, q$ の存在条件をしらべれば良い.

$$
\begin{align*}
2(1-r^2)p^2 - 2p + (1-r^2)q^2 + 1 = 0 \quad \cdots \text{②}
\end{align*}
$$

$$
\begin{align*}
2(1-r^2)\left[ p - \frac{1}{2(1-r^2)} \right]^2 + (1-r^2)q^2 + 1 - \frac{1}{2(1-r^2)} = 0
\end{align*}
$$

①及び $p, q \in \mathbb{R}$ から, $p, q$ の存在条件は

$$
\begin{align*}
1 - \frac{1}{2(1-r^2)} \le 0 \iff \frac{\sqrt{2}}{2} \le r < 1 \quad (\because \text{①})
\end{align*}
$$

\begin{tikzpicture}[scale=1.2, >=stealth]
\draw[->] (0,0,0) -- (3,0,0) node[right] {$y$};
\draw[->] (0,0,0) -- (0,3,0) node[above] {$z$};
\draw[->] (0,0,0) -- (0,0,3) node[below left] {$x$};

\coordinate (O) at (0,0,0);
\coordinate (A) at (0,0,2);
\coordinate (B) at (2,0,0);
\coordinate (P) at (1.5, 2.0, 1.5);

\draw[dashed] (0,0,0) -- (2,0,2);
\draw[thick] (O) -- (A) node[below left] {$A$};
\draw[thick] (O) -- (B) node[below right] {$B$};

\draw[thick] (P) circle (1pt) node[above right] {$P$};
\draw (P) -- (A);
\draw (P) -- (B);
\draw (P) -- (O);
\draw[dashed] (P) -- (1.5, 0, 1.5);
\end{tikzpicture}

\bigskip

(2) ②が満たされているとする. また $r \to 1-0$ をかんがえるので, $r$ は(1)の条件を満たすとして良い.

$$
\begin{align*}
\vec{PA} \cdot \vec{PB} = \begin{pmatrix} 1-p \\ -p \\ -q \end{pmatrix} \cdot \begin{pmatrix} -p \\ 1-p \\ -q \end{pmatrix} = 2p(p-1) + q^2
\end{align*}
$$

$$
\begin{align*}
= 2p(p-1) + \left[ \frac{2}{1-r^2}p - \frac{1}{1-r^2} - 2p^2 \right] = \frac{2r^2}{1-r^2}p - \frac{1}{1-r^2} \quad \cdots \text{③}
\end{align*}
$$

ここで, ②から

$$
\begin{align*}
p = \frac{1}{2(1-r^2)}\left[ 1 \pm \sqrt{1 - 2(1-r^2)\left\{(1-r^2)q^2+1\right\}} \right] = \frac{1}{2(1-r^2)}\left[ 1 \pm \sqrt{2r^2-1 - 2(1-r^2)^2 q^2} \right]
\end{align*}
$$

これを $\alpha, \beta$ ($\alpha \le \beta$) とすると, ①から

$$
\begin{align*}
\begin{cases}
\max \beta = \frac{1}{2(1-r^2)} \left[ 1 + \sqrt{2r^2-1} \right] \equiv a \\
\min \alpha = \frac{1}{2(1-r^2)} \left[ 1 - \sqrt{2r^2-1} \right] \equiv b
\end{cases}
\end{align*}
$$

で, $b \le p \le a$ である. ②, ③から

$$
\begin{align*}
M(r) - m(r) = \frac{2r^2}{1-r^2}(a-b) = \frac{2r^2 \cdot 2}{2(1-r^2)^2} \sqrt{2r^2-1}
\end{align*}
$$

だから

$$
\begin{align*}
(1-r)^2 \{ M(r) - m(r) \} = \frac{2(1-r)^2 r^2}{(1+r)^2(1-r)^2} \sqrt{2r^2-1}
\end{align*}
$$

$$
\begin{align*}
= 2 \left(\frac{r}{1+r}\right)^2 \sqrt{2r^2-1} \longrightarrow \frac{1}{2} \quad (r \to 1-0)
\end{align*}
$$