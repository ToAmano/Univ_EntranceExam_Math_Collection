---
university: "todai"
category: "kouki"
year: "1990"
question: "3"
type: "solution"
title: "TODAI 1990 kouki Q3 (solution)"
---

## 【解】

  \newcommand{\drawTriangle}[3]{
    \draw (#1) -- (#2) -- (#3) -- cycle;
  }

  \newcommand{\recursiveTriangleQTwo}[4]{
    \ifnum#4=0
      \drawTriangle{#1}{#2}{#3};
    \else
      \path let
      \p1 = (#1), \p2 = (#2), \p3 = (#3)
      in
      coordinate (MAB2) at ($ (\p1)!0.5!(\p2) $)
      coordinate (MBC2) at ($ (\p2)!0.5!(\p3) $)
      coordinate (MCA2) at ($ (\p3)!0.5!(\p1) $);
      \drawTriangle{#1}{#2}{#3};
      \drawTriangle{MAB2}{MBC2}{MCA2};
    \fi
  }

  (1)

  

<figure id="1990-3:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1990/3/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 図形$Q_2$</figcaption>
</figure>

  まず$y_2$について，$C_2$を通る時，$A_2$ から $C_1(1) \to C_2 \to C_1(2)$ を経由して $B_2$ に行くルートだから，
  \begin{itemize}
    \item $A_2 \to C_1(1) \to C_2 \to C_1(2) \to B_2 $
    \item $A_2 \to C_1(1) \to C_2 \to C_1(2) \to B_1(1) \to B_2 $
    \item $A_2 \to B_1(1) \to C_1(1) \to C_2 \to C_1(2) \to B_2 $
  \end{itemize}
  の3通りである．よって$y_2 = 3$である．

  一方$x_2$について，$C_2$ を通らない時はパターンを列挙すると
  \begin{itemize}
    \item $B_1(1)$から$Q_1(2)$へ移動する場合
          \begin{itemize}
            \item $A_2 \to B_1(1) \to C_1(2) \to B_2 $
            \item $A_2 \to B_1(1) \to B_2 $
            \item $A_2 \to C_1(1) \to B_1(1) \to B_2 $
            \item $A_2 \to C_1(1) \to B_1(1) \to  C_1(2) \to B_2 $
          \end{itemize}
    \item $C_1(2)$から$Q_1(2)$へ移動する場合
          \begin{itemize}
            \item $A_2 \to B_1(1) \to C_1(1) \to C_1(2) \to B_2 $
            \item $A_2 \to C_1(1) \to C_1(2) \to B_2 $
            \item $A_2 \to C_1(1) \to C_1(2) \to B_1(1) \to B_2 $
          \end{itemize}
  \end{itemize}
  の合計$7$通りなので$x_2=7$である．

  以上まとめて
  

$$
\begin{align*}
\begin{dcases}
      x_2 = 7 \\
      y_2 = 3
    \end{dcases}
\end{align*}
$$

$\cdots$(答)

  
  (2)
  

<figure id="1990-3:fig:2">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/todai/kouki/1990/3/fig_2.svg" alt="図 2" />
  <figcaption>図 2: 図形$Q_{n+1}$</figcaption>
</figure>

  まず$x_{n+1}$ をもとめる．
  すなわち $C_n$ を通らない時はパターンを考える．
  これは以下のように場合分けできる．

  

1.  [$1^\circ$] $Q_n(1)$ を $B_n(1)$ から脱出する

2.  [$2^\circ$] $Q_n(1)$ を $C_n(1)$ から脱出する

  
  **$1^\circ$ の時**

  $Q_n(1)$ を出た後は $Q_n(2)$ 内を通って $B_{n+1}$ へ行く．
  よって$Q_n(1)$を脱出するのに$x_n+y_n$通り，さらに$Q_n(2)$を通るのに$x_n+y_n$通りで，合計
  

$$
\begin{align*}
(x_n+y_n)^2
\end{align*}
$$

  通りである．

  
  **$2^\circ$ の時**

  $Q_n(1)$ を出たあと，$Q_n(3)$を経由して $Q_n(2)$ 内を通って $B_{n+1}$ へ行く．
  この時，$Q_n(1)$ 内を通過中，$B_n(1)$ を通るか否かで場合分けして考える．

  \begin{itemize}
    \item[（ア）] $Q_n(1)$ 内を通過中に $B_n(1)$ を通る時．\\
          $C_n(2)$ を通過中，$B_n(1)$ を通ることができないことに注意すると，
          対称性から，$A_{n+1} \to C_n(1)$ が $y_n$ 通り，
          $C_n(1) \to C_n(2)$ が $x_n$ 通り，
          $C_n(2) \to B_{n+1}$ が $x_n$ 通りある．
          よってあわせて $y_n \cdot x_n^2$ 通りである．
    \item[（イ）] $Q_n(1)$ を通過中，$B_n(1)$ を通らない時．\\
          （ア）と同様に考えて $x_n \cdot x_n \cdot (x_n+y_n)$ 通りある．
  \end{itemize}

  以上から
  

$$
\begin{align*}
x_{n+1}& = (x_n+y_n)^2 + y_nx^2_n + x^2_n(x_n+y_n) \\& = (x_n+y_n)^2 + 2x_n^2y_n + x_n^3
\end{align*}
$$

  である．

  

  次に，$y_{n+1}$ をもとめる．
  これは $Q_n(1) \to Q_n(3) \to Q_n(2)$ と行く経路のみである．
  $x_{n+1}$ の時と同様に，$B_n(1)$を通るかどうかで場合分けして考える．
  $B_n(1)$を通る場合は$y_ny_nx_n$通り，通らない場合は$x_ny_n(x_n+y_n)$通りだから，
  

$$
\begin{align*}
y_{n+1}& = x_ny_n(x_n+y_n) + x_ny_n^2 \\& = 2x_n y_n^2 + x_n^2 y_n
\end{align*}
$$

  である．

  以上まとめて
  

$$
\begin{align*}
\begin{dcases}
      x_{n+1} = (x_n+y_n)^2 + 2x_n^2y_n + x_n^3
      y_{n+1} = 2x_n y_n^2 + x_n^2 y_n
    \end{dcases}
\end{align*}
$$

  である．$\cdots$(答)

  
  (3)
  (2)の漸化式で$n=2$として，(1)の結果を代入すれば
  

$$
\begin{align*}
x_3 & = 10^2 + 2 \cdot 49 \cdot 3 + 49 \cdot 7 = 737 \\
    y_3 & = 2 \cdot 7 \cdot 9 + 49 \cdot 3 = 273
\end{align*}
$$

  より
  

$$
\begin{align*}
\begin{dcases}
      x_3 = 737 \\
      y_3 = 273
    \end{dcases}
\end{align*}
$$

  である．

  $\cdots$(答)

  
  

## 【解説】