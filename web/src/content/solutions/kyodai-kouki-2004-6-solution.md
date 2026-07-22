---
university: "kyodai"
category: "kouki"
year: "2004"
question: "6"
type: "solution"
title: "KYODAI 2004 kouki Q6 (solution)"
---

## 【解】

  対称性から，題意をみた正方形のうち第一象限にあるものを$a(n)$として
  

$$
\begin{align}
N(n) = 4a(n) \label{2004-6:eq:1}
\end{align}
$$

  である．第一章限の様子を[図1](#2004-6:fig:1)に示す．
  

<figure id="2004-6:fig:1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2004/6/fig_1.svg" alt="図 1" />
  <figcaption>図 1: $n=5$の場合に第一象限に正方形を敷き詰めた様子．</figcaption>
</figure>

  また， $y = \sqrt{n^2-x^2}$ は $0 \leq x \leq n$ で単調減少だから
  

$$
\begin{align*}
a(n) = \sum_{k=1}^{n}\lfloor\sqrt{n^2-k^2}\rfloor
\end{align*}
$$

  である．ここで$\lfloor x\rfloor$はガウス記号であり，$x$以下の最大の整数を表す．
  ガウス記号の性質から
  

$$
\begin{align*}
\sqrt{n^2-k^2} - 1 < \lfloor\sqrt{n^2-k^2}\rfloor\leq\sqrt{n^2-k^2}
\end{align*}
$$

  である．$n>0$ だから両辺$n^2$で割ると
  

$$
\begin{align*}
\frac{1}{n}\sqrt{1-\left(\frac{k}{n}\right)^2} - \frac{1}{n^2} < \frac{1}{n^2}\lfloor\sqrt{n^2-k^2}\rfloor\leq\frac{1}{n}\sqrt{1-\left(\frac{k}{n}\right)^2}
\end{align*}
$$

  $k=1,2,\cdots, n$について和を取って
  

$$
\begin{align*}
& \sum_{k=1}^{n}\left(\frac{1}{n}\sqrt{1-\left(\frac{k}{n}\right)^2} - \frac{1}{n^2}\right) < \frac{a(n)}{n^2}\leq\sum_{k=1}^{n}\frac{1}{n}\sqrt{1-\left(\frac{k}{n}\right)^2}\\& \sum_{k=1}^{n}\frac{1}{n}\sqrt{1-\left(\frac{k}{n}\right)^2} - \frac{1}{n} < \frac{a(n)}{n^2}\leq\sum_{k=1}^{n}\frac{1}{n}\sqrt{1-\left(\frac{k}{n}\right)^2}
\end{align*}
$$

  ここで両辺の和の$n\to\infty$での極限値は区分求積法によって評価でき，
  

$$
\begin{align*}
\lim_{n \to \infty}\sum_{k=1}^{n}\frac{1}{n}\sqrt{1-\left(\frac{k}{n}\right)^2}& =\int_{0}^{1}\sqrt{1-x^2} dx \\& = \frac{\pi}{4}
\end{align*}
$$

  だから，はさみうちの定理より，$n \to \infty$ のとき
  

$$
\begin{align}
\lim_{n\to\infty}\frac{a(n)}{n^2}\to\frac{\pi}{4}\label{2004-6:eq:2}
\end{align}
$$

  [(式1)](#2004-6:eq:1)，[(式2)](#2004-6:eq:2)から
  

$$
\begin{align*}
\lim_{n\to\infty}\frac{N(n)}{n^2} = \pi
\end{align*}
$$

  が求める極限値である．$\cdots$(答)

  
  

## 【解説】

  解答が$\pi$になるのはもっともらしい．
  なぜならば，$n$を大きくしていくと敷き詰めた正方形の面積と円の面積はほぼ等しくなるため，
  正方形の面積の合計は$n^2\pi$に近づくはずである．従ってこれを$n^2$で割った極限値が$\pi$になる．
  これで，解答があっていそうだというのが直感的に理解できる．
  実際に問題を解いている際もこうした極端な場合を考えることで，答えを大はずししていないかわかるため
  極限を考える癖をつけておくと良いだろう．