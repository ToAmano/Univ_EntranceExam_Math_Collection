---
university: "utokyo"
category: "zenki"
year: "1975"
question: "1"
type: "solution"
title: "UTOKYO 1975 zenki Q1 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $P, Q$ が2辺 $CA, AB$ 上にある時, $P$ が $CA$, $Q$ が $AB$ 上にあるとして良い。
$|PA|=x, |QA|=y \quad (0 \le x \le 36, 0 \le y \le 25 \quad \cdots \text{①})$ とする。題意から

$$
\begin{align*}
xy = \frac{1}{2} \cdot 25 \cdot 36 = 450 \quad \cdots \text{②}
\end{align*}
$$

$\triangle APQ$ で余弦定理から,

$$
\begin{align*}
\begin{aligned}
|PQ|^2 &= |AP|^2 + |AQ|^2 - 2 AP \cdot AQ \cos \angle PAQ \\
&= x^2 + y^2 - 900 \cos \angle PAQ
\end{aligned}
\end{align*}
$$

$x^2, y^2 > 0$ から, AM-GM 及び ② から,

$$
\begin{align*}
|PQ|^2 \ge 900 (1 - \cos \angle PAQ) \quad \cdots \text{③}
\end{align*}
$$

等号成立は $x=y=15\sqrt{2}$ の時成立する。ここで $\triangle ABC$ について余弦定理から,

$$
\begin{align*}
\cos \angle CAB = \frac{36^2 + 25^2 - 32^2}{2 \cdot 36 \cdot 25} = \frac{897}{2 \cdot 900}
\end{align*}
$$

から, ③より,

$$
\begin{align*}
|PQ|^2 \ge \frac{903}{2} \quad \cdots \text{④}
\end{align*}
$$

以下同様にして,

1.  $P, Q$ が2辺 $AB, BC$ 上にある時
  

$$
\begin{align*}
|PQ|^2 \ge \frac{1247}{2} \quad (\text{等号成立は } |PB|=|QB|=20) \quad \cdots \text{⑤}
\end{align*}
$$

2.  $P, Q$ が2辺 $BC, CA$ 上にある時
  

$$
\begin{align*}
|PQ|^2 \ge \frac{609}{2} \quad (\text{等号成立は } |PC|=|QC|=24) \quad \cdots \text{⑥}
\end{align*}
$$

④, ⑤, ⑥から, もとめるのは,

$$
\begin{align*}
\text{2辺 } BC, CA \text{上の, } C \text{からの距離が } 24 \text{である2点.}
\end{align*}
$$