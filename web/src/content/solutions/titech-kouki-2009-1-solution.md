---
university: "titech"
category: "kouki"
year: "2009"
question: "1"
type: "solution"
title: "TITECH 2009 kouki Q1 (solution)"
---

## 【解】

  $P(X,Y,0)$, 球の中心$O' (0,0,1)$とする．
  球の様子は[図1](#2009-1:fig:1)のようになる．

  

<figure id="2009-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2009/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 球と点光源の様子</figcaption>
</figure>

  線分$CP$が球に遮られるためには，
  線分$CP$と球の中心$O'$の距離が球の半径である$1$より小さければ良い．
  直線$CP$はパラメータ表示で
  

$$
\begin{align*}
\begin{pmatrix}x   \\y\\ z\end{pmatrix}
    = \begin{pmatrix}a \\ 0 \\ 3\end{pmatrix} + t \begin{pmatrix}X-a \\ Y \\ -3\end{pmatrix}\quad(t \in\mathbb{R})
\end{align*}
$$

  だから、CP上の点$Q(t)$として、
  

$$
\begin{align*}
& |\vec{O'Q(t)}|^2                              \\
    = & \{ a+t(X-a) \}^2 + (tY)^2 + \{ 3-3t-1 \}^2    \\
    = & \{ a+t(X-a) \}^2 + (tY)^2 + (2-3t)^2          \\
    = & \{(X-a)^2+Y^2+9\}t^2 + 2\{a(X-a)-6\}t + a^2+4
\end{align*}
$$

  となる．ここで簡単のため
  

$$
\begin{align*}
A & =(X-a)^2+Y^2+9(>0) \\
    B & =aX-a^2-6
\end{align*}
$$

  とおいて，式変形を続けると
  

$$
\begin{align*}
|O'Q|^2= & A\left(t+\frac{B}{A}\right)+a^2+4-\frac{B^2}{A}
\end{align*}
$$

  だから，$t = - B/A$ の時最小値$a^2+4-B^2/A$をとる．
  よって条件は
  

$$
\begin{align*}
& \min |\vec{O'Q}|^2 \le 1                                    \\\Leftrightarrow& a^2+4 - \frac{\{a(X-a)-6\}^2}{(X-a)^2+Y^2+9}\le 1          \\\Leftrightarrow& a^2+3 - \frac{\{a(X-a)-6\}^2}{(X-a)^2+Y^2+9}\le 0          \\\Leftrightarrow& (a^2+3) \{(X-a)^2+Y^2+9\} - \{a(X-a)-6\}^2 \le 0            \\\Leftrightarrow& (a^2+3)(X-a)^2+(a^2+3)Y^2+9(a^2+3)                          \\& - \{a^2(X-a)^2-12a(X-a)+36\}\le 0                          \\\Leftrightarrow& 3(X-a)^2+(a^2+3)Y^2+12a(X-a)+9a^2-9 \le 0                   \\\Leftrightarrow& 3\left[(X-a)+2a\right]^2+(a^2+3)Y^2+12a(X-a)-3(a^2+3) \le 0 \\\Leftrightarrow& \frac{(X+a)^2}{a^2+3} + \frac{Y^2}{3}\le 1
\end{align*}
$$

  という楕円となり，これが求めるべき条件である．従って答えは
  

$$
\begin{align*}
\frac{(X+a)^2}{a^2+3} + \frac{Y^2}{3}\le 1
\end{align*}
$$

  である．$\cdots$(答)

  
  

## 【解説】

  空間図形の問題．球体が点光源に対して作る影の形をとう問題で，我々は日常的な経験からこれが楕円になることを知っている．
  それを数学的に確かめなさいという面白い問題である．
  答案を見ればわかるように少し式変形が煩雑なので，答えが楕円になるという想定を持って変形を進めることで見通しが良くなるだろう．

  $CP$と$O'$の距離が$1$以下となる条件を立式する際，
  解答では直線$CP$上の点と$O'$の距離の最小値が$1$以下となるように立式した．
  ほぼ同じだが別の方法として，点と直線の距離を直接求めに行く方法も紹介しよう．
  一定検算に利用できるだろう．
  $O'$から直線$CP$におろした垂線の足を$H$とする．

  

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/2009/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 直線$CP$と$O'$の距離．</figcaption>
</figure>

  $CH$はCO'のCPへの正射影ベクトルだから
  

$$
\begin{align*}
\vec{CH} = \frac{\vec{CP}\cdot\vec{CO'}}{|\vec{CP}|^2}\vec{CP}
\end{align*}
$$

  であるから，
  

$$
\begin{align*}
\vec{O'H}& = \vec{CH}-\vec{CO}\\& = \frac{\vec{CP}\cdot\vec{CO'}}{|\vec{CP}|^2}\vec{CP} - \vec{CO}
\end{align*}
$$

  となる．各ベクトルは
  

$$
\begin{align*}
\vec{CO'}& = \begin{pmatrix}-a  \\ 0 \\ -2\end{pmatrix}\\\vec{CP}& = \begin{pmatrix}X-a \\ Y \\ -3\end{pmatrix}
\end{align*}
$$

  だから，
  

$$
\begin{align*}
\vec{O'H}& = \frac{-a(X-a)+6}{(X-a)^2+Y^2+9}\begin{pmatrix}X-a \\ Y \\ -3\end{pmatrix} - \begin{pmatrix}-a  \\ 0 \\ -2\end{pmatrix} \\& = \frac{-B}{A}\begin{pmatrix}X-a                    \\ Y \\ -3\end{pmatrix} - \begin{pmatrix}-a  \\ 0 \\ -2\end{pmatrix}
\end{align*}
$$

  この長さが$1$よりも小さければ良いので，
  

$$
\begin{align*}
\left|\vec{O'H}\right|^2 \le 1
\end{align*}
$$

  が条件である．
  

$$
\begin{align*}
& \left|\vec{O'H}\right|^2                                                                          \\& = \left(\frac{-B}{A}(X-a)+a\right)^2+\left(\frac{-B}{A}Y\right)^2 + \left(\frac{3B}{A}+2\right)^2 \\& = \frac{1}{A^2}\left(-B(X-a)+aA\right)^2+\frac{B^2Y^2}{A^2} + \frac{1}{A^2}\left(3B+2A\right)^2   \\
\end{align*}
$$

  を得る．さらに整理すると
  

$$
\begin{align*}
\left|\vec{O'H}\right|^2
     & = \frac{B^2}{A^2}\left((X-a)^2+Y^2+9\right)\\& \quad\quad + \frac{-2aAB(X-a)}{A^2} + a^2 + 4 + \frac{12AB}{A^2}\\& = \frac{B^2}{A} + a^2 + 4 + \frac{-2B(a(X-a)-6)}{A}\\& = \frac{B^2}{A} + a^2 + 4 + \frac{-2B^2}{A}\\& = -\frac{B^2}{A} + a^2 + 4
\end{align*}
$$

  となり，解答の最小値と一致する．

  これでふた通りの方法でもとまった．
  導出を見ればわかるようにどちらも計算量には大差ないので，お好みで使い分けると良いだろう．