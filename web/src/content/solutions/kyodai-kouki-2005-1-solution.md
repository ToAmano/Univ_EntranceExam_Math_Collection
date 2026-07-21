---
university: "kyodai"
category: "kouki"
year: "2005"
question: "1"
type: "solution"
title: "KYODAI 2005 kouki Q1 (solution)"
---

## 【解】

    $f(x)=x^3$とおくと，$f'(x)=3x^2$より，$x=t$ ($t>0$)における$C$の接線 $l$および法線 $m$ の方程式は
    
$$
\begin{align*}
\begin{dcases}
            l: & y = 3t^2 x - 2t^3              \\
            m: & y = -\frac{1}{3t^2}(x-t) + t^3
        \end{dcases}
\end{align*}
$$

    で与えられる．

    従って，$l$と$x$軸の交点$Q$の座標は
    
$$
\begin{align*}
Q\left(\frac{2}{3}t, 0\right)
\end{align*}
$$

    であり，$m$と$y$軸の交点$R$の座標は
    
$$
\begin{align*}
R\left(0, t^3+\frac{1}{3t}\right)
\end{align*}
$$

    である．

    以下，
    
$$
\begin{align*}
g(x)=\frac{QR}{OQ}
\end{align*}
$$

    と置いてその最小値を求める．$t>0$だから，$g(t)$は
    
$$
\begin{align*}
g(t)
         & = \frac{t^3+\frac{1}{3t}}{\frac{2}{3}t}\\& = \frac{3t^4+1}{2t^2}
\end{align*}
$$

    で与えられる．$t^2>0$より相加相乗平均の関係から
    
$$
\begin{align*}
g(t)
         & = frac{1}{2}\left(3t^2+\frac{1}{t^2}\right)\\& \ge\frac{1}{2}\cdot 2\sqrt{3t^2 \cdot \frac{1}{t^2}}\\& = \sqrt{3}
\end{align*}
$$

    と下から評価できる．
    等号成立は $3t^2 = \frac{1}{t^2}$ つまり $t = \frac{1}{\sqrt[4]{3}}$ の時である．
    以上から，求める最小値は
    
$$
\begin{align*}
g\left(\frac{1}{\sqrt[4]{3}}\right) = \sqrt{3}
\end{align*}
$$

    である．$\cdots$(答)

    

## 【解説】