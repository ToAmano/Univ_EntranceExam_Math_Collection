---
university: "todai"
category: "zenki"
year: "1972"
question: "5"
type: "solution"
title: "TODAI 1972 zenki Q5 (solution)"
---

\input{macros}
     \begin{oframed}
     $h(x)$は$-\infty<x<\infty$で$2$回微分可能なある関数で，$f(x)$がどのような一次関数であって
     も，$u(x)=\dint{o}{x}h(t)f(t)dt+h(x)\dint{x}{1}f(t)dt$とおけば，
          

1.  $\dfrac{d^2u}{dx^2}=f(x)$

     および
          

1.  $u(0)=0$

     が成り立つ．このとき，$h(x)$を求めよ．     
     \end{oframed}

## 【解】

$f(x)$を$f$などと略記する．題意の条件から
     
<span id="1"></span><span id="2"></span><span id="3"></span>
$$
\begin{cases}
u=\dint{o}{x}hfdt+h\dint{x}{1}fdt \\
     u''=f \\
     u=0
\end{cases}
$$

まず，\eqref{1}で$x=0$として,\eqref{3}から
     
$$
\begin{align*}
0=h(0)\dint{x}{1}fdt
\end{align*}
$$

ここで$f$は任意の一次関数だから$\dint{x}{1}fdt\equiv0$とはならないので(例えば$f=x$)
     
$$
\begin{align}
h(0)=0\label{0}
\end{align}
$$

である．

 \eqref{1}の両辺を$x$で微分する．
     
$$
\begin{align*}
u'&=hf+h'\int_x^1fdt-hf  \\&=h'\int_x^1fdt
\end{align*}
$$

 さらに微分して
      
$$
\begin{align*}
u''=h''\int_x^1fdt-h'f
\end{align*}
$$

\eqref{2}を代入して
     
$$
\begin{align}
\{1+h'\}f=h''\int_x^1fdt\label{4}
\end{align}
$$

$f(x)$は任意の一次関数で，$a_{\not=0},b\in\mathbb{R}$として，\eqref{4}に$f(x)=ax+b$を代入したとき両辺$a$で割ることにより，$f(x)=x+b$のみ考えれば良いことがわかる．実際に代入して
     
$$
\begin{align*}
&\{1+h'\}(x+b)=\left[\frac{1}{2}t^2+bt\right]_x^1h'' \\
     =&\{\frac{1}{2}(1-x^2)+b(1-x)\}h'' \\
\end{align*}
$$

これが$b$についての恒等式だから係数比較して，
     
<span id="5"></span><span id="6"></span>
$$
\begin{cases}
1+h'-(1-x)h''=0 \\
     (1+h')x-\frac{1}{2}h''(1-x)(1+x)=0 
\end{cases}
$$

となる．\eqref{5}を\eqref{6}に代入して
     
$$
\begin{align*}
&(1+h')x-\frac{1}{2}(1+h')(1+x)=0 \\\Longleftrightarrow&(1+h')(x-1)=0
\end{align*}
$$

これが$x$についての恒等式だから，$h'=-1$が従う．\eqref{0}と合わせて
     
$$
\begin{align*}
h(x)=-x
\end{align*}
$$

である．これが\eqref{1}，\eqref{2}，\eqref{3}を満たすことは容易に確かめられる．ゆえに求める関数は
     \[h(x)=-x\]
である．$\cdots$(答)