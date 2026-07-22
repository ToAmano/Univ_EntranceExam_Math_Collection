---
university: "ukyoto"
category: "kouki"
year: "1995"
question: "2"
type: "solution"
title: "UKYOTO 1995 kouki Q2 (solution)"
---

## 【解】

  題意の$\alpha_n$と同様の置き方をして，
  

$$
\begin{align*}
& \angle\text{B}_n \text{O}\text{C}_n = \beta_n  \\& \angle\text{C}_n \text{O}\text{A}_n = \gamma_n
\end{align*}
$$

  とする．この様子を[図1](#1995-2:fig:1)に示す．

  

<figure id="1995-2:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/ukyoto/kouki/1995/2/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 点$A_n,B_n,C_n$の様子</figcaption>
</figure>

  すると置き方からして
  

$$
\begin{align}
\alpha_n + \beta_n + \gamma_n & = 2\pi\label{1995-2:eq:1}
\end{align}
$$

  を満たす．

  また，題意より漸化式は以下のようになる．
  

$$
\begin{align}
\begin{dcases}
      \alpha_{n+1} = \frac{1}{2}(\alpha_n + \beta_n) \\
      \beta_{n+1} = \frac{1}{2}(\beta_n + \gamma_n)  \\
      \gamma_{n+1} = \frac{1}{2}(\alpha_n + \gamma_n)
    \end{dcases}\label{1995-2:eq:2}
\end{align}
$$

  (1)
  [(式1)](#1995-2:eq:2,1995-2:eq:1)より
  

$$
\begin{align*}
4\alpha_{n+1}& = 2(\alpha_n + \beta_n)                                                               \\& = 2\alpha_n + (\beta_{n-1} + \gamma_{n-1}) \quad(\because\text{[(式2)](#1995-2:eq:2)}) \\& = 2\alpha_n + 2\pi - \alpha_{n-1}\quad(\because\text{[(式1)](#1995-2:eq:1)})          \\
\end{align*}
$$

  であり，題意は示された．$\cdots$(答)

  
  (2)
  [(式1)](#1995-2:eq:2,1995-2:eq:1)を繰り返し用いて
  

$$
\begin{align*}
\alpha_{n+2}& = \frac{1}{2}(\alpha_{n+1} +\beta_{n+1})                 \\& = \frac{1}{2}(2\pi - \gamma_{n+1})                        \\& = \pi - \frac{1}{4}(\alpha_n + \gamma_n)                  \\& = \pi - \frac{1}{4}(2\pi - \beta_{n})                     \\& = \frac{1}{2}\pi + \frac{1}{8}(\beta_{n-1} +\gamma_{n-1}) \\& = \frac{1}{2}\pi + \frac{1}{8}(2\pi - \alpha_{n-1})       \\& = \frac{3}{4}\pi - \frac{1}{8}\alpha_{n-1}
\end{align*}
$$

  であり，題意は示された．$\cdots$(答)

  
  (3)
  (2)の漸化式でラベルを張り替えて
  

$$
\begin{align*}
& \alpha_{3(n+1)}                  = -\frac{1}{8}\alpha_{3n} + \frac{3}{4}\pi\\\therefore& \alpha_{3(n+1)} - \frac{2}{3}\pi = -\frac{1}{8}\left(\alpha_{3n} - \frac{2}{3}\pi\right)
\end{align*}
$$

  と書ける．
  等比数列の公式から
  

$$
\begin{align*}
\alpha_{3n} = \left(-\frac{1}{8}\right)^n \left(\alpha_0 - \frac{2}{3}\pi\right) + \frac{2}{3}\pi
\end{align*}
$$

  と書ける．$\cdots$(答)

  
  

## 【解説】