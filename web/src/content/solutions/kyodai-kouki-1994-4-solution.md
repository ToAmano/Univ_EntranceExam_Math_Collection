---
university: "kyodai"
category: "kouki"
year: "1994"
question: "4"
type: "solution"
title: "KYODAI 1994 kouki Q4 (solution)"
---

## 【解】

### (1)

  二回で勝敗が決まるのは，A又はBが2連勝する確率で，
  
$$
\begin{align*}
\frac{1}{2}(1-p) \cdot 2 = 1-p
\end{align*}
$$

  である．$\cdots$(答)

### (2)

  ちょうど4回で優勝者が決まるのは，2回目でCが勝ち，3回目でC以外が勝つ時である．
  このような確率は
  
$$
\begin{align*}
p(1-p)
\end{align*}
$$

  である．$\cdots$(答)

  

<figure id="1994-4:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/1994/4/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 丁度4回で優勝が決まる例．Cが2回目で勝ち，3回目で負ける場合である．</figcaption>
</figure>

### (3)

  A,B,Cのいずれかが必ず優勝するから，三者が優勝する確率が等しい時，その確率は$1/3$である．

  以下，Aの優勝する確率を $P_A$ として，
  
$$
\begin{align*}
P_A = \frac{1}{3}
\end{align*}
$$

  を満たすような$p$を求める．

  先に2勝した人の優勝なのでゲームは多くとも4回しか行われない．
  そこで何回ゲームが行われるかで場合分けして考える．

  
  \textbf{$1^{\circ}$ 2回}

### (1)
において，Aが優勝する確率とBが優勝する確率は半々である．
  従ってAが優勝する確率は(1)の半分の確率だから$\frac{1}{2}(1-p)$である．

  
  \textbf{$2^{\circ}$ 3回}

  対戦のやり方からして，Aが3回で優勝することはない．

  
  \textbf{$3^{\circ}$ 4回}

### (2)
において，Aが優勝する確率とBが優勝する確率は半々である．
  従って，Aが優勝する確率は(2)の半分の確率だから $\frac{1}{2} p(1-p)$である．

  

  以上から，Aの優勝する確率は
  
$$
\begin{align*}
P_A
     & = \frac{1}{2}(1-p) + \frac{1}{2} p(1-p) \\& = \frac{1}{2}(1+p)(1-p)
\end{align*}
$$

  である．これが$1/3$に等しいから
  
$$
\begin{align*}
& \frac{1}{2}(1+p)(1-p) = \frac{1}{3}\\\iff& p = \frac{\sqrt{3}}{3}\quad(\because p > 0 )
\end{align*}
$$

  が求める値である．$\cdots$(答)

  

## 【解説】