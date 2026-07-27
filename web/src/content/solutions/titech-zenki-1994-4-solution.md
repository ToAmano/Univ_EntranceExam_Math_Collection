---
university: "titech"
category: "zenki"
year: "1994"
question: "4"
type: "solution"
title: "TITECH 1994 zenki Q4 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

## 【解】

$$
\begin{align*}
f(m,n)=\frac12(m+n)(m+n+1)+n \quad(m,n\in\mathbb{Z}_{\ge0})
\end{align*}
$$

である．

**(1)** $(m,n)=(0,0)$は題意をみたす．以下他の場合をかんがえる．

$$
\begin{align*}
\frac12(m+n)(m+n+1)+n\le5
\end{align*}
$$

$$
\begin{align*}
(m+n)(m+n+1)+2n\le10 \quad\cdots\text{①}
\end{align*}
$$

$t=m+n$とすると，$n\ge0$から$t(t+1)\le10$となり，$1\le t$，$t\in\mathbb{N}$とあわせて，$t=1,2$となる．

**$1^\circ$ $t=1$**

$(m,n)=(0,1),(1,0)$で共に①をみたし十分．

**$2^\circ$ $t=2$**

$(m,n)=(0,2),(1,1),(2,0)$で共に①をみたし十分．

以上から，もとめる$(m,n)$は

$$
\begin{align*}
(m,n)=(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)
\end{align*}
$$

で図示して右図黒丸．

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/zenki/1994/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 条件を満たす$(m,n)$の図示（黒丸）</figcaption>
</figure>

**(2)** $f(m,n)=f(m',n')$とする．$(m,n)=(0,0)$の時は明らかで，他の場合をかんがえる．

$$
\begin{align*}
\frac12(m+n)(m+n+1)+n=\frac12(m'+n')(m'+n'+1)+n'
\end{align*}
$$

$$
\begin{align*}
t(t+1)+2n=t'(t'+1)+2n' \quad(t'=m'+n') \quad\cdots\text{②}
\end{align*}
$$

ここで，$f(x,y)=x^2+x+2y\ (0\le y\le x)$とおくと，これは$y$の単調増加関数で，

$$
\begin{align*}
x^2+x\le f(x,y)\le x^2+3x \quad\cdots\text{③}
\end{align*}
$$

となる．この両辺は$x$については単調増加で，$x=t$として，

$$
\begin{align*}
t^2+t\le f(t,n)\le t^2+3t
\end{align*}
$$

であり，$\{(t+1)^2+(t+1)\}-(t^2+3t)=2>0$から，異なる2自然数$t,t'$に対し，$f(t,n)=f(t',n')$となることはない．すなわち②が成立するには$t=t'$が必要で，この時，$n=n'$とすれば十分，この時$m=m'$も成立する．以上から，$f(m,n)=f(m',n')$ならば，$(m,n)=(m',n')$となる．