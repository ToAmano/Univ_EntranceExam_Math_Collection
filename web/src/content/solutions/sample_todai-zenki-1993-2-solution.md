---
university: "sample_todai"
category: "zenki"
year: "1993"
question: "2"
type: "solution"
title: "SAMPLE_TODAI 1993 zenki Q2 (solution)"
---

**【解】**

### (1)

  三角形ABCの重心の座標を
  
$$
\begin{align}
    \begin{dcases}
      x_g = \frac{x_1+x_2+x_3}{3} \\
      y_g = \frac{y_1+y_2+y_3}{3}
    \end{dcases}
  \end{align}
$$

  とおく．

  与えられた曲線と平行な曲線を
  
$$
\begin{align*}
    l: g(x,y) = a(x-x_g) + b(y-y_g) + c = 0
  \end{align*}
$$

  とおく．
  ここで$a,b$は所与の固定値（ただし$(a,b) \neq (0,0)$）であり，$c$が色々変わる時の$f(l)$の最小値を考えれば良い．
  $K=A,B,C$ に対し$k=1,2,3$ とおくと，点と直線の距離公式から
  
$$
\begin{align*}
    d(l,k) = \frac{|g(x_k, y_k)|}{\sqrt{a^2+b^2}}
  \end{align*}
$$

  なので，
  
$$
\begin{align*}
    T_k = a(x_k-x_g) + b(y_k-y_g)
  \end{align*}
$$

  とおくと，
  
$$
\begin{align*}
    f(l)
     & = \frac{1}{a^2+b^2} \sum_{k=1}^{3} \{g(x_k, y_k)\}^2                                                              \\
     & = \frac{1}{a^2+b^2} \sum_{k=1}^{3} [c^2 + 2T_kc + T_k^2]                                                          \\
     & = \frac{1}{a^2+b^2} \left[3c^2 + 2(\sum_{k=1}^{3} T_k)c + \sum_{k=1}^{3} T_k^2\right]                             \\
     & = \frac{3}{a^2+b^2} \left[\left(c+\frac{1}{3}\sum_{k=1}^{3} T_k\right)^2 + \frac{8}{9}\sum_{k=1}^{3} T_k^2\right]
  \end{align*}
$$

  である．
  $c$を動かすと
  
$$
\begin{align*}
    c = -\frac{1}{3}\sum_{k=1}^{3}T_k
  \end{align*}
$$

  で $f(l)$ は最小値をとる．
  この時の$c$を具体的に計算すると
  
$$
\begin{align*}
    c
     & = -\frac{1}{3} [a(x_1+x_2+x_3 - 3x_g) + b(y_1+y_2+y_3 - 3y_g)] \\
     & = 0
  \end{align*}
$$

  だから，$l$の方程式は
  
$$
\begin{align*}
    l_0 : a(x-x_g) + b(y-y_g) = 0
  \end{align*}
$$

  となる．従ってたしかに $l_0$ は $\triangle ABC$ の重心 $(x_g, y_g)$ を通る．
  よって題意は示された．$\cdots$(答)

### (2)

  並進対称性より$\triangle ABC$ の重心が $O(0,0)$ となるようにして考えて良い．
  回転対称性より$A(1,0)$ の時をかんがえれば良い．

  この時，残りのB，Cの座標について重心の条件から
  
$$
\begin{align}
    \begin{dcases}
      1+x_2+x_3=0 \\
      y_2+y_3=0
    \end{dcases} \label{1993-2:eq:1}
  \end{align}
$$

  である．

  以下，$0\le \theta < 2\pi$なる実数$\theta$を用いて
  
$$
\begin{align*}
    l: -\sin\theta x+\cos\theta y=0
  \end{align*}
$$

  とおく．$\theta$ と $l$ は１対１に対応する．
  従って，$f(l)$が最小になるような$\theta$が3つ存在する時を考えれば良い．

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \begin{axis}[
          axis lines=middle,   
          xlabel=$x$,          
          ylabel=$y$,          
          xmin=-1.8, xmax=1.8, 
          ymin=-1.8, ymax=1.8, 
          xtick=\empty,        
          ytick=\empty,        
          axis equal,          
          clip=false,          
        ]

        \coordinate (O) at (0,0);
        \coordinate (A) at (1,0);
        \coordinate (B) at (-0.5, {sqrt(3)/2});
        \coordinate (C) at (-0.5, {-sqrt(3)/2});

        \draw (A) -- (B) -- (C) -- cycle;

        \addplot[domain=-1.7:1.7, samples=2, thin] {tan(35)*x} node[pos=0.9, anchor=west] {$l$};

        \fill (A) circle (1.5pt) node[anchor=west, xshift=1pt] {A};
        \fill (B) circle (1.5pt) node[anchor=east, xshift=-2pt, yshift=1pt] {B};
        \fill (C) circle (1.5pt) node[anchor=east, xshift=-2pt, yshift=-1pt] {C};

        \node[anchor=north] at (A) {1};
        \node[anchor=north west] at (O) {O};

        \draw[->, thin] (0.6,0) arc (0:35:0.6);
        \node at (0.7, 0.22) {$\theta$};

      \end{axis}
    \end{tikzpicture}
    \caption{三角形ABCの様子}
    \label{1993-2:fig:1}
  \end{figure}

  点と直線の距離公式から
  
