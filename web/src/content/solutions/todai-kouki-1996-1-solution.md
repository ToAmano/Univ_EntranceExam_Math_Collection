---
university: "todai"
category: "kouki"
year: "1996"
question: "1"
type: "solution"
title: "TODAI 1996 kouki Q1 (solution)"
---

## 【解】

    (1)
    1つの玉がどの箱に入るか考えて $3^n$ 通りである．$\cdots$(答)

    
    (2)
    $n$個のボールと, $2$本のしきりのならべ方を考えて
    

$$
\begin{align*}
_{n+2}\mathrm{C}_2 = \frac{1}{2}(n+2)(n+1)
\end{align*}
$$

    通りである．$\cdots$(答)

    
    (3)
    以下のように場合分けして考える．

    **$1^\circ$ 1つの箱にしか玉が入らない** \\
    この場合は$1$通りである．

    
    **$2^\circ$ それ以外の場合** \\
    全ての箱を区別すると，$1^{\circ}$の場合を除いて $3^n-3$ 通りである．
    従って，箱の区別をなくすと，$3!$で割れば
    

$$
\begin{align*}
\frac{3^n-3}{3!} = \frac{3^n-1}{2}
\end{align*}
$$

    通りである．

    
    以上二つの場合で全てが尽くされ，求める場合の数は
    

$$
\begin{align*}
1 + \frac{3^{n-1}-1}{2} = \frac{3^{n-1}+1}{2}
\end{align*}
$$

    通りである．$\cdots$(答)

    
    (4)
    3つの箱の内の玉の数を $X, Y, Z$ とおくと，題意より
    

$$
\begin{align}
X+Y+Z=6m \label{1996-1:eq:1}
\end{align}
$$

    である．対称性から
    

$$
\begin{align*}
X \ge Y \ge Z
\end{align*}
$$

    として良い．
    ここで
    

$$
\begin{align*}
\begin{dcases}
            1^{\circ}\, X=Y=Z \text{をみたす}                   & \alpha \text{通り} \\
            2^{\circ}\, X=Y>Z \text{ or } X>Y=Z \text{をみたす} & \beta \text{通り}  \\
            3^{\circ}\, X>Y>Z \text{をみたす}                   & \gamma \text{通り}
        \end{dcases}
\end{align*}
$$

    とおくと，箱の区別をした場合，$1^{\circ}$は一倍，$2^{\circ}$は三倍，$3^{\circ}$は六倍の場合の数があるから，
    (2)から
    

$$
\begin{align}
\alpha + 3\beta + 6\gamma = \frac{1}{2}(n+2)(n+1) \label{1996-1:eq:2}
\end{align}
$$

    である．

    さて，$1^{\circ}$の場合は明らかに一通りで
    

$$
\begin{align}
\alpha = 1 \label{1996-1:eq:3}
\end{align}
$$

    である．

    次に$\beta$は
    

$$
\begin{align*}
\begin{dcases}
            X=Y>Z: (6m,0,0), (6m-2,1,1), \dots, (2m+2,2m-1,2m-1) \\
            X>Y=Z: (3m,3m,0), (3m-1,3m-1,2), \dots, (2m+1,2m+1,2m-2)
        \end{dcases}
\end{align*}
$$

    の合計 $2m+m=3m$ 通りで
    

$$
\begin{align}
\beta = 3m \label{1996-1:eq:4}
\end{align}
$$

    従って，[(式4)](#1996-1:eq:3,1996-1:eq:4)を[(式2)](#1996-1:eq:2)に代入して
    

$$
\begin{align*}
& 1 + 9m + 6\gamma = \frac{1}{2}(n+2)(n+1)                           \\\therefore& \gamma = \frac{1}{6}\left[\frac{1}{2}(n+2)(n+1) - 1 - 9m \right]
\end{align*}
$$

    なので, もとめる場合の数は[(式4)](#1996-1:eq:3,1996-1:eq:4)と合わせて，
    

$$
\begin{align*}
\alpha+\beta+\gamma& = 1+3m+ \frac{1}{6}\left[\frac{1}{2}(n+2)(n+1) - 1 - 9m \right]\\& = \frac{1}{6}\left[\frac{1}{2}(n+2)(n+1) + 9m + 5 \right]\\
\end{align*}
$$

    である．ここで$n=6m$を代入して
    

$$
\begin{align*}
\alpha+\beta+\gamma& = \frac{1}{6}\left[\frac{1}{2}(n+2)(n+1) + \frac{3}{2}m + 5 \right]\\& = \frac{1}{12}\left(n^2+6n+12\right)
\end{align*}
$$

    通りである．$\cdots$(答)

    
    

## 【解説】