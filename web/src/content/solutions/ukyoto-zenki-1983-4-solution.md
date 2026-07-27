---
university: "ukyoto"
category: "zenki"
year: "1983"
question: "4"
type: "solution"
title: "UKYOTO 1983 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解]\\
(1)\\
\begin{tikzpicture}
\coordinate (A) at (0,0);
\coordinate (B) at (4,0);
\coordinate (C) at (2,3);
\draw (A) -- (B) -- (C) -- cycle;
\coordinate (R) at (1,0);
\coordinate (P) at (3,0);
\coordinate (Q) at (1,1.5);
\draw (Q) -- (P) -- (R) -- cycle;
\node[below left] at (A) {A};
\node[below right] at (B) {B};
\node[above] at (C) {C};
\node[below] at (R) {R};
\node[below] at (P) {P};
\node[left] at (Q) {Q};
\end{tikzpicture}
\begin{tikzpicture}
\coordinate (O) at (0,0);
\coordinate (A) at (3,0);
\coordinate (B) at (0,3);
\coordinate (C) at (1.5,1.5);
\draw (O) -- (A) node[midway, below] {$a$};
\draw (O) -- (B) node[midway, left] {$b$};
\draw (O) -- (C) node[midway, right] {$c$};
\draw (A) -- (B) -- (C) -- cycle;
\node[below left] at (O) {O};
\node[right] at (A) {A};
\node[above] at (B) {B};
\node[above right] at (C) {C};
\end{tikzpicture}

底面を各々$\triangle ABC, \triangle PQR$とみると、高さ一定だから

$$
\begin{align*}
V_{OPQR} : V_{OABC} = \triangle PQR : \triangle ABC \quad \cdots \text{①}
\end{align*}
$$

である。三角形の相似から

$$
\begin{align*}
\overline{AQ} : \overline{AO} = a : \sqrt{a^2+c^2} \therefore \overline{AQ} = \frac{a^2}{\sqrt{a^2+c^2}}
\end{align*}
$$

同様にして

$$
\begin{align*}
\overline{AR} = \frac{a^2}{\sqrt{a^2+b^2}}, \quad \overline{BP} = \frac{b^2}{\sqrt{b^2+c^2}}
\end{align*}
$$

だから $\triangle ABC$の面積を1として

$$
\begin{align*}
\triangle ARQ &= \frac{a^2}{a^2+b^2}\cdot\frac{a^2}{a^2+c^2}\\\triangle BPR &= \frac{b^2}{a^2+b^2}\cdot\frac{b^2}{b^2+c^2}\\\triangle PCQ &= \frac{c^2}{b^2+c^2}\cdot\frac{c^2}{a^2+c^2}
\end{align*}
$$

だから

$$
\begin{align*}
\triangle PQR &= 1 - \frac{a^4(b^2+c^2) + b^4(c^2+a^2) + c^4(a^2+b^2)}{(a^2+b^2)(b^2+c^2)(c^2+a^2)}\\&= \frac{2a^2b^2c^2}{(a^2+b^2)(b^2+c^2)(c^2+a^2)}
\end{align*}
$$

より ①から

$$
\begin{align*}
V_{OPQR} : V_{OABC} = 2a^2b^2c^2 : (b^2+c^2)(c^2+a^2)(a^2+b^2)
\end{align*}
$$

(2) (1)から

$$
\begin{align*}
\frac{2a^2b^2c^2}{(b^2+c^2)(c^2+a^2)(a^2+b^2)} \le \frac{1}{4}
\end{align*}
$$

$$
\begin{align*}
8ABC \le (B+C)(C+A)(A+B) \quad \cdots \text{②}
\end{align*}
$$

($A=a^2, B=b^2, C=c^2$ とおいた)\\
を示せばよい。A,B,CからAM-GMより

$$
\begin{align*}
B+C \ge 2\sqrt{BC} > 0
\end{align*}
$$

などとした3式をかけあわせると ②は示される(終)