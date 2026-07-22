---
university: "utokyo"
category: "kouki"
year: "2005"
question: "1"
type: "solution"
title: "UTOKYO 2005 kouki Q1 (solution)"
---

## 【解】

    (1)

    

<figure id="2005-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2005/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 三角形OPQと点ABの様子</figcaption>
</figure>

    線分$PQ$の長さの二乗は
    

$$
\begin{align*}
|PQ|^2
         & = (1-\cos\theta)^2 + \sin^2\theta\\& = 2(1-\cos\theta)                 \\& = 4\sin^2\frac{\theta}{2}
\end{align*}
$$

    である．
    $0 < \theta < \pi$ より $\sin^2(\theta/2) > 0$ だから，
    両辺ルートをとって
    

$$
\begin{align*}
|PQ| = 2\sin\frac{\theta}{2}
\end{align*}
$$

    である．
    ここで，$\angle PQO = \frac{\pi-\theta}{2}$だから，
    三角形$OPQ$および$ABQ$の面積は，$|PO|=1$より
    

$$
\begin{align*}
(\triangle OPQ)
         & = \frac{1}{2}|PQ||PO|\sin\frac{\pi-\theta}{2}\\& = \frac{1}{2} 2\sin\frac{\theta}{2}\sin\frac{\pi-\theta}{2}\\(\triangle ABQ)
         & = \frac{1}{2}|AQ||BQ|\sin\frac{\pi-\theta}{2}\\& = \frac{1}{2} ab \sin\frac{\pi-\theta}{2}
\end{align*}
$$

    である．題意の条件より$\triangle ABQ$の面積が$\triangle OPQ$の半分だから
    

$$
\begin{align*}
\frac{1}{2}\sin\frac{\theta}{2}\sin\frac{\pi-\theta}{2} =  \frac{1}{2} ab \sin\frac{\pi-\theta}{2}
\end{align*}
$$

    $0<\theta<\pi$より$\sin\frac{\pi-\theta}{2}\neq 0$だから
    

$$
\begin{align}
ab = \sin\frac{\theta}{2}\label{2005-1:eq:1}
\end{align}
$$

    である．よって題意は示された．$\cdots$(答)

    
    (2)
    $\angle PQO=\frac{\pi-\theta}{2}$だから，$\triangle ABQ$に余弦定理を用いて
    

