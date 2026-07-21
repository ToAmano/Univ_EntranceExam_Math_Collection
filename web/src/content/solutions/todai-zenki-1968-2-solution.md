---
university: "todai"
category: "zenki"
year: "1968"
question: "2"
type: "solution"
title: "TODAI 1968 zenki Q2 (solution)"
---

\input{macros}
     \begin{oframed}
     正方形$ABCD$を底面とし，$V$を原点とする正四角錐において，底面と斜面のなす角が$45^\circ$
     のとき，となりあう二つの斜面のなす二面角を求めよ．
     \end{oframed}

## 【解】

 底面が一辺$2$の正方形であるとしてよい．そこで$xyz$座標を設定し$A(1,1,0)$，
$B(1,-1,0)$，$C(-1,-1,0)$，$D(-1,1,0)$とおく．底面と斜面の成す角が$\pi/4$だから，
$V(0,0,1)$として考えてよい．対称性から平面$VAB$と平面$VBC$のみ考えればよい．これらの平面の基底をなす$2$ベクトルは
     
$$
\begin{align*}
VAB:&\vthree{0}{1}{0} , \vthree{-1}{0}{1}\\
     VBC:&\vthree{1}{0}{0} , \vthree{0}{1}{1}
\end{align*}
$$

であるから，法線ベクトルは
     
$$
\begin{align*}
&VAB:\vec{a}=\vthree{1}{0}{1}&VBC:\vec{b}=\vthree{0}{1}{1}
\end{align*}
$$

となる．故にこれら$2$ベクトルの成す角$\theta$として($0\le\theta\le\pi$)
     
$$
\begin{align*}
\cos\theta&=\frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}\\&=\frac{1}{\sqrt{2}\sqrt{2}}=\frac{1}{2}
\end{align*}
$$

である．従って$\theta=\dfrac{\pi}{3}$である．
故に$2$平面の成す角$t$は$0\le t\le\dfrac{\pi}{2}$で考えて
     
$$
\begin{align*}
t=\min(\theta,\pi-\theta)=\frac{\pi}{3}
\end{align*}
$$

である．$\cdots$(答)