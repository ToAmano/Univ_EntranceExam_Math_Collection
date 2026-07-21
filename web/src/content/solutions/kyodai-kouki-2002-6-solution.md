---
university: "kyodai"
category: "kouki"
year: "2002"
question: "6"
type: "solution"
title: "KYODAI 2002 kouki Q6 (solution)"
---

## 【解】

    加法定理を用いて被積分関数を変形すると
    
$$
\begin{align}
& f(x) + \int_{-\pi/2}^{\pi/2}(\sin x \cos y - \cos x \sin y) f(y) dy = x+1 \nonumber\\& f(x) + \sin x \int_{-\pi/2}^{\pi/2}\cos y f(y) dy           \nonumber\\& - \cos x \int_{-\pi/2}^{\pi/2}\sin y f(y) dy = x+1 \label{2002-6:eq:1}
\end{align}
$$

    となる．ここで定数$A,B$を
    
$$
\begin{align}
\begin{dcases}
            A & = \int_{-\pi/2}^{\pi/2} \cos y f(y) dy, \\
            B & = \int_{-\pi/2}^{\pi/2} \sin y f(y) dy
        \end{dcases}\label{2002-6:eq:2}
\end{align}
$$

    と置いて$\eqref{2002-6:eq:1}$に代入すると，
    
$$
\begin{align*}
f(x) = x+1 - A\sin x + B\cos x
\end{align*}
$$

    である．$\eqref{2002-6:eq:2}$に代入して
    
$$
\begin{align}
\begin{dcases}
            A = \int_{-\pi/2}^{\pi/2} \cos y (y+1-A\sin y+B\cos y) dy \\
            B = \int_{-\pi/2}^{\pi/2} \sin y (y+1-A\sin y+B\cos y) dy
        \end{dcases}\label{2002-6:eq:3}
\end{align}
$$

    である．

    ここで偶奇関数の性質も援用して，各種定積分は以下のように評価できる．
    
$$
\begin{align*}
& \int_{-\pi/2}^{\pi/2} y \cos y dy = 0                                                 \\& \int_{-\pi/2}^{\pi/2} y \sin y dy = 2                                                 \\& \int_{-\pi/2}^{\pi/2}\cos y dy =  2                                                  \\& \int_{-\pi/2}^{\pi/2}\sin y dy = 0                                                   \\& \int_{-\pi/2}^{\pi/2}\sin y \cos y dy = 0                                            \\& \int_{-\pi/2}^{\pi/2}\sin^2 y dy = \int_{-\pi/2}^{\pi/2}\cos^2 y dy = \frac{\pi}{2}
\end{align*}
$$

    これらを$\eqref{2002-6:eq:3}$に代入すると
    
$$
\begin{align}
& \begin{dcases}
               A = 2 + \frac{\pi}{2} B \\
               B = 2 - \frac{\pi}{2} A
           \end{dcases}\therefore& \begin{dcases}
               A = \frac{4\pi+8}{4+\pi^2} \\
               B = \frac{-4\pi+8}{4+\pi^2}
           \end{dcases}
\end{align}
$$

    となる．これらを$\eqref{2002-6:eq:1}$に代入して
    
$$
\begin{align*}
f(x) = x+1 - \frac{4\pi+8}{4+\pi^2}\sin x + \frac{4\pi-8}{4+\pi^2}\cos x
\end{align*}
$$

    が求める関数である．    $\cdots$(答)
    

## 【解説】