$$
\begin{align*}
& |AB|^2 = |AQ|^2 + |BQ|^2 -2 |AQ||BQ|\cos\frac{\pi-\theta}{2}\\\therefore& |AB|^2 = a^2 + b^2 -2ab\sin\frac{\theta}{2}
\end{align*}
$$

    を得る．$\theta$を固定して$a,b$を動かしたときの$|AB|^2$の最小値が$f(\theta)$を与える．

    そこで，新しく$T=a+b$とおいて[(式1)](#2005-1:eq:1)を代入して
    

$$
\begin{align}
|AB|^2
         & = (a+b)^2 - 2ab -2ab\sin\frac{\theta}{2}\\& = T^2 -2\sin\frac{\theta}{2}\left(1+\sin\frac{\theta}{2}\right)\label{2005-1:eq:2}
\end{align}
$$

    である．

    以下，[(式1)](#2005-1:eq:1)のもとでの$T$の最小値を求めれば良い．
    まず，Aが線分PQ上にあり，Bが線分QOにあることから
    

$$
\begin{align*}
\begin{dcases}
            0 \le a \le 2\sin\frac{\theta}{2} \\
            0 \le b \le 1
        \end{dcases}
\end{align*}
$$

    を満たすことに注意すると，以下の二つの場合わけが必要になる．

    
    \textbf{$1^\circ \sqrt{\sin(\theta/2)} \le 2\sin(\theta/2) \iff \sin(\theta/2) \ge \frac{1}{4} \iff \overline{PQ} \ge \frac{1}{2}$ の時}

    

<figure id="2005-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2005/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $t=a+b$の存在範囲は，太線部分と直線$b=-a+t$との交点が存在するような$t$である．</figcaption>
</figure>

    $(a,b)$ の存在範囲は上図太線部 (境界含む)だから，
    

$$
\begin{align*}
(a,b)=(2\sin(\theta/2), \frac{1}{2})\text{の時 } t                 & =2\sin(\theta/2)+\frac{1}{2}\\(a,b)=(\frac{1}{2}, 2\sin(\theta/2))\text{の時 } t                 & =\frac{1}{2}+2\sin(\theta/2) \\(a,b)=(\sqrt{\sin(\theta/2)}, \sqrt{\sin(\theta/2)})\text{の時 } t & =2\sqrt{\sin(\theta/2)}
\end{align*}
$$

    であることに注意すると，$T=a+b$の下限は
    

$$
\begin{align*}
2\sqrt{\sin(\theta/2)}\le t
\end{align*}
$$

    だから，[(式2)](#2005-1:eq:2)から
    

$$
\begin{align*}
2\sin\left(\theta/2\right) - 2\sin^2\left(\theta/2\right)\le\overline{AB}^2
\end{align*}
$$

    であり，$f(\theta)$は
    

$$
\begin{align}
f(\theta) = 2\sin\left(\theta/2\right) - 2\sin^2\left(\theta/2\right)\label{2005-1:eq:3}
\end{align}
$$

    である．

    
    \textbf{$2^\circ 2\sin(\theta/2) \le \sqrt{\sin(\theta/2)} \iff \overline{PQ} le \frac{1}{2} \iff \sin(\theta/2) \le \frac{1}{4}$ の時}

    

<figure id="2005-1:fig:3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2005/1/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $t=a+b$の存在範囲は，太線部分と直線$b=-a+t$との交点が存在するような$t$である．</figcaption>
</figure>

    $(a,b)$ の存在範囲は上図太線部(境界含む)だから，
    $1^\circ$ と同様に考えて
    

$$
\begin{align*}
2\sin\left(\theta/2\right)+\frac{1}{2}\le t
\end{align*}
$$

    だから，[(式2)](#2005-1:eq:2)から
    

$$
\begin{align*}
2\sin^2\left(\theta/2\right)+\frac{1}{4}\le\overline{AB}^2
\end{align*}
$$

    であり，$f(\theta)$は
    

$$
\begin{align}
f(\theta) = 2\sin^2\left(\theta/2\right)+\frac{1}{4}\label{2005-1:eq:4}
\end{align}
$$

    である．

    
    以上\label{2005-1:eq:3,2005-1:eq:4}より
    

$$
\begin{align*}
\begin{dcases}
            \overline{PQ} \ge \frac{1}{2} \text{ の時 } f(\theta) = 2\sin\frac{\theta}{2} - 2\sin^2\frac{\theta}{2} \quad (\sin\frac{\theta}{2} \ge \frac{1}{4}) \quad (\equiv g(\theta)) \\
            \overline{PQ} < \frac{1}{2} \text{ の時 } f(\theta) = 2\sin^2\frac{\theta}{2} + \frac{1}{4} \quad (\sin\frac{\theta}{2} < \frac{1}{4}) \quad (\equiv h(\theta))
        \end{dcases}
\end{align*}
$$

    である．$\cdots$(答)

    
    (3)
    $y = g(\theta)$, $y = h(\theta)$ は全区間で微分可能だから，これら二つの関数の境界，
    である$0 < \alpha < \pi$ かつ $\sin(\alpha/2) = \frac{1}{4}$ をみたす $\alpha$ に対して
    $f(\theta)$ の微分可能性を示せば良い．
    そのためには微分係数の左右極限が一致することを示せば良い．
    実際に計算すると，
    

$$
\begin{align*}
\lim_{h \to +0}\frac{f(\alpha+h) - f(\alpha)}{h}& = g'(\alpha)                                               \\& = \cos\frac{\theta}{2}\left(1-2\sin\frac{\alpha}{2}\right)\\& = \frac{\sqrt{15}}{4}\left(1-\frac{1}{2}\right)\\& = \frac{\sqrt{15}}{8}\\\lim_{h \to +0}\frac{f(\alpha) - f(\alpha-h)}{-h}& = h'(\alpha)                                               \\& = 2\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}\\& = 2\frac{1}{4}\frac{\sqrt{15}}{4}\\& = \frac{\sqrt{15}}{8}
\end{align*}
$$

    より，左右極限が一致し，さらに $g(2\alpha) = h(2\alpha)$ であるから，微分可能である．$\cdots$(答)

    
    以下，$y=f(\theta)$のグラフの概形と最大値を求める．
    新しく
    

$$
\begin{align*}
t = \sin\frac{\theta}{2}
\end{align*}
$$

    とおくと，(2)から
    

$$
\begin{align*}
f(\theta) =
        \begin{dcases}
            2t - 2t^2          & \left(\frac{1}{2} \le t < 1\right) \\
            2t^2 + \frac{1}{4} & \left(0 < t \le \frac{1}{2}\right)
        \end{dcases}
\end{align*}
$$

    だから，$t$で微分すると
    

$$
\begin{align*}
\frac{df}{dt} =
        \begin{cases}
            2(1-2t) & \left(\frac{1}{4} \le t < 1\right) \\
            4t      & \left(0 < t \le \frac{1}{4}\right)
        \end{cases}
\end{align*}
$$

    だから，$f(\theta)$の増減表は[表1](#2005-1:table:1)となる．
    

<figure id="2005-1:table:1" class="table-wrapper">

| $\theta$ | $0$ |  | $\alpha$ |  | $\pi/3$ |  | $\pi$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| $P$ | $0$ |  | $\frac{1}{4}$ |  | $\frac{1}{2}$ |  | $1$ |
| $f'$ |  | $+$ | $+$ | $+$ | $0$ | $-$ |  |
| $f$ | $(1/4)$ | $\nearrow$ | $\nearrow$ | $\nearrow$ | $1/2$ | $\searrow$ | $(0)$ |

  <figcaption>表 1: $f(\theta)$の増減表</figcaption>
</figure>

    したがって，$y=f(\theta)$のグラフの概形は[図4](#2005-1:fig:4)で，
    最大値は
    

$$
\begin{align*}
f\left(\frac{\pi}{3}\right) = \frac{1}{2}
\end{align*}
$$

    である．$\cdots$(答)

    

<figure id="2005-1:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/2005/1/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $y=f(\theta)$のグラフ概形．</figcaption>
</figure>

    

## 【解説】

    **[別解](2)**

    (2)
    $B(1-b, 0)$ である．$\vec{QA} = \frac{a}{2S\sin\frac{\theta}{2}} \begin{pmatrix} \cos\theta - 1 \\ \sin\theta \end{pmatrix} = \frac{a}{2S\sin\frac{\theta}{2}} \begin{pmatrix} -2\sin^2\frac{\theta}{2} \\ 2\sin\frac{\theta}{2}\cos\frac{\theta}{2} \end{pmatrix} = a \begin{pmatrix} -S \\ C \end{pmatrix}$ から，
    $A(1-aS, aC)$ だから．
    $\quad \overline{AB}^2 = \{(1-aS)-(1-b)\}^2 + (aC)^2 = (b-aS)^2 + a^2C^2 = b^2 - 2abS + a^2S^2 + a^2C^2$
    $\quad = b^2 - 2abS + a^2(S^2+C^2) = a^2+b^2-2abS$
    となる．

    (2) の (1) 以外

    $b$ を消去する．$0 < a < 2S$, $0 < b < \dots$ から．$b=\frac{S}{a}$ より
    $$
        \begin{cases}
            \overline{AB}^2 = a^2 + \frac{S^2}{a^2} - 2S^2 \quad \text{...*} \\
            0 < S < 1
        \end{cases}
    $$
    から，$S, 0 < a < 2S \cdots$ のもとでの $\min$ を求めれば良い．
    $y = A + \frac{S^2}{A}$ のグラフは右図から $4S^2$ と $S$ の大小によって
    場合分け．

    \begin{tikzpicture}[scale=0.8]
        \draw[->] (0,0) -- (5,0) node[right] {$A$};
        \draw[->] (0,0) -- (0,5) node[above] {$y$};

        \draw[domain=0.5:4.5] plot(\x, {\x + 1/\x});

        \node at (1,0) {$S$};
        \node at (2.5,0) {$2S$};
        \node at (0,1) {$S^2$};
        \node at (0,2.5) {$2S$};

        \draw[dashed] (1,0) -- (1,2) node[above left] {$y=A+\frac{S^2}{A}$};
        \draw[dashed] (2.5,0) -- (2.5,4); 
        \draw[fill] (1,2) circle (1.5pt); 
        \draw[fill] (2.5, 4) circle (1.5pt); 
    \end{tikzpicture}

    
    $1^\circ \quad 4S^2 \ge S \quad : S \ge \frac{1}{4}$
    $f(\theta) = 2S-2S^2$ ($a=\sqrt{S}$ でmin)

    
    $2^\circ \quad 4S^2 < S \quad : S < \frac{1}{4}$
    $f(\theta) = (4S^2+\frac{1}{4}) - 2S^2 = 2S^2+\frac{1}{4}$ ($a=2S$ でmin)

    (以下略)