---
university: "titech"
category: "kouki"
year: "1997"
question: "1"
type: "solution"
title: "TITECH 1997 kouki Q1 (solution)"
---

## 【解】

  方針として，まず$C_2$の軌跡を求め，ついで面積$S_a$を求める．

  そこでまず$C_2$ の軌跡を求める．
  題意の直線の 2 端点 P$(\alpha,\alpha^2)$, Q$(\beta,\beta^2)$ ($\alpha < \beta$) とおく．
  この概形は[図1](#1997-1:fig:2)である．

  

<figure id="1997-1:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1997/1/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $C_1$の概形</figcaption>
</figure>

  $|PQ| > 0$, $|PQ|=1 \Longleftrightarrow |PQ|^2=1$ だから，
  

$$
\begin{align}
& (\beta-\alpha)^2+(\beta^2-\alpha^2)^2 = 1 \nonumber\\\therefore& (\beta-\alpha)^2\left[1 + (\alpha+\beta)^2\right] = 1 \label{1997-1:eq:1}
\end{align}
$$

  ここで，$p=\alpha+\beta$, $q=\beta-\alpha$ とおく．$\alpha,\beta \in\mathbb{R}$ および $\alpha < \beta$から
  

$$
\begin{align}
q >0    \label{1997-1:eq:2}
\end{align}
$$

  となる．題意の中点を$M(X,Y)$ とすると
  

$$
\begin{align}
X
     & = \frac{1}{2}(\alpha+\beta)                                 \\& =\frac{p}{2}\label{1997-1:eq:3}\\
    Y
     & = \frac{1}{2}\left(\alpha^2+\beta^2\right)\\& = \frac{1}{4}\left[(\alpha+\beta)^2+(\beta-\alpha)^2\right]\\& = \frac{1}{4}\left(p^2+q^2\right)\label{1997-1:eq:4}
\end{align}
$$

  となることに注意する．さらに，[(式1)](#1997-1:eq:1)を$p$ と $q$ で書くと
  

$$
\begin{align*}
& q^2(1+p^2)  = 1                                    \\\therefore& q^2 = \frac{1}{1+p^2}\quad(\because 1+p^2\neq 0)
\end{align*}
$$

  で，これは[(式2)](#1997-1:eq:2)を満たす．[(式4)](#1997-1:eq:3,1997-1:eq:4)に代入して$p$および$q$を消去して$X$, $Y$の関係を求めれば，それが求める軌跡である．
  [(式3)](#1997-1:eq:3)から$p=2X$だから，[(式4)](#1997-1:eq:4)から，
  

$$
\begin{align*}
Y
     & = \frac{1}{4}\left(p^2+1/(1+p^2)\right)\\& = \frac{1}{4}\left((2X)^2+1/(1+(2X)^2)\right)\\& = \frac{1}{4}\left(4X^2+1/(1+4X^2)\right)
\end{align*}
$$

  である，これが$C_2$の軌跡である．$X$はすべての実数を取る．

  以上より，求める面積$S_{a}$は[図2](#1997-1:fig:1)の斜線部である．

  

<figure id="1997-1:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/titech/kouki/1997/1/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $C_1$と$C_2$の概形</figcaption>
</figure>

  $C_1$と$C_2$が偶関数だから，$0\le x$の部分の面積の$2$倍が求める面積であり，
  

$$
\begin{align}
\frac{1}{2}S_a
     & = \int_0^a \left(x^2+\frac{1}{4(1+4x^2)} - x^2 \right)dx \nonumber\\& = \frac{1}{4}\int_{0}^{a}\frac{1}{1+4x^2} dx \label{1997-1:eq:5}
\end{align}
$$

  ここで，$x=\frac{1}{2}\tan\theta$ ($0 \le \theta < \pi/2$) とすると，$\frac{dx}{d\theta} = \frac{1}{2\cos^2\theta}$，又 $a = \frac{1}{2}\tan \alpha$ となる $\alpha$ があるので，
  [(式5)](#1997-1:eq:5)に代入して
  

$$
\begin{align}
\frac{1}{2}S_a
        & = \frac{1}{4}\int_{0}^{\alpha}\frac{1}{1+\tan^2\theta}\cdot\frac{1}{2\cos^2\theta} d\theta\nonumber\\& = \frac{1}{8}\int_{0}^{\alpha} d\theta\nonumber\\& = \frac{\alpha}{8}\nonumber\\\therefore
    S_a & = \frac{\alpha}{4}\label{1997-1:eq:6}
\end{align}
$$

  と面積が求まる．$a = \frac{1}{2}\tan \alpha$より，$a\to\infty$で$\alpha\to\pi/2$だから，[(式6)](#1997-1:eq:6)の極限は
  

$$
\begin{align*}
\lim_{a\to\infty} S_a = \frac{1}{4}\frac{\pi}{2} = \frac{\pi}{8}
\end{align*}
$$

  となる．$\cdots$(答)

  

## 【解説】

  かなり典型的な軌跡の問題である．
  軌跡さえもとまれば後半の積分部分はただの計算であるから，前半軌跡を求めるところまでがポイントである．

  軌跡を求める部分はわかりやすく対称式を利用することになる．
  式の形的に$(\alpha+\beta,\alpha\beta)$よりも，解答のように$(\alpha+\beta,\alpha-\beta)$とおいた方が計算は多少楽だろう．

  求めた軌跡
  

$$
\begin{align*}
y =  \frac{1}{4}\left(4x^2+1/(1+4x^2)\right)
\end{align*}
$$

  は$x\to\pm\infty$の極限で
  

$$
\begin{align*}
y = x^2
\end{align*}
$$

  に漸近し，かつ$x=0$で$y=\frac{1}{4}$になっており，最もらしい軌跡であるから一定検算できて安心だろう．

  後半の積分部分は
  

$$
\begin{align*}
\int_{0}^{a}\frac{1}{1+4x^2} dx
\end{align*}
$$

  という典型的な形の定積分であり，$2x=\tan\theta$の形の置換で解ける．
  この積分の一般的な形の原始関数は
  

$$
\begin{align*}
\int\frac{1}{x^2+a^2} dx = \frac{1}{a}\arctan\left(\frac{x}{a}\right)
\end{align*}
$$

  になることは受験生ならば覚えておきたい．