$$
\begin{align*}
    d(l,k)^2
     & = (-\sin\theta x_k+\cos\theta y_k)^2                                  \\
     & = \sin^2\theta x_k^2+\cos^2\theta y_k^2-2\cos\theta \sin\theta x_ky_k
  \end{align*}
$$

  だから，
  
$$
\begin{align*}
    f(l)
     & = \sum_{k=1}^3 d(l,k)^2
     & = \sin^2\theta(1+x_2^2+x_3^2) + \cos^2\theta (y_2^2+y_3^2) - 2\cos\theta\sin\theta (x_2y_2+x_3y_3)
  \end{align*}
$$

  である．
  \cref{1993-2:eq:1}および半角公式より
  
$$
\begin{align}
    f(l)
     & = \sin^2\theta (2x_2^2+2x_2+2) + 2y_2^2\cos^2\theta - 2\cos\theta\sin\theta(2x_2y_2+y_2) \\
     & = P(1-\cos2\theta) + Q(1+\cos2\theta) - R\sin2\theta                                     \\
     & = (-P+Q)\cos2\theta - R\sin2\theta + (P+Q) \label{1993-2:eq:2}
  \end{align}
$$

  と書ける．ただし
  
$$
\begin{align}
    \begin{dcases}
      P=x_2^2+x_2+1 \\
      Q=y_2^2       \\
      R=(2x_2+1)y_2
    \end{dcases} \label{1993-2:eq:3}
  \end{align}
$$

  とした．

  \cref{1993-2:eq:2}が３つの$\theta$で最小値をとる時，
  $\triangle ABC$が正三角形であることを示せば良い．

  
$$
\begin{align*}
    (-P+Q)^2+R^2 \neq 0
  \end{align*}
$$

  の時，三角関数の合成を用いて適当な実数$\alpha$があって
  
$$
\begin{align*}
    f(l) = \sqrt{(-P+Q)^2+R^2} \sin(2\theta+\alpha) + (P+Q)
  \end{align*}
$$

  が成り立つ．
  $0 \le \theta < 2\pi$から$\alpha \le 2\theta+\alpha < 2\pi+\alpha$ だから，
  $f(l)$は３つの$\theta$で最小値をとりえず不適である．

  したがって $(-P+Q)^2+R^2=0$ が必要である．この時$P,Q,R \in \mathbb{R}$ から
  
$$
\begin{align*}
    -P+Q=R=0
  \end{align*}
$$

  であり，この時$f(l)=P+Q$で$\theta$によらず一定であり，$3$つの$\theta$で最小値をとる．

  一定で十分である。\cref{1993-2:eq:3}に値を代入して
  
$$
\begin{align*}
    \begin{dcases}
      y_2^2 = x_2^2+x_2+1 \\
      y_2(2x_2+1) = 0
    \end{dcases}
  \end{align*}
$$

  第二式から $y_2=0$ または $x_2=-\frac{1}{2}$ である．
  $y_2=0$の時\cref{1993-2:eq:1}から$y_3=0$となり$\triangle ABC$ が三角形とならず不適である．

  よって$x_2=-\frac{1}{2}$ である．この時第一式から$y_2=\pm\frac{\sqrt{3}}{2}$ である．
  \cref{1993-2:eq:1}から$x_3 =-\frac{1}{2}, y_3=\mp\frac{\sqrt{3}}{2}$である．

  まとめると
  
$$
\begin{align*}
     & A=(1,0)
     & B=(-\frac{1}{2}, \pm\frac{\sqrt{3}}{2}) \\
     & C=(-\frac{1}{2}, \mp\frac{\sqrt{3}}{2})
  \end{align*}
$$

  であり$\triangle ABC$ は正三角形である．
  よって題意は示された．$\cdots$(答)
  

  **【解説】**