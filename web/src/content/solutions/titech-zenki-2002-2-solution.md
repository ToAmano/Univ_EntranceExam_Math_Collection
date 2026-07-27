---
university: "titech"
category: "zenki"
year: "2002"
question: "2"
type: "solution"
title: "TITECH 2002 zenki Q2 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

楕円$\dfrac{x^2}{17}+\dfrac{y^2}8=1$の外部の点$P(a,b)$を考える．

\textbf{$a=\pm\sqrt{17}$の時：} 一方の接線が$x=\pm\sqrt{17}$（垂直）だから，直交するにはもう一方が$y=\pm\sqrt8$（水平）である必要があり，このとき$P=(\pm\sqrt{17},\pm\sqrt8)$．

\textbf{$a\ne\pm\sqrt{17}$の時：} $P$から引いた接線は$y$軸に平行にならず，傾き$m$を持つので$\ell:y=m(x-a)+b$とおける．$P$は楕円の外部だから

$$
\begin{align*}
\frac{a^2}{17}+\frac{b^2}8>1 \quad\cdots\text{①}
\end{align*}
$$

$X=x/\sqrt{17},\ Y=y/\sqrt8$なる変換を行うと，楕円は$X^2+Y^2=1$（単位円）に，接線$\ell$は

$$
\begin{align*}
\ell':\ \sqrt8\,Y=m(\sqrt{17}X-a)+b
\end{align*}
$$

に移り，これも単位円に接する（接する条件は座標変換で保たれる）．よって，原点から$\ell'$までの距離が$1$：

$$
\begin{align*}
\frac{|b-ma|}{\sqrt{17m^2+8}}=1
\end{align*}
$$

両辺2乗して

$$
\begin{align*}
(b-ma)^2=17m^2+8 \iff(a^2-17)m^2-2abm+(b^2-8)=0 \quad\cdots\text{②}
\end{align*}
$$

$a\ne\pm\sqrt{17}$だから②は$m$の2次方程式で，2つの解が2本の接線の傾き$m_1,m_2$を与える．判別式（の$1/4$）は

$$
\begin{align*}
D/4=(ab)^2-(a^2-17)(b^2-8)=8a^2+17b^2-8\cdot17
\end{align*}
$$

①（両辺を$136=8\cdot17$倍）から$8a^2+17b^2>136$，よって$D/4>0$．したがって②は常に2つの異なる実解$m_1,m_2$を持つ（$P$から引いた2接線は常に存在する）．2接線が直交する条件は$m_1m_2=-1$で，解と係数の関係$m_1m_2=(b^2-8)/(a^2-17)$から

$$
\begin{align*}
\frac{b^2-8}{a^2-17}=-1 \iff a^2+b^2=25 \quad\cdots\text{③}
\end{align*}
$$

（$a=\pm\sqrt{17}$の場合の点$(\pm\sqrt{17},\pm\sqrt8)$も$17+8=25$をみたし，③に含まれる．）さらに，$a^2+b^2=25$をみたす点は自動的に①をみたす：$8<17$より$b^2/8\ge b^2/17$だから，$a^2/17+b^2/8\ge(a^2+b^2)/17=25/17>1$．

以上から，もとめる軌跡は円

$$
\begin{align*}
a^2+b^2=25
\end{align*}
$$