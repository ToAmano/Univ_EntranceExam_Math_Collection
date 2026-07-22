---
university: "todai"
category: "kouki"
year: "2006"
question: "1"
type: "solution"
title: "TODAI 2006 kouki Q1 (solution)"
---

## 【解】

    (1)
    題意の媒介変数表示を
    

$$
\begin{align}
\begin{dcases}
            x(t) = 2t+t^2 \\
            y(t) = t+2t^2
        \end{dcases}\label{2006-1:eq:1}
\end{align}
$$

    とおく．一回微分は
    

$$
\begin{align*}
x'(t) & = 2(1+t) \\
        y'(t) & = 4t+1
\end{align*}
$$

    だから，$t\neq 1$の時
    

$$
\begin{align*}
\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{4t+1}{2(1+t)}
\end{align*}
$$

    である．$\cdots$(答)

    
    (2)
    $t = -1$ の時は$x'(t)=0$より不適なので，以下$t \neq -1$として考える．
    （1）より，$dy/dx=-1/2$となる時，
    

$$
\begin{align*}
& \frac{dy}{dx} = \frac{4t+1}{2(1+t)} = -\frac{1}{2}\\\therefore& 4t+1 = -(1+t)                                      \\& t = -\frac{2}{5}
\end{align*}
$$

    である．[(式1)](#2006-1:eq:1)に代入して
    

$$
\begin{align*}
x\left(-\frac{2}{5}\right) = -\frac{16}{25}\\
        y\left(-\frac{2}{5}\right) = -\frac{2}{25}
\end{align*}
$$

    だから，求める座標は
    

$$
\begin{align*}
A\left(-\frac{16}{25}, -\frac{2}{25}\right)
\end{align*}
$$

    である．$\cdots$(答)

    
    (3)
    $X,Y$の表現に[(式1)](#2006-1:eq:1)を代入して
    

$$
\begin{align*}
X
         & = \frac{1}{\sqrt{5}}((4t+2t^2)-(t+2t^2)) \\& = \frac{3\sqrt{5}}{5}t                   \\
        Y
         & = \frac{1}{\sqrt{5}}((2t+t^2)+(2t+4t^2)) \\& = \frac{\sqrt{5}}{5}(5t^2+4t)
\end{align*}
$$

    を得る．第一式より$t = \sqrt{5}X/3$だから，第二式に代入して
    

$$
\begin{align*}
Y
         & = \frac{\sqrt{5}}{5}\left(5\frac{5}{9}X^2 + \frac{4\sqrt{5}}{3}X \right)\\& = \frac{5\sqrt{5}}{9}X^2 + \frac{4}{3}X
\end{align*}
$$

    という放物線である．$\cdots$(答)

    
    (4)
    (3) の変換を $f$ とおく．$\alpha$ を $0 < \alpha < \pi/2$ で $\tan\alpha = \frac{1}{2}$ をみたす角とおくと，
    

$$
\begin{align*}
\begin{dcases}
            \sin \alpha = \frac{1}{\sqrt{5}} \\
            \cos \alpha = \frac{2}{\sqrt{5}}
        \end{dcases}
\end{align*}
$$

    だから，$f$は
    

$$
\begin{align*}
X + iY = (\cos\alpha + i\sin\alpha)(x+iy)
\end{align*}
$$

    である．すなわち，$f$ は曲線 $C$ を原点中心に $\alpha$ だけ回転させる変換である．

    したがって(3) から， $C$ は放物線 $Y = f(X) = \frac{5\sqrt{5}}{9}X^2 + \frac{4}{3}X$ を原点中心に $-\alpha$ だけ回転させた曲線である．
    $C$ の頂点での接線の傾き$dy/dx$は $\tan(-\alpha) = -\tan\alpha = -\frac{1}{2}$ であり，放物線の異なる2点における接線は平行ではないこと及び (2) から，
    $C$ の頂点はAである．

    以下，グラフの概形のためにいくつか特徴のある点を求める．
    \begin{itemize}
        \item $x=0 \iff t=0, -2$ に対応する点は $(0,0)$, $(0,6)$．
        \item $y=0 \iff t=0, -\frac{1}{2}$ に対応する点は $(0,0)$, $(-\frac{3}{4},0)$．
        \item $\frac{dy}{dx}=0 \iff t = -\frac{1}{4}$ に対応する点は $(-\frac{7}{16}, -\frac{1}{8})$．
        \item $t=-1$ に対応する点は $(-1,1)$．
    \end{itemize}
    以上を踏まえて，$C$の概形は

    $\cdots$(答)

    

<figure id="2006-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2006/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 曲線$C$の概形．</figcaption>
</figure>

    

<figure id="2006-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/2006/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 曲線$C$の概形．頂点付近の拡大図．</figcaption>
</figure>

    

## 【解説】