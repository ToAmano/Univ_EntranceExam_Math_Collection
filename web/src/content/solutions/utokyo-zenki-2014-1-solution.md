---
university: "utokyo"
category: "zenki"
year: "2014"
question: "1"
type: "solution"
title: "UTOKYO 2014 zenki Q1 (solution)"
---

1.  右のように空間座標をとる．
  四角形 $OPQR$ は平行四辺形である．
  

$$
\begin{align*}
\vec{OP} = \begin{pmatrix} 1 \\ 0 \\ \tan\alpha \end{pmatrix}, \quad \vec{OQ} = \begin{pmatrix} 0 \\ 1 \\ \tan\beta \end{pmatrix}
\end{align*}
$$

  だから，
  

$$
\begin{align*}
S &= \sqrt{|\vec{OP}|^2 |\vec{OQ}|^2 - (\vec{OP} \cdot \vec{OQ})^2}\\&= \sqrt{(1 + \tan^2\alpha)(1 + \tan^2\beta) - (\tan\alpha \cdot \tan\beta)^2}\\&= \sqrt{1 + \tan^2\alpha + \tan^2\beta}
\end{align*}
$$

2.  $a = \tan\alpha, \, b = \tan\beta$ とおく．$\alpha + \beta = \dfrac{\pi}{4}$ より，
  

$$
\begin{align*}
\tan\frac{\pi}{4} = \tan(\alpha + \beta) = \frac{a + b}{1 - ab} = 1 \quad \cdots \text{①}
\end{align*}
$$

  また，(1) 及び $S = \dfrac{7}{6}$ から，
  

$$
\begin{align*}
\left(\frac{7}{6}\right)^2 = 1 + a^2 + b^2 = 1 + (a+b)^2 - 2ab \quad \cdots \text{②}
\end{align*}
$$

  ①より $ab = 1 - (a+b)$ だから，これを②に代入して，
  

$$
\begin{align*}
\frac{49}{36} = 1 + (a+b)^2 - 2 + 2(a+b)
\end{align*}
$$

  

$$
\begin{align*}
(a+b)^2 + 2(a+b) - \frac{85}{36} = 0
\end{align*}
$$

  これを $a+b$ について解くと，
  

$$
\begin{align*}
a+b = -1 \pm \sqrt{1 + \frac{85}{36}} = -1 \pm \frac{11}{6}
\end{align*}
$$

  $0 \leqq \alpha < \dfrac{\pi}{2}, \, 0 \leqq \beta < \dfrac{\pi}{2}$ より $a + b \geqq 0$ だから，複号正を採用して，
  

$$
\begin{align*}
a+b = \frac{5}{6}
\end{align*}
$$

  ①から $ab = 1 - \dfrac{5}{6} = \dfrac{1}{6}$ だから，$a, b$ は次の2次方程式
  

$$
\begin{align*}
x^2 - \frac{5}{6}x + \frac{1}{6} = 0
\end{align*}
$$

  の2解であり，これを解くと $x = \dfrac{1}{2}, \, \dfrac{1}{3}$ となる．
  $\alpha \leqq \beta$ から $a \leqq b$（$0 \leqq x < \dfrac{\pi}{2}$ で $\tan x$ は単調増加）だから，
  

$$
\begin{align*}
\tan\alpha = a = \frac{1}{3}
\end{align*}
$$