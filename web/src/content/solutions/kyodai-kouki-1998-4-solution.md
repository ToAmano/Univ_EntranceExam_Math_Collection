---
university: "kyodai"
category: "kouki"
year: "1998"
question: "4"
type: "solution"
title: "KYODAI 1998 kouki Q4 (solution)"
---

## 【解】

  （1）
  $f(x) = \sin(x+a) - x\sin a$ とおく．
  問題文から，
  
$$
\begin{align*}
x_n = n\pi+\alpha_n \quad(0<\alpha_n<\pi)
\end{align*}
$$

  とおける．

  題意の条件より $f(x_n)=0$ なので，
  
$$
\begin{align*}
\sin(n\pi+\alpha_n+a) - (n\pi+\alpha_n) \sin(n\pi + \alpha_n) = 0
\end{align*}
$$

  ここで
  
$$
\begin{align*}
\sin(n\pi+\alpha_n+a) & = (-1)^n \sin(\alpha_n+a) \\\sin(n\pi+\alpha_n)   & = (-1)^n \sin\alpha_n
\end{align*}
$$

  だから，$n$ の偶奇にかかわらず
  
$$
\begin{align}
\sin(\alpha_n+a) - (n\pi+\alpha_n) \sin\alpha_n = 0 \label{1998-4:eq:1}
\end{align}
$$

  である．

  さて，$\alpha_n$ の定義から題意の極限は
  
$$
\begin{align*}
\lim_{n\to\infty}\alpha_n
\end{align*}
$$

  に等しい．
  $\eqref{1998-4:eq:1}$を整理して
  
$$
\begin{align}
\sin\alpha_n
     & = \frac{\sin(\alpha_n+a)}{n\pi+\alpha_n}\\& \xrightarrow{n\to\infty} 0 \quad(\because 0<\alpha_n<\pi)  \label{1998-4:eq:2}
\end{align}
$$

  だから， $\sin x$ の連続性 と $\alpha_n$ の値域から
  
$$
\begin{align}
\lim_{n\to\infty}\alpha_n = 0 \quad\text{or}\quad\pi\label{1998-4:eq:3}
\end{align}
$$

  である．

  以下でどちらが正しいかを調べる．
  そのために$n\sin\alpha_n$の極限を求める．
  $\eqref{1998-4:eq:1}$を整理して
  
$$
\begin{align*}
\pi n \sin\alpha_n = \sin(\alpha_n+a) - \alpha_n \sin\alpha_n
\end{align*}
$$

  だから，$\eqref{1998-4:eq:3}$に注意して$n\to\infty$の極限を取ると
  
$$
\begin{align*}
\lim_{n\to\infty} n \sin\alpha_n =
    \begin{dcases}
      \frac{\sin a}{\pi} >0  & (\text{if } \lim_{n\to\infty} \alpha_n = 0)   \\
      -\frac{\sin a}{\pi} <0 & (\text{if } \lim_{n\to\infty} \alpha_n = \pi)
    \end{dcases}
\end{align*}
$$

  である．ただし$0<a<\pi$から$\sin a>0$であることを用いた．
  $0<\alpha_n<\pi$より，$\sin \alpha_n>0$であるから，極限値が負になることはないため，
  
$$
\begin{align*}
\lim_{n\to\infty}\alpha_n = 0
\end{align*}
$$

  が正しい．よってこれが求める極限値である．$\cdots$(答)

### (2)
 (1)と同様に $n\alpha_n$ の極限を求めれば良い．
  $\eqref{1998-4:eq:1}$の両辺に $\alpha_n$ をかけて整理すると
  
$$
\begin{align*}
& \alpha_n\sin(\alpha_n+a) - (n\pi\alpha_n+\alpha^2_n) \sin\alpha_n = 0                            \\& n\pi\alpha_n = \frac{\alpha_n\sin (\alpha_n+a)}{\sin \alpha_n } - \alpha^2_n                       \\& n \alpha_n = \frac{1}{\pi}\left(\frac{\sin(\alpha_n+a)}{\sin \alpha_n/\alpha_n} - \alpha_n^2\right)
\end{align*}
$$

  である．

### (1)
から $n\to\infty$ の時 $\alpha_n \to 0$ だから
  
$$
\begin{align*}
\lim_{n\to\infty} n \alpha_n
     & =     \lim_{n\to\infty}\frac{1}{\pi}\left(\frac{\sin(\alpha_n+a)}{\sin \alpha_n/\alpha_n} - \alpha_n^2\right)\\& =    \frac{\sin a}{\pi}
\end{align*}
$$

  が求める極限値である．$\cdots$(答)

  
  

## 【解説】