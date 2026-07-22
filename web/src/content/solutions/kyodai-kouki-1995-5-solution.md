---
university: "kyodai"
category: "kouki"
year: "1995"
question: "5"
type: "solution"
title: "KYODAI 1995 kouki Q5 (solution)"
---

## 【解】

    (1)

    **$n=1$の時**

    

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1995/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $n=1$でBが引いた時，勝ちになるパターンはBが$1$を引くこと</figcaption>
</figure>

    

<figure id="fig_2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1995/5/fig_2.svg" alt="図 2" />
  <figcaption>図 2: $n=1$でBが引いた時，勝ちにならないパターンはBが$0$を引くこと．
            この時，次にAがBから引くので状況は対称的になる．</figcaption>
</figure>

    まず$n=1$の時，最初Aは$0,1$を，Bは$1$を持っている．
    最初にBが$1$を引いた場合はBの勝ちである．これは確率$1/2$である．
    一方最初にBが$0$を引いた場合，AとBを入れ替えて最初の状況に戻る．
    従って，
    

$$
\begin{align*}
& p_1 = \frac{1}{2}q_1             \\& q_1 = \frac{1}{2}+\frac{1}{2}p_1
\end{align*}
$$

    が成立する．これを解いて
    

$$
\begin{align*}
\begin{dcases}
            p_1 = \frac{1}{3} \\
            q_1 = \frac{2}{3}
        \end{dcases}
\end{align*}
$$

    が求める答えである．$\cdots$(答)

    
    **$n=2$の時**

    

<figure id="fig_3">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1995/5/fig_3.svg" alt="図 3" />
  <figcaption>図 3: $n=2$でBが引いた時，勝ちになるパターンはBが$1$または$2$を引くこと</figcaption>
</figure>

    

<figure id="fig_4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1995/5/fig_4.svg" alt="図 4" />
  <figcaption>図 4: $n=2$でBが$0$を引いた時，AとBが入れ替わって最初の状態に戻る．</figcaption>
</figure>

    $n=2$の時，まずBが$0$を確率$1/3$でひくと，AとBが入れ替わった状態で最初の状況に戻る．
    次にBが$1$か$2$を確率$2/3$で引くと，Bがカード$1$枚，Aがカード$2$枚になり，次のターンでAがBのカードを引いて，Bの勝ちとなる．
    従って，
    

$$
\begin{align*}
& \begin{dcases}
               p_2 = \frac{1}{3} q_2 \\
               q_2 = \frac{2}{3} + \frac{1}{3} p_2
           \end{dcases}\\\therefore& \begin{dcases}
               p_2 = \frac{1}{4} \\
               q_2 = \frac{3}{4}
           \end{dcases}
\end{align*}
$$

    となる．$\cdots$(答)

    
    (2)
    $n \geq 3$の時, ゲームの進行は下図のようになる.

    

<figure id="1995-5:fig:4">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1995/5/fig_5.svg" alt="図 5" />
  <figcaption>図 5: 最初にBが$0$を引いた場合，AとBを入れ替えて最初の状況に戻る</figcaption>
</figure>

    

<figure id="1995-5:fig:5">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1995/5/fig_6.svg" alt="図 6" />
  <figcaption>図 6: 最初にBが$0$以外を引いた場合，Bは一枚カードを捨てられる．
            次のAのターンでも確実にAがカードを捨て，Aが$n-2$枚，Bが$n-1$枚のカードを持った状態になる．</figcaption>
</figure>

    すなわち，Bが確率$1/(n+1)$で$0$をひくと，AとBが入れ替わってゲームの開始時点に戻る．
    Bが確率$n/(n+1)$で他のカードを引くとBはそのカードを捨てられる．次のターンでAも確実にカードを1枚捨てられ，
    その時Aが$n-1$枚，Bが$n-2$枚カードを持った状態である．

    したがって漸化式は
    

$$
\begin{align}
\begin{dcases}
            p_n = \frac{1}{n+1} p_n + \frac{n}{n+1} p_{n-2} \\
            q_n = \frac{1}{n+1} p_n + \frac{n}{n+1} q_{n-2}
        \end{dcases}\label{1995-5:eq:1}
\end{align}
$$

    となる．

    まず, 「$p_n+q_n=1$」を数学的帰納法で示す．
    $n=1,2$では(1)から成立するので，$n=k, k+1 (k \in \mathbb{N})$での成立を仮定すると
    [(式1)](#1995-5:eq:1)で$n=k+2$として両辺足し算すると
    

$$
\begin{align*}
p_{k+2} + q_{k+2}& = \frac{p_{k+1}+q_{k+1}}{n+1} + \frac{n(p_{n}+q_{n})}{n+1}\\& = \frac{1}{n+1} + \frac{n}{n+1}\\& = 1
\end{align*}
$$

    だから$n=k+2$でも成立する．
    以上から数学的帰納法により，全ての自然数$n$について$p_n+q_n=1$であることが示された．

    従って，[(式1)](#1995-5:eq:1)の一式目から$q_n$を消去すると
    

$$
\begin{align*}
& p_n - \frac{1}{n+1}(1-p_n) = \frac{n}{n+1}p_{n-2}\\& (n+2)p_n - n p_{n-2} = 1
\end{align*}
$$

    という漸化式を得る．よって題意は示された．$\cdots$(答)

    
    (3)
    新しく
    

$$
\begin{align}
r_n = (n+2)p_n  \label{1995-5:eq:2}
\end{align}
$$

    とおいて(2)の漸化式に代入すると
    

$$
\begin{align*}
r_{n+2} = r_{n}+1
\end{align*}
$$

    である．
    初期条件は(1)より
    

$$
\begin{align*}
& r_1 = 3 p_1 = 1 \\& r_2 = 4 p_2 = 1
\end{align*}
$$

    となるから，漸化式を解いて
    

$$
\begin{align*}
r_{2k}& = k \\
        r_{2k-1}& = k
\end{align*}
$$

    である．
    [(式2)](#1995-5:eq:2)より，
    

$$
\begin{align*}
p_{2k}& = \frac{k}{2k+2}\\
        p_{2k+1}& = \frac{k}{2k+1}
\end{align*}
$$

    となる．これを書き直して
    

$$
\begin{align*}
p_n =
        \begin{dcases}
            \frac{n}{2(n+2)}   & (n \text{ even}) \\
            \frac{n-1}{2(n+1)} & (n \text{ odd})
        \end{dcases}
\end{align*}
$$

    が求める一般項である．$\cdots$(答)

    
    

## 【解説】