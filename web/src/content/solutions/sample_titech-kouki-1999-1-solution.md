---
university: "sample_titech"
category: "kouki"
year: "1999"
question: "1"
type: "solution"
title: "SAMPLE_TITECH 1999 kouki Q1 (solution)"
---

## 【解】

  $\displaystyle F_n = \int_0^{\frac{\pi}{2}} \frac{\sin^2 nx}{x^2} dx$ とおく．半角公式から，
  
$$
\begin{align}
F_n
     & = \int_0^{\frac{\pi}{2}}\frac{1-\cos 2nx}{2(1+x)} dx \nonumber\\& = \int_0^{\frac{\pi}{2}}\frac{1}{2(1+x)} dx - \int_0^{\frac{\pi}{2}}\frac{\cos 2nx}{2(1+x)} dx \label{1999-1:eq:1}
\end{align}
$$

  である．第一項は$n$に依存しない定数で，
  
$$
\begin{align}
\int_0^{\frac{\pi}{2}}\frac{1}{2(1+x)} dx
     & = \frac{1}{2}\left[\log(1+x)\right]_0^{\frac{\pi}{2}}\nonumber\\& = \frac{1}{2}\log\left(1+\frac{\pi}{2}\right)\label{1999-1:eq:2}
\end{align}
$$

  である．次に第二項は以下のように$n\to\infty$で$0$に収束することを示せる．
  部分積分法から，
  
$$
\begin{align}
\int_0^{\frac{\pi}{2}}\frac{\cos 2nx}{2(1+x)} dx
     & = \frac{1}{2n}\left[\frac{\sin 2nx}{2(1+x)}\right]_0^{\frac{\pi}{2}} + \frac{1}{2n}\int_0^{\frac{\pi}{2}}\frac{\sin 2nx}{2(1+x)^2} dx \nonumber\\& =  \frac{1}{2n}\int_0^{\frac{\pi}{2}}\frac{\sin 2nx}{2(1+x)^2} dx \label{1999-1:eq:3}
\end{align}
$$

  ここで$\eqref{1999-1:eq:3}$において，区間内で $1/(1+x)^2 \ge 0$および$\sin 2nx\le 1$だから，
  
$$
\begin{align*}
\left|\frac{1}{2n}\int_0^{\frac{\pi}{2}}\frac{\sin 2nx}{2(1+x)^2} dx \right|& \le\frac{1}{2n}\int_0^{\frac{\pi}{2}}\frac{1}{2(1+x)^2} dx \\& \xrightarrow{n \to \infty} 0
\end{align*}
$$

  となる．挟み撃ちの定理から極限値は
  
$$
\begin{align}
\frac{1}{2n}\int_0^{\frac{\pi}{2}}\frac{\sin 2nx}{2(1+x)^2} dx & \to 0 \label{1999-1:eq:4}
\end{align}
$$

  となり，したがって$\eqref{1999-1:eq:1,1999-1:eq:2,1999-1:eq:4}$から求める$F_n$の極限値は
  
$$
\begin{align*}
\lim_{n\to\infty} F_n = \frac{1}{2}\log\left(1+\frac{\pi}{2}\right)
\end{align*}
$$

  を得る．$\cdots$(答)

  
  

## 【解説】

  典型的な積分値の極限の問題．鍵となるのは$\sin nx$と三角関数の中に入った$n$をどのように評価するか．$n\to\infty$のときに$\sin nx$は激しく振動するが，うまいこと収束する部分を取り出して計算を進める必要がある．解答では$\sin^2 nx$を半角公式で展開した．$n$をを積分から取り出すてっとり早い方法は部分積分なので覚えておきたい．$\cos 2nx$のほうが$0$に収束することがかなりゆるい不等式評価でわかり，かなり簡単に答えが求まる問題となっている．

  さて，別解としてもうひとつ頻出の方法があるので紹介したい．それは積分区間を三角関数の関数の半周期で区切る方法である．すなわち
  
