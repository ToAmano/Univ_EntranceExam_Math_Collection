---
university: "kyodai"
category: "kouki"
year: "2000"
question: "5"
type: "solution"
title: "KYODAI 2000 kouki Q5 (solution)"
---

## 【解】

  極座標表示で，実数$r>0,0\le\theta<2\pi$に対して
  
$$
\begin{align}
\begin{dcases}
       & \alpha=re(\theta)                   \\
       & e(\theta)=\cos \theta + i\sin\theta
    \end{dcases}\label{2000-5:eq:1}
\end{align}
$$

  とおく．すると，
  および
  
$$
\begin{align*}
e^{-1}(\theta)
     & = \frac{1}{\cos \theta + i\sin\theta}\\& = \cos\theta -i\sin\theta\\& = e(-\theta)
\end{align*}
$$

  が成立する．
  また，加法定理によって
  
$$
\begin{align*}
e^2(\theta)
     & = \left(\cos\theta + i\sin\theta\right)^2          \\& = \cos^2\theta-\sin^2\theta + 2i\sin\theta\cos\theta\\& = e(2\theta)
\end{align*}
$$

  が成立する．
  従ってこれらの関係を繰り返し用いると，任意の整数$n$に対して
  
$$
\begin{align}
e^n(\theta) = e(n\theta) \label{2000-5:eq:2}
\end{align}
$$

  が成立する．以下この関係を用いる．

### (1)

  与えられた$a_n$の表現に$\eqref{2000-5:eq:1}$を代入して$\eqref{2000-5:eq:2}$を用いると
  
$$
\begin{align}
a_n
     & = r^n e^{n}(\theta) + \frac{1}{r^n} e^{-n}(\theta)                                                              \\& = r^n e(n\theta) + \frac{1}{r^n} e(-n\theta)                                                                    \\& = \left(r^n+\frac{1}{r^n}\right)\cos n\theta + i\left(r^n-\frac{1}{r^n}\right)\sin n\theta\label{2000-5:eq:3}
\end{align}
$$

  を得る．従って，
  
$$
\begin{align*}
|a_n|^2
     & = \left(r^n+\frac{1}{r^n}\right)^2 \cos^2 n\theta + \left(r^n-\frac{1}{r^n}\right)^2 \sin^2 n\theta\\& = \left(r^{2n}+\frac{1}{r^{2n}}+2\right)\cos^2 n\theta + \left(r^{2n}+\frac{1}{r^{2n}}-2\right)\sin^2 n\theta\\& = r^{2n}+\frac{1}{r^{2n}}+2(\cos^2 n\theta - \sin^2 n\theta)                                                  \\& = r^{2n}+\frac{1}{r^{2n}}+2\cos 2n\theta
\end{align*}
$$

  である．
  $n \to \infty$での$|a_n|^2 < 4$の成立が必要だが，$r \neq 1$の時，$|a_n|^2 \to \infty$となる
  から $r=1$．つまり $|\alpha|=1$である．$\cdots$(答)

### (2)

  $r=1$を$\eqref{2000-5:eq:3}$に代入すると，
  
$$
\begin{align*}
a_n = 2\cos n\theta
\end{align*}
$$

  となる．
  従って題意を示すには
  
$$
\begin{align*}
|\cos m\theta|> \frac{1}{2}\\
\end{align*}
$$

  となる$m \in \mathbb{N}$があることを示せば良い．
  $\theta$の値で場合分けすると，以下のようになる．
  \begin{itemize}
    \item $|\cos\theta| > \frac{1}{2}$の時，$|a_1|=2|\cos\theta|>1$より$m=1$とすれば良い．
    \item $|\cos\theta| < \frac{1}{2}$の時，$|a_2| = 2|\cos 2\theta| = 2|2\cos^2\theta - 1| = 2(1-2\cos^2\theta)> 1$ より$m=2$とすれば良い．
    \item $|\cos\theta| = \frac{1}{2}$の時，$|a_3| = 2|\cos 3\theta| = 2|4\cos^3\theta - 3\cos\theta| = 2 > 1 $より$m=3$とすれば良い．
  \end{itemize}
  以上で全ての場合が尽くされ，題意は示された．$\cdots$(答)
  
  

## 【解説】

### (1)
だけ解くのであれば，$|\alpha|$の大きさで場合分けするのが良いだろう．
  すなわち，$|\alpha|=1$以外の時は$a_n$が発散することを示せば良い．
  証明には三角不等式を利用する．複素数$a,b$に対して
  
$$
\begin{align*}
|a| + |b| \ge |a+b|
\end{align*}
$$

  が成立するというものだ．これは三角形の各辺の長さから図形的に示せるもので，
  複素数だけでなくベクトルでも成立する．
  高校数学では不等式の中から不要なものを排除したいときによく出てくる不等式である．

  今回の場合，愚直に$a=\alpha^n,b=\alpha^{-n}$としてしまうと不等号の向きが使いたい方向と逆になってしまう．
  すなわち
  
$$
\begin{align*}
|a_n| = \left|\alpha^n+\alpha^{-n}\right|\le\left|\alpha^n\right| + \left|\alpha^{-n}\right|
\end{align*}
$$

  で，$|a_n|$の発散を示したいのに上から押さえてしまう．
  こういう時はよく使われるテクニックがあり，式を
  
$$
\begin{align*}
|a| \ge |a+b| - |b|
\end{align*}
$$

  の形で利用する．ここで$a=\alpha^n+\alpha^{-n}$, $b=-\alpha^{-n}$とすれば
  
$$
\begin{align*}
|a_n| = \left|\alpha^n+\alpha^{-n}\right|\ge\left|\alpha^n\right| - \left|\alpha^{-n}\right|
\end{align*}
$$

  となって綺麗に使える．

  まず，$|\alpha|>1$の時は，三角不等式より
  
$$
\begin{align*}
|a_n| = |\alpha^n+\alpha^{-n}| \ge\left|\alpha^n\right| - \left|\alpha^{-n}\right|
\end{align*}
$$

  であり，
  
$$
\begin{align*}
& \lim_{n\to\infty}\left|\alpha^n\right| = \infty\\& \lim_{n\to\infty}\left|\alpha^{-n}\right| = 0
\end{align*}
$$

  より追い出しの原理より
  
$$
\begin{align*}
\lim_{n\to\infty} |a_n| = \infty
\end{align*}
$$

  となり発散する．

  同様に$|\alpha|<1$の時は三角不等式で$b=-\alpha^{n}$として
  
$$
\begin{align*}
|a_n| = |\alpha^n+\alpha^{-n}| \ge\left|\alpha^{-n}\right| - \left|\alpha^{n}\right|
\end{align*}
$$

  だから，同様に$a_n$は発散する．

  最後に$|\alpha|=1$の時は$\alpha=\cos\theta+i\sin\theta$とかけるから，本解答と同様に変形すれば$|a_n|<2$を満たすことがわかるだろう．