---
university: "ukyoto"
category: "zenki"
year: "1964"
question: "6"
type: "solution"
title: "UKYOTO 1964 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

[解] $-\frac{\pi}{2} \leqq x \leqq \frac{\pi}{2}$ で考える。以下 $C = \cos t, S = \sin t$ とする。

まずAについて、面積が最大になるのは、明らかに4頂点が $(\pm t, 0), (\pm t, \cos t)$ で与えられる時で ($0 < t < \pi/2$) この時

$$
\begin{align*}
A = 2t C \quad (0 < t < \pi/2)
\end{align*}
$$

である。

$$
\begin{align*}
\frac{dA}{dt} = 2(C - t S) = 2C (1 - t \tan t)
\end{align*}
$$

より、下表をとる。($t_0$ は $t_0 \tan t_0 = 1$ を満たす)

| $t$  |  0  |  $\cdots$  | $t_0$ |  $\cdots$  | $\pi/2$ |
|:------:|:---:|:------------:|:-------:|:------------:|:---------:|
| $A'$ |     |    $+$     |    0    |    $-$     |           |
| $A$  |     | $\nearrow$ |         | $\searrow$ |           |

$\left( \frac{\pi}{4} \cdot \tan \frac{\pi}{4} < 1 \text{ より } \frac{\pi}{4} < t_0 \text{ である。} \quad \cdots (*) \right)$

したがって

$$
\begin{align*}
A = 2 t_0 \cos t_0 = 2 \frac{\cos^2 t_0}{\sin t_0} \quad \cdots \text{①}
\end{align*}
$$

となる。

次にBについて、$C'' = -\cos t \leqq 0 \ (-\frac{\pi}{2} \leqq t \leqq \frac{\pi}{2})$ より $y=\cos x$ のグラフは上に凸なので、Bは3頂点が $(\pm \pi/2, 0), (1, 0)$ の時の $\triangle$ の面積で、

$$
\begin{align*}
B = \frac{1}{2}\pi \quad \cdots \text{②}
\end{align*}
$$

最後にCについて、中心は原点である。半径 $r$ とすると、対称性から $0 \leqq t \leqq \pi/2$ で

$$
\begin{align*}
t^2 + \cos^2 t \geqq r^2 \quad \cdots \text{③}
\end{align*}
$$

となれば良い。この左辺を $f(t)$ とする。

$$
\begin{align*}
f'(t) = 2t - 2C \cdot S = 2t - \sin 2t \geqq 0 \quad (\because 0 \leqq t \leqq \pi/2 \text{ で } t \geqq \sin t)
\end{align*}
$$

より、$f$ は単調増加だから、③を満たす $\max r$ は $r = \sqrt{0 + \cos 0} = 1$ となり、

$$
\begin{align*}
C = \frac{1}{2} \cdot 1^2 \cdot \pi = \frac{1}{2}\pi \quad \cdots \text{④}
\end{align*}
$$

である。

以上これらの大小を比べる。(*)及び①からAが区間内で単調減少であることから

$$
\begin{align*}
A < 2 \frac{\cos^2 \frac{\pi}{4}}{\sin \frac{\pi}{4}} = \sqrt{2} < \frac{1}{2}\pi \quad (\because 8 < \pi^2 \text{ より } 2\sqrt{2} < \pi)
\end{align*}
$$

だから②, ④とあわせて

$$
\begin{align*}
A < B = C \quad (\cdots \text{以下、原稿がここで途切れている})
\end{align*}
$$