$$
\begin{align*}
A_k = \int_{\frac{k-1}{2n}\pi}^{\frac{k}{2n}\pi} f(x) \sin^2 nx \, dx
\end{align*}
$$

  とおく．ただし$f(x)=1/(1+x)$である．このようにおくメリットは三角関数の周期性を利用した変形が行えることと，（今回は$\sin^2$なので関係ないが）この積分区間内で三角関数の符号が一定であるため評価しやすい点である．

  この積分区間$\left[ \frac{k-1}{2n}\pi, \frac{k}{2n}\pi \right]$ で $f(x)$ の max min を与える$x$ を各々 $M_k, m_k$ とする．
  今回は$f(x)$は単調減少なのでなのでわざわざ置く必要もないが，一般性を保って議論を進めよう．
  $\sin^2 nx \ge 0$ からこの区間では
  
$$
\begin{align*}
f(m_k) \sin^2 nx \le f(x) \sin^2 nx \le f(M_k) \sin^2 nx
\end{align*}
$$

  であり，両辺積分して
  
$$
\begin{align}
\int_{\frac{k-1}{2n}\pi}^{\frac{k}{2n}\pi} f(m_k) \sin^2 nx \, dx
    \le A_k
    \le\int_{\frac{k-1}{2n}\pi}^{\frac{k}{2n}\pi} f(M_k) \sin^2 nx \, dx \label{1999-1:eq:5}
\end{align}
$$

  を得る．両辺の積分は簡単に評価できて
  
$$
\begin{align*}
\int_{\frac{k-1}{2n}\pi}^{\frac{k}{2n}\pi}\sin^2 nx \, dx
     & = \left[\frac{1}{2}x - \frac{1}{4n}\sin 2nx \right]_{\frac{k-1}{2n}\pi}^{\frac{k}{2n}\pi}\\& = \frac{1}{2}\cdot\frac{\pi}{2n}\\& = \frac{\pi}{4n}
\end{align*}
$$

  だから $\eqref{1999-1:eq:5}$ に代入して
  
$$
\begin{align*}
\frac{\pi}{4n} f(m_k) \le A_k \le\frac{\pi}{4n} f(M_k)
\end{align*}
$$

  だから，もとの$F_n$を求めるために$k=0,1,\cdots,n$ について和をとって，
  
$$
\begin{align}
\frac{\pi}{4n}\sum_{k=1}^{n} f(m_k)
    \le F_n
    \le\frac{\pi}{4n}\sum_{k=1}^{n} f(M_k) \label{1999-1:eq:6}
\end{align}
$$

  を得る．両辺の$n\to\infty$での極限値は，区分求積法によって求まる．
  
$$
\begin{align*}
\lim_{n\to\infty}\frac{\pi}{4n}\sum_{k=1}^{n} f(m_k) = \frac{1}{2}\int_0^{\pi/2} f(x) \, dx = \frac{1}{2}\log\left(1+\frac{\pi}{2}\right)\\\lim_{n\to\infty}\frac{\pi}{4n}\sum_{k=1}^{n} f(M_k) = \frac{1}{2}\int_0^{\pi/2} f(x) \, dx =  \frac{1}{2}\log\left(1+\frac{\pi}{2}\right)
\end{align*}
$$

  この時のポイントは，区間$\left[ \frac{k-1}{2n}\pi, \frac{k}{2n}\pi \right]$の幅が$n\to\infty$で$0$に収束するから，
  $m_k$も$M_k$も区分求積の時の変数と同一視できることである．

  したがって，$\eqref{1999-1:eq:6}$および挟み撃ちの定理から，
  
$$
\begin{align*}
\lim_{n\to\infty} F_n = \frac{1}{2}\log\left(1+\frac{\pi}{2}\right)
\end{align*}
$$

  となる．

  この方法は汎用的にいろいろな問題に使える．また，この解法だと，問題の本質がわかりやすい．結局のところ，因子$\sin^2 nx$をかけて積分すると，もとの関数$f(x)$の積分を半分にする効果がある，ということだ．もとの解答ではこの$1/2$の因子が半角公式によって出てきていたことがわかるだろう．