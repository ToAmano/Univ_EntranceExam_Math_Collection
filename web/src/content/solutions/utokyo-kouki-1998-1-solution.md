---
university: "utokyo"
category: "kouki"
year: "1998"
question: "1"
type: "solution"
title: "UTOKYO 1998 kouki Q1 (solution)"
---

## 【解】

    (1)
    $C_1,C_2$の方程式は
    

$$
\begin{align*}
\begin{dcases}
            C_1 : x^2 + (y-10)^2=1 \\
            C_2 : x^2 + y^2 = 4
        \end{dcases}
\end{align*}
$$

    で与えられる．

    点 Q が円 $C_1$ 上を動き, 点 R が円 $C_2$ 上を動くとき，$0 \le \alpha, \beta < 2\pi$ をみたす $\alpha, \beta$ によって，
    $Q(\cos\alpha, 10+\sin\alpha)$, $R(2\cos\beta, 2\sin\beta)$ と書ける．
    この時$S(X, Y)$ とおいて，$S$の軌跡を求める．
    まず，
    

$$
\begin{align}
\overrightarrow{RQ}& = \begin{pmatrix} \cos\alpha - 2\cos\beta \\ \sin\alpha +10 - 2\sin\beta \end{pmatrix}\label{1998-1:eq:2}\\\overrightarrow{RS}& = \begin{pmatrix} X-2\cos\beta \\ Y-2\sin\beta \end{pmatrix}\label{1998-1:eq:3}
\end{align}
$$

    と書ける．

    三角形QRSが二等辺三角形になる条件より，
    

$$
\begin{align*}
\begin{dcases}
            RQ \cdot RS = 0 \\
            |QR|^2 = |RS|^2
        \end{dcases}
\end{align*}
$$

    であるが，[(式2)](#1998-1:eq:2)より
    

$$
\begin{align*}
\overrightarrow{RS} = \pm\begin{pmatrix} \sin\alpha - 2\sin\beta + 10 \\ -(\cos\alpha - 2\cos\beta) \end{pmatrix}
\end{align*}
$$

    が従う．

    [(式3)](#1998-1:eq:3)と比較して
    

$$
\begin{align*}
\begin{pmatrix} X \\ Y \end{pmatrix}& = 2\begin{pmatrix} \cos\beta \\ \sin\beta \end{pmatrix}\pm\begin{pmatrix} \sin\alpha - 2\sin\beta + 10 \\ -\cos\alpha + 2\cos\beta \end{pmatrix}\\& = \pm\begin{pmatrix} \sin\alpha \\ -\cos\alpha \end{pmatrix} + 2\begin{pmatrix} \cos\beta \mp \sin\beta \\ \sin\beta \pm \cos\beta \end{pmatrix}\pm\begin{pmatrix} 10 \\ 0 \end{pmatrix}\\& = \pm\begin{pmatrix} \sin\alpha \\ -\cos\alpha \end{pmatrix} + 2\sqrt{2}\begin{pmatrix} \cos(\beta \pm \pi/4) \\ \sin(\beta \pm \pi/4) \end{pmatrix}\pm\begin{pmatrix} 10 \\ 0 \end{pmatrix}
\end{align*}
$$

    を得る．ただし複合同順である．

    複合正の時，$(X, Y)$はドーナツ型の領域
    

$$
\begin{align*}
(2\sqrt{2}-1)^2 \le(x-10)^2+y^2 \le(1+2\sqrt{2})^2
\end{align*}
$$

    の内部を動く．

    複合負の時，$(X, Y)$はドーナツ型の領域
    

$$
\begin{align*}
(2\sqrt{2}-1)^2 \le(x+10)^2+y^2 \le(1-2\sqrt{2})^2
\end{align*}
$$

    の内部を動く．

    以上二つの領域をまとめると
    

$$
\begin{align}
\begin{dcases}
            (2\sqrt{2}-1)^2 \le (x-10)^2+y^2 \le (1+2\sqrt{2})^2 \\
            (2\sqrt{2}-1)^2 \le (x+10)^2+y^2 \le (1-2\sqrt{2})^2
        \end{dcases}\label{1998-1:eq:5}
\end{align}
$$

    であり，図示して[図1](#1998-1:fig:1)の斜線部分(境界線含む)となる．
    $\cdots$(答)

    

<figure id="1998-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1998/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $S$の存在領域は斜線部境界を含む．</figcaption>
</figure>

    
    (2)
    (1)の領域の境界の円の方程式は複合任意で
    

$$
\begin{align}
(X \pm 10)^2+Y^2 = (2\sqrt{2}\pm 1)^2 \label{1998-1:eq:4}
\end{align}
$$

    の合計四つである．

    $Q, R$ が一意に定まる，つまり $\alpha, \beta$ が一意に定まるような $C_3$ の軌跡は，
    (1)の領域の境界[(式4)](#1998-1:eq:4)である．

    したがって，[(式5)](#1998-1:eq:5)の領域と円 $C_3$ がただ1つ共有点を持つ（この時の共有点は[(式4)](#1998-1:eq:4)上になる）ように円の中心 $P_3$ を定めればよい．

    ここで[(式4)](#1998-1:eq:4)の四つの円のうち，中心を$(-10,0)$とする二つの円
    

$$
\begin{align*}
(X+10)^2+Y^2 = (2\sqrt{2}\pm 1)^2
\end{align*}
$$

    について，題意の直線
    

$$
\begin{align*}
\ell: x+2y=10
\end{align*}
$$

    との距離は点と直線の距離公式より
    

$$
\begin{align*}
L = \frac{|-10+10|}{\sqrt{1^2+2^2}}=4\sqrt{5}
\end{align*}
$$

    であり，これは$C_3$とこれらの円の半径の合計
    

$$
\begin{align*}
\left(2\sqrt{2}\pm 1\right) + \sqrt{2} = 3\sqrt{2}\pm 1
\end{align*}
$$

    よりも大きいから，これらの円と$C_3$が交点を持つことはない．

    従って，残りの$E(10,0)$を中心とする二つの円
    

$$
\begin{align*}
\begin{dcases}
            C_{+} : (X-10)^2+Y^2=(2\sqrt{2}+1)^2 \\
            C_{-} : (X-10)^2+Y^2=(2\sqrt{2}-1)^2
        \end{dcases}
\end{align*}
$$

    について考える．$\ell$は点Eを通る直線だから，この二つの円は[図2](#1998-1:fig:2)のように直線$\ell$と合計$4$つの交点を持つ．
    これらを$x$座標の小さい順にA，B，C，Dとおく．

    

<figure id="1998-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/utokyo/kouki/1998/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 直線$l$と円$C_{\pm}$の様子．</figcaption>
</figure>

    $\ell$上の点$P_3$を中心とする円$C_3$が$C_{\pm}$と唯一交点を持つのは
    

\begin{enumerate}
\item 点BまたはCで$C_3$と$C_{-}$が内接する \\
        \item 点AまたはDで$C_3$と$C_{+}$が外接する
\end{enumerate}

    二つのパターンである．

    **$B$ 又は $C$ で $C_3, C_5$ が内接する時**

    $\overline{BC}=2(\sqrt{2}-1) > 2$ だから，この時，他の交点は存在せず条件に適する．
    よって，$B, C$ からの距離が $\sqrt{2}$ ，すなわちEからの距離が
    

$$
\begin{align*}
\left(2\sqrt{2}-1\right) - \sqrt{2} = \sqrt{2}-1
\end{align*}
$$

    となるような $\ell$ 上の点が$P_3$であり，
    

$$
\begin{align*}
\overrightarrow{EP_3}& = (\sqrt{2}-1)\frac{\pm}{\sqrt{5}}\begin{pmatrix} 2 \\ -1 \end{pmatrix}\\\overrightarrow{OP_3}& = \begin{pmatrix} 10 \\ 0 \end{pmatrix} + (\sqrt{2}-1)\frac{\pm}{\sqrt{5}}\begin{pmatrix} 2 \\ -1 \end{pmatrix}\\
\end{align*}
$$

    だから，求める$P_3$は
    

$$
\begin{align*}
P_3\left(10\pm\frac{2\sqrt{5}(\sqrt{2}-1)}{5}, \mp\frac{\sqrt{5}(\sqrt{2}-1)}{5}\right)
\end{align*}
$$

    である（複合同順）．

    
    **$A$ 又は $D$ で $C_3, C_4$ が外接する時**

    この時，他の交点は存在せず条件に適する．
    よって，$A, D$ からの距離が $\sqrt{2}$ ，すなわちEからの距離が
    

$$
\begin{align*}
\left(2\sqrt{2}+1\right) + \sqrt{2} = 3\sqrt{2}+1
\end{align*}
$$

    となるような $\ell$ 上の点が$P_3$であり，
    

$$
\begin{align*}
\overrightarrow{EP_3}& = (3\sqrt{2}+1)\frac{\pm}{\sqrt{5}}\begin{pmatrix} 2 \\ -1 \end{pmatrix}\\\overrightarrow{OP_3}& = \begin{pmatrix} 10 \\ 0 \end{pmatrix} + (3\sqrt{2}+1)\frac{\pm}{\sqrt{5}}\begin{pmatrix} 2 \\  -1 \end{pmatrix}
\end{align*}
$$

    より
    

$$
\begin{align*}
P_3\left(10\pm\frac{2\sqrt{5}(3\sqrt{2}+1)}{5}, \mp\frac{\sqrt{5}(3\sqrt{2}+1)}{5}\right)
\end{align*}
$$

    となる（複合同順）．

    
    以上で全ての場合が尽くされ，求める点は複号同順として
    

$$
\begin{align*}
& P_3\left(10\pm\frac{2\sqrt{5}(\sqrt{2}-1)}{5}, \mp\frac{\sqrt{5}(\sqrt{2}-1)}{5}\right)\\& P_3\left(10\pm\frac{2\sqrt{5}(3\sqrt{2}+1)}{5}, \mp\frac{\sqrt{5}(3\sqrt{2}+1)}{5}\right)
\end{align*}
$$

    の四つである．$\cdots$(答)

    

    

## 【解説】