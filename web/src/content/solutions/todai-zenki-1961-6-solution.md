---
university: "todai"
category: "zenki"
year: "1961"
question: "6"
type: "solution"
title: "TODAI 1961 zenki Q6 (solution)"
---

\input{macros}
\begin{oframed}
$a$，$b$，$c$は定数であって，函数$f(x)=a\sin x+b\cos x+c\cos 2x$は$x=\dfrac{\pi}{4}$において
極大値$6\sqrt{2}$をとり，また$\int_0^{2\pi} f(x)\cos x dx=5\pi$である．このとき　\\

1.  $a$，$b$，$c$を求める．

2.  $0\le x\le 2\pi$の範囲で$f(x)$を最小にする$x$の値とその時の$f(x)$の値とを求めよ．

\end{oframed}

## 【解】

     $\cos x=t$,$\sin x=s$とおく．
     \[f'(x)=at-bs+2c\cos 2x\]
     である．まず，極大値の条件から
     $f\left(\dfrac{\pi}{4}\right)=0$が必要である．これと題意の条件から
          
$$
\begin{align*}
&\left\{\begin{array}{l}
               f'\left(\dfrac{\pi}{4}\right)=0 \\
               f\left(\dfrac{\pi}{4}\right)=6\sqrt{2} \\
               \dint{0}{2\pi}f(x)\cos x dx=5\pi 
               \end{array}\right.\\\Leftrightarrow&\left\{\begin{array}{l}
               \dfrac{\sqrt{2}}{2}(a-b)=0 \\
               \dfrac{\sqrt{2}}{2}(a+b)+c=6\sqrt{2} \\
               b\pi=5\pi 
               \end{array}\right.
\end{align*}
$$

    故に$(a,b,c)=(5,5,\sqrt{2})$となる．
      $f'(x)$に値を代入する．
          
$$
\begin{align*}
f'(x)&=5t-5s+2\sqrt{2}(t^2-s^2) \\&=(t-s)\left(5+4\sin\left(x+\frac{\pi}{4}\right)\right)
\end{align*}
$$

     したがって，下表を得る．
      
$$
\begin{align*}
\begin{array}{|c|c|c|c|c|c|c|c|} \hline
     x & 0 &    &  \pi/4&     &5\pi/4            &     &2\pi  \\ \hline
     f' &    &+  & 0      & -    & 0                 &+   &        \\ \hline
     f &  5 &\ne&        &\se &-4\sqrt{2}      &\ne&        \\ \hline
     \end{array}
\end{align*}
$$

     故に$x=\dfrac{\pi}{4}$で極大となり十分である．以上から
     

1.  $(a,b,c)=(5,5,\sqrt{2})$

2.  $\min f(x)=f\left(\dfrac{5\pi}{4}\right)=-4\sqrt{2}$

     となる．$\cdots$(答)