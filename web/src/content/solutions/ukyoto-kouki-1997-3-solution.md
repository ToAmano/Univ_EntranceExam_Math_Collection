---
university: "ukyoto"
category: "kouki"
year: "1997"
question: "3"
type: "solution"
title: "UKYOTO 1997 kouki Q3 (solution)"
---

## 【解】

  点 X の位置ベクトル (O 始点) を $\vec{x}$ と表すと，与式は
  

$$
\begin{align}
\vec{a} + \vec{b} + \vec{c} + \vec{d} = 0 \label{1997-3:eq:1}
\end{align}
$$

  である．また，各点が球面上にあるから
  

$$
\begin{align}
|\vec{a}|=|\vec{b}|=|\vec{c}|=|\vec{d}|= 1 \label{1997-3:eq:2}
\end{align}
$$

  である．

  

<figure id="1997-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1997/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 球面上に点ABCDが配置されている様子</figcaption>
</figure>

  (1)
  [(式1)](#1997-3:eq:1)から
  

$$
\begin{align*}
\vec{a} + \vec{b} = -(\vec{c} + \vec{d})
\end{align*}
$$

  だから，両辺2乗して, [(式2)](#1997-3:eq:2)を用いて
  

$$
\begin{align}
\vec{a}\cdot\vec{b} = \vec{c}\cdot\vec{d}\label{1997-3:eq:3}
\end{align}
$$

  となる．

  ここで，
  

$$
\begin{align*}
|\vec{a} - \vec{b}|^2
     & = |\vec{a}|^2 - 2\vec{a}\cdot\vec{b} + |\vec{b}|^2 \\& = 2 - 2\vec{a}\cdot\vec{b}\\
    |\vec{c} - \vec{d}|^2
     & =|\vec{c}|^2 - 2\vec{c}\cdot\vec{d} + |\vec{d}|^2  \\& = 2 - 2\vec{c}\cdot\vec{d}
\end{align*}
$$

  だから，[(式3)](#1997-3:eq:3)よりこれらは等しく，
  

$$
\begin{align*}
& |\vec{a} - \vec{b}|^2 = |\vec{c} - \vec{d}|^2               \\\therefore& |\vec{a} - \vec{b}| = |\vec{c} - \vec{d}|                   \\& |\overrightarrow{\text{AB}}| = |\overrightarrow{\text{CD}}|
\end{align*}
$$

  となる．よって題意は示された．  $\cdots$(答)

  
  （2）
  AB'CD'が長方形をなすことを示すには，
  対角線ACとB'D'の長さが等しく，またその中点で交わることを示せばよい．

  

<figure id="1997-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1997/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 点A,B',C,D'の様子</figcaption>
</figure>

  まずは対角線の長さACとB'D'を考える．
  題意より，$\vec{b}' = -\vec{b}, \vec{d}' = -\vec{d}$ である.
  [(式1)](#1997-3:eq:1)に代入して
  

$$
\begin{align}
\vec{a} + \vec{c} = \vec{b}'+\vec{d}' \label{1997-3:eq:4}
\end{align}
$$

  だから，
  (1) と同様に両辺二乗して[(式2)](#1997-3:eq:2)より
  

$$
\begin{align*}
\vec{a}\cdot\vec{c} = \vec{b}' \cdot\vec{d}'
\end{align*}
$$

  であり，(1)と同様に
  

$$
\begin{align*}
|\overrightarrow{\text{AC}}| = |\overrightarrow{\text{B'D'}}|
\end{align*}
$$

  となる．従って対角線の長さは等しい．

  次に，対角線ACとB'D'の交点がこれらの線分の中点であることを示す．
  [(式4)](#1997-3:eq:4)より
  

$$
\begin{align*}
\vec{p} = \frac{\vec{a} + \vec{c}}{2} = \frac{\vec{b}'+\vec{d}'}{2}
\end{align*}
$$

  だから，ベクトル$\vec{p}$の表す点Pは線分AC，B'D'の中点である．
  従って点Pがこれらの交点かつ中点になっている．

  以上および，AB'CD'が互いに異なる点であることから，
  四角形 AB'CD' は長方形をなす．$\cdots$(答)

  
  

## 【